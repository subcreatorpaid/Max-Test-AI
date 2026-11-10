# INV-007 part worker: python3 render_part7.py <PART> <vo_dir> <out_dir> <stills_dir> <clips_dir>
# Each script row becomes the shot from the approved storyboard (v1f): graphics from scripts/storyboard2 (kit, kit2, spec7),
# matched video clips (clips_dir/picks.json -> <code>.mp4) and matched photos (stills_dir/<code>.jpg, Ken Burns).
# Look rules: docs/look-rules.md (30% shadow, colour by intensity, colour 20% darker, beige paper, one background, no particles).
import sys, os, json, subprocess, pathlib, runpy
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path[:0] = [str(ROOT/"scripts/storyboard2"), str(HERE)]
import kit, kit2, spec7, visuals_v2
from PIL import Image, ImageDraw, ImageFilter
PART, VOD, OUT, STILLS, CLIPS = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4]), pathlib.Path(sys.argv[5])
OUT.mkdir(parents=True, exist_ok=True); TMP = OUT/f"tmp-{PART}"; TMP.mkdir(exist_ok=True)
spec7.ST = str(STILLS)
FPS = 25; XF = 0.5; PW, PH = 1920, 1080
R = runpy.run_path(str(HERE/"script_v2.py"))["R"]; ROW = {r[0]: r for r in R}; V = visuals_v2.V
SG = json.load(open(VOD/"segs7.json"))["segs"][PART]

# ---- capture footage() arguments from the storyboard spec (photo, labels, tag) ----
CAP = {}
def _cap(photo, title="", sub="", glow=None, t="", src="", mode="warm", corner=""):
    return dict(photo=photo, title=title, sub=sub, glow=glow, t=t, src=src, corner=corner)
def foot_args(code):
    if code not in CAP:
        old = spec7.footage; spec7.footage = _cap
        try: CAP[code] = spec7.SPEC[code]()
        finally: spec7.footage = old
        if not isinstance(CAP[code], dict): CAP[code] = None
    return CAP[code]
def dur_of(f):
    try: return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",str(f)]).decode().strip())
    except Exception: return 0.0
def photo_of(code):
    a = foot_args(code)
    p = pathlib.Path(a["photo"]) if a and a.get("photo") else STILLS/f"{code}.jpg"
    return p if p.exists() else None
def clip_of(code):
    p = CLIPS/f"{code}.mp4"
    return p if p.exists() else None

# ---- plan ----
starts = SG["starts"]; total = SG["dur"]; plan = []
for i, (code, st) in enumerate(starts):
    en = starts[i+1][1] if i+1 < len(starts) else total
    if i == 0: st = 0.0
    d = en - st; kind = V[code][0]
    if kind == "G": plan.append(("gfx", code, d)); continue
    clip, ph = clip_of(code), photo_of(code)
    if kind == "F" and clip:
        cl = dur_of(clip) - 0.6
        if d <= cl or not ph: plan.append(("clip", code, d))
        else:
            a = max(4.0, min(cl, d*0.6)); plan.append(("clip", code, a)); plan.append(("photo", code, d-a))
    elif ph: plan.append(("photo", code, d))
    else: plan.append(("gfx", code, d))
if PART == "RC": plan.append(("end", "RC-11", 6.0))
acc = 0.0; fr = []
for p in plan:
    a = round(acc*FPS); acc += p[2]; b = round(acc*FPS); fr.append(b-a)

# ---- pictures ----
def up(im):  # kit renders at 1280x720; upscale cleanly to 1080p
    return im.convert("RGB").resize((PW, PH), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 60, 2))
def overlay_png(code, path):
    a = foot_args(code) or {}; im = Image.new("RGBA", (kit.W, kit.H), (0,0,0,0))
    if a.get("title"):  # same paper lower-third as kit.lower, kept transparent
        title, sub = a["title"], a.get("sub",""); d = ImageDraw.Draw(im); ft = kit.F(28,"xb"); fs = kit.F(22,"s")
        w = int(max(d.textlength(title.upper(), font=ft), d.textlength(sub, font=fs) if sub else 0)) + 44; h = 88 if sub else 58
        p = kit.paper_rect((w,h), kit.PAPER, True, len(title)); pd = ImageDraw.Draw(p); pd.text((20,12), title.upper(), font=ft, fill=(30,26,22))
        if sub: pd.text((20,48), sub, font=fs, fill=kit.ORANGE)
        sh = Image.new("RGBA", im.size, (0,0,0,0)); ImageDraw.Draw(sh).rectangle([70, kit.H-h-56, 70+w, kit.H-56], fill=(0,0,0,150))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(14))); im.paste(p, (60, kit.H-h-70), p)
    if a.get("t"): kit.tag(im, a["t"], a.get("src",""))
    if a.get("corner"):
        f = kit.F(110, "b"); d = ImageDraw.Draw(im); w = d.textlength(a["corner"], font=f)
        sh = Image.new("RGBA", im.size, (0,0,0,0)); ImageDraw.Draw(sh).text((kit.W-w-70+4, 104), a["corner"], font=f, fill=(0,0,0,200))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(6))); ImageDraw.Draw(im).text((kit.W-w-70, 100), a["corner"], font=f, fill=kit.PAPER)
    im.resize((PW, PH), Image.LANCZOS).save(path)
def graded_photo(code, path):
    a = foot_args(code) or {}; kit.CUR[0] = code
    W0, H0 = kit.W, kit.H; kit.W, kit.H = 2400, 1350
    try:
        g = a.get("glow"); g = (int(g[0]*2400/W0), int(g[1]*1350/H0)) if g else None
        kit.tone(Image.open(photo_of(code)), g).save(path, quality=93)
    finally: kit.W, kit.H = W0, H0
GRADE_VF = {"shadow": "eq=saturation=0.12:contrast=1.2:brightness=-0.10:gamma=0.82,colorbalance=bs=0.05:bm=0.03,vignette=PI/3.6",
            "low":    "eq=saturation=0.80:contrast=1.0:brightness=-0.05:gamma=0.86,colorbalance=bs=0.04",
            "mid":    "eq=saturation=0.90:contrast=1.05:brightness=-0.05:gamma=0.85,colorbalance=bs=0.03",
            "high":   "eq=saturation=1.15:contrast=1.12:brightness=-0.04:gamma=0.86,colorbalance=rs=0.04:rm=0.02"}
ENC = ["-c:v","libx264","-crf","16","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS)]
def ff(args): subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y"]+args, check=True)
def render(k):
    kind, code, _ = plan[k]; n = fr[k] + (int(XF*FPS) if k < len(plan)-1 else 0); dur = n/FPS
    out = TMP/f"{k:03d}.mp4"
    if out.exists(): return str(out)
    if kind in ("gfx", "end"):
        png = TMP/f"{k:03d}.png"
        im = kit.endcard() if kind == "end" else spec7.SPEC[code]()
        up(im).save(png)
        z = 0.02 if kind == "end" else 0.035
        ff(["-loop","1","-i",str(png),"-vf",f"scale=3840:2160,zoompan=z='1+{z}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={PW}x{PH}:fps={FPS},format=yuv420p","-frames:v",str(n)]+ENC+[str(out)])
        return str(out)
    g = kit.GRADE.get(code, "mid"); png = TMP/f"{k:03d}.png"; overlay_png(code, png)
    if kind == "clip":
        vf = (f"[0:v]scale={PW+96}:{PH+54}:force_original_aspect_ratio=increase,crop={PW+96}:{PH+54},crop={PW}:{PH}:x='48+40*sin(t/{dur:.2f})':y='27',"
              f"{GRADE_VF[g]},fps={FPS},format=yuv420p[v];[1:v]format=rgba,fade=in:st=0.4:d=0.6:alpha=1[o];[v][o]overlay=0:0")
        ff(["-stream_loop","-1","-i",str(clip_of(code)),"-loop","1","-i",str(png),"-filter_complex",vf,"-frames:v",str(n),"-an"]+ENC+[str(out)])
        return str(out)
    jpg = TMP/f"{k:03d}.jpg"; graded_photo(code, jpg)
    dr = k % 4
    zexpr = {0: f"1.0+0.09*on/{n}", 1: f"1.09-0.09*on/{n}", 2: "1.07", 3: "1.07"}[dr]
    xexpr = {0: "iw/2-(iw/zoom/2)", 1: "iw/2-(iw/zoom/2)", 2: f"(iw-iw/zoom)*on/{n}", 3: f"(iw-iw/zoom)*(1-on/{n})"}[dr]
    vf = (f"[0:v]scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='{zexpr}':x='{xexpr}':y='ih/2-(ih/zoom/2)':d={n}:s={PW}x{PH}:fps={FPS},format=yuv420p[v];"
          f"[1:v]format=rgba,fade=in:st=0.4:d=0.6:alpha=1[o];[v][o]overlay=0:0")
    ff(["-loop","1","-i",str(jpg),"-loop","1","-i",str(png),"-filter_complex",vf,"-frames:v",str(n),"-an"]+ENC+[str(out)])
    return str(out)

def is_part_card(code): return code.endswith("-01") and code[0] in "PR" and V[code][0] == "G"
if __name__ == "__main__":
    with Pool(int(os.environ.get("WORKERS", "4"))) as pool: segs = list(pool.imap(render, range(len(plan))))
    TR = ["fade", "dissolve", "fade", "smoothleft", "fade", "dissolve", "fade", "smoothright"]
    inputs = []; [inputs.extend(["-i", s]) for s in segs]
    fc = []; last = "[0:v]"; off = 0.0
    for k in range(1, len(segs)):
        off += fr[k-1]/FPS
        tr = "fadeblack" if (is_part_card(plan[k][1]) and plan[k][1] != plan[k-1][1]) or plan[k][0] == "end" else TR[k % len(TR)]
        if plan[k][1] == plan[k-1][1]: tr = "dissolve"
        lab = f"[x{k}]"; fc.append(f"{last}[{k}:v]xfade=transition={tr}:duration={XF}:offset={off:.3f}{lab}"); last = lab
    fc.append(f"{last}noise=alls=5:allf=t,format=yuv420p[vout]")
    final = OUT/f"{PART}.mp4"
    subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y"]+inputs+["-filter_complex",";".join(fc),"-map","[vout]","-frames:v",str(sum(fr)),
        "-c:v","libx264","-crf","23","-maxrate","12M","-bufsize","24M","-preset","medium","-g","50","-pix_fmt","yuv420p","-r",str(FPS),str(final)], check=True)
    t = 0.0; log = []
    for k, p in enumerate(plan):
        row = ROW[p[1]]; log.append({"code": p[1], "kind": p[0], "t": round(t,3), "dur": round(fr[k]/FPS,3), "visual": row[3][:60], "sfx": row[6] if p[0] != "end" else ""}); t += fr[k]/FPS
    json.dump({"part": PART, "dur": sum(fr)/FPS, "vo_dur": total, "shots": log}, open(OUT/f"{PART}-shots.json","w"), indent=1)
    tot = sum(fr); share = {x: sum(fr[k] for k, p in enumerate(plan) if p[0] in x) for x in (("gfx","end"), ("clip",), ("photo",))}
    print(PART, "done", f"{tot/FPS:.1f}s", "graphics/video/photos %", [round(100*v/tot) for v in share.values()])
