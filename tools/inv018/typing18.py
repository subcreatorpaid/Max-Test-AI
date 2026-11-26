# INV-018 typing engine (Hammad, 26 Nov 2026: "use the typing animation and sound for each").
# Patches anim12 so EVERY caption in a graphic types on letter by letter from the moment it first appears,
# and logs each typing run (start, duration, characters) so the mixer can put a key sound under it.
# Skipped on purpose: tiny labels (< 20 px logical), big counting numbers (>= 100 px with digits, they count up instead),
# the giant faded part-card digit, and text already drawn by anim12.typewriter (logged, not double-typed).
import re
import anim12 as A

CPS = 34                    # characters per second (a brisk typewriter)
MAXDUR = 1.1                # a long caption speeds up so it is always typed within 1.1 s
STATE = {}                  # key -> first time the text was visible in this shot
EVENTS = []                 # [t0, dur, nchars] for this shot (shot-relative seconds)
_NOTYPE = [False]
_orig_text = A.D.text
_orig_tw = A.typewriter

def reset():
    STATE.clear(); EVENTS.clear()

def _key(t, font):
    return (re.sub(r"\d[\d,\.]*", "#", t), getattr(font, "lsize", 0))

def _log(t0, n, cps):
    EVENTS.append([round(t0, 3), round(max(0.12, n / cps), 3), n])

def _text(self, xy, t, font, fill, anchor=None):
    a = fill[3] if len(fill) > 3 else 255
    sz = getattr(font, "lsize", 40)
    if _NOTYPE[0] or a <= 0 or not t or not t.strip() or sz < 20 or sz >= 200 or (sz >= 100 and re.search(r"\d", t)):
        return _orig_text(self, xy, t, font, fill, anchor)
    k = _key(t, font)
    if k not in STATE:
        cps = max(CPS, len(t) / MAXDUR); STATE[k] = (A.T, cps); _log(A.T, len(t), cps)
    t0, cps = STATE[k]
    n = int((A.T - t0) * cps) + 1
    if n >= len(t): return _orig_text(self, xy, t, font, fill, anchor)
    s = t[:n]
    _orig_text(self, xy, s, font, fill, anchor)
    if int(A.T * 6) % 2 == 0 and anchor is None:   # blinking block cursor while typing
        x = xy[0] + self.tl(s, font) + 3
        self.rect((x, xy[1] + sz * 0.18, x + max(4, sz * 0.12), xy[1] + sz * 0.95), fill=tuple(fill[:3]) + (min(255, a),))

def _typewriter(d, xy, text, font, fill, t0, cps=28):
    k = ("TW", text, getattr(font, "lsize", 0))
    if k not in STATE and A.T >= t0:
        STATE[k] = t0; _log(t0, len(text), cps)
    _NOTYPE[0] = True
    try: _orig_tw(d, xy, text, font, fill, t0, cps)
    finally: _NOTYPE[0] = False

def install():
    A.D.text = _text
    A.typewriter = _typewriter

class notype:
    """with typing18.notype(): ...  draws text instantly (corner invoice, overlays drawn by hand)"""
    def __enter__(self): self.p = _NOTYPE[0]; _NOTYPE[0] = True
    def __exit__(self, *a): _NOTYPE[0] = self.p
