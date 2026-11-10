---
name: publisher
description: Prepare the History Invoice upload pack, and upload only after Hammad's OK.
---

# publisher

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
Write `videos/<id>/upload.md` like `Documentry\INV-003-pickaxe-mountain\upload\youtube-upload-pack.md`: title, description (search phrase in the first 2 lines, chapters as searches, disclaimer, sources), 3-5 tags, file name with the phrase, pinned comment, end screen target, AI-disclosure tick, Test & Compare thumbnails. **Gate 5.** Upload is manual by Hammad until he OKs an automated route.

Before asking for Gate 5, tick every line of `docs/reference/youtube/pre-publish-checklist.md` and paste the ticked list at the bottom of `upload.md`. Limits come from `docs/reference/youtube/seo-playbook.md`.
