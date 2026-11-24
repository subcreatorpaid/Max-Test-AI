# INV-017 graphics spec: script code -> lambda(on_screen, tag) -> PIL frame (anim12 globals T, CUES, SENTS).
# Main channel look (Round Two / INV-011 / INV-012): dark ledger, beige paper, Inter + Caladea + Bebas, everything animated on the word.
# New for this video: a space set (orbit shells, satellite swarms that die, radiation belt, sky flash, streetlights, EMP trace).
import sys, pathlib, math
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "inv012"))
from anim12 import *
import anim12 as _A
from anim12 import _globe_rings
_quote12 = quote
def quote(q, who, when, tag="", cue=0):
    """INV-017 review: words appear early (by 1.5 s) instead of waiting on the cue word, so the paper is never empty."""
    save = _A.CUES
    try:
        _A.CUES = [min(save[cue] if len(save) > cue else 1.5, 1.5)]
        return _quote12(q, who, when, tag=tag, cue=0)
    finally:
        _A.CUES = save
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

MOSCOW = (37.62, 55.75); JOHNSTON = (-169.53, 16.73); HONOLULU = (-157.86, 21.31); KAUAI = (-159.5, 22.05); SAMOA = (-171.8, -13.8)
ZHEZ = (67.7, 47.8); KARAG = (73.1, 49.8); ASTANA = (71.4, 51.2); ALMATY = (76.9, 43.25); BERLIN = (13.4, 52.52)
PACIFIC = (-178.0, -20.0, -150.0, 28.0); HAWAII = (-160.8, 18.6, -154.6, 22.6); KAZ = (46.0, 40.0, 87.0, 55.5); WRUS = (18.0, 46.0, 62.0, 62.0)
SKY = (8, 12, 20); BELT = (120, 255, 170)

# ---------------- space set ----------------
def earth(im, cx, cy, R, lon0=20.0, lat0=15.0, lights=True, glow_a=0.7):
    """small orthographic Earth with country shapes (Natural Earth) and a blue limb glow."""
    im = glow(im, lambda g: g.ell((cx - R*1.08, cy - R*1.08, cx + R*1.08, cy + R*1.08), fill=(40, 140, 220, 160)), 30, glow_a)
    d = D(im); d.ell((cx - R, cy - R, cx + R, cy + R), fill=(12, 22, 34))
    l0 = math.radians(lon0 + 4*_A.T/ max(1, _A.DUR)); p0 = math.radians(lat0)
    for name, ring in _globe_rings():
        lon, lat = ring[:, 0], ring[:, 1]
        cosc = math.sin(p0)*np.sin(lat) + math.cos(p0)*np.cos(lat)*np.cos(lon - l0)
        if (cosc > 0).sum() < 3: continue
        x = cx + R*np.cos(lat)*np.sin(lon - l0); y = cy - R*(math.cos(p0)*np.sin(lat) - math.sin(p0)*np.cos(lat)*np.cos(lon - l0))
        pts = [(a, b) for a, b, v in zip(x, y, cosc) if v > 0]
        if len(pts) >= 3: d.poly(pts, fill=(40, 52, 50, 255)); d.line(pts + [pts[0]], (80, 96, 96, 180), 1)
    return im

def orbit_pt(cx, cy, a, b, tilt, th):
    x, y = a*math.cos(th), b*math.sin(th); ct, st = math.cos(tilt), math.sin(tilt)
    return cx + x*ct - y*st, cy + x*st + y*ct, math.sin(th)   # z>0 = in front

def space(n=60, fill_at=None, fill_n=None, burst=None, belt=None, die_at=None, die_frac=0.0, shells=(), title="", tag="", R=150,
          cx=None, cy=None, kill_ring=None, debris=None, hilite=None, lon0=20.0, newsats=None, colors=None, label_dots=None):
    """Earth + satellites on tilted orbits. fill_at: time when the sky fills from n to fill_n dots. burst: time of a nuclear flash.
       belt: time the artificial radiation belt draws. die_at/die_frac: from that time a fraction of dots go dark one by one.
       shells: [(label, radius_px, cue_time, col)] labelled orbit rings. kill_ring: (time, px) small quick-kill ring around the burst.
       debris: time collisions start spraying fragments. newsats: time replacement sats rise into the belt and blink red."""
    im = base(); cx = cx or W/2; cy = cy or H/2 + 20; T_ = _A.T
    rng = np.random.default_rng(17)
    d = D(im)
    for i in range(140):   # stars
        sx, sy = rng.random()*W, rng.random()*H; d.ell((sx, sy, sx + 2, sy + 2), fill=(90, 90, 100, 160))
    for (lab, r, t0, col) in shells:
        k = seg(t0, 0.6)
        if k > 0:
            d.ell((cx - r, cy - r*0.36, cx + r, cy + r*0.36), outline=alpha(col, 0.7*k), width=2)
            d.text((cx + r*0.72, cy - r*0.36*0.7 - 34), lab, f(24, "inter"), alpha(col, k))
    # satellites: parameters
    total = n if fill_n is None else fill_n
    sats = []
    for i in range(total):
        a = R*1.18 + rng.random()*R*0.55; b = a*(0.22 + rng.random()*0.5); tilt = rng.normal(0, 0.5); ph = rng.random()*6.28; sp = 0.35 + rng.random()*0.4
        sats.append((a, b, tilt, ph, sp, rng.random()))
    front, back = [], []
    for i, (a, b, tilt, ph, sp, rr) in enumerate(sats):
        if i >= n:
            if fill_at is None: break
            if T_ < fill_at + (i - n)/max(1, total - n)*1.6: continue
        dead_t = None
        if die_at is not None and rr < die_frac: dead_t = die_at + rr/max(1e-6, die_frac)*max(0.8, (_A.DUR - die_at)*0.55)
        th = ph + sp*T_ if (dead_t is None or T_ < dead_t) else ph + sp*dead_t + 0.15*sp*(T_ - dead_t)
        x, y, z = orbit_pt(cx, cy, a, b, tilt, th)
        col = (colors[i % len(colors)] if colors else PAPER_HI)
        if dead_t is not None and T_ >= dead_t: col = mix(col, (70, 40, 36), seg(dead_t, 0.3))
        (front if z > -0.25 else back).append((x, y, col))
    for (x, y, col) in back: d.ell((x - 2.5, y - 2.5, x + 2.5, y + 2.5), fill=alpha(col, 0.55))
    if belt is not None and T_ > belt:
        k = seg(belt, 1.4)
        lay = Image.new("RGBA", (PW, PH), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay, "RGBA")
        for j in range(3):
            rx, ry = (R*1.45 + j*22)*S, (R*0.55 + j*12)*S
            ld.arc([cx*S - rx, cy*S - ry, cx*S + rx, cy*S + ry], 180, 180 + 360*k, fill=BELT + (int(110 - 25*j),), width=int((16 - 4*j)*S))
        lay = lay.filter(ImageFilter.GaussianBlur(6*S)); im.paste(lay, (0, 0), lay); d = D(im)
    im = earth(im, cx, cy, R, lon0=lon0); d = D(im)
    for (x, y, col) in front:
        d.ell((x - 3.2, y - 3.2, x + 3.2, y + 3.2), fill=col)
    if burst is not None and T_ > burst - 0.05:
        bx, by = cx + R*0.75, cy - R*1.05
        k = seg(burst, 0.25); fade = 1 - 0.75*seg(burst + 0.4, 1.4)
        im = glow(im, lambda g: g.ell((bx - 70*k, by - 70*k, bx + 70*k, by + 70*k), fill=(255, 250, 230, 255)), 50, 1.4*fade); d = D(im)
        r = 30 + 260*ease((T_ - burst)/1.6)
        d.ell((bx - r, by - r, bx + r, by + r), outline=alpha(PAPER_HI, 0.6*(1 - seg(burst + 0.6, 1.2))), width=3)
        if kill_ring:
            kt, kr = kill_ring; kk = seg(kt, 0.5)
            if kk > 0: d.ell((bx - kr*kk, by - kr*kk, bx + kr*kk, by + kr*kk), outline=alpha(RED, 0.95), width=4); d.text((bx + kr + 10, by - 14), "QUICK KILL ≈ 80 KM", f(22, "inter"), alpha(RED, kk))
    if debris is not None and T_ > debris:
        for j in range(6):
            t0 = debris + j*0.9
            if T_ < t0: continue
            px, py = cx - R*1.4 + rng.random()*R*2.8, cy - R*0.6 + rng.random()*R*1.2
            q = min(1, (T_ - t0)/1.2)
            d.ell((px - 10*(1-q), py - 10*(1-q), px + 10*(1-q), py + 10*(1-q)), fill=alpha(WARN, 1 - q))
            for m in range(14):
                ang = m/14*6.28 + j; L = 8 + 70*q
                d.ell((px + L*math.cos(ang) - 1.6, py + L*math.sin(ang)*0.6 - 1.6, px + L*math.cos(ang) + 1.6, py + L*math.sin(ang)*0.6 + 1.6), fill=alpha(ORANGE, 0.9))
    if newsats is not None and T_ > newsats:
        for j in range(5):
            t0 = newsats + j*0.5; q = ease((T_ - t0)/1.6)
            if q <= 0: continue
            x = cx - 200 + j*100; y = cy + R - (R*1.6)*q
            blink = int(T_*5 + j) % 2 == 0 and q >= 1
            d.rect((x - 6, y - 6, x + 6, y + 6), fill=RED if blink else PAPER_HI); d.rect((x - 18, y - 2, x - 8, y + 2), fill=CYAN); d.rect((x + 8, y - 2, x + 18, y + 2), fill=CYAN)
    if label_dots:
        for (txt, t0) in label_dots:
            center(d, H - 130, txt, f(40, "inter"), alpha(ORANGE, seg(t0, 0.4)))
    if title: d.text((70, 50), title.upper(), fit(d, title.upper(), 34, 900), alpha(PAPER_HI, seg(0.1, 0.4)))
    tagline(im, tag); return im

def satlogo(d, x, y, s=1.0, col=PAPER_HI, a=1.0):
    d.rect((x - 12*s, y - 10*s, x + 12*s, y + 10*s), fill=alpha(col, a))
    d.rect((x - 52*s, y - 6*s, x - 16*s, y + 6*s), fill=alpha(CYAN if col == PAPER_HI else col, a)); d.rect((x + 16*s, y - 6*s, x + 52*s, y + 6*s), fill=alpha(CYAN if col == PAPER_HI else col, a))
    d.line([(x, y - 10*s), (x, y - 26*s)], alpha(col, a), 3); d.ell((x - 5*s, y - 32*s, x + 5*s, y - 22*s), fill=alpha(col, a))

def satcards(names, cues, title="", stamp_txt="FAILED", tag=""):
    im = base(); d = D(im); n = len(names); gw = (W - 200)/n
    if title: center(d, 70, title.upper(), f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i, nm in enumerate(names):
        x = 100 + gw*i + gw/2; a = seg(0.2 + 0.2*i, 0.4); hit = c(cues[i] if i < len(cues) else 0, 1.0 + i)
        dead = seg(hit + 0.1 + 0.25*i, 0.5)
        satlogo(d, x, 300, 1.6, mix(PAPER_HI, (70, 60, 56), dead), a)
        center(d, 420, nm, f(46, "bebas"), alpha(PAPER_HI, a), cx=x)
        stamp(im, stamp_txt, x, 330, hit + 0.1 + 0.25*i, size=56, angle=-12)
    tagline(im, tag); return im

def skyflash(o, t):
    """night horizon over the sea; the sky flashes white -> green -> red (one colour per phrase), palm silhouettes."""
    im = Image.new("RGB", (PW, PH), (6, 8, 14)); T_ = _A.T; hit = c(0, 3.0)
    p = max(0.0, T_ - 0.3); k1 = seg(0.3, 0.15)*(1 - seg(1.3, 0.8)); k2 = seg(1.1, 0.6)*(1 - seg(2.6, 0.8)); k3 = seg(2.4, 0.7)*(1 - 0.5*seg(lead(hit, 0.2), 1.0))
    top = np.array([6, 8, 14], float)
    for col, k in (((255, 255, 250), k1), ((60, 255, 150), k2*0.8), ((200, 30, 30), k3*0.85)): top = top*(1 - k) + np.array(col)*k
    lay = Image.new("RGB", (PW, PH)); ld = ImageDraw.Draw(lay)
    for y in range(0, PH, 4):
        q = y/PH; c_ = top*(1 - q)**1.4 + np.array([6, 8, 14])*(1 - (1 - q)**1.4); ld.rectangle([0, y, PW, y + 4], fill=tuple(int(v) for v in c_))
    im = lay; d = D(im)
    d.rect((0, 520, W, H), fill=(4, 6, 10))
    for x in (90, 210, 1080, 1180):   # palm silhouettes
        d.line([(x, 520), (x + 18, 360)], (2, 2, 4), 10)
        for ang in range(0, 360, 45): d.line([(x + 18, 360), (x + 18 + 70*math.cos(math.radians(ang)), 360 + 30*math.sin(math.radians(ang)) + 12)], (2, 2, 4), 6)
    # streetlights along the shore that go out on the cue word
    nlamp = 26
    for i in range(nlamp):
        x = 270 + i*29; off = lead(hit, 0.1) + i*0.06; on = T_ < off
        d.line([(x, 520), (x, 470)], (20, 20, 22), 3)
        if on:
            im2 = im; d.ell((x - 5, 463, x + 5, 473), fill=(255, 214, 140))
        else: d.ell((x - 5, 463, x + 5, 473), fill=(40, 36, 30))
    if T_ < lead(hit, 0.1) + nlamp*0.06:
        im = glow(im, lambda g: [g.ell((270 + i*29 - 14, 454, 270 + i*29 + 14, 482), fill=(255, 200, 120, 200)) for i in range(nlamp) if T_ < lead(hit, 0.1) + i*0.06], 18, 0.9); d = D(im)
    center(d, 600, o, fit(d, o, 34, 1100), alpha(PAPER_HI, seg(lead(hit, 0.1) + 1.2, 0.5)))
    tagline(im, t); return im

def streetlight_map(o, t):
    """Hawaii map: Oahu lamps go dark; the Kauai phone link breaks."""
    im = map_scene(HAWAII, z=7, pins=[(KAUAI[0], KAUAI[1], "KAUAI", PAPER_HI, None), (HONOLULU[0], HONOLULU[1], "OAHU · HONOLULU", ORANGE, 0)],
                   lines=[(KAUAI, (HONOLULU[0], HONOLULU[1]), CYAN, 3, None, True)], title="HAWAII · 8 JULY 1962, 11 PM LOCAL", tag=t)
    m = Map(HAWAII, 7); d = D(im); rng = np.random.default_rng(5); hit = c(0, 1.5)
    for i in range(70):
        lo = HONOLULU[0] - 0.35 + rng.random()*0.55; la = HONOLULU[1] + rng.random()*0.35 - 0.05; x, y = m.P(lo, la)
        off = lead(hit, 0.3) + rng.random()*1.5
        d.ell((x - 3, y - 3, x + 3, y + 3), fill=(255, 210, 130) if _A.T < off else (50, 46, 40))
    k = seg(c(1, 3.0), 0.3); mx, my = m.P((KAUAI[0] + HONOLULU[0])/2, (KAUAI[1] + HONOLULU[1])/2)
    if k > 0: d.line([(mx - 22*k, my - 22*k), (mx + 22*k, my + 22*k)], RED, 7); d.line([(mx - 22*k, my + 22*k), (mx + 22*k, my - 22*k)], RED, 7); d.text((mx + 30, my - 10), "PHONE LINK CUT", f(26, "inter"), alpha(RED, k))
    return im

def waveform(o, t):
    im = base(); d = D(im); hit = c(0, 1.5)
    x0, x1, yb = 160, W - 120, 420; top = 170
    d.line([(x0, top), (x1, top)], alpha(RED, 0.8), 2); d.text((x1 - 260, top - 34), "INSTRUMENT LIMIT", f(22, "inter"), alpha(RED, 0.8))
    d.line([(x0, yb), (x1, yb)], DIM, 2)
    e = ease_io((_A.T - 0.3)/max(0.6, hit + 0.6 - 0.3)); pts = []
    for i in range(301):
        q = i/300
        if q > e: break
        xq = x0 + (x1 - x0)*q; tp = q - 0.55
        v = 6*math.sin(q*90) + (0 if tp < 0 else -620*math.exp(-tp*40)*(1 if tp < 0.004 else 1)) * (1 if tp >= 0 else 0)
        pts.append((xq, max(40, yb + v)))
    if len(pts) > 1: d.line(pts, ORANGE, 4)
    if e > 0.56: stamp(im, "OFF SCALE", W - 330, 300, lead(hit, 0.1), size=80)
    center(d, 520, o, fit(d, o, 40, 1000), alpha(PAPER_HI, seg(hit + 0.3, 0.5)))
    tagline(im, t); return im

def ladder(items, title="", tag="", flash_i=None):
    """vertical altitude scale: items [(km, label, cue_i, col)]."""
    im = base(); d = D(im); y0, y1 = H - 110, 110; x = 360; kmax = max(k for k, *_ in items) * 1.1
    d.line([(x, y0), (x, y1 + (1 - seg(0.1, 0.8))*(y0 - y1))], PAPER, 3)
    for j, (km, lab, ci, col) in enumerate(items):
        t0 = lead(c(ci, 0.5 + 0.6*j), 0.4); a = seg(t0, 0.4); y = y0 - (y0 - y1)*km/kmax
        d.line([(x - 16, y), (x + 16, y)], alpha(col, a), 4)
        d.text((x - 30 - d.tl(f"{km:,} KM", f(30, "bebas")), y - 18), f"{km:,} KM", f(30, "bebas"), alpha(col, a))
        d.text((x + 40, y - 20), lab, f(30, "inter"), alpha(PAPER_HI, a))
        if flash_i == j and a > 0:
            im = glow(im, lambda g: g.ell((x + 600 - 40, y - 40, x + 600 + 40, y + 40), fill=(255, 245, 220, 255)), 40, seg(t0, 0.2)*(1 - 0.6*seg(t0 + 0.5, 1.0))); d = D(im)
            pulse_rings(d, x + 600, y, PAPER_HI, t0, 2, 90)
    if title: d.text((180, 50), title.upper(), fit(d, title.upper(), 34, 900), alpha(ORANGE, seg(0, 0.4)))
    tagline(im, tag); return im

def mastheads(o, t):
    im = base(); d = D(im)
    for i, (nm, kind) in enumerate((("WDR", "inter"), ("NDR", "inter"), ("Süddeutsche Zeitung", "serif"))):
        t0 = 0.3 + 0.5*i if i < 2 else lead(c(0, 1.6), 0.3); k = seg(t0, 0.5); x = (1 - k)*W
        dd = paper(im, (220 + x, 120 + i*140, W - 220 + x, 230 + i*140), col=(226, 220, 208), seed=i + 3)
        center(dd, 140 + i*140, nm, f(64, kind), INK, cx=W/2 + x)
    stamp(im, "23 NOV 2026", W - 240, H - 150, c(0, 1.6) + 0.5, col=ORANGE, size=54)
    tagline(im, t); return im

def votes(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    center(d, 70, "UN SECURITY COUNCIL · 24 APRIL 2024", f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i in range(15):
        x = 150 + (i % 8)*130; y = 190 + (i // 8)*170; t0 = 0.4 + i*0.12
        col = GREEN if i < 13 else (GREY if i == 13 else CRIMSON)
        lab = "YES" if i < 13 else ("CHINA" if i == 13 else "RUSSIA")
        a = seg(t0 if i < 14 else lead(hit, 0.3), 0.3)
        d.rrect((x, y, x + 110, y + 120), 10, fill=alpha(col, 0.85*a))
        center(d, y + 40, lab, fit(d, lab, 28, 100), alpha(PAPER_HI, a), cx=x + 55)
    center(d, 560, "13 YES · 1 ABSTAIN · 1 NO", f(46, "inter"), alpha(PAPER_HI, seg(lead(hit, 0.2), 0.4)))
    stamp(im, "VETO", 1150, 360, hit + 0.2, size=110)
    tagline(im, t); return im

def unknowns(o, t):
    im = base(); d = D(im)
    for i, lab in enumerate(("LAUNCH?", "WARHEAD?", "EVIDENCE PUBLIC?")):
        x = 160 + i*340; a = seg(0.2 + 0.3*i, 0.4); hit = c(0, 1.5) + 0.35*i
        d.rect((x, 200, x + 300, 440), outline=alpha(PAPER, a), width=4)
        center(d, 470, lab, f(34, "inter"), alpha(PAPER_HI, a), cx=x + 150)
        center(d, 210, "?", f(200, "serif"), alpha(RED, seg(hit, 0.3)), cx=x + 150)
    stamp(im, "NOT CONFIRMED", W/2, 600, c(0, 1.5) + 1.0, size=64)
    tagline(im, t); return im

def treaty(title, date, lines_, stamp_txt=None, hl=0, tag=""):
    im = base(); dx = (1 - seg(0, 0.5))*W; d = paper(im, (220 + dx, 90, W - 220 + dx, H - 120), col=(226, 218, 200), seed=9); hit = c(0, 1.2)
    center(d, 120, title, fit(d, title, 46, W - 520, "serif"), INK, cx=W/2 + dx); center(d, 186, date, f(28, "inter"), (110, 60, 40), cx=W/2 + dx)
    y = 250
    for i, l in enumerate(lines_):
        if i == hl: highlight(d, (290 + dx, y + 6, 290 + dx + d.tl(l, f(30, "reg")), y + 40), lead(hit, 0.2), MARKER, 0.5)
        d.text((290 + dx, y), l, f(30, "reg"), alpha(INK, seg(0.4 + 0.2*i, 0.3))); y += 50
    for j, sgn in enumerate(("USA", "UK", "USSR")):
        x = 300 + j*240 + dx; pencil(d, [(x, H - 190), (x + 40, H - 205), (x + 80, H - 185), (x + 140, H - 200)], hit + 0.6 + 0.3*j, 0.4, GRAPHITE, 3, seed=j + 5)
        d.text((x, H - 175), sgn, f(20, "inter"), alpha((90, 80, 70), seg(hit + 0.6 + 0.3*j, 0.3)))
    if stamp_txt: stamp(im, stamp_txt, W - 300, H - 220, hit + 1.6, size=64)
    tagline(im, tag); return im

def rocketfail(o, t):
    im = base(); d = D(im); hit = c(0, 2.5)
    x0, y0 = 220, 600; e = min(1.0, max(0, _A.T - 0.3)/max(0.5, hit - 0.3))
    pts = [(x0 + 640*q, y0 - 420*(1 - (1 - q)**2)) for q in np.linspace(0, e*0.55, 40)]
    if len(pts) > 1: d.line(pts, ORANGE, 5)
    d.rect((120, 600, 340, 620), fill=(70, 66, 60)); d.text((120, 630), "JOHNSTON ATOLL", f(24, "inter"), PAPER)
    if _A.T >= hit:
        bx, by = pts[-1]; k = seg(hit, 0.4)
        im = glow(im, lambda g: g.ell((bx - 50, by - 50, bx + 50, by + 50), fill=(255, 140, 40, 255)), 40, 1 - 0.6*seg(hit + 0.4, 1.0)); d = D(im)
        d.line([(bx - 30, by - 30), (bx + 30, by + 30)], RED, 8); d.line([(bx - 30, by + 30), (bx + 30, by - 30)], RED, 8)
        d.text((bx + 40, by - 50), "59 S · ENGINE OUT", f(28, "inter"), alpha(PAPER_HI, k))
        rng = np.random.default_rng(3)
        for i in range(30):
            q = min(1, (_A.T - hit - 0.5 - rng.random()*0.8)/2.0)
            if q <= 0: continue
            sx = bx - rng.random()*260; d.ell((sx - 3, by + (600 - by)*q - 3, sx + 3, by + (600 - by)*q + 3), fill=alpha(WARN, 0.9))
    stamp(im, "20 JUN 1962 · FAILED", W - 280, 160, hit + 0.6, size=58)
    tagline(im, t); return im

def particles(o, t, aurora=False):
    """burst point with particles expanding, then magnetic field lines from pole to pole (dipole)."""
    im = base(); d = D(im); cx, cy, R = W/2, H/2 + 40, 120; hit = c(0, 1.5)
    if aurora: im = earth(im, cx, cy, R, lon0=-165, lat0=5); d = D(im)
    else: d.ell((cx - R, cy - R, cx + R, cy + R), fill=(20, 40, 60), outline=(70, 110, 130), width=2)
    k = seg(lead(hit, 0.4), 1.2)
    for L in (1.6, 2.2, 2.9, 3.7):
        pts = []
        for i in range(81):
            th = math.radians(-80 + 160*i/80); r = R*L*math.cos(th)**2
            if r < R: continue
            pts.append((cx + r*math.cos(th), cy - r*math.sin(th)))
        for side in (1, -1):
            pp = [(cx + side*(x - cx), y) for x, y in pts]
            sub = pp[:max(2, int(len(pp)*k))]
            if len(sub) > 1 and k > 0: d.line(sub, alpha(CYAN, 0.6), 2)
    bx, by = cx + R*1.35, cy - R*0.55
    rng = np.random.default_rng(8)
    for i in range(160):
        ang = rng.random()*6.28; sp = 40 + rng.random()*260; q = max(0, _A.T - 0.3)
        r = sp*min(1.4, q*0.6); d.ell((bx + r*math.cos(ang) - 2, by + r*math.sin(ang) - 2, bx + r*math.cos(ang) + 2, by + r*math.sin(ang) + 2), fill=alpha(PAPER_HI if i % 3 else ORANGE, max(0, 1 - q*0.25)))
    im = glow(im, lambda g: g.ell((bx - 30, by - 30, bx + 30, by + 30), fill=(255, 250, 230, 255)), 40, 1.0); d = D(im)
    if aurora:
        for (ax, ay) in ((cx + R*0.5, cy - R*0.86), (cx + R*0.35, cy + R*0.92)):
            a2 = seg(lead(hit, 0.2), 0.8)*(0.6 + 0.4*math.sin(_A.T*3))
            im = glow(im, lambda g: g.ell((ax - 60, ay - 18, ax + 60, ay + 18), fill=(80, 255, 160, 230)), 26, a2); d = D(im)
        d.text((cx + R*0.5 + 70, cy - R*0.86 - 20), "BURST AREA", f(24, "inter"), alpha(BELT, seg(hit, 0.4)))
        d.text((cx + R*0.35 + 70, cy + R*0.92 - 10), "NEAR SAMOA", f(24, "inter"), alpha(BELT, seg(hit + 0.3, 0.4)))
    center(d, 60, o, fit(d, o, 36, 1100), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, t); return im

def compare_bars(o, t):
    """Hiroshima vs Starfish yield"""
    im = base(); d = D(im); hit = c(0, 1.0)
    center(d, 80, "1.4 MEGATONS", f(110, "inter"), alpha(PAPER_HI, seg(lead(hit, 0.4), 0.4)))
    e = ease_io((_A.T - lead(hit, 0.2))/1.6)
    d.rect((260, 380, 260 + 9, 430), fill=PAPER); d.text((260, 440), "HIROSHIMA ≈ 15 KT", f(26, "inter"), PAPER)
    d.rect((260, 480, 260 + 870*e, 530), fill=ORANGE); d.text((260, 540), "STARFISH PRIME 1,400 KT", f(26, "inter"), alpha(ORANGE, seg(lead(hit, 0.2) + 1.0, 0.4)))
    d.text((W - 360, 380), "≈ 100x", f(70, "bebas"), alpha(RED, seg(lead(hit, 0.2) + 1.6, 0.4)))
    tagline(im, t); return im

def belt_health(o, t):
    """one satellite looping through the belt: every pass flashes, health bar drops."""
    im = space(n=1, belt=0.2, R=140, title="", tag="")
    d = D(im); passes = int(max(0, _A.T - 0.8)/1.4); hp = max(0.05, 1 - 0.18*passes)
    d.text((70, 60), "SATELLITE HEALTH", f(28, "inter"), PAPER_HI); d.rect((70, 100, 470, 130), outline=PAPER, width=2)
    d.rect((72, 102, 72 + 396*hp, 128), fill=GREEN if hp > 0.5 else (WARN if hp > 0.25 else CRIMSON))
    if passes and (_A.T - 0.8) % 1.4 < 0.25: d.rect((0, 0, W, H), fill=(120, 255, 170, 40))
    center(d, H - 130, o, fit(d, o, 40, 1000), alpha(ORANGE, seg(c(0, 1.0), 0.4)))
    tagline(im, t); return im

def calendar_dead(o, t):
    return calendar(["JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB"], circles=[(0, "10 JUL · LAUNCH", -1), (7, "DEAD", 0)], stamps=[(7, "DEAD", 0)], title="TELSTAR 1 · 1962-63", tag=t)

def kz_map(o, t, mode=0):
    pins = [(ZHEZ[0] - 1.5, ZHEZ[1], "BURST · 290 KM UP", RED, 0 if mode == 0 else None), (KARAG[0], KARAG[1], "KARAGANDA", ORANGE, None if mode == 0 else 1),
            (ASTANA[0], ASTANA[1], "ASTANA", PAPER_HI, None), (ALMATY[0], ALMATY[1], "ALMATY", PAPER_HI, None)]
    lines = [] if mode == 0 else [((ZHEZ[0] - 5.5, ZHEZ[1] - 0.6), (ZHEZ[0] + 1.6, ZHEZ[1] + 0.8), ORANGE, 6, 0, False), (ASTANA, ALMATY, RED, 5, 2, True)]
    im = map_scene(KAZ, z=5, hi=("Kazakhstan",), pins=pins, lines=lines, title="KAZAKHSTAN · 22 OCT 1962", tag=t)
    if mode == 1:
        d = D(im); m = Map(KAZ, 5, ("Kazakhstan",)); x, y = m.P(*KARAG); k = seg(lead(c(1, 3.0), 0.2), 0.4)
        if k > 0:
            for j in range(5):
                h = 30 + 18*math.sin(_A.T*9 + j); d.poly([(x - 20 + j*8, y), (x - 16 + j*8, y - h*k), (x - 10 + j*8, y)], fill=alpha(WARN, 0.9))
        d.text((m.P(ZHEZ[0] - 5.5, ZHEZ[1] - 0.6)[0], m.P(ZHEZ[0] - 5.5, ZHEZ[1] - 0.6)[1] + 20), "570 KM PHONE LINE (SCHEMATIC)", f(22, "inter"), alpha(ORANGE, seg(lead(c(0), 0.4), 0.4)))
        mx, my = m.P((ASTANA[0] + ALMATY[0])/2, (ASTANA[1] + ALMATY[1])/2)
        _ca = alpha(RED, seg(lead(c(2, 5.0), 0.4), 0.4)); d.text((mx + 30, my + 30), "1,000 KM", f(22, "inter"), _ca); d.text((mx + 30, my + 58), "BURIED CABLE", f(22, "inter"), _ca)
    return im

def roadmap(o, t, items):
    im = base(); d = D(im); n = len(items); gap = (W - 240) / (n - 1)
    d.line([(120, 360), (W - 120, 360)], DIM, 4)
    for i, lab in enumerate(items):
        t0 = 0.5 + i * (_A.DUR - 1.5) / n
        a = seg(t0, 0.4); x = 120 + i*gap
        d.ell((x - 22, 338, x + 22, 382), fill=alpha(ORANGE if a > 0.5 else DIM, max(0.3, a)))
        center(d, 410, lab, fit(d, lab, 28, gap - 10), alpha(PAPER_HI, max(0.25, a)), cx=x)
        pulse_rings(d, x, 360, ORANGE, t0, 1, 50, 0.5)
    tagline(im, t); return im

def clockface(o, t):
    im = base(); d = D(im); cx, cy, r = 300, 360, 150; hit = c(0, 1.5)
    d.ell((cx - r, cy - r, cx + r, cy + r), outline=PAPER_HI, width=6)
    for i in range(12):
        a = i/12*6.28; d.line([(cx + (r - 20)*math.sin(a), cy - (r - 20)*math.cos(a)), (cx + (r - 6)*math.sin(a), cy - (r - 6)*math.cos(a))], PAPER, 4)
    a = _A.T*1.2; d.line([(cx, cy), (cx + (r - 30)*math.sin(a), cy - (r - 30)*math.cos(a))], ORANGE, 5); d.ell((cx - 8, cy - 8, cx + 8, cy + 8), fill=ORANGE)
    satlogo(d, 760, 140, 1.0); k = seg(lead(hit, 0.3), 0.8)
    for j, (tx, ty, lab) in enumerate(((620, 520, "PHONE MAST"), (980, 520, "TRAFFIC LIGHT"))):
        kk = seg(lead(hit, 0.3) + 0.4*j, 0.8)
        if kk > 0: d.line([(760, 160), (760 + (tx - 760)*kk, 160 + (ty - 160)*kk)], alpha(ORANGE, 0.9), 3)
        d.text((tx - d.tl(lab, f(28, "inter"))/2, ty + 20), lab, f(28, "inter"), alpha(PAPER_HI, kk))
        if j == 0: d.line([(tx, ty), (tx - 30, ty + 110 - 100)], PAPER, 0)
    d.rect((605, 520, 635, 560), outline=PAPER, width=3); d.line([(620, 470), (620, 520)], PAPER, 4)
    d.rrect((962, 450, 998, 520), 8, fill=(30, 30, 30)); [d.ell((970, 456 + i*21, 990, 476 + i*21), fill=[RED, WARN, GREEN][i] if int(_A.T*0.8) % 3 == i else (60, 60, 60)) for i in range(3)]
    center(d, 60, o, fit(d, o, 38, 1100), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, t); return im

def gps4(o, t):
    im = base(); im = earth(im, W/2, H/2 + 60, 200, lon0=-10, lat0=30); d = D(im); hit = c(0, 2.0)
    px, py = W/2 + 30, H/2 + 10
    for j, (sx, sy) in enumerate(((240, 120), (520, 70), (820, 90), (1060, 160))):
        satlogo(d, sx, sy, 0.6); t0 = lead(hit, 0.6) + j*0.25; k = seg(t0, 0.5)
        if k > 0: d.line([(sx, sy), (sx + (px - sx)*k, sy + (py - sy)*k)], alpha(ORANGE, 0.85), 3)
    k = seg(lead(hit, 0.6) + 1.2, 0.3)
    if k > 0: d.ell((px - 10, py - 10, px + 10, py + 10), fill=RED); pulse_rings(d, px, py, RED, lead(hit, 0.6) + 1.2, 2, 40)
    center(d, H - 120, o, fit(d, o, 40, 1000), alpha(PAPER_HI, seg(0.3, 0.4)))
    tagline(im, t); return im

def scale(o, t):
    im = base(); d = D(im); a = 0.08*math.sin(_A.T*0.8)
    cx, cy = W/2, 220; d.line([(cx, cy), (cx, 520)], PAPER, 6); d.poly([(cx - 60, 540), (cx + 60, 540), (cx, 500)], fill=PAPER)
    L = 360; xa, ya = cx - L*math.cos(a), cy - L*math.sin(a); xb, yb = cx + L*math.cos(a), cy + L*math.sin(a)
    d.line([(xa, ya), (xb, yb)], PAPER_HI, 6)
    for (x, y, lab, col, t0) in ((xa, ya, "THREAT", CRIMSON, 0.3), (xb, yb, "RESPONSE", CYAN, lead(c(0, 1.5), 0.3))):
        d.line([(x, y), (x - 60, y + 120)], PAPER, 2); d.line([(x, y), (x + 60, y + 120)], PAPER, 2); d.rect((x - 80, y + 120, x + 80, y + 140), fill=PAPER)
        center(d, y + 160, lab, f(40, "bebas"), alpha(col, seg(t0, 0.4)), cx=x)
    center(d, 620, o, fit(d, o, 36, 1100), alpha(ORANGE, seg(c(0, 1.5) + 0.6, 0.4)))
    tagline(im, t); return im

def checklist(items, title="", tag=""):
    im = base(); d = paper(im, (260, 90, W - 260, H - 110), seed=12)
    center(d, 120, title, f(44, "bebas"), INK)
    for i, l in enumerate(items):
        y = 220 + i*110; t0 = lead(c(i, sn(i) + 0.5), 0.3)
        d.rect((320, y, 360, y + 40), outline=INK, width=3); d.text((390, y), l, f(36, "inter"), alpha(INK, seg(t0 - 0.3, 0.3)))
        pencil_tick(d, 324, y + 4, t0 + 0.2, RED, seed=i + 3, s=1.3)
    tagline(im, tag); return im

def iconrow(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    for j, (lab, col) in enumerate((("AMBULANCE", PAPER_HI), ("FIRE ENGINE", RED), ("POLICE", CYAN))):
        x = 250 + j*390; a = seg(0.2 + 0.3*j, 0.4)
        d.rrect((x - 120, 200, x + 120, 300), 16, fill=alpha(col, a)); d.ell((x - 90, 285, x - 40, 335), fill=alpha(INK, a)); d.ell((x + 40, 285, x + 90, 335), fill=alpha(INK, a))
        d.rect((x - 40, 180, x + 40, 200), fill=alpha(WARN if int(_A.T*4 + j) % 2 else CYAN, a))
        center(d, 350, lab, f(30, "inter"), alpha(PAPER, a), cx=x)
        center(d, 110, "?", f(90, "serif"), alpha(RED, seg(lead(hit, 0.3) + 0.2*j, 0.3)), cx=x)
    e = ease_io((_A.T - lead(hit, 0.6))/1.2); center(d, 430, countup("£1.97", e) + " BN", f(110, "inter"), alpha(ORANGE, min(1, e*4)))
    center(d, 580, "LOST IN ONE WEEK · NOT KNOWING WHERE THEY ARE", f(30, "serif"), alpha(PAPER, seg(lead(hit, 0.6) + 1.0, 0.4)))
    tagline(im, t); return im

def callerpin(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    x, y = 330, 180; d.rrect((x, y, x + 200, y + 360), 30, outline=PAPER_HI, width=6); center(d, y + 140, "999", f(70, "inter"), PAPER_HI, cx=x + 100)
    k = seg(0.6, 0.4)
    for i in range(0, 360, 30):
        a = math.radians(i); d.line([(x + 100 + 150*math.cos(a), y + 180 + 150*math.sin(a)), (x + 100 + 160*math.cos(a), y + 180 + 160*math.sin(a))], alpha(RED, k), 3)
    center(d, y + 380, "WHERE ARE YOU?", f(30, "inter"), alpha(RED, k), cx=x + 100)
    e = ease_io((_A.T - lead(hit, 0.8))/1.2); center(d, 260, countup("£1.56", e) + " BN", f(110, "inter"), alpha(ORANGE, min(1, e*4)), cx=870)
    center(d, 410, "CALLERS NOT LOCATED · 1 WEEK", f(30, "serif"), alpha(PAPER, seg(lead(hit, 0.8) + 1.0, 0.4)), cx=870)
    tagline(im, t); return im

def floorbar(o, t):
    im = base(); d = D(im); hit = c(0, 3.0)
    d.text((180, 70), "HOW LONG THE OUTAGE LASTS", f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    for i, (lab, wv) in enumerate((("1 DAY · £1.4BN", 60), ("7 DAYS · £7.6BN", 330))):
        e = ease_io((_A.T - 0.3 - 0.5*i)/0.8); d.rect((180, 200 + i*130, 180 + wv*e, 270 + i*130), fill=ORANGE); d.text((200 + wv, 215 + i*130), lab, f(30, "inter"), alpha(PAPER_HI, e))
    k = seg(lead(hit, 0.4), 1.4); y = 460
    for q in range(0, int((W - 420)*k), 34): d.rect((180 + q, y, 180 + q + 22, y + 70), fill=alpha(RED, 0.85))
    d.text((200, y + 90), "A RADIATION BELT: MONTHS?", f(34, "inter"), alpha(RED, seg(lead(hit, 0.4) + 0.6, 0.4)))
    stamp(im, "A FLOOR, NOT A CEILING", W - 430, 250, c(1, hit + 2.5), size=50)
    tagline(im, t); return im

def blanks(o, t):
    lines_ = [("NAVIGATION (STUDIES)", "£7.6BN / WK"), ("WEATHER SATELLITES", "?"), ("SATELLITE INTERNET", "?"), ("REBUILDING THE FLEET", "?")]
    im = receipt(lines_, title="NOT EVEN COUNTED YET", tag=t, show=1, cues_from=[c(0, 1.5) - 0.8, c(0, 1.5) - 0.2, c(0, 1.5) + 0.6])
    return im

def hidden(o, t):
    return chain(["DELAYS", "INSURANCE", "999", "PRICES"], title="THE BILL ARRIVES HIDDEN", tag=t)

# corner receipt lines (rulebook 5) are set in render17
P = lambda n, title: (lambda o, t: part(n, title))
SPEC = {
"CO-01": lambda o, t: space(n=40, R=130, title="", tag=t, label_dots=[(o, c(0, 2.0))], lon0=37, newsats=None) if False else countdown(o, t),
"CO-02": lambda o, t: space(n=40, fill_at=0.6, fill_n=260, R=140, burst=None, title="", tag=t, label_dots=[("AIMED AT THE SKY", lead(c(0, 2.0), 0.3))]),
"CO-03": lambda o, t: card(["HAWAII · 1962"], tag=t),
"CO-03b": lambda o, t: number("AMERICAN", sub="A test, on purpose, by the country that owned the satellites", kicker="THE BOMB WAS", tag=t),
"CO-04": skyflash,
"CO-05": lambda o, t: satcards(["ARIEL", "TRAAC", "TRANSIT 4B", "TELSTAR"], [0, 0, 0, 0], title="IT KILLED SATELLITES", stamp_txt="DEAD", tag=t),
"CO-06": lambda o, t: roadmap(o, t, ["THE SATELLITE", "1962", "THE DAMAGE", "THE SKY NOW", "YOUR BILL"]),
"P1-01": P(1, "The satellite in the hangar"),
"P1-02": mastheads,
"P1-02b": lambda o, t: flow({"b": (260, 200, "BND (SPY SERVICE)", ORANGE), "m": (260, 360, "GERMAN MILITARY", ORANGE), "n": (260, 520, "NATO ALLIES", ORANGE), "r": (820, 360, "WDR · NDR · SZ", PAPER_HI)},
                             [("b", "r", "", 0), ("m", "r", "", 0), ("n", "r", "WARNINGS", 0)], title="WHERE THE STORY CAME FROM", tag=t),
"P1-03": lambda o, t: typed(["NAME: SPUTNIK-S", "PAYLOAD: NUCLEAR (REPORTED)"], label="INTELLIGENCE FILE · REPORTED", tag=t, cue_lines=[0, 0], stamps=[("REPORTED", c(0) + 3.0)]),
"P1-04": lambda o, t: map_scene(WRUS, z=5, hi=("Russia",), pins=[(MOSCOW[0], MOSCOW[1], "MOSCOW REGION · STORED", ORANGE, 0)], title="WHERE IT IS SAID TO BE STORED", tag=t),
"P1-05": lambda o, t: calendar(["NOV", "DEC", "JAN"], circles=[(1, "DECEMBER?", 1)], flames_every=None, stamps=[(2, "60 DAYS", 0)], title="THE WARNING · EARLY NOVEMBER 2026", tag=t),
"P1-05b": lambda o, t: typed(["BRIEFED: MINISTER PISTORIUS", "MINISTRY: NO COMMENT"], label="BERLIN", tag=t, cue_lines=[0, 0]),
"P1-06": lambda o, t: quote("Nothing new, but no less shocking", "Friedrich Merz, German chancellor", "23 Nov 2026", tag=t),
"P1-06b": lambda o, t: quote("How far Russia is prepared to escalate", "Friedrich Merz", "23 Nov 2026", tag=t),
"P1-07": lambda o, t: quote("Every inch of NATO territory", "Mark Rutte, NATO secretary general", "23 Nov 2026", tag=t),
"P1-08": lambda o, t: typed(["NO IMMEDIATE THREAT", "3 NOV: SECURITY COUNCIL"], label="GERMAN GOVERNMENT", tag=t, cue_lines=[0, 0], stamps=[("CLASSIFIED", sn(1) + 2.0)]),
"P1-09": lambda o, t: quote("Hardly worth taking seriously", "Dmitry Peskov, Kremlin spokesman", "Nov 2026", tag=t),
"P1-10": unknowns,
"P1-10b": lambda o, t: split(("SPUTNIK-S", "REPORTED", "Not proven. Treat it with care."), ("1962", "PROVEN", "We have the receipts."), tag=t),
"P1-11": lambda o, t: quote("Designed to carry a nuclear weapon", "US Defense Intelligence Agency", "2026", tag=t),
"P1-11b": lambda o, t: number("THOUSANDS", sub="'rapid and sudden loss or degradation of thousands of satellites'", kicker="DIA, 2026", tag=t),
"P1-11c": lambda o, t: tiles([("MISSILES", "smash one satellite, debris for centuries"), ("JAMMING", "drowns out signals"), ("LASERS", "blind a camera"), ("NUCLEAR", "thousands at once")], title="WAYS TO ATTACK SPACE · DIA 2026", tag=t, cues=[-1, -1, 0, 1] if len(_A.CUES) > 1 else None),
"P1-12": lambda o, t: timeline([("FEB 2022", "Kosmos 2553 launched"), ("FEB 2024", "White House: 'troubling' weapon"), ("APR 2024", "Russia vetoes UN text"), ("NOV 2026", "Sputnik-S report")], [1], title="THE WARNINGS", tag=t),
"P1-13": lambda o, t: space(n=18, R=130, title="KOSMOS 2553 · 5 FEB 2022", tag=t, label_dots=[("A DUMMY? A RADIATION TEST?", lead(c(0, 2.0), 0.3))], colors=[GREY]),
"P1-13b": lambda o, t: tumble(o, t),
"P1-13c": lambda o, t: timeline([("5 FEB 2022", "Kosmos 2553 launched"), ("24 FEB 2022", "Russia invades Ukraine")], [0, 1], title="LOOK AT THE DATE", tag=t),
"P1-14": lambda o, t: treaty("OUTER SPACE TREATY", "27 JANUARY 1967", ["Article IV: States shall not place in orbit", "any objects carrying nuclear weapons", "or any other weapons of mass destruction."], hl=1, tag=t),
"P1-14b": lambda o, t: number("118", sub="countries are parties to the treaty", kicker="OUTER SPACE TREATY · OCT 2025", tag=t),
"P1-15": votes,
"P1-16": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1")], title="RUNNING TOTAL", tag=t, show=0),
"BR-01": lambda o, t: number("SUBSCRIBE", sub="every crisis, all the way to your bill", kicker="THE HISTORY INVOICE", tag=t),
"P2-01": P(2, "The night they bombed the sky"),
"P2-02": lambda o, t: number("1962", kicker="THE COLD WAR AT ITS HOTTEST", faded="1962", tag=t),
"P2-03": lambda o, t: timeline([("30 AUG 1961", "USSR ends 3-year test pause"), ("1962", "US: Operation Dominic"), ("1962", "Fishbowl: tests in space")], [0, 2], title="THE TEST RACE", tag=t),
"P2-04": lambda o, t: map_scene(PACIFIC, z=5, pins=[(JOHNSTON[0], JOHNSTON[1], "JOHNSTON ATOLL", ORANGE, 0), (HONOLULU[0], HONOLULU[1], "HAWAII", PAPER_HI, None)],
                                measure=(JOHNSTON, HONOLULU, "1,450 KM", 0), title="THE PACIFIC · 1962", tag=t),
"P2-04b": lambda o, t: map_scene(PACIFIC, z=5, pins=[(JOHNSTON[0], JOHNSTON[1], "LAUNCH", ORANGE, None), (HONOLULU[0], HONOLULU[1], "HAWAII", PAPER_HI, 0)],
                                 arcs=[(JOHNSTON, (-175, 12), ORANGE, 5, 0, False)], labels=[(-174, 10.5, "FIRED SOUTH-WEST", 26, ORANGE)], title="AWAY FROM PEOPLE", tag=t),
"P2-05": rocketfail,
"P2-06": lambda o, t: typed(["OPERATION FISHBOWL", "SHOT: STARFISH PRIME", "9 JULY 1962"], label="US ATOMIC ENERGY COMMISSION", tag=t, cue_lines=[-1, 0, 0]),
"P2-06b": lambda o, t: typed(["BLUEGILL · LOST BY RADAR", "STARFISH · ENGINE FAILED", "STARFISH PRIME · 9 JULY"], label="FISHBOWL LOG", tag=t, cue_lines=[0, 0, 0], stamps=[("FALSE STARTS", c(0) + 4.0)]),
"P2-07": compare_bars,
"P2-08": lambda o, t: ladder([(0, "SEA LEVEL", -1, PAPER), (100, "WHERE SPACE BEGINS", -1, PAPER), (400, "STARFISH PRIME · ISS TODAY", 0, ORANGE)], title="400 KM UP · 13 MIN 41 S", tag=t, flash_i=2),
"P2-08b": lambda o, t: map_scene(PACIFIC, z=5, pins=[(JOHNSTON[0], JOHNSTON[1], "27 ROCKETS", ORANGE, None), (JOHNSTON[0] + 3, JOHNSTON[1] - 3, "SOVIET SHIP (UNINVITED)", RED, 0), (SAMOA[0], SAMOA[1] + 2, "US SHIPS · SOUTH", PAPER_HI, None)], title="WATCHED FROM EVERYWHERE", tag=t),
"P2-09": lambda o, t: particles("NO AIR · NO MUSHROOM CLOUD · RADIATION", t),
"P2-10": lambda o, t: particles("AURORAS ON BOTH SIDES OF THE EQUATOR", t, aurora=True),
"P2-11": lambda o, t: quote("A brilliant white flash burned through the clouds", "US 'Quick Look' report, Kwajalein", "Aug 1962", tag=t),
"P2-11b": lambda o, t: map_scene(PACIFIC, z=5, pins=[(SAMOA[0], SAMOA[1], "SAMOA · SOUTHERN GLOW", (120, 255, 170), 0), (JOHNSTON[0], JOHNSTON[1], "BURST", ORANGE, None), (HONOLULU[0], HONOLULU[1], "HAWAII", PAPER_HI, None)],
                                  rings=[(SAMOA[0], SAMOA[1], 500, 0, ""), (JOHNSTON[0], JOHNSTON[1], 600, -1, "")], title="SEEN FROM SAMOA TO HAWAII", tag=t),
"P2-12": lambda o, t: card(["HONOLULU · 11 PM"], tag=t),
"P2-13": waveform,
"P2-14": streetlight_map,
"P2-15": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2")], title="RUNNING TOTAL", tag=t, show=1),
"P3-01": P(3, "What the bomb left behind"),
"P3-02": lambda o, t: space(n=10, belt=lead(c(0, 2.0), 0.6), R=140, title="A MAN-MADE RADIATION BELT", tag=t),
"P3-03": belt_health,
"P3-03b": lambda o, t: space(n=40, burst=0.4, kill_ring=(lead(c(0, 2.0), 0.3), 80), belt=sn(2) if len(_A.SENTS) > 2 else 5.0, R=140, title="THE FLASH VS THE BELT", tag=t),
"P3-04": lambda o, t: satcards(["ARIEL", "TRAAC", "TRANSIT 4B"], [0, 0, 0], title="KILLED BY THE BELT", tag=t),
"P3-05": lambda o, t: stats3([("TELSTAR 1", "launched the day after", -1), ("10 JUL 1962", "", 0), ("≈ $50M", "project cost, AT&T", 1)], title="TELSTAR", tag=t),
"P3-06": lambda o, t: card(["FIRST LIVE TV ACROSS THE ATLANTIC"], tag=t),
"P3-07": calendar_dead,
"P3-07b": lambda o, t: gauge(90, "radiation 4 months later", sub="still dangerous for astronauts", tag=t, stamp_txt="NASA WORRIED", valtxt=lambda e: "HIGH"),
"P3-07c": lambda o, t: typed(["URRACA · ≈ 1 MEGATON", "PLANNED ABOVE 1,000 KM"], label="FISHBOWL · PLANNED TEST", tag=t, cue_lines=[0, 0], stamps=[("CANCELLED", c(0) + 2.6)]),
"P3-08": lambda o, t: kz_map(o, t, 0),
"P3-09": lambda o, t: timeline([("14 OCT", "Missiles spotted in Cuba"), ("22 OCT", "Project K: 300 kt, 290 km up"), ("28 OCT", "Crisis ends")], [1], title="THE CUBAN MISSILE CRISIS · 1962", tag=t),
"P3-10": lambda o, t: kz_map(o, t, 1),
"P3-10b": lambda o, t: split(("STARFISH · 1962", "1.4 MT", "over open ocean"), ("PROJECT K · 1962", "300 KT", "over land: more damage"), tag=t),
"P3-10c": lambda o, t: split(("FISHBOWL", "USA", "high blasts · late 1962"), ("PROJECT K", "USSR", "high blasts · late 1962"), tag=t),
"P3-11": lambda o, t: treaty("PARTIAL TEST BAN TREATY", "5 AUGUST 1963 · MOSCOW", ["No nuclear test explosions:", "in the atmosphere,", "in outer space,", "or under water."], hl=2, tag=t),
"P3-11b": lambda o, t: timeline([("1963", "Test ban signed"), ("1974", "France: last above-ground test"), ("1980", "China: last above-ground test"), ("NOW", "None since")], [3], title="THE TABOO HELD", tag=t),
"P3-12": lambda o, t: timeline([("1962", "Starfish Prime"), ("1963", "Test ban"), ("1967", "Space treaty"), ("2026", "Sputnik-S?")], [2], title="ALMOST 60 YEARS OF A PROMISE", tag=t),
"P3-13": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2"), ("SATELLITES DEAD FOR MONTHS", "LINE 3")], title="RUNNING TOTAL", tag=t, show=2),
"P4-01": P(4, "Why one blast now is worse"),
"P4-02": lambda o, t: space(n=6, fill_at=lead(c(0, 2.0), 0.2), fill_n=420, R=140, title="1962 → 2026", tag=t),
"P4-03": lambda o, t: number("13,000+", sub="satellites in low Earth orbit", kicker="PRINCETON STUDY · NOV 2026", tag=t),
"P4-04": lambda o, t: stacked([("STARLINK ≈ 11,190", 11190, ORANGE, 0), ("EVERYONE ELSE", 2000, DIM, -1)], title="WHO OWNS LOW ORBIT", total="", tag=t),
"P4-05": lambda o, t: globe((-20, -30), title="THE SIMULATION: 1 MT · 500 KM · SOUTH ATLANTIC", tag=t) if False else burst_globe(o, t),
"P4-06": lambda o, t: space(n=200, burst=0.4, kill_ring=(1.0, 80), belt=lead(c(0, 3.0), 0.3), R=140, title="THE FLASH · THEN THE BELT", tag=t),
"P4-07": lambda o, t: gauge(98, "disabled within one week", sub="central case of the study", tag=t),
"P4-08": lambda o, t: bars([("NORMAL · 1 WEEK", 98), ("3x TOUGHER · 2 WEEKS", 97)], title="MAKING THEM TOUGHER BARELY HELPS", unit="%", hi=1, tag=t, cues=[-1, 0]),
"P4-09": lambda o, t: space(n=200, die_at=0.2, die_frac=0.95, debris=lead(c(0, 2.5), 0.4), R=140, title="≈ 20 COLLISIONS IN 2 YEARS", tag=t),
"P4-10": lambda o, t: space(n=120, die_at=0.0, die_frac=0.9, debris=0.3, R=140, title="EVERY CRASH MAKES MORE BULLETS", tag=t),
"P4-11": lambda o, t: space(n=60, die_at=0.0, die_frac=1.0, belt=0.0, newsats=lead(c(0, 2.5), 1.0), R=140, title="REPLACEMENTS FLY INTO IT", tag=t),
"P4-12": lambda o, t: card(["FEB 2022 · UP TO 40 STARLINKS LOST"], tag=t),
"P4-12b": lambda o, t: ladder([(0, "GROUND", -1, PAPER), (210, "RELEASE HEIGHT · AIR GOT THICKER", 0, RED), (550, "WHERE THEY WERE GOING", -1, CYAN)], title="WHY THEY FELL", tag=t),
"P4-13": lambda o, t: split(("NATURE · 2022", "UP TO 40", "lost to a mild storm"), ("A BOMB", "THOUSANDS?", "a storm somebody chooses"), tag=t),
"P4-14": lambda o, t: space(n=80, R=110, shells=[("LEO · INTERNET, WEATHER", 200, 0.5, ORANGE), ("MEO · GPS", 330, lead(c(0, 2.0), 0.3), CYAN), ("GEO · COMMUNICATIONS", 470, lead(c(0, 2.0), 0.3) + 1.6, PAPER_HI)], title="IT COULD BE AIMED HIGHER · DIA", tag=t),
"P4-15": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2"), ("SATELLITES DEAD FOR MONTHS", "LINE 3"), ("≈ 98% OF LOW ORBIT IN A WEEK (STUDY)", "LINE 4")], title="RUNNING TOTAL", tag=t, show=3),
"P5-01": P(5, "The chores the sky does for you"),
"P5-02": lambda o, t: card(["START WITH THE MORNING"], tag=t),
"P5-03": lambda o, t: space(n=30, R=130, shells=[("METOP · NOAA · ≈ 850 KM", 215, lead(c(0, 2.0), 0.3), ORANGE)], title="WEATHER SATELLITES FLY LOW", tag=t),
"P5-04": lambda o, t: chain(["SATELLITE", "DATA", "FORECAST", "WARNINGS"], title="LOSE THEM, FORECASTS GET WORSE", tag=t),
"P5-05": lambda o, t: card(["FARMS · FLIGHTS · STORM WARNINGS"], tag=t),
"P5-05b": lambda o, t: number("£223.6M", sub="lost by UK farming in one week without satellite navigation", kicker="LONDON ECONOMICS · 2023", tag=t),
"P5-06": lambda o, t: card(["SHIPS · PLANES · REMOTE HOMES"], tag=t),
"P5-07": lambda o, t: flow({"s": (300, 360, "STARLINK", ORANGE), "a": (880, 200, "COMMANDS", PAPER_HI), "b": (880, 360, "POWER GRID", PAPER_HI), "c": (880, 520, "DRONES", PAPER_HI)},
                           [("s", "a", "", 0), ("s", "b", "", 0), ("s", "c", "", 0)], title="UKRAINE RUNS ON STARLINK", tag=t),
"P5-08": lambda o, t: space(n=220, die_at=lead(c(0, 2.0), 0.3), die_frac=0.9, burst=lead(c(0, 2.0), 0.4), R=140, title="NOT ONE SATELLITE · THE WHOLE NETWORK", tag=t),
"P5-09": lambda o, t: space(n=40, R=100, shells=[("LEO", 170, 0.4, ORANGE), ("GPS · ≈ 20,200 KM", 420, lead(c(0, 2.0), 0.3), CYAN)], title="GPS FLIES MUCH HIGHER", tag=t),
"P5-09b": gps4,
"P5-10": lambda o, t: split(("A BLAST IN LOW ORBIT", "GPS OK?", "it sits ≈ 20,000 km up"), ("A TAILORED BLAST", "GPS AT RISK", "DIA: a blast could be aimed at that orbit"), tag=t),
"P5-11": clockface,
"P5-12": lambda o, t: card(["TIME COMES FROM SPACE"], tag=t),
"P5-13": lambda o, t: card(["THE AMBULANCE FINDS YOU"], tag=t),
"P5-14": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2"), ("SATELLITES DEAD FOR MONTHS", "LINE 3"), ("≈ 98% OF LOW ORBIT IN A WEEK", "LINE 4"), ("FORECAST · MAP · CLOCK · SIGNAL", "LINE 5")], title="RUNNING TOTAL", tag=t, show=4),
"P6-01": P(6, "The bill"),
"P6-02": lambda o, t: typed(["NO PRICE FOR A SPACE BLAST", "BUT A GPS OUTAGE: PRICED"], label="THE NEAREST PRICE TAG", tag=t, cue_lines=[-1, 0]),
"P6-03": lambda o, t: number("£1.424 BN", sub="one day without satellite navigation, UK", kicker="LONDON ECONOMICS FOR THE UK GOVERNMENT · 2023", tag=t),
"P6-04": lambda o, t: bars([("1 DAY", 1.424), ("7 DAYS", 7.644)], title="THE UK BILL FOR A NAVIGATION OUTAGE", unit=" BN", fmt="£{:.1f}", hi=1, tag=t, cues=[-1, 0]),
"P6-04b": floorbar,
"P6-05": lambda o, t: stacked([("EMERGENCY · SHIPPING · ROADS 87.6%", 87.6, ORANGE, 2), ("EVERYTHING ELSE", 12.4, DIM, -1)], title="WHERE THE £7.6BN LANDS", total="87.6%", tag=t),
"P6-06": iconrow,
"P6-06b": lambda o, t: split(("AVIATION · 7 DAYS", "≈ £4M", "backup systems"), ("EMERGENCY · SHIPPING · ROADS", "≈ £6.7BN", "far fewer backups"), tag=t),
"P6-06c": lambda o, t: split(("2017 REPORT", "£5.2BN", "a 5-day outage"), ("2023 REPORT", "£7.6BN", "a 7-day outage"), tag=t),
"P6-07": lambda o, t: number("$1 BN A DAY", sub="the cost to the US of losing GPS", kicker="RTI INTERNATIONAL FOR NIST · 2019", tag=t),
"P6-08": lambda o, t: calendar(["MAR", "APR", "MAY", "JUN"], circles=[(1, "PLANTING", 0), (2, "+50%", 0)], stamps=[(2, "+50%", 0)], title="IF IT HAPPENED IN PLANTING SEASON", tag=t),
"P6-08b": lambda o, t: number("$1.4 TRILLION", sub="value of GPS to US business since the 1980s", kicker="RTI / NIST · 2019", tag=t),
"P6-09": lambda o, t: pricetags([("UK HOME · WEEK", "£267", ORANGE, 0)], title="ON YOUR KITCHEN TABLE (OUR MATHS)", tag=t),
"P6-10": lambda o, t: pricetags([("US HOME · DAY", "$7.60", ORANGE, 0), ("US HOME · WEEK", "$53", RED, 0)], title="ON YOUR KITCHEN TABLE (OUR MATHS)", tag=t),
"P6-11": hidden,
"P6-11b": callerpin,
"P6-12": blanks,
"P6-13": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2"), ("SATELLITES DEAD FOR MONTHS", "LINE 3"), ("≈ 98% OF LOW ORBIT IN A WEEK", "LINE 4"), ("FORECAST · MAP · CLOCK · SIGNAL", "LINE 5"), ("≈ £50 / $7.60 PER HOME PER DAY", "LINE 6")], title="RUNNING TOTAL", tag=t, show=5),
"P7-01": P(7, "Why would anyone pull the trigger?"),
"P7-02": lambda o, t: space(n=200, die_at=lead(c(0, 1.5), 0.2), die_frac=1.0, R=140, colors=[PAPER_HI, CYAN, ORANGE, RED, GREEN], title="RADIATION DOESN'T CHECK FLAGS", tag=t),
"P7-03": lambda o, t: split(("WHO FIRED STARFISH?", "USA", "9 July 1962"), ("WHO LOST TELSTAR?", "USA", "early 1963"), tag=t),
"P7-04": lambda o, t: number("THREAT", sub="push too far, and the sky goes dark for everyone", kicker="WHAT IT MAY BE FOR", badge="NOT A FORECAST", tag=t),
"P7-04b": scale,
"P7-05": lambda o, t: tiles([("NEVER FLIES", "a bargaining chip"), ("PARKED IN ORBIT", "a loaded gun overhead"), ("USED", "what the studies describe")], title="THREE WAYS THIS COULD GO", tag=t, cues=[0, 9, 9]),
"P7-06": lambda o, t: tiles([("NEVER FLIES", "a bargaining chip"), ("PARKED IN ORBIT", "breaks the 1967 treaty"), ("USED", "what the studies describe")], title="SCENARIO 2", tag=t, cues=[-1, 0, 9]),
"P7-07": lambda o, t: tiles([("NEVER FLIES", "a bargaining chip"), ("PARKED IN ORBIT", "breaks the 1967 treaty"), ("USED", "what everyone wants to avoid")], title="SCENARIO 3", tag=t, cues=[-1, -1, 0]),
"P7-08": lambda o, t: quote("A nuclear war should never be fought", "Shenzhen declaration (US, China, Russia)", "19 Nov 2026", tag=t),
"P7-08b": lambda o, t: timeline([("JUL 1962", "Starfish Prime"), ("OCT 1962", "Cuban crisis"), ("AUG 1963", "Test ban signed")], [2], title="A SCARE, THEN A DEAL", tag=t),
"P7-09": lambda o, t: checklist(["AN UNEXPLAINED LAUNCH", "A NEW VOTE AT THE UN", "CONFIRMED IN ORBIT"], title="WHAT TO WATCH", tag=t),
"P7-09b": lambda o, t: card(["THE PEOPLE WHO PAY DON'T DECIDE"], tag=t),
"P7-10": lambda o, t: receipt([("BANNED · DENIED · WEEKS AWAY?", "LINE 1"), ("ONE BLAST · 1,450 KM AWAY", "LINE 2"), ("SATELLITES DEAD FOR MONTHS", "LINE 3"), ("≈ 98% OF LOW ORBIT IN A WEEK", "LINE 4"), ("FORECAST · MAP · CLOCK · SIGNAL", "LINE 5"), ("≈ £50 / $7.60 PER HOME PER DAY", "LINE 6"), ("A THREAT OVER EVERYONE", "LINE 7")], title="RUNNING TOTAL", tag=t, show=6),
}
RC_LINES = [("SPUTNIK-S: BANNED · DENIED · WEEKS AWAY?", ""), ("1962: 300 LIGHTS OUT · 1,450 KM AWAY", ""), ("TELSTAR: DEAD IN 7 MONTHS", ""),
            ("≈ 98% OF LOW ORBIT IN A WEEK (STUDY)", ""), ("FORECAST · MAP · CLOCK · SIGNAL", ""), ("≈ £50 A DAY PER UK HOME (NAV ONLY)", ""), ("PAID BY: EVERYONE", "")]
SPEC["RC-01"] = lambda o, t: receipt(RC_LINES, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(6):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RC_LINES[:i+1], title="THE RECEIPT", tag="", show=i))(i)
def _rc08(o, t):
    im = receipt(RC_LINES, title="THE RECEIPT", tag="", show=6)
    stamp(im, "PAID BY EVERYONE", W/2 + 60, H - 95, c(1, sn(1)) + 0.4, size=70)
    return im
SPEC["RC-08"] = _rc08
SPEC["RC-09"] = lambda o, t: endcard("RUSSIA'S FUEL CRISIS", "Every crisis sends a bill. History keeps the receipts.")

def countdown(o, t):
    im = space(n=50, R=130, lon0=37, title="", tag=t)
    d = D(im); hit = c(0, 2.5); e = ease_io((_A.T - lead(hit, 1.0))/1.0)
    d.text((70, 60), "RUSSIA'S NUCLEAR SATELLITE", f(40, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    d.text((70, 112), "REPORTED · 23 NOV 2026", f(24, "inter"), alpha(ORANGE, seg(0.5, 0.4)))
    d.text((W - 330, 520), countup("60", e), f(150, "bebas"), alpha(RED, min(1, e*3))); d.text((W - 190, 610), "DAYS?", f(44, "bebas"), alpha(RED, seg(lead(hit, 0.2), 0.3)))
    return im

def tumble(o, t):
    im = space(n=12, R=130, colors=[GREY], title="KOSMOS 2553", tag=t); d = D(im); hit = c(0, 2.5)
    cx, cy = W/2 + 330, H/2 - 160; a = _A.T*(0.4 + 3.0*seg(lead(hit, 0.4), 0.6))
    for s_ in (-1, 1):
        d.line([(cx + s_*20*math.cos(a), cy + s_*20*math.sin(a)), (cx + s_*70*math.cos(a), cy + s_*70*math.sin(a))], CYAN, 12)
    d.rect((cx - 16, cy - 16, cx + 16, cy + 16), fill=GREY)
    stamp(im, "TUMBLING · 2025", W - 300, 470, hit + 0.3, size=60)
    return im

def burst_globe(o, t):
    im = base(); im = earth(im, W/2 - 60, H/2 + 40, 240, lon0=-20, lat0=-25); d = D(im); hit = c(0, 2.0)
    bx, by = W/2 + 90, H/2 - 60
    k = seg(lead(hit, 0.1), 0.25)
    if k > 0:
        im = glow(im, lambda g: g.ell((bx - 60, by - 60, bx + 60, by + 60), fill=(255, 245, 225, 255)), 50, 1.5*(1 - 0.7*seg(lead(hit, 0.1) + 0.5, 1.5))); d = D(im)
        r = 20 + 300*ease((_A.T - lead(hit, 0.1))/2.0); d.ell((bx - r, by - r, bx + r, by + r), outline=alpha(PAPER_HI, 0.7*(1 - seg(lead(hit, 0.1) + 1.0, 1.0))), width=3)
    d.text((70, 60), "THE SIMULATION", f(34, "inter"), alpha(PAPER_HI, seg(0.1, 0.4)))
    for j, l in enumerate(("1 MEGATON", "500 KM UP", "SOUTH ATLANTIC")):
        d.text((W - 360, 200 + j*60), l, f(44, "bebas"), alpha(ORANGE, seg(lead(hit, 0.3) + 0.6 + 0.3*j, 0.3)))
    tagline(im, t); return im
