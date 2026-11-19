# review contact sheets: python3 sheet11.py <video.mp4> <out_prefix> [step_s=1.5] [per_sheet=48]
import sys, subprocess, os, math, tempfile, glob
from PIL import Image, ImageDraw
v, pre = sys.argv[1], sys.argv[2]; step = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5; per = int(sys.argv[4]) if len(sys.argv) > 4 else 48
td = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", v, "-vf", f"fps=1/{step},scale=320:180", f"{td}/f%05d.jpg"], check=True)
fs = sorted(glob.glob(f"{td}/f*.jpg")); cols = 6
for s in range(0, len(fs), per):
    chunk = fs[s:s+per]; rows = math.ceil(len(chunk) / cols); sh = Image.new("RGB", (cols*320, rows*180)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(chunk):
        t = (s + k) * step + step / 2; x, y = (k % cols)*320, (k // cols)*180
        sh.paste(Image.open(f), (x, y)); d.text((x+4, y+166), f"{int(t//60)}:{t%60:04.1f}", fill=(255, 255, 0))
    sh.save(f"{pre}{s//per:02d}.jpg", quality=80)
print(len(fs), "frames", math.ceil(len(fs)/per), "sheets")
