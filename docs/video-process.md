# The Invoice: video production process (the rule for every video)

This file keeps the original Round Two system and adds the Motion Graphics MAX quality gate (step 8b) and kit SFX (step 9). Update by adding, never by replacing.

Set 2026-11-04 by Hammad: "make it the best process, a rule into the brain to use it next videos".
The code in this folder is the working renderer from "Round Two". Copy it, change the shot list and the facts, then render.

## The steps, in order
1. **Script.** Start from a sourced fact pack, then write a Word (.docx) script. Every number needs a source and a tag (VERIFIED / REPORTED / ESTIMATE / ILLUSTRATION).
2. **Voice.** Free local Kokoro, blend `am_onyx:0.5,am_michael:0.5`, speed 0.92, -16 LUFS, one MP3 per chapter (`kok/render.py`, `kok/full.py`). Never use vidIQ or ElevenLabs.
3. **Timing.** Find paragraph start times from silence in each chapter MP3 (RMS < 0.01, 10 ms frames). Every shot cut lands on a paragraph start.
4. **Storyline and storyboard.** Write the storyline doc, then build pictorial panels (`sb/panels.py`, `sb/build.py`) and get Hammad's OK.
5. **B-roll list.** Give Hammad a coded clip list (CO-, A1-, CL-...). He downloads clips from Pexels/Pixabay (stills are fine when no video exists) into a local folder, which I stage into the container. Stock sites are blocked from the cloud, and Pinterest is for inspiration only.
6. **Shot list.** In `ten.py`, `build_shots()` maps clips to VO paragraphs:
   - `B(t0, t1, clip, overlays)` is footage: graded, a slow pan or push, slowed down if the clip is too short, and a text overlay PNG faded in.
   - `Gx(t0, t1, fn, args)` is a graphic made with PIL (maps, number cards, bars, timelines, globe, PART cards).
   - Aim for one visual change every 6-10 s. Put a number card or chart on every key figure, and a PART card at every act.
7. **Test frames first.** Run `python ten.py test` and look at the contact sheet. Fix overlaps, clipping and black edges before the full render.
8. **Render.** Segments render in a `Pool(3)` (never `imap` over all frames, which runs out of memory). Concat them, then add a vignette and grain. **Always encode with `-crf 23 -maxrate 12M -bufsize 24M`**, because grain at crf 20 made 4 GB.
8b. **Quality gate (Motion Graphics MAX bar, added 2026-11-04).** Before Hammad sees any cut, score it against the kit's `references/flagship-bar.md` 17 checks, scaled for a calm documentary look (holds up to 3 s with motion inside; a slow push, a light sweep or a focus pull counts as "new"):
   - **Never parked:** every card and chart keeps moving after it builds, with a slow push-in, a drifting light or glow, and a light sweep across big type.
   - **Real numbers count up** through real values, with tick SFX, landing on the spoken word.
   - **Layouts rotate:** footage text alternates bottom-left, centre, top-left and right. No three shots in a row share a composition. At least 3 frame-breaks per act (a macro push, a full-bleed number, a camera move into the map).
   - **Transitions:** at least 6 kinds per act (hard cut on beat, flash cut, whip with blur, light-edge wipe, match cut by shape, iris or dip). No plain crossfades.
   - **One hero carried through each part** (for example the strait map that returns, changes and gets marked), and a "how was that made?" moment about every 30-60 s in long-form.
   - **Light is the design:** every bright thing is a light source (glow, edge, sweep). Grain and vignette go on every frame.
   - **Sound per hit:** each visual hit gets its kit SFX on the same frame, plus 2+ musical events per act (drop, stop, silence). VO sits ≥12 LU over the bed.
   - **Review:** make a contact sheet (one frame every 0.75 s), then have a fresh reviewer (a subagent, or a separate pass done before re-reading the code) score it with the kit's `REVIEW-PROMPT.md`. Fix the hard fails, max 3 rounds, then send with the score.
   - The kit docs are read from Hammad's PC (`Motion-Graphics-MAX\motion-studio\references\`) and are never copied into shared files.

9. **Sound.** Run `sfx_mix.py`: the VO plus a low drone bed, with **Motion Graphics MAX kit SFX** on every cut:
   - deep whoosh on map shots
   - whip + card + counter on number cards
   - chart_grow on charts
   - reverse cymbal + sub drop + stone on PART cards
   - sub_808 on big reveals
   - loudnorm to -16 LUFS
   - The kit WAVs stay private: stage them from `C:\Users\hamma\Documents\Motion-Graphics-MAX\motion-studio\sound-fx\` and never commit or share them.
10. **Deliver.** Send the 1080p file to `/mnt/project-files/documentary-channel/<video>/`. Make a 720p two-pass copy under 25 MB (about 1350k) with `device_commit_files` into `C:\Users\hamma\Documents\Documentry\<video>\`. Keep the thread open until he OKs it.

## Look (locked)
- **Colours:** ink black (16,15,14), paper (236,228,214), orange (232,89,12). Weapons red #E63946, water cyan #00B4D8, SPENT crimson #C1121F, warning orange #FF5400.
- **Fonts:** Inter Bold for headlines, Caladea Bold Italic in orange for the second line, Bebas for stamps.
- **Footage grade:** `eq=saturation=0.6:contrast=1.06:brightness=-0.045:gamma=0.94` plus a cool colorbalance, with a bottom-left shade under text.
- **Maps:** AWS terrarium DEM hillshade (`assets/relief.png`, `assets/gulf.png`) and Natural Earth borders, re-downloaded from naturalearth.s3 when needed.

## Gotchas
- PIL draw on an RGBA image *replaces* alpha. Draw faded text on a transparent layer and composite it onto the background, or fades pop and rings turn black.
- Keep clips with recognisable wrong places (Sydney harbour, consumer quadcopters) for generic lines only, or tag them ILLUSTRATION.
- No AI faces of real people. Never copy Paycheckology's lines or titles.

## Engagement rules (2026-11-06, from Round Two launch data; these override older lines)
Round Two: average view 8:58 of 27:14, money started at 14:30, subscribe ask at 2:14, 1 subscriber from 412 views. So every video:
1. 18-20 minutes (about 2,400-2,800 words). Cut, never pad.
2. A household money number inside the first 30 seconds, plus a 2 s flash of the final receipt as a promise. Nothing (logo, disclaimer card) before the first story line.
3. First real money payoff by minute 6-8; half-receipt around the middle.
4. Bring it back to "your bill" every 60-90 seconds.
5. Running corner invoice that prints one line at the end of each part.
6. Every part ends on a specific question the next part answers.
7. Subscribe ask right after the first payoff (6-8 min), tied to the next video; one 5 s line again at the receipt.
8. Change the pace: fast 3 s cuts plus 2-3 slow moments; nothing longer than about 90 s at one speed.
9. One comment question in the video, and the same question pinned.
10. End screen points to another video, not only the subscribe button.
11. Title under 60 characters with the wallet stake; Test & Compare with 3 thumbnails on every upload.
12. Review the data at 24 hours, 7 days and after every 3 videos.
Full text: master-prompt-v3.md (ENGAGEMENT RULES) and pipeline/PROCESS.md in the project files.

## Script rulebook v1 (2026-11-06, Round Two at 26 h: 479 views, CTR 6.8%, AVD 8:41, search 1%)
Use library/rules/History-Invoice-Script-Rulebook-v1.docx for every new script. Changes: first money payoff by 4:00 and subscribe ask at 4:00-4:30 (home-feed viewers leave at ~4.6 min); half-receipt at ~9 min; history/background capped at 2 min and must end on money; SEARCH: one real search phrase chosen first, in the first 40 characters of the title, spoken by 0:15 and once per part, chapters named as searches, description opens with it; 16-point script checklist before Hammad sees a script.
