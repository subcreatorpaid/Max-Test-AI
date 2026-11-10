# INV-007 style adaptation: what we took from the Round Two draft (part 3)

Studied 2026-11-10 at 3 frames a second: `round-two-full-v1-draft-360p-part3.mp4` (9:02, 1,626 frames, 51 shots). Hammad's brief: "make it somewhat similar to that"; keep the mix (50% graphics / 30% video / 20% photos); every clip and photo must match the line being spoken; no "Illustration" label on screen.

## What the reference does (timestamps in the reference)
| Time | Element | What it looks like |
|---|---|---|
| 0:00 | Ledger number card | dark ruled paper, small kicker with orange dash, big white number, orange serif italic line, tiny tag top-right |
| 0:17, 5:36 | Toned footage | warm grey, slightly posterised, one soft orange glow on the subject, torn-paper wipe in, paper lower-third (bold caps + orange italic) |
| 0:39 | Document under magnifier (NOT used: Hammad said no magnifier) | report page on dark desk, lens slides along, one row highlighted orange |
| 0:58, 4:48 | Typed card + rubber stamp | paper card, serif italic types in, red stamp (ESTIMATE / SCENARIO / PAID / UNPAID) slams on |
| 1:22 | Split-flap board | orange letters flip into place |
| 1:38 | Cut-paper figures | faceless paper people with paper result tags |
| 2:06 | Night/infrared footage | history beat with lower-third |
| 2:29, 8:10 | Navy globe / map | dark beige land, orange arcs draw, red pins with paper labels |
| 2:52 | B&W ship footage | chapter label lower-third |
| 3:15 | Part card | "PART 5 / Your Table", giant faded "05", orange sub |
| 3:18-5:03 | Receipt printer | paper slides out of a slot, mono lines type in, red amounts, stamps |
| 5:52 | Mini-chart tiles | dashboard of small sparklines |
| 6:46 | Folder + index cards | manila folder, map photo, "WHAT YOU CAN DO" cards |
| 8:51 | Particle logo | confetti assembles into the channel name |

What we do NOT copy: the reference holds one frame for 20-40 seconds (e.g. 0:00-0:16, 1:38-2:05, 3:18-4:47). Our rulebook says nothing longer than ~90 s in one visual system and a change every 4-8 s, so each element animates and we cut more often.

## Our kit v2 (code in `scripts/storyboard2/kit.py`)
N ledger number · L toned footage + glow + paper label · D document, key line highlighted and circled in red pen (no magnifier) · T typed card + stamp (the stamp IS the confidence tag) · B split-flap · K cut-paper figures · M navy globe/map · P part card · R receipt printer · W mini-chart tiles · X folder + index cards · E particle end card. Kept from our brand: ink/paper/orange, Inter + Caladea, confidence tags on every number, the Receipt, running half-receipt.

## Picture rules for INV-007
0. Footage and photos stay in COLOUR like INV-006 (Hammad, 2026-11-10), lightly graded; the paper labels and stamps carry the reference look.
0b. About 30% of footage/photo time is SHADOW (dark, near-colourless, cold, heavy vignette) on the sombre beats: deaths, abandonment, the crews left out. The rest is colour graded by scene intensity: CALM (cooler, softer), COLOUR (INV-006 look), INTENSE (punchier, warmer) on danger and money spikes. Grade map: kit.GRADE in scripts/storyboard2/kit.py (Hammad, 2026-11-10).
0c. All paper cards use the beige document paper (214,204,186), never white (Hammad, 2026-11-10).
0d. Colour shots are 20% darker than the source (brightness x0.8) on top of the intensity grade (Hammad, 2026-11-10).
0e. Every graphic sits on the part-card background (dark ledger with faint lines), maps included. No particle-assemble effect anywhere; the end card is plain type that fades in.
0f. A different graphic type for each explanation (kit2.py has 31 one-off types). Only the chapter cards, the Receipt, and graphics for the same explanation (Gulf map, same checklist, leaders' quotes, What you can do) repeat (Hammad, 2026-11-10).
1. Every clip/photo is chosen for its line (query per paragraph in `visuals_v2.py`), never by theme word. If no good match, the shot becomes a graphic.
2. Candidates (4 per shot) are fetched and picked by eye before render; the storyboard shows the pick.
3. No faces of identifiable people; no brands in focus; no explosions on people.
4. No "Illustration" label on screen (pending Hammad's confirmation); YouTube's synthetic-content box still ticked at upload.
