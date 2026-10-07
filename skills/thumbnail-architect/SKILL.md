---
name: thumbnail-architect
description: High-CTR YouTube thumbnail strategy and generation prompt workflow. Use this skill whenever the user asks for YouTube thumbnail ideas, thumbnail prompts, CTR thumbnails, mobile-readable thumbnails, 1280x720 artwork, title-to-thumbnail concepts, or 5 thumbnail concepts. Especially use it for story channels, Afro-Korean mafia romance/drama, faceless narration, revenge stories, betrayal hooks, documentary thumbnails, and any niche where the thumbnail must stop scrolling. Outputs 5 concepts, chooses the strongest, and prepares AI33 Pro image-generation prompts.
---

# Thumbnail Architect

Use this skill to create high-click YouTube thumbnails that read on mobile. The goal is not pretty poster art. The goal is an image a viewer understands in less than one second.

## Mandatory Checks

Before writing thumbnail concepts or prompts:

1. Identify the niche and emotional click trigger.
2. Run the blocked-name pass if this is connected to YouTube Content Studio.
3. Avoid copied thumbnail layouts from a single source video. Use genre patterns, not clones.
4. Keep text to 3-6 words.
5. Design for phone size first.
6. Avoid clutter. One main emotion, one core clue, one text hook.

## Output: 5 Concepts

When the user asks for thumbnail ideas, produce exactly 5 concepts:

```text
CONCEPT 1 - <name>
Text: "<3-6 word hook>"
Visual: <main face/object/composition>
CTR trigger: <betrayal, secret, danger, proof, transformation, money, shock>
Color contrast: <specific palette>
Why it clicks: <one sentence>
AI33 Pro prompt: <ready prompt>
```

After the 5 concepts, recommend the strongest concept and explain why in one sentence.

## High-CTR Formula

Use this structure for most thumbnails:

- Dominant expressive face or unmistakable object.
- Clear power imbalance or emotional contradiction.
- One concrete clue: document, ring, suitcase, phone, pregnancy test, blood test, deportation paper, broken contract, hidden photo, bank alert.
- 3-6 word text overlay.
- High contrast text: white or yellow fill, thick black outline, subtle shadow.
- Red arrow/circle only when it points to a specific clue. Do not use arrows as decoration.

## Afro-Korean Mafia Romance / Drama Formula

For this niche, prioritize:

- One Black woman face with strong emotion: fear, betrayal, controlled rage, tears held back.
- One Korean mafia boss or power figure in black suit, visually distinct from other Korean male characters.
- One simple story clue: deportation paper, child's birthmark, blue suitcase, wedding ring, phone message, court stamp.
- Soap-opera clarity over cinematic subtlety.
- Text like: `HE SIGNED IT`, `SECRET CHILD`, `DEPORTED HER`, `DNA SHOCK`, `SHE VANISHED`.

Avoid:

- Too many characters.
- Twin-like faces.
- Tiny unreadable documents.
- Long sentence text.
- Random luxury background that competes with the faces.
- Purple generic gradients.
- Fake UI text that the model may misspell.

## Exact Generation Prompt Template

Use this prompt structure for AI33 Pro image generation:

```text
Create a professional ultra high-CTR YouTube thumbnail, exact 1280x720 composition, 16:9 landscape, mobile-first readability.

Niche: <niche>
Video title: <title>

Main visual: <dominant subject and emotion>
Secondary visual: <supporting subject or clue>
Thumbnail text: "<3-6 words>"

Composition:
- <left/right/center layout>
- large expressive face occupying 35-50 percent of frame
- one concrete clue enlarged and easy to understand
- leave clean space for text

Style:
High-contrast cinematic YouTube drama thumbnail, vibrant but controlled colors, sharp facial detail, dramatic rim lighting, premium story-channel look, bold large sans-serif text with white or yellow fill, thick black outline, subtle shadow, readable at phone size. Human faces must have realistic, tactile skin texture, not plasticky AI smoothness.

Anti-plastic facial texture:
Visible vellus hair and peach fuzz catching light along the jawline, cheek, temple, and forehead. Real pores, visible skin grain, subtle stochastic micro-texture, natural melanin variance, small tone mottling, slight redness around the nose where appropriate, natural oil sheen on nose and forehead, faint capillaries in the sclera, wet reflective lower waterline, complex iris striations, and lips with natural vertical lines or light dryness instead of smooth plastic.

Character locks:
<include character lock details from the project>

Negative prompt:
No duplicated faces, no twin-like characters, no cloned people, no extra limbs, no distorted hands, no tiny unreadable text, no misspelled text, no fake logos, no gore, no explicit sexuality, no clutter, no generic stock photo look, no cartoon style, no smooth wax skin, no airbrushed poreless face, no glossy mannequin face, no doll-like skin, no beauty-filter plastic texture. Skin must show pores, visible grain, vellus hair, melanin variance, subtle capillaries, realistic eye moisture, iris texture, and natural lip lines.
```

For thumbnail concepts with close-up faces, include the anti-plastic facial texture block in the AI33 Pro prompt. Keep it after the style section so it strengthens realism without crowding the visual concept.

## AI33 Pro Model Policy

Use AI33 Pro for generation:

Primary image model:

- `gemini-3-pro-image-preview`

Fallback image model:

- `gpt-image-2`

Use 16:9 aspect ratio. Generate at 2K or 4K when possible, then crop/resize/export to exact 1280x720 for the final thumbnail.

## Final Thumbnail Review

Before accepting a thumbnail:

- Text readable at phone size.
- One obvious emotion.
- One obvious clue.
- Faces do not look duplicated.
- The image still works if shrunk to 10 percent.
- No blocked names or disallowed terms.
- No copied composition from one source reference.
