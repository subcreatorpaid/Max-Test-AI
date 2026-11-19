# INV-012 graphics spec: script code -> lambda(on_screen, tag) -> PIL frame (anim12 globals T, CUES, SENTS).
# No gore, no patients: people are drawn only as plain icons.
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from anim12 import *
import anim12 as _A

AFRICA = (-20, -36, 55, 38); DRC = (11.0, -14.0, 36.5, 7.0); EAST = (26.5, -3.6, 31.6, 3.6); ITURI = (28.9, 0.6, 31.6, 3.2)
EUR = (-11, 35, 31, 60); WORLD = (-110, -40, 60, 62); USA = (-126, 23, -64, 50)
MONG = (30.04, 1.95); BUNIA = (30.25, 1.56); BENI = (29.47, 0.49); BUTEMBO = (29.29, 0.14); GOMA = (29.22, -1.68); BUKAVU = (28.86, -2.5)
KISANGANI = (25.19, 0.52); RUBAYA = (28.88, -1.55); KAMPALA = (32.58, 0.35); KINSHASA = (15.27, -4.33); KOLWEZI = (25.47, -10.71)
NAIROBI = (36.82, -1.29); LAGOS = (3.38, 6.52); ARU = (30.86, 2.86); ISIRO = (27.62, 2.77); KATANA = (28.83, -2.22); RWAMPARA = (30.18, 1.50)
DJUGU = (30.5, 1.92); LUBERO = (29.24, -0.16); MASISI = (28.82, -1.40); OICHA = (29.52, 0.70); KIGALI = (30.06, -1.95)
PARIS = (2.35, 48.86); BERLIN = (13.4, 52.52); AMS = (4.9, 52.37); GENEVA = (6.14, 46.2); LONDON = (-0.13, 51.5); BRUSSELS = (4.35, 50.85)
IAD = (-77.45, 38.95)

def roadmap(o, t, items):
    im = base(); d = D(im); n = len(items); gap = (W - 240) / (n - 1)
    d.line([(120, 360), (W - 120, 360)], DIM, 4)
    for i, lab in enumerate(items):
        t0 = 0.5 + i * (_A.DUR - 1.5) / n
        if i == 3 and _A.CUES: t0 = lead(_A.CUES[0], 0.2)
        a = seg(t0, 0.4); x = 120 + i*gap
        d.ell((x - 22, 338, x + 22, 382), fill=alpha(ORANGE if a > 0.5 else DIM, max(0.3, a)))
        center(d, 410, lab, fit(d, lab, 28, gap - 10), alpha(PAPER_HI, max(0.25, a)), cx=x)
        pulse_rings(d, x, 360, ORANGE, t0, 1, 50, 0.5)
    tagline(im, t); return im

def figures(o, t, n=50, cols=10, title="", cue=0, grey_every=1, crimson_every=None, hit_txt=None, found=None):
    """plain person icons; they fade to grey one by one (deaths) - no faces, no bodies."""
    im = base(); d = D(im); hit = c(cue, 1.0)
    if title: center(d, 60, title.upper(), fit(d, title.upper(), 34, 900), alpha(PAPER_HI, seg(0, 0.4)))
    rows = math.ceil(n / cols); sx = min(96, (W - 300) / cols); sy = min(110, (H - 260) / rows); x0 = (W - sx*cols)/2 + sx*0.25; y0 = 140
    for i in range(n):
        x = x0 + (i % cols)*sx; y = y0 + (i // cols)*sy; a = seg(0.02*i, 0.25)
        col = PAPER
        t0 = lead(hit, 0.4) + i*0.045
        if crimson_every and i % crimson_every == crimson_every - 1: col = mix(PAPER, CRIMSON, seg(t0, 0.3))
        elif found is not None: col = mix(PAPER, CYAN if i < found else (60, 56, 52), seg(t0, 0.3))
        elif not crimson_every: col = mix(PAPER, (70, 66, 60), seg(t0, 0.3))
        r = sx*0.16
        d.ell((x - r, y, x + r, y + 2*r), fill=alpha(col, a)); d.rrect((x - r*1.5, y + 2.3*r, x + r*1.5, y + 5.6*r), 8, fill=alpha(col, a))
    if hit_txt: center(d, H - 150, hit_txt, f(40, "inter"), alpha(ORANGE, seg(hit + 1.0, 0.5)))
    tagline(im, t); return im

def counter2(o, t):
    im = base(); d = D(im); hit = c(0, 1.5); e = ease_io((_A.T - lead(hit, 1.4))/1.4); e2 = ease_io((_A.T - lead(hit + 1.6, 1.2))/1.2)
    center(d, 110, "CONGO EBOLA OUTBREAK · CONFIRMED", f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    center(d, 620, "SIX MONTHS AFTER IT WAS DECLARED · 15 MAY 2026", f(30, "serif"), alpha(PAPER, seg(0.3, 0.6)))
    center(d, 180, countup("11,376", e), f(150, "inter"), alpha(PAPER_HI, min(1, e*4))); center(d, 350, "CASES", f(34, "inter"), alpha(PAPER, seg(hit, 0.4)))
    center(d, 410, countup("5,568", e2), f(130, "inter"), alpha(CRIMSON, min(1, e2*4))); center(d, 560, "DEATHS", f(34, "inter"), alpha(PAPER, seg(hit + 1.6, 0.4)))
    stamp(im, "ECDC · 15 NOV 2026", W - 230, 420, hit + 2.8, col=ORANGE, size=40, angle=-6)
    tagline(im, t); return im

def phone_link(o, t):
    """phone outline -> glowing capacitor -> line out to a map pin"""
    im = base(); d = D(im); a = seg(0.1, 0.5); hit = c(0, 2.0)
    x, y = 300, 130
    d.rrect((x, y, x + 260, y + 480), 34, outline=alpha(PAPER_HI, a), width=6); d.rrect((x + 20, y + 40, x + 240, y + 420), 14, fill=alpha((30, 32, 36), a))
    k = seg(lead(hit, 0.3), 0.5); cx, cy = x + 130, y + 300
    d.rect((cx - 30, cy - 16, cx + 30, cy + 16), fill=alpha(ORANGE, max(0.2, k))); d.text((cx - 70, cy + 30), "CAPACITOR", f(22, "inter"), alpha(ORANGE, k))
    if k > 0: im = glow(im, lambda g: g.rect((cx - 34, cy - 20, cx + 34, cy + 20), fill=(232, 89, 12, 220)), 22, k); d = D(im)
    e = seg(hit + 0.6, 1.2); xe = cx + (1000 - cx)*e; ye = cy + (330 - cy)*e
    if e > 0: d.line([(cx + 30, cy), (xe, ye)], ORANGE, 4)
    if e >= 1:
        d.ell((1000 - 14, 330 - 14, 1000 + 14, 330 + 14), fill=RED); pulse_rings(d, 1000, 330, RED, hit + 1.8, 2, 50)
        d.text((900, 370), "ITURI · EASTERN CONGO", f(30, "inter"), PAPER_HI); d.text((900, 410), "GOLD · TIN · TANTALUM", f(24, "reg"), PAPER)
    tagline(im, t); return im

def risk_after(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    center(d, 80, "WHERE THE VIRUS IS (SCHEMATIC)", f(30, "inter"), alpha(ORANGE, seg(0, 0.4)))
    x0, x1, yb = 200, W - 160, 560; xm = (x0 + x1)/2
    d.line([(x0, yb), (x1, yb)], DIM, 3)
    e = ease_io((_A.T - 0.4)/max(1, hit + 1.5 - 0.4)); pts = []
    for i in range(61):
        q = i/60
        if q > e: break
        v = 0.15 + 0.5*q if q < 0.5 else 0.4 + 0.55*min(1, (q - 0.5)*3)
        pts.append((x0 + (x1 - x0)*q, yb - 380*v))
    if len(pts) > 1: d.line(pts, CRIMSON, 7)
    k = seg(lead(hit, 0.3), 0.4); d.line([(xm, 150), (xm, yb)], alpha(PAPER, k), 3); center(d, yb + 20, "DEATH", f(30, "inter"), alpha(PAPER_HI, k), cx=xm)
    center(d, yb + 20, "ILLNESS", f(26, "reg"), alpha(PAPER, seg(0.4, 0.4)), cx=x0 + 140); center(d, yb + 20, "BURIAL", f(26, "reg"), alpha(PAPER, seg(hit + 0.6, 0.4)), cx=x1 - 140)
    tagline(im, "SHAPE ILLUSTRATIVE · WHO: BODIES STAY INFECTIOUS"); return im

def lab_report(o, t):
    im = base(); d = paper(im, (330, 120, W - 330, H - 140), seed=14); hit = c(0, 2.0)
    d.text((370, 150), "LABORATORY RESULT (RECREATED)", f(26, "inter"), (120, 40, 20)); d.line([(370, 192), (W - 370, 192)], (60, 50, 40), 2)
    for i, (l, at) in enumerate([("SAMPLE ........ 30 APR 2026", 0.5), ("TESTED FOR ..... EBOLA (ZAIRE)", 1.4), ("RESULT ......... ", 2.4)]):
        typewriter(d, (380, 230 + i*72), l, f(36, "inter"), (30, 26, 22), at, 32)
    stamp(im, "NEGATIVE", W/2 + 60, H - 230, hit, col=CRIMSON, size=96)
    tagline(im, t); return im

def big_word(o, t, word, sub=""):
    im = base(); d = D(im); hit = c(0, 1.0); a = seg(lead(hit, 0.3), 0.4)
    fo = fit(d, word, 200, W - 160)
    center(d, 220 + (1 - a)*30, word, fo, alpha(PAPER_HI, a))
    if sub: center(d, 470, sub, f(40, "serif"), alpha(ORANGE, seg(hit + 0.4, 0.5)))
    im = sweep(im, (0, 200, W, 440), hit + 0.4, 1.3)
    tagline(im, t); return im

def tree(o, t, lit=0):
    """Ebola family tree: lit=0 Zaire orange; lit=1 Bundibugyo crimson."""
    im = base(); d = D(im); a = seg(0.1, 0.5)
    d.rrect((W/2 - 200, 100, W/2 + 200, 180), 12, fill=alpha((40, 37, 34), a), outline=alpha(PAPER, a), width=3); center(d, 120, "EBOLA VIRUSES", f(34, "inter"), alpha(PAPER_HI, a))
    kids = ["ZAIRE", "SUDAN", "BUNDIBUGYO", "TAÏ FOREST", "RESTON"]; gap = (W - 200) / len(kids)
    for i, k_ in enumerate(kids):
        x = 100 + gap*i + gap/2; t0 = 0.4 + 0.2*i; b = seg(t0, 0.4)
        d.line([(W/2, 180), (x, 300)], alpha(DIM, b), 3)
        hot = (lit == 0 and i == 0) or (lit == 1 and i == 2); cue_t = lead(c(0, 1.5), 0.3)
        col = PAPER
        if hot: col = mix(PAPER, ORANGE if lit == 0 else CRIMSON, seg(cue_t, 0.4))
        elif lit == 1 and i == 0: col = mix(PAPER, ORANGE, 0.6)
        d.rrect((x - gap/2 + 12, 300, x + gap/2 - 12, 380), 10, fill=alpha((40, 37, 34), b), outline=alpha(col, b), width=4 if hot else 2)
        center(d, 322, k_, fit(d, k_, 30, gap - 40), alpha(col, b), cx=x)
        if hot: pulse_rings(d, x, 340, col, cue_t, 2, 80)
    sub = "WEST AFRICA 2014-16 · MOST PAST CONGO OUTBREAKS" if lit == 0 else "FIRST FOUND: BUNDIBUGYO DISTRICT, UGANDA, 2007"
    center(d, 460, sub, f(32, "serif"), alpha(ORANGE, seg(lead(c(0, 1.5), 0.0) + 0.6, 0.5)))
    tagline(im, t); return im

def shelves(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    for i, lab in enumerate(["VACCINE", "TREATMENT"]):
        x = 260 + i*440; a = seg(0.2 + 0.4*i, 0.5)
        d.rect((x, 200, x + 320, 460), outline=alpha(PAPER, a), width=4); d.line([(x, 330), (x + 320, 330)], alpha(PAPER, a), 3)
        center(d, 480, lab, f(38, "inter"), alpha(PAPER_HI, a), cx=x + 160)
        center(d, 250, "—", f(60, "inter"), alpha(GREY, a), cx=x + 160)
    stamp(im, "NONE LICENSED", W/2, 600, hit, col=CRIMSON, size=70, angle=-4)
    tagline(im, t); return im

def vial(o, t):
    im = base(); d = D(im); a = seg(0.1, 0.5); hit = c(0, 1.0)
    x, y = 380, 160
    d.rect((x, y, x + 90, y + 40), fill=alpha(GREY, a)); d.rrect((x - 10, y + 40, x + 100, y + 380), 16, outline=alpha(PAPER_HI, a), width=5)
    d.rect((x + 6, y + 200, x + 84, y + 370), fill=alpha(CYAN, 0.6*a))
    d.text((620, 220), "ERVEBO", f(80, "inter"), alpha(PAPER_HI, seg(lead(hit, 0.3), 0.4)))
    d.text((620, 330), "BUILT FOR: ZAIRE", f(40, "inter"), alpha(ORANGE, seg(hit + 0.5, 0.4)))
    d.text((620, 400), "AGAINST BUNDIBUGYO: ?", f(40, "inter"), alpha(CRIMSON, seg(sn(1), 0.4)))
    tagline(im, t); return im

def twostep(o, t, a_txt, b_txt, ka="28 MAY", kb="NOW"):
    im = base(); d = D(im)
    for i, (k_, tx, t0) in enumerate([(ka, a_txt, 0.3), (kb, b_txt, sn(1) - 0.2 if len(_A.SENTS) > 1 else 2.0)]):
        e = seg(t0, 0.5); x = 140 + i*540
        dd = paper(im, (x, 210 + (1 - e)*40, x + 460, 470 + (1 - e)*40), seed=40 + i) if e > 0 else None
        if dd:
            dd.text((x + 30, 236 + (1 - e)*40), k_, f(30, "inter"), (120, 40, 20))
            for j, l in enumerate(wrap(dd, tx, f(40, "inter"), 400)): dd.text((x + 30, 296 + j*52 + (1 - e)*40), l, f(40, "inter"), (30, 26, 22))
    d = D(im); k = seg(sn(1) - 0.4 if len(_A.SENTS) > 1 else 1.8, 0.4); d.line([(610, 340), (610 + 60*k, 340)], ORANGE, 6)
    tagline(im, t); return im

def two_vials(o, t):
    im = base(); d = D(im); hit = c(0, 1.5)
    for i, lab in enumerate(["REMDESIVIR", "MBP-134"]):
        x = 300 + i*420; a = seg(lead(hit, 0.3) + 0.4*i, 0.4)
        d.rect((x + 40, 170, x + 120, 200), fill=alpha(GREY, a)); d.rrect((x + 30, 200, x + 130, 470), 14, outline=alpha(PAPER_HI, a), width=4)
        d.rect((x + 36, 340, x + 124, 462), fill=alpha(ORANGE, 0.55*a)); center(d, 500, lab, f(36, "inter"), alpha(PAPER_HI, a), cx=x + 80)
    stamp(im, "TRIALS · 12 JUL", W/2 + 330, 200, hit + 1.2, col=ORANGE, size=54)
    tagline(im, t); return im

def race_days(o, t):
    """horizontal race bars: 2026 40 days vs 2018 235 days (second bar on cue of the next row)."""
    im = base(); d = D(im); hit = c(0, 1.5)
    center(d, 70, "DAYS TO 1,000 CONFIRMED CASES", f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    x0, x1 = 300, W - 140
    x1 = W - 400
    for i, (lab, v, t0, col) in enumerate([("CONGO 2026", 40, lead(hit, 0.8), CRIMSON), ("CONGO 2018", 235, (lead(hit, 0.8) if _A.CUES and o.startswith("2018") else 99), GREY)]):
        if o.startswith("2018") and i == 0: t0 = 0.2
        e = ease_io((_A.T - t0)/1.0); y = 220 + i*170
        d.text((80, y + 20), lab, f(32, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
        w = (x1 - x0)*v/235*e
        if e > 0: d.rect((x0, y, x0 + w, y + 90), fill=col); d.text((x0 + w + 20, y + 20), countup(str(v), e) + " DAYS", f(44, "inter"), alpha(PAPER_HI, min(1, e*3)))
    tagline(im, t); return im

def map_pins(bbox, z, pts, title, t, hi=(), hi2=(), cues=None, extra_lines=(), arcs=(), rings=(), labels=()):
    pins = [(lo, la, lab, col, (cues[i] if cues and i < len(cues) else None)) for i, (lo, la, lab, col) in enumerate(pts)]
    return map_scene(bbox, z, hi=hi, hi2=hi2, pins=pins, lines=list(extra_lines), arcs=list(arcs), rings=list(rings), title=title, tag=t, labels=list(labels))

def provinces(o, t):
    im = map_scene(DRC, 5, hi=["Democratic Republic of the Congo"], pins=[(*BUNIA, "ITURI", RED, None), (*GOMA, "NORTH KIVU", RED, None), (27.6, 3.0, "HAUT-UELE", ORANGE, None),
                   (*KISANGANI, "TSHOPO", ORANGE, None), (24.8, 3.6, "BAS-UELE", WARN, None), (21.5, 3.6, "NORD-UBANGI", WARN, None), (*BUKAVU, "SOUTH KIVU", WARN, None), (19.0, 3.0, "SUD-UBANGI", WARN, None)],
                   title="8 OF 26 PROVINCES · 68 HEALTH ZONES", tag=t)
    d = D(im); hit = c(0, 1.5); e = ease_io((_A.T - lead(hit, 0.6))/0.8)
    d.rect((60, 520, 420, 660), fill=(0, 0, 0, 170)); d.text((90, 530), countup("68", e), f(96, "inter"), ORANGE); d.text((230, 575), "HEALTH ZONES", f(26, "inter"), PAPER)
    return im

def france_overlay(o, t):
    im = map_scene((14.0, -14.0, 44.0, 12.0), 5, hi2=[], pins=[(*BUNIA, "BUNIA", PAPER_HI, None), (*GOMA, "GOMA", PAPER_HI, None)], title="'AN AREA THE SIZE OF FRANCE'", tag=t)
    m = Map((14.0, -14.0, 44.0, 12.0), 5, (), [])
    d = D(im); k = seg(lead(c(0, 2.0), 0.5), 0.8)
    if k > 0:
        for rec, shp in shapes():
            if (rec.get("ADMIN") or rec.get("NAME")) != "France": continue
            pts = shp.points; parts = list(shp.parts) + [len(pts)]
            for a_, b_ in zip(parts[:-1], parts[1:]):
                raw = pts[a_:b_]
                if len(raw) < 200: continue   # mainland only
                cx_ = sum(p[0] for p in raw)/len(raw); cy_ = sum(p[1] for p in raw)/len(raw)
                if not (40 < cy_ < 52): continue
                ring = [m.P(29.5 + (lo - cx_)*math.cos(math.radians(cy_)), 0.3 + (la - cy_)) for lo, la in raw]
                d.line(ring + [ring[0]], alpha(PAPER_HI, k), 4)
        d.text((m.P(26.0, 6.2)[0], m.P(26.0, 6.2)[1]), "FRANCE (SAME SCALE)", f(26, "inter"), alpha(PAPER_HI, k))
    return im

def iceberg(o, t):
    im = base(); d = D(im); hit = c(0, 1.5); y = 300
    d.line([(100, y), (W - 100, y)], CYAN, 3); a = seg(0.2, 0.5)
    d.poly([(W/2 - 160, y), (W/2 - 40, 140), (W/2 + 90, 190), (W/2 + 170, y)], fill=alpha(PAPER_HI, a)); center(d, 230, "CONFIRMED", f(30, "inter"), alpha(INK, a))
    k = seg(lead(hit, 0.2) + 1.0, 0.6)
    pts = [(W/2 - 170, y), (W/2 - 330, 470), (W/2 - 120, 620), (W/2 + 260, 580), (W/2 + 330, 420), (W/2 + 180, y)]
    for i in range(len(pts) - 1):
        for q in range(0, 10, 2):
            a0 = q/10; a1 = (q + 1)/10; p0 = pts[i]; p1 = pts[i + 1]
            d.line([(p0[0] + (p1[0] - p0[0])*a0, p0[1] + (p1[1] - p0[1])*a0), (p0[0] + (p1[0] - p0[0])*a1, p0[1] + (p1[1] - p0[1])*a1)], alpha(PAPER, k), 3)
    center(d, 440, "SUSPECTED · DEATHS AT HOME · NOT COUNTED", f(28, "inter"), alpha(PAPER, k))
    tagline(im, t); return im

def clock16(o, t):
    im = base(); d = D(im); cx, cy, r = W/2 - 220, 360, 210; a = seg(0.1, 0.5); hit = c(0, 2.0)
    d.ell((cx - r, cy - r, cx + r, cy + r), outline=alpha(PAPER, a), width=6)
    for i in range(12):
        ang = math.radians(i*30 - 90); d.line([(cx + math.cos(ang)*(r - 24), cy + math.sin(ang)*(r - 24)), (cx + math.cos(ang)*(r - 6), cy + math.sin(ang)*(r - 6))], alpha(PAPER, a), 4)
    n = int(max(0, min(4, (_A.T - lead(hit, 1.0))/0.35))) if _A.T > lead(hit, 1.0) else 0
    for i in range(n + 1 if _A.T > lead(hit, 1.0) else 0):
        ang = math.radians(i*16/60*360 - 90); x, y = cx + math.cos(ang)*(r - 50), cy + math.sin(ang)*(r - 50)
        d.ell((x - 12, y - 12, x + 12, y + 12), fill=CRIMSON)
    ang = math.radians((_A.T*40) % 360 - 90); d.line([(cx, cy), (cx + math.cos(ang)*(r - 40), cy + math.sin(ang)*(r - 40))], ORANGE, 5)
    d.text((W/2 + 60, 260), "≈ 1 NEW CASE", f(56, "inter"), alpha(PAPER_HI, seg(lead(hit, 0.3), 0.4)))
    d.text((W/2 + 60, 330), "EVERY 16 MINUTES", f(56, "inter"), alpha(CRIMSON, seg(hit, 0.4)))
    d.text((W/2 + 60, 420), "179 cases in ~2 days, mid-Nov", f(30, "serif"), alpha(ORANGE, seg(hit + 0.5, 0.4)))
    tagline(im, t); return im

def net(o, t):
    """contact net: inner web of traced dots; most new dots appear outside it."""
    im = base(); d = D(im); rng = random.Random(7); hit = c(0, 2.0); cx, cy = W/2 - 120, 380
    pts = [(cx + 200*math.cos(i/12*6.283), cy + 150*math.sin(i/12*6.283)) for i in range(12)]
    a = seg(0.2, 0.5)
    for i, p in enumerate(pts):
        d.line([(cx, cy), p], alpha(CYAN, 0.5*a), 2); d.line([p, pts[(i + 1) % 12]], alpha(CYAN, 0.5*a), 2)
        d.ell((p[0] - 8, p[1] - 8, p[0] + 8, p[1] + 8), fill=alpha(CYAN, a))
    d.ell((cx - 12, cy - 12, cx + 12, cy + 12), fill=alpha(PAPER_HI, a))
    for j in range(20):
        t0 = lead(hit, 0.5) + j*0.12; k = seg(t0, 0.3)
        if k <= 0: continue
        inside = j % 5 == 0
        ang = rng.random()*6.283; rr = (rng.random()*120) if inside else (260 + rng.random()*180)
        x, y = cx + rr*math.cos(ang), cy + rr*0.8*math.sin(ang); y = max(130, min(H - 120, y))
        d.ell((x - 9*k, y - 9*k, x + 9*k, y + 9*k), fill=RED if not inside else CYAN)
    d.text((W - 400, 200), "CONTACT LIST", f(30, "inter"), alpha(CYAN, a)); d.text((W - 400, 250), "NEW CASES", f(30, "inter"), alpha(RED, seg(hit, 0.4)))
    tagline(im, t); return im

def payslip(o, t):
    im = base(); d = paper(im, (330, 130, W - 330, H - 150), seed=22); hit = c(0, 1.0)
    d.text((370, 160), "HEALTH WORKER PAYSLIP (ILLUSTRATIVE)", f(26, "inter"), (120, 40, 20)); d.line([(370, 202), (W - 370, 202)], (60, 50, 40), 2)
    for i, (l, at) in enumerate([("ROLE ......... NURSE, EBOLA WARD", 0.4), ("MONTHS ....... SEVERAL", lead(hit, 0.8)), ("SALARY ....... UNPAID", hit)]):
        typewriter(d, (380, 240 + i*70), l, f(34, "inter"), (30, 26, 22), at, 34)
    stamp(im, "STRIKE · JUL 2026", W/2 + 120, H - 230, sn(1) + 0.4 if len(_A.SENTS) > 1 else hit + 2, col=CRIMSON, size=60)
    tagline(im, t); return im

def overlap(o, t):
    """outbreak heat circles over mining zones in eastern DRC"""
    im = map_scene(EAST, 7, pins=[(*BUNIA, "BUNIA", PAPER_HI, None), (*GOMA, "GOMA", PAPER_HI, None), (*RUBAYA, "RUBAYA", ORANGE, None), (*MONG, "MONGBWALU", ORANGE, None)],
                   title="THE OUTBREAK SITS ON THE MINES", tag=t)
    d = D(im); m = Map(EAST, 7); hit = c(0, 2.0)
    for (lo, la, r) in [(30.15, 1.7, 110), (29.4, 0.3, 90), (29.1, -1.6, 70)]:
        x, y = m.P(lo, la); k = seg(0.5, 0.8)
        for q in range(3): d.ell((x - r*(1 + q*0.3)*k, y - r*(1 + q*0.3)*k, x + r*(1 + q*0.3)*k, y + r*(1 + q*0.3)*k), outline=alpha(RED, 0.5 - q*0.15), width=3)
    for i, (lo, la) in enumerate([(30.0, 1.95), (30.4, 1.4), (29.6, 0.6), (29.0, -1.5), (28.9, -1.6), (29.3, 0.0), (30.2, 2.2)]):
        x, y = m.P(lo, la); k = seg(lead(hit, 0.4) + i*0.12, 0.3)
        if k > 0: d.rect((x - 10, y - 10, x + 10, y + 10), fill=alpha(WARN, k)); d.line([(x - 14, y + 14), (x + 14, y - 14)], alpha(INK, k), 3)
    d.text((60, H - 100), "● OUTBREAK HOT SPOTS   ■ MINING AREAS (APPROXIMATE)", f(22, "inter"), PAPER)
    return im

def scale(o, t):
    im = base(); d = D(im); hit = c(0, 2.0); k = seg(lead(hit, 0.4), 0.8); tilt = 40*k
    cx, cy = W/2, 280
    d.line([(cx, cy), (cx, 580)], PAPER, 6); d.poly([(cx - 70, 600), (cx + 70, 600), (cx, 560)], fill=PAPER)
    xl, yl = cx - 320, cy - tilt; xr, yr = cx + 320, cy + tilt
    d.line([(xl, yl), (xr, yr)], PAPER, 6)
    d.rect((xl - 40, yl + 20, xl + 40, yl + 70), fill=CYAN); center(d, yl + 80, "$1.6BN", f(36, "inter"), PAPER_HI, cx=xl); center(d, yl + 124, "THE FIX NOT RELEASED", f(22, "reg"), PAPER, cx=xl)
    d.rect((xr - 110, yr + 20, xr + 110, yr + 190), fill=CRIMSON); center(d, yr + 80, "$53BN", f(56, "inter"), PAPER_HI, cx=xr); center(d, yr + 200, "WEST AFRICA'S BILL", f(22, "reg"), PAPER, cx=xr)
    if k > 0.9: stamp(im, "≈ 3%", W/2, 140, hit + 0.9, col=ORANGE, size=80, angle=-4, box=False)
    tagline(im, t); return im

def form21(o, t):
    im = base(); d = paper(im, (300, 140, W - 300, H - 160), seed=33); hit = c(0, 2.0)
    d.text((340, 170), "PASSENGER ATTESTATION (RECREATED)", f(26, "inter"), (120, 40, 20)); d.line([(340, 212), (W - 340, 212)], (60, 50, 40), 2)
    for i, l in enumerate(["In the last 21 days, have you been", "in the Democratic Republic of the Congo?"]): d.text((340, 250 + i*52), l, fit(d, l, 34, W - 700, "reg"), (30, 26, 22))
    d.rect((360, 400, 400, 440), outline=(30, 26, 22), width=3); d.text((420, 402), "NO", f(36, "inter"), (30, 26, 22))
    k = seg(lead(hit, 0.2), 0.3)
    if k > 0: d.line([(364, 420), (376, 434)], RED, 6); d.line([(376, 434), (364 + 40*k, 404 - 10*k)], RED, 6)
    d.text((340, 480), "Required on international flights into the US since 3 Nov 2026", fit(d, "Required on international flights into the US since 3 Nov 2026", 24, W - 700, "reg"), (90, 80, 70))
    tagline(im, t); return im

def loop(o, t):
    im = base(); d = D(im); steps = ["HUNGER", "FAMILIES MOVE", "UNTRACED", "NEW CASES"]; cx, cy, r = W/2, 370, 210
    for i, s in enumerate(steps):
        ang = math.radians(-90 + i*90); x, y = cx + r*math.cos(ang), cy + r*math.sin(ang)
        t0 = sn(i) - 0.2 if i < len(_A.SENTS) else 0.5 + i; a = seg(t0, 0.4)
        d.rrect((x - 130, y - 36, x + 130, y + 36), 10, fill=alpha((40, 37, 34), a), outline=alpha(ORANGE, a), width=3)
        center(d, y - 16, s, f(26, "inter"), alpha(PAPER_HI, a), cx=x)
    rot = (_A.T*35) % 360
    d.arc((cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30), rot, rot + 250, fill=alpha(CRIMSON, seg(1.0, 0.6)), width=5)
    tagline(im, t); return im

def calendar21(o, t):
    im = base(); d = D(im); hit = c(0, 1.5)
    center(d, 70, "21 DAYS, THEN WASHINGTON", f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i in range(21):
        x = 200 + (i % 7)*110; y = 150 + (i // 7)*110; d.rect((x, y, x + 90, y + 90), outline=PAPER, width=2); center(d, y + 26, str(i + 1), f(30, "inter"), PAPER, cx=x + 45)
        k = seg(lead(hit, 0.6) + i*0.08, 0.15)
        if k > 0: d.line([(x + 10, y + 10), (x + 80, y + 80)], alpha(RED, k), 5)
    k = seg(lead(hit, 0.6) + 21*0.08, 0.8)
    if k > 0:
        x = 1000 + 120*k; d.poly([(x - 40, 300), (x + 40, 300), (x + 50, 290), (x + 50, 310)], fill=PAPER_HI); d.text((960, 340), "WASHINGTON", f(32, "inter"), alpha(PAPER_HI, k))
    tagline(im, t); return im

FULL = [("HEAD START", "≈ 3 MONTHS"), ("CASES · NO VACCINE", "11,376"), ("TRACING MISSED", "> 80%"), ("YOUR PHONE", "SAME HILLS"),
        ("AID NOT RELEASED", "$1.6BN"), ("PAID BY", "THEM, FIRST")]
RUN = [("HEAD START", "≈ 3 MONTHS"), ("VACCINE", "NONE LICENSED"), ("PACE", "1 CASE / 16 MIN"), ("TRACING", "> 80% MISSED"),
       ("THE WAR", "KEEPS DOCTORS OUT"), ("YOUR PHONE", "SAME HILLS"), ("HUNGER", "30.3M (RECORD)"), ("AID", "$1.6BN NOT RELEASED")]
def run_line(n, t):   # running receipt: n-th line prints on the row's cue
    return receipt(RUN[:n], title="RUNNING TOTAL", tag=t, show=n - 1, cues_from=[c(0, 1.5)])

SPEC = {
"CO-01": lambda o, t: map_scene(ITURI, 8, hi2=[], pins=[(*BUNIA, "BUNIA", PAPER_HI, None), (*MONG, "MONGBWALU · GOLD TOWN", PAPER_HI, None)] + ([(*MONG, "", RED, 0)] if _A.T > c(0, 9) - 0.3 else []), title="ITURI · EASTERN CONGO · 4 FEB 2026", tag=t, labels=[(30.8, 2.9, "UGANDA →", 28, PAPER)]),
"CO-02": lambda o, t: figures(o, t, 50, 10, "IN THE WEEKS THAT FOLLOWED", 0, hit_txt="≈ 50 DEATHS · NO TEST"),
"CO-03": counter2,
"CO-04": lambda o, t: quote("Still not under control.", "Jean Kaseya, Africa CDC", "15 Nov 2026", tag=t, cue=9),
"CO-05": phone_link,
"CO-06": lambda o, t: roadmap(o, t, ["THE FUNERAL", "THE VIRUS", "THE WAR", "THE GOLD", "YOUR BILL"]),
"P1-01": lambda o, t: part(1, "The funeral"),
"P1-02": lambda o, t: map_scene(AFRICA, 4, hi=["Democratic Republic of the Congo"], pins=[(*BUNIA, "ITURI", RED, 0)], title="ITURI · NORTH-EAST CONGO", tag=t) if _A.T < c(0, 1.5) + 1.8 else
          map_scene(ITURI, 8, hi2=["Uganda"], pins=[(*MONG, "MONGBWALU", ORANGE, None), (*BUNIA, "BUNIA", PAPER_HI, None)], title="A TOWN BUILT ON GOLD", tag=t),
"P1-02b": lambda o, t: map_scene(ITURI, 8, pins=[(*MONG, "MONGBWALU", ORANGE, None), (*BUNIA, "BUNIA", PAPER_HI, 0), (30.5, 1.92, "", WARN, None), (29.95, 2.2, "", WARN, None), (30.3, 2.3, "", WARN, None)],
          lines=[(MONG, BUNIA, PAPER, 4, None, False), (MONG, (29.95, 2.2), PAPER, 3, None, True), (BUNIA, (30.5, 1.92), PAPER, 3, None, True), (MONG, (30.3, 2.3), PAPER, 3, None, True)],
          streams=(BUNIA, [MONG, (30.5, 1.92), (29.95, 2.2)], 60, 0), title="ROADS BETWEEN MINES AND TOWNS", tag=t),
"P1-05": risk_after,
"P1-06": lambda o, t: map_scene(ITURI, 8, pins=[(*MONG, "THE FUNERAL", RED, 0)], shock=(*MONG, [("HOMES", 1), ("MARKETS", 2), ("MINES", 3)]),
          title="IT LEFT WITH THE MOURNERS", tag=t or "ILLUSTRATION · rings show spread, not real distances"),
"P1-06b": lambda o, t: calendar(["FEB", "MAR", "APR", "MAY"], stamps=[(1, "NOBODY LOOKING", 0)], flames_every=6, title="FUNERALS BEFORE ANYONE KNEW · FEB-MAY 2026", tag=t),
"P1-07": lambda o, t: timeline([("4 FEB", "Pastor's funeral, Mongbwalu"), ("27 MAR", "Red Cross volunteers handle bodies"), ("MAY", "All three volunteers die"), ("15 MAY", "Outbreak declared")], [1, 2], title="BEFORE THE ALARM", tag=t),
"P1-08": lambda o, t: tiles([("MALARIA", "fever, aches"), ("TYPHOID", "fever, weakness"), ("EBOLA?", "fever, at first")], title="IT LOOKED LIKE MALARIA", tag=t, cues=None),
"P1-09": lambda o, t: card(["LESS BLEEDING", "→ STAYED HOME"], kicker="WHY THE SICK WEREN'T SEEN", tag=t, cues=[0, 0] if False else None),
"P1-10": lab_report,
"P1-11": lambda o, t: big_word(o, t, "WRONG TEST", "It wasn't the Zaire strain"),
"P1-12": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0, cues_from=[c(0, 1.5)]),
"BR-01": lambda o, t: _sub(o, t),
"P2-01": lambda o, t: part(2, "The virus nobody tested for"),
"P2-02": lambda o, t: tree(o, t, 0),
"P2-03": lambda o, t: tree(o, t, 1),
"P2-04": lambda o, t: bars([("UGANDA · 2007", 37), ("ISIRO, CONGO · 2012", 13)], title="BUNDIBUGYO OUTBREAKS BEFORE 2026 · DEATHS", tag=t, cues=[0, 0]),
"P2-05": shelves,
"P2-05b": lambda o, t: _maths(o, t, ["37 deaths (Uganda 2007)", "+ 13 deaths (Isiro 2012)"], "= ≈ 50 · NO MARKET"),
"P2-06": vial,
"P2-06b": lambda o, t: twostep(o, t, "WHO: NOT ADVISED OUTSIDE TRIALS", "MAINLY INSIDE RESEARCH RULES"),
"P2-07": lambda o, t: typed(["MODERNA · $50 MILLION", "OXFORD · $8.6 MILLION", "IAVI · $3.2 MILLION"], label="CEPI VACCINE MONEY · 1 JUN 2026", tag=t, cue_lines=[0, 1, 2], title="STARTING FROM ZERO · NO VACCINE FOR THIS STRAIN"),
"P2-08": lambda o, t: calendar(["AUG", "SEP", "OCT", "NOV"], circles=[(0, "27 AUG · FRONTLINE WORKERS", -9), (2, "23 OCT · TRIAL IN BUNIA", 0)], title="ERVEBO GOES IN, UNDER RESEARCH RULES", tag=t),
"P2-09": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR"], circles=[(0, "TRIALS APPROVED", -9), (2, "RESULTS EXPECTED", 0)], title="TWO NEW VACCINES · TRIALS", tag=t),
"P2-09b": two_vials,
"P2-10": lambda o, t: gauge(49, "of confirmed cases have died", sub="5,568 of 11,376 · 15 Nov 2026", tag=t, valtxt=lambda e: "≈ " + countup("49", e) + "%"),
"P2-11": lambda o, t: chain(["Village", "Road", "Lab", "Result"], title="NO QUICK TEST · A PROPER LAB, HOURS AWAY", tag=t),
"P2-12": lambda o, t: run_line(2, t),
"P3-01": lambda o, t: part(3, "The fastest outbreak on record"),
"P3-02": race_days,
"P3-03": lambda o, t: race_days("2018", t),
"P3-04": lambda o, t: linechart({"CONGO 2026": [("DAY 0", 0), ("DAY 100", 5000)], "WEST AFRICA 2014": [("DAY 0", 0), ("DAY 100", 1000)]}, title="CONFIRMED CASES IN THE FIRST 100 DAYS",
          tag=t + " · SHAPE ILLUSTRATIVE BETWEEN POINTS", hit=c(1, 3.0), ylab_fmt="{:,.0f}"),
"P3-05": lambda o, t: map_pins(EAST, 7, [(*GOMA, "GOMA · 17 MAY", RED), (*BUTEMBO, "BUTEMBO · 18 MAY", ORANGE), (*BUKAVU, "BUKAVU · 21 MAY", ORANGE), (*BENI, "BENI · 29 MAY", ORANGE), (*BUNIA, "BUNIA", PAPER_HI)],
          "OUT OF ITURI", t, hi2=["Rwanda"], cues=[0, 1, 2, 3, None]),
"P3-06": provinces,
"P3-06b": france_overlay,
"P3-07": lambda o, t: bars([("ITURI", 7858), ("NORTH KIVU", 2860), ("HAUT-UELE", 523), ("5 OTHERS", 135)], title="CONFIRMED CASES BY PROVINCE · 15 NOV", tag=t, cues=[-5, 0, 0, 0]),
"P3-08": lambda o, t: map_pins((-8, -14, 46, 16), 5, [(*KAMPALA, "UGANDA · 20", ORANGE), (*NAIROBI, "KENYA · 9", ORANGE), (*LAGOS, "NIGERIA · 1", ORANGE)], "BEYOND CONGO", t, hi2=["Democratic Republic of the Congo"], cues=[None, 0, 1]),
"P3-08b": lambda o, t: timeline([("19 MAY", "No handshakes, no hugs"), ("27 MAY", "Border with Congo shut"), ("28 JUL", "Outbreak declared over")], [0, 1, 2], title="UGANDA SHUTS IT DOWN", tag=t),
"P3-09": lambda o, t: map_scene(AFRICA, 4, pins=[(*NAIROBI, "EAST", ORANGE, None), (*BUNIA, "CENTRAL", RED, None), (*LAGOS, "WEST", ORANGE, 0)], title="THE WIDEST SPREAD OF ANY EBOLA OUTBREAK IN AFRICA", tag=t,
          hi=["Kenya", "Uganda", "Nigeria"], hi2=["Democratic Republic of the Congo"], glow_hi=True),
"P3-10": lambda o, t: globe((12, 22), arcs=[(BUNIA, p, n, i) for i, (p, n) in enumerate([(PARIS, "FRANCE"), (BERLIN, "GERMANY"), (AMS, "NETHERLANDS"), (GENEVA, "SWITZERLAND"), (LONDON, "BRITAIN · NOV")])],
          hi=["Democratic Republic of the Congo"], title="AID WORKERS FLOWN OUT FOR CARE", tag=t, spin=8, R=320),
"P3-10b": lambda o, t: map_pins(EUR, 5, [(*PARIS, "FIRST CASE OUTSIDE AFRICA · 24 JUN", ORANGE)], "FRANCE · A DOCTOR COMES HOME", t, cues=[0]),
"P3-11": lambda o, t: lights_out("The hardest numbers.", at=0.0, until=sn(1)) if _A.T < sn(1) else stats3([("≈ 3,000", "child cases (2,959)", 0), ("1,737", "children have died", 2), ("1 IN 3", "of all deaths is a child", 3)], title="CHILDREN · UNICEF, DATA TO 4 NOV", tag=t),
"P3-12": lambda o, t: number("≈ 72%", "of infected children under five have died · 2,280+ children orphaned or separated", kicker="UNICEF · 13 NOV 2026", tag=t),
"P3-12b": lambda o, t: gauge(80, "of child deaths happened outside a treatment centre", sub="1 in 3 under-5s admitted die within 24 hours", tag=t, valtxt=lambda e: "≈ " + countup("80", e) + "%"),
"P3-13": iceberg,
"P3-14": clock16,
"P4-01": lambda o, t: part(4, "Not under control"),
"P4-02": lambda o, t: quote("Still serious, and still not under control.", "Jean Kaseya, Africa CDC", "15 Nov 2026", tag=t, cue=9),
"P4-03": lambda o, t: quote("The worst Ebola outbreak that the world will have.", "Jean Kaseya, if it isn't stopped now", "15 Nov 2026", tag=t, cue=9),
"P4-04": lambda o, t: split(("AFRICA CDC", "NOT UNDER CONTROL", "Jean Kaseya, 15 Nov"), ("WHO", "SLOWING", "in several early epicentres · Tedros"), tag=t),
"P4-05": lambda o, t: gauge(80, "of new cases come from outside contact lists", sub="Africa CDC figure", tag=t, stamp_txt="CLAIM", valtxt=lambda e: "> " + countup("80", e) + "%"),
"P4-06": net,
"P4-06b": lambda o, t: figures(o, t, 5, 5, "CONTACTS FOUND · JUNE 2026 (IRC)", 0, hit_txt="≈ 1 IN 5 FOUND", found=1),
"P4-07": lambda o, t: gauge(65, "of deaths happen at home, not in a clinic", sub="every one is a funeral", tag=t, stamp_txt="CLAIM", valtxt=lambda e: "> " + countup("65", e) + "%"),
"P4-08": lambda o, t: timeline([("21 MAY", "Rwampara: tents burned"), ("23 MAY", "Mongbwalu: tent burned, 18 fled"), ("1 JUN", "Bunia: burial team hurt"), ("17 JUN", "Mongbwalu: 5 workers held")], [0, 1], title="ATTACKS ON THE RESPONSE", tag=t),
"P4-09": lambda o, t: _stamped(timeline([("21 MAY", "Rwampara: tents burned"), ("23 MAY", "Mongbwalu: tent burned, 18 fled"), ("1 JUN", "Bunia: burial team hurt"), ("17 JUN", "Mongbwalu: 5 workers held")], [2, 3], title="ATTACKS ON THE RESPONSE", tag=t), "5 HEALTH WORKERS HELD", c(1, 3.0) + 0.5),
"P4-10": lambda o, t: number("150+", "patients had left treatment centres by 19 June", kicker="THE GOVERNMENT'S OWN COUNT", tag=t, badge="CLAIM"),
"P4-11": lambda o, t: icongrid(40, [(11, CRIMSON, 0, "43 OF 160 DIED")], title="HEALTH WORKERS INFECTED: 160 (EACH ICON ≈ 4)", tag=t),
"P4-12": payslip,
"P4-13": lambda o, t: map_pins(EAST, 7, [(*BENI, "BENI · 30 MAY", RED), (*BUTEMBO, "BUTEMBO", PAPER_HI)], "20 CIVILIANS KILLED NEARBY · 3 PATIENTS FLED", t, cues=[0, None]),
"P4-14": lambda o, t: run_line(4, t) if False else receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=2, cues_from=[0.6, c(0, 1.5)]),
"P5-01": lambda o, t: part(5, "The war over the ground"),
"P5-02": lambda o, t: tiles([("ADF", "an armed group with links to Islamic State")], title="THREE NAMES · ONE", tag=t, cues=[0]),
"P5-03": lambda o, t: tiles([("ADF", "links to Islamic State"), ("CODECO", "militia in Ituri"), ("M23", "UN experts: Rwanda-backed · Rwanda denies")], title="THREE NAMES", tag=t, cues=[-1, 0, 0]),
"P5-03b": lambda o, t: map_scene(EAST, 7, labels=[(29.6, 0.9, "ADF", 40, RED), (30.3, 2.1, "CODECO", 40, RED), (28.6, -1.2, "M23", 40, RED)], nv=True,
          pins=[(lo, la, "", ORANGE, None) for lo, la in [(30.1, 1.8), (30.3, 1.5), (29.5, 0.5), (29.3, 0.1), (29.2, -1.7), (29.9, 2.0)]], title="THREE ARMED GROUPS · ONE OUTBREAK ZONE", tag=t),
"P5-04": lambda o, t: map_pins(EAST, 7, [(30.05, 1.95, "GOLD", ORANGE), (29.6, 0.2, "TIN", PAPER_HI), (28.7, -0.9, "TUNGSTEN", PAPER_HI), (28.88, -1.55, "TANTALUM", ORANGE)], "WHAT'S UNDER THE GROUND (APPROXIMATE AREAS)", t, cues=[0, 0, 0, 0]),
"P5-05": lambda o, t: flow({"m": (220, 360, "MINER", PAPER), "t": (W/2, 360, "MILITIA TAX", RED), "g": (W - 220, 360, "GUNS", CRIMSON)}, [("m", "t", "every bag", 0), ("t", "g", "", None)], title="WHO TAXES THE GOLD", tag=t),
"P5-06": lambda o, t: map_scene((28.5, -1.0, 33.5, 3.6), 7, hi=["Uganda"], lines=[(MONG, KAMPALA, ORANGE, 5, 0, True)], pins=[(*MONG, "MONGBWALU", PAPER_HI, None), (*KAMPALA, "KAMPALA", ORANGE, 0)], title="SMUGGLED TO UGANDA (UN EXPERTS)", tag=t),
"P5-07": lambda o, t: bars([("ITURI · OFFICIAL EXPORTS", 0.5), ("UGANDA · DECLARED EXPORTS", 62)], title="GOLD EXPORTS IN 2025 (TONNES)", unit=" t", tag=t, fmt="{:,.1f}", cues=[0, 1], hi=1, reveal=(1, "RECORD")),
"P5-07b": lambda o, t: flow({"g": (220, 360, "GOLD", ORANGE), "b": (W/2, 360, "BORDER", PAPER), "u": (W - 220, 360, "UGANDA", PAPER_HI), "c": (W/2, 560, "CONGO TAX: $0", CRIMSON)},
          [("g", "b", "no papers", None), ("b", "u", "", None), ("b", "c", "", 0)], title="NO PAPERWORK · NO TAX", tag=t),
"P5-08": lambda o, t: card(["MUCH OF IT STARTED IN CONGO"], kicker="UN EXPERTS ON UGANDA'S GOLD", tag=t, cues=[0], style="serif"),
"P5-09": lambda o, t: map_scene((28.0, -2.6, 30.0, -0.6), 9, pins=[(*RUBAYA, "RUBAYA", ORANGE, None), (*GOMA, "GOMA", PAPER_HI, None)], rings=[(*RUBAYA, 15, 0, "> 15% OF WORLD TANTALUM")],
          reticle=(*RUBAYA, 0, "COLTAN MINE"), title="RUBAYA · TAKEN BY M23, APR 2024", tag=t),
"P5-10": lambda o, t: number("$300,000", "a month from a tax on what came out of the ground", kicker="M23 AT RUBAYA · UN, 2024", tag=t),
"P5-11": overlap,
"P5-11b": lambda o, t: tiles([("LATE", "delayed detection"), ("WAR", "conflict, no access"), ("STRETCHED", "health services thin")], title="WHY IT SPREAD FASTER", tag=t, cues=[0, 0, 0]),
"P5-12": lambda o, t: map_pins(EAST, 7, [(*KATANA, "KATANA · REBEL-HELD", RED), (*BUKAVU, "BUKAVU", PAPER_HI)], "THE VIRUS IN REBEL TERRITORY", t, cues=[0, None]),
"P5-13": lambda o, t: quote("If I stay at home, what are my children going to eat?", "Justin Okaume, gold digger, Mongbwalu", "AFP, 2026", tag=t, cue=9),
"P5-14": lambda o, t: receipt(RUN[:5], title="RUNNING TOTAL", tag=t, show=4, cues_from=[c(0, 1.5)]),
"P6-01": lambda o, t: part(6, "Your phone"),
"P6-03": lambda o, t: map_scene(AFRICA, 4, hi2=["Democratic Republic of the Congo"], glow_hi=True, strips=("DR CONGO · ≈ 1,300 T OF TANTALUM", "WORLD TOTAL · ≈ 2,500 T", 0),
          title="TANTALUM MINED IN 2025 (USGS ESTIMATE)", tag=t),
"P6-03b": lambda o, t: bars([("DR CONGO", 1300), ("RWANDA", 400), ("NIGERIA", 390), ("BRAZIL", 190), ("USA", 0)], title="TANTALUM MINED IN 2025 (TONNES, EST.)", unit=" t", tag=t, hi=1, cues=[-5, -5, 0, 0, 0]),
"P6-04": lambda o, t: gauge(68, "of the world's tantalum: DR Congo + Rwanda", sub="1,700 of 2,500 tonnes", tag=t, valtxt=lambda e: "≈ " + countup("68", e) + "%"),
"P6-05": lambda o, t: number("100%", "Every gram of tantalum the US uses is imported", kicker="NO US TANTALUM MINE SINCE 1959", tag=t),
"P6-05b": lambda o, t: map_scene((-122, -46, 192, 62), 2, hi=["United States of America"], arcs=[(p, (-77.0, 38.9), ORANGE, 4, i, False) for i, p in enumerate([(116.4, 39.9), (122.0, -26.0), (10.0, 51.0)])],
          pins=[(116.4, 39.9, "CHINA 22%", ORANGE, 0), (122.0, -26.0, "AUSTRALIA 14%", ORANGE, 1), (10.0, 51.0, "GERMANY 11%", ORANGE, 2), (-77.0, 38.9, "USA", PAPER_HI, None)],
          title="WHERE US TANTALUM IMPORTS COME FROM", tag=t, terrain=False),
"P6-06": lambda o, t: _tags(o, t),
"P6-07": lambda o, t: map_scene(DRC, 5, hi=["Democratic Republic of the Congo"], pins=[(*KOLWEZI, "KATANGA · COBALT", CYAN, 1), (*BUNIA, "ITURI · EBOLA", RED, None)], measure=(KOLWEZI, BUNIA, "≈ 1,500 KM", 1), strips=("CONGO · ≈ 73% OF WORLD COBALT", "MOSTLY FROM THE FAR SOUTH-EAST", 0, 120), title="COBALT: SOUTH · EBOLA: NORTH-EAST", tag=t),
"P6-07b": lambda o, t: number("96,600 t", "a year, 2026-27 · a price policy, not Ebola", kicker="CONGO'S COBALT EXPORT QUOTA", tag=t),
"P6-08": lambda o, t: flow({"p": (180, 360, "YOUR PHONE", PAPER_HI), "c": (460, 360, "CAPACITOR", PAPER), "t": (730, 360, "TANTALUM", ORANGE), "m": (1000, 250, "MINE", ORANGE), "g": (1000, 480, "ARMED GROUP TAX", RED)},
          [("p", "c", "", 0), ("c", "t", "", None), ("t", "m", "", None), ("m", "g", "", None)], title="FOLLOW THE MONEY BACKWARDS", tag=t),
"P6-09": lambda o, t: chain(["Mine", "Trader", "Border", "Smelter", "Factory"], title="WHERE THE ORIGIN GETS LOST", tag=t, times=[0.5 + i*0.9 for i in range(5)]),
"P6-10": lambda o, t: headline("Bloomberg (reported)", "Investors skip Congo's mining conference as Ebola curbs travel", "Jun 2026", tag=t),
"P6-11": lambda o, t: map_pins(EUR, 5, [(*PARIS, "PARIS", ORANGE), (*BRUSSELS, "BRUSSELS", ORANGE), (*LONDON, "LONDON", ORANGE)], "THE MEETINGS MOVED", t, cues=[0, 0, 0]),
"P6-11b": calendar21,
"P6-12": lambda o, t: receipt(RUN[:6], title="RUNNING TOTAL", tag=t, show=5, cues_from=[c(0, 1.5)]),
"P7-01": lambda o, t: part(7, "The hunger line"),
"P7-02": lambda o, t: chain(["Quarantine", "No fields", "No market", "No food"], title="HOW EBOLA MAKES PEOPLE HUNGRY", tag=t),
"P7-03b": lambda o, t: map_scene(ITURI, 8, pins=[(*BUNIA, "BUNIA", ORANGE, None)], streams=(BUNIA, [MONG, (30.6, 1.9), (29.9, 1.3), (30.5, 1.2), (30.0, 2.3)], 90, 0), title="16,000+ CROSSINGS A DAY · BUNIA CORRIDOR", tag=t),
"P7-04": lambda o, t: quote("Food assistance is a public health tool.", "World Food Programme", "Aug 2026", tag=t, cue=9),
"P7-05": lambda o, t: number("≈ 29M", "people in crisis-level hunger or worse · Sep-Dec 2026", kicker="DR CONGO · IPC", tag=t),
"P7-06": lambda o, t: flap([("SEP-DEC 2026", "--.-M", "≈29M"), ("JAN-JUN 2027", "--.-M", "30.3M")], header="CONGO · PEOPLE IN CRISIS HUNGER OR WORSE (IPC 3+)", tag=t, hit_i=-1, record=[1]),
"P7-06b": lambda o, t: diverging([("BIRTHS IN CLINICS · N KIVU EBOLA ZONES", -18, 0, "≈ -18%"), ("MEASLES FIRST DOSE · 3 PROVINCES", 0, 0, "DOWN · SIZE NOT GIVEN")], title="CARE PUSHED ASIDE · JAN-SEP 2026", tag=t),
"P7-07": lambda o, t: map_pins(EAST, 7, [(*DJUGU, "DJUGU", RED), (*LUBERO, "LUBERO", RED), (*MASISI, "MASISI", RED), (*OICHA, "OICHA", RED)], "EMERGENCY LEVEL (IPC 4) · ONE STEP BELOW FAMINE", t, cues=[0, 0, 0, 0]),
"P7-08": lambda o, t: quote("Putting food beyond their reach.", "Ross Smith, World Food Programme", "Nov 2026", tag=t, cue=9),
"P7-09": loop,
"P7-10": lambda o, t: number("7,500", "schools, nearly 2.5 million children, not yet reached with infection protection", kicker="UNICEF · 13 NOV 2026", tag=t),
"P7-10b": lambda o, t: split(("CHILDREN, ITURI", "81%", "said Ebola made them afraid or stressed"), ("PARENTS", "89%", "said their stress had gone up"), tag=t),
"P7-11": lambda o, t: receipt(RUN[:7], title="RUNNING TOTAL", tag=t, show=6, cues_from=[c(0, 1.5)]),
"P8-01": lambda o, t: part(8, "Who pays"),
"P8-02": lambda o, t: _pledge(o, t, 0),
"P8-02b": lambda o, t: _maths(o, t, ["$1.3 billion released", "÷ 11,376 confirmed cases"], "≈ $114,000 A CASE"),
"P8-03": lambda o, t: _pledge(o, t, 1),
"P8-04": lambda o, t: tiles([("UK £20M", "up to, 21 May"), ("US $112M", "State Department"), ("EU €15M", "DRC + Uganda")], title="SOME OF IT IS YOUR TAX", tag=t, cues=None),
"P8-05": lambda o, t: _maths(o, t, ["£20M ÷ 69.3M people in Britain", "$112M ÷ 340M people in America"], "≈ 29p · ≈ 33¢ EACH"),
"P8-06": lambda o, t: headline("The Guardian", "US 'notably absent' from Congo's Ebola response", "21 May 2026", tag=t),
"P8-07": lambda o, t: stacked([("DR CONGO · JUST OVER $1BN", 1.05, RED, 1), ("REST OF AFRICA", 2.55, (96, 88, 80), 0)], title="POSSIBLE LOSS TO AFRICAN ECONOMIES · UNDP, JUN 2026", total="UP TO $3.6BN", tag=t),
"P8-08": lambda o, t: split(("EXTREME POVERTY", "985,000", "people pushed in"), ("JOBS AT RISK", "300,000", "if it spreads beyond Ituri"), tag=t),
"P8-09": lambda o, t: gauge(85, "of the economic damage comes from fear", sub="World Bank, past outbreaks (80-90%)", tag=t, valtxt=lambda e: countup("80", e) + "-" + countup("90", e) + "%"),
"P8-09b": lambda o, t: tiles([("11.3% → -2.0%", "Sierra Leone"), ("4.3% → -0.2%", "Guinea"), ("6.8% → 3.0%", "Liberia")], title="2015 GROWTH FORECASTS CUT · WORLD BANK, DEC 2014", tag=t, cues=[0, 0, 0]),
"P8-10": lambda o, t: map_scene((-100, 18, -20, 56), 4, arcs=[(p, IAD, PAPER_HI, 3, None, True) for p in [(-25, 50), (-22, 40), (-24, 30), (-30, 22), (-26, 55)]],
          pins=[(*IAD, "DULLES (IAD)", ORANGE, 0)], title="RETURNING FROM CONGO? ONE AIRPORT", tag=t),
"P8-11": form21,
"P8-12": lambda o, t: gauge(8, "risk to people living in Europe", sub="ECDC, 16 Nov 2026", tag=t, valtxt=lambda e: "VERY LOW"),
"P8-12b": lambda o, t: split(("AIRPORT SCREENING", "WEAK", "judged ineffective by ECDC"), ("TELLING TRAVELLERS", "BETTER", "symptoms + what to do"), tag=t),
"P8-13": lambda o, t: number("$53BN", "economic and social cost, Huber et al., 2018", kicker="WEST AFRICA'S EBOLA BILL · 2014-16", tag=t, badge="ESTIMATE"),
"P8-14": scale,
"P8-15": lambda o, t: receipt(RUN[:8], title="RUNNING TOTAL", tag=t, show=7, cues_from=[c(0, 1.5)]),
"P9-01": lambda o, t: part(9, "What happens next"),
"P9-02": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR"], circles=[(2, "VACCINE RESULTS", 0)], title="THREE THINGS TO WATCH", tag=t),
"P9-03": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR"], circles=[(2, "VACCINE RESULTS", -9), (0, "THE MONEY", 0)], title="THREE THINGS TO WATCH", tag=t),
"P9-04": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR"], circles=[(2, "VACCINE RESULTS", -9), (0, "THE MONEY", -9), (4, "ACCESS", 0)], title="THREE THINGS TO WATCH", tag=t),
"P9-04b": lambda o, t: map_scene(AFRICA, 4, hi=["Angola", "United Republic of Tanzania", "Ethiopia", "Zambia"], hi2=["Democratic Republic of the Congo"], title="AFRICA CDC: 10 COUNTRIES AT ELEVATED RISK (4 NAMED)", tag=t),
"P9-05": lambda o, t: scenario(1, "It winds down", -1, ylab="NEW CASES (SHAPE ILLUSTRATIVE)"),
"P9-06": lambda o, t: scenario(2, "It keeps burning", 0, ylab="NEW CASES (SHAPE ILLUSTRATIVE)"),
"P9-07": lambda o, t: scenario(3, "It spreads", 1, ylab="NEW CASES (SHAPE ILLUSTRATIVE)"),
"P9-08": lambda o, t: tiles([("1", "winds down"), ("2", "keeps burning"), ("3", "spreads")], title="SCENARIOS, NOT FORECASTS", tag="SCENARIO", cues=None),
"P9-08b": lambda o, t: map_scene(ITURI, 8, pins=[(*MONG, "MONGBWALU", RED, None)], title="THE CHEAPEST LINE: TELL PEOPLE IN TIME", tag=""),
"RC-01": lambda o, t: receipt(FULL, show=0, cues_from=[99]*6),
"RC-02": lambda o, t: receipt(FULL[:1], show=0, cues_from=[0.3]),
"RC-03": lambda o, t: receipt(FULL[:2], show=1, cues_from=[0.3]),
"RC-04": lambda o, t: receipt(FULL[:3], show=2, cues_from=[0.3]),
"RC-05": lambda o, t: receipt(FULL[:4], show=3, cues_from=[0.3]),
"RC-06": lambda o, t: receipt(FULL[:5], show=4, cues_from=[0.3]),
"RC-07": lambda o, t: receipt(FULL, show=5, cues_from=[0.4], final_stamp="PAID BY THEM, FIRST"),
"RC-08": lambda o, t: endcard(next_title="RUSSIA'S FUEL CRISIS"),
}

def _sub(o, t):
    im = base(); d = D(im)
    center(d, 120, "EVERY CRISIS SENDS A BILL", f(56, "inter"), alpha(PAPER_HI, seg(0.1, 0.6)))
    center(d, 196, "History keeps the receipts.", f(36, "serif"), alpha(ORANGE, seg(0.6, 0.6)))
    a = seg(0.8, 0.4); d.rrect((W/2 - 190, 300, W/2 + 190, 390), 14, fill=alpha(CRIMSON, a)); center(d, 320, "SUBSCRIBE", f(44, "inter"), alpha(PAPER_HI, a))
    b = seg(lead(c(0, 3.0), 0.4), 0.5)
    d.rect((W/2 - 260, 440, W/2 + 260, 600), fill=alpha((40, 37, 34), b), outline=alpha(ORANGE, b), width=3)
    center(d, 462, "THIS TIME", f(22, "inter"), alpha(ORANGE, b)); center(d, 500, "A FUNERAL → YOUR PHONE", f(40, "inter"), alpha(PAPER_HI, b))
    return im

def _maths(o, t, lines, result):
    im = base(); d = paper(im, (280, 120, W - 280, H - 140), seed=9)
    for i, l in enumerate(lines): typewriter(d, (330, 160 + i*70), l, fit(d, l, 40, W - 660), (30, 26, 22), sn(i) + 0.1 if i < len(_A.SENTS) else 0.4 + i, 30)
    hit = c(0, _A.DUR*0.6); e = ease_io((_A.T - lead(hit, 1.0))/1.0)
    d.line([(330, 160 + len(lines)*70), (W - 330, 160 + len(lines)*70)], (60, 50, 40), 3)
    d.text((330, 180 + len(lines)*70), countup(result, e), fit(d, result, 60, W - 680), alpha(CRIMSON, min(1, e*4)))
    tagline(im, t or "ILLUSTRATION · our maths"); return im

def _tags(o, t):
    im = pricetags([("2024 · PER KG", "$167", INK, None), ("2025 · PER KG", "$180", INK, 0)], title="TANTALUM ORE PRICE (USGS)", tag=t)
    stamp(im, "NO EBOLA SPIKE FOUND", W/2, 610, sn(2) if len(_A.SENTS) > 2 else _A.DUR - 2, col=ORANGE, size=54, angle=-3)
    return im

def _pledge(o, t, gap_mode):
    im = base(); d = D(im); hit = c(0, 2.0)
    d.text((180, 80), "EBOLA RESPONSE MONEY · MID-NOV 2026", f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    x0, x1, y = 200, W - 140, 260
    d.rect((x0, y, x1, y + 130), outline=alpha(PAPER, seg(0.2, 0.4)), width=3); d.text((x0, y - 46), "PLEDGED: $2.9BN", f(32, "inter"), alpha(PAPER, seg(0.2, 0.4)))
    e = 1.0 if gap_mode else ease_io((_A.T - lead(hit, 0.9))/0.9)
    xm = x0 + (x1 - x0)*0.45*e; d.rect((x0, y, xm, y + 130), fill=ORANGE)
    if e > 0.3: d.text((x0 + 20, y + 40), "RELEASED $1.3BN", f(40, "inter"), alpha(INK, min(1, e*2)))
    if gap_mode:
        k = seg(lead(hit, 0.3), 0.4); fl = 0.5 + 0.5*math.sin(_A.T*6)
        d.rect((xm + 4, y + 4, x1 - 4, y + 126), fill=alpha(CRIMSON, 0.35*k*fl + 0.2*k)); d.text((xm + 30, y + 40), "$1.6BN NOT THERE", f(40, "inter"), alpha(PAPER_HI, k))
        center(d, 480, "“A COLLECTIVE FAILURE” · JEAN KASEYA", f(34, "serif"), alpha(ORANGE, seg(sn(1), 0.5) if len(_A.SENTS) > 1 else k))
    tagline(im, t); return im

def _stamped(im, txt, at):
    stamp(im, txt, W/2, 590, at, size=64, angle=-5); return im
