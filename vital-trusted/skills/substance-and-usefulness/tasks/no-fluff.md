# Task TR-1.1.2 No fluff

## Formula

| Slot | For this task |
|---|---|
| Worker | Senior editor and engagement lead |
| Workflow | Find filler, buzzwords, padding, repetition and throat-clearing; cut or replace with what the sentence was trying to say |
| Skill | TR-1.1.2 |
| Knowledge | `references/patterns.md` (L1–L7) |
| Tool | `scripts/scan_fluff.py` where code can run. Companion slot: none yet |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/repair-note.md` |
| Input | The draft, the context card |
| Governance | TR-H1, TR-H3, TR-H9 |

## What counts as fluff

- **Buzzwords that replace a meaning:** "leverage", "synergies", "holistic", "robust",
  "landscape", "ecosystem", "unlock value", "drive engagement", "best practices",
  "value-add", "paradigm shift", "move the needle", "end-to-end".
- **Throat-clearing openings:** "In today's rapidly evolving healthcare landscape…", "It
  is important to note that…", "As we all know…", "This document aims to provide an
  overview of…".
- **Padding:** sentences that restate the heading, summarize what is about to be said,
  or announce that the point is important.
- **The same point twice:** a point made in the summary, again in the body and again in
  the close, with no new information; two bullets that say the same thing in different
  words.
- **Stacked hedges:** "may potentially help to somewhat improve", where the material
  supports one plain qualifier.

## When a listed word is not fluff

A word on the list carries meaning in some uses. "Robust" in "robust to sensitivity
analyses" is a statistical term. "Competitive landscape" as the title of a slide that
then lists named competitors is a label. "Ecosystem" may name a real set of partners.
Ask: if this word were removed, would the reader lose information? If yes, keep it.

## Guard (while drafting)

1. **Open on the point.** The first sentence says what the reader most needs, not what
   the document is about.
2. **One point, one place.** Make each point once, where it does the most work. A
   summary may repeat a point only when it is a genuine summary of a long document.
3. **Replace each buzzword with what it stands for**, from the material: "leverage our
   field team" becomes "ask the two key account managers in canton X to…" if the notes
   say so; otherwise the sentence goes, or becomes a gap if the action is needed.
4. **Keep the qualifiers the material requires.** Cutting fluff never removes a
   limitation, a "forecast" label or a hedge the evidence needs; those are True and
   Unbiased.

## Repair (existing draft)

1. **Scan.** Where code can run: `python scripts/scan_fluff.py draft.txt`. It lists
   buzzword hits, throat-clearing openers, stacked hedges and near-duplicate sentences
   with line numbers. Read each hit in context.
2. **For each passage, decide:** cut (it says nothing); replace (it stands for something
   the material names); merge (it repeats a point); keep (it carries meaning).
3. **Fix.** When a buzzword stood for something specific that the material does not
   hold, do not guess it: cut the sentence, or keep the intent with a gap if the reader
   needs it.
4. **Report the cuts** in the repair note as a count and the main examples, not a list
   of every word. Never delete a figure, a qualifier, a source or a risk while cutting.

## Check line

Counts feed the substance line in `assets/check-line.md`: passages of filler or
repetition.

## Boundaries

- This is not a word-count exercise. A long draft that says something useful in every
  paragraph is not fluff; length for the deliverable is `fit-for-reader`.
- Tone, voice and house style are out of scope (TR-H9). "We are delighted" in a partner
  email is a tone choice, not fluff, unless it displaces the content.
- Superlatives such as "best-in-class" or "leading" are also claims. Cut them here if
  they carry no meaning, and leave the claim question to True and Rule-compliant.
