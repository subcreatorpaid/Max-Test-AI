---
name: secretary
description: Morning briefing and dashboard for Hammad: max 3 to-dos, approvals queue, pipeline. Use for 'what do I need to do today', 'status'.
---

# secretary

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. Read `brain/status.json`, `brain/plan.json`, the newest files in `brain/log/`.
2. Rebuild `brain/status.json -> today` (max 3 to-dos, most urgent gate first) and `approvals`.
3. Reply to Hammad in under 80 words, plain English: today's 3 to-dos, what is waiting on him (with the file to open), what the team did since last time.
4. Update the Control Room dashboard when it exists.
Never add a 4th to-do: push extras to tomorrow.
