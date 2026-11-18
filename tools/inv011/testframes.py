# contact sheet of graphic frames: python3 testframes.py out.jpg CODE...  (uses segs11.json for cue times)
import os, sys, json, runpy, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import anim11 as A, spec11
from PIL import Image, ImageDraw
SG = json.load(open(os.environ.get("SEGS", "/tmp/claude-0/inv011/vo/segs11.json")))["segs"]
R = runpy.run_path("script_v1.py")["R"]; ROW = {r[0]: r for r in R}
out = sys.argv[1]; codes = sys.argv[2:]; tiles = []
for code in codes:
    p = code.split("-")[0]; s = SG.get(p); starts = dict((c_, t) for c_, t in s["starts"]) if s else {}
    keys = [c_ for c_, _ in s["starts"]] if s else []; i = keys.index(code) if code in keys else -1
    st = starts.get(code, 0); en = (s["starts"][i+1][1] if i+1 < len(keys) else s["dur"]) if s else 8
    A.CUES = [t - st for t in s["cues"].get(code, [])] if s else []; A.SENTS = [a - st for a, b in s["sents"].get(code, [])] if s else [0]
    A.DUR = en - st; times = [0.4, (A.CUES[0] + 0.6) if A.CUES else A.DUR*0.4, A.DUR - 0.5]
    for t in times:
        A.T = t; t0 = time.time(); im = spec11.SPEC[code](ROW[code][4], ROW[code][5]).convert("RGB")
        dt = time.time() - t0; im = im.resize((480, 270)); ImageDraw.Draw(im).text((6, 4), f"{code} t={t:.1f} {dt*1000:.0f}ms", fill=(255, 255, 0)); tiles.append(im)
cols = 3; sheet = Image.new("RGB", (480*cols, 270*math.ceil(len(tiles)/cols)))
for k, im in enumerate(tiles): sheet.paste(im, ((k % cols)*480, (k // cols)*270))
sheet.save(out, quality=85); print("ok", len(tiles))
