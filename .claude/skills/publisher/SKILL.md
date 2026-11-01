---
name: publisher
description: Prepare the upload pack for a Max Tests AI video and schedule it ONLY after Hammad's final OK.
---

# publisher

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job `videos/<slug>/upload.md`
- Description: 2 lines (keyword first) + chapters with timestamps + links (affiliate links marked) + disclosure lines ("Max is an AI host." / "Some links are affiliate links...").
- 10-15 tags, end screen (next video + subscribe), pinned comment text.
- Checklist: altered/synthetic content box = YES; paid promotion box if any sponsor; captions .srt uploaded; category Science & Technology; language English (US).
- Upload only after gate 3 OK in `brain/status.json`, as **private or scheduled**, never public directly. Never post comments without OK.
Shorts phase: use handbook Prompt 7 (`docs/handbook.md` ch.10) for per-platform copy.
