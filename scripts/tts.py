#!/usr/bin/env python3
"""Max's voiceover. Usage: python scripts/tts.py videos/<slug>/narration.txt videos/<slug>/audio/
narration.txt: one paragraph per beat, separated by a blank line. Lines starting with # are ignored.
Writes beat_001.wav ... and timing.json [{beat, file, seconds, text}].

Voice (locked in brain/host.md): Max uses ONE Google (Gemini) voice everywhere, the same one his
Google Vids avatar uses. With GEMINI_API_KEY set (GitHub Secret) this script uses Gemini TTS with
MAX_VOICE. Without a key it falls back to Kokoro am_michael, for timing previews only (not final)."""
import base64, json, os, pathlib, sys, urllib.request

MAX_VOICE = "TBD"   # Gemini voice name chosen in Google Vids; set in brain/host.md, then here
GEMINI_MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
STYLE = "Read in a calm, warm, slightly witty American voice, like a friendly tech explainer: "
KOKORO_VOICE, SPEED, LANG = "am_michael", 1.0, "en-us"
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
CACHE = pathlib.Path.home() / ".cache/kokoro"

def gemini(text, key, voice):
    """Returns (int16 numpy samples, 24000)."""
    import numpy as np
    body = {"contents": [{"parts": [{"text": STYLE + text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
    return np.frombuffer(base64.b64decode(data), dtype="<i2"), 24000   # 16-bit PCM, mono, 24 kHz

def kokoro():
    from kokoro_onnx import Kokoro
    CACHE.mkdir(parents=True, exist_ok=True)
    for name, remote in [("kokoro.onnx", "kokoro-v1.0.int8.onnx"), ("voices.bin", "voices-v1.0.bin")]:
        if not (CACHE / name).exists():
            urllib.request.urlretrieve(MODEL_URL + remote, CACHE / name)
    k = Kokoro(str(CACHE / "kokoro.onnx"), str(CACHE / "voices.bin"))
    return lambda t: k.create(t, voice=KOKORO_VOICE, speed=SPEED, lang=LANG)

def main(src, out):
    import soundfile as sf
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    text = "\n".join(l for l in pathlib.Path(src).read_text().splitlines() if not l.startswith("#"))
    beats = [b.strip().replace("\n", " ") for b in text.split("\n\n") if b.strip()]
    key, voice = os.environ.get("GEMINI_API_KEY"), os.environ.get("MAX_VOICE", MAX_VOICE)
    if key and voice != "TBD":
        speak = lambda t: gemini(t, key, voice); print(f"voice: Gemini {voice}")
    else:
        speak = kokoro(); print("voice: Kokoro am_michael (PREVIEW ONLY, not Max's final voice)")
    timing = []
    for i, b in enumerate(beats, 1):
        samples, sr = speak(b)
        f = out / f"beat_{i:03d}.wav"
        sf.write(f, samples, sr)
        timing.append({"beat": i, "file": f.name, "seconds": round(len(samples) / sr, 3), "text": b})
        print(f"beat {i}: {timing[-1]['seconds']}s")
    (out / "timing.json").write_text(json.dumps(timing, indent=1))
    print(f"total {sum(t['seconds'] for t in timing):.1f}s")

if __name__ == "__main__":
    main(*sys.argv[1:3])
