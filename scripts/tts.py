#!/usr/bin/env python3
"""Placeholder voiceover with Kokoro (free) so previews have sound before Hammad's real narration exists.
Usage: python scripts/tts.py videos/<slug>/voiceover.md videos/<slug>/audio/
Reads voiceover.md (one sentence per line, '---' = chapter break with 1 s pause; headings and [RESULT] lines skipped)
and writes audio/voiceover-placeholder.wav + audio/voiceover-placeholder.json (start/end of every line, for edit.json).
Hammad's real file is audio/voiceover.mp3 and always wins."""
import json, pathlib, sys, urllib.request
import soundfile as sf
from kokoro_onnx import Kokoro

VOICE, SPEED, LANG = "am_michael", 1.0, "en-us"   # FALLBACK ONLY: Max's real voice is one Google voice (Vids), see brain/host.md
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
    import json as _j, numpy as np
    k, sr0, chunks, marks, t = None, 24000, [], [], 0.0
    for line in pathlib.Path(src).read_text().splitlines():
        line = line.strip()
        if line == "---":
            chunks.append(np.zeros(sr0)); t += 1.0; continue
        if not line or line.startswith(("#", "**", "Make this")) or "[RESULT" in line:
            continue
        k = k or model()
        samples, sr0 = k.create(line, voice=VOICE, speed=SPEED, lang=LANG)
        marks.append({"text": line, "start": round(t, 2), "end": round(t + len(samples) / sr0, 2)})
        chunks += [samples, np.zeros(int(sr0 * 0.3))]; t += len(samples) / sr0 + 0.3
    sf.write(out / "voiceover-placeholder.wav", np.concatenate(chunks), sr0)
    (out / "voiceover-placeholder.json").write_text(_j.dumps(marks, indent=1))
    print(f"{len(marks)} lines, {t:.1f}s")

if __name__ == "__main__":
    main(*sys.argv[1:3])
