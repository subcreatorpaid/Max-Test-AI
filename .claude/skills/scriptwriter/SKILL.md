---
name: scriptwriter
description: Write the numbered AV script for a History Invoice video (Stage B, Opus). Uses only the approved fact pack.
---

# scriptwriter

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. `docs/master-prompt-v3.md` Stage B with `docs/script-rulebook-v1.md` on top (rulebook wins). 2,400-2,800 words, 18-20 min.
2. Number every paragraph `INV-NNN · Pn · NN` per `docs/script-numbering-and-review.md`; table columns Code | Narration | Words/sec | Facts | Shot(s) | Visual | On-screen text | Tag + source | SFX.
3. Return the Stage B section 8 extras (claims check, NEED FACT list, titles, chapters as searches, 3 Shorts, pinned comment, sources).
4. Save `videos/<id>/INV-NNN-<slug>-script-vN.docx` + `.md`; never overwrite an old version. Run script-qa, then **Gate 2**.
