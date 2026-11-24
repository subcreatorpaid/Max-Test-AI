# INV-017 sound: VO + in-house music bed + kit/library SFX placed ON the cue words, -15 LUFS integrated, true-peak safe.
# usage: python3 mix11.py <parts_dir> <sfx_dir> <out.wav>
# parts_dir holds <PART>.wav (voice) and <PART>-shots.json (from render17.py). sfx_dir = kit sound-fx + library sfx,
# staged to /tmp only (licence: never commit or share kit files).
import sys, json, glob, os, numpy as np, soundfile as sf, pyloudnorm as pyln
from numpy.fft import rfft, irfft
PD, SFXD, OUT = sys.argv[1:4]; SR = 48000
ORDER = os.environ.get("ORDER", "CO,P1,BR,P2,P3,P4,P5,P6,P7,RC").split(",")
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
    x = load(f"{VOD}/INV-017-{p}.wav"); a = int(offs[p] * SR); vo[a:a + len(x)] += x[:N - a]

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
music = pyln.normalize.loudness(music.astype("float64"), meter.integrated_loudness(music.astype("float64")), -31.0).astype(np.float32)

# ---------- SFX on the words ----------
ALIAS = {"hit-thud-low": "land_stone_01", "printer-dot-matrix-1s2": "ratchet_zip_02", "drone-bed-30s": "wind_whistle_01", "pen-scratch": "land_card_01", "typing-keys-3s": "type_01", "paper-rustle-short": "swipe_paper_01"}
def find(name):
    g = glob.glob(f"{SFXD}/**/{name}.wav", recursive=True) or glob.glob(f"{SFXD}/**/{ALIAS.get(name, name)}.wav", recursive=True)
    return g[0]
S = {k: load(find(k)) for k in ["reverse_cymbal_01", "sub_drop_01", "sub_drop_808_01", "land_card_01", "land_soft_01", "whoosh_deep_01",
     "whoosh_deep_02", "tick_fine_01", "counter_roll_01", "chart_grow_02", "riser_air_01", "fire_flare_01", "swipe_paper_01",
     "printer-dot-matrix-1s2", "hit-thud-low", "pen-scratch", "paper-rustle-short", "typing-keys-3s", "drone-bed-30s", "powerdown_machine_01"]}
fx = np.zeros(N, np.float32); placed = []
def put(name, t, g, end_at=False, maxlen=None, fade=0.3):
    x = S[name] * g
    if maxlen: x = x[:int(maxlen * SR)].copy(); fl = min(len(x), int(fade * SR)); x[-fl:] *= np.linspace(1, 0, fl)
    a = int((t - (len(x) / SR if end_at else 0)) * SR)
    if a < 0: x = x[-a:]; a = 0
    if a >= N: return
    fx[a:a + len(x)] += x[:N - a]; placed.append((round(t, 2), name))
last = -99.0
for s in shots:
    T = s["T"]; sfxd = (s.get("sfx") or "").lower(); cue0 = T + (s["cues"][0] if s["cues"] else 0.6)
    if is_card(s):
        put("reverse_cymbal_01", T + 0.05, 0.10, end_at=True); put("sub_drop_01", T + 0.05, 0.22); last = T; continue
    if s["kind"] != "gfx":
        continue
    if T - last < 5.0 and not ("sub hit" in sfxd or "boom" in sfxd): continue
    hit = False
    if "boom" in sfxd or "sub hit" in sfxd: put("sub_drop_808_01", cue0 - 0.05, 0.13); hit = True
    if "stamp" in sfxd or "thud" in sfxd: put("hit-thud-low", cue0 + 0.1, 0.30); hit = True
    if "counter" in sfxd or "ticker" in sfxd or "count" in sfxd: put("counter_roll_01", max(T, cue0 - 1.2), 0.05); put("land_card_01", cue0 + 0.05, 0.09); hit = True
    if "receipt" in sfxd or "printer" in sfxd: put("printer-dot-matrix-1s2", T + 0.5, 0.14); hit = True
    if "swarm" in sfxd or "hiss" in sfxd or "drone" in sfxd: put("drone-bed-30s", T, 0.10, maxlen=min(8.0, s["dur"]), fade=1.5); hit = True
    if "flame" in sfxd or "fire" in sfxd or "flare" in sfxd: put("fire_flare_01", cue0, 0.10); hit = True
    if "pen" in sfxd: put("pen-scratch", cue0, 0.20); hit = True
    if "typ" in sfxd: put("typing-keys-3s", T + 0.3, 0.10, maxlen=2.5); hit = True
    if "paper" in sfxd or "unfold" in sfxd or "card" in sfxd: put("swipe_paper_01", T + 0.1, 0.08); hit = True
    if "riser" in sfxd: put("riser_air_01", cue0, 0.07, end_at=True); hit = True
    if "power" in sfxd or "lights out" in sfxd: put("powerdown_machine_01", cue0, 0.10); hit = True
    if not hit and ("whoosh" in sfxd or "map" in sfxd): put("whoosh_deep_01" if len(placed) % 2 else "whoosh_deep_02", T, 0.06); hit = True
    if not hit and ("tick" in sfxd or "gauge" in sfxd or "bar" in sfxd or "chart" in sfxd): put("chart_grow_02", T + 0.3, 0.05); put("tick_fine_01", cue0, 0.06); hit = True
    if not hit and s["cues"]: put("land_soft_01", cue0, 0.07); hit = True
    if hit: last = T

mix = vo + music + fx
L = meter.integrated_loudness(mix.astype("float64")); mix = pyln.normalize.loudness(mix.astype("float64"), L, -13.9)  # tanh limiter below costs ~1.1 LU -> ~-15 LUFS
mix = np.tanh(mix / 0.95) * 0.95 * 0.94
mix = mix[:int(TOTAL * SR)].astype(np.float32)
sf.write(OUT, mix, SR)
json.dump(placed, open(OUT + ".sfx.json", "w"))
print("mix", round(TOTAL, 1), "s; LUFS", round(meter.integrated_loudness(mix.astype("float64")), 1), "; sfx placed", len(placed))
