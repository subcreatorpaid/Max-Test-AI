---
name: creator
description: Make the storyboard stills, motion graphics, voiceover, captions and renders for a Max Tests AI video.
---

# creator

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. **Voiceover:** `python scripts/tts.py videos/<slug>/narration.txt videos/<slug>/audio/` (Kokoro, voice am_michael). If Hammad supplied Speechify audio, use that instead.
2. **spec.json:** build `videos/<slug>/spec.json` from the storyboard: an ordered list of scenes, each `{"id", "type": "host|screen|card|zoom", "src", "start", "end", "text", "zoom": [x,y,scale], "caption": true}`. Same format later feeds Shorts (9:16).
3. **Motion graphics (HyperFrames kit, see below):** step cards, verdict card, arrows from `brain/brand.md` tokens (Inter, #2F6BFF, #FFD23F). Follow the Motion System approach in handbook ch.6 (Prompts 2 and 3 in `docs/handbook.md` ch.10) when building new graphic types.
4. **Preview render (after storyboard OK):** run the `render-preview` GitHub Action (480p, burned captions). Gate 2: Hammad reviews.
5. **Final render (after review OK):** the `render-final` Action (1080p, captions .srt, -14 LUFS).
6. Log licences in `videos/<slug>/licences.md`.
Never re-render without a change. Never upload.

## Motion graphics with the motion-studio kit (Motion Graphics MAX)
**Decision 2026-11-01 (Hammad): the kit stays on Hammad's PC only** (`C:\Users\hamma\Documents\Motion-Graphics-MAX`). The repo is public, so never commit kit code, its docs or SFX `.wav` files. Motion graphics, the SFX/music pass (`build_audio.py`) and the FINAL render run on Hammad's PC (Claude drives it through a Remote Control session, or Hammad runs the commands). GitHub Actions only does previews without kit sounds. Commit back only the rendered `footage/G*.mp4` clips (no raw SFX).
- Follow `motion-studio/SKILL.md` steps 3-8 (setup, look + style frames, voice, build, verify, sound, draft, final). Our director/scriptwriter replace its intake + script steps: hand it a filled `BRIEF.md` (intake table) and `SCRIPT.md` with `ON SCREEN:` lines, then run `check_brief.py`.
- Load `references/shapes/tool-film.md`, `styles/minimal.md`, the Cobalt Field look (recoloured per `brain/brand.md`), and `references/flagship-bar.md` before building.
- Framework rules: everything a pure function of time (no `Date.now()`/`Math.random()`, use `RH.hash`); one paused GSAP timeline; `js/cues.js` is generated, never hand-edited; run `node tools/overlap_scan.mjs` before render.
- Sound pass: `node tools/export_sfx.mjs` -> `python3 tools/build_audio.py` -> read `assets/audio/mix-report.txt`; any line under 12 LU blocks the render.
- Render graphic segments with `npx hyperframes@0.8.140 render` and drop them into `videos/<slug>/footage/G*.mp4`; `scripts/render.py` then assembles them (scene type `graphic`) with the screen recordings and Max clips.
- Shorts later: the kit's reel mode (text behind Max, screen behind, cut-out pop) on the 9:16 host clips.
