# Brand: Max Tests AI

## Voice
- Mood: **clean, smart, honest**. A calm tech explainer, like a smart friend showing you his screen.
- Plain US English, short sentences, active voice, about 150 words a minute. Write for the ear.
- Every video has a real point of view: a test, a comparison, a verdict. Never just restate a tool's website.
- Promise only what we show working on screen.

## Never-list
- No hype words: insane, game-changer, mind-blowing, crazy, "you won't believe".
- No fake income claims or "make $X a day".
- No AI news round-ups (stale in days). Always a hands-on test with a visible result.
- No copying other creators' scripts, thumbnails, voices, faces or branding. Copy structure ideas only.
- No "smash that like button", no "hey guys", no channel intro before the hook.
- No medical, legal or financial advice.

## Look
| Token | Value | Use |
|---|---|---|
| Background | #FFFFFF / soft grey #E9EDF3 | cards, frames |
| Ink | #141A26 | text |
| Accent | electric blue #2F6BFF | highlights, progress, the "look here" signal |
| Highlight | yellow #FFD23F | arrows, circles, labels, key word in captions |
| Muted | #5B6578 | secondary text |
- Font: **Inter** (titles 700/800, body 500). Nothing important under 22 px at 1080p.
- Corners 16 px on cards; soft shadow only on the one card in focus.

## Thumbnails
Same layout every time: Max's face (in his electric-blue overshirt) (reacting: surprised / sceptical / smiling) on one side, the finished result on the other, **2-3 big words** in Inter Black, white or yellow on a blue bar. Text never repeats the title. 3 options per video, scored with vidIQ before choosing.

## Motion (clean motion graphics)
**Engine:** HyperFrames + GSAP via Hammad's motion-studio kit (Motion Graphics MAX, `hyperframes@0.8.140`), **minimal** style, **Cobalt Field** look recoloured to our tokens (field/accent #2F6BFF, white surfaces, ink #141A26, grey #5B6578) with Inter 800/900 headlines and Inter 500/600 labels. Shape: the kit's **tool film** (open on the input -> the prompt -> the tool responding -> proof -> one big result -> CTA as an interaction). No title card or logo at the start. Something lands every 0.2-0.6 s; camera always pushing 1.00 -> 1.05; the accent only on state changes (checked, sent, done).

- Zoom-ins on the screen recording to the exact button or result (1.15-1.6x, eased, 0.4 s).
- Yellow arrows and circles to show where to click. Step cards ("Step 2: export the timeline").
- Kinetic captions: Inter 600, white with dark outline, bottom third, current word in yellow. Never over the key part of the screen.
- One thing moves at a time. Smooth ease-in-out, no bounce, no glitch effects.
- A visual change every 3-5 seconds (handbook 4-second cut rule).
- Clean image: no film grain, lens flare or colour filters.

## Video standard (every long video must have)
1. **0:00-0:05 click confirmation:** show the finished result and say the title's promise. Max on screen.
2. **0:05-0:25 belief challenge:** why the usual way is slow/wrong, and the open loop ("by the end you'll see if it beats a real editor").
3. **Chapters** (4-6), each answering one question, re-hook every 35-45 s.
4. **Proof:** the real screen recording of doing it, including one honest problem and the fix.
5. **Verdict:** score or clear yes/no, who it's for, cost (free/paid).
6. **Outro:** one takeaway, tease the next video, sign-off line. No like/subscribe begging.
7. Captions burned in + .srt uploaded. Loudness -14 LUFS, music -20 dB under voice.
8. Disclosures: AI host (YouTube altered-content box), affiliate/sponsor lines spoken and written.
Length 8-12 min. 16:9, 1080p, 30 fps.

## Sound
- SFX from the Motion Graphics MAX pack (195 sounds, `catalog.json` placement rules): `tech/*` for on-screen AI UI (click, ai-generate, type, data, success, notify, scan), `ui/*` for physical presses, `move/swipe` + `texture/shimmer` for minimal transitions. `hit_ms` lands on the motion's landing frame. Max 2 sounds per moment; never the same file twice in a row. Three well-placed sounds beat thirty.
- Music: the kit's synthesised score (bright plucky synth ~116 BPM) or a YouTube Audio Library track at `assets/audio/music.wav`; licence logged in `videos/<slug>/licences.md`.
- Mix (kit `build_audio.py`): voice >= 12 LU over music + SFX on every line; master -14 LUFS, -1 dBTP. Any line under 12 LU blocks the render. Check on a phone speaker.
- Never upload, share or Content-ID the SFX files themselves (licence).
