# INV-011 animation engine ("Round Two" look, animated, synced to the narration).
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
    def text(s, xy, t, font, fill, anchor=None): s.d.text((xy[0]*S, xy[1]*S), t, font=font, fill=fill, anchor=anchor)
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
        for i in range(40): vd.rectangle([i*3, i*2, PW//4 - i*3, PH//4 - i*2], fill=int(i*6.3))
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
    center(d, 205, countup(big, e) if not strike else big, fb, alpha(PAPER_HI, min(1, e*4) if not strike else seg(0, 0.4)))
    if strike:
        w = d.tl(big, fb); x0 = (W - w)/2; k = seg(hit - 0.2, 0.35)
        if k > 0: d.line([(x0-10, 300), (x0-10 + (w+20)*k, 290 - 26*k)], fill=CRIMSON, width=11)
        center(d, 400, strike, f(130, "inter"), alpha(ORANGE, seg(hit, 0.4)))
    if sub:
        a = seg(hit + 0.2, 0.5)
        for i, l in enumerate(wrap(d, sub, f(42, "serif"), W - 220)[:2]): center(d, (430 if not strike else 560) + i*54, l, f(42, "serif"), alpha(ORANGE, a))
    if badge: stamp(im, badge, W - 250, 140, hit + 0.4, col=ORANGE, size=64, angle=-6)
    im = sweep(im, (0, 200, W, 380), hit + 0.1, 1.2)
    tagline(im, tag); return im

def quote(q, who, when, tag="", cue=0):
    im = base(); d = paper(im, (190, 130, W-190, H-150), seed=3); hit = c(cue, 0.8)
    a = seg(0.1, 0.5)
    center(d, 160, "“", f(180, "serif"), alpha(ORANGE, a))
    y = 300 - 40
    qf = f(110 if len(q) < 20 else 60, "serif"); y = 280 if len(q) < 20 else 260
    for l in wrap(d, q, qf, W - 480): center(d, y, l, qf, alpha((30, 26, 22), seg(lead(hit, 0.4), 0.5))); y += qf.lsize + 12
    center(d, y + 20, f"{who} · {when}", f(28, "inter"), alpha((90, 60, 40), seg(hit + 0.3, 0.5)))
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
    if stamp_txt: stamp(im, stamp_txt, W/2, min(H-120, y + 80), c(len(lines) if cues is None else cues[-1], sn(len(lines))) + 0.2)
    tagline(im, tag); return im

def typed(lines, label="FILE", tag="", stamps=(), cue_lines=None):
    """index cards typed in turn (Round Two typewriter G08), optional stamps [(text, at_time)]."""
    im = base(); d = D(im); n = len(lines)
    for i, l in enumerate(lines):
        t0 = c(cue_lines[i]) - 0.6 if cue_lines else sn(i) + 0.1
        a = seg(t0 - 0.3, 0.4)
        if a <= 0: continue
        x0 = 170 + i*40; y0 = 120 + i*150
        dd = paper(im, (x0, y0 + (1-a)*30, x0 + 760, y0 + 120 + (1-a)*30), seed=i+5)
        dd.text((x0 + 24, y0 + 14), label, f(18, "inter"), (150, 60, 40))
        typewriter(dd, (x0 + 24, y0 + 48), l, f(40, "inter"), (30, 26, 22), t0, 30)
    for txt, at in stamps: stamp(im, txt, W - 260, H - 170, at)
    tagline(im, tag); return im

def headline(outlet, text, date, stamp_txt=None, tag=""):
    im = base(); dx = (1 - seg(0, 0.5)) * W
    d = paper(im, (150+dx, 110, W-150+dx, H-150), col=(226, 220, 208), seed=7)
    d.text((190+dx, 140), outlet.upper(), f(34, "inter"), INK); d.text((W-190-d.tl(date, f(26, "reg"))+dx, 146), date, f(26, "reg"), (90, 90, 90))
    d.line([(190+dx, 196), (W-190+dx, 196)], INK, 3)
    y = 224
    for i, l in enumerate(wrap(d, text, f(56, "inter"), W - 380)):
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
        y += 50
    if final_stamp: stamp(im, final_stamp, W/2 + 120, H - 150, c(len(lines) - show, sn(1)) + 0.4, size=84)
    tagline(im, tag); return im

def bars(items, title="", unit="", hi=None, tag="", cues=None, fmt="{:,.0f}", log=False):
    im = base(); d = D(im)
    if title: d.text((180, 60), title.upper(), f(36, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    vals = [v for _, v in items]; mx = max(vals) or 1
    n = len(items); bw = min(220, (W - 340) // n - 40); gap = ((W - 300) - n*bw) // max(1, n)
    for i, (lab, v) in enumerate(items):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i) + 0.3) - 0.5
        e = ease_io((T - t0) / 0.9)
        x = 200 + i*(bw+gap) + gap//2
        frac = (math.log10(max(v, 1)) / math.log10(mx)) if log else v / mx
        h = int(430 * frac * e); y = H - 150 - h
        col = ORANGE if (hi is None or i == hi) else (96, 88, 80)
        if h > 0: d.rect((x, y, x+bw, H-150), fill=col)
        val = fmt.format(v*e) + unit; tw = d.tl(val, f(38, "inter"))
        d.text((x + (bw-tw)/2, y - 50), val, f(38, "inter"), alpha(PAPER_HI, min(1, e*4)))
        for j, l in enumerate(wrap(d, lab, f(24, "reg"), bw + 60)[:2]):
            tw = d.tl(l, f(24, "reg")); d.text((x + (bw-tw)/2, H - 138 + j*28), l, f(24, "reg"), alpha(PAPER, seg(0.1, 0.4)))
    tagline(im, tag); return im

def linechart(series, title="", marks=(), tag="", unit="", band=None, hit=None, ylab_fmt="{:g}"):
    """series: {name: [(label, value), ...]}; the line draws up to the hit word; marks: [(text, idx, series_idx)]."""
    im = base(); d = D(im)
    if title: d.text((180, 52), title.upper(), f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
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
    if sub: center(d, cy + 274, sub, f(34, "serif"), alpha(ORANGE, seg(hit + 0.3, 0.5)))
    if stamp_txt: stamp(im, stamp_txt, cx + 300, cy - 180, hit + 0.5, size=72)
    im = glow(im, lambda g: g.arc((cx-r, cy-r, cx+r, cy+r), 135, a1, fill=(232, 89, 12, 200), width=40), 26, 0.8) if e > 0 else im
    tagline(im, tag); return im

def tiles(items, title="", tag="", cues=None):
    """option / scenario tiles lighting in turn. items: [(big, small)]"""
    im = base(); d = D(im); n = len(items)
    if title: center(d, 70, title.upper(), f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    tw = (W - 240 - (n-1)*30) / n
    for i, (big, small) in enumerate(items):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i)) - 0.3; a = seg(t0, 0.45); lit = seg(t0, 0.2) * (1 - 0.6*seg((c(cues[i+1]) if cues and i+1 < len(cues) else sn(i+1)) - 0.3, 0.4) if i < n-1 else 1)
        x = 120 + i*(tw + 30); y = 220 + (1-a)*30
        d.rect((x, y, x+tw, y+300), fill=alpha(mix((40, 38, 35), (70, 40, 26), lit), a), outline=alpha(ORANGE, a*lit), width=3)
        for j, l in enumerate(wrap(d, big, f(46, "inter"), tw - 40)): center(d, y + 70 + j*56, l, f(46, "inter"), alpha(PAPER_HI, a), cx=x + tw/2)
        for j, l in enumerate(wrap(d, small, f(24, "reg"), tw - 40)[:3]): center(d, y + 210 + j*30, l, f(24, "reg"), alpha(PAPER, a), cx=x + tw/2)
    tagline(im, tag); return im

def timeline(events, active, title="", tag="", stamp_txt=None):
    """dated nodes; nodes up to `active` light (earlier ones dim to 40%), the active ones on their cue."""
    im = base(); d = D(im); n = len(events)
    if title: d.text((180, 70), title.upper(), f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
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
        if i in active: pulse_rings(d, x, y, col, lead(c(active.index(i)), 0.3), 2, 36)
    if stamp_txt: stamp(im, stamp_txt, W - 330, 170, c(len(active), c(0) + 1.2))
    tagline(im, tag); return im

def calendar(months, circles=(), flames_every=None, stamps=(), title="", tag=""):
    """month strip; circles: [(month_idx, label, cue_i)] red pen circles; stamps: [(month_idx, text, cue_i)]; flames_every: n days."""
    im = base(); d = D(im)
    if title: d.text((180, 56), title.upper(), f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    n = len(months); cw = (W - 260) / n
    for i, m in enumerate(months):
        x = 200 + i*cw; a = seg(0.05*i, 0.3)
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
    for (mi, lab, ci) in circles:
        x = 200 + mi*cw + cw/2; t0 = lead(c(ci), 0.3); k = seg(t0, 0.5)
        if k > 0:
            d.arc((x - cw*0.46, 230, x + cw*0.46, 440), -90, -90 + 360*k, fill=RED, width=7)
            center(d, 470, lab, f(30, "inter"), alpha(RED, seg(t0 + 0.4, 0.3)), cx=x)
    for (mi, txt, ci) in stamps: stamp(im, txt, 200 + mi*cw + cw/2, 360, c(ci), size=58, angle=-12)
    tagline(im, tag); return im

def chain(steps, title="", tag="", cues=None):
    im = base(); d = D(im); n = len(steps)
    if title: center(d, 80, title.upper(), f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    gap = (W - 260) / n
    for i, s in enumerate(steps):
        t0 = (c(cues[i]) if cues and i < len(cues) else sn(i)) - 0.25; a = seg(t0, 0.4)
        x = 160 + i*gap + gap/2; y = 360
        d.ell((x-70, y-70, x+70, y+70), fill=alpha((44, 40, 36), a), outline=alpha(ORANGE, a), width=4)
        center(d, y - 20, s.upper(), f(26 if len(s) > 7 else 32, "inter"), alpha(PAPER_HI, a), cx=x)
        if i < n - 1:
            k = seg(t0 + 0.3, 0.4); xa = x + 76; xb = x + gap - 76
            if k > 0: d.line([(xa, y), (xa + (xb - xa)*k, y)], ORANGE, 4)
        pulse_rings(d, x, y, ORANGE, t0, 1, 90, 0.4)
    tagline(im, tag); return im

def flow(nodes, arrows, title="", tag="", cues=None):
    """box-and-arrow diagram. nodes: {key: (x, y, label, col)}, arrows: [(a, b, label, cue_i)]"""
    im = base(); d = D(im)
    if title: d.text((180, 56), title.upper(), f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
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
    if title: d.text((180, 56), title.upper(), f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
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
        center(d, 260 + (1-a)*20, big, f(88, "inter"), alpha(PAPER_HI, a), cx=cx)
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

def flap(rows, header="", tag="", hit_i=0):
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
        if T >= t0 + 0.5: stamp(im, "RECORD", 620 + len(txt)*62 + 140, y + 48, t0 + 0.55, size=50, angle=-10)
    tagline(im, tag); return im

def scenario(n, title, direction, tag="SCENARIO, NOT A FORECAST"):
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
    d.text((x0, y0 + 130), "DIESEL PRICE PRESSURE (SHAPE ILLUSTRATIVE)", f(20, "reg"), GREY)
    tagline(im, tag); return im

def lights_out(text):
    im = Image.new("RGB", (PW, PH), (6, 6, 6)); d = D(im)
    a = seg(lead(c(0, 0.8), 0.6), 1.0) * (1 - seg(DUR - 0.6, 0.5))
    center(d, H/2 - 40, text, f(62, "serif"), alpha(PAPER_HI, a))
    return im

def endcard(next_title="THE WINTER BILL", sub="Every crisis sends a bill. History keeps the receipts."):
    im = base(); d = D(im)
    center(d, 120, "THE HISTORY INVOICE", f(70, "inter"), alpha(PAPER_HI, seg(0.2, 0.8)))
    center(d, 210, sub, f(36, "serif"), alpha(ORANGE, seg(0.8, 0.8)))
    a = seg(lead(c(0, 1.5), 0.5), 0.5)
    d.rect((180, 330, 620, 578), fill=alpha((40, 37, 34), a), outline=alpha(ORANGE, a), width=3)
    center(d, 360, "WATCH NEXT", f(28, "inter"), alpha(ORANGE, a), cx=400); center(d, 420, next_title, f(46, "inter"), alpha(PAPER_HI, a), cx=400)
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
        p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return Image.open(p).convert("RGB")
def hillshade(bbox, z):
    """returns an RGB hillshade image covering bbox (lon0, lat0, lon1, lat1) at PWxPH in Mercator, cached."""
    key = CACHE / ("hs_%s_%d_%d.png" % ("_".join(f"{v:.2f}" for v in bbox), z, PW))
    if key.exists(): return Image.open(key).convert("RGB")
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
    img.save(key); return img
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
def map_scene(bbox, z=6, hi=(), hi2=(), pins=(), lines=(), arcs=(), title="", tag="", measure=None, terrain=True, rings=(), labels=(), streams=None):
    """pins: [(lon, lat, label, col, cue_i)], lines: [((lon,lat),(lon,lat), col, width, cue_i, dashed)], arcs: same but curved,
       rings: [(lon, lat, km, cue_i, label)], labels: [(lon, lat, text, size, col)], measure: ((lon,lat),(lon,lat),text,cue_i),
       streams: (src(lon,lat), [dst...], n, cue_i) moving dots (drone swarm)."""
    m = Map(bbox, z, hi, hi2, terrain=terrain); im = m.frame(); d = D(im)
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
    if measure:
        p0, p1, txt, ci = measure; (xa, ya), (xb, yb) = m.P(*p0), m.P(*p1); t0 = lead(c(ci), 0.6); k = seg(t0, 0.7)
        if k > 0:
            d.line([(xa, ya), (xa + (xb - xa)*k, ya + (yb - ya)*k)], PAPER_HI, 4)
            for (x, y) in ((xa, ya), (xa + (xb - xa)*k, ya + (yb - ya)*k)): d.line([(x - 8, y - 8), (x + 8, y + 8)], PAPER_HI, 3)
            d.text(((xa + xb)/2 + 20, (ya + yb)/2 - 60), txt, f(40, "bebas"), alpha(PAPER_HI, seg(t0 + 0.5, 0.3)))
    if title:
        d.rect((0, 0, W, 96), fill=(0, 0, 0, 120)); d.text((60, 30), title.upper(), f(36, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, tag); return im

# ---------------- corner invoice (running, one line per part) ----------------
CORNER = []   # list of lines already printed; renderer sets per part
def corner(im, lines, new_at=None):
    if not lines: return im
    d = D(im); x0, y0 = W - 300, 20; h = 34 + 24*len(lines)
    d.rect((x0, y0, W - 20, y0 + h), fill=(214, 204, 186, 215))
    d.text((x0 + 12, y0 + 6), "YOUR INVOICE", f(16, "inter"), (120, 40, 20))
    for i, l in enumerate(lines):
        a = 1.0 if (new_at is None or i < len(lines) - 1) else seg(new_at, 0.3)
        d.text((x0 + 12, y0 + 28 + i*24), l, f(16, "reg"), alpha(INK, a))
    return im
