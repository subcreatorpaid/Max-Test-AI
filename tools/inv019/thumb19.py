# INV-019/020 thumbnail drafts, Iran series rule (plan 26 Nov): flag + ONE hero object + 1-2 words, no map, no sentence bar.
# Layout = style v2 (flag top-left, hero left third in front of it, white word + golden brush bar bottom-right).
# The hero here is DRAWN as a stand-in; swap in the Gemini hero photo (upload/INV-0NN-gemini-hero-prompt.md).
import sys, math, pathlib, random
ROOT = pathlib.Path('/mnt/project-files/the-history-invoice'); sys.path.insert(0, str(ROOT/'scripts')); sys.path.insert(0, str(ROOT/'scripts/storyboard2'))
import thumb_v2 as TV
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops, ImageFont
W, H = TV.W, TV.H
OUT = sys.argv[1] if len(sys.argv) > 1 else 'INV-018-thumb-draft.jpg'
TOP, BAN, MODE = sys.argv[2], sys.argv[3], sys.argv[4]   # MODE: flag (white flag) | barrel (falling oil barrel) | lock (padlock) | atom (yellow drum + trefoil) | pump (1970s petrol pump)
FLAG = sys.argv[5] if len(sys.argv) > 5 else 'ir'
# ---- background: either the drawn sea, or the Gemini hero photo (MODE photo:<path>)
PHOTO = MODE.startswith('photo:')
if PHOTO:
    import json
    ph = Image.open(MODE[6:]).convert('RGB'); sc = max(W / ph.width, H / ph.height)
    ph = ph.resize((round(ph.width * sc), round(ph.height * sc)), Image.LANCZOS); ox, oy = (ph.width - W) // 2, (ph.height - H) // 2
    ph = ph.crop((ox, oy, ox + W, oy + H)); canvas = ph.copy()
    m = json.loads(sys.argv[6]); hm = Image.new('L', (W, H), 0); md = ImageDraw.Draw(hm)
    e = [v * sc for v in m['ellipse']]; md.ellipse([e[0] - ox, e[1] - oy, e[2] - ox, e[3] - oy], fill=255)
    for (x0, y0, x1, y1, wd) in m.get('lines', []): md.line([(x0 * sc - ox, y0 * sc - oy), (x1 * sc - ox, y1 * sc - oy)], fill=255, width=int(wd * sc))
    for (x0, y0, x1, y1) in m.get('rects', []): md.rectangle([x0 * sc - ox, y0 * sc - oy, x1 * sc - ox, y1 * sc - oy], fill=255)
    hm = hm.filter(ImageFilter.GaussianBlur(3))
    wv, wm = TV.fabric(TV.flag_img(FLAG, 980, 560)); wv = ImageEnhance.Brightness(wv).enhance(1.05)
    bl = wv.filter(ImageFilter.GaussianBlur(14)); gm = Image.linear_gradient('L').rotate(90).resize(wv.size).point(lambda v: int(255 * max(0, v / 255 - 0.35) / 0.65)); wv = Image.composite(bl, wv, gm)
    fade = Image.new('L', wm.size, 255); fd = ImageDraw.Draw(fade)
    for xx in range(int(980 * 0.6), wm.size[0]): fd.line([(xx, 0), (xx, wm.size[1])], fill=int(255 * max(0, 1 - (xx - 980 * 0.6) / (980 * 0.4)) ** 1.3))
    for yy in range(int(560 * 0.55), wm.size[1]): fd.line([(0, yy), (wm.size[0], yy)], fill=0)
    fade = fade.filter(ImageFilter.GaussianBlur(40))
    wm = ImageChops.multiply(wm, fade).point(lambda v: int(v * 0.85)); wv = wv.rotate(3, resample=Image.BICUBIC); wm = wm.rotate(3, resample=Image.BICUBIC)
    canvas.paste(wv, (-70, -90), wm); canvas.paste(ph, (0, 0), hm)
else:
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
    wv, wm = TV.fabric(TV.flag_img(FLAG, 980, 560)); wv = ImageEnhance.Brightness(wv).enhance(1.25)
    bl = wv.filter(ImageFilter.GaussianBlur(14)); gm = Image.linear_gradient('L').rotate(90).resize(wv.size).point(lambda v: int(255 * max(0, v / 255 - 0.35) / 0.65)); wv = Image.composite(bl, wv, gm)
    fade = Image.new('L', wm.size, 255); fd = ImageDraw.Draw(fade)
    for xx in range(int(980 * 0.7), wm.size[0]): fd.line([(xx, 0), (xx, wm.size[1])], fill=int(255 * max(0, 1 - (xx - 980 * 0.7) / (980 * 0.3)) ** 1.3))
    wm = ImageChops.multiply(wm, fade); wv = wv.rotate(3, resample=Image.BICUBIC); wm = wm.rotate(3, resample=Image.BICUBIC)
    canvas.paste(wv, (-70, -90), wm)
    # ---- hero (stand-in drawing), warm light from the left
    hero = Image.new('RGBA', (W, H), (0, 0, 0, 0)); hd = ImageDraw.Draw(hero)
    if MODE == 'flag':
        hd.rectangle([520, 250, 548, 1080], fill=(120, 96, 70, 255)); hd.ellipse([510, 228, 558, 276], fill=(200, 170, 90, 255))
        pts = []
        for i in range(0, 61):
            u = i / 60; pts.append((548 + 470 * u, 280 + 26 * math.sin(u * 6.0) + 40 * u))
        pts2 = [(x, y + 330 - 40 * ((x - 548) / 470)) for x, y in reversed(pts)]
        hd.polygon(pts + pts2, fill=(238, 236, 228, 255))
        for i in range(0, 60, 6):   # soft folds
            u = i / 60; x = 548 + 470 * u; hd.line([(x, 285 + 26 * math.sin(u * 6) + 40 * u), (x + 10, 600 - 20 * u)], fill=(222, 220, 212, 255), width=6)
    elif MODE == 'lock':
        hd.arc([400, 250, 720, 620], 180, 360, fill=(170, 170, 176, 255), width=56)
        hd.line([(428, 435), (428, 560)], fill=(170, 170, 176, 255), width=56); hd.line([(692, 435), (692, 560)], fill=(170, 170, 176, 255), width=56)
        hd.rounded_rectangle([330, 520, 790, 940], 40, fill=(200, 150, 60, 255)); hd.rounded_rectangle([350, 540, 770, 920], 30, outline=(150, 105, 35, 255), width=10)
        hd.ellipse([525, 640, 595, 710], fill=(30, 22, 16, 255)); hd.polygon([(545, 690), (575, 690), (590, 820), (530, 820)], fill=(30, 22, 16, 255))
    elif MODE == 'atom':
        hd.rounded_rectangle([340, 330, 780, 940], 30, fill=(214, 176, 40, 255))
        for yb in (450, 820): hd.rectangle([340, yb - 14, 780, yb + 14], fill=(150, 120, 20, 255))
        hd.ellipse([340, 290, 780, 370], fill=(236, 200, 60, 255)); cx, cy, r = 560, 635, 130
        hd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(20, 16, 10, 255)); hd.ellipse([cx - r + 14, cy - r + 14, cx + r - 14, cy + r - 14], fill=(214, 176, 40, 255))
        for a0 in (-120, 0, 120):
            hd.pieslice([cx - r + 24, cy - r + 24, cx + r - 24, cy + r - 24], a0 - 30, a0 + 30, fill=(20, 16, 10, 255))
        hd.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=(214, 176, 40, 255)); hd.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(20, 16, 10, 255))
    elif MODE == 'pump':
        hd.rounded_rectangle([380, 300, 740, 1000], 40, fill=(196, 60, 40, 255)); hd.rounded_rectangle([420, 360, 700, 560], 16, fill=(236, 226, 200, 255))
        for i, yy in enumerate((400, 470)):
            for k in range(4): hd.rectangle([440 + k * 62, yy, 490 + k * 62, yy + 50], fill=(30, 22, 16, 255))
        hd.ellipse([450, 170, 670, 330], fill=(238, 232, 214, 255)); hd.rounded_rectangle([400, 640, 720, 700], 10, fill=(236, 226, 200, 255))
        hd.line([(740, 620), (800, 640), (820, 800), (790, 900)], fill=(30, 22, 16, 255), width=26); hd.rectangle([770, 880, 830, 960], fill=(60, 60, 64, 255))
    else:
        cx, top, bot, w2 = 560, 330, 900, 230
        yy, xx = np.mgrid[0:H, 0:W]; inside = (abs(xx - cx) < w2) & (yy > top) & (yy < bot)
        nx = (xx - cx) / w2; lam = np.clip(0.8 - 0.9 * nx, 0.15, 1)
        col = np.stack([40 + 170 * lam, 30 + 70 * lam, 20 + 30 * lam], -1); col = np.clip(col + np.random.default_rng(1).normal(0, 6, (H, W, 1)), 0, 255)
        arr = np.zeros((H, W, 4), np.uint8); arr[..., :3] = col.astype(np.uint8); arr[..., 3] = (inside * 255).astype(np.uint8)
        hero = Image.alpha_composite(hero, Image.fromarray(arr)); hd = ImageDraw.Draw(hero)
        for yb in (top + 120, bot - 120): hd.rectangle([cx - w2, yb - 12, cx + w2, yb + 12], fill=(30, 22, 16, 255))
        hd.ellipse([cx - w2, top - 50, cx + w2, top + 50], fill=(90, 60, 30, 255)); hd.ellipse([cx - w2 + 20, top - 34, cx + w2 - 20, top + 34], fill=(30, 22, 16, 255))
        hd.polygon([(cx - 45, 470), (cx + 45, 470), (cx + 45, 680), (cx + 120, 680), (cx, 830), (cx - 120, 680), (cx - 45, 680)], fill=(60, 210, 110, 255), outline=(10, 40, 20, 255), width=6)
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
