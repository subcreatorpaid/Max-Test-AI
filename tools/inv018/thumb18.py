# INV-018 thumbnail draft, Iran series rule (plan 26 Nov): flag + ONE hero object + 1-2 words, no map, no sentence bar.
# Layout = style v2 (flag top-left, hero left third in front of it, white word + golden brush bar bottom-right).
# The mine here is DRAWN as a stand-in; swap in the Gemini hero photo (upload/INV-018-gemini-hero-prompt.md).
import sys, math, pathlib, random
ROOT = pathlib.Path('/mnt/project-files/the-history-invoice'); sys.path.insert(0, str(ROOT/'scripts')); sys.path.insert(0, str(ROOT/'scripts/storyboard2'))
import thumb_v2 as TV
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops, ImageFont
W, H = TV.W, TV.H
OUT = sys.argv[1] if len(sys.argv) > 1 else 'INV-018-thumb-draft.jpg'
TOP, BAN = (sys.argv[2] if len(sys.argv) > 2 else 'HORMUZ'), (sys.argv[3] if len(sys.argv) > 3 else 'MINED?')
# ---- background: cold teal sea at dusk, warm horizon glow
y = np.linspace(0, 1, H)[:, None, None]; x = np.linspace(0, 1, W)[None, :, None]
sky = np.array([18, 34, 44]) * (1 - y) + np.array([6, 14, 20]) * y
glow = np.exp(-((x - 0.78) ** 2 / 0.08 + (y - 0.52) ** 2 / 0.01)) * np.array([120, 60, 20])
bg = np.clip(sky + glow + np.zeros((H, W, 3)), 0, 255).astype(np.uint8); canvas = Image.fromarray(bg)
d = ImageDraw.Draw(canvas); rnd = random.Random(3)
for i in range(260):   # water glints
    yy = int(H * (0.56 + rnd.random() * 0.44)); xx = rnd.random() * W; L = 20 + rnd.random() * 80
    d.line([(xx, yy), (xx + L, yy)], fill=(40 + int(60 * rnd.random()), 70, 80), width=2)
# ---- flag top-left
wv, wm = TV.fabric(TV.flag_img('ir', 980, 560)); wv = ImageEnhance.Brightness(wv).enhance(1.25)
bl = wv.filter(ImageFilter.GaussianBlur(14)); gm = Image.linear_gradient('L').rotate(90).resize(wv.size).point(lambda v: int(255 * max(0, v / 255 - 0.35) / 0.65)); wv = Image.composite(bl, wv, gm)
fade = Image.new('L', wm.size, 255); fd = ImageDraw.Draw(fade)
for xx in range(int(980 * 0.7), wm.size[0]): fd.line([(xx, 0), (xx, wm.size[1])], fill=int(255 * max(0, 1 - (xx - 980 * 0.7) / (980 * 0.3)) ** 1.3))
wm = ImageChops.multiply(wm, fade); wv = wv.rotate(3, resample=Image.BICUBIC); wm = wm.rotate(3, resample=Image.BICUBIC)
canvas.paste(wv, (-70, -90), wm)
# ---- hero: a horned naval mine (stand-in drawing), warm light from the left
R = 300; cx, cy = 560, 600; hero = Image.new('RGBA', (W, H), (0, 0, 0, 0)); hd = ImageDraw.Draw(hero)
for k in range(8):
    a = -math.pi / 2 + k * math.pi / 4 + 0.2
    if math.sin(a) > 0.75: continue
    x1, y1 = cx + R * 0.92 * math.cos(a), cy + R * 0.92 * math.sin(a); x2, y2 = cx + (R + 70) * math.cos(a), cy + (R + 70) * math.sin(a)
    hd.line([(x1, y1), (x2, y2)], fill=(70, 66, 60, 255), width=34); hd.ellipse([x2 - 26, y2 - 26, x2 + 26, y2 + 26], fill=(95, 88, 78, 255))
yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2); inside = r < R
nx, ny = (xx - cx) / R, (yy - cy) / R; nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0, 1))
lam = np.clip(-0.75 * nx - 0.35 * ny + 0.55 * nz, 0, 1); rim = np.clip(0.9 * nx - 0.1 * ny, 0, 1) ** 3
col = np.stack([28 + 150 * lam + 20 * rim, 30 + 105 * lam + 60 * rim, 32 + 70 * lam + 85 * rim], -1)
noise = np.random.default_rng(1).normal(0, 7, (H, W, 1)); col = np.clip(col + noise, 0, 255)
sph = np.zeros((H, W, 4), np.uint8); sph[..., :3] = col.astype(np.uint8); sph[..., 3] = (inside * 255).astype(np.uint8)
hero = Image.alpha_composite(hero, Image.fromarray(sph)); hd = ImageDraw.Draw(hero)
hd.arc([cx - R, cy - R * 0.22, cx + R, cy + R * 0.22], 0, 180, fill=(20, 20, 20, 220), width=7)
for k in range(9):
    a = -math.pi / 2 + k * math.pi / 4 - 0.4
    if math.sin(a) > 0.6: continue
    bx, by = cx + R * 0.97 * math.cos(a), cy + R * 0.97 * math.sin(a); hd.ellipse([bx - 9, by - 9, bx + 9, by + 9], fill=(28, 26, 24, 255))
hero = hero.filter(ImageFilter.UnsharpMask(radius=2, percent=80))
sh = Image.new('L', (W, H), 0); sh.paste(hero.split()[3], (14, 20)); canvas.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(24)).point(lambda v: int(v * 0.6)))
canvas.paste(hero, (0, 0), hero)
# ---- banner + big white word (same code path as thumb_v2)
d = ImageDraw.Draw(canvas); bh = 240; fb = ImageFont.truetype(TV.BEBAS, 240)
while d.textlength(BAN, font=fb) > W * 0.42: fb = ImageFont.truetype(TV.BEBAS, fb.size - 6)
bw = int(max(d.textlength(BAN, font=fb) + 260, W * 0.44)); bx1 = W - 28; bx0 = bx1 - bw; by0 = 722; by1 = by0 + bh
tpl = Image.open(ROOT / 'docs/reference/thumbnails/banner-template.png').convert('RGBA').resize((bw, bh), Image.LANCZOS)
sh = Image.new('L', (W, H), 0); sh.paste(tpl.split()[3], (bx0 + 12, by0 + 16)); canvas.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.6)))
canvas.paste(tpl, (bx0, by0), tpl)
tl = Image.new('L', (W, H), 0); dt = ImageDraw.Draw(tl); bb = dt.textbbox((0, 0), BAN, font=fb, stroke_width=4)
TX = bx0 + (bw - (bb[2] - bb[0])) / 2 - bb[0] + 14; TY = by0 + (bh - (bb[3] - bb[1])) / 2 - bb[1]
dt.text((TX, TY), BAN, font=fb, fill=255, stroke_width=4, stroke_fill=255)
cyy = TY + (bb[1] + bb[3]) / 2; tl = tl.transform((W, H), Image.AFFINE, (1, 0.2, -0.2 * cyy, 0, 1, 0), resample=Image.BICUBIC)
canvas.paste((8, 6, 4), (0, 0), tl)
sz = 300
while d.textlength(TOP, font=TV.F(sz)) > W * 0.46: sz -= 6
ft = TV.F(sz); bb = d.textbbox((0, 0), TOP, font=ft); tw = bb[2] - bb[0]
x0 = int(bx0 + (bw - tw) / 2 - bb[0]); y0 = by0 - 22 - bb[3]
sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).text((x0 + 8, y0 + 12), TOP, font=ft, fill=255)
canvas.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(20)).point(lambda v: min(255, v * 2)))
ImageDraw.Draw(canvas).text((x0, y0), TOP, font=ft, fill=(255, 255, 255))
canvas = canvas.filter(ImageFilter.UnsharpMask(radius=40, percent=22, threshold=0)).filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
canvas.resize((1280, 720), Image.LANCZOS).save(OUT, quality=93); print(OUT)
