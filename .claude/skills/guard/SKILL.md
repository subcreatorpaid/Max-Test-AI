---
name: guard
description: Run release checks for The History Invoice: facts, tags, AI disclosure, licences, policy, specs, secrets. Use before every commit and every gate.
---

# guard

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. `python scripts/guard.py`.
2. Every on-screen number has a fact pack row, date and correct tag; no relative time words.
3. Policy: no gore, no AI faces of real people, no fake documents, recreated headlines credited, no investment picks, "not financial advice" present, AI-disclosure box noted.
4. `licences.md` covers music, SFX, stock; kit files not committed. Final file 1920x1080 30 fps, loudness per `docs/video-process.md`.
Any fail goes to `brain/status.json -> alerts` and blocks the gate.
