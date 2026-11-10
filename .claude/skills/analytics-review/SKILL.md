---
name: analytics-review
description: Review History Invoice video data at 24 h, 7 days and every 3 videos, and update learnings and the rulebook.
---

# analytics-review

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
Pull vidIQ `video_stats` / `channel_analytics` (CTR, AVD, retention, traffic sources, subs per view). Compare with targets in `brain/goals.json`. Add one dated line per video to `brain/learnings.md`; propose rulebook changes (new version, never overwrite) when a pattern repeats in 3 videos. Update `brain/goals.json -> latest`.
