#!/usr/bin/env python3
"""Assemble a Max Tests AI video from videos/<slug>/edit.json (the editor skill writes it).

    python scripts/render.py videos/<slug> --preview   # 854x480, fast check
    python scripts/render.py videos/<slug> --final     # 1920x1080, -14 LUFS, captions .srt (+ faster-whisper if installed)

Runs on Hammad's PC (Windows/Mac/Linux, needs ffmpeg + Pillow) or in GitHub Actions for previews.

edit.json:
{
  "music": "footage/music.wav" | null,        # bed under everything, -20 dB (kit score or YouTube Audio Library)
  "sfx_mix": "footage/sfx.wav" | null,         # optional full-length SFX track from the kit's build_audio.py
  "scenes": [
    {"type": "host",    "src": "footage/max-01-hook.mp4"},                       # Max clip: keeps its own audio, full length
    {"type": "screen",  "src": "footage/R1.mp4", "start": 3.0, "vo": "audio/vo-01.wav", "speed": 1.0, "zoom": [0.8, 0.2, 1.5]},
    {"type": "graphic", "src": "footage/G2.mp4", "vo": "audio/voiceover.mp3", "vo_start": 41.2, "vo_end": 47.9},  # slice of the one narration file
    {"type": "card", "title": "Step 1", "text": "Export the timeline", "vo": "audio/vo-04.wav"}
  ]
}
Scene length = its VO length (+0.2 s), or the clip's own length for host clips, or "dur" if given.
A missing src renders a grey placeholder naming the clip; a missing VO file is silence of "dur" (default 3 s).
Paths are relative to the video folder. Also writes edit-list.md so Hammad can rebuild the cut in CapCut.
"""
import argparse, json, pathlib, shutil, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

BRAND = {"bg": "#FFFFFF", "soft": "#E9EDF3", "ink": "#141A26", "accent": "#2F6BFF", "muted": "#5B6578"}
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT_DIRS = [ROOT / "assets/brand", pathlib.Path("/usr/share/fonts"), pathlib.Path("C:/Windows/Fonts")]
FPS, SR, PAD = 30, 48000, 0.2


def font(size, bold=True):
    names = ["Inter-Bold.ttf", "Inter-SemiBold.ttf", "DejaVuSans-Bold.ttf", "arialbd.ttf"] if bold else ["Inter-Medium.ttf", "Inter-Regular.ttf", "DejaVuSans.ttf", "arial.ttf"]
    for d in FONT_DIRS:
        if d.exists():
            for n in names:
                hits = list(d.rglob(n))
                if hits:
                    return ImageFont.truetype(str(hits[0]), size)
    return ImageFont.load_default()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed: {' '.join(map(str, cmd[:8]))}...\n{r.stderr[-1500:]}")
    return r.stdout


def length(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]).strip() or 0)


def has_audio(path):
    return bool(run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(path)]).strip())


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
        d.text((int(240 * s), int(370 * s)), title, font=font(int(84 * s)), fill=BRAND["accent"])
        y = int(500 * s)
        for line in textwrap.wrap(text, 34):
            d.text((int(240 * s), y), line, font=font(int(64 * s)), fill=BRAND["ink"]); y += int(84 * s)
    img.save(path)


def segment(sc, vdir, out, W, H):
    """Render one scene to out (video + stereo audio). Returns its duration."""
    src = vdir / sc["src"] if sc.get("src") else None
    vo = vdir / sc["vo"] if sc.get("vo") else None
    vo_ok = vo is not None and vo.exists()
    vo_cut = ["-ss", str(sc["vo_start"]), "-to", str(sc["vo_end"])] if "vo_start" in sc else []
    if sc["type"] == "host" and src and src.exists():
        dur = sc.get("dur") or length(src)
    elif vo_ok:
        dur = (sc["vo_end"] - sc["vo_start"] if vo_cut else length(vo)) + PAD
    else:
        dur = sc.get("dur", 3.0)
    fit = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps={FPS}"
    inputs, vf = [], fit
    if sc["type"] in ("host", "screen", "graphic") and src and src.exists():
        if sc.get("speed", 1.0) != 1.0:
            vf = f"setpts=PTS/{sc['speed']}," + vf
        if sc.get("zoom"):
            cx, cy, z = sc["zoom"]
            Z = f"if(lt(t\\,0.4)\\,1+({z}-1)*t/0.4\\,{z})"
            vf += f",scale=w='{W}*{Z}':h='{H}*{Z}':eval=frame,crop={W}:{H}:'(iw-{W})*{cx}':'(ih-{H})*{cy}'"
        inputs = ["-stream_loop", "-1", "-ss", str(sc.get("start", 0)), "-i", str(src)]
    else:
        png = out.with_suffix(".png")
        if sc["type"] == "card":
            card_png(png, W, H, sc.get("title", ""), sc.get("text", ""))
        else:
            card_png(png, W, H, f"{sc['type'].upper()}: {sc.get('src', '?')}", sc.get("note", "Footage not added yet."), placeholder=True)
        inputs = ["-loop", "1", "-i", str(png)]
        vf = f"scale={W*2}:{H*2},zoompan=z='min(1+0.0008*on\\,1.04)':d=1:s={W}x{H}:fps={FPS},setsar=1"
    # audio: host clip's own voice, else the VO file, else silence
    if sc["type"] == "host" and src and src.exists() and has_audio(src):
        amap = ["-map", "0:a"]
    elif vo_ok:
        inputs += [*vo_cut, "-i", str(vo)]; amap = ["-map", "1:a"]
    else:
        inputs += ["-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=stereo"]; amap = ["-map", "1:a"]
    run(["ffmpeg", "-y", *inputs, "-t", f"{dur:.3f}", "-vf", vf, "-map", "0:v", *amap,
         "-af", f"aresample={SR},aformat=channel_layouts=stereo,apad", "-t", f"{dur:.3f}",
         "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", str(out.with_suffix(".mov"))])
    return dur


def ts(t, srt=True):
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",") if srt else f"{h:d}:{m:02d}:{s:05.2f}"


def captions(scenes, starts, durs, vdir, mix, use_whisper):
    if use_whisper:
        try:
            from faster_whisper import WhisperModel
            segs, _ = WhisperModel("small.en", compute_type="int8").transcribe(str(mix), word_timestamps=True)
            words = [w for sg in segs for w in sg.words]
            return [(g[0].start, g[-1].end, "".join(w.word for w in g).strip()) for g in (words[i:i + 5] for i in range(0, len(words), 5))]
        except ImportError:
            print("faster-whisper not installed: captions from the script text")
    caps = []
    for sc, st, du in zip(scenes, starts, durs):
        words = (sc.get("say") or "").split()
        if not words:
            continue
        n = max(1, (len(words) + 4) // 5)
        step = (du - PAD) / n
        caps += [(st + i * step, st + (i + 1) * step, " ".join(words[i * 5:(i + 1) * 5])) for i in range(n)]
    return caps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video_dir")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--preview", action="store_true")
    g.add_argument("--final", action="store_true")
    a = ap.parse_args()
    vdir = pathlib.Path(a.video_dir)
    W, H = (854, 480) if a.preview else (1920, 1080)
    edit = json.loads((vdir / "edit.json").read_text())
    work = vdir / "build" / ("preview" if a.preview else "final")
    shutil.rmtree(work, ignore_errors=True); work.mkdir(parents=True)

    segs, durs, starts, t = [], [], [], 0.0
    for i, sc in enumerate(edit["scenes"], 1):
        out = work / f"seg_{i:03d}"
        d = segment(sc, vdir, out, W, H)
        segs.append(out.with_suffix(".mov")); durs.append(d); starts.append(t); t += d
    (work / "list.txt").write_text("".join(f"file '{p.name}'\n" for p in segs))
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-c", "copy", str(work / "cut.mov")])

    # audio: voice track (+ SFX track) (+ music bed at -20 dB), master -14 LUFS / -1.5 dBTP
    ins, chain, n = ["-i", str(work / "cut.mov")], "[0:a]volume=1[v]", 1
    labels = ["[v]"]
    for key, vol in (("sfx_mix", "0dB"), ("music", "-20dB")):
        if edit.get(key) and (vdir / edit[key]).exists():
            ins += (["-stream_loop", "-1"] if key == "music" else []) + ["-i", str(vdir / edit[key])]
            chain += f";[{n}:a]volume={vol}[x{n}]"; labels.append(f"[x{n}]"); n += 1
    chain += f";{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]"
    run(["ffmpeg", "-y", *ins, "-filter_complex", chain, "-map", "[out]", "-ar", str(SR), str(work / "mix.wav")])

    caps = captions(edit["scenes"], starts, durs, vdir, work / "mix.wav", a.final)
    (work / "captions.srt").write_text("".join(f"{i}\n{ts(s)} --> {ts(e)}\n{x}\n\n" for i, (s, e, x) in enumerate(caps, 1)))
    fs = int(56 * H / 1080)
    ass = ("[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\n\n[V4+ Styles]\n"
           "Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, BorderStyle, Outline, Shadow, Alignment, MarginV\n"
           "Style: Cap,Inter,%d,&H00FFFFFF,&H00261A14,&H00000000,1,1,%d,0,2,%d\n\n[Events]\nFormat: Layer, Start, End, Style, Text\n"
           % (W, H, fs, max(2, fs // 12), int(H * 0.08)))
    ass += "".join(f"Dialogue: 0,{ts(s, False)},{ts(e, False)},Cap,{x}\n" for s, e, x in caps)
    (work / "captions.ass").write_text(ass)
    fontsdir = next((d for d in FONT_DIRS if d.exists()), ROOT)
    out = vdir / ("preview_480p.mp4" if a.preview else "final_1080p.mp4")
    sub = str(work / "captions.ass").replace("\\", "/").replace(":", "\\:")
    run(["ffmpeg", "-y", "-i", str(work / "cut.mov"), "-i", str(work / "mix.wav"),
         "-vf", f"subtitles='{sub}':fontsdir='{str(fontsdir).replace(chr(92), '/').replace(':', chr(92) + ':')}'",
         "-map", "0:v", "-map", "1:a", "-shortest", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "veryfast" if a.preview else "medium", "-crf", "28" if a.preview else "18",
         "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", str(out)])
    shutil.copy(work / "captions.srt", vdir / ("preview.srt" if a.preview else "final.srt"))

    # edit list so Hammad can rebuild or tweak the cut in CapCut
    rows = ["| # | at | type | source | in | length | audio | note |", "|---|---|---|---|---|---|---|---|"]
    for i, (sc, st, du) in enumerate(zip(edit["scenes"], starts, durs), 1):
        rows.append(f"| {i} | {ts(st, False)} | {sc['type']} | {sc.get('src') or sc.get('title', '')} | {sc.get('start', 0)} | {du:.2f}s | "
                    f"{'own' if sc['type'] == 'host' else sc.get('vo', '-')} | {'zoom ' + str(sc['zoom']) if sc.get('zoom') else ''} |")
    (vdir / "edit-list.md").write_text(f"# Edit list ({out.name}, {t:.1f}s)\n\n" + "\n".join(rows) + "\n")
    print(f"done: {out} ({t:.1f}s)")


if __name__ == "__main__":
    main()
