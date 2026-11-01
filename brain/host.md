# Max Reed: character bible

**Who:** Max Reed, the host of Max Tests AI. A realistic AI character, openly an AI ("Max here. Yes, I'm an AI."). Looks early-to-mid 30s.
**Look (locked 2026-11-01, Hammad, v3):** same face as `brain/host/max-vids-ref.jpg`: short tousled brown hair, light stubble beard, warm smile. Wears a **plain black crew-neck T-shirt with no logo, print or text**. Set: **modern YouTube tech studio**: light-grey acoustic panels, a soft electric-blue (#2F6BFF) LED strip along the wall, a small shelf with a plant out of focus, white desk with a silver laptop, and a **black podcast mic on a boom arm** in front of him, below and to one side of his mouth (lips always visible). Reference: `brain/host/studio-ref.jpg` (to add once made).
**Signature:** plain black tee, the podcast mic and the blue LED glow. Never change outfit or set without Hammad's OK.
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
Full screen: the hook, reactions, verdict and outro. Over screen recordings, Max also appears **in a corner bubble** at the start of each chapter (Hammad, 2026-11-01): a 16:9 rounded box, bottom-left, about 28% of the frame width, 24 px margin, 2 px electric-blue (#2F6BFF) border and a soft shadow. The move from full screen to the bubble is a 0.6 s spring scale-and-slide (and the reverse when he comes back full screen). Never crop out the "Veo" mark, so the bubble is never a circle. Everything else is screen recording + motion graphics.
**Acting standard (every clip):** human, not a mannequin: natural blinking, eye contact with small glances away, clear lip sync, hand gestures that match the words, changing expressions, conversational American delivery with small pauses. Each clip prompt = the Direction block + Framing block in `vids-scenes.md` + action + line. Max 8 s per clip.
**Talking clips (hook, reactions, outro): Google Vids custom avatar "Max Reed"** (saved in the Vids file "Max master"; copy it per video). Claude writes `videos/<slug>/vids-scenes.md`; Hammad returns one MP4 per scene (`max-01-hook.mp4` ...), lip-synced in Max's voice. Max 60 s per scene, about 25 generations a month. How-to: `docs/google-vids-max.md`.
**Rare action shots (walking, holding a phone): Google Flow** from `videos/<slug>/flow-prompts.md`, 16:9 for long videos, 9:16 for Shorts, reference image `max-vids-ref.jpg`. Every prompt repeats the locked look line:
> Same man as the reference image: early 30s, short tousled brown hair, light stubble, plain black crew-neck T-shirt with no logo, in a modern tech studio with light-grey acoustic panels, a soft electric-blue LED strip on the wall, a white desk with a silver laptop and a black podcast mic on a boom arm in front of him. Clean sharp image, no film grain, no colour filter.

## Disclosure
Max looks like a real person, so every upload ticks YouTube's "altered or synthetic content" box, and the channel About page and banner say Max is an AI.

## Watermark
Google Vids/Veo clips carry a small "Veo" mark bottom-right (plus Google's invisible SynthID). Leave it in: never crop, blur or cover it to hide it. Keep captions and graphics clear of that corner.
