---
name: shorts
description: Cut 1-3 YouTube Shorts from a finished History Invoice video and write their pack. Use after the long video's final render, before or after upload.
---

# shorts

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. Read `docs/reference/youtube/shorts-playbook.md` (stats are REPORTED) and the script's "3 Shorts cut-downs" (master prompt Stage B section 8) plus the hook-lab runner-up.
2. Pick up to 3: the scariest number, the Receipt, one surprising mechanism. 30-55 s each, 9:16, 1080x1920.
3. Per Short write: start/end codes from the numbered script (`INV-NNN · Pn · NN`), a new 1-2 s opening line that works with no context, on-screen text, the number's tag + source still on screen, a last line that loops back into the first, title (under 60 chars, search phrase first), 3-5 hashtags, Related video = the long video.
4. Same rules as the long video: tags on numbers, no gore, AI-disclosure tick, Kokoro voice only, no new facts beyond the fact pack.
5. Save `videos/<id>/shorts.md`. Renders go through animator (360p review first). Posting is public: each Short needs Hammad's OK, spread over the week (`docs/script-rulebook-v1.md` section on after-upload).
