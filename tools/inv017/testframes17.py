# Contact sheet of every graphic at 3 moments (start+0.5, after cue, end-0.5). INV_S=0.5. usage: python3 testframes17.py vo_dir out_dir [codes...]
import sys, os, json, runpy, pathlib, traceback
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import spec17, anim12 as A
from PIL import Image, ImageDraw
R = runpy.run_path(str(HERE/"script_v1.py"))["R"]; ROW = {r[0]: r for r in R}
VOD, OUT = sys.argv[1], pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True); want = sys.argv[3:]
sg = json.load(open(os.path.join(VOD, "segs17.json")))["segs"]
sheets = []; errs = []
for p, S in sg.items():
    st = S["starts"]
    for i, (code, t0) in enumerate(st):
        if want and code not in want: continue
        t1 = st[i+1][1] if i+1 < len(st) else S["dur"]; dur = t1 - t0
        cues = [x - t0 for x in S["cues"].get(code, [])]; sents = [a - t0 for a, b in S["sents"].get(code, [])]
        A.DUR = dur; A.CUES = cues; A.SENTS = sents or [0.0]
        ts = [0.6, (cues[0] + 1.2) if cues else dur*0.5, dur - 0.3]
        ims = []
        for tt in ts:
            A.T = tt
            try:
                im = spec17.SPEC[code](ROW[code][4], ROW[code][5]) if code in spec17.SPEC else A.card([ROW[code][4]], tag=ROW[code][5])
            except Exception as e:
                errs.append((code, repr(e))); traceback.print_exc(); im = Image.new("RGB", (A.PW, A.PH), (255, 0, 0))
            ims.append(im.convert("RGB"))
        row = Image.new("RGB", (A.PW*3 + 20, A.PH + 24), (40, 40, 40))
        for j, im in enumerate(ims): row.paste(im, (j*(A.PW + 10), 24))
        ImageDraw.Draw(row).text((6, 4), f"{code}  {dur:.1f}s  cues {[round(x,1) for x in cues]}", fill=(255, 255, 0))
        sheets.append(row)
for k in range(0, len(sheets), 8):
    grp = sheets[k:k+8]; sh = Image.new("RGB", (grp[0].width, sum(g.height for g in grp)), (0, 0, 0)); y = 0
    for g in grp: sh.paste(g, (0, y)); y += g.height
    sh.save(OUT / f"sheet{k//8:02d}.jpg", quality=80)
print("errors", errs)
