# Storyboard v1 (gate 1: needs Hammad's OK)

Runtime target ~9:30. Mix: Max ~12% (6 clips, ~45 s), screen recordings ~65%, motion graphics ~23%. A visual change every 3-5 s; one thing moves at a time. Captions bottom third, never over the area being zoomed.
Graphics (G*) are built with the Motion Graphics MAX kit on Hammad's PC (minimal style, Cobalt Field look in our blue, Inter). SFX from the kit: `tech/*` on Claude answers, `ui/click` on cuts, `move/swipe` on cards.

| # | Time | Type | On screen | On-screen text | Motion / SFX | Line (short) |
|---|---|---|---|---|---|---|
| 1 | 0:00 | MAX | max-01-hook | - | slow push-in; voice on frame 0 | "This video was edited by Claude..." |
| 2 | 0:04 | SCREEN | R1 raw timeline scroll | "RAW: 8:12" | zoom to waveform gaps; ui/click | "Here's the raw recording..." |
| 3 | 0:08 | GRAPHIC G1 | split raw vs finished + stopwatch | "8:12 -> [final]" | stopwatch ticks; tech/success | "And here's what came out..." |
| 4 | 0:12 | MAX | max-02-intro + lower third | "Max is an AI host" | static | "I'm Max, and yes..." |
| 5 | 0:18 | GRAPHIC G2 | "AI can write. Can it edit?" card | same | type-on; tech/type | belief challenge |
| 6 | 0:26 | GRAPHIC G3 | 3-level ladder (Plan / Cut / Drive) | Level 1-2-3 | each step lands; move/swipe | "three levels..." |
| 7 | 0:38 | MAX | max-01 second half (or reuse) | - | static | "Level three did not go the way I expected." (open loop 1) |
| 8 | 0:45 | SCREEN | R1 waveform zoom | - | zoom 1.4x | the raw mess |
| 9 | 0:58 | SCREEN | R2 auto captions + export | "Step 1: Auto captions" | sped up 4x; tech/scan | transcript |
| 10 | 1:25 | GRAPHIC G4 | "Claude reads the transcript" (file -> chat icon) | - | one move | reality check |
| 11 | 1:40 | SCREEN | R3 paste + prompt | "Step 2: one prompt" | zoom on prompt | Level 1 |
| 12 | 2:05 | SCREEN | R3 Claude answer scrolling | - | tech/ai-generate | cut list arrives |
| 13 | 2:30 | SCREEN | R3 zoom on hook suggestion | yellow highlight | zoom 1.6x | open loop 2 / what Claude spotted |
| 14 | 2:45 | MAX | max-03-surprised | - | static | "That's an editor's instinct." |
| 15 | 2:52 | GRAPHIC G5 | Level 1 verdict card | "LEVEL 1: [result]" | accent on state change; tech/success | verdict 1 |
| 16 | 3:10 | SCREEN | R4 transcript editing | "Step 3: delete text = cut video" | zooms on deleted lines; ui/click per cut | Level 2 |
| 17 | 3:50 | SCREEN | R4 remove pauses | - | sped up | auto pauses |
| 18 | 4:15 | GRAPHIC G6 | timeline shrinking + stopwatch | "[time] vs 1 hour" | one move | time saved |
| 19 | 4:30 | SCREEN | R4 the bad cut | red circle | zoom | "Here's the catch" |
| 20 | 4:45 | GRAPHIC G7 | Level 2 verdict | "LEVEL 2: [result]" | tech/success | verdict 2 |
| 21 | 5:00 | SCREEN | R5 Claude driving CapCut | "Level 3: Claude takes the mouse" | sped up 2-4x | Level 3 |
| 22 | 5:40 | MAX | max-04-broke | - | static | "And this is where it broke." (open loop 3) |
| 23 | 5:45 | SCREEN | R5 failure moment | red circle | zoom | the failure |
| 24 | 6:10 | GRAPHIC G8 | the fix card | "Fix: [result]" | move/swipe | fix |
| 25 | 6:30 | SCREEN | R5 finishing | stopwatch | sped up | result |
| 26 | 6:50 | GRAPHIC G9 | Level 3 verdict | "LEVEL 3: [result]" | tech/notify | verdict 3 |
| 27 | 7:00 | SCREEN | R6 captions, zooms, music | "Finishing touches" | zooms | finishing |
| 28 | 7:40 | GRAPHIC G1b | before/after split, full screen | "8:12 -> [final]" | musical event on the turn | before/after |
| 29 | 8:00 | MAX | max-05-verdict | - | slight push-in | "So, can Claude replace a video editor?" |
| 30 | 8:05 | GRAPHIC G10 | scorecard, 3 rows + time saved + cost | Yes / Mostly / Not yet | rows land one by one; tech/success | the verdict |
| 31 | 8:40 | GRAPHIC G11 | next video tease (Flow host) | "Next: consistent AI host" | CTA as interaction | outro |
| 32 | 8:50 | MAX | max-06-outro | - | static, wave | sign-off |

Assets Hammad supplies: R1-R7 (see `recordings.md`), max-01 to max-06 (see `flow-prompts.md`), stopwatch times, Claude's answer text.
Built by Claude: G1-G11 (kit, on Hammad's PC), voiceover (Max's Google voice, see brain/host.md), captions, music bed (YouTube Audio Library or kit score).
After the recordings, `[RESULT]` lines are filled in from the real footage, then the narration is locked and the preview renders.
