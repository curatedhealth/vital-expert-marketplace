# Task TR-4.1.1 Clinical safety statements (Part A, content)

## Formula

| Slot | For this task |
|---|---|
| Worker | Drug safety physician who supports colleagues |
| Workflow | Find each safety statement in the supplied label; quote it word for word with its section, market and date; keep its conditions; gap the rest |
| Skill | TR-4.1.1 |
| Knowledge | `references/rules.md` (S10 to S12), `references/patterns.md` (C1 to C10) |
| Tool | `scripts/label_match.py` where code can run. Companion slot: label source (none yet) |
| Prompt | This guide |
| Template | `assets/label-statements.md`, `assets/repair-note.md`, `assets/check-line.md` |
| Input | The draft or request, the supplied label (SmPC, prescribing information, package leaflet, instructions for use) and the market from intake |
| Governance | TR-H1, TR-H6, TR-H7, TR-H8, TR-H11 |

## What counts as a safety statement

Any sentence, table cell, bullet or chart label about:

- dose, how to take or give it, how long, missed doses, stopping;
- contraindications (who must not use it);
- warnings and precautions, including any boxed warning;
- interactions with other medicines, food or drink;
- special populations: pregnancy, breastfeeding, fertility and contraception, children,
  the elderly, kidney or liver impairment, a genotype;
- side effects as the label lists them, and their frequency.

## Which label

- **The supplied label only.** Pasted text, an attached file, or a page the person gave.
  Your memory is not a label, even for a product you think you know.
- **The right market.** The label for the market the work is for (from intake or the
  person). Another country's label is not used for this market; say so and ask
  (`claims-and-label` owns the wider label boundary).
- **Dated.** Note the label's revision date if it shows one. If none shows,
  `[GAP: out of date or unclear date — label revision date — confirm this is the current
  approved label]`.
- **The right reader.** For a patient, the patient leaflet is the label to quote where it
  was supplied; for a doctor, the SmPC or prescribing information.

## Guard (while drafting)

1. **If no label was supplied, do not draft safety content.** Ask for it in one line:
   "Please paste or attach the current approved label for <market> so I can quote it."
   If the person wants to go on, give the structure with every safety cell as
   `[GAP: not supplied — <what> — from section <n> of the approved label]`.
2. **Find the section first** (`references/rules.md` S11 for EU, S12 for US) and quote
   the statement word for word, in quotation marks or as a table cell marked as label
   text, with the section number.
3. **Keep every condition.** Population, cut-off, timing, route, formulation, "in
   combination with". If the label says "creatinine clearance 30 to 50 mL/min", the draft
   says that, not "kidney problems".
4. **Do not fill silence.** If the label does not address a population or interaction,
   do not write that there is no risk or no need to adjust. Write what the label says,
   or `[GAP: not supplied — label does not address <x> in the supplied text — ask your
   medical information function]` when the full label was read; `not supplied` when only
   part was given.
5. **Do not answer for a patient.** A doctor asking "can my patient with X take it"
   gets the label's statements on X, quoted, and no recommendation. The decision is the
   prescriber's (TR-H6).
6. **No rounding, converting or merging.** Units, frequencies and doses stay as the label
   gives them. Do not convert mg/kg to a fixed dose, or combine two sections into one
   sentence that neither says.

## Repair (existing draft)

1. **List every safety statement** in the draft. Where code can run,
   `scripts/label_match.py <label.txt> <draft.txt>` lists them with the closest label
   sentence and any numbers that differ.
2. **Classify each:** word for word from the label; reworded but same meaning; changed
   (a number, condition, population or strength of wording differs); broader than the
   label (generalized); not in the supplied label; from another market's label.
3. **Fix:** restore the exact label wording for changed, broader and reworded statements
   in material for professionals. For patient material, use the patient leaflet's wording
   if supplied; otherwise keep the label wording and mark the passage for your medical
   review. Replace statements not in the label with a gap. Never delete a warning
   silently.
4. **Note each change** in `assets/repair-note.md`, in plain words.

## Check line

See `assets/check-line.md`.

## Boundaries

- Do not judge whether a statement is clinically right, only whether it matches the
  supplied label.
- Do not decide whether a use is within the approved indication; that is
  `claims-and-label`.
- Do not judge whether benefits and risks are shown in proportion; that is
  `balanced-evidence`.
- A match to the label is not a statement that the content is safe or approved (TR-H3).
