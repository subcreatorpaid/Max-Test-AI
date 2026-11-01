# Max Reed: character bible

**Who:** Max Reed, the host of Max Tests AI. A realistic AI character, openly an AI ("Max here. Yes, I'm an AI."). Looks early-to-mid 30s.
**Look (locked 2026-11-01 from the first Google Vids clip, Hammad's pick "keep dark-tee look"):** same face as `brain/host/host-hero.jpeg`: short tousled brown hair, light stubble beard, warm smile. Wears a **plain dark charcoal crew-neck tee with a small white face-icon logo on the left chest**. Set: bright white desk studio by a big window: a large monitor and a second laptop showing code behind him, white shelves with camera lenses and books, a green monstera plant on the right, a laptop lid in the foreground at the bottom of frame. Chest-up, centred, natural daylight.
**Signature:** the dark tee with the chest logo and the bright desk studio. The channel's electric blue lives in the graphics and thumbnails, not on Max. Never change outfit or set without Hammad's OK.
**Reference files:** `max-vids-ref.jpg` (main 16:9 reference, a frame from the first Google Vids clip), `host-hero.jpeg` (face source, old outfit), `host-angles.jpeg` (angles), `host-expressions.jpeg` (surprised / sceptical / laughing), `host-full-body.jpeg` (poses), `host-clip-1.mp4`, `host-clip-2.mp4` (vertical 9:16 test clips). Angles, expressions and clips show the old charcoal-tee look: use them for the face only.

## Personality
Calm, slightly witty builder. Honest about being an AI and about what tools can't do. Says "here's exactly how I did it". Curious, never hype. Tests things for real and shows the result, including failures.
- **Opener (every video):** state the result in the first 5 seconds. No "hey guys", no channel intro.
- **Catchphrase:** "Let's see if it actually works."
- **Sign-off:** "I'm Max. I test AI so you don't waste your time."
- **Never:** fake income claims, hype words ("insane", "game-changer"), pretending to be human, trash-talking other creators, reading a sponsor line without disclosure.

## Voice
**One Google (Gemini) voice everywhere** (Hammad's pick, 2026-11-01): the same voice on Max's Google Vids avatar and on all narration. Voice name: **TBD**. Hammad picks it in Vids with **Select voice** (calm, warm, mid-pitch, American; closest to the old sample `brain/host/voice-sample-michael.mp3`). Once known, write it here and in `scripts/tts.py` `MAX_VOICE`.
Narration: Hammad makes it in one go in the same voice (`voiceover.md` -> `audio/voiceover.mp3`). If the `GEMINI_API_KEY` secret is set, `scripts/tts.py` can make it in the same Gemini voice (`MAX_VOICE`); otherwise Kokoro am_michael is a placeholder for previews only. Never change the voice without Hammad's OK.

## On-screen use
20-30% max: the hook, 1-2 reactions, the outro. Everything else is screen recording + motion graphics.
**Talking clips (hook, reactions, outro): Google Vids custom avatar "Max Reed"** (saved in the Vids file "Max master"; copy it per video). Claude writes `videos/<slug>/vids-scenes.md`; Hammad returns one MP4 per scene (`max-01-hook.mp4` ...), lip-synced in Max's voice. Max 60 s per scene, about 25 generations a month. How-to: `docs/google-vids-max.md`.
**Rare action shots (walking, holding a phone): Google Flow** from `videos/<slug>/flow-prompts.md`, 16:9 for long videos, 9:16 for Shorts, reference image `max-vids-ref.jpg`. Every prompt repeats the locked look line:
> Same man as the reference image: early 30s, short tousled brown hair, light stubble, plain dark charcoal crew-neck tee with a small white logo on the left chest, in a bright white desk studio by a big window, a monitor and laptop showing code behind him, shelves with camera lenses, a green monstera plant. Natural daylight, clean sharp image, no film grain, no colour filter.

## Disclosure
Max looks like a real person, so every upload ticks YouTube's "altered or synthetic content" box, and the channel About page and banner say Max is an AI.

## Watermark
Google Vids/Veo clips carry a small "Veo" mark bottom-right (plus Google's invisible SynthID). Leave it in: never crop, blur or cover it to hide it. Keep captions and graphics clear of that corner.
