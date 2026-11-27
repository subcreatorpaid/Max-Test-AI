# INV-024 part renderer (copy of render17 + typing on every caption): python3 render18.py <PART> <vo_dir> <out_dir> <clips_dir> <stills_dir>
# env INV_S=0.5 -> 640x360 review, INV_S=1.5 -> 1080p final. WORKERS=4.
# Each script row -> shots from visuals_v1.V. Graphics are drawn frame by frame (anim12) with the row's {cue} word times and
# sentence starts, so every hit lands on the narrator's word. Footage: matched clip / photo, graded per look-rules, lower-third + tag.
import sys, os, json, subprocess, pathlib, runpy, math, hashlib
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "inv012")); sys.path.insert(0, str(HERE.parent / "inv017")); sys.path.insert(0, str(HERE.parent / "inv018")); sys.path.insert(0, str(HERE.parent / "inv019"))
import anim12 as A, spec24 as spec12, typing18
from PIL import Image, ImageDraw, ImageFilter
PART, VOD, OUT, CLIPS, STILLS = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4]), pathlib.Path(sys.argv[5])
OUT.mkdir(parents=True, exist_ok=True); TMP = OUT / f"tmp-{PART}-{A.PW}"; TMP.mkdir(exist_ok=True)
FPS = 25; XF = 0.4; PW, PH = A.PW, A.PH
_S = runpy.run_path(str(HERE / "script_v1.py")); R = _S["R"]; ROW = {r[0]: r for r in R}
V = runpy.run_path(str(HERE / "visuals_v1.py"))["V"]
SG = json.load(open(VOD / "segs24.json"))["segs"][PART]
# corner invoice: one line printed at the end of each part (rulebook 5)
CORNER_LINES = _S["CORNER"]
# real 1962 archive photos (public domain): framed on a blurred copy, tagged as archive, not stock
ARCH = {}
ORDER = ["CO", "P1", "BR", "P2", "P3", "P4", "P5", "P6", "RC"]
prev = [CORNER_LINES[p] for p in ORDER[:ORDER.index(PART)] if p in CORNER_LINES]
GRADE = {}  # code -> shadow / low / mid / high from the visual note
for r in R:
    v = r[3].upper(); GRADE[r[0]] = "shadow" if "SHADOW" in v else "high" if "INTENSE" in v else "low" if "CALM" in v else "mid"
GRADE_VF = {"shadow": "eq=saturation=0.15:contrast=1.18:brightness=-0.10:gamma=0.84,colorbalance=bs=0.05:bm=0.03",
            "low":    "eq=saturation=0.80:contrast=1.0:brightness=-0.06:gamma=0.88,colorbalance=bs=0.04",
            "mid":    "eq=saturation=0.90:contrast=1.05:brightness=-0.06:gamma=0.86,colorbalance=bs=0.03",
            "high":   "eq=saturation=1.10:contrast=1.12:brightness=-0.05:gamma=0.86,colorbalance=rs=0.04:rm=0.02"}

def asset(code, i, kind):
    name = code + ("x" if (i > 0 or V[code][0][0] == "G") else "")
    p = (CLIPS / f"{name}.mp4") if kind == "F" else (STILLS / f"{name}.jpg")
    if kind == "F" and not p.exists():   # fall back to a photo of the same name, then nothing
        q = STILLS / f"{name}.jpg"; return ("S", q) if q.exists() else (None, None)
    if kind == "S" and not p.exists():
        q = CLIPS / f"{name}.mp4"; return ("F", q) if q.exists() else (None, None)
    return kind, p

# ---------------- plan ----------------
starts = SG["starts"]; total = SG["dur"]; plan = []   # (kind, code, dur, info)
for i, (code, st) in enumerate(starts):
    en = starts[i+1][1] if i+1 < len(starts) else total
    st0 = 0.0 if i == 0 else st; d = en - st0
    cues = [t - st0 for t in SG["cues"].get(code, [])]; sents = [a - st0 for a, b in SG["sents"].get(code, [])]
    shots = V[code]; foot = [(j, s) for j, s in enumerate(shots) if s[0] != "G"]
    resolved = []
    for j, s in foot:
        k_, p = asset(code, j, s[0])
        if k_: resolved.append((k_, p))
    has_g = shots[0][0] == "G"
    late = bool(cues) and cues[-1] + 2.2 > d - 3.0   # the hit lands too late for a cutaway: keep the graphic
    if has_g and resolved and d > 5.5 and not late:
        last = max(cues + [sents[-1] if sents else 0.0])
        g = min(d - 3.0, max(d * 0.5, (cues[-1] + 2.2) if cues else d * 0.55, 4.0))
        plan.append(("gfx", code, g, {"cues": cues, "sents": sents, "off": 0.0}))
        k_, p = resolved[0]; plan.append(("clip" if k_ == "F" else "photo", code, d - g, {"path": p, "off": g}))
    elif has_g and resolved and late and d > 5.5 and cues and min(cues[0] - 2.0, d - 3.0) >= 2.5:
        # the hit is on the last word: show the matched footage first, then bring the graphic in fresh for the hit
        g = min(cues[0] - 2.0, d - 3.0)
        k_, p = resolved[0]; plan.append(("clip" if k_ == "F" else "photo", code, g, {"path": p, "off": 0.0}))
        plan.append(("gfx", code, d - g, {"cues": [x - g for x in cues], "sents": [max(0.0, x - g) for x in sents], "off": 0.0}))
    elif has_g or not resolved:
        plan.append(("gfx", code, d, {"cues": cues, "sents": sents, "off": 0.0, "fallback": not has_g}))
    else:
        k_, p = resolved[0]; plan.append(("clip" if k_ == "F" else "photo", code, d, {"path": p, "off": 0.0}))
acc = 0.0; fr = []
for p in plan:
    a = round(acc * FPS); acc += p[2]; b = round(acc * FPS); fr.append(b - a)
LAST_CODE = starts[-1][0]

def is_part_card(code): return code.endswith("-01") and code[0] in "PW" and V[code][0][0] == "G"
def corner_lines(code, t_in_row, row_dur):
    if PART in ("RC",) or is_part_card(code): return None, None
    lines = list(prev)
    if code == LAST_CODE and PART in CORNER_LINES: return lines + [CORNER_LINES[PART]], max(0.0, row_dur - 2.5) - t_in_row
    return lines, None

# ---------------- graphics ----------------
def gfx_frame(code, info, t, dur):
    A.T = t + info["off"]; A.DUR = dur; A.CUES = info["cues"]; A.SENTS = info["sents"] or [0.0]
    row = ROW[code]
    if info.get("fallback") or code not in spec12.SPEC:
        im = A.card([row[4] or row[1][:60]], tag=row[5])
    else:
        im = spec12.SPEC[code](row[4], row[5])
    im = im.convert("RGB")
    lines, new_at = corner_lines(code, 0, dur)
    if lines:
        A.T = t
        with typing18.notype(): im = A.corner(im, lines, (t + (new_at or 0)) if new_at is not None else None)
    # camera: never parked: slow push + gentle drift (part cards push harder)
    z = 1.0 + (0.06 if is_part_card(code) else 0.035) * A.ease_io(t / max(dur, 1))
    dx = 6 * math.sin(t * 0.37 + hash(code) % 7) * A.S; dy = 4 * math.cos(t * 0.29) * A.S
    cw, ch = PW / z, PH / z; x0 = (PW - cw) / 2 + dx; y0 = (PH - ch) / 2 + dy
    x0 = max(0, min(PW - cw, x0)); y0 = max(0, min(PH - ch, y0))
    return im.resize((PW, PH), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))

ENC = ["-c:v", "libx264", "-crf", "17" if PW >= 1920 else "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]
def ff(args): subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y"] + args, check=True)
def dur_of(f):
    try: return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).decode().strip())
    except Exception: return 0.0

info_path = {}
def frame_archive(src, dst):
    im = Image.open(src).convert("RGB"); bg = im.resize((PW, PH)).filter(ImageFilter.GaussianBlur(int(40 * A.S)))
    bg = Image.eval(bg, lambda v: int(v * 0.45)); h = int(PH * 0.80); w = int(im.width * h / im.height)
    fr_ = Image.new("RGB", (w + int(16 * A.S), h + int(16 * A.S)), A.PAPER); fr_.paste(im.resize((w, h), Image.LANCZOS), (int(8 * A.S), int(8 * A.S)))
    bg.paste(fr_, ((PW - fr_.width) // 2, (PH - fr_.height) // 2 - int(20 * A.S))); bg.save(dst, quality=92); return dst

TCPS = typing18.CPS; LT0 = 0.55   # lower-third: box slides in at 0.3 s, letters type from 0.55 s
def overlay_png(code, path, show_text=True, t=None):
    """lower-third (paper, bottom-left) typing on + tag + corner invoice, transparent PNG at time t (None = finished)"""
    A.T = 10; A.DUR = 20; im = Image.new("RGBA", (PW, PH), (0, 0, 0, 0)); row = ROW[code]
    sh = Image.new("L", (PW, PH), 0); ImageDraw.Draw(sh).rectangle([0, int(PH * 0.62), int(PW * 0.7), PH], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(int(60 * A.S))); im.putalpha(sh)
    d = A.D(im); txt = (row[4] if show_text else "")[:60]
    with typing18.notype():
        if txt:
            fo = A.f(30, "inter"); w = d.tl(txt, fo) + 44; k = 1.0 if t is None else A.ease(max(0, min(1, (t - 0.3) / 0.25)))
            bw = min(w, A.W - 140) * k
            if k > 0:
                d.rect((60, A.H - 150, 60 + bw, A.H - 92), fill=A.PAPER + (240,))
                d.rect((60, A.H - 150, 68, A.H - 92), fill=A.ORANGE + (255,))
            n = len(txt) if t is None else max(0, int((t - LT0) * TCPS) + 1) if t >= LT0 else 0
            s_ = txt[:n]
            if s_: d.text((80, A.H - 140), s_, fo, (30, 26, 22, 255))
            if t is not None and 0 < n < len(txt) and int(t * 6) % 2 == 0:
                x = 80 + d.tl(s_, fo) + 3; d.rect((x, A.H - 134, x + 4, A.H - 106), fill=(30, 26, 22, 255))
        tg = ((row[5].upper() + " · ") if row[5] else "") + "ILLUSTRATIVE STOCK IMAGE"
        d.rect((40, A.H - 52, 46, A.H - 28), fill=A.ORANGE + (255,)); d.text((56, A.H - 50), tg[:120], A.f(18, "reg"), A.GREY + (255,))
        lines, _ = corner_lines(code, 0, 0)
        if lines: A.corner(im, lines, None)
    im.save(path)
    return len(txt)

def overlay_seq(code, k):
    """typed lower-third as a PNG sequence; ffmpeg holds the last frame (eof_action=repeat). Returns (pattern, events)."""
    dd = TMP / f"{k:03d}-ov"; dd.mkdir(exist_ok=True); n = len((ROW[code][4] or "")[:60])
    nf = int((LT0 + n / TCPS + 0.3) * FPS) + 2
    for j in range(nf): overlay_png(code, dd / f"{j:04d}.png", t=j / FPS)
    return str(dd / "%04d.png"), ([[LT0, round(max(0.12, n / TCPS), 3), n]] if n else [])

def render(k):
    kind, code, _, info = plan[k]; n = fr[k] + (int(XF * FPS) if k < len(plan) - 1 else 0); dur = n / FPS
    out = TMP / f"{k:03d}.mp4"; ev = TMP / f"{k:03d}.typing.json"
    if out.exists() and out.stat().st_size > 0 and ev.exists(): return str(out), json.load(open(ev))
    if kind == "gfx":
        typing18.reset()
        p = subprocess.Popen(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{PW}x{PH}", "-r", str(FPS), "-i", "-", "-an"] + ENC + [str(out) + ".t.mp4"], stdin=subprocess.PIPE)
        for j in range(n): p.stdin.write(gfx_frame(code, info, j / FPS, dur).tobytes())
        p.stdin.close(); p.wait(); os.rename(str(out) + ".t.mp4", out)
        evs = [e for e in typing18.EVENTS if e[0] < dur - 0.2]; json.dump(evs, open(ev, "w")); return str(out), evs
    png, evs = overlay_seq(code, k); g = GRADE_VF[GRADE[code]]
    if pathlib.Path(str(info["path"])).stem in ARCH:
        info = dict(info); info["path"] = frame_archive(info["path"], TMP / f"{k:03d}-arch.jpg"); g = "eq=contrast=1.02"
    if kind == "clip":
        cl = dur_of(info["path"]); slow = max(1.0, min(2.0, dur / max(0.5, cl - 0.3)))   # slow-mo if the clip is short (max 2x), else loop
        mv = int(hashlib.md5(code.encode()).hexdigest(), 16) % 3
        cx = {0: f"{int(48*A.S)}+{int(40*A.S)}*sin(t/{dur:.2f})", 1: f"{int(96*A.S)}*t/{dur:.2f}", 2: f"{int(96*A.S)}*(1-t/{dur:.2f})"}[mv]
        vf = (f"[0:v]setpts={slow:.3f}*PTS,scale={PW + int(96*A.S)}:{PH + int(54*A.S)}:force_original_aspect_ratio=increase,crop={PW + int(96*A.S)}:{PH + int(54*A.S)},"
              f"crop={PW}:{PH}:x='{cx}':y='{int(27*A.S)}',{g},fps={FPS},format=yuv420p[v];[1:v]format=rgba[o];[v][o]overlay=0:0:eof_action=repeat")
        ff(["-stream_loop", "-1", "-i", str(info["path"]), "-framerate", str(FPS), "-i", png, "-filter_complex", vf, "-frames:v", str(n), "-an"] + ENC + [str(out)])
        json.dump(evs, open(ev, "w")); return str(out), evs
    dr = k % 4
    zexpr = {0: f"1.0+0.09*on/{n}", 1: f"1.09-0.09*on/{n}", 2: "1.08", 3: "1.08"}[dr]
    xexpr = {0: "iw/2-(iw/zoom/2)", 1: "iw/2-(iw/zoom/2)", 2: f"(iw-iw/zoom)*on/{n}", 3: f"(iw-iw/zoom)*(1-on/{n})"}[dr]
    big = f"{PW*2}:{PH*2}"
    vf = (f"[0:v]scale={big}:force_original_aspect_ratio=increase,crop={big},zoompan=z='{zexpr}':x='{xexpr}':y='ih/2-(ih/zoom/2)':d={n}:s={PW}x{PH}:fps={FPS},{g},format=yuv420p[v];"
          f"[1:v]format=rgba[o];[v][o]overlay=0:0:eof_action=repeat")
    ff(["-loop", "1", "-i", str(info["path"]), "-framerate", str(FPS), "-i", png, "-filter_complex", vf, "-frames:v", str(n), "-an"] + ENC + [str(out)])
    json.dump(evs, open(ev, "w")); return str(out), evs

# transitions: Round Two flash + rotation (>= 6 kinds per act, no plain crossfade runs)
TR = ["fadewhite", "smoothleft", "hblur", "circleopen", "wiperight", "zoomin", "slideup", "radial", "smoothright", "dissolve"]
if __name__ == "__main__":
    with Pool(int(os.environ.get("WORKERS", "4"))) as pool: res = list(pool.imap(render, range(len(plan)))); segs = [r[0] for r in res]; TYP = [r[1] for r in res]
    inputs = []; [inputs.extend(["-i", s]) for s in segs]
    fc = []; last = "[0:v]"; off = 0.0; trs = []
    for k in range(1, len(segs)):
        off += fr[k-1] / FPS
        if is_part_card(plan[k][1]) and plan[k][1] != plan[k-1][1]: tr = "fadeblack"
        elif plan[k][1] == plan[k-1][1]: tr = "dissolve"          # graphic -> its own cutaway
        else: tr = TR[k % len(TR)]
        trs.append(tr); lab = f"[x{k}]"
        fc.append(f"{last}[{k}:v]xfade=transition={tr}:duration={XF}:offset={off:.3f}{lab}"); last = lab
    fc.append(f"{last}noise=alls=6:allf=t,vignette=PI/5,format=yuv420p[vout]")
    final = OUT / f"{PART}.mp4"
    crf = "23" if PW >= 1920 else "26"
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y"] + inputs + ["-filter_complex", ";".join(fc), "-map", "[vout]", "-frames:v", str(sum(fr)),
        "-c:v", "libx264", "-crf", crf, "-maxrate", "12M", "-bufsize", "24M", "-preset", "medium", "-g", "50", "-pix_fmt", "yuv420p", "-r", str(FPS), str(final)], check=True)
    t = 0.0; log = []
    for k, p in enumerate(plan):
        row = ROW[p[1]]; info = p[3]
        log.append({"code": p[1], "kind": p[0], "t": round(t, 3), "dur": round(fr[k] / FPS, 3), "off": info.get("off", 0.0),
                    "cues": [round(x - info.get("off", 0.0), 3) for x in info.get("cues", [])] if p[0] == "gfx" else [],
                    "sfx": row[6], "tr": trs[k-1] if k > 0 else "", "typing": TYP[k]})
        t += fr[k] / FPS
    json.dump({"part": PART, "dur": sum(fr) / FPS, "vo_dur": total, "shots": log}, open(OUT / f"{PART}-shots.json", "w"), indent=1)
    tot = sum(fr); share = [sum(fr[k] for k, p in enumerate(plan) if p[0] == x) for x in ("gfx", "clip", "photo")]
    print(PART, "done", f"{tot/FPS:.1f}s", "graphics/video/photos %", [round(100 * v / tot) for v in share], flush=True)
