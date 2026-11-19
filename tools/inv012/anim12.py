# INV-012 animation engine ("Round Two" look, animated, synced to the narration).
# Logical canvas 1280x720, drawn at 1920x1080 (S=1.5). Per frame the renderer sets:
#   T      seconds into the shot
#   DUR    shot length (s)
#   CUES   times (s, shot-relative) of the {cue} words of this script row  -> c(i)
#   SENTS  sentence start times (s, shot-relative)                          -> sn(i)
# Every element's entrance is keyed to a cue or a sentence start, so hits land on the spoken word.
# Look: dark ledger background with faint lines (look-rules), beige paper (214,204,186), Inter Bold, Caladea orange serif line,
# Bebas stamps (crimson, 140->100% + 3-frame shake), terrain hillshade maps with pulse rings, count-ups, typewriter, light sweeps.
import os, re, math, json, pathlib, io, urllib.request
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import shapefile
HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parent / "inv006" / "assets"
CACHE = HERE / "cache"; CACHE.mkdir(exist_ok=True)
W, H = 1280, 720
S = float(os.environ.get("INV_S", "1.5"))   # 1.5 -> 1920x1080, 0.5 -> 640x360 review
PW, PH = int(W*S), int(H*S)
INK=(16,15,14); PAPER=(214,204,186); PAPER_HI=(236,228,214); ORANGE=(232,89,12); RED=(230,57,70); CYAN=(0,180,216)
CRIMSON=(193,18,31); WARN=(255,84,0); GREY=(128,120,110); DIM=(70,66,60); LAND=(40,38,35); BORDER=(78,72,64); GREEN=(88,170,110)
T = 0.0; DUR = 8.0; CUES = []; SENTS = [0.0]

# ---------------- timing helpers ----------------
def c(i=0, d=None):
    """time of cue i (shot-relative). Fallback: d, else spread over the first 60% of the shot."""
    if i < 0: return -10.0
    if i < len(CUES): return CUES[i]
    if d is not None: return d
    return 0.4 + i * 0.9
def sn(i):
    if i < len(SENTS): return SENTS[i]
    return (SENTS[-1] if SENTS else 0) + 1.5 * (i - len(SENTS) + 1)
def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def ease_io(x): x = max(0.0, min(1.0, x)); return x*x*(3-2*x)
def seg(t0, d=0.5): return ease((T - t0) / d) if d > 0 else (1.0 if T >= t0 else 0.0)
def lead(t, k=0.35): return max(0.0, t - k)          # start an entrance slightly before the word so it *lands* on it
def alpha(col, a): return tuple(col[:3]) + (int(255 * max(0, min(1, a))),)
def mix(c1, c2, a): return tuple(int(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))

# ---------------- fonts / drawing ----------------
_FC = {}
def f(sz, kind="inter"):
    k = (sz, kind)
    if k not in _FC:
        p = {"inter": A/"Inter-Bold.otf", "reg": A/"Inter-Regular.otf", "serif": A/"CaladeaBI.ttf", "bebas": A/"Bebas.ttf"}[kind]
        fo = ImageFont.truetype(str(p), int(round(sz * S))); fo.lsize = sz; _FC[k] = fo
    return _FC[k]
class D:
    def __init__(s, im): s.im = im; s.d = ImageDraw.Draw(im, "RGBA")
    def text(s, xy, t, font, fill, anchor=None):
        # Pillow ignores fill alpha for text on RGB images, so fades go through a mask
        a = fill[3] if len(fill) > 3 else 255
        if a <= 0 or not t: return
        x, y = xy[0]*S, xy[1]*S
        if a >= 255: s.d.text((x, y), t, font=font, fill=fill, anchor=anchor); return
        b = s.d.textbbox((x, y), t, font=font, anchor=anchor); x0, y0 = int(b[0]) - 2, int(b[1]) - 2
        m = Image.new("L", (int(b[2]) - x0 + 4, int(b[3]) - y0 + 4), 0)
        ImageDraw.Draw(m).text((x - x0, y - y0), t, font=font, fill=int(a), anchor=anchor)
        s.im.paste(tuple(fill[:3]) + ((255,) if s.im.mode == "RGBA" else ()), (x0, y0), m)
    def tl(s, t, font): return s.d.textlength(t, font=font) / S
    def line(s, pts, fill, width=1): s.d.line([(x*S, y*S) for x, y in pts], fill=fill, width=max(1, int(width*S)), joint="curve")
    def rect(s, b, fill=None, outline=None, width=1):
        if b[2] <= b[0] or b[3] <= b[1]: return
        s.d.rectangle([b[0]*S, b[1]*S, b[2]*S, b[3]*S], fill=fill, outline=outline, width=max(1, int(width*S)))
    def rrect(s, b, r, fill=None, outline=None, width=1):
        if b[2] <= b[0] or b[3] <= b[1]: return
        s.d.rounded_rectangle([b[0]*S, b[1]*S, b[2]*S, b[3]*S], radius=r*S, fill=fill, outline=outline, width=max(1, int(width*S)))
    def ell(s, b, fill=None, outline=None, width=1): s.d.ellipse([b[0]*S, b[1]*S, b[2]*S, b[3]*S], fill=fill, outline=outline, width=max(1, int(width*S)))
    def poly(s, pts, fill=None, outline=None): s.d.polygon([(x*S, y*S) for x, y in pts], fill=fill, outline=outline)
    def arc(s, b, a0, a1, fill, width=1): s.d.arc([b[0]*S, b[1]*S, b[2]*S, b[3]*S], a0, a1, fill=fill, width=max(1, int(width*S)))
def fit(d, text, sz, maxw, kind="inter"):
    while sz > 20 and d.tl(text, f(sz, kind)) > maxw: sz -= 2
    return f(sz, kind)
def center(d, y, text, font, fill, cx=W/2): d.text((cx - d.tl(text, font)/2, y), text, font, fill)
def wrap(d, text, font, maxw):
    out, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if d.tl(t, font) <= maxw: cur = t
        else: out.append(cur); cur = w_
    if cur: out.append(cur)
    return out
def countup(s, e):
    def rep(m):
        txt = m.group(0); dec = len(txt.split(".")[1]) if "." in txt else 0; v = float(txt.replace(",", "")) * e
        return f"{v:,.{dec}f}" if "," in txt else f"{v:.{dec}f}"
    return re.sub(r"\d[\d,]*(?:\.\d+)?", rep, s)

# ---------------- background: dark ledger (part-card background) ----------------
_BG = {}
def base(kind="ledger"):
    if kind not in _BG:
        im = Image.new("RGB", (PW, PH), (19, 18, 17)); d = ImageDraw.Draw(im)
        if kind == "ledger":
            for y in range(0, PH, int(36*S)): d.line([(0, y), (PW, y)], fill=(29, 28, 26), width=2)
            d.line([(int(150*S), 0), (int(150*S), PH)], fill=(44, 26, 20), width=3)
        v = Image.new("L", (PW//4, PH//4), 0); vd = ImageDraw.Draw(v)
        vw, vh = PW//4, PH//4
        for i in range(40): vd.rectangle([int(i*vw/320*3), int(i*vh/180*2), vw - int(i*vw/320*3), vh - int(i*vh/180*2)], fill=int(i*6.3))
        v = v.filter(ImageFilter.GaussianBlur(22)).resize((PW, PH))
        _BG[kind] = Image.composite(im, Image.new("RGB", (PW, PH), (4, 4, 4)), v.point(lambda x: min(255, 110 + x)))
    return _BG[kind].copy()

def glow(im, draw_fn, radius=18, strength=1.0):
    """draw_fn(D) on a small layer, blur, add -> cheap bloom for 'light is the design'."""
    sm = Image.new("RGBA", (PW//4, PH//4), (0, 0, 0, 0)); d = ImageDraw.Draw(sm, "RGBA")
    class Q(D):
        def __init__(s, im_): s.im = im_; s.d = d
    global S
    S0 = S; S = S0 / 4
    try: draw_fn(Q(sm))
    finally: S = S0
    sm = sm.filter(ImageFilter.GaussianBlur(radius/4)).resize((PW, PH), Image.BILINEAR)
    rgb = sm.convert("RGB"); a = sm.getchannel("A").point(lambda v: int(v*strength))
    lit = ImageChops.add(im.convert("RGB"), ImageChops.multiply(rgb, Image.merge("RGB", (a, a, a))))
    return lit

def sweep(im, box, t0, d=1.2):
    """light sweep across big type (a moving soft diagonal band), once, starting at t0."""
    k = (T - t0) / d
    if k <= 0 or k >= 1: return im
    x0, y0, x1, y1 = box; cx = x0 + (x1 - x0 + 300) * k - 150
    band = Image.new("L", (PW, PH), 0); bd = ImageDraw.Draw(band)
    bd.polygon([((cx-40)*S, y0*S), ((cx+40)*S, y0*S), ((cx-20)*S, y1*S), ((cx-100)*S, y1*S)], fill=70)
    band = band.filter(ImageFilter.GaussianBlur(12))
    return Image.composite(Image.new("RGB", (PW, PH), (255, 240, 220)), im, band)

def tagline(im, tag):
    if not tag: return
    d = D(im); a = seg(0.8, 0.6); col = GREY
    d.rect((40, H-52, 46, H-28), fill=alpha(ORANGE, a)); d.text((56, H-50), tag.upper()[:110], f(18, "reg"), alpha(col, a))

def paper(im, box, col=PAPER, seed=1, shadow=True):
    d = D(im); x0, y0, x1, y1 = box
    if shadow: d.rect((x0+8, y0+10, x1+8, y1+10), fill=(0, 0, 0, 120))
    d.rect(box, fill=col)
    rng = np.random.default_rng(seed)
    for i in range(int((x1-x0)//14)):  # torn bottom edge
        x = x0 + i*14; d.poly([(x, y1), (x+7, y1+rng.integers(2, 7)), (x+14, y1)], fill=col)
    return d

def stamp(im, text, cx, cy, t0, col=CRIMSON, size=96, angle=-8, box=True):
    k = (T - t0) / 0.22
    if k <= 0: return
    k = min(1.0, k)
    fo = f(size, "bebas"); tmp = Image.new("RGBA", (10, 10)); w = ImageDraw.Draw(tmp).textlength(text, font=fo) / S
    sw, sh = int((w + 50) * S), int((size + 34) * S)
    st = Image.new("RGBA", (sw, sh), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    if box: sd.rectangle([6, 6, sw-6, sh-6], outline=col + (235,), width=int(7*S))
    sd.text((25*S, 10*S), text, font=fo, fill=col + (235,))
    # grunge: knock out speckles
    rng = np.random.default_rng(len(text)); m = np.array(st.getchannel("A"))
    holes = rng.random(m.shape) < 0.06; m[holes] = (m[holes] * 0.25).astype(np.uint8); st.putalpha(Image.fromarray(m))
    st = st.rotate(angle, expand=True, resample=Image.BICUBIC)
    z = 1.4 - 0.4 * ease(k)
    st = st.resize((max(1, int(st.width*z)), max(1, int(st.height*z))), Image.BILINEAR)
    if k < 1: st.putalpha(st.getchannel("A").point(lambda v: int(v * k)))
    shake = 0
    fr_after = (T - t0 - 0.22) * 25
    if 0 <= fr_after < 3: shake = [5, -4, 2][int(fr_after)]
    im.paste(st, (int(cx*S - st.width/2 + shake*S), int(cy*S - st.height/2)), st)

def typewriter(d, xy, text, font, fill, t0, cps=28):
    n = int(max(0, (T - t0)) * cps)
    if n <= 0: return
    s = text[:n]; d.text(xy, s, font, fill)
    if n < len(text) and int(T*4) % 2 == 0: d.rect((xy[0] + d.tl(s, font) + 3, xy[1] + 4, xy[0] + d.tl(s, font) + 14, xy[1] + font.lsize), fill=fill)

def pulse_rings(d, x, y, col, t0, n=2, rmax=46, speed=0.6):
    if T < t0: return
    for ph in range(n):
        q = ((T - t0) * speed + ph / n) % 1.0; r = 10 + rmax * q
        d.ell((x-r, y-r, x+r, y+r), outline=alpha(col, (1-q)*0.9), width=2)

# ---------------- hand-drawn layer: pencil strokes, pen circles, marker highlights (everything draws itself on the word) ----------------
PENCIL = (230, 222, 206); GRAPHITE = (58, 50, 44); MARKER = (255, 196, 40)
def _poly_upto(pts, k):
    """the first k (0..1) of a polyline, by length."""
    if k >= 1: return pts
    L = [0.0]
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]): L.append(L[-1] + math.hypot(xb - xa, yb - ya))
    tgt = L[-1] * k; out = [pts[0]]
    for i in range(1, len(pts)):
        if L[i] <= tgt: out.append(pts[i]); continue
        q = (tgt - L[i-1]) / max(1e-6, L[i] - L[i-1]); (xa, ya), (xb, yb) = pts[i-1], pts[i]
        out.append((xa + (xb - xa)*q, ya + (yb - ya)*q)); break
    return out
def pencil(d, pts, t0, dur=0.5, col=None, w=3.5, seed=1, passes=2):
    """graphite/pen stroke that draws itself along pts from t0 (two slightly offset passes = hand-drawn)."""
    k = ease_io((T - t0) / dur) if dur > 0 else 1.0
    if k <= 0: return
    col = col or PENCIL; rng = np.random.default_rng(seed)
    for p in range(passes):
        jit = rng.normal(0, 1.1, (len(pts), 2)); q = [(x + jit[i][0] + p*0.9, y + jit[i][1] + p*0.7) for i, (x, y) in enumerate(pts)]
        sub = _poly_upto(q, k)
        if len(sub) > 1: d.line(sub, alpha(col, 0.95 if p == 0 else 0.5), w if p == 0 else w*0.6)
def pencil_underline(d, x0, x1, y, t0, col=None, seed=1, w=4, dur=0.45):
    rng = np.random.default_rng(seed + 7); n = 26
    pts = [(x0 + (x1 - x0)*i/(n-1), y + 3*math.sin(i/(n-1)*math.pi) - 2*i/(n-1) + rng.normal(0, 0.6)) for i in range(n)]
    pts += [(x1 - 26, y + 7), (x1 - 52, y + 8)]   # little return flick
    pencil(d, pts, t0, dur, col, w, seed)
def pencil_circle(d, cx, cy, rx, ry, t0, col=RED, seed=1, w=5, dur=0.6):
    """loose pen ellipse, a bit more than one turn, starting top-left, like a hand circling a number."""
    rng = np.random.default_rng(seed + 3); n = 64; a0 = math.radians(-120); span = math.radians(395)
    pts = []
    for i in range(n):
        q = i/(n-1); a = a0 + span*q; r = 1.0 + 0.05*math.sin(q*7 + seed) + 0.06*q
        pts.append((cx + rx*r*math.cos(a) + rng.normal(0, 0.5), cy + ry*r*math.sin(a) + rng.normal(0, 0.5)))
    pencil(d, pts, t0, dur, col, w, seed)
def pencil_tick(d, x, y, t0, col=GRAPHITE, seed=1, s=1.0):
    pencil(d, [(x, y + 10*s), (x + 8*s, y + 20*s), (x + 26*s, y - 4*s)], t0, 0.25, col, 4, seed)
def highlight(d, box, t0, col=MARKER, a=0.38, dur=0.45):
    """marker highlight sweeping left to right behind text (draw it BEFORE the text)."""
    k = ease_io((T - t0) / dur)
    if k <= 0: return
    x0, y0, x1, y1 = box; xe = x0 + (x1 - x0)*k
    d.poly([(x0 - 6, y0 + 4), (xe, y0), (xe + 4, y1 - 2), (x0 - 2, y1 + 3)], fill=alpha(col, a))

# ---------------- generic types ----------------
def part(n, title, sub=""):
    im = base(); d = D(im)
    center(d, 10, str(n), f(600, "bebas"), alpha((44, 40, 36), seg(0, 1.0)))
    a = seg(0.1, 0.5); center(d, 230 - (1-a)*20, f"PART {n}", f(40, "inter"), alpha(ORANGE, a))
    b = seg(0.35, 0.6)
    lines = wrap(d, title.upper(), f(104, "inter"), W - 160)
    for i, l in enumerate(lines): center(d, 290 + i*112 + (1-b)*40, l, f(104, "inter"), alpha(PAPER_HI, b))
    if sub: center(d, 300 + len(lines)*112, sub, f(40, "serif"), alpha(ORANGE, seg(0.9, 0.5)))
    im = sweep(im, (0, 280, W, 300 + len(lines)*112), 0.9, 1.4)
    return im

def number(big, sub="", kicker="", tag="", faded="", strike=None, cue=0, badge=None):
    im = base(); d = D(im); hit = c(cue, 1.0)
    if kicker: center(d, 140, kicker.upper(), f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    fb = f(160 if len(big) < 9 else 116, "inter")
    if faded: center(d, 170, faded, f(250, "bebas"), alpha((48, 44, 40), seg(0.2, 0.8)))
    e = ease_io((T - lead(hit, 1.1)) / 1.1)
    if not strike:
        bw_ = d.tl(big, fb); highlight(d, ((W - bw_)/2 - 18, 238, (W + bw_)/2 + 18, 205 + fb.lsize + 26), hit + 0.05, ORANGE, 0.30, 0.4)
    center(d, 205, countup(big, e) if not strike else big, fb, alpha(PAPER_HI, min(1, e*4) if not strike else seg(0, 0.4)))
    if strike:
        w = d.tl(big, fb); x0 = (W - w)/2; k = seg(hit - 0.2, 0.35)
        if k > 0: d.line([(x0-10, 300), (x0-10 + (w+20)*k, 290 - 26*k)], fill=CRIMSON, width=11)
        center(d, 400, strike, f(130, "inter"), alpha(ORANGE, seg(hit, 0.4)))
    if sub:
        a = seg(hit + 0.2, 0.5)
        sl = wrap(d, sub, f(42, "serif"), W - 220)[:2]
        for i, l in enumerate(sl): center(d, (430 if not strike else 560) + i*54, l, f(42, "serif"), alpha(ORANGE, a))
        uw = d.tl(sl[0], f(42, "serif")); uy = (430 if not strike else 560) + len(sl)*54 + 2
        pencil_underline(d, (W - uw)/2, (W + uw)/2, uy, hit + 0.7, PENCIL, seed=len(big))
    if badge: stamp(im, badge, W - 250, 140, hit + 0.4, col=ORANGE, size=64, angle=-6)
    im = sweep(im, (0, 200, W, 380), hit + 0.1, 1.2)
    tagline(im, tag); return im

def quote(q, who, when, tag="", cue=0):
    im = base(); d = paper(im, (190, 130, W-190, H-150), seed=3); hit = c(cue, 0.8)
    a = seg(0.1, 0.5)
    center(d, 160, "“", f(180, "serif"), alpha(ORANGE, a))
    y = 300 - 40
    qf = f(110 if len(q) < 20 else 60, "serif"); y = 280 if len(q) < 20 else 260
    ql = wrap(d, q, qf, W - 480)
    for j, l in enumerate(ql):
        lw = d.tl(l, qf); highlight(d, ((W - lw)/2, y + qf.lsize*0.35, (W + lw)/2, y + qf.lsize*1.12), hit + 0.5 + j*0.45, MARKER, 0.42, 0.45)
        center(d, y, l, qf, alpha((30, 26, 22), seg(lead(hit, 0.4), 0.5))); y += qf.lsize + 12
    center(d, y + 20, f"{who} · {when}", f(28, "inter"), alpha((90, 60, 40), seg(hit + 0.3, 0.5)))
    ww = d.tl(f"{who} · {when}", f(28, "inter")); pencil_underline(d, (W - ww)/2, (W + ww)/2, y + 58, hit + 0.6 + len(ql)*0.45, GRAPHITE, seed=len(q), w=3)
    tagline(im, tag); return im

def card(lines, kicker="", tag="", stamp_txt=None, cues=None, style="big"):
    im = base(); d = D(im); y = 170 if kicker else 160
    if kicker: center(d, 92, kicker.upper(), f(30, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i, l in enumerate(lines):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i)) - 0.3
        fo = f(66, "inter") if style == "big" else f(52, "serif")
        col = PAPER_HI if i % 2 == 0 else ORANGE
        a = seg(t0, 0.5)
        for ll in wrap(d, l, fo, W - 200): center(d, y + (1-a)*16, ll, fo, alpha(col, a)); y += fo.lsize + 22
        if i == len(lines) - 1:
            lw = d.tl(wrap(d, l, fo, W - 200)[-1], fo); pencil_underline(d, (W - lw)/2, (W + lw)/2, y - 12, t0 + 0.55, RED, seed=i + 41, w=5)
    if stamp_txt: stamp(im, stamp_txt, W/2, min(H-120, y + 80), c(len(lines) if cues is None else cues[-1], sn(len(lines))) + 0.2)
    tagline(im, tag); return im

def typed(lines, label="FILE", tag="", stamps=(), cue_lines=None, title=""):
    """index cards typed in turn (Round Two typewriter G08), optional stamps [(text, at_time)]."""
    im = base(); d = D(im); n = len(lines)
    if title: d.text((170, 50), title.upper(), fit(d, title.upper(), 34, 900), alpha(ORANGE, seg(0.1, 0.4)))
    for i, l in enumerate(lines):
        t0 = c(cue_lines[i]) - 0.6 if cue_lines else sn(i) + 0.1
        a = seg(t0 - 0.3, 0.4)
        if a <= 0: continue
        x0 = 170 + i*40; y0 = 120 + i*150
        dd = paper(im, (x0, y0 + (1-a)*30, x0 + 760, y0 + 120 + (1-a)*30), seed=i+5)
        dd.text((x0 + 24, y0 + 14), label, f(18, "inter"), (150, 60, 40))
        typewriter(dd, (x0 + 24, y0 + 48), l, f(40, "inter"), (30, 26, 22), t0, 30)
        tdone = t0 + len(l)/30 + 0.2
        if i == n - 1: pencil_underline(dd, x0 + 24, x0 + 24 + dd.tl(l, f(40, "inter")), y0 + 100, tdone, RED, seed=i + 81, w=4)
    for txt, at in stamps: stamp(im, txt, W - 260, H - 170, at)
    tagline(im, tag); return im

def headline(outlet, text, date, stamp_txt=None, tag=""):
    im = base(); dx = (1 - seg(0, 0.5)) * W
    d = paper(im, (150+dx, 110, W-150+dx, H-150), col=(226, 220, 208), seed=7)
    d.text((190+dx, 140), outlet.upper(), f(34, "inter"), INK); d.text((W-190-d.tl(date, f(26, "reg"))+dx, 146), date, f(26, "reg"), (90, 90, 90))
    d.line([(190+dx, 196), (W-190+dx, 196)], INK, 3)
    y = 224
    for i, l in enumerate(wrap(d, text, f(56, "inter"), W - 380)):
        highlight(d, (190+dx, y + 18, 190+dx + d.tl(l, f(56, "inter")), y + 66), c(0, 1.2) + i*0.4, MARKER, 0.5, 0.45)
        d.text((190+dx, y), l, f(56, "inter"), alpha(INK, seg(0.3 + i*0.25, 0.3))); y += 70
    d.text((190+dx, H-196), "Recreated headline · outlet credited", f(20, "reg"), (110, 110, 110))
    if stamp_txt: stamp(im, stamp_txt, W - 330, H - 190, c(0, 2.0))
    tagline(im, tag); return im

def receipt(lines, title="THE RECEIPT", tag="", show=None, final_stamp=None, cues_from=None, cols=False):
    """paper receipt rising, lines print in turn (receipt-printer). show = how many lines are already printed at T=0."""
    im = base(); d = D(im); pw = 760 if not cols else 900; x = (W - pw)/2
    rise = (1 - seg(0, 0.7)) * H if (show is None or show == 0 or show >= len(lines)) and title != "RUNNING TOTAL" else 0
    d.rect((x+10, 50+rise+12, x+pw+10, H-30+rise+12), fill=(0, 0, 0, 120)); d.rect((x, 50+rise, x+pw, H-30+rise), fill=PAPER)
    for i in range(0, int(pw), 24): d.poly([(x+i, H-30+rise), (x+i+12, H-16+rise), (x+i+24, H-30+rise)], fill=PAPER)
    center(d, 70+rise, "THE HISTORY INVOICE", f(24, "inter"), INK); center(d, 102+rise, title, f(42, "bebas"), INK)
    d.line([(x+30, 152+rise), (x+pw-30, 152+rise)], INK, 2)
    y = 172 + rise; show = len(lines) if show is None else show
    for i, l in enumerate(lines):
        if i < show: t0 = -1
        else: t0 = (c(i - show) if cues_from is None else cues_from[i - show]) - 0.3
        a = seg(t0, 0.18)
        if a <= 0: break
        col = CRIMSON if (final_stamp and i == len(lines)-1) else INK
        left, right = (l if isinstance(l, tuple) else (l, ""))
        d.text((x+30, y), left, f(29, "reg"), alpha(col, a))
        if right: d.text((x+pw-30-d.tl(right, f(29, "inter")), y), right, f(29, "inter"), alpha(col, a))
        if i >= show and a > 0: pencil_tick(d, x + pw + 12, y + 2, t0 + 0.35, PENCIL, seed=i)
        y += 50
    if final_stamp: stamp(im, final_stamp, W/2 + 120, H - 150, c(len(lines) - show, sn(1)) + 0.4, size=84)
    tagline(im, tag); return im

def bars(items, title="", unit="", hi=None, tag="", cues=None, fmt="{:,.0f}", log=False, reveal=None):
    im = base(); d = D(im)
    if title:
        sz = 36
        while sz > 22 and d.tl(title.upper(), f(sz, "inter")) > 840: sz -= 2
        d.text((180, 60), title.upper(), f(sz, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    vals = [v for _, v in items]; mx = max(vals) or 1
    n = len(items); bw = min(220, (W - 340) // n - 40); gap = ((W - 300) - n*bw) // max(1, n)
    for i, (lab, v) in enumerate(items):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i) + 0.3) - 0.5
        e = ease_io((T - t0) / 0.9)
        x = 200 + i*(bw+gap) + gap//2
        frac = (math.log10(max(v, 1)) / math.log10(mx)) if log else v / mx
        h = int(380 * frac * e); y = H - 150 - h
        col = ORANGE if (hi is None or i == hi) else (96, 88, 80)
        if reveal and i == reveal[0] and 0 < T - (t0 + 0.9) < 0.45 and int((T - t0) * 20) % 2: col = PAPER_HI   # flicker as it lands (G18)
        if h > 0: d.rect((x, y, x+bw, H-150), fill=col)
        if reveal and i == reveal[0]: stamp(im, reveal[1], min(W - 150, x + bw + 150) if x + bw + 150 < W - 100 else x - 150, max(220, y + 80), t0 + 1.35, size=70, angle=-7)
        val = fmt.format(v*e) + unit; tw = d.tl(val, f(38, "inter"))
        d.text((x + (bw-tw)/2, y - 50), val, f(38, "inter"), alpha(PAPER_HI, min(1, e*4)))
        if hi is not None and i == hi: pencil_circle(d, x + bw/2, y - 28, tw/2 + 34, 36, t0 + 1.0, RED, seed=i + 2)
        for j, l in enumerate(wrap(d, lab, f(24, "reg"), bw + 60)[:2]):
            tw = d.tl(l, f(24, "reg")); d.text((x + (bw-tw)/2, H - 138 + j*28), l, f(24, "reg"), alpha(PAPER, seg(0.1, 0.4)))
    tagline(im, tag); return im

def linechart(series, title="", marks=(), tag="", unit="", band=None, hit=None, ylab_fmt="{:g}"):
    """series: {name: [(label, value), ...]}; the line draws up to the hit word; marks: [(text, idx, series_idx)]."""
    im = base(); d = D(im)
    if title: d.text((180, 52), title.upper(), fit(d, title.upper(), 34, 840), alpha(PAPER_HI, seg(0, 0.4)))
    allv = [v for s in series.values() for _, v in s]; mn = min(0, min(allv)); mx = max(allv) * 1.15
    x0, x1, y0, y1 = 220, W - 90, 130, H - 120
    Y = lambda v: y1 - (y1 - y0) * (v - mn) / (mx - mn)
    d.line([(x0, y1), (x1, y1)], GREY, 2)
    if band:
        d.rect((x0, Y(band[1]), x1, Y(band[0])), fill=alpha((80, 120, 140), 0.25 * seg(0.4, 0.6)))
        d.text((x1 - 260, Y(band[1]) - 30), band[2], f(22, "inter"), alpha(CYAN, seg(0.6, 0.6)))
    cols = [ORANGE, CYAN, PAPER, RED]; end = c(0, DUR * 0.6) if hit is None else hit
    e = ease_io((T - 0.3) / max(0.6, end - 0.3))
    for k, (name, pts) in enumerate(series.items()):
        n = len(pts); xy = [(x0 + (x1 - x0) * i / max(1, n-1), Y(v)) for i, (_, v) in enumerate(pts)]
        pos = e * (n - 1); full = int(pos); fr = pos - full; part_ = xy[:full+1]
        if full < n - 1: part_ = part_ + [(xy[full][0] + (xy[full+1][0] - xy[full][0]) * fr, xy[full][1] + (xy[full+1][1] - xy[full][1]) * fr)]
        if len(part_) > 1: d.line(part_, cols[k % 4], 6)
        for i, ((lab, v), (x, y)) in enumerate(zip(pts, xy)):
            if i <= pos + 1e-6:
                d.ell((x-7, y-7, x+7, y+7), fill=cols[k % 4])
                if k == 0 or len(series) == 1:
                    vt = ylab_fmt.format(v) + unit; d.text((x - d.tl(vt, f(24, "inter"))/2, y - 40), vt, f(24, "inter"), PAPER_HI)
            if lab and k == 0: d.text((x - d.tl(lab, f(20, "reg"))/2, y1 + 12), lab, f(20, "reg"), alpha(GREY, seg(0.1, 0.4)))
        if len(series) > 1 and pos >= n - 1 - 1e-6:
            lx, ly = xy[-1]; d.text((lx - 10 - d.tl(name, f(24, "inter")), ly + 14), name, f(24, "inter"), alpha(cols[k % 4], seg(end, 0.4)))
    for (txt, i, s_) in marks:
        pts = list(series.values())[s_]; n = len(pts)
        if e * (n - 1) < i - 1e-6: continue
        x = x0 + (x1 - x0) * i / max(1, n-1); y = Y(pts[i][1])
        pulse_rings(d, x, y, PAPER_HI, end - 0.2, 2, 40)
        d.text((x - d.tl(txt, f(28, "inter")) - 24, y + 22), txt, f(28, "inter"), alpha(ORANGE, seg(end, 0.4)))
    tagline(im, tag); return im

def gauge(pct, label, sub="", tag="", ring_max=100, stamp_txt=None, outline_pct=None, unit="%", valtxt=None):
    im = base(); d = D(im); hit = c(0, 1.2)
    cx, cy, r = W/2, 330, 200
    d.arc((cx-r, cy-r, cx+r, cy+r), 135, 405, fill=(52, 48, 44), width=34)
    if outline_pct is not None:
        d.arc((cx-r, cy-r, cx+r, cy+r), 135, 135 + 270*outline_pct/ring_max, fill=alpha(CYAN, seg(0.3, 0.6)), width=8)
    e = ease_io((T - lead(hit, 1.2)) / 1.2)
    a1 = 135 + 270 * (pct/ring_max) * e
    if e > 0: d.arc((cx-r, cy-r, cx+r, cy+r), 135, a1, fill=ORANGE, width=34)
    txt = valtxt(e) if valtxt else countup(f"{pct:g}", e) + unit
    center(d, cy - 80, txt, f(118, "inter"), alpha(PAPER_HI, min(1, e*4)))
    center(d, cy + 232, label.upper(), f(30, "inter"), alpha(PAPER, seg(0.2, 0.4)))
    if sub:
        center(d, cy + 274, sub, f(34, "serif"), alpha(ORANGE, seg(hit + 0.3, 0.5)))
        sw_ = d.tl(sub, f(34, "serif")); pencil_underline(d, (W - sw_)/2, (W + sw_)/2, cy + 318, hit + 0.8, PENCIL, seed=int(pct))
    if stamp_txt: stamp(im, stamp_txt, cx + 300, cy - 180, hit + 0.5, size=72)
    im = glow(im, lambda g: g.arc((cx-r, cy-r, cx+r, cy+r), 135, a1, fill=(232, 89, 12, 200), width=40), 26, 0.8) if e > 0 else im
    tagline(im, tag); return im

def tiles(items, title="", tag="", cues=None):
    """option / scenario tiles lighting in turn. items: [(big, small)]"""
    im = base(); d = D(im); n = len(items)
    if title: center(d, 70, title.upper(), fit(d, title.upper(), 34, 760), alpha(ORANGE, seg(0, 0.4)))
    tw = (W - 240 - (n-1)*30) / n
    for i, (big, small) in enumerate(items):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i)) - 0.3; a = seg(t0, 0.45); lit = seg(t0, 0.2) * (1 - 0.6*seg((c(cues[i+1]) if cues and i+1 < len(cues) else sn(i+1)) - 0.3, 0.4) if i < n-1 else 1)
        x = 120 + i*(tw + 30); y = 220 + (1-a)*30
        d.rect((x, y, x+tw, y+300), fill=alpha(mix((40, 38, 35), (70, 40, 26), lit), a), outline=alpha(ORANGE, a*lit), width=3)
        bl = wrap(d, big, f(46, "inter"), tw - 40)
        for j, l in enumerate(bl): center(d, y + 70 + j*56, l, f(46, "inter"), alpha(PAPER_HI, a), cx=x + tw/2)
        lw = min(tw - 50, max(d.tl(l, f(46, "inter")) for l in bl)); pencil_underline(d, x + tw/2 - lw/2, x + tw/2 + lw/2, y + 70 + len(bl)*56 + 4, t0 + 0.45, ORANGE, seed=i + 11, w=3)
        for j, l in enumerate(wrap(d, small, f(24, "reg"), tw - 40)[:3]): center(d, y + 210 + j*30, l, f(24, "reg"), alpha(PAPER, a), cx=x + tw/2)
    tagline(im, tag); return im

def timeline(events, active, title="", tag="", stamp_txt=None):
    """dated nodes; nodes up to `active` light (earlier ones dim to 40%), the active ones on their cue."""
    im = base(); d = D(im); n = len(events)
    if title: d.text((180, 70), title.upper(), fit(d, title.upper(), 34, 840), alpha(PAPER_HI, seg(0, 0.4)))
    x0, x1, y = 230, W - 120, 380
    d.line([(x0, y), (x1, y)], DIM, 4)
    for i, (date, label) in enumerate(events):
        x = x0 + (x1 - x0) * i / max(1, n - 1)
        if i < active[0]: a, col = 0.45, PAPER
        elif i in active:
            k = active.index(i); a = seg(lead(c(k), 0.3), 0.4); col = ORANGE if i < n-1 else RED
        else: a, col = 0.12, GREY
        d.ell((x-14, y-14, x+14, y+14), fill=alpha(col, max(a, 0.12)))
        center(d, y - 80, date, f(40, "bebas"), alpha(col, max(a, 0.15)), cx=x)
        for j, l in enumerate(wrap(d, label, f(22, "reg"), 210)[:3]): center(d, y + 34 + j*28, l, f(22, "reg"), alpha(PAPER, a), cx=x)
        if i in active:
            pulse_rings(d, x, y, col, lead(c(active.index(i)), 0.3), 2, 36)
            dw = d.tl(date, f(40, "bebas")); pencil_circle(d, x, y - 58, dw/2 + 26, 30, lead(c(active.index(i)), 0.3) + 0.35, RED, seed=i + 5, w=4)
    if stamp_txt: stamp(im, stamp_txt, W - 330, 170, c(len(active), c(0) + 1.2))
    tagline(im, tag); return im

def calendar(months, circles=(), flames_every=None, stamps=(), title="", tag=""):
    """month strip; circles: [(month_idx, label, cue_i)] red pen circles; stamps: [(month_idx, text, cue_i)]; flames_every: n days."""
    im = base(); d = D(im)
    if title: d.text((180, 56), title.upper(), fit(d, title.upper(), 34, 840), alpha(PAPER_HI, seg(0, 0.4)))
    n = len(months); cw = (W - 420) / n; X0 = 160
    for i, m in enumerate(months):
        x = X0 + i*cw; a = seg(0.05*i, 0.3)
        d.rect((x+6, 140, x+cw-6, H-140), fill=alpha((36, 34, 31), a), outline=alpha(DIM, a), width=2)
        center(d, 152, m, f(34, "bebas"), alpha(PAPER, a), cx=x + cw/2)
        if flames_every:
            days = 30; per_row = 5; gx = (cw - 30) / per_row; hit = c(0, DUR*0.5)
            for dday in range(days):
                gxx = x + 18 + (dday % per_row)*gx; gyy = 200 + (dday // per_row)*52
                if dday % flames_every == 0:
                    t0 = 0.4 + (hit - 0.4) * (i*days + dday) / (n*days)
                    if T >= t0:
                        d.poly([(gxx+8, gyy+30), (gxx+gx/2, gyy+2), (gxx+gx-8, gyy+30)], fill=alpha(ORANGE, seg(t0, 0.2)))
                else: d.ell((gxx+gx/2-3, gyy+14, gxx+gx/2+3, gyy+20), fill=(70, 66, 60))
    for j, (mi, lab, ci) in enumerate(circles):
        x = X0 + mi*cw + cw/2; t0 = lead(c(ci), 0.3); k = seg(t0, 0.5)
        if k > 0:
            pencil_circle(d, x, 335, cw*0.46, 105, t0, RED, seed=j + 21, w=7, dur=0.5)
            fo = fit(d, lab, 26, 300); lx = min(max(x, X0 + d.tl(lab, fo)/2), X0 + n*cw - d.tl(lab, fo)/2)
            center(d, 468 + (j % 2)*40, lab, fo, alpha(RED, seg(t0 + 0.4, 0.3)), cx=lx)
    for (mi, txt, ci) in stamps: stamp(im, txt, X0 + mi*cw + cw/2, 360, c(ci), size=58, angle=-12)
    tagline(im, tag); return im

def chain(steps, title="", tag="", cues=None, times=None):
    im = base(); d = D(im); n = len(steps)
    if title: center(d, 80, title.upper(), f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    gap = (W - 260) / n
    for i, s in enumerate(steps):
        t0 = (times[i] if times else c(cues[i]) if cues and i < len(cues) else sn(i)) - 0.25; a = seg(t0, 0.4)
        x = 160 + i*gap + gap/2; y = 360
        d.ell((x-70, y-70, x+70, y+70), fill=alpha((44, 40, 36), a), outline=alpha(ORANGE, a), width=4)
        center(d, y - 20, s.upper(), fit(d, s.upper(), 32, 124), alpha(PAPER_HI, a), cx=x)
        if i < n - 1:
            k = seg(t0 + 0.3, 0.4); xa = x + 76; xb = x + gap - 76
            if k > 0: d.line([(xa, y), (xa + (xb - xa)*k, y)], ORANGE, 4)
        pulse_rings(d, x, y, ORANGE, t0, 1, 90, 0.4)
    tagline(im, tag); return im

def flow(nodes, arrows, title="", tag="", cues=None):
    """box-and-arrow diagram. nodes: {key: (x, y, label, col)}, arrows: [(a, b, label, cue_i)]"""
    im = base(); d = D(im)
    if title: d.text((180, 56), title.upper(), fit(d, title.upper(), 34, 840), alpha(PAPER_HI, seg(0, 0.4)))
    shown = {}
    for j, (a_, b_, lab, ci) in enumerate(arrows):
        t0 = lead(c(ci), 0.4) if ci is not None else sn(j)
        for k_ in (a_, b_): shown[k_] = min(shown.get(k_, 99), t0 if k_ == b_ else 0.2)
    for k_, (x, y, lab, col) in nodes.items():
        a = seg(shown.get(k_, 0.2), 0.4); bw = max(170, d.tl(lab, f(28, "inter")) + 40)
        d.rrect((x - bw/2, y - 40, x + bw/2, y + 40), 10, fill=alpha((40, 37, 34), a), outline=alpha(col, a), width=3)
        center(d, y - 18, lab, f(28, "inter"), alpha(PAPER_HI, a), cx=x)
    for j, (a_, b_, lab, ci) in enumerate(arrows):
        t0 = lead(c(ci), 0.4) if ci is not None else sn(j); k = seg(t0, 0.6)
        if k <= 0: continue
        (xa, ya, *_), (xb, yb, *_) = nodes[a_], nodes[b_]
        L = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa)/L, (yb - ya)/L
        sx, sy = xa + ux*95, ya + uy*50; ex, ey = xb - ux*95, yb - uy*50
        px, py = sx + (ex - sx)*k, sy + (ey - sy)*k
        d.line([(sx, sy), (px, py)], ORANGE, 4)
        if k > 0.95: d.poly([(ex, ey), (ex - ux*18 - uy*10, ey - uy*18 + ux*10), (ex - ux*18 + uy*10, ey - uy*18 - ux*10)], fill=ORANGE)
        if lab: d.text(((sx+ex)/2 + 10, (sy+ey)/2 - 34), lab, f(22, "inter"), alpha(ORANGE, seg(t0 + 0.4, 0.3)))
    tagline(im, tag); return im

def icongrid(n, groups, title="", tag="", big=None):
    """n icons (refineries); groups: [(count, colour, cue_i, label)] switch state in turn."""
    im = base(); d = D(im)
    if title: d.text((180, 56), title.upper(), fit(d, title.upper(), 34, 840), alpha(PAPER_HI, seg(0, 0.4)))
    cols = 10; sz = 64; x0 = (W - cols*sz*1.25)/2 + 40; y0 = 150
    state = [None]*n; k = 0
    for cnt, col, ci, lab in groups:
        for j in range(cnt):
            t0 = lead(c(ci), 0.5) + j*0.05
            if k < n: state[k] = (col, t0)
            k += 1
    for i in range(n):
        x = x0 + (i % cols)*sz*1.25; y = y0 + (i // cols)*sz*1.3; a = seg(0.03*i, 0.2)
        col = PAPER
        if state[i] and T >= state[i][1]: col = mix(PAPER, state[i][0], seg(state[i][1], 0.25))
        d.rect((x, y + 20, x + 18, y + sz), fill=alpha(col, a)); d.rect((x + 24, y + 6, x + 40, y + sz), fill=alpha(col, a))
        d.rect((x, y + sz - 12, x + 52, y + sz), fill=alpha(col, a))
    ly = y0 + 4*sz*1.3 + 30
    for j, (cnt, col, ci, lab) in enumerate(groups):
        d.rect((x0 + j*330, ly, x0 + j*330 + 26, ly + 26), fill=alpha(col, seg(lead(c(ci), 0.3), 0.3)))
        d.text((x0 + j*330 + 40, ly - 2), lab, f(26, "inter"), alpha(PAPER_HI, seg(lead(c(ci), 0.3), 0.3)))
    if big: d.text((W - 380, ly - 6), countup(big[0], ease_io((T - lead(c(big[1]), 1.0))/1.0)), f(54, "inter"), alpha(ORANGE, seg(lead(c(big[1]), 1.0), 0.3)))
    tagline(im, tag); return im

def split(left, right, tag=""):
    """two halves: (kicker, big, sub) each; right lands on cue 0."""
    im = base(); d = D(im)
    for side, (k_, big, sub) in enumerate((left, right)):
        t0 = 0.2 if side == 0 else lead(c(0), 0.4); a = seg(t0, 0.5)
        cx = W*0.3 if side == 0 else W*0.7
        center(d, 200, k_, f(34, "inter"), alpha(ORANGE, a), cx=cx)
        fb_ = fit(d, big, 88, W*0.4); center(d, 260 + (1-a)*20, big, fb_, alpha(PAPER_HI, a), cx=cx)
        bw_ = d.tl(big, fb_); pencil_underline(d, cx - bw_/2, cx + bw_/2, 262 + fb_.lsize + 14, t0 + 0.5, RED if side else ORANGE, seed=side + 31, w=5)
        for j, l in enumerate(wrap(d, sub, f(30, "serif"), W*0.36)[:3]): center(d, 380 + j*40, l, f(30, "serif"), alpha(PAPER, a), cx=cx)
    d.line([(W/2, 160 + (1-seg(0.1, 0.6))*400), (W/2, 560)], DIM, 3)
    tagline(im, tag); return im

def pricetags(items, tag="", title=""):
    """price tags flipping in: [(label, price, col, cue_i)]"""
    im = base(); d = D(im)
    if title: center(d, 70, title.upper(), f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    n = len(items)
    for i, (lab, price, col, ci) in enumerate(items):
        t0 = lead(c(ci), 0.4) if ci is not None else 0.3; k = seg(t0, 0.5)
        x = W/2 + (i - (n-1)/2) * 420; y = 200
        sq = abs(math.cos((1 - k) * math.pi / 2))
        w = 330 * sq
        if k > 0:
            d.poly([(x - w/2, y + 60), (x - w/2 + 40*sq, y), (x + w/2, y), (x + w/2, y + 300), (x - w/2 + 40*sq, y + 300), (x - w/2, y + 240)], fill=PAPER)
            d.ell((x - w/2 + 30*sq, y + 140, x - w/2 + 50*sq, y + 160), fill=INK)
            if sq > 0.6:
                center(d, y + 50, lab, f(28, "inter"), (60, 50, 40), cx=x + 20)
                center(d, y + 110, price, f(72, "inter"), col, cx=x + 20)
    tagline(im, tag); return im

def flap(rows, header="", tag="", hit_i=0, record=None):
    """split-flap price board: rows [(label, old, new)] flips old->new on cue hit_i."""
    im = base(); d = D(im)
    if header: center(d, 90, header.upper(), f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i, (lab, old, new) in enumerate(rows):
        y = 210 + i*170; t0 = lead(c(hit_i + i, 1.2 + i), 0.5)
        d.text((180, y + 24), lab, f(34, "inter"), alpha(PAPER, seg(0.1, 0.4)))
        txt = new if T >= t0 + 0.5 else old
        flick = (t0 <= T < t0 + 0.5)
        for j, ch in enumerate(txt):
            x = 620 + j*62
            d.rect((x, y, x + 56, y + 96), fill=(30, 28, 26)); d.line([(x, y + 48), (x + 56, y + 48)], (12, 12, 12), 2)
            show = ch if not flick else "0123456789"[int(T*30 + j) % 10] if ch.isdigit() else ch
            center(d, y + 10, show, f(70, "inter"), ORANGE if T >= t0 + 0.5 else PAPER_HI, cx=x + 28)
        if T >= t0 + 0.5 and (record is None or i in record): stamp(im, "RECORD", 620 + len(txt)*62 + 140, y + 48, t0 + 0.55, size=50, angle=-10)
        if T >= t0 + 0.5: pencil_underline(d, 620, 620 + len(txt)*62 - 6, y + 112, t0 + 0.6, ORANGE, seed=i + 151, w=4)
    tagline(im, tag); return im

def scenario(n, title, direction, tag="SCENARIO, NOT A FORECAST", ylab="DIESEL PRICE PRESSURE (SHAPE ILLUSTRATIVE)"):
    """scenario card with an arrow that holds (0), drifts down (-1) or spikes (+1)."""
    im = base(); d = D(im); a = seg(0, 0.4)
    d.text((180, 120), f"SCENARIO {n}", f(36, "bebas"), alpha(ORANGE, a))
    d.text((180, 170), title.upper(), f(64, "inter"), alpha(PAPER_HI, a))
    x0, x1, y0 = 220, W - 140, 470; hit = c(0, DUR*0.6)
    e = ease_io((T - 0.5) / max(0.8, hit - 0.5))
    pts = []
    for i in range(41):
        q = i / 40
        if q > e: break
        yy = y0 - 40*math.sin(q*9)*0.3 - (direction == 1)*(220*q**3) + (direction == -1)*(150*q) - (direction == 0)*10
        pts.append((x0 + (x1 - x0)*q, yy))
    col = CRIMSON if direction == 1 else (CYAN if direction == -1 else ORANGE)
    if len(pts) > 1: d.line(pts, col, 7)
    if pts:
        im = glow(im, lambda g: g.ell((pts[-1][0]-14, pts[-1][1]-14, pts[-1][0]+14, pts[-1][1]+14), fill=col + (255,)), 30, 1.0)
        d = D(im); d.ell((pts[-1][0]-9, pts[-1][1]-9, pts[-1][0]+9, pts[-1][1]+9), fill=col)
    d.text((x0, y0 + 130), ylab, f(20, "reg"), GREY)
    tagline(im, tag); return im

def lights_out(text, at=None, until=None):
    im = Image.new("RGB", (PW, PH), (6, 6, 6)); d = D(im); end = (until if until is not None else (sn(1) if at is not None and len(SENTS) > 1 else DUR))
    a = seg(at if at is not None else lead(c(0, 0.8), 0.6), 0.5 if at is not None else 1.0) * (1 - seg(end - 0.35, 0.3))
    center(d, H/2 - 40, text, f(62, "serif"), alpha(PAPER_HI, a))
    return im

def endcard(next_title="THE WINTER BILL", sub="Every crisis sends a bill. History keeps the receipts."):
    im = base(); d = D(im)
    center(d, 120, "THE HISTORY INVOICE", f(70, "inter"), alpha(PAPER_HI, seg(0.2, 0.8)))
    center(d, 210, sub, f(36, "serif"), alpha(ORANGE, seg(0.8, 0.8)))
    a = seg(lead(c(0, 1.5), 0.5), 0.5)
    d.rect((180, 330, 620, 578), fill=alpha((40, 37, 34), a), outline=alpha(ORANGE, a), width=3)
    center(d, 360, "WATCH NEXT", f(28, "inter"), alpha(ORANGE, a), cx=400); center(d, 420, next_title, fit(d, next_title, 46, 400), alpha(PAPER_HI, a), cx=400)
    b = seg(lead(c(1, 3.5), 0.5), 0.5)
    d.rrect((760, 410, 1100, 490), 12, fill=alpha(CRIMSON, b)); center(d, 428, "SUBSCRIBE", f(40, "inter"), alpha(PAPER_HI, b), cx=930)
    return im

# ---------------- maps (Web Mercator, terrain hillshade from AWS terrarium tiles + Natural Earth borders) ----------------
def merc(lon, lat):
    lat = max(-85, min(85, lat)); return lon, math.degrees(math.log(math.tan(math.pi/4 + math.radians(lat)/2)))
_SH = None
def shapes():
    global _SH
    if _SH is None:
        r = shapefile.Reader(str(A / "ne_50m_admin_0_countries.shp")); fl = [x[0] for x in r.fields[1:]]
        _SH = [(dict(zip(fl, rec.record)), rec.shape) for rec in r.shapeRecords()]
    return _SH
def _tile(z, x, y):
    p = CACHE / f"t{z}_{x}_{y}.png"
    if not p.exists():
        req = urllib.request.Request(f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png", headers={"User-Agent": "history-invoice/1.0"})
        tmp = p.with_suffix(".%d.tmp" % os.getpid()); tmp.write_bytes(urllib.request.urlopen(req, timeout=60).read()); os.replace(tmp, p)
    return Image.open(p).convert("RGB")
def hillshade(bbox, z):
    """returns an RGB hillshade image covering bbox (lon0, lat0, lon1, lat1) at PWxPH in Mercator, cached."""
    key = CACHE / ("hs_%s_%d_%d.png" % ("_".join(f"{v:.2f}" for v in bbox), z, PW))
    if key.exists():
        try: return Image.open(key).convert("RGB")
        except Exception: pass   # half-written by another worker: rebuild
    lon0, lat0, lon1, lat1 = bbox
    def tx(lon): return (lon + 180) / 360 * 2**z
    def ty(lat): r = math.radians(lat); return (1 - math.log(math.tan(r) + 1/math.cos(r)) / math.pi) / 2 * 2**z
    X0, X1 = int(tx(lon0)), int(tx(lon1)); Y0, Y1 = int(ty(lat1)), int(ty(lat0))
    mos = Image.new("RGB", ((X1 - X0 + 1)*256, (Y1 - Y0 + 1)*256))
    for x in range(X0, X1 + 1):
        for y in range(Y0, Y1 + 1):
            try: mos.paste(_tile(z, x % 2**z, y), ((x - X0)*256, (y - Y0)*256))
            except Exception: pass
    a = np.asarray(mos).astype(np.float32); el = a[..., 0]*256 + a[..., 1] + a[..., 2]/256 - 32768
    sea = el <= 0; el = np.maximum(el, 0)
    gy, gx = np.gradient(el); slope = np.arctan(np.hypot(gx, gy) / (40000000 / (256 * 2**z)) * 3.0)
    aspect = np.arctan2(-gx, gy); az, alt = math.radians(315), math.radians(40)
    shade = np.sin(alt)*np.cos(slope) + np.cos(alt)*np.sin(slope)*np.cos(az - aspect); shade = np.clip(shade, 0, 1)
    land = np.stack([34 + 70*shade, 32 + 64*shade, 29 + 56*shade], -1)
    water = np.stack([12 + 0*shade, 17 + 0*shade, 22 + 0*shade], -1)
    rgb = np.where(sea[..., None], water, land).astype(np.uint8)
    img = Image.fromarray(rgb)
    px0 = (tx(lon0) - X0) * 256; px1 = (tx(lon1) - X0) * 256; py0 = (ty(lat1) - Y0) * 256; py1 = (ty(lat0) - Y0) * 256
    img = img.crop((int(px0), int(py0), int(px1), int(py1))).resize((PW, PH), Image.BICUBIC)
    tmp = key.with_suffix(".%d.tmp.png" % os.getpid()); img.save(tmp); os.replace(tmp, key); return img
class Map:
    def __init__(s, bbox, z=6, hi=(), hi2=(), dim_others=False, terrain=True):
        s.bbox = bbox; s.hi = list(hi); s.hi2 = list(hi2)
        lon0, lat0, lon1, lat1 = bbox; s.mx0, s.my0 = merc(lon0, lat0); s.mx1, s.my1 = merc(lon1, lat1)
        key = (bbox, z, tuple(hi), tuple(hi2), terrain)
        if key not in _MAPS:
            im = hillshade(bbox, z) if terrain else Image.new("RGB", (PW, PH), (14, 18, 22))
            lay = Image.new("RGBA", (PW, PH), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay, "RGBA")
            lay2 = Image.new("RGBA", (PW, PH), (0, 0, 0, 0)); ld2 = ImageDraw.Draw(lay2, "RGBA")
            for rec, shp in shapes():
                name = rec.get("ADMIN") or rec.get("NAME"); pts = shp.points; parts = list(shp.parts) + [len(pts)]
                for a_, b_ in zip(parts[:-1], parts[1:]):
                    ring = [s.P(*p) for p in pts[a_:b_]]; ring = [(x*S, y*S) for x, y in ring]
                    if len(ring) < 3: continue
                    if not terrain: ld.polygon(ring, fill=LAND + (255,))
                    ld.line(ring + [ring[0]], fill=(150, 140, 125, 150), width=2)
                    raw = pts[a_:b_]; cx_ = sum(p[0] for p in raw)/len(raw); cy_ = sum(p[1] for p in raw)/len(raw)
                    if 32.3 < cx_ < 36.8 and 44.2 < cy_ < 46.3 and len(raw) > 20:
                        # Crimea: disputed. Never shade it as either country; dashed outline only.
                        for q in range(0, len(ring) - 1, 2): ld2.line([ring[q], ring[q+1]], fill=(200, 190, 175, 200), width=2)
                        continue
                    if name in s.hi: ld2.polygon(ring, fill=ORANGE + (95,)); ld2.line(ring + [ring[0]], fill=ORANGE + (255,), width=4)
                    elif name in s.hi2: ld2.polygon(ring, fill=RED + (80,)); ld2.line(ring + [ring[0]], fill=RED + (255,), width=3)
            base_ = Image.alpha_composite(im.convert("RGBA"), lay).convert("RGB")
            _MAPS[key] = (base_, lay2)
        s.base, s.hl = _MAPS[key]
    def P(s, lon, lat):
        mx, my = merc(lon, lat); return ((mx - s.mx0)/(s.mx1 - s.mx0)*W, (s.my1 - my)/(s.my1 - s.my0)*H)
    def frame(s, hl_t=0.4):
        im = s.base.copy(); a = seg(hl_t, 0.8)
        if a > 0 and (s.hi or s.hi2):
            hl = s.hl if a >= 1 else s.hl.copy()
            if a < 1: hl.putalpha(hl.getchannel("A").point(lambda v: int(v*a)))
            im.paste(hl, (0, 0), hl)
        return im
_MAPS = {}
def map_scene(bbox, z=6, hi=(), hi2=(), pins=(), lines=(), arcs=(), title="", tag="", measure=None, terrain=True, rings=(), labels=(), streams=None,
              push=0.05, glow_hi=False, nv=False, reticle=None, strips=None, shock=None):
    """pins: [(lon, lat, label, col, cue_i)], lines: [((lon,lat),(lon,lat), col, width, cue_i, dashed)], arcs: same but curved,
       rings: [(lon, lat, km, cue_i, label)], labels: [(lon, lat, text, size, col)], measure: ((lon,lat),(lon,lat),text,cue_i),
       streams: (src(lon,lat), [dst...], n, cue_i) moving dots (drone swarm).
       Round Two extras: push = slow push-in (G01), glow_hi = glowing borders (G11), nv = teal night-vision grade (G10),
       reticle = (lon, lat, cue_i, label) HUD reticle + shutter (G04), strips = (s1, s2, cue_i) Bebas label strips (G12),
       shock = (lon, lat, [(label, cue_i)]) seismic rings, active ring lit, earlier rings at 40% (G06)."""
    m = Map(bbox, z, hi, hi2, terrain=terrain); im = m.frame()
    if glow_hi and (hi or hi2):
        g = m.hl.filter(ImageFilter.GaussianBlur(14*S)); a = g.getchannel("A").point(lambda v: int(min(255, v*2.2*seg(0.4, 0.8))))
        im = ImageChops.add(im, ImageChops.multiply(g.convert("RGB"), Image.merge("RGB", (a, a, a))))
    if nv:
        g = np.asarray(im.convert("L")).astype(np.float32) / 255.0
        g = np.clip((g - 0.12) * 1.6, 0, 1) ** 1.5
        rgb = np.stack([4 + g*60, 14 + g*200, 16 + g*160], -1)
        rgb[::max(2, int(3*S))] *= 0.72   # scan lines
        im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
    d = D(im)
    for (lo, la, txt, sz, col) in labels: d.text(m.P(lo, la), txt, f(sz, "inter"), alpha(col, seg(0.3, 0.6)))
    for (lo, la, km, ci, lab) in rings:
        x, y = m.P(lo, la); x2, _ = m.P(lo + km/(111.0*math.cos(math.radians(la))), la); r = abs(x2 - x)
        k = seg(lead(c(ci), 0.8), 0.8)
        if k > 0:
            d.ell((x - r*k, y - r*k, x + r*k, y + r*k), outline=alpha(ORANGE, 0.85), width=3)
            if lab: d.text((x + r*k*0.71 + 8, y - r*k*0.71 - 30), lab, f(28, "inter"), alpha(ORANGE, k))
    def path(p0, p1, curved, k):
        (xa, ya), (xb, yb) = m.P(*p0), m.P(*p1); pts = []
        for i in range(int(40*k) + 1):
            q = i / 40
            bend = (math.hypot(xb - xa, yb - ya) * 0.18) if curved else 0
            pts.append((xa + (xb - xa)*q - (yb - ya)/max(1, math.hypot(xb-xa, yb-ya))*bend*math.sin(math.pi*q)*0,
                        ya + (yb - ya)*q - bend*math.sin(math.pi*q)))
        return pts
    for group, curved in ((lines, False), (arcs, True)):
        for (p0, p1, col, w, ci, dashed) in group:
            t0 = lead(c(ci), 0.7) if ci is not None else 0.6; k = seg(t0, 1.0)
            if k <= 0: continue
            pts = path(p0, p1, curved, k)
            if dashed:
                for i in range(0, len(pts) - 1, 2): d.line([pts[i], pts[i+1]], col, w)
            elif len(pts) > 1: d.line(pts, col, w)
            if len(pts) > 1 and k < 1: d.ell((pts[-1][0]-6, pts[-1][1]-6, pts[-1][0]+6, pts[-1][1]+6), fill=PAPER_HI)
    if streams:
        src, dsts, nd, ci = streams; t0 = lead(c(ci), 2.0); xs, ys = m.P(*src)
        rng = np.random.default_rng(11)
        for i in range(nd):
            dst = dsts[i % len(dsts)]; xd, yd = m.P(*dst); ph = rng.random(); sp = 0.25 + 0.2*rng.random(); jit = rng.normal(0, 18, 2)
            q = ((T - t0)*sp + ph) % 1.0 if T > t0 + ph/sp*0 else 0
            if T < t0 + ph*1.5: continue
            x = xs + (xd - xs)*q + jit[0]; y = ys + (yd - ys)*q + jit[1] - 30*math.sin(math.pi*q)
            d.ell((x-2.5, y-2.5, x+2.5, y+2.5), fill=alpha(ORANGE, 0.9))
    for j, (lo, la, txt, col, ci) in enumerate(pins):
        x, y = m.P(lo, la); t0 = lead(c(ci), 0.25) if ci is not None else 0.3 + 0.12*j; e = seg(t0, 0.35)
        if e <= 0: continue
        d.ell((x - 9*e, y - 9*e, x + 9*e, y + 9*e), fill=col, outline=(20, 18, 16), width=2); pulse_rings(d, x, y, col, t0, 2, 40)
        if txt: d.text((x + 16, y - 16), txt, f(26, "inter"), alpha(PAPER_HI, e))
        if ci is not None and ci >= 0:   # the spoken place gets circled by hand, its name underlined
            pencil_circle(d, x, y, 30, 26, t0 + 0.3, col if col != PAPER_HI else ORANGE, seed=j + 61, w=4, dur=0.5)
            if txt: pencil_underline(d, x + 16, x + 16 + d.tl(txt, f(26, "inter")), y + 16, t0 + 0.6, PENCIL, seed=j + 71, w=3, dur=0.35)
    if measure:
        p0, p1, txt, ci = measure; (xa, ya), (xb, yb) = m.P(*p0), m.P(*p1); t0 = lead(c(ci), 0.6); k = seg(t0, 0.7)
        if k > 0:
            d.line([(xa, ya), (xa + (xb - xa)*k, ya + (yb - ya)*k)], PAPER_HI, 4)
            for (x, y) in ((xa, ya), (xa + (xb - xa)*k, ya + (yb - ya)*k)): d.line([(x - 8, y - 8), (x + 8, y + 8)], PAPER_HI, 3)
            d.text(((xa + xb)/2 + 20, (ya + yb)/2 - 60), txt, f(40, "bebas"), alpha(PAPER_HI, seg(t0 + 0.5, 0.3)))
            if k >= 1: pencil_underline(d, (xa + xb)/2 + 20, (xa + xb)/2 + 20 + d.tl(txt, f(40, "bebas")), (ya + yb)/2 - 14, t0 + 0.8, ORANGE, seed=91, w=4)
    if shock:
        lo, la, rl = shock; x, y = m.P(lo, la); n = len(rl)
        for i, (lab, ci) in enumerate(rl):
            t0 = lead(c(ci), 0.5); k = seg(t0, 0.9)
            if k <= 0: continue
            nxt = lead(c(rl[i+1][1]), 0.5) if i + 1 < n else 1e9
            lit = 1.0 if T < nxt else 0.4; r = (80 + 75*i) * ease_io(k)
            d.ell((x - r, y - r*0.8, x + r, y + r*0.8), outline=alpha(ORANGE if lit == 1 else PAPER, 0.9*lit), width=4 if lit == 1 else 2)
            fo = f(44 if lit == 1 else 30, "bebas"); lx, ly = x + r*0.72 + 12, y - r*0.8*0.72 - 34
            d.text((lx, ly), lab, fo, alpha(PAPER_HI if lit == 1 else PAPER, lit*seg(t0 + 0.3, 0.3)))
            if lit == 1: pencil_underline(d, lx, lx + d.tl(lab, fo), ly + fo.lsize + 6, t0 + 0.6, ORANGE, seed=i + 101, w=4)
    if push and push > 0:   # slow push-in toward the frame centre (G01)
        z_ = 1 + push * ease_io(T / max(1.0, DUR))
        if z_ > 1.0005:
            cw_, ch_ = PW / z_, PH / z_; im = im.crop((int((PW - cw_)/2), int((PH - ch_)/2), int((PW + cw_)/2), int((PH + ch_)/2))).resize((PW, PH), Image.BILINEAR)
            d = D(im)
    if reticle:
        lo, la, ci, lab = reticle; x, y = m.P(lo, la); z_ = 1 + (push or 0) * ease_io(T / max(1.0, DUR)); x = W/2 + (x - W/2)*z_; y = H/2 + (y - H/2)*z_
        t0 = lead(c(ci), 0.6); k = seg(t0, 0.6)
        if k > 0:
            r = 150 - 80*ease_io(k); L = 34
            for sx in (-1, 1):
                for sy in (-1, 1):
                    cx_, cy_ = x + sx*r, y + sy*r; d.line([(cx_, cy_), (cx_ - sx*L, cy_)], PAPER_HI, 4); d.line([(cx_, cy_), (cx_, cy_ - sy*L)], PAPER_HI, 4)
            d.line([(x - 14, y), (x + 14, y)], RED, 3); d.line([(x, y - 14), (x, y + 14)], RED, 3)
            d.text((x - r - 14 - d.tl(lab, f(28, "inter")), y + r - 30), lab, f(28, "inter"), alpha(PAPER_HI, seg(t0 + 0.6, 0.3)))
            d.text((60, 120), "REC ● " + "%02d:%02d" % (int(T)//60, int(T) % 60), f(22, "inter"), alpha(RED, k))
            fl = 1 - seg(t0 + 0.6, 0.12) if T >= t0 + 0.6 else 0   # shutter flash as the reticle locks
            if fl > 0: d.rect((0, 0, W, H), fill=(255, 250, 240, int(150*fl)))
    if strips:
        s1, s2, ci = strips[:3]; sy = strips[3] if len(strips) > 3 else H - 250; t0 = lead(c(ci), 0.4)
        for j, txt in enumerate((s1, s2)):
            k = ease_io((T - t0 - 0.35*j) / 0.45)
            if k <= 0: continue
            fo = f(56, "bebas"); tw = d.tl(txt, fo) + 50; y0 = sy + j*86; x0 = -tw + (tw + 60)*k
            d.rect((x0, y0, x0 + tw, y0 + 72), fill=(CRIMSON if j == 0 else (24, 22, 20)) + (235,)); d.text((x0 + 25, y0 + 8), txt, fo, PAPER_HI)
    if nv: d.text((W - 300, 120), "ILLUSTRATION · NV GRADE", f(18, "inter"), alpha((120, 230, 200), 0.8))
    if title:
        d.rect((0, 0, W, 96), fill=(0, 0, 0, 120)); d.text((60, 30), title.upper(), fit(d, title.upper(), 36, 940), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, tag); return im

# ---------------- corner invoice (running, one line per part) ----------------
CORNER = []   # list of lines already printed; renderer sets per part
def corner(im, lines, new_at=None):
    if not lines: return im
    d = D(im); x0, y0 = W - 250, 16; h = 28 + 19*len(lines)
    d.rect((x0, y0, W - 16, y0 + h), fill=(214, 204, 186, 205))
    d.text((x0 + 10, y0 + 5), "YOUR INVOICE", f(14, "inter"), (120, 40, 20))
    for i, l in enumerate(lines):
        a = 1.0 if (new_at is None or i < len(lines) - 1) else seg(new_at, 0.3)
        d.text((x0 + 10, y0 + 24 + i*19), l, fit(d, l, 14, 214, "reg"), alpha(INK, a))
    return im

# ---------------- Round Two set, part 2 (INV-002 G13 globe, G21 stacked bar, G22 diverging bars, G23 three stats) ----------------
_GLOBE = {}
def _globe_rings():
    if "r" not in _GLOBE:
        out = []
        for rec, shp in shapes():
            name = rec.get("ADMIN") or rec.get("NAME"); pts = shp.points; parts = list(shp.parts) + [len(pts)]
            for a_, b_ in zip(parts[:-1], parts[1:]):
                ring = pts[a_:b_][::3] if b_ - a_ > 60 else pts[a_:b_]
                if len(ring) >= 3: out.append((name, np.radians(np.array(ring))))
        _GLOBE["r"] = out
    return _GLOBE["r"]
def globe(center, arcs=(), hi=(), title="", tag="", spin=6.0, R=300):
    """orthographic globe that turns slowly; arcs: [((lon,lat) src, (lon,lat) dst, label, cue_i)] draw on their cue with a moving pulse."""
    im = base(); d = D(im); cx, cy = W/2 - 60, H/2 + 30
    lon0 = math.radians(center[0] - spin/2 + spin*min(1, T/max(1, DUR))); lat0 = math.radians(center[1])
    def P(lon, lat):
        cosc = math.sin(lat0)*np.sin(lat) + math.cos(lat0)*np.cos(lat)*np.cos(lon - lon0)
        x = np.cos(lat)*np.sin(lon - lon0); y = math.cos(lat0)*np.sin(lat) - math.sin(lat0)*np.cos(lat)*np.cos(lon - lon0)
        return cx + R*x, cy - R*y, cosc
    a = seg(0, 0.6)
    im = glow(im, lambda g: g.ell((cx - R, cy - R, cx + R, cy + R), fill=(0, 120, 160, 120)), 40, 0.6); d = D(im)
    d.ell((cx - R, cy - R, cx + R, cy + R), fill=alpha((14, 20, 26), a), outline=alpha((70, 110, 130), a), width=2)
    for name, ring in _globe_rings():
        X, Y, V = P(ring[:, 0], ring[:, 1])
        if (V > 0).sum() < 3: continue
        pts = [(x, y) for x, y, v in zip(X, Y, V) if v > 0]
        fill = ORANGE + (170,) if name in hi else (48, 46, 42, int(255*a))
        if len(pts) >= 3: d.poly(pts, fill=fill); d.line(pts + [pts[0]], (110, 104, 96, int(200*a)), 1)
    for j, (src, dst, lab, ci) in enumerate(arcs):
        t0 = lead(c(ci), 0.6) if ci is not None else 0.6 + 0.3*j; k = seg(t0, 0.9)
        if k <= 0: continue
        l1, p1, l2, p2 = map(math.radians, (src[0], src[1], dst[0], dst[1]))
        v1 = np.array([math.cos(p1)*math.cos(l1), math.cos(p1)*math.sin(l1), math.sin(p1)]); v2 = np.array([math.cos(p2)*math.cos(l2), math.cos(p2)*math.sin(l2), math.sin(p2)])
        om = math.acos(max(-1, min(1, float(v1 @ v2)))); pts = []
        for i in range(int(48*k) + 1):
            q = i/48; v = (math.sin((1-q)*om)*v1 + math.sin(q*om)*v2) / max(1e-6, math.sin(om)); v = v * (1 + 0.12*math.sin(math.pi*q))
            lon, lat = math.atan2(v[1], v[0]), math.asin(v[2]/np.linalg.norm(v)); x, y, vis = P(lon, lat); sc = np.linalg.norm(v)
            if vis > -0.05: pts.append((cx + (x - cx)*sc, cy + (y - cy)*sc))
        if len(pts) > 1:
            d.line(pts, ORANGE, 4)
            if k < 1: d.ell((pts[-1][0]-7, pts[-1][1]-7, pts[-1][0]+7, pts[-1][1]+7), fill=PAPER_HI)
            else:
                q = ((T - t0) * 0.6) % 1.0; px, py = pts[min(len(pts)-1, int(q*(len(pts)-1)))]; d.ell((px-5, py-5, px+5, py+5), fill=PAPER_HI)
        if k >= 1 and lab and pts:   # label in its own slot right of the globe, joined by a hand-drawn leader
            ex, ey = pts[-1]; lx, ly = cx + R + 40, cy - R + 40 + j*62; kk = seg(t0 + 0.8, 0.3)
            pencil(d, [(ex, ey), (lx - 10, ly + 18)], t0 + 0.8, 0.3, (200, 190, 175), 2, seed=j + 111, passes=1)
            d.text((lx, ly), lab, f(28, "inter"), alpha(PAPER_HI, kk))
            pencil_underline(d, lx, lx + d.tl(lab, f(28, "inter")), ly + 36, t0 + 1.0, ORANGE, seed=j + 121, w=3, dur=0.3)
    if title: d.text((70, 60), title.upper(), fit(d, title.upper(), 34, 760), alpha(PAPER_HI, seg(0, 0.4)))
    tagline(im, tag); return im

def stats3(items, title="", tag=""):
    """three big stats in a row (G23): [(big, small, cue_i)] each counts up on its word, then gets underlined."""
    im = base(); d = D(im)
    if title: center(d, 90, title.upper(), fit(d, title.upper(), 34, 900), alpha(ORANGE, seg(0, 0.4)))
    n = len(items); gw = (W - 200) / n
    for i, (big, small, ci) in enumerate(items):
        t0 = lead(c(ci, sn(i) + 0.4), 0.9); e = ease_io((T - t0) / 0.9); cx = 100 + gw*i + gw/2
        if e <= 0: continue
        fo = fit(d, big, 92, gw - 40); center(d, 250 + (1-e)*20, countup(big, e) if len(re.findall(r"\d[\d,]*", big)) == 1 and "IN" not in big else big, fo, alpha(PAPER_HI, min(1, e*3)), cx=cx)
        bw_ = d.tl(big, fo); pencil_underline(d, cx - bw_/2, cx + bw_/2, 262 + fo.lsize + 10, t0 + 1.0, RED if i == n-1 else ORANGE, seed=i + 131, w=5)
        for j, l in enumerate(wrap(d, small, f(28, "serif"), gw - 50)[:3]): center(d, 400 + j*38, l, f(28, "serif"), alpha(PAPER, seg(t0 + 0.6, 0.4)), cx=cx)
        if i: d.line([(100 + gw*i, 230 + (1-seg(t0, 0.5))*200), (100 + gw*i, 520)], DIM, 2)
    tagline(im, tag); return im

def stacked(segments, title="", total="", tag=""):
    """horizontal stacked bar (G21): segments [(label, value, colour, cue_i)] grow one after another; total label on the end."""
    im = base(); d = D(im)
    if title: d.text((180, 70), title.upper(), fit(d, title.upper(), 34, 900), alpha(PAPER_HI, seg(0, 0.4)))
    tot = sum(v for _, v, _, _ in segments) or 1; x0, x1, y0, y1 = 180, W - 140, 290, 400; x = x0
    k0 = seg(0.2, 0.8); d.rect((x0, y0, x0 + (x1 - x0)*k0, y1), outline=alpha(DIM, 1), width=2)   # empty frame draws itself first
    for i, (lab, v, col, ci) in enumerate(segments):
        t0 = lead(c(ci, sn(i) + 0.3), 0.7); e = ease_io((T - t0) / 0.8); wseg = (x1 - x0) * v / tot
        if e > 0:
            d.rect((x, y0, x + wseg*e, y1), fill=col, outline=(20, 18, 16), width=2)
            if e >= 1:
                tl_ = wrap(d, lab, f(26, "inter"), max(160, wseg - 10))
                for j, l in enumerate(tl_[:2]): d.text((x + 12, y1 + 22 + j*32), l, f(26, "inter"), alpha(col if col != DIM else PAPER, seg(t0 + 0.8, 0.3)))
                pencil(d, [(x + 4, y0 - 18), (x + 4, y0 - 32), (x + wseg - 4, y0 - 32), (x + wseg - 4, y0 - 18)], t0 + 0.9, 0.4, PENCIL, 3, seed=i + 141)   # hand-drawn bracket
        x += wseg
    if total:
        t0 = lead(c(0, 0.8), 0.3); center(d, 180, total, f(70, "inter"), alpha(ORANGE, seg(t0, 0.4)), cx=(x0 + x1)/2)
    tagline(im, tag); return im

def diverging(items, title="", tag="", unit="%", span=25):
    """diverging bars around a zero line (G22): [(label, value, cue_i, valtxt)]; negatives grow left in red, positives right in green."""
    im = base(); d = D(im)
    if title: d.text((180, 60), title.upper(), fit(d, title.upper(), 34, 900), alpha(PAPER_HI, seg(0, 0.4)))
    zx = W/2 + 120; k0 = seg(0.1, 0.5); d.line([(zx, 150), (zx, 150 + 420*k0)], PAPER, 3); d.text((zx - 8, 120), "0", f(24, "inter"), alpha(PAPER, k0))
    for i, (lab, v, ci, vt) in enumerate(items):
        y = 190 + i*150; t0 = lead(c(ci, sn(i) + 0.3), 0.7); e = ease_io((T - t0) / 0.8)
        d.text((zx - 600, y - 42), lab, fit(d, lab, 28, 700, "inter"), alpha(PAPER_HI, seg(0.2 + 0.2*i, 0.4)))
        if e <= 0: continue
        L = 320 * min(1, abs(v) / span) * e; col = RED if v < 0 else GREEN
        if v is not None and v != 0:
            (d.rect((zx - L, y, zx, y + 70), fill=col) if v < 0 else d.rect((zx, y, zx + L, y + 70), fill=col))
        else:   # change known in direction only: hatched, open-ended bar
            for q in range(0, int(220*e), 18): d.line([(zx - q, y + 70), (zx - q - 18, y)], RED, 3)
        txt = vt if vt else (f"{v:+g}{unit}")
        tx = zx - L - 20 - d.tl(txt, f(40, "inter")) if (v or -1) < 0 else zx + L + 20
        if v == 0 or v is None: tx = zx - 240 - d.tl(txt, f(30, "inter"))
        d.text((tx, y + 12), txt, f(40 if v else 30, "inter"), alpha(PAPER_HI, seg(t0 + 0.7, 0.3)))
    tagline(im, tag); return im
