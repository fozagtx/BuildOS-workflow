---
name: script-forensics
description: Forensic cleanup gate for scripts. Use this skill whenever the user asks to audit, clean, de-slop, de-repeat, tighten, polish, or prepare a YouTube script, content script, voiceover, VSL, narration, hook, intro, outline, or transcript before it moves to thumbnails, voiceover, captions, image prompts, or media production. It finds and removes useless repetition, repeated sentence shapes, repeated beats, filler loops, and AI-slop contrast patterns like "not just X, but Y", "it is not X, it is Y", and "more than just X".
---

# Script Forensics

Use this as a cleanup gate before a script moves to another stage. The job is not to make the writing prettier. The job is to protect the video from viewer complaints caused by repetition, filler, and recognizable AI-shaped phrasing.

## What To Kill

Remove or rewrite:

- Repeated phrases that do not add new information.
- Repeated sentence openings.
- Repeated emotional beats.
- Repeated explanations of the same point.
- Repeated hook language in later sections.
- Repeated character labels when names or pronouns would be cleaner.
- Filler summary loops.
- Over-explaining after the point has landed.
- AI-slop contrast templates.

## Banned Contrast Patterns

These patterns are usually lazy and should be rewritten unless the contrast is genuinely necessary:

- `not just X, but Y`
- `not only X, but Y`
- `it is not X, it is Y`
- `this is not X, this is Y`
- `more than just X`
- `not merely X`
- `it is not about X, it is about Y`
- `it is not a story about X, it is a story about Y`
- `not just a X, but a Y`
- `not because X, but because Y`

Preferred fixes:

- State the stronger idea directly.
- Use a fresh concrete image.
- Cut the first half if it only delays the point.
- Turn the contrast into cause and effect.
- Replace abstract contrast with a specific action, consequence, or scene.

Example:

```text
Weak: This is not just a betrayal. It is a warning.
Better: The betrayal works because it arrives as a warning.
Cleaner: The betrayal is the warning.
```

## Forensic Workflow

1. Read the script or outline.
2. Run `scripts/forensic_scan.py` when text is available in a file, or manually scan if the text is only in chat.
3. Identify:
   - repeated phrases,
   - repeated sentence starts,
   - repeated structure,
   - repeated ideas,
   - banned contrast patterns.
4. Produce a short forensic report.
5. Rewrite the affected sections.
6. Run a final pass and confirm the script is cleaner.

## Report Format

Use this when auditing or cleaning an existing script:

```text
FORENSIC REPORT

Major repetition:
- <phrase or idea> appears <count> times. Fix: <cut/merge/rewrite>.

AI-slop contrast:
- "<quoted line>" -> <rewrite>.

Structural loops:
- <section> repeats the same beat as <section>. Fix: <new beat or cut>.

CLEANED SCRIPT
<script>

FINAL CHECK
- Repetition reduced:
- Contrast slop removed:
- Meaning preserved:
- Pacing improved:
```

If the user only wants the cleaned script, keep the report short and put the cleaned script first.

## Editing Rules

- Do not flatten the user's voice.
- Do not remove intentional motifs, callbacks, or rhythmic repetition that clearly serves a purpose.
- Do remove repetition that exists because the draft is circling the same idea.
- Preserve facts, names, chronology, and core story beats.
- When cutting repeated text, make the remaining line stronger instead of leaving a hole.
- If a section repeats an earlier section, either escalate the stakes, add new information, or delete it.
- Never send a script to voiceover, captions, thumbnail prompts, image prompts, or media generation until this pass is complete.
