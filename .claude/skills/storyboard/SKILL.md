---
name: storyboard
description: Write the shot-by-shot storyboard for a Max Tests AI video.
---

# storyboard

`videos/<slug>/storyboard.md` as a table, one row per 3-5 s beat:
| # | time | type (MAX / SCREEN / CARD / ZOOM) | what's on screen | on-screen text | motion | SFX / music | spoken line |
Rules: Max rows max 30% of runtime; a visual change every 3-5 s; one thing moves at a time; captions in the bottom third never over the key area; step cards use brand tokens. Reference recording ids from `recordings.md` and clip ids from `flow-prompts.md`.
End with a summary: runtime, % Max / screen / graphics, list of assets Hammad must supply. This is gate 1: Hammad OKs before any render.
