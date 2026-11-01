#!/usr/bin/env python3
"""Max's narration from voiceover.md. Usage: python scripts/tts.py videos/<slug>/voiceover.md videos/<slug>/audio/
voiceover.md: one sentence per line, '---' = chapter break (1 s pause); headings, '**' lines and [RESULT] lines are skipped.
Writes audio/voiceover-generated.wav + voiceover-generated.json (start/end of every line, for edit.json vo_start/vo_end).
Hammad's own recording, audio/voiceover.mp3, always wins over this file.

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
    import numpy as np, soundfile as sf
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    key, voice = os.environ.get("GEMINI_API_KEY"), os.environ.get("MAX_VOICE", MAX_VOICE)
    if key and voice != "TBD":
        speak = lambda t: gemini(t, key, voice); print(f"voice: Gemini {voice}")
    else:
        speak = None; print("voice: Kokoro am_michael (PREVIEW ONLY, not Max's final voice)")
    chunks, marks, t, sr = [], [], 0.0, 24000
    for line in pathlib.Path(src).read_text().splitlines():
        line = line.strip()
        if line == "---":
            chunks.append(np.zeros(sr, dtype=np.float32)); t += 1.0; continue
        if not line or line.startswith(("#", "**", "Make this")) or "[RESULT" in line:
            continue
        speak = speak or kokoro()
        samples, sr = speak(line)
        samples = np.asarray(samples, dtype=np.float32) / (32768.0 if np.asarray(samples).dtype == np.int16 else 1.0)
        marks.append({"text": line, "start": round(t, 2), "end": round(t + len(samples) / sr, 2)})
        chunks += [samples, np.zeros(int(sr * 0.3), dtype=np.float32)]; t += len(samples) / sr + 0.3
    sf.write(out / "voiceover-generated.wav", np.concatenate(chunks), sr)
    (out / "voiceover-generated.json").write_text(json.dumps(marks, indent=1))
    print(f"{len(marks)} lines, {t:.1f}s")

if __name__ == "__main__":
    main(*sys.argv[1:3])
