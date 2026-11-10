---
name: storyboard
description: Build the History Invoice storyboard sheet (still + voice line per scene) from the numbered script.
---

# storyboard

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
Use the paragraph codes from the script. One panel per paragraph (or shot a/b/c): code, still, narration line, visual type, on-screen text, SFX. Export PDF/docx to `videos/<id>/` and Hammad's `Documentry\INV-NNN-<slug>\`. Reuse graphics by ID from `docs/library.md`.
