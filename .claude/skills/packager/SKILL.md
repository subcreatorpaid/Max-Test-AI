---
name: packager
description: Make and score 3 titles and 3 thumbnails per Max Tests AI video and pick the best.
---

# packager

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job `videos/<slug>/title-thumb.md`
1. 3 titles < 60 chars. Patterns that work now: "I Tested X", "I Edited/Built X With Claude + Y", "How to X With AI (Full Guide)". Honest: only promise what the video shows.
2. Score each with vidIQ `score_title`; keep the scores.
3. 3 thumbnail concepts (brand layout: Max's face reacting on one side, result on the other, 2-3 big words in Inter Black on a blue bar). Write each as a Gemini/Flow image prompt using `brain/host/host-hero.jpeg` as reference. Optional: Canva.
4. Score with vidIQ `score_thumbnail` and compare to competitors with `similar_thumbnails`.
5. Recommend one title + one thumbnail with one line why. Hammad OKs at the final-upload gate.
