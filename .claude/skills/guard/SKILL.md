---
name: guard
description: Run release checks for Max Tests AI: facts, copyright, AI disclosure, links, specs, secrets. Use before every commit and before every gate.
---

# guard

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. `python scripts/guard.py` (brain files valid, JSON parses, no secrets, log format, video folder completeness).
2. Before gate 3, run the handbook's **60-second pre-flight audit** (Prompt 6, `docs/handbook.md` ch.10) on the script + shot list, as a table: Risk | GREEN/YELLOW/RED | Issue | Fix, covering: real-person likeness, brand logos/trade dress, voice consent, AI disclosure, music rights, sensitive claims.
3. Check: every claim in the script has a row in `facts.md`; `licences.md` covers all music/SFX; disclosure lines present (spoken + written); all links open; final file is 1920x1080, 30 fps, -14 LUFS, captions match narration.
4. Any RED blocks the gate: add it to `brain/status.json -> alerts`.
