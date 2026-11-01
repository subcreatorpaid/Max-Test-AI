#!/usr/bin/env python3
"""Voiceover with Kokoro (free). Usage: python scripts/tts.py videos/<slug>/narration.txt videos/<slug>/audio/
narration.txt: one paragraph per beat, separated by a blank line. Lines starting with # are ignored.
Writes beat_001.wav ... and timing.json [{beat, file, seconds, text}]."""
import json, pathlib, sys, urllib.request
import soundfile as sf
from kokoro_onnx import Kokoro

VOICE, SPEED, LANG = "am_michael", 1.0, "en-us"   # locked in brain/host.md
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
CACHE = pathlib.Path.home() / ".cache/kokoro"

def model():
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, remote in [("kokoro.onnx", "kokoro-v1.0.int8.onnx"), ("voices.bin", "voices-v1.0.bin")]:
        if not (CACHE / name).exists():
            urllib.request.urlretrieve(MODEL_URL + remote, CACHE / name)
    return Kokoro(str(CACHE / "kokoro.onnx"), str(CACHE / "voices.bin"))

def main(src, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    text = "\n".join(l for l in pathlib.Path(src).read_text().splitlines() if not l.startswith("#"))
    beats = [b.strip().replace("\n", " ") for b in text.split("\n\n") if b.strip()]
    k, timing = model(), []
    for i, b in enumerate(beats, 1):
        samples, sr = k.create(b, voice=VOICE, speed=SPEED, lang=LANG)
        f = out / f"beat_{i:03d}.wav"
        sf.write(f, samples, sr)
        timing.append({"beat": i, "file": f.name, "seconds": round(len(samples) / sr, 3), "text": b})
        print(f"beat {i}: {timing[-1]['seconds']}s")
    (out / "timing.json").write_text(json.dumps(timing, indent=1))
    print(f"total {sum(t['seconds'] for t in timing):.1f}s")

if __name__ == "__main__":
    main(*sys.argv[1:3])
