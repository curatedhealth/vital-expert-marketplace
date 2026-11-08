# Task TR-1.1.1 Specificity

## Formula

| Slot | For this task |
|---|---|
| Worker | Senior editor and engagement lead |
| Workflow | Find each generic statement, ask what it would say if it were specific, fill from the material or ask |
| Skill | TR-1.1.1 |
| Knowledge | `references/patterns.md` (V1–V6, P1–P3), `references/rules.md` |
| Tool | `scripts/scan_fluff.py` (vague-word prompts) where code can run. Companion slot: none yet |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/repair-note.md` |
| Input | The request, the draft, the supplied material, the context card from `trusted-intake` |
| Governance | TR-H1, TR-H2, TR-H7, TR-H9 |

## What counts as too vague to act on

A statement the reader cannot act on or check because one of these is missing, and the
work needs it:

- **Who:** "stakeholders", "the team", "key accounts", "partners", "customers" where a
  named group, function or account is meant.
- **What:** "initiatives", "activities", "optimizing the approach", "addressing gaps"
  where a specific action or object is meant.
- **How much:** "significant", "strong", "many", "substantial growth", "improved" where
  a figure, range or count exists or is needed.
- **By when:** "soon", "going forward", "in the near term", "shortly", "in due course"
  where a date, quarter or milestone is meant.
- **Compared with what:** "better", "ahead", "lagging" with no plan, prior period or
  comparator.

Not every statement needs all five. A team email saying "let's meet soon" is fine. Ask
what this reader needs to act.

## Guard (while drafting)

1. **Read the material and the context card.** List the specifics the material holds:
   figures, names, groups, dates, comparators.
2. **Write each point with the specifics the material supports.** "Uptake is strong"
   becomes "12% of new patients in September, up from 10% in July" when the notes say so.
3. **Where the material does not hold the specific and the reader needs it**, write the
   gap where the specific would go: `[GAP: not supplied — owner for the access plan —
   name the person or function]`.
4. **Do not reach for a plausible specific** (`references/patterns.md` P1–P3). A
   typical-looking number, a likely date or an obvious-seeming owner is invented content.
5. **Group the questions.** When several specifics are missing, ask for them in one
   short list rather than one at a time.

## Repair (existing draft)

1. **Find the generic statements.** Read for the five questions above. Where code can
   run, `scripts/scan_fluff.py --json draft.txt` lists vague words as prompts; read each
   sentence, do not count hits as findings.
2. **For each one, decide:** the material holds the specific (fill it from the
   material); the material does not and the reader needs it (gap or question); the
   statement is fine as it is for this reader (leave it).
3. **Fix** by replacing the generic wording with the supplied specific, or by inserting
   the gap. Keep the person's meaning; do not change a claim's strength while making it
   specific.
4. **List every change** in the repair note, including what you left as a gap and why.

## "Make it more concrete"

When the person asks for more concrete wording and supplies no data, do not produce a
more concrete-sounding version with invented figures, names or dates. Return the draft
with gaps where the specifics would go and a short list of what to send: "To make this
concrete I need: the Q3 uptake figure, who owns the payer follow-up, and the target
date for the listing decision." Make concrete what can be made concrete from the
existing text (a named group already mentioned elsewhere, a date already in the notes).

## Check line

Counts feed the substance line in `assets/check-line.md`: statements too vague to act
on.

## Boundaries

- Whether a supplied specific is right is True (`grounded-statements`). This task only
  moves it from the material into the sentence, unchanged.
- Whether the specific is pitched at the reader's level is `fit-for-reader`.
- A generic statement is not a style problem. Leave a vague but harmless phrase alone
  when the reader does not need the specific (TR-H9).
