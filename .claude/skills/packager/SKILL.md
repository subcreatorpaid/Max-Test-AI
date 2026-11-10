---
name: packager
description: Make and score 3 titles + 3 thumbnails for a History Invoice video.
---

# packager

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
Titles: search phrase in first 40 chars + wallet stake, under 60 chars; score with vidIQ `score_title`. Thumbnails: one map/object, one glowing element, 2-3 words that never repeat the title (World View layout notes in `brain/competitors/`); score with vidIQ `score_thumbnail`. Save `videos/<id>/title-thumb.md`. Thumbnail promise must match the hook.

Read `docs/reference/youtube/thumbnail-ctr-guide.md` and the title rules in `docs/reference/youtube/seo-playbook.md`. While vidIQ is out of credits (until 30 Nov 2026), score titles and thumbnails by hand against those guides and say so in `title-thumb.md`. Faceless channel: ignore the guide's face advice.
