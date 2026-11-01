---
name: strategist
description: Pick the next videos and write the one-page brief for Max Tests AI. Use for 'what should we make next', 'brief for X', monthly plan.
---

# strategist

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. Pick from `brain/ideas.json` using research + `brain/learnings.md`. Prefer: a tool people search for now, a visible result we can build, a topic a tracked competitor proved (same or close variant).
2. Run the **goal-lock** skill on it.
3. Write `videos/<slug>/brief.md` (one page):
   - Viewer + their problem · Promise (title-level, one line) · What Max builds/tests on screen · Verdict question
   - Packaging idea: working title + thumbnail idea (face + result + 2-3 words)
   - 3 hook options (use **hook-lab**) · Length 8-12 min · Chapters (4-6)
   - Screen recordings likely needed · Affiliate/sponsor links (with disclosure) · CTA = next video
4. Update `brain/plan.json` (stage: brief) and `brain/status.json`.
Monthly: plan the next 4 videos in `brain/plan.json`, mixing pillars: tool test (50%), build-a-workflow/bot (25%), AI video/creative how-to (25%).
