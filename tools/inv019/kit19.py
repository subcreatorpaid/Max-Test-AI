# Shared graphics for INV-019 / INV-020 (Iran series 2 and 3). Builds on anim12 + spec17 + spec18 (typing installed by spec18).
import sys, pathlib, math
HERE = pathlib.Path(__file__).resolve().parent
for p in ("inv012", "inv017", "inv018"): sys.path.insert(0, str(HERE.parent / p))
import anim12 as _A
from anim12 import *
import spec18 as S18
from spec18 import ladder_price, dots, two_numbers, barrel, seafloor, hz, HZ, GULF, WIDE, STRAIT, QATAR, KUWAIT
from spec17 import checklist, roadmap, quote as quote17
quote = quote17
P = lambda n, title: (lambda o, t: part(n, title))

def tg(fn):
    """call fn() with the shot tag available to helpers that read _A.TAG"""
    def w(o, t):
        _A.TAG = t
        try: return fn()
        finally: _A.TAG = ""
    return w

def ladder2(start, end, start_lab, end_lab, vmin, vmax, step, fmt="${:g}", bracket="", title="", tag=""):
    """a price moving from start to end on a vertical scale (either direction), on the cue word"""
    im = base(); d = D(im); hit = c(0, 2.0)
    x = 470; y0, y1 = H - 130, 150
    Y = lambda v: y0 - (y0 - y1) * (v - vmin) / (vmax - vmin)
    d.line([(x, y0), (x, y1)], PAPER, 3)
    v = vmin
    while v <= vmax + 1e-6:
        d.line([(x - 10, Y(v)), (x + 10, Y(v))], PAPER, 2); d.text((x - 95, Y(v) - 14), fmt.format(v), f(24, "reg"), GREY); v += step
    up = end > start; ca, cb = (CYAN, ORANGE) if up else (ORANGE, CYAN)
    d.ell((x - 14, Y(start) - 14, x + 14, Y(start) + 14), fill=ca); d.text((x + 34, Y(start) - 22), start_lab, f(32, "inter"), alpha(ca, seg(0.2, 0.4)))
    e = ease_io((_A.T - lead(hit, 1.0)) / 1.0); vv = start + (end - start) * e
    if e > 0:
        d.line([(x, Y(start)), (x, Y(vv))], cb, 10); d.ell((x - 16, Y(vv) - 16, x + 16, Y(vv) + 16), fill=cb)
        d.text((x + 34, Y(end) - 22), end_lab, f(32, "inter"), alpha(cb, seg(hit, 0.4)))
        if bracket and e >= 1:
            pencil(d, [(x - 40, Y(start)), (x - 60, Y(start)), (x - 60, Y(end)), (x - 40, Y(end))], hit + 0.3, 0.5, RED, 4, seed=7)
            fb = f(36, "inter"); d.text((x - 110 - d.tl(bracket, fb), (Y(start) + Y(end)) / 2 - 22), bracket, fb, alpha(RED, seg(hit + 0.6, 0.4)))
    if title: d.text((180, 60), title, fit(d, title, 34, 900), alpha(PAPER_HI, seg(0, 0.4)))
    tagline(im, tag); return im

def clocks2(items, tag="", title=""):
    """clocks side by side: items [(label, speed_before, speed_after_cue, colour)]"""
    im = base(); d = D(im); hit = c(0, 2.0); n = len(items); gw = W / n
    if title: center(d, 70, title, f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    for i, (lab, s0, s1, col) in enumerate(items):
        cx = gw * i + gw / 2; a = seg(0.2 + i * 0.3, 0.4); r = 150 if n <= 2 else 115
        spd = s0 + (s1 - s0) * seg(hit, 0.6)
        d.ell((cx - r, 330 - r, cx + r, 330 + r), outline=alpha(PAPER, a), width=5)
        for h in range(12):
            ang = h * math.pi / 6; d.line([(cx + (r - 18) * math.sin(ang), 330 - (r - 18) * math.cos(ang)), (cx + (r - 6) * math.sin(ang), 330 - (r - 6) * math.cos(ang))], alpha(PAPER, a), 3)
        ang = _A.T * spd * 2 * math.pi; d.line([(cx, 330), (cx + (r - 30) * math.sin(ang), 330 - (r - 30) * math.cos(ang))], col, 6)
        center(d, 330 + r + 40, lab, fit(d, lab, 32, gw - 40), alpha(col, a), cx=cx)
    tagline(im, tag); return im

def rocket_feather(mode="both", tag="", title=""):
    """a rocket line shooting up and a feather line drifting down slowly (rockets and feathers)"""
    im = base(); d = D(im); x0, x1, ym = 180, W - 120, 380
    if title: d.text((180, 60), title, fit(d, title, 34, 900), alpha(PAPER_HI, seg(0, 0.4)))
    d.line([(x0, ym + 220), (x1, ym + 220)], GREY, 2)
    if mode in ("both", "up"):
        k = ease_io((_A.T - 0.3) / 1.2); pts = [(x0 + 60 + i * 6, ym + 180 - (i * 6) ** 1.25 * 0.55) for i in range(int(60 * k) + 1)]
        pts = [q for q in pts if q[1] > 150]
        if len(pts) > 1: d.line(pts, ORANGE, 7)
        if pts: d.text((pts[-1][0] + 24, pts[-1][1] - 10), "▲ ROCKET · UP IN ≈ 4 WEEKS", f(28, "inter"), alpha(ORANGE, seg(0.5, 0.4)))
    if mode in ("both", "down"):
        t0 = 0.3 if mode == "down" else 1.6; k = ease_io((_A.T - t0) / 3.0); n = int(110 * k)
        pts = [(x0 + 480 + i * 5, ym - 120 + i * 2.6 + 18 * math.sin(i / 6.0)) for i in range(n + 1)]
        if len(pts) > 1: d.line(pts, CYAN, 5)
        if pts: d.text((pts[-1][0] - 420, pts[-1][1] + 34), "FEATHER · DOWN IN ≈ 8 WEEKS ▼", f(28, "inter"), alpha(CYAN, seg(t0 + 0.4, 0.4)))
    tagline(im, tag); return im

def sub_card(n, nxt):
    def fn(o, t):
        im = base(); d = D(im)
        center(d, 110, f"{n} OF 4 · THE IRAN WAR BILL", f(32, "inter"), alpha(ORANGE, seg(0, 0.4)))
        center(d, 190, "NEXT WEEK", f(40, "inter"), alpha(PAPER, seg(0.3, 0.4)))
        center(d, 250, nxt, fit(d, nxt, 54, 1080), alpha(PAPER_HI, seg(0.6, 0.4)))
        b = seg(lead(c(0, 3.0), 0.5), 0.4)
        d.rrect((W/2 - 190, 420, W/2 + 190, 510), 14, fill=alpha(CRIMSON, b)); center(d, 440, "SUBSCRIBE", f(44, "inter"), alpha(PAPER_HI, b))
        return im
    return fn

def signs(o, t):
    """two forecourt price signs; neither cuts until one does"""
    im = base(); d = D(im); hit = c(0, 3.0)
    for i, (x, name) in enumerate(((330, "STATION A"), (830, "STATION B"))):
        cut = i == 0 and _A.T > hit
        price = "157.9" if cut else "167.9"
        d.rect((x, 160, x + 260, 500), fill=(28, 28, 30), outline=PAPER, width=3); d.rect((x + 110, 500, x + 150, 620), fill=(60, 60, 64))
        center(d, 180, name, f(26, "inter"), PAPER, cx=x + 130); center(d, 240, "UNLEADED", f(24, "reg"), GREY, cx=x + 130)
        center(d, 290, price, f(72, "bebas"), ORANGE if not cut else GREEN, cx=x + 130)
        if i == 1 and _A.T > hit + 1.2: center(d, 420, "…WAITING", f(26, "inter"), alpha(RED, seg(hit + 1.2, 0.4)), cx=x + 130)
    center(d, 70, "WHO CUTS FIRST?", f(36, "inter"), alpha(PAPER_HI, seg(0, 0.4)))
    tagline(im, t); return im

def barrel_cut(o, t):
    """barrel cross-section: light products top, diesel middle (highlighted on cue), heavy bottom"""
    im = base(); d = D(im); hit = c(0, 2.0); x0, x1 = 480, 800
    layers = [("PETROL", (90, 120, 150), 170, 300), ("DIESEL", (200, 120, 40), 300, 450), ("HEAVY OILS", (70, 60, 50), 450, 580)]
    for i, (lab, col, ya, yb) in enumerate(layers):
        a = seg(0.2 + i * 0.25, 0.4); hl = lab == "DIESEL" and _A.T > hit
        d.rect((x0, ya, x1, yb), fill=alpha(col if not hl else ORANGE, a), outline=alpha(PAPER, a), width=3)
        center(d, (ya + yb) / 2 - 20, lab, f(34, "inter"), alpha(PAPER_HI, a), cx=(x0 + x1) / 2)
    if _A.T > hit: d.text((x1 + 30, 355), "← THE WORLD IS SHORT", f(30, "inter"), alpha(ORANGE, seg(hit, 0.4)))
    center(d, 90, "ONE BARREL, REFINED", f(34, "inter"), alpha(ORANGE, seg(0, 0.4)))
    tagline(im, t); return im

def uk_ni(o, t):
    return map_scene((-11.0, 49.6, 2.5, 59.2), z=5, hi=("United Kingdom",), pins=[(-6.5, 54.6, "NORTHERN IRELAND · 159.2p", GREEN, 0), (-1.5, 52.6, "UK AVERAGE ≈ 165p", ORANGE, None)],
                     title="PETROL, 17 NOV 2026 · RAC", tag=t)
