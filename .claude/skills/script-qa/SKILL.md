---
name: script-qa
description: Review a History Invoice script before Hammad sees it: rulebook 16-point checklist + numbering review.
---

# script-qa

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: `python scripts/guard.py`, one commit, push, one log file in `brain/log/`, any ask for Hammad in `brain/status.json -> approvals`.

## Job
Run `docs/script-rulebook-v1.md` section 6 (16 ticks) and `docs/script-numbering-and-review.md` section 3 (facts, story, makeability). Output: verdict per part PASS/FIX, fixes as `code · problem · fix`. Any facts fail blocks the voice step. Also run on any script Hammad pastes in (number it first).
