# INV-019 sound (copy of mix17b + a key / typing sound under EVERY caption that types on, from the render's typing events): VO + in-house music bed + kit/library SFX placed ON the cue words, -15 LUFS integrated, true-peak safe.
# usage: python3 mix11.py <parts_dir> <sfx_dir> <out.wav>
# parts_dir holds <PART>.wav (voice) and <PART>-shots.json (from render17.py). sfx_dir = kit sound-fx + library sfx,
# staged to /tmp only (licence: never commit or share kit files).
import sys, json, glob, os, numpy as np, soundfile as sf, pyloudnorm as pyln
from numpy.fft import rfft, irfft
PD, SFXD, OUT = sys.argv[1:4]; SR = 48000
ORDER = os.environ.get("ORDER", "CO,P1,BR,P2,P3,P4,P5,P6,RC").split(",")
VOD = os.environ.get("VOD", PD)

def load(p):
    x, sr = sf.read(p, dtype="float32", always_2d=True); x = x.mean(1)
    if sr != SR:
        n = int(len(x) * SR / sr); x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)
    return x

offs = {}; t = 0.0; shots = []
for p in ORDER:
    offs[p] = t; js = json.load(open(f"{PD}/{p}-shots.json"))
    for s in js["shots"]: shots.append(dict(s, T=t + s["t"], part=p))
    t += js["dur"]
TOTAL = t; N = int(TOTAL * SR) + SR
vo = np.zeros(N, np.float32)
for p in ORDER:
    x = load(f"{VOD}/INV-019-{p}.wav"); a = int(offs[p] * SR); vo[a:a + len(x)] += x[:N - a]

# ---------- music bed: slow, dark, cold (A minor: Am F C Em), pads + low pulse + sparse felt piano ----------
rng = np.random.default_rng(11)
def note(m): return 440.0 * 2 ** ((m - 69) / 12)
CH = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [52, 55, 59]]
CL = 9.0; nchord = int(TOTAL / CL) + 2; music = np.zeros(N, np.float32)
for k in range(nchord):
    a = int(k * CL * SR); L = min(int(CL * SR * 1.35), N - a)
    if L <= 0: break
    ts = np.arange(L) / SR; env = np.minimum(1, ts / 3.0) * np.exp(-np.maximum(0, ts - CL) / 1.3)
    ch = CH[k % 4]; sig = np.zeros(L, np.float32)
    for m in ch:
        for det in (-0.10, 0.0, 0.09):
            f = note(m - 12 + det); sig += np.sin(2 * np.pi * f * ts + rng.random() * 6) * 0.09 + 0.025 * np.sin(4 * np.pi * f * ts)
    sig += 0.24 * np.sin(2 * np.pi * note(ch[0] - 24) * ts) * (0.75 + 0.25 * np.sin(2 * np.pi * ts / 1.5))  # low pulse
    music[a:a + L] += (sig * env).astype(np.float32)
mot = [69, 72, 71, 64]
for k in range(0, nchord, 3):
    for j, m in enumerate(mot):
        a = int((k * CL + j * 1.8 + 0.6) * SR); L = min(int(3.5 * SR), N - a)
        if L <= 0: continue
        ts = np.arange(L) / SR; f = note(m)
        s = (np.sin(2 * np.pi * f * ts) + 0.35 * np.sin(4 * np.pi * f * ts) + 0.1 * np.sin(6 * np.pi * f * ts)) * np.exp(-ts * 1.7) * np.minimum(1, ts / 0.01)
        music[a:a + L] += 0.15 * s.astype(np.float32)
ir_len = int(2.4 * SR); ir = (rng.standard_normal(ir_len) * np.exp(-np.arange(ir_len) / (0.6 * SR))).astype(np.float32); ir /= np.sqrt((ir ** 2).sum())
nfft = 1 << int(np.ceil(np.log2(ir_len + SR * 20))); IR = rfft(ir, nfft); wet = np.zeros(N + ir_len, np.float32); B = nfft - ir_len
for i in range(0, N, B):
    blk = music[i:i + B]; y = irfft(rfft(blk, nfft) * IR, nfft)[:len(blk) + ir_len]; wet[i:i + len(y)] += y[:len(wet) - i]
music = 0.5 * music + 0.5 * wet[:N]
def is_card(s): return s["code"].endswith("-01") and s["code"][0] in "PW" and s["kind"] == "gfx"
gain = np.ones(N, np.float32)
for s in shots:   # music drops out under each PART card, swells back
    if is_card(s):
        a = int((s["T"] - 0.9) * SR); b = int((s["T"] + 1.8) * SR); c = int((s["T"] + 4.5) * SR)
        gain[max(0, a):b] = 0.0; gain[b:c] = np.linspace(0, 1, max(0, c - b))[:len(gain[b:c])]
end = int((TOTAL - 6) * SR); gain[end:] *= np.linspace(1, 0, N - end)
gain = np.convolve(gain, np.ones(2400) / 2400, mode="same").astype(np.float32); music *= gain
envv = np.sqrt(np.convolve(vo ** 2, np.ones(SR // 5) / (SR // 5), mode="same")); music *= (1 - 0.35 * np.clip(envv / 0.05, 0, 1)).astype(np.float32)
meter = pyln.Meter(SR)
music = pyln.normalize.loudness(music.astype("float64"), meter.integrated_loudness(music.astype("float64")), -29.5).astype(np.float32)

# ---------- SFX v2 (25 Nov, Hammad: "no sound effects"): every transition, every reveal, every cue; clearly audible ----------
SEGS = json.load(open(os.path.join(VOD, "segs19.json")))["segs"]
ALIAS = {"hit-thud-low": "land_stone_01", "printer-dot-matrix-1s2": "ratchet_zip_02", "drone-bed-30s": "wind_whistle_01", "pen-scratch": "land_card_01", "typing-keys-3s": "type_01"}
_cache = {}
def snd(name):
    if name not in _cache:
        g = glob.glob(f"{SFXD}/**/{name}.wav", recursive=True) or glob.glob(f"{SFXD}/**/{ALIAS.get(name, name)}.wav", recursive=True)
        x = load(g[0]); x = x / (np.abs(x).max() + 1e-9)          # peak-normalise every sound, so gains mean the same thing
        _cache[name] = x.astype(np.float32)
    return _cache[name]
fx = np.zeros(N, np.float32); placed = []; busy = []
def put(name, t, g, end_at=False, maxlen=None, fade=0.3, force=False, gap=0.9):
    if not force and any(abs(t - u) < gap for u in busy): return False
    x = snd(name) * g
    if maxlen: x = x[:int(maxlen * SR)].copy(); fl = min(len(x), int(fade * SR)); x[-fl:] *= np.linspace(1, 0, fl)
    a = int((t - (len(x) / SR if end_at else 0)) * SR)
    if a < 0: x = x[-a:]; a = 0
    if a >= N: return False
    fx[a:a + len(x)] += x[:N - a]; placed.append((round(t, 2), name)); busy.append(t); return True
WH = ["whoosh_01", "whoosh_02", "whoosh_03", "whoosh_clean_01", "swipe_01", "swipe_air_01", "whip_air_01", "glide_01"]
POP = ["pop_soft_01", "tap_wood_01", "click_felt_01", "pop_soft_02", "tap_soft_02", "tick_wood_01", "pop_04", "land_card_02"]
dips = []
for i, s in enumerate(shots):
    T = s["T"]; sfxd = (s.get("sfx") or "").lower(); cue0 = T + (s["cues"][0] if s["cues"] else 0.6)
    if is_card(s):
        put("reverse_cymbal_01", T + 0.05, 0.45, end_at=True, force=True); put("sub_drop_01", T + 0.05, 0.5, force=True)
        put("whoosh_deep_metal_01", T + 0.9, 0.35, force=True); continue
    # 1) transition into every shot
    if s["kind"] == "gfx":
        put(WH[i % len(WH)], T - 0.15, 0.30, force=True)
    else:
        put("whoosh_deep_01" if i % 2 else "whoosh_deep_02", T - 0.2, 0.30, force=True)
    # 2) a soft pop on every sentence start inside a graphic (the graphics build on the sentences)
    if s["kind"] == "gfx":
        sg = SEGS.get(s["part"], {}).get("sents", {}).get(s["code"].rstrip("x"), [])
        p0 = shots and SEGS[s["part"]]["starts"]
        st = dict((c, v) for c, v in SEGS[s["part"]]["starts"]).get(s["code"].rstrip("x"))
        if st is not None:
            for j, (a0, a1) in enumerate(sg[1:], 1):
                tt = T + (a0 - st) + 0.05
                if T + 0.8 < tt < T + s["dur"] - 0.4: put(POP[(i + j) % len(POP)], tt, 0.26)
    # 3) the cue word: the hit named in the script
    if "boom" in sfxd or "sub hit" in sfxd or "explosion" in sfxd:
        put("sub_drop_808_01", cue0 - 0.05, 0.55, force=True); put("reverse_02", cue0 - 0.02, 0.35, end_at=True, force=True); dips.append(cue0)
    if "stamp" in sfxd or "thud" in sfxd: put("land_stone_01", cue0 + 0.1, 0.65, force=True); put("bip_bass_01", cue0 + 0.12, 0.35, force=True)
    if "counter" in sfxd or "ticker" in sfxd or "count" in sfxd: put("counter_roll_01", max(T + 0.3, cue0 - 1.2), 0.30, force=True); put("land_card_01", cue0 + 0.05, 0.45, force=True)
    if "receipt" in sfxd or "printer" in sfxd: put("ratchet_zip_02", T + 0.5, 0.35, force=True); put("data_stream_01", T + 0.9, 0.12, maxlen=2.0, force=True)
    if "register" in sfxd or "ding" in sfxd: put("cash_01", cue0, 0.4, force=True)
    if "drone" in sfxd or "hum" in sfxd or "waves" in sfxd: put("wind_whistle_01", T, 0.22, maxlen=min(8.0, s["dur"]), fade=1.5, force=True)
    if "flame" in sfxd or "fire" in sfxd or "flare" in sfxd or "crackle" in sfxd: put("fire_flare_01", cue0, 0.4, force=True)
    if "flash" in sfxd or "zap" in sfxd or "electric" in sfxd: put("glitch_bitcrush_01", cue0, 0.30, force=True)
    if "warning" in sfxd or "alarm" in sfxd: put("error_blip_01", cue0, 0.30, force=True)
    if "pen" in sfxd or "pencil" in sfxd: put("land_card_01", cue0, 0.4, force=True)
    if "paper" in sfxd or "card" in sfxd: put("swipe_paper_01", T + 0.1, 0.40, force=True)
    if "riser" in sfxd or "rising" in sfxd: put("riser_tonal_01", cue0, 0.30, end_at=True, force=True)
    if "power" in sfxd or "lights out" in sfxd: put("powerdown_screen_01", cue0, 0.35, force=True)
    if "shimmer" in sfxd: put("shimmer_glint_02", cue0, 0.35, force=True)
    if "chart" in sfxd or "bar" in sfxd or "gauge" in sfxd: put("chart_grow_02", T + 0.3, 0.30, force=True)
    if "tick" in sfxd or "clock" in sfxd: put("tick_fine_01", cue0, 0.35, force=True)
    if "map" in sfxd: put("scan_01", T + 0.4, 0.14, maxlen=2.0, force=True)
    if "chain" in sfxd: put("connect_magnet_01", cue0, 0.35, force=True)
    put("land_soft_02", cue0, 0.40)   # every cue word lands, unless something already sits there

# ---------- typing (Hammad 26 Nov: "use the typing animation and sound for each"): one key run per caption as it types ----------
TYPS = ["type_01", "type_02", "type_soft_keys_01"]; TAPS = ["tap_key_01", "tap_key_02", "tap_key_03"]
TGAIN = float(os.environ.get("TYPGAIN", "0.34")); covered = []; ntyp = 0
for i, s in enumerate(shots):
    if is_card(s): continue
    for (t0, dur, nch) in s.get("typing", []):
        a = s["T"] + t0; b = a + dur
        if a > s["T"] + s["dur"] - 0.1: continue
        for (ca, cb) in covered:            # overlapping captions share one run of keys
            if ca <= a < cb: a = cb
        if b - a < 0.06: continue
        if b - a < 0.3: x = snd(TAPS[ntyp % 3]) * TGAIN * 0.9
        else:
            src = snd(TYPS[ntyp % 3]); off = int((ntyp * 0.137 % 0.3) * SR); src = src[off:]
            reps = int(np.ceil((b - a) * SR / max(1, len(src)))) + 1; x = np.tile(src, reps)[:int((b - a) * SR)].copy() * TGAIN
            fl = min(len(x), int(0.06 * SR)); x[-fl:] *= np.linspace(1, 0, fl)
        st = int(a * SR)
        if st < N: fx[st:st + len(x)] += x[:N - st]; ntyp += 1; placed.append((round(a, 2), "typing")); covered.append((a, b))
print("typing runs", ntyp)
# a breath of silence in the music under the big blasts
for c in dips:
    a = int((c - 0.3) * SR); b = int((c + 1.6) * SR); m = min(N, b + SR)
    music[a:b] *= 0.15; music[b:m] *= np.linspace(0.15, 1, m - b)
# keep the effects under the voice: duck fx 4 dB while words are spoken
fx *= float(os.environ.get("FXGAIN", "2.0")) * (1 - 0.37 * np.clip(envv / 0.05, 0, 1)).astype(np.float32)
if os.environ.get("STEMS"): sf.write(OUT + ".vo.wav", vo, SR); sf.write(OUT + ".fx.wav", fx, SR); sf.write(OUT + ".mu.wav", music, SR)
mix = vo + music + fx
L = meter.integrated_loudness(mix.astype("float64")); mix = pyln.normalize.loudness(mix.astype("float64"), L, -13.9)  # tanh limiter below costs ~1.1 LU -> ~-15 LUFS
mix = np.tanh(mix / 0.95) * 0.95 * 0.94
mix = mix[:int(TOTAL * SR)].astype(np.float32)
sf.write(OUT, mix, SR)
json.dump(placed, open(OUT + ".sfx.json", "w"))
print("mix", round(TOTAL, 1), "s; LUFS", round(meter.integrated_loudness(mix.astype("float64")), 1), "; sfx placed", len(placed))
