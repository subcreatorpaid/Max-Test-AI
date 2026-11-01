#!/usr/bin/env python3
"""Render a Max Tests AI video from videos/<slug>/spec.json.

    python scripts/render.py videos/<slug> --preview     # 854x480, fast, for gate 2
    python scripts/render.py videos/<slug> --final       # 1920x1080, -14 LUFS, .srt (+ faster-whisper if installed)

Needs: ffmpeg, Pillow. Voiceover from scripts/tts.py (videos/<slug>/audio/timing.json).
spec.json:
{
  "music": "assets/music/track.mp3" | null,
  "scenes": [
    {"beat": 1, "type": "host",   "src": "footage/max-01.mp4", "start": 0},
    {"beat": 2, "type": "screen", "src": "footage/R1.mp4", "start": 3.5, "zoom": [0.8, 0.2, 1.5]},
    {"beat": 3, "type": "card",   "title": "Step 1", "text": "Export the timeline as XML"}
  ]
}
Scenes that share a beat split its voice time equally. Paths are relative to the video folder.
A missing src renders a grey placeholder naming the clip, so previews work before footage exists.
"""
import argparse, json, pathlib, shutil, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

BRAND = {"bg": "#FFFFFF", "soft": "#E9EDF3", "ink": "#141A26", "accent": "#2F6BFF", "hi": "#FFD23F", "muted": "#5B6578"}
FONT_DIRS = [pathlib.Path(__file__).resolve().parent.parent / "assets/brand", pathlib.Path("/usr/share/fonts")]
FPS = 30


def font(size, bold=True):
    names = ["Inter-Bold.ttf", "Inter-SemiBold.ttf", "DejaVuSans-Bold.ttf"] if bold else ["Inter-Medium.ttf", "Inter-Regular.ttf", "DejaVuSans.ttf"]
    for d in FONT_DIRS:
        for n in names:
            hits = list(d.rglob(n)) if d.exists() else []
            if hits:
                return ImageFont.truetype(str(hits[0]), size)
    return ImageFont.load_default()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed: {' '.join(cmd[:6])}...\n{r.stderr[-1500:]}")


def card_png(path, W, H, title, text, placeholder=False):
    s = W / 1920
    img = Image.new("RGB", (W, H), BRAND["soft"] if placeholder else BRAND["bg"])
    d = ImageDraw.Draw(img)
    if placeholder:
        d.text((int(80 * s), int(80 * s)), "PLACEHOLDER", font=font(int(40 * s)), fill=BRAND["muted"])
        d.text((int(80 * s), int(150 * s)), title, font=font(int(72 * s)), fill=BRAND["ink"])
        y = int(260 * s)
        for line in textwrap.wrap(text, 48):
            d.text((int(80 * s), y), line, font=font(int(44 * s), False), fill=BRAND["muted"]); y += int(60 * s)
    else:
        d.rounded_rectangle([int(160 * s), int(300 * s), W - int(160 * s), H - int(300 * s)], radius=int(16 * s), fill=BRAND["bg"], outline=BRAND["soft"], width=max(1, int(3 * s)))
        d.rectangle([int(160 * s), int(300 * s), int(176 * s), H - int(300 * s)], fill=BRAND["accent"])
        tf = font(int(84 * s))
        d.text((int(240 * s), int(370 * s)), title, font=tf, fill=BRAND["accent"])
        y = int(500 * s)
        for line in textwrap.wrap(text, 34):
            d.text((int(240 * s), y), line, font=font(int(64 * s)), fill=BRAND["ink"]); y += int(84 * s)
    img.save(path)


def segment(scene, dur, vdir, out, W, H):
    src = vdir / scene["src"] if scene.get("src") else None
    fit = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps={FPS}"
    if scene["type"] in ("host", "screen", "graphic") and src and src.exists():
        vf = fit
        if scene.get("zoom"):
            cx, cy, z = scene["zoom"]
            Z = f"if(lt(t\\,0.4)\\,1+({z}-1)*t/0.4\\,{z})"
            vf += f",scale=w='{W}*{Z}':h='{H}*{Z}':eval=frame,crop={W}:{H}:'(iw-{W})*{cx}':'(ih-{H})*{cy}'"
        # loop short clips so a long beat never runs out of footage
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", str(scene.get("start", 0)), "-i", str(src), "-t", f"{dur:.3f}",
             "-vf", vf, "-an", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", str(out)])
        return
    png = out.with_suffix(".png")
    if scene["type"] == "card":
        card_png(png, W, H, scene.get("title", ""), scene.get("text", ""))
    else:
        card_png(png, W, H, f"{scene['type'].upper()}: {scene.get('src', '?')}", scene.get("note", "Footage not added yet."), placeholder=True)
    run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-t", f"{dur:.3f}",
         "-vf", f"scale={W*2}:{H*2},zoompan=z='min(1+0.0008*on,1.04)':d=1:s={W}x{H}:fps={FPS},setsar=1",
         "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", str(out)])


def ts(t, srt=True):
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",") if srt else f"{h:d}:{m:02d}:{s:05.2f}"


def captions(timing, gap, whisper_wav=None):
    """[(start, end, text)] in chunks of ~5 words. Uses faster-whisper word times when available."""
    chunks = []
    if whisper_wav:
        try:
            from faster_whisper import WhisperModel
            segs, _ = WhisperModel("small.en", compute_type="int8").transcribe(str(whisper_wav), word_timestamps=True)
            words = [w for sg in segs for w in sg.words]
            for i in range(0, len(words), 5):
                grp = words[i:i + 5]
                chunks.append((grp[0].start, grp[-1].end, "".join(w.word for w in grp).strip()))
            return chunks
        except ImportError:
            print("faster-whisper not installed: using script timing for captions")
    t = 0.0
    for b in timing:
        words = b["text"].split()
        n = max(1, (len(words) + 4) // 5)
        step = b["seconds"] / n
        for i in range(n):
            chunks.append((t + i * step, t + (i + 1) * step, " ".join(words[i * 5:(i + 1) * 5])))
        t += b["seconds"] + gap
    return chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video_dir")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--preview", action="store_true")
    g.add_argument("--final", action="store_true")
    a = ap.parse_args()
    vdir = pathlib.Path(a.video_dir)
    W, H = (854, 480) if a.preview else (1920, 1080)
    spec = json.loads((vdir / "spec.json").read_text())
    timing = json.loads((vdir / "audio/timing.json").read_text())
    beat_len = {t["beat"]: t["seconds"] for t in timing}
    GAP = 0.25
    work = vdir / "build" / ("preview" if a.preview else "final")
    shutil.rmtree(work, ignore_errors=True); work.mkdir(parents=True)

    # 1. video segments
    per_beat = {}
    for sc in spec["scenes"]:
        per_beat.setdefault(sc["beat"], []).append(sc)
    segs = []
    for beat in sorted(per_beat):
        if beat not in beat_len:
            sys.exit(f"spec uses beat {beat}, but narration has only {len(timing)} beats")
        share = (beat_len[beat] + GAP) / len(per_beat[beat])
        for j, sc in enumerate(per_beat[beat]):
            out = work / f"seg_{beat:03d}_{j}.mp4"
            segment(sc, share, vdir, out, W, H)
            segs.append(out)
    (work / "list.txt").write_text("".join(f"file '{p.name}'\n" for p in segs))
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-c", "copy", str(work / "video.mp4")])

    # 2. voice track (beats + small gaps), optional music, loudness
    parts = []
    for t in timing:
        parts += ["-i", str(vdir / "audio" / t["file"])]
    n = len(timing)
    filt = "".join(f"[{i}:a]apad=pad_dur={GAP}[a{i}];" for i in range(n)) + "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[voice]"
    run(["ffmpeg", "-y", *parts, "-filter_complex", filt, "-map", "[voice]", str(work / "voice.wav")])
    mix_in = ["-i", str(work / "voice.wav")]
    af = "[0:a]loudnorm=I=-14:TP=-1.5:LRA=11[out]"
    if spec.get("music") and (vdir / spec["music"]).exists():
        mix_in += ["-stream_loop", "-1", "-i", str(vdir / spec["music"])]
        af = "[1:a]volume=-20dB[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0[mx];[mx]loudnorm=I=-14:TP=-1.5:LRA=11[out]"
    run(["ffmpeg", "-y", *mix_in, "-filter_complex", af, "-map", "[out]", "-ar", "48000", str(work / "mix.wav")])

    # 3. captions (.srt for YouTube, .ass burned in)
    caps = captions(timing, GAP, work / "voice.wav" if a.final else None)
    (work / "captions.srt").write_text("".join(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n" for i, (s, e, t) in enumerate(caps, 1)))
    fs = int(56 * H / 1080)
    ass = ("[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, BorderStyle, Outline, Shadow, Alignment, MarginV\n"
           "Style: Cap,Inter,%d,&H00FFFFFF,&H00261A14,&H00000000,1,1,%d,0,2,%d\n\n[Events]\nFormat: Layer, Start, End, Style, Text\n"
           % (W, H, fs, max(2, fs // 12), int(H * 0.08)))
    ass += "".join(f"Dialogue: 0,{ts(s, False)},{ts(e, False)},Cap,{t}\n" for s, e, t in caps)
    (work / "captions.ass").write_text(ass)
    fontsdir = FONT_DIRS[0] if FONT_DIRS[0].exists() else pathlib.Path("/usr/share/fonts")
    out = vdir / ("preview_480p.mp4" if a.preview else "final_1080p.mp4")
    run(["ffmpeg", "-y", "-i", str(work / "video.mp4"), "-i", str(work / "mix.wav"),
         "-vf", f"subtitles={work / 'captions.ass'}:fontsdir={fontsdir}", "-map", "0:v", "-map", "1:a", "-shortest",
         "-c:v", "libx264", "-preset", "veryfast" if a.preview else "medium", "-crf", "28" if a.preview else "18",
         "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", str(out)])
    shutil.copy(work / "captions.srt", vdir / ("preview.srt" if a.preview else "final.srt"))
    print(f"done: {out}")


if __name__ == "__main__":
    main()
