# INV-011 graphics spec: script code -> lambda(on_screen, tag) -> PIL frame (uses anim11 globals T, CUES, SENTS).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from anim11 import *
import anim11 as _A

KERCH = (35.75, 44.95, 37.35, 45.62); CRIMEA = (31.8, 43.6, 39.6, 47.4); WRUS = (21, 42, 66, 63); RUSSIA = (20, 38, 112, 69)
WORLD = (-85, -42, 150, 72); BELARUS = (22.5, 50.6, 41.5, 57.5); CASIA = (44, 34, 92, 56); GER = (4, 46.5, 20.5, 55.5)
BR = ((36.505, 45.305), (36.665, 45.245))  # Kerch bridge, Taman side -> Kerch side (approx)
KER = (36.30, 45.36); TAMAN = (36.85, 45.18); MOSCOW = (37.62, 55.75); UA = (32.0, 49.0); SEV = (33.52, 44.6)
REG = [(50.1, 53.2), (44.5, 48.7), (39.7, 54.6), (32.0, 59.45), (39.9, 57.6), (44.2, 56.15), (46.0, 51.5), (39.7, 47.2), (34.4, 53.25), (39.1, 44.1),
       (37.8, 44.7), (28.6, 60.35), (36.6, 50.6), (41.9, 45.0), (38.1, 46.9)]
REFS = [(32.0,59.45),(37.75,55.65),(39.7,54.6),(39.9,57.6),(44.2,56.15),(44.5,48.7),(46.0,51.5),(49.9,53.1),(50.3,53.2),(48.5,53.15),(55.97,54.7),(56.0,54.8),
        (56.1,54.75),(55.9,53.4),(56.2,58.0),(51.8,55.6),(52.0,55.55),(58.6,51.2),(73.4,55.0),(104.1,52.5),(90.5,56.3),(39.1,44.1),(38.4,44.85),(38.4,44.8),
        (39.9,47.8),(53.7,63.55),(65.6,57.15),(48.0,46.35),(28.4,59.7),(42.1,45.0),(50.8,53.4),(49.5,56.1),(53.4,54.7),(47.2,56.1),(61.4,55.2),(60.6,56.85),(84.9,56.5),(86.1,55.35)]
PLANTS = [(12.02,51.32),(14.58,53.53),(13.64,50.5),(12.38,51.2),(11.6,52.1),(12.13,51.05),(18.2,50.35),(7.1,51.5),(7.03,51.6),(6.98,50.82),(6.93,51.52),
          (7.3,51.55),(8.43,49.48),(11.78,51.3),(18.3,50.4),(15.98,48.3)]
PRIM = (28.6, 60.35); NOVO = (37.8, 44.7)

def roadmap(o, t, items, cue_offset=0):
    im = base(); d = D(im); n = len(items); gap = (W - 240) / (n - 1)
    d.line([(120, 360), (W - 120, 360)], DIM, 4)
    for i, lab in enumerate(items):
        t0 = lead(c(i + cue_offset, 0.6 + i*1.2), 0.3) if _A.CUES else 0.5 + i*(_A.DUR - 1.5)/n
        a = seg(t0, 0.4); x = 120 + i*gap
        d.ell((x - 22, 338, x + 22, 382), fill=alpha(ORANGE if a > 0.5 else DIM, max(0.3, a)))
        center(d, 410, lab, f(30, "inter"), alpha(PAPER_HI, max(0.25, a)), cx=x)
        pulse_rings(d, x, 360, ORANGE, t0, 1, 50, 0.5)
    tagline(im, t); return im

def ration(o, t):
    im = base(); d = paper(im, (330, 140, W - 330, H - 160), seed=21); hit = c(0, 1.0)
    center(d, 170, "FUEL SALES LIMIT", f(30, "inter"), (120, 40, 20))
    d.line([(370, 220), (W - 370, 220)], (60, 50, 40), 2)
    for i, (l, at) in enumerate([("PETROL ......... 30 L", hit), ("DIESEL ......... 60 L", hit + 1.0), ("CANISTERS ....... NO", hit + 1.8)]):
        typewriter(d, (400, 250 + i*70), l, f(40, "inter"), (30, 26, 22), lead(at, 0.6), 34)
    stamp(im, "PER VISIT", W/2 + 140, H - 210, hit + 2.6, size=70)
    tagline(im, t); return im

def subscribe_card(o, t):
    im = base(); d = D(im)
    center(d, 120, "EVERY CRISIS SENDS A BILL", f(56, "inter"), alpha(PAPER_HI, seg(0.1, 0.6)))
    center(d, 196, "History keeps the receipts.", f(36, "serif"), alpha(ORANGE, seg(0.6, 0.6)))
    a = seg(lead(c(0, 1.5), 0.3), 0.4)
    d.rrect((W/2 - 190, 300, W/2 + 190, 390), 14, fill=alpha(CRIMSON, a)); center(d, 320, "SUBSCRIBE", f(44, "inter"), alpha(PAPER_HI, a))
    b = seg(sn(1), 0.5)
    d.rect((W/2 - 260, 440, W/2 + 260, 600), fill=alpha((40, 37, 34), b), outline=alpha(ORANGE, b), width=3)
    center(d, 462, "LAST TIME ON THE INVOICE", f(22, "inter"), alpha(ORANGE, b)); center(d, 500, "TAIWAN 2027: YOUR BILL", f(40, "inter"), alpha(PAPER_HI, b))
    return im

def refinery_cut(o, t):
    """crude barrel -> column -> petrol / diesel / jet, each on its word"""
    im = base(); d = D(im); a = seg(0.1, 0.4)
    d.rect((140, 380, 260, 560), fill=alpha((60, 50, 40), a), outline=alpha(PAPER, a), width=3); center(d, 580, "CRUDE", f(28, "inter"), alpha(PAPER, a), cx=200)
    k = seg(0.6, 0.6); d.line([(260, 470), (260 + 190*k, 470)], ORANGE, 6)
    b = seg(1.0, 0.5)
    d.rect((480, 140, 620, 600), fill=alpha((50, 47, 44), b), outline=alpha(PAPER, b), width=3)
    for i in range(6): d.line([(480, 200 + i*70), (620, 200 + i*70)], alpha(GREY, b), 2)
    center(d, 620, "REFINERY", f(28, "inter"), alpha(PAPER, b), cx=550)
    outs = [("PETROL", 220, ORANGE), ("DIESEL", 360, WARN), ("JET FUEL", 500, CYAN)]
    t_out = [c(0, 2.0) + 0.6 + 0.8*i for i in range(3)] if len(_A.CUES) < 2 else [_A.CUES[1] + 0.2*i for i in range(3)]
    t_out = [sn(2) + 0.4*i for i in range(3)] if len(_A.SENTS) > 2 else t_out
    for i, (lab, y, col) in enumerate(outs):
        e = seg(t_out[i] - 0.3, 0.5)
        if e <= 0: continue
        d.line([(620, y), (620 + 260*e, y)], col, 6)
        d.text((900, y - 22), lab, f(44, "inter"), alpha(col, e))
    tagline(im, t); return im

def column_target(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    for i, (x, h) in enumerate([(380, 360), (520, 460), (660, 300), (820, 400)]):
        d.rect((x, 600 - h, x + 80, 600), fill=(52, 48, 44), outline=(90, 84, 76), width=2)
    x, y = 560, 270; k = seg(lead(hit, 0.6), 0.6)
    if k > 0:
        r = 140 - 80*k
        d.ell((x - r, y - r, x + r, y + r), outline=alpha(RED, k), width=4); d.line([(x - r - 30, y), (x + r + 30, y)], alpha(RED, k), 2); d.line([(x, y - r - 30), (x, y + r + 30)], alpha(RED, k), 2)
        d.text((x + 100, y - 40), "DISTILLATION COLUMN", f(30, "inter"), alpha(PAPER_HI, k))
    b = seg(sn(2) - 0.2, 0.5)
    if b > 0: d = paper(im, (700, 440, 1200, 560), seed=4); d.text((730, 474), "WEEKS TO MONTHS TO FIX", f(30, "inter"), alpha(INK, b))
    tagline(im, t); return im

def two_big(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    center(d, 200, "OIL", f(130, "inter"), alpha(PAPER_HI, seg(0.2, 0.5)), cx=W*0.3); center(d, 360, "PLENTY", f(40, "serif"), alpha(GREEN, seg(0.6, 0.4)), cx=W*0.3)
    center(d, 200, "PETROL", f(130, "inter"), alpha(PAPER_HI, seg(lead(hit, 0.4), 0.5)), cx=W*0.7)
    stamp(im, "SHORT", W*0.7, 400, hit + 0.1, size=90)
    tagline(im, t); return im

def scale_card(o, t):
    im = base(); d = D(im); hit = c(0, 1.5); k = seg(lead(hit, 0.4), 0.8); tilt = 26*k
    cx, cy = W/2, 300
    d.line([(cx, cy), (cx, 560)], PAPER, 6); d.poly([(cx - 70, 580), (cx + 70, 580), (cx, 540)], fill=PAPER)
    xl, yl = cx - 300, cy - tilt; xr, yr = cx + 300, cy + tilt
    d.line([(xl, yl), (xr, yr)], PAPER, 6)
    d.rect((xl - 60, yl + 20, xl + 60, yl + 140), fill=(70, 60, 50)); center(d, yl + 150, "CRUDE", f(28, "inter"), PAPER, cx=xl)
    d.rect((xr - 50, yr + 20, xr + 50, yr + 150), fill=ORANGE); center(d, yr + 160, "FUEL", f(28, "inter"), PAPER_HI, cx=xr)
    center(d, 110, "REFINED FUEL IS WORTH MORE", f(40, "inter"), alpha(PAPER_HI, seg(0.3, 0.5)))
    if k > 0.9: stamp(im, "A WAR ON THE WALLET", W/2, 640, hit + 0.9, col=ORANGE, size=56, angle=-4, box=False)
    tagline(im, t); return im

def maths(o, t, lines, result, hit_i=0):
    im = base(); d = paper(im, (300, 120, W - 300, H - 140), seed=9)
    for i, l in enumerate(lines): typewriter(d, (350, 160 + i*70), l, f(42, "inter"), (30, 26, 22), sn(i) + 0.1 if i < len(_A.SENTS) else 0.4 + i, 30)
    hit = c(hit_i, _A.DUR*0.6); e = ease_io((_A.T - lead(hit, 1.0))/1.0)
    d.line([(350, 160 + len(lines)*70), (W - 350, 160 + len(lines)*70)], (60, 50, 40), 3)
    d.text((350, 180 + len(lines)*70), countup(result, e), fit(d, result, 64, W - 720), alpha(CRIMSON, min(1, e*4)))
    tagline(im, t); return im

def stacked(o, t):
    im = base(); d = D(im); hit = c(0, 1.5)
    d.text((180, 80), "RUSSIA'S OIL EXPORT MONEY, OCT 2026", f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    x0, x1, y = 200, W - 140, 260; e = ease_io((_A.T - lead(hit, 0.8))/0.8)
    xm = x0 + (x1 - x0)*0.82*e
    d.rect((x0, y, xm, y + 120), fill=ORANGE); d.text((x0 + 20, y + 36), "CRUDE > 80%", f(40, "inter"), alpha(INK, min(1, e*3)))
    e2 = seg(lead(c(1, hit + 2), 0.4), 0.5)
    d.rect((xm, y, xm + (x1 - xm)*e2, y + 120), fill=(110, 100, 90)); d.text((xm + 14, y + 40), "FUEL", f(30, "inter"), alpha(INK, e2))
    a = seg(lead(c(2, hit + 4), 0.4), 0.5)
    center(d, 460, "FUEL EXPORTS: ABOUT A THIRD DOWN ON A YEAR", f(38, "inter"), alpha(CRIMSON, a))
    tagline(im, t); return im

def then_now(o, t):
    im = base(); d = D(im); hit = c(0, 3.0)
    a = seg(0.2, 0.5); center(d, 120, "1944", f(80, "bebas"), alpha(PAPER, a), cx=W*0.27)
    for i in range(18):
        x = 120 + (i % 6)*62; y = 240 + (i // 6)*80; k = seg(0.3 + i*0.05, 0.3)
        d.poly([(x, y + 20), (x + 50, y + 14), (x + 50, y + 26)], fill=alpha(GREY, k)); d.line([(x + 18, y + 4), (x + 30, y + 36)], alpha(GREY, k), 5)
    center(d, 520, "THOUSANDS OF HEAVY BOMBERS", f(28, "inter"), alpha(PAPER, a), cx=W*0.27)
    b = seg(lead(hit, 0.4), 0.5); center(d, 120, "2026", f(80, "bebas"), alpha(ORANGE, b), cx=W*0.73)
    x, y = W*0.73, 330
    d.poly([(x - 90, y), (x + 90, y - 6), (x + 90, y + 6)], fill=alpha(ORANGE, b)); d.line([(x - 10, y - 60), (x + 20, y + 60)], alpha(ORANGE, b), 8)
    center(d, 520, "A DRONE: LESS THAN A FAMILY CAR", f(28, "inter"), alpha(PAPER_HI, b), cx=W*0.73)
    d.line([(W/2, 120), (W/2, 580)], DIM, 3)
    tagline(im, t); return im

def big_word(o, t):
    im = base(); d = D(im); hit = c(0, 1.0); a = seg(lead(hit, 0.3), 0.4)
    center(d, 200 + (1 - a)*30, "DIESEL", f(240, "inter"), alpha(PAPER_HI, a))
    im = sweep(im, (0, 200, W, 460), hit + 0.4, 1.3); d = D(im)
    x = -260 + (W + 520) * ((_A.T - hit) / max(1.0, _A.DUR - hit)) if _A.T > hit else -400
    d.rect((x, 560, x + 170, 640), fill=ORANGE); d.rect((x + 170, 584, x + 240, 640), fill=WARN)
    for wx in (x + 30, x + 140, x + 210): d.ell((wx - 18, 630, wx + 18, 666), fill=INK, outline=PAPER, width=3)
    tagline(im, t); return im

def pool(o, t):
    im = base(); d = D(im); a = seg(0.2, 0.5)
    d.ell((W/2 - 150, 260, W/2 + 150, 460), fill=alpha((50, 45, 38), a), outline=alpha(WARN, a), width=4)
    center(d, 340, "WORLD DIESEL", f(36, "inter"), alpha(PAPER_HI, a))
    names = [("EUROPE", 220, 160), ("TURKEY", W - 220, 160), ("BRAZIL", 220, 560), ("AFRICA", W - 220, 560)]
    hit = c(0, _A.DUR*0.7)
    for i, (n_, x, y) in enumerate(names):
        t0 = sn(min(i + 1, max(0, len(_A.SENTS) - 1))) if i < 2 else sn(2) + 0.4*(i - 2)
        k = seg(t0, 0.6)
        if k <= 0: continue
        d.text((x - d.tl(n_, f(34, "inter"))/2, y - 20), n_, f(34, "inter"), alpha(PAPER_HI, k))
        sx, sy = W/2 + (x - W/2)*0.2, 360 + (y - 360)*0.3
        d.line([(sx, sy), (sx + (x - sx)*0.8*k, sy + (y - sy)*0.8*k)], WARN, 5)
        if _A.T > hit: pulse_rings(d, x, y, ORANGE, hit, 1, 50)
    tagline(im, t); return im

def staircase(o, t):
    im = base(); d = D(im); vals = [("300k t", 0.3), ("500k t", 0.5), ("1M t", 1.0), ("3M t", 3.0)]
    for i, (lab, v) in enumerate(vals):
        t0 = sn(min(i, len(_A.SENTS) - 1)) + (0.3*i if i >= len(_A.SENTS) - 1 else 0) if len(_A.SENTS) > 1 else 0.3 + i*1.0
        t0 = 0.3 + i*1.1 if len(_A.SENTS) < 3 else [sn(0) + 0.2, sn(1), sn(2) - 0.2, sn(2) + 0.6][i]
        k = seg(t0, 0.4); h = 60 + 120*math.sqrt(v); x = 220 + i*230
        d.rect((x, 560 - h*k, x + 180, 560), fill=alpha(ORANGE if i < 3 else WARN, k))
        center(d, 560 - h*k - 50, lab, f(38, "inter"), alpha(PAPER_HI, k), cx=x + 90)
    a = seg(lead(c(0, _A.DUR*0.7), 0.3), 0.4)
    stamp(im, "SANCTIONS OFF TO APR 2027", W/2, 140, lead(c(0, _A.DUR*0.7), 0.1), col=ORANGE, size=54, angle=-3)
    tagline(im, t); return im

def two_quotes(o, t):
    im = base(); d = D(im)
    for i, (q, who) in enumerate([("“A weak decision by strong partners.”", "Volodymyr Zelensky"), ("“Shuffling deck chairs on the Titanic.”", "Michael Lynch, energy analyst")]):
        t0 = sn(i) - 0.2; k = seg(t0, 0.5); y = 150 + i*190; dx = (1 - k)*(-W if i == 0 else W)
        dd = paper(im, (160 + dx, y, W - 160 + dx, y + 150), seed=30 + i)
        dd.text((200 + dx, y + 26), q, f(44, "serif"), (30, 26, 22)); dd.text((200 + dx, y + 96), who.upper(), f(22, "inter"), (120, 40, 20))
    stamp(im, "BAN LIFTED · 10 OCT", W/2 + 180, 600, sn(2) + 0.6 if len(_A.SENTS) > 2 else _A.DUR - 1.5, col=ORANGE, size=60)
    tagline(im, t); return im

def us_tiles(o, t):
    """US tile map: ~half of the states light, one by one"""
    grid = ["AK,,,,,,,,,,ME", ",,,,,,,,,VT,NH", "WA,ID,MT,ND,MN,IL,WI,MI,NY,RI,MA", "OR,NV,WY,SD,IA,IN,OH,PA,NJ,CT,", "CA,UT,CO,NE,MO,KY,WV,VA,MD,DE,",
            ",AZ,NM,KS,AR,TN,NC,SC,DC,,", ",,,OK,LA,MS,AL,GA,,,", "HI,,,TX,,,,,FL,,"]
    im = base(); d = D(im); cells = []
    for r, row in enumerate(grid):
        for q, s in enumerate(row.split(",")):
            if s: cells.append((r, q, s))
    import random; rnd = random.Random(4); lit = set(rnd.sample(range(len(cells)), len(cells)//2))
    hit = c(0, 1.0); order = sorted(lit)
    for i, (r, q, s) in enumerate(cells):
        x = 300 + q*64; y = 120 + r*64; col = (52, 48, 44)
        if i in lit:
            t0 = lead(hit, 0.5) + 0.06*order.index(i)
            col = mix(col, ORANGE, seg(t0, 0.25))
        d.rect((x, y, x + 58, y + 58), fill=col); center(d, y + 18, s, f(18, "inter"), PAPER_HI, cx=x + 29)
    d.text((300, 660), "STATES WAIVING DYED-DIESEL RULES (ILLUSTRATIVE LAYOUT, ≈ HALF)", f(18, "reg"), GREY)
    tagline(im, t); return im

def race(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    for i, (lab, col, sp) in enumerate([("REPAIR", CYAN, 0.9), ("STRIKE", RED, 1.0)]):
        y = 260 + i*180; k = ease_io((_A.T - 0.4)/max(1, _A.DUR - 1.0)) * sp
        d.text((160, y - 70), lab, f(40, "inter"), alpha(col, seg(0.2 + i*0.6, 0.4)))
        d.line([(160, y), (160 + 900*k, y)], col, 14); d.poly([(160 + 900*k, y - 22), (200 + 900*k, y), (160 + 900*k, y + 22)], fill=col)
    center(d, 600, "RUSSIA: 'QUICKLY'  ·  KYIV: 'AGAIN'", f(30, "inter"), alpha(PAPER, seg(lead(hit, 0.3), 0.4)))
    tagline(im, t); return im

def comment_q(o, t):
    return tiles([("THE CAR", "drive less"), ("THE HEATING", "turn it down"), ("THE SHOPPING", "buy less")], title="WHAT WOULD YOU CUT FIRST?  ·  TELL US BELOW", tag=t, cues=None)

FULL_RECEIPT = [("BRIDGE: $3.7BN, HIT AGAIN", "LINE 1"), ("REFINING OUT: 45-55%", "LINE 2"), ("MOSCOW: 30 L A VISIT", "LINE 3"),
                ("DIESEL: RECORDS · +$35K/TRUCK", "LINE 4"), ("YOUR TABLE: + CENTS ON ALL", "LINE 5"), ("PAID BY: YOU", "TOTAL")]

SPEC = {
"CO-02": lambda o, t: map_scene(WRUS, 5, hi=["Ukraine"], streams=(UA, REG, 520, 0), pins=[(*MOSCOW, "MOSCOW", PAPER_HI, None)], title="ONE NIGHT · 15 REGIONS",
            tag=t, labels=[]) if _A.T < c(0, 2) + 0.5 else _drone_count(o, t),
"CO-03": ration,
"CO-04": lambda o, t: flap([("UK DIESEL / LITRE", "---.--p", "199.18p"), ("US DIESEL / GALLON", "$-.--", "$6.52")], header="RECORD PRICES · SEP 2026", tag=t, hit_i=1),
"CO-05": lambda o, t: receipt(FULL_RECEIPT, show=len(FULL_RECEIPT), tag="") if _A.T < _A.DUR - 1.2 else lights_out(""),
"CO-06": lambda o, t: roadmap(o, t, ["THE BRIDGE", "THE DRONES", "THE PUMP", "1944", "YOUR BILL"]),
"P1-01": lambda o, t: part(1, "The bridge"),
"P1-02": lambda o, t: map_scene(KERCH, 10, lines=[(BR[0], BR[1], ORANGE, 6, 0, False)], measure=((36.50, 45.255), (36.66, 45.195), "≈ 19 KM", 0),
            pins=[(*KER, "KERCH · CRIMEA", PAPER_HI, None), (*TAMAN, "TAMAN · RUSSIA", PAPER_HI, None)], title="THE KERCH STRAIT", tag=t),
"P1-02b": lambda o, t: map_scene(KERCH, 10, lines=[((36.48, 45.34), (36.66, 45.23), PAPER, 3, None, True), (BR[0], BR[1], ORANGE, 6, 1 if len(_A.CUES) > 1 else None, False)],
            title="BEFORE 2018: FERRY ONLY", tag=t, pins=[(36.57, 45.29, "FERRY", PAPER_HI, 0)]),
"P1-03": lambda o, t: number("$3.7BN", "Road opened May 2018 · rail December 2019", kicker="WHAT THE BRIDGE COST", tag=t),
"P1-05": lambda o, t: map_scene(CRIMEA, 7, lines=[((38.6, 45.5), (36.55, 45.3), ORANGE, 6, None, False), ((38.6, 45.0), (36.6, 45.15), PAPER, 3, None, True)],
            pins=[(36.55, 45.3, "BRIDGE", ORANGE, None), (36.6, 45.1, "FERRY", PAPER_HI, None)], title="HOW FUEL REACHES CRIMEA", tag=t),
"P1-05b": lambda o, t: map_scene(CRIMEA, 7, pins=[(*SEV, "SEVASTOPOL · BLACK SEA FLEET", ORANGE, None), (33.98, 44.95, "AIRFIELD", PAPER_HI, None), (34.1, 45.6, "DEPOTS", PAPER_HI, None)],
            lines=[((34.1, 45.6), (34.4, 46.6), WARN, 4, 0, False), ((35.3, 45.3), (35.9, 46.6), WARN, 4, 0, False)], title="CRIMEA RUNS ON DIESEL", tag=t),
"P1-06": lambda o, t: timeline([("OCT 2022", "Truck bomb · road spans fall · fuel tankers burn"), ("JUL 2023", "Sea drones · 2 killed"), ("JUN 2025", "Charges at the pillars"), ("NOV 2026", "Two strikes, two days")], [0], title="ATTACKS ON THE BRIDGE", tag=t),
"P1-07": lambda o, t: timeline([("OCT 2022", "Truck bomb · road spans fall · fuel tankers burn"), ("JUL 2023", "Sea drones · 2 killed"), ("JUN 2025", "Charges at the pillars"), ("NOV 2026", "Two strikes, two days")], [1, 2], title="ATTACKS ON THE BRIDGE", tag=t),
"P1-08": lambda o, t: timeline([("OCT 2022", "Truck bomb · road spans fall · fuel tankers burn"), ("JUL 2023", "Sea drones · 2 killed"), ("JUN 2025", "Charges at the pillars"), ("NOV 2026", "Two strikes, two days")], [3], title="ATTACKS ON THE BRIDGE", tag=t, stamp_txt="2 STRIKES · 2 DAYS"),
"P1-09": lambda o, t: quote("Minor.", "Dmitry Peskov, Kremlin", "16 Nov 2026", tag=t),
"P1-11": lambda o, t: receipt([("UK DIESEL, FAMILY CAR", "≈ £110"), ("SINCE THE IRAN WAR", "+£31")], title="LINE 1", tag=t, show=0, cues_from=[c(0, 1.5), c(0, 1.5) + 2.5]),
"P1-12": lambda o, t: receipt([("UK DIESEL, FAMILY CAR", "≈ £110"), ("SINCE THE IRAN WAR", "+£31"), ("US TRUCK, 150 GAL", "≈ $920"), ("ON A YEAR AGO", "+$345")], title="LINE 1", tag=t, show=2,
            cues_from=[c(0, 1.5), sn(1) + 0.3], final_stamp=None),
"BR-01": subscribe_card,
"P2-01": lambda o, t: part(2, "The refinery war"),
"P2-02": refinery_cut,
"P2-03": lambda o, t: map_scene(RUSSIA, 4, hi2=["Ukraine"], pins=[(lo, la, "", ORANGE, None) for lo, la in REFS[:38]], title="38 MAJOR REFINERIES", tag=t,
            rings=[(33.5, 50.0, 1000, 1 if len(_A.CUES) > 1 else 0, "1,000 KM"), (33.5, 50.0, 2000, 1 if len(_A.CUES) > 1 else 0, "2,000 KM")]) ,
"P2-04c": lambda o, t: map_scene((-12, 34, 95, 68), 4, hi2=["Ukraine"], rings=[(34.0, 50.3, 2500, 0, "≈ 2,500 KM")], lines=[((-0.12, 51.5), MOSCOW, PAPER, 3, None, True)],
            pins=[(-0.12, 51.5, "LONDON", PAPER_HI, None), (*MOSCOW, "MOSCOW", PAPER_HI, None), (73.4, 55.0, "", RED, 0)], title="HOW FAR THE DRONES FLY", tag=t),
"P2-05": column_target,
"P2-06": lambda o, t: calendar(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG"], flames_every=3, title="A REFINERY HIT ABOUT EVERY 3 DAYS · JAN-AUG 2026", tag=t),
"P2-07": lambda o, t: linechart({"RUNS": [("2025", 5.4), ("JAN 26", 5.0), ("MAR", 4.6), ("MAY", 4.2), ("JUN 26", 3.8)]}, title="RUSSIAN REFINERY RUNS, MILLION BARRELS A DAY", unit="", marks=[("LOWEST SINCE 2004", 4, 0)], tag=t + " · SHAPE ILLUSTRATIVE BETWEEN POINTS", ylab_fmt="{:.1f}"),
"P2-07b": lambda o, t: gauge(58, "of capacity in use, June 2026", sub="3.8 of 6.5 million barrels a day", tag=t, outline_pct=100),
"P2-08": lambda o, t: gauge(55, "of refining knocked out", sub="Zelensky, 15 Nov 2026", tag=t, stamp_txt="CLAIM", valtxt=lambda e: "> " + countup("55", e) + "%"),
"P2-09": lambda o, t: icongrid(38, [(15, RED, 0, "15 OUT"), (12, ORANGE, 1, "12 REDUCED")], title="RUSSIA'S 38 MAJOR REFINERIES (UKRAINE'S COUNT)", tag=t, big=("> $23.2BN", 2)),
"P2-10": lambda o, t: bars([("KYIV CLAIM", 55), ("INDUSTRY ESTIMATE", 45)], title="HOW MUCH REFINING IS OUT?", unit="%", hi=None, tag=t, cues=[None, 0] if False else None),
"P2-12": scale_card,
"P2-12b": lambda o, t: typed(["LONG-RANGE SANCTIONS", "NO VOTE NEEDED IN BRUSSELS", "NO VOTE NEEDED IN WASHINGTON"], label="KYIV'S NAME FOR IT", tag=t),
"P3-01": lambda o, t: part(3, "The gas station with no gas"),
"P3-02": two_big,
"P3-03": lambda o, t: calendar(["APR", "MAY", "JUN", "JUL"], stamps=[(0, "PETROL", -1), (2, "JET FUEL", 0), (3, "DIESEL", 1)], title="RUSSIA BANS ITS OWN FUEL EXPORTS · 2026", tag=t) if True else None,
"P3-04": lambda o, t: map_scene(WRUS, 5, hi=["Russia"], pins=[(*MOSCOW, "MOSCOW · 30 L", ORANGE, 0)] + [(lo, la, "", WARN, None) for lo, la in REG[:17]], title="FUEL SALES LIMITS", tag=t),
"P3-06": lambda o, t: pricetags([("AT THE PUMP (CAPPED)", "71 ₽", INK, None), ("WHOLESALE", "105 ₽", CRIMSON, 0)], title="ONE LITRE OF PETROL · JUNE 2026", tag=t),
"P3-08": lambda o, t: linechart({"PETROL ₽/L": [("JAN 26", 65.5), ("MAR", 68.5), ("MAY", 72.0), ("JUL 27", 77.89)]}, title="RUSSIA: AVERAGE PETROL PRICE, 2026", marks=[("+19%", 3, 0)], tag=t + " · SHAPE ILLUSTRATIVE", ylab_fmt="{:.1f}"),
"P3-08b": lambda o, t: _doc(o, t, "GOVERNMENT DECREE (RECREATED SUMMARY)", ["Fuel grades permitted for sale:", "EURO 5 (standard)", "EURO 2, 3, 4 — permitted until 1 July 2027", "Applies to: refiners, wholesalers"], 2),
"P3-09": lambda o, t: quote("The authorities have run out of easy solutions.", "Sergey Vakulenko, Carnegie", "June 2026", tag=t),
"P3-09b": lambda o, t: tiles([("SCRAP THE CAP", "pump prices jump"), ("QR CODES", "ration by app"), ("QUEUES", "first come, first served")], title="THE HARD OPTIONS", tag=t),
"P3-10": lambda o, t: bars([("JUNE 2025", 1000), ("JUNE 2026", 141000)], title="BELARUS PETROL TO RUSSIA (TONNES, 1-25 JUNE)", unit=" t", tag=t, cues=None),
"P3-10b": lambda o, t: bars([("BELARUS · 25 DAYS OF JUNE", 141000), ("RUSSIA BURNS · ONE DAY", 110000)], title="25 DAYS OF HELP vs ONE DAY OF DEMAND", unit=" t", tag=t, cues=[-1, 0]),
"P3-11": lambda o, t: map_scene(WORLD, 3, hi=["Russia"], arcs=[((72.8, 19.0), NOVO, ORANGE, 4, 0, False), ((-7.6, 33.6), NOVO, ORANGE, 4, 0, False), ((29.0, 41.0), NOVO, ORANGE, 4, 0, False)],
            pins=[(72.8, 19.0, "INDIA", PAPER_HI, None), (-7.6, 33.6, "MOROCCO", PAPER_HI, None), (29.0, 41.0, "TURKEY", PAPER_HI, None)], title="> 6.6M BARRELS INTO RUSSIA SINCE AUGUST", tag=t),
"P3-13": lambda o, t: maths(o, t, ["30 litres (the Moscow limit)", "× 77.89 roubles a litre"], "= 2,337 ROUBLES", 0),
"P3-14": lambda o, t: number("$21.2BN", "Russia's oil export revenue · October 2026", kicker="THE TWIST", tag=t, badge="+65%"),
"P3-15": stacked,
"P3-16": lambda o, t: lights_out("Has this happened before?"),
"P4-01": lambda o, t: part(4, "The last time"),
"P4-03": lambda o, t: map_scene(GER, 6, hi=["Germany"], pins=[(lo, la, "", RED, None) for lo, la in PLANTS], title="THE OIL PLAN · MAY 1944 · 16 FUEL PLANTS", tag=t),
"P4-04": lambda o, t: bars([("APR 1944", 175000), ("JUL 1944", 30000), ("SEP 1944", 5000)], title="GERMAN SYNTHETIC AVIATION FUEL (TONNES)", unit=" t", hi=2, tag=t),
"P4-05": lambda o, t: typed(["PILOT TRAINING: CUT SHORT", "REASON: NO FUEL TO TRAIN WITH", "DEC 1944, ARDENNES: TAKE THEIR FUEL"], label="1944 FILE", tag=t),
"P4-06": lambda o, t: quote("Catastrophic.", "Albert Speer, armaments minister", "December 1944", tag=t),
"P4-07": then_now,
"P4-08": lambda o, t: map_scene(WORLD, 3, hi2=["Russia"], arcs=[(PRIM, (-46.6, -23.5), DIM, 3, None, True), (NOVO, (29.0, 41.0), DIM, 3, None, True), (NOVO, (103.8, 1.3), DIM, 3, None, True)],
            title="WHEN RUSSIA'S FUEL DISAPPEARS…", tag=t),
"P4-09": big_word,
"P5-01": lambda o, t: part(5, "The diesel bill"),
"P5-02": lambda o, t: map_scene(WORLD, 3, hi=["Russia"], arcs=[(PRIM, (-46.6, -23.5), WARN, 4, None, False), (NOVO, (29.0, 41.0), WARN, 4, None, False), (NOVO, (3.4, 6.5), WARN, 4, None, False), (NOVO, (103.8, 1.3), WARN, 4, None, False)],
            pins=[(*PRIM, "PRIMORSK", PAPER_HI, None), (*NOVO, "NOVOROSSIYSK", PAPER_HI, None)], title="WHERE RUSSIA'S DIESEL USED TO GO", tag=t),
"P5-03": pool,
"P5-04": lambda o, t: linechart({"EUROPE DIESEL MARGIN $/bbl": [("JUN 26", 45), ("JUL", 70), ("AUG", 85), ("1 SEP", 98.01), ("OCT", 60), ("16 OCT", 74)]}, title="EUROPE'S DIESEL MARGIN OVER CRUDE, $ A BARREL", marks=[("$98.01 · 1 SEP", 3, 0)], tag=t + " · SHAPE ILLUSTRATIVE BETWEEN POINTS", ylab_fmt="{:.0f}"),
"P5-05": lambda o, t: linechart({"EUROPE DIESEL MARGIN $/bbl": [("JUN 26", 45), ("JUL", 70), ("AUG", 85), ("1 SEP", 98.01), ("OCT", 60), ("16 OCT", 74)]}, title="TWO SHOCKS AT ONCE: RUSSIA'S BAN + THE GULF WAR", band=(20, 35, "A NORMAL YEAR (APPROX.)"), tag=t, hit=0.4, ylab_fmt="{:.0f}"),
"P5-05b": lambda o, t: gauge(8, "million barrels released by September", sub="of more than 20 million planned", tag=t, ring_max=20, outline_pct=20, unit="M"),
"P5-05c": us_tiles,
"P5-07": lambda o, t: flap([("UK DIESEL · JUNE 2022", "199.09p", "199.09p"), ("UK DIESEL · 28 SEP 2026", "199.09p", "199.18p")], header="BRITAIN'S DIESEL RECORD", tag=t, hit_i=0),
"P5-08": lambda o, t: headline("AP", "Trump strikes deal with Putin for Russian diesel in sharp reversal of U.S. policy", "9 Oct 2026", tag=t),
"P5-09": staircase,
"P5-10": two_quotes,
"P5-11": lambda o, t: linechart({"US DIESEL $/gal": [("YEAR AGO", 3.84), ("22 SEP", 6.52), ("9 OCT", 6.28), ("10 NOV", 6.13)]}, title="US DIESEL, NATIONAL AVERAGE", marks=[("$6.13", 3, 0)], tag=t, ylab_fmt="${:.2f}"),
"P5-12": lambda o, t: map_scene((22, 46, 80, 64), 4, hi=["Russia"], hi2=["Ukraine"], pins=[(32.0, 59.45, "KIRISHI", RED, None), (73.4, 55.0, "OMSK", RED, None)],
            lines=[((33, 50), (32.0, 59.45), ORANGE, 3, None, True), ((33, 50), (73.4, 55.0), ORANGE, 3, None, True)], title="THE STRIKES RESUME", tag=t),
"P5-13": lambda o, t: receipt([("UK DIESEL, FAMILY CAR", "≈ £110"), ("US TRUCK, 150 GAL", "≈ $920"), ("RUSSIAN DIESEL SUPPLY", "UNRELIABLE")], title="HALF-RECEIPT", tag=t, show=0,
            cues_from=[sn(1) + 0.2, sn(1) + 2.6, c(0, sn(2) + 1)]),
"W-01": lambda o, t: part(6, "Who wins, who's left behind"),
"W-02": lambda o, t: map_scene(BELARUS, 6, hi=["Belarus"], hi2=["Russia"], pins=[(28.6, 55.53, "NAFTAN", ORANGE, None), (29.25, 52.05, "MOZYR", ORANGE, None)],
            lines=[((28.6, 55.53), (37.6, 55.75), WARN, 5, 0, False), ((29.25, 52.05), (36.0, 53.5), WARN, 5, 0, False)], title="BELARUS · JAN-JUL 2026: PETROL TO RUSSIA ×25", tag=t),
"W-04": lambda o, t: map_scene(WORLD, 3, hi=["Russia"], arcs=[((72.8, 19.0), NOVO, PAPER_HI, 6, None, False), ((29.0, 41.0), NOVO, PAPER_HI, 6, None, False), ((-7.6, 33.6), NOVO, PAPER_HI, 6, None, False)],
            pins=[(72.8, 19.0, "INDIA", PAPER_HI, None), (29.0, 41.0, "TURKEY", PAPER_HI, None), (-7.6, 33.6, "MOROCCO", PAPER_HI, None), (-80.5, 30.5, "US REFINERS", CYAN, 0)],
            title="THE ARROWS REVERSED: FUEL FLOWING INTO RUSSIA", tag=t),
"W-05": lambda o, t: bars([("KYRGYZSTAN · PETROL", 90), ("TAJIKISTAN · FUEL IMPORTS", 84)], title="SHARE OF FUEL FROM RUSSIA", unit="%", tag=t, fmt="{:.0f}"),
"W-07": lambda o, t: map_scene(CASIA, 5, hi=["Kazakhstan", "Kyrgyzstan", "Tajikistan", "Uzbekistan", "Turkmenistan"], title="FAR FROM THE FRONT · STILL PAYING", tag=t,
            pins=[(74.6, 42.87, "BISHKEK", PAPER_HI, None), (68.78, 38.56, "DUSHANBE", PAPER_HI, None), (69.24, 41.3, "TASHKENT", PAPER_HI, None)]),
"W-08": lambda o, t: number("8.9 TRN ₽", "Russia's 2026 oil and gas revenue forecast, cut in September", kicker="MOSCOW'S BUDGET", strike="7.6 TRN ₽", tag=t),
"W-09": lambda o, t: receipt([("UK DIESEL, FAMILY CAR", "≈ £110"), ("US TRUCK, 150 GAL", "≈ $920"), ("CENTRAL ASIA PUMPS", "+15-25%"), ("YOUR SHARE", "?")], title="RUNNING TOTAL", tag=t, show=2, cues_from=[sn(0) + 1.0, c(0, sn(1) + 1)]),
"P6-01": lambda o, t: part(7, "Your table"),
"P6-02": lambda o, t: chain(["Farm", "Truck", "Factory", "Lorry", "Shop"], title="EVERYTHING YOU EAT RODE ON DIESEL", tag=t, times=[sn(1), sn(2), sn(2) + 1.3, sn(3), c(0, sn(3) + 1.3)]),
"P6-03": lambda o, t: maths(o, t, ["100,000 miles a year", "÷ 6.5 mpg = 15,385 gallons", "× $2.29 more per gallon"], "≈ +$35,000 A YEAR", 0),
"P6-10": lambda o, t: receipt([("UK DIESEL, FAMILY CAR", "≈ £110"), ("US TRUCK, 150 GAL", "≈ $920"), ("CENTRAL ASIA PUMPS", "+15-25%"), ("THE GAP RUSSIA LEFT", "IN EVERY DELIVERY")], title="RUNNING TOTAL", tag=t, show=3, cues_from=[c(0, 2.0)]),
"P6-11": comment_q,
"P7-01": lambda o, t: part(8, "What happens next"),
"P7-02": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR", "APR 27"], circles=[(0, "30 NOV · JET FUEL", 0)], title="THREE DATES TO WATCH", tag=t),
"P7-03": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR", "APR 27"], circles=[(0, "30 NOV · JET FUEL", -9), (2, "31 JAN · PETROL + DIESEL", 0)], title="THREE DATES TO WATCH", tag=t),
"P7-04": lambda o, t: calendar(["NOV 26", "DEC", "JAN 27", "FEB", "MAR", "APR 27"], circles=[(0, "30 NOV · JET FUEL", -9), (2, "31 JAN · PETROL + DIESEL", -9), (5, "APR · US WAIVER ENDS", 0)], title="THREE DATES TO WATCH", tag=t),
"P7-04b": race,
"P7-05": lambda o, t: scenario(1, "The squeeze stays", 0),
"P7-06": lambda o, t: scenario(2, "A slow ease", -1),
"P7-07": lambda o, t: scenario(3, "The wider war", 1),
"P7-08b": lambda o, t: map_scene(KERCH, 10, lines=[(BR[0], BR[1], ORANGE, 6, None, False)], title="A REFINERY IS A FRONT LINE. A FRONT LINE SENDS A BILL.", tag=""),
"RC-01": lambda o, t: receipt(FULL_RECEIPT, show=0, cues_from=[99]*6),
"RC-02": lambda o, t: receipt(FULL_RECEIPT[:1], show=0, cues_from=[0.3]),
"RC-03": lambda o, t: receipt(FULL_RECEIPT[:2], show=1, cues_from=[0.3]),
"RC-04": lambda o, t: receipt(FULL_RECEIPT[:3], show=2, cues_from=[0.3]),
"RC-05": lambda o, t: receipt(FULL_RECEIPT[:4], show=3, cues_from=[0.3]),
"RC-06": lambda o, t: receipt(FULL_RECEIPT[:5], show=4, cues_from=[0.3]),
"RC-07": lambda o, t: receipt(FULL_RECEIPT, show=5, cues_from=[0.4], final_stamp="PAID BY YOU"),
"RC-08": lambda o, t: endcard(next_title="MORE BILLS"),
}

def _drone_count(o, t):
    im = map_scene(WRUS, 5, hi=["Ukraine"], streams=(UA, REG, 520, 0), pins=[(*MOSCOW, "MOSCOW", PAPER_HI, None)], title="ONE NIGHT · 15 REGIONS", tag=t)
    d = D(im); hit = c(0, 2); e = ease_io((_A.T - lead(hit, 0.9))/0.9)
    d.rect((W - 470, 520, W - 60, 660), fill=(0, 0, 0, 170)); d.text((W - 440, 530), countup("1,336", e), f(96, "inter"), ORANGE)
    d.text((W - 440, 630), "DRONES DOWNED, SAYS RUSSIA", f(20, "inter"), PAPER)
    if len(_A.CUES) > 1: stamp(im, "TARGET: FUEL", W/2, 160, _A.CUES[1], col=ORANGE, size=70)
    return im
SPEC["CO-02"] = _drone_count

def _doc(o, t, title, rows, hi):
    im = base(); d = paper(im, (220, 100, W - 220, H - 120), seed=12)
    d.text((260, 130), title, f(26, "inter"), (120, 40, 20)); d.line([(260, 172), (W - 260, 172)], (60, 50, 40), 2)
    hit = c(0, 2.0)
    for i, r in enumerate(rows):
        y = 200 + i*70
        if i == hi:
            k = seg(lead(hit, 0.6), 0.5); d.rect((250, y - 6, 250 + (W - 500)*k, y + 46), fill=(240, 200, 60, 150))
        d.text((260, y), r, f(36 if i else 30, "inter" if i == hi else "reg"), (30, 26, 22))
    k = seg(hit + 0.3, 0.6)
    if k > 0: d.arc((230, 200 + hi*70 - 30, W - 230, 200 + hi*70 + 80), 200, 200 + 330*k, fill=RED, width=5)
    tagline(im, t); return im

UA_BOX = (21.5, 44.0, 41.0, 53.0)
SPEC.update({
"P2-11b": lambda o, t: _ua_energy(o, t),
"P5-10b": lambda o, t: map_scene(WORLD, 3, hi=["Russia"], hi2=["United States of America"], arcs=[(PRIM, (-74.0, 40.6), WARN, 4, 0, False)],
            pins=[(-74.0, 40.6, "US EAST COAST", PAPER_HI, None)], title="RUSSIAN FUEL TO THE US · OCT 2026: ≈ 34,000 BARRELS A DAY", tag=t),
"P5-12b": lambda o, t: card(["NO SIGNIFICANT EFFECT ON EXPORTS"], kicker="RUSSIA'S DEPUTY PM, ALEXANDER NOVAK, SAYS THE ATTACKS WILL HAVE", tag=t, stamp_txt="CLAIM", cues=[-1]),
"W-06b": lambda o, t: bars([("CHINA'S JET FUEL OFFER", 3000), ("KYRGYZSTAN'S FUEL, ONE MONTH", 125000)], title="HELP vs NEED (TONNES)", unit=" t", tag=t),
"P7-05b": lambda o, t: chain(["Bans roll over", "Belarus trains", "Winter demand"], title="SCENARIO 1 · WHAT IT LOOKS LIKE", tag=t),
"P7-06b": lambda o, t: linechart({"PRICE": [("SHOCK", 1.0), ("", 3.0), ("", 2.8), ("", 2.5), ("", 2.2), ("", 1.9), ("", 1.6)]}, title="UP LIKE A ROCKET, DOWN LIKE A FEATHER", tag="SCENARIO · SHAPE ILLUSTRATIVE", ylab_fmt=""),
"P7-07b": lambda o, t: _two_shocks(o, t),
})
def _ua_energy(o, t):
    im = map_scene(UA_BOX, 6, hi2=["Ukraine"], pins=[(35.0, 48.45, "DNIPRO", RED, 0), (30.5, 50.45, "", WARN, None), (36.2, 49.99, "", WARN, None), (32.0, 46.97, "", WARN, None), (35.1, 47.84, "", WARN, None)],
                   title="THE ENERGY WAR RUNS BOTH WAYS", tag=t)
    d = D(im); hit = c(0, 2); e = ease_io((_A.T - lead(hit, 0.9))/0.9)
    d.rect((W - 420, 520, W - 60, 660), fill=(0, 0, 0, 170)); d.text((W - 390, 530), countup("131", e), f(96, "inter"), RED)
    d.text((W - 390, 630), "STRIKES ON DNIPRO'S ENERGY (KYIV)", f(18, "inter"), PAPER)
    return im
def _two_shocks(o, t):
    im = base(); d = D(im); hit = c(0, 2.5)
    for i, (lab, x, col, t0) in enumerate([("GULF WAR", W*0.35, ORANGE, 0.3), ("RUSSIAN CRUDE", W*0.65, CRIMSON, lead(hit, 0.6))]):
        if _A.T < t0: continue
        for k in range(3):
            q = ((_A.T - t0)*0.5 + k/3) % 1.0; r = 40 + 260*q
            d.ell((x - r, 360 - r, x + r, 360 + r), outline=alpha(col, (1 - q)*0.9), width=4)
        center(d, 340, lab, f(34, "inter"), alpha(PAPER_HI, seg(t0, 0.4)), cx=x)
    if _A.T > hit: center(d, 620, "TWO OIL SHOCKS AT ONCE", f(44, "inter"), alpha(PAPER_HI, seg(hit, 0.4)))
    tagline(im, t); return im

# ---- v1.1: rows whose stock footage didn't match the line -> graphics; +4 rows for length ----
import random as _rnd
_rnd.seed(11)
_WS = [(_rnd.uniform(24.5, 38.5), _rnd.uniform(46.8, 51.6)) for _ in range(26)]
UKR = (21.5, 44.0, 41.0, 53.0)
SPEC.update({
"P2-04": lambda o, t: tiles([("SMALL PLANE", "lawnmower-sized engine"), ("WARHEAD", "aimed at one unit"), ("1,000+ KM", "low, slow, at night")], title="LONG-RANGE DRONES", tag=t, cues=[0, 1, 2]),
"P2-04b": lambda o, t: map_scene(UKR, 5, hi=["Ukraine"], pins=[(lo, la, "", ORANGE, None) for lo, la in _WS], title="NO SINGLE FACTORY TO BOMB", tag="ILLUSTRATION · dots are not real sites"),
"P2-04d": lambda o, t: number("≈ 600", "drones at the Moscow region in one night", kicker="MOSCOW'S MAYOR SAYS", tag=t, badge="CLAIM"),
"P2-13": lambda o, t: card(["YOU QUEUE."], kicker="WHEN THE REFINERIES GO DARK", tag=t, cues=[0]),
"P3-07": lambda o, t: card(["STOPPED SELLING TO SMALL STATIONS", "KEPT THE FUEL FOR THEIR OWN PUMPS", "SMALL STATIONS RAN DRY"], kicker="RUSSIA'S BIG FUEL SELLERS", tag=t, cues=None, style="serif"),
"P4-08b": lambda o, t: split(("US CRUDE · WTI", "≈ $88", "a barrel, mid-November 2026"), ("BRENT", "< $96", "with the US blockade of Iran still in place"), tag=t),
"P5-02b": lambda o, t: gauge(30, "less diesel from Russia's refineries", sub="IEA estimate, 2026", tag=t, valtxt=lambda e: "≈ -" + countup("30", e) + "%"),
"P6-07": lambda o, t: tiles([("BUSES", "and rickshaws"), ("PUMPS", "watering the fields"), ("GENERATORS", "when the grid fails")], title="SOUTH ASIA RUNS ON DIESEL", tag=t, cues=[0, 1, 2]),
"P6-08b": lambda o, t: card(["WAGES BUY LESS", "THE QUEUES COME HOME"], kicker="RUSSIA, FAR FROM THE FRONT", tag=t, cues=None),
"P6-08c": lambda o, t: receipt([("BUS FARE", "UP"), ("DELIVERY CHARGE", "UP"), ("FIELD WATERED", "LESS OFTEN"), ("SIGNED BY YOU", "NEVER")], title="SMALL LINES", tag="ILLUSTRATION", show=0, cues_from=[sn(1) + 0.4, c(0), c(0) + 1.6, c(1)]),
"P7-08": lambda o, t: tiles([("1", "same pace"), ("2", "ceasefire"), ("3", "strikes widen")], title="SCENARIOS, NOT FORECASTS", tag="SCENARIO", cues=None),
})

# ---- 360p review round 1 ----
def _co01(o, t):
    im = map_scene(KERCH, 10, lines=[(BR[0], BR[1], ORANGE, 6, None, False)],
                   pins=[(36.585, 45.275, "EXPLOSION REPORTED · ~02:22", RED, 0), (*KER, "CRIMEA", PAPER_HI, None), (*TAMAN, "RUSSIA", PAPER_HI, None)],
                   title="CRIMEAN BRIDGE · 16 NOV 2026", tag=t)
    return im
SPEC["CO-01"] = _co01
