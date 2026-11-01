---
name: editor
description: Do the full edit of a Max Tests AI video on Hammad's PC and deliver the finished, upload-ready MP4 (plus an edit list for CapCut). Use after the storyboard OK when the footage, Max clips, narration and kit graphics exist.
---

# editor

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`, the video's `storyboard.md`. End: guard, one commit (no kit files, no raw SFX), push, one log file, approvals in `status.json`.

## Production split (Hammad, 2026-11-01)
- **Max clips:** Hammad makes them in Google Vids from `videos/<slug>/vids-scenes.md` (prompts/voice owned by the Google Vids setup, `docs/google-vids-max.md`). Each clip keeps its own audio.
- **Screen narration:** ONE file `videos/<slug>/audio/voiceover.mp3`, recorded by Hammad from `voiceover.md` in Max's voice.
- **Screen recordings:** `footage/R*.mp4` per `recordings.md`.
- **Animations:** made locally with Claude using the Motion Graphics MAX kit on Hammad's PC -> `footage/G*.mp4` (+ the kit's SFX track).
- **Edit:** Claude does the whole edit and hands back the final video.

## How (CapCut has no API; new CapCut versions encrypt `draft_content.json`)
1. Runs on Hammad's PC (Remote Control session or local Claude Code), where the footage and the kit live.
2. Find each narration line's start/end in `voiceover.mp3`: run faster-whisper (word timestamps) and match the lines of `voiceover.md`. Write `edit.json` (format in `scripts/render.py`): one scene per storyboard row, `vo_start`/`vo_end` slices for screen/graphic/card scenes, host clips with their own audio, `zoom` and `speed` for screen recordings (speed up waits 2-4x).
3. Sound: kit `export_sfx.mjs` + `build_audio.py` for the SFX/music track (voice >= 12 LU over the bed, -14 LUFS master); pass it as `sfx_mix` / `music` in `edit.json`.
4. `python scripts/render.py videos/<slug> --preview` -> watch it against the storyboard and the 17 checks (`flagship-bar.md`) and the brand rules; fix; Gate 2: Hammad reviews `preview_480p.mp4`.
5. After the review OK: `python scripts/render.py videos/<slug> --final` -> `final_1080p.mp4` + `final.srt`, ready to upload (1920x1080, 30 fps, -14 LUFS, burned captions + .srt).
6. `render.py` also writes `edit-list.md` (every cut, in-point, length, audio, zoom) so Hammad can rebuild or tweak the edit in CapCut by hand if he wants.

## CapCut draft (only if it works)
If Hammad's CapCut version saves an UNENCRYPTED `draft_content.json`, Claude may write the draft directly so the edit opens in CapCut. Test on a copy first (one cut, open in CapCut, confirm), never on his only project. If it's encrypted, use the MP4 + edit list route above.
