---
name: animator
description: Make the History Invoice visuals and render: maps, number cards, PART cards, the Receipt, B-roll grade, sound mix (Stage V).
---

# animator

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. Stage V lists (`docs/master-prompt-v3.md`): paragraph list, graphics list (library IDs), coded B-roll list for Hammad (Pexels/Pixabay search phrases + still fallback), SFX plan.
2. Pipeline is on Hammad's PC: copy `Documentry\library\code\` into the video folder; steps in `Documentry\library\README.md` and `docs/video-process.md` (Kokoro voice, `wordtimes2.py`, test sheets, draft, mix).
3. 360p review render first (**Gate 4**), then 1080p final once. crf 23, maxrate 12M. Kit SFX loaded from the PC only.
4. After the final: update `docs/library.md` (new graphics, SFX picks, B-roll, one lesson).

## Look rules
Before any storyboard or render, read `docs/look-rules.md` (Hammad's picture notes). When he gives a new note, add it there the same day, update the kit, and log it in `brain/learnings.md`.
