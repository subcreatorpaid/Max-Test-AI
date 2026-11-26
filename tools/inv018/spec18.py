# INV-018 graphics spec: script code -> lambda(on_screen, tag) -> PIL frame (anim12 globals _A.T, CUES, SENTS).
# Main channel look (Round Two / INV-011 / INV-017): dark ledger, beige paper, Inter + Caladea + Bebas, animated on the word.
# New for this video: a sea set (mine cross-sections, a frigate hit below the waterline, a drone sweeping the sea floor,
# a barrel that splits into gallons and litres, a price ladder, two clocks). Every caption types on (typing18).
import sys, pathlib, math
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "inv012")); sys.path.insert(0, str(HERE.parent / "inv017"))
import anim12 as _A
from anim12 import *
import typing18; typing18.install()
from spec17 import treaty, checklist, roadmap, quote as quote17
import numpy as np
from PIL import Image, ImageDraw

quote = quote17
HZ = (54.6, 24.9, 58.4, 27.6); GULF = (47.0, 23.6, 58.9, 30.7); WIDE = (-12.0, 6.0, 70.0, 50.0)
STRAIT = (56.45, 26.45); FARSI = (50.17, 27.98); KUWAIT = (47.98, 29.37); QATAR = (51.55, 25.93); BAHRAIN = (50.55, 26.07)
SEA_TOP = (20, 44, 60); SEA_BOT = (8, 16, 22)

# ---------------- sea set ----------------
def sea(surface=220, floor=640):
    im = base(); arr = np.asarray(im).astype(np.float32)
    y0, y1 = int(surface*S), int(floor*S)
    for y in range(y0, min(PH, y1)):
        q = (y - y0) / max(1, y1 - y0); col = np.array(SEA_TOP)*(1 - q) + np.array(SEA_BOT)*q
        arr[y] = arr[y]*0.25 + col*0.75
    im = Image.fromarray(arr.clip(0, 255).astype(np.uint8)); d = D(im)
    pts = [(x, surface + 4*math.sin(x/38 + _A.T*1.6)) for x in range(0, W + 10, 10)]
    d.line(pts, (120, 170, 190), 3)
    d.rect((0, floor, W, H), fill=(34, 30, 26)); d.line([(0, floor), (W, floor)], (70, 62, 52), 3)
    rng = np.random.default_rng(5)
    for i in range(40):
        x = rng.random()*W; y = floor + 8 + rng.random()*50; d.ell((x, y, x + 6 + rng.random()*10, y + 5 + rng.random()*4), fill=(48, 42, 36))
    return im, d

def hull(d, x, y, L=420, col=(26, 26, 28), outline=(150, 150, 150)):
    """tanker / frigate silhouette sitting on the surface line y, bow to the right."""
    pts = [(x - L/2, y - 30), (x + L/2 - 40, y - 30), (x + L/2, y - 50), (x + L/2 - 30, y + 26), (x - L/2 + 20, y + 26)]
    d.poly(pts, fill=col); d.line(pts + [pts[0]], outline, 2)
    d.rect((x - L/2 + 30, y - 90, x - L/2 + 110, y - 30), fill=col, outline=outline)
    d.rect((x - L/2 + 50, y - 120, x - L/2 + 70, y - 90), fill=col)

def flash(im, x, y, t0, r=70):
    k = seg(t0, 0.15) * (1 - seg(t0 + 0.35, 1.2))
    if k <= 0: return im
    return glow(im, lambda g: g.ell((x - r, y - r, x + r, y + r), fill=(255, 210, 140, 255)), 46, 1.6*k)

def mine_x(o, t, mode="contact"):
    im, d = sea(); hit = c(0, 2.0); mx = 640
    sx = -260 + (mx + 260) * ease_io(min(1.0, (_A.T - 0.2) / max(0.6, hit - 0.2)))
    if mode == "contact":
        my = 296; d.line([(mx, 640), (mx, my + 40)], (120, 110, 96), 3)
        for j in range(8):
            a_ = j * math.pi / 4; d.line([(mx + 40*math.cos(a_), my + 40*math.sin(a_)), (mx + 58*math.cos(a_), my + 58*math.sin(a_))], (90, 86, 80), 6)
        d.ell((mx - 42, my - 42, mx + 42, my + 42), fill=(54, 52, 50), outline=(140, 130, 116), width=3)
        hull(d, sx, 220, 380)
        im = flash(im, mx, 250, hit); d = D(im)
        lab = "MOORED CONTACT MINE"
    else:
        my = 610; d.poly([(mx - 70, 640), (mx - 50, my - 10), (mx + 50, my - 10), (mx + 70, 640)], fill=(58, 56, 52), outline=(140, 130, 116))
        hull(d, sx, 220, 380)
        for i, (lab_, col) in enumerate((("MAGNET", CYAN), ("SOUND", ORANGE), ("PRESSURE", RED))):
            t0 = hit + i*0.9; k = seg(t0, 0.5)
            if k <= 0: continue
            r = 90 + i*95; d.arc((mx - r, my - r, mx + r, my + r), 200, 340, alpha(col, 0.9*k), 4)
            d.text((mx + r*0.62 + 14, my - r*0.78 - 18), lab_, f(26, "inter"), alpha(col, k))
        lab = "INFLUENCE MINE · ON THE SEA FLOOR"
    d.text((90, 70), lab, f(36, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, t); return im

def frigate(o, t, stage="hit"):
    im, d = sea(surface=330, floor=700); hit = c(0, 2.0); x = 640
    hull(d, x, 330, 760, col=(44, 46, 50), outline=(170, 170, 170))
    if stage == "hit":
        im = flash(im, 760, 380, hit, 90); d = D(im)
        k = seg(hit + 0.2, 0.4)
        if k > 0:
            d.ell((735, 342, 790, 372), fill=alpha((8, 8, 8), k))
            d.text((800, 400), "15-FT HOLE", f(34, "inter"), alpha(RED, k))
        pencil(d, [(620, 356), (680, 352), (720, 358), (760, 350)], hit + 0.6, 0.6, RED, 5, seed=3)
        if _A.T > hit + 1.2: d.text((520, 420), "KEEL BROKEN", f(30, "inter"), alpha(PAPER_HI, seg(hit + 1.2, 0.4)))
        d.text((90, 70), "USS SAMUEL B. ROBERTS · 14 APRIL 1988", f(34, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    else:
        t0 = c(0, 1.5); up = ease_io((_A.T - t0 + 1.0) / 1.2); dn = ease_io((_A.T - t0 - 0.6) / 1.2)
        bx = 560; by = 300
        if dn <= 0: d.rect((bx, by - 200*up, bx + 140, by + 50 - 200*up), fill=alpha((80, 70, 60), 1 - 0.7*up), outline=(150, 140, 120))
        if dn > 0: d.rect((bx, by - 260*(1 - dn), bx + 140, by + 50 - 260*(1 - dn)), fill=ORANGE + (230,), outline=PAPER_HI)
        d.text((bx + 170, by - 70), "315-TON NEW ENGINE ROOM", f(30, "inter"), alpha(ORANGE, seg(t0 + 0.6, 0.4)))
        d.text((90, 70), "BACK IN SERVICE · OCTOBER 1989", f(34, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, t); return im

def seafloor(o, t):
    im = base(); d = D(im); hit = c(0, _A.DUR*0.6)
    x0, y0, x1, y1 = 160, 150, W - 120, H - 110
    d.rect((x0, y0, x1, y1), fill=(16, 22, 26), outline=DIM, width=2)
    for i in range(1, 8): d.line([(x0, y0 + (y1 - y0)*i/8), (x1, y0 + (y1 - y0)*i/8)], (30, 38, 42), 1)
    rng = np.random.default_rng(9); objs = [(x0 + 60 + rng.random()*(x1 - x0 - 120), y0 + 30 + rng.random()*(y1 - y0 - 60)) for _ in range(9)]
    lanes = 8; lh = (y1 - y0) / lanes; total = max(1.0, _A.DUR - 0.8); q = max(0, min(1, (_A.T - 0.3) / total)) * lanes
    ln = int(q); fr = q - ln; ly = y0 + lh*(min(ln, lanes - 1) + 0.5)
    dx = x0 + 20 + (x1 - x0 - 40) * (fr if ln % 2 == 0 else 1 - fr)
    for i in range(min(ln, lanes)): d.rect((x0, y0 + lh*i, x1, y0 + lh*(i + 1)), fill=(40, 90, 110, 40))
    for j, (ox, oy) in enumerate(objs):
        lane = int((oy - y0) // lh); pos = (ox - x0 - 20) / (x1 - x0 - 40); tl = lane + (pos if lane % 2 == 0 else 1 - pos)
        if q < tl: d.ell((ox - 6, oy - 6, ox + 6, oy + 6), fill=(70, 66, 60)); continue
        tf = 0.3 + tl / lanes * total
        d.ell((ox - 9, oy - 9, ox + 9, oy + 9), fill=alpha(ORANGE, 0.5 + 0.5*(int(_A.T*6) % 2)) if _A.T < tf + 0.6 else (90, 40, 36))
        if _A.T >= tf + 0.6: d.line([(ox - 12, oy - 12), (ox + 12, oy + 12)], RED, 4); d.line([(ox - 12, oy + 12), (ox + 12, oy - 12)], RED, 4)
    if ln < lanes:
        d.rrect((dx - 22, ly - 9, dx + 22, ly + 9), 8, fill=(240, 200, 60)); d.arc((dx - 70, ly - 70, dx + 70, ly + 70), -25, 25, alpha(CYAN, 0.6), 2)
    d.text((x0, 90), "FIND · CHECK · DESTROY · REPEAT", f(34, "inter"), alpha(PAPER_HI, seg(0.2, 0.4)))
    tagline(im, t); return im

def barrel(o, t):
    im = base(); d = D(im); hit = c(0, 2.0); k = ease_io((_A.T - lead(hit, 0.8)) / 0.8)
    cx = W/2; sep = 300*k
    for side in (-1, 1):
        x = cx + side*sep*0.5
        d.rrect((x - 90, 190, x + 90, 470), 18, fill=(52, 70, 92) if side < 0 else (92, 60, 40), outline=PAPER, width=3)
        for yy in (250, 330, 410): d.line([(x - 90, yy), (x + 90, yy)], PAPER, 3)
    if k < 0.2: center(d, 500, "1 BARREL", f(40, "inter"), PAPER_HI)
    if k > 0.3:
        center(d, 500, countup("42", min(1, k*1.2)) + " US GALLONS", f(40, "inter"), alpha(CYAN, k), cx=cx - sep*0.5 - 40)
        center(d, 500, countup("159", min(1, k*1.2)) + " LITRES", f(40, "inter"), alpha(ORANGE, k), cx=cx + sep*0.5 + 40)
    center(d, 90, "THE MATHS", f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    tagline(im, t); return im

def ladder_price(lo, hi, lo_lab, hi_lab, bracket="", title="", tags=()):
    im = base(); d = D(im); hit = c(0, 2.0)
    x = 420; y0, y1 = H - 140, 140; vmin, vmax = 60, 140
    Y = lambda v: y0 - (y0 - y1) * (v - vmin) / (vmax - vmin)
    d.line([(x, y0), (x, y1)], PAPER, 3)
    for v in range(60, 141, 20): d.line([(x - 10, Y(v)), (x + 10, Y(v))], PAPER, 2); d.text((x - 80, Y(v) - 14), f"${v}", f(24, "reg"), GREY)
    d.ell((x - 14, Y(lo) - 14, x + 14, Y(lo) + 14), fill=CYAN); d.text((x + 34, Y(lo) - 22), lo_lab, f(32, "inter"), alpha(CYAN, seg(0.2, 0.4)))
    e = ease_io((_A.T - lead(hit, 1.0)) / 1.0); v = lo + (hi - lo)*e
    if e > 0:
        d.line([(x, Y(lo)), (x, Y(v))], ORANGE, 10); d.ell((x - 16, Y(v) - 16, x + 16, Y(v) + 16), fill=ORANGE)
        d.text((x + 34, Y(hi) - 22), hi_lab, f(32, "inter"), alpha(ORANGE, seg(hit, 0.4)))
        if bracket and e >= 1:
            pencil(d, [(x - 40, Y(lo)), (x - 60, Y(lo)), (x - 60, Y(hi)), (x - 40, Y(hi))], hit + 0.3, 0.5, RED, 4, seed=7)
            fb = f(36, "inter"); d.text((x - 100 - d.tl(bracket, fb), (Y(lo) + Y(hi))/2 - 22), bracket, fb, alpha(RED, seg(hit + 0.6, 0.4)))
    for i, (lab, price, col) in enumerate(tags):
        t0 = c(1 + i, hit + 1.2 + i*0.9) if len(_A.CUES) > 1 + i else hit + 1.6 + i*1.2; kk = seg(t0, 0.4)
        if kk <= 0: continue
        bx = 780; by = 220 + i*190
        d.rect((bx, by, bx + 380, by + 150), fill=alpha(PAPER, kk)); d.ell((bx + 16, by + 66, bx + 34, by + 84), fill=INK)
        d.text((bx + 56, by + 18), lab, f(26, "inter"), alpha((60, 50, 40), kk)); d.text((bx + 56, by + 56), price, f(64, "inter"), alpha(col, kk))
    if title: d.text((180, 60), title, f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    tagline(im, _A.TAG if hasattr(_A, "TAG") else ""); return im

def clocks(o, t):
    im = base(); d = D(im); hit = c(0, 2.0)
    for i, (cx, lab, spd, col) in enumerate(((400, "LAY IT · 1 DAY", 0.25, CYAN), (880, "CLEAR IT · UP TO 200x LONGER", 6.0 * seg(hit, 0.5) + 0.25, RED))):
        a = seg(0.2 + i*0.3, 0.4); r = 150
        d.ell((cx - r, 330 - r, cx + r, 330 + r), outline=alpha(PAPER, a), width=5)
        for h in range(12): ang = h*math.pi/6; d.line([(cx + (r - 18)*math.sin(ang), 330 - (r - 18)*math.cos(ang)), (cx + (r - 6)*math.sin(ang), 330 - (r - 6)*math.cos(ang))], alpha(PAPER, a), 3)
        ang = _A.T*spd*2*math.pi; d.line([(cx, 330), (cx + (r - 30)*math.sin(ang), 330 - (r - 30)*math.cos(ang))], col, 6)
        center(d, 510, lab, fit(d, lab, 32, 460), alpha(col, a), cx=cx)
    tagline(im, t); return im

def dots(n_on, n_total, label, big="", col=ORANGE, title="", per=None):
    im = base(); d = D(im); hit = c(0, 2.0); cols = 25; rows = (n_total + cols - 1) // cols
    x0, y0, gs = (W - cols*34)/2, 150, 34
    for i in range(n_total):
        x = x0 + (i % cols)*gs; y = y0 + (i // cols)*gs; t0 = lead(hit, 1.0) + i * 1.0 / max(1, n_on)
        on = i < n_on and _A.T >= t0
        d.ell((x, y, x + 22, y + 22), fill=alpha(col, seg(t0, 0.15)) if on else (54, 50, 46))
    ly = y0 + rows*gs + 30
    d.text((x0, ly), label, f(30, "inter"), alpha(PAPER_HI, seg(0.3, 0.4)))
    if per: d.text((x0, ly + 44), per, f(22, "reg"), alpha(GREY, seg(0.3, 0.4)))
    if big: d.text((W - 380, 40), countup(big, ease_io((_A.T - lead(hit, 1.0))/1.0)), f(60, "inter"), alpha(col, seg(lead(hit, 1.0), 0.3)))
    if title: d.text((180, 60), title, f(34, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    tagline(im, _A.TAG if hasattr(_A, "TAG") else ""); return im

def two_numbers(lk, lv, rk, rv, tag="", note=""):
    im = base(); d = D(im)
    for side, (k_, v) in enumerate(((lk, lv), (rk, rv))):
        t0 = 0.2 if side == 0 else lead(c(0), 0.6); e = ease_io((_A.T - t0) / 0.9); cx = W*0.3 if side == 0 else W*0.7
        center(d, 190, k_, f(34, "inter"), alpha(ORANGE if side else CYAN, seg(t0, 0.4)), cx=cx)
        center(d, 250, countup(v, e), fit(d, v, 110, W*0.4), alpha(PAPER_HI, min(1, e*3)), cx=cx)
    d.line([(W/2, 170), (W/2, 520)], DIM, 3)
    if note: center(d, 520, note, f(30, "serif"), alpha(ORANGE, seg(c(0, 1.0) + 0.8, 0.5)))
    tagline(im, tag); return im

def hz(pins=(), title="", tag="", measure=None, lines=(), rings=(), labels=()):
    return map_scene(HZ, z=8, hi=("Iran",), pins=pins, title=title, tag=tag, measure=measure, lines=lines, rings=rings, labels=labels)

def subscribe_card(o, t):
    im = base(); d = D(im)
    center(d, 110, "1 OF 4 · THE IRAN WAR BILL", f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
    center(d, 190, "NEXT WEEK", f(40, "inter"), alpha(PAPER, seg(0.3, 0.4)))
    center(d, 250, "WHAT IF THE IRAN WAR ENDS TOMORROW?", fit(d, "WHAT IF THE IRAN WAR ENDS TOMORROW?", 54, 1000), alpha(PAPER_HI, seg(0.6, 0.4)))
    b = seg(lead(c(0, 3.0), 0.5), 0.4)
    d.rrect((W/2 - 190, 420, W/2 + 190, 510), 14, fill=alpha(CRIMSON, b)); center(d, 440, "SUBSCRIBE", f(44, "inter"), alpha(PAPER_HI, b))
    return im

def tagged(fn):
    """wrap a helper that reads the tag from _A.TAG"""
    def w(o, t, *a, **k):
        _A.TAG = t
        try: return fn(*a, **k)
        finally: _A.TAG = ""
    return w

P = lambda n, title: (lambda o, t: part(n, title))
RT = ["3 TANKERS · CLAIM", "$1,500 MINE · $89.5M REPAIR", "UP TO 6 MONTHS TO CLEAR", "INSURANCE: THOUSANDS → MILLIONS", "+22p A LITRE · +90¢ A GALLON"]
RUN = [("A $1,500 MINE · AN $89.5M REPAIR", "LINE 1"), ("A MINE ONLY HAS TO EXIST", "LINE 2"), ("OIL $88 TODAY · $126 AT THE PEAK", "LINE 3"), ("+22p A LITRE · +90¢ A GALLON (IF $126)", "LINE 4")]
L = lambda lon, lat: (lon, lat)

SPEC = {
"CO-01": lambda o, t: hz(pins=[(57.05, 25.95, "TANKER 1", ORANGE, 0), (57.35, 25.7, "TANKER 2", ORANGE, 0), (55.9, 25.95, "TANKER 3", ORANGE, 0)],
                        title="23 NOV 2026 · THE IRGC'S CLAIM", tag=t, labels=[(56.0, 26.9, "IRAN", 28, PAPER_HI), (55.6, 25.2, "UAE", 24, PAPER), (57.6, 24.95, "OMAN", 24, PAPER)]),
"CO-02": lambda o, t: card(["WHAT IF IRAN", "MINES HORMUZ?"], tag=t, stamp_txt="FOR REAL?"),
"CO-03": lambda o, t: ladder_price(88, 126, "$88 · TODAY", "$126 · THE 2026 PEAK", bracket="+$38", title="BRENT CRUDE, $ A BARREL",
                                   tags=[("UK · PER LITRE", "+22p", ORANGE), ("US · PER GALLON", "+90¢", RED)]) if not setattr(_A, "TAG", t) else None,
"CO-04": lambda o, t: two_numbers("THE MINE", "$1,500", "THE REPAIR", "$89,500,000", tag=t, note="USS Samuel B. Roberts · 1988"),
"CO-05": lambda o, t: roadmap(o, t, ["THE CLAIM", "THE WEAPON", "THE CLEAN-UP", "THE CARGO", "YOUR BILL"]),

"P1-01": P(1, "What Iran says happened"),
"P1-02": lambda o, t: hz(pins=[(55.75, 25.95, "NEAR THE SOUTHERN COAST", ORANGE, None), (57.1, 25.85, "EAST OF THE STRAIT", RED, 0), (57.4, 25.55, "", RED, 0)],
                        title="WHERE THE IRGC SAYS THE MINES WERE", tag=t, labels=[(56.0, 26.9, "IRAN", 28, PAPER_HI), (57.6, 24.95, "OMAN", 24, PAPER)]),
"P1-02b": lambda o, t: hz(title="A NARROW DOOR", tag=t, measure=((56.36, 26.38), (56.52, 26.92), "≈ 21 MILES", 0),
                         lines=[((55.6, 26.25), (57.0, 26.15), CYAN, 5, 0, False), ((55.6, 26.45), (57.0, 26.35), ORANGE, 5, 0, False)],
                         labels=[(56.9, 26.05, "INBOUND · 2 MILES", 22, CYAN), (56.9, 26.6, "OUTBOUND · 2 MILES", 22, ORANGE)]),
"P1-03": lambda o, t: quote("Will not serve as a substitute", "IRGC statement via IRNA", "24 Nov 2026", tag=t),
"P1-04": lambda o, t: checklist(["SHIP NAMES?", "CREW?", "PHOTOS?", "US COMMENT?"], title="WHAT WE HAVEN'T SEEN", tag=t),
"P1-05": lambda o, t: typed(["17 NOV · SUPERTANKER · 2M+ BARRELS", "17 NOV · LNG CARRIER · 'UNAUTHORISED'"], label="IRGC CLAIM", tag=t, cue_lines=[0, 0]),
"P1-06": lambda o, t: card(["NOVEMBER MINES:", "A CLAIM, NOT PROVEN"], tag=t, stamp_txt="CLAIM"),
"P1-07": lambda o, t: bars([("OCTOBER", 30), ("NOVEMBER (TO 22 NOV)", 22)], title="ATTACKS ON SHIPS PER MONTH", unit="+", hi=0, tag=t, cues=[0, 0]),
"P1-08": lambda o, t: gauge(65, "below pre-war traffic", sub="308 crossings in 7 days", tag=t),
"P1-09": lambda o, t: timeline([("28 FEB", "War begins"), ("8 APR", "Ceasefire"), ("13 APR", "US blockade"), ("NOV", "No talks")], [0], title="HOW WE GOT HERE · 2026", tag=t),
"P1-10": lambda o, t: timeline([("10 MAR", "US intel: Iran laying mines"), ("25 AUG", "100+ suspected mines found")], [0, 1], title="MINES IN THIS WAR", tag=t),
"P1-10b": lambda o, t: pricetags([("TOLL PER SHIP · APRIL", "$1M+", ORANGE, 0)], title="TO PASS THE STRAIT", tag=t),
"P1-10c": lambda o, t: typed(["OPERATION PROJECT FREEDOM", "4 MAY · 7 SMALL BOATS SUNK"], label="US ESCORT MISSION", tag=t, cue_lines=[-1, 0], stamps=[("PAUSED", c(0) + 0.8)]),
"P1-10d": lambda o, t: timeline([("MAY", "US escorts"), ("8 JUL", "Truce collapses"), ("15 JUL", "Blockade back"), ("NOV", "Mines?")], [1], title="THE SUMMER", tag=t),
"P1-11": lambda o, t: card(["NOT 'CAN IRAN?'", "WHAT IF IT GOES ALL THE WAY?"], tag=t),

"BR-01": subscribe_card,

"P2-01": P(2, "The cheapest weapon at sea"),
"P2-02": lambda o, t: mine_x(o, t, "contact"),
"P2-03": lambda o, t: mine_x(o, t, "influence"),
"P2-04": lambda o, t: dots(60, 60, "EACH DOT ≈ 100 MINES", big="6,000", title="IRAN'S ESTIMATED MINES", per="estimate: 5,000-6,000") if not setattr(_A, "TAG", t) else None,
"P2-05": lambda o, t: bars([("LAY IT", 5), ("CLEAR IT", 100)], title="COST TO LAY VS COST TO CLEAR (INDEX)", unit="", hi=1, tag=t, cues=[-1, 0]),
"P2-06": lambda o, t: two_numbers("SHIPS DAMAGED BY MINES", "14", "BY PLANES + MISSILES", "4", tag=t, note="US Navy, since World War II"),
"P2-07": lambda o, t: card(["1987", "THE TANKER WAR"], kicker="IRAN-IRAQ WAR · YEAR 7", tag=t),
"P2-08": lambda o, t: map_scene(GULF, z=6, hi=("Iran",), pins=[(FARSI[0], FARSI[1], "BRIDGETON · 24 JUL 1987", RED, 0), (KUWAIT[0], KUWAIT[1], "KUWAIT", PAPER_HI, None)],
                                lines=[((56.4, 26.3), (FARSI[0] + 0.3, FARSI[1] - 0.2), ORANGE, 4, None, True)], title="THE FIRST US CONVOY", tag=t),
"P2-09": lambda o, t: split(("1987", "MINE HIT", "the first US convoy"), ("2026", "MINES?", "Iran's claim, unconfirmed"), tag=t),
"P2-10": lambda o, t: typed(["SHIP: IRAN AJR", "21 SEP 1987 · CAUGHT LAYING MINES"], label="US NAVY", tag=t, cue_lines=[-1, 0]),
"P2-11": lambda o, t: frigate(o, t, "hit"),
"P2-12": lambda o, t: stats3([("10", "sailors injured", 0), ("5 HOURS", "fighting fire and flooding", 0), ("AFLOAT", "she didn't sink", 0)], title="SAVING THE SHIP", tag=t),
"P2-12b": lambda o, t: frigate(o, t, "repair"),
"P2-13": lambda o, t: chain(["MINES FOUND", "SERIALS MATCH", "IRAN AJR", "PRAYING MANTIS"], title="THE EVIDENCE · APRIL 1988", tag=t),
"P2-13b": lambda o, t: stats3([("2", "oil platforms hit", 0), ("SAHAND", "frigate", 0), ("SABALAN", "frigate", 0)], title="18 APRIL 1988 · OPERATION PRAYING MANTIS", tag=t),
"P2-13c": lambda o, t: number("290", kicker="IRAN AIR 655 · 3 JULY 1988", sub="shot down by mistake by the USS Vincennes", tag=t),
"P2-14": lambda o, t: split(("18 FEB 1991", "TRIPOLI", "USS Tripoli, hit by an Iraqi mine"), ("≈ 3 HOURS LATER", "PRINCETON", "USS Princeton, hit by Iraqi mines"), tag=t),
"P2-14b": lambda o, t: dots(40, 40, "1,000+ MINES IN FIVE MONTHS · EACH DOT ≈ 25", big="1,000", title="IRAQ, 1991", col=RED) if not setattr(_A, "TAG", t) else None,
"P2-15": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0),

"P3-01": P(3, "Why you can't just sweep it"),
"P3-02": lambda o, t: card(["YOU DON'T HAVE TO SINK A SHIP.", "YOU HAVE TO MAKE THEM BELIEVE."], tag=t),
"P3-03": clocks,
"P3-04": seafloor,
"P3-04b": lambda o, t: typed(["25 AUG 2026 · 100+ SUSPECTED MINES", "REMOVED BY PRIVATE CONTRACTORS"], label="US OFFICIALS", tag=t, cue_lines=[-1, 0]),
"P3-05": lambda o, t: calendar(["1", "2", "3", "4", "5", "6"], circles=[(5, "UP TO 6 MONTHS", 0)], stamps=[(2, "AFTER THE FIGHTING", 0)], title="THE CLEAN-UP CLOCK · PENTAGON, APR 2026", tag=t),
"P3-06": lambda o, t: card(["PEACE ON PAPER.", "MINES IN THE WATER."], tag=t),
"P3-07": lambda o, t: flow({"a": (260, 360, "TANKER OWNER", PAPER_HI), "b": (640, 360, "INSURER", ORANGE), "c": (1010, 360, "NO COVER = NO SAILING", RED)},
                            [("a", "b", "asks for cover", 0), ("b", "c", "", 0)], title="WHO REALLY DECIDES", tag=t),
"P3-07b": lambda o, t: split(("LEGALLY", "OPEN", "no law closed the strait"), ("IN PRACTICE", "CLOSED", "war cover withdrawn, 5 Mar 2026"), tag=t),
"P3-08": lambda o, t: two_numbers("BEFORE THE WAR", "$54,000", "NOW (CLAIM)", "$64,000,000", tag=t, note="per trip · Hung Cao to the US Senate, 17 Nov · unverified"),
"P3-09": lambda o, t: bars([("BEFORE · 1-3%", 3), ("NOW · 7.5-10%", 10)], title="WAR COVER, % OF THE SHIP'S VALUE · S&P", unit="%", hi=1, tag=t, cues=[-1, 0], reveal=(1, "≈ $21M A TRIP")),
"P3-10": lambda o, t: chain(["INSURANCE", "FREIGHT", "CARGO PRICE", "YOUR BILL"], title="WHERE THE PREMIUM GOES", tag=t),
"P3-11": lambda o, t: dots(80, 80, "EACH DOT ≈ 250 SEAFARERS · 2,000 SHIPS", big="20,000", title="STUCK IN THE GULF · IMO, APRIL 2026", col=CYAN) if not setattr(_A, "TAG", t) else None,
"P3-12": lambda o, t: receipt(RUN[:2], title="RUNNING TOTAL", tag=t, show=1),

"P4-01": P(4, "What's on those ships"),
"P4-02": lambda o, t: map_scene(GULF, z=6, hi=("Iran",), title="≈ 20 MILLION BARRELS A DAY", tag=t, streams=((50.5, 27.0), [(57.8, 25.0)], 40, 0),
                                labels=[(52.0, 29.8, "IRAN", 28, PAPER_HI), (51.0, 24.4, "SAUDI · UAE · QATAR · KUWAIT · IRAQ", 20, PAPER)]),
"P4-03": lambda o, t: split(("OIL MOVED BY SEA", "≈ 25%", "before the war"), ("WORLD LNG", "≈ 20%", "before the war"), tag=t),
"P4-04": lambda o, t: globe((85, 25), arcs=[(STRAIT, (116.4, 39.9), "CHINA", 0), (STRAIT, (77.2, 28.6), "INDIA", 1), (STRAIT, (139.7, 35.7), "JAPAN", 2), (STRAIT, (127.0, 37.5), "SOUTH KOREA", 3)],
                            title="84% OF IT WENT TO ASIA (2024)", tag=t),
"P4-04b": lambda o, t: gauge(33, "of China's oil came through Hormuz", sub="the world's biggest buyer", tag=t, valtxt=lambda e: "≈ ⅓"),
"P4-05": lambda o, t: flow({"a": (250, 360, "ASIA LOSES GULF OIL", PAPER_HI), "b": (640, 360, "BIDS FOR OTHER BARRELS", ORANGE), "c": (1030, 360, "PRICES RISE EVERYWHERE", RED)},
                            [("a", "b", "", 0), ("b", "c", "", 0)], title="ONE WORLD MARKET", tag=t),
"P4-06": lambda o, t: map_scene(WIDE, z=4, hi=("Qatar",), title="QATAR'S GAS TO EUROPE · 12-14% OF EUROPE'S LNG", tag=t,
                                lines=[((51.6, 25.9), (56.4, 26.4), ORANGE, 4, None, False), ((56.4, 26.4), (58.5, 22.5), ORANGE, 4, None, False), ((58.5, 22.5), (43.4, 12.6), ORANGE, 4, None, False),
                                       ((43.4, 12.6), (32.5, 29.9), ORANGE, 4, None, False), ((32.5, 31.2), (5.0, 43.0), ORANGE, 4, 0, False)],
                                pins=[(56.4, 26.4, "HORMUZ", RED, None), (QATAR[0], QATAR[1], "QATAR", ORANGE, None)]),
"P4-07": lambda o, t: dots(30, 100, "UP TO 30% OF TRADED FERTILISER SAILS THROUGH HORMUZ", big="30%", title="FERTILISER", col=GREEN) if not setattr(_A, "TAG", t) else None,
"P4-08": lambda o, t: linechart({"UREA": [("FEB", 100), ("MID MAR", 125), ("LATE MAR", 150)]}, title="UREA PRICE, INDEX (FEB = 100)", tag=t, marks=[("+50%", 2, 0)]),
"P4-09": lambda o, t: chain(["FERTILISER", "SPRING", "HARVEST", "BREAD"], title="≈ A YEAR FROM FIELD TO SHELF", tag=t),
"P4-10": lambda o, t: linechart({"BRENT": [("JAN", 70), ("8 MAR", 100), ("PEAK", 126), ("JUL", 90), ("24 NOV", 88)]}, title="BRENT CRUDE IN 2026, $ A BARREL", tag=t,
                                 marks=[("$100 · 8 MAR", 1, 0), ("PEAK $126", 2, 0)], ylab_fmt="${:g}"),
"P4-10b": lambda o, t: gauge(70, "traffic drop on day one", sub="28 Feb 2026 · fear, not mines", tag=t),
"P4-11": lambda o, t: receipt(RUN[:3], title="RUNNING TOTAL", tag=t, show=2),

"P5-01": P(5, "Your bill"),
"P5-02": lambda o, t: card(["START AT THE PUMP"], tag=t),
"P5-03": lambda o, t: pricetags([("UK PETROL", "171.8p", ORANGE, -1), ("UK DIESEL", "198.4p", RED, 0)], title="PER LITRE · WEEK TO 1 NOV 2026", tag=t),
"P5-04": lambda o, t: number("$3.78", kicker="US AVERAGE GALLON · 17 NOV 2026", sub="lowest since March, still above pre-war", tag=t),
"P5-05": barrel,
"P5-06": lambda o, t: ladder_price(88, 126, "$88 · TODAY", "$126 · THE PEAK", bracket="+$38 A BARREL", title="IF A MINE WAR SENT OIL BACK TO THE PEAK") if not setattr(_A, "TAG", t) else None,
"P5-07": lambda o, t: pricetags([("US · EVERY GALLON", "+90¢", RED, 0)], title="CRUDE COST ONLY (OUR MATHS)", tag=t),
"P5-08": lambda o, t: stacked([("CRUDE ≈ 18p", 18, ORANGE, -1), ("VAT ≈ 4p", 4, RED, 0)], title="UK · EVERY LITRE (OUR MATHS, $1.30/£)", total="≈ +22p", tag=t),
"P5-09": lambda o, t: pricetags([("55-LITRE TANK", "+£12", ORANGE, 0)], title="EVERY FILL-UP (OUR MATHS)", tag=t),
"P5-09b": lambda o, t: linechart({"CRUDE": [("W1", 88), ("W2", 126), ("W3", 126), ("W4", 110), ("W5", 100), ("W6", 95)], "PUMP": [("W1", 88), ("W2", 92), ("W3", 110), ("W4", 122), ("W5", 118), ("W6", 112)]},
                                  title="THE PUMP LAGS (SHAPE ILLUSTRATIVE)", tag=t),
"P5-10": lambda o, t: number("$4.50+", kicker="US AVERAGE GALLON · MAY 2026", sub="a four-year record", tag=t),
"P5-11": lambda o, t: number("$71.1 BN", kicker="BROWN UNIVERSITY ESTIMATE", sub="extra US fuel costs, February to July 2026", tag=t),
"P5-12": lambda o, t: chain(["DIESEL", "LORRIES", "SHOPS", "YOUR BASKET"], title="DIESEL MOVES EVERYTHING", tag=t),
"P5-12b": lambda o, t: number("$5.11", kicker="US DIESEL · JULY 2026", sub="on every truckload of food", tag=t),
"P5-13": lambda o, t: chain(["QATAR LNG", "GAS PRICE", "POWER PRICE", "YOUR BILL"], title="GAS SETS THE PRICE OF POWER", tag=t),
"P5-14": lambda o, t: chain(["FERTILISER", "FARMS", "FLOUR", "BREAD"], title="THE SLOW ONE", tag=t),
"P5-15": lambda o, t: receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=3),

"P6-01": P(6, "What happens next"),
"P6-02": lambda o, t: tiles([("THE CLAIMS FADE", "traffic returns, oil drifts lower"), ("A MONTH OF MINES", "ships stop, oil back to the peak"), ("A LONG MINE WAR", "no deal, a long clean-up")], title="THREE PATHS · NOT A FORECAST", tag=t, cues=[-1, 50, 50]),
"P6-02b": lambda o, t: checklist(["CROSSINGS CLIMBING", "INSURANCE FALLING", "FEWER WARNINGS"], title="SIGNS OF PATH 1", tag=t),
"P6-03": lambda o, t: tiles([("THE CLAIMS FADE", "traffic returns, oil drifts lower"), ("A MONTH OF MINES", "+22p a litre · +90¢ a gallon"), ("A LONG MINE WAR", "no deal, a long clean-up")], title="PATH 2", tag=t, cues=[-1, 0, 9]),
"P6-03b": lambda o, t: card(["CHEAP. QUICK.", "HARD TO PROVE."], tag=t),
"P6-04": lambda o, t: tiles([("THE CLAIMS FADE", "traffic returns, oil drifts lower"), ("A MONTH OF MINES", "+22p a litre · +90¢ a gallon"), ("A LONG MINE WAR", "the 6-month clock starts later")], title="PATH 3", tag=t, cues=[-1, -1, 0]),
"P6-04b": lambda o, t: chain(["DIESEL", "GAS", "FERTILISER", "A YEAR OF BILLS"], title="THE BILL OUTLASTS THE NEWS", tag=t),
"P6-05": lambda o, t: typed(["SANCTIONS LIFTED", "BLOCKADE ENDED", "FROZEN FUNDS RELEASED"], label="IRAN'S CONDITIONS FOR TALKS", tag=t),
"P6-05b": lambda o, t: number("2.82M", kicker="RIALS PER US DOLLAR · 24 NOV 2026", sub="down about 5% in a day, black market", tag=t),
"P6-06": lambda o, t: checklist(["SHIP NAMES + PHOTOS", "WEEKLY CROSSINGS", "WAR INSURANCE RATES"], title="WHAT TO WATCH", tag=t),
"P6-07": lambda o, t: card(["THE PEOPLE WHO LAY THE MINES", "DON'T PAY FOR THEM."], tag=t, stamp_txt="EVERYONE ELSE DOES"),
}
SPEC["RC-01"] = lambda o, t: receipt(RT, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(5):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RT[:i+1], title="THE RECEIPT", tag="", show=i))(i)
SPEC["RC-07"] = lambda o, t: receipt(RT + [("PAID BY EVERYONE", "")], title="THE RECEIPT", tag="", show=5, final_stamp="PAID")
SPEC["RC-08"] = lambda o, t: endcard("WHAT HAPPENS IF THE IRAN WAR RESTARTS?", "Every crisis sends a bill. History keeps the receipts.")
