# Task TR-3.1.1 Fair balance

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical reviewer (an experienced colleague; not the company's medical review) |
| Workflow | Pair every benefit with the risks, discontinuations and limitations the material gives for it; keep them in the same piece with comparable weight; replace reassurance with data |
| Skill | TR-3.1.1 |
| Knowledge | `references/rules.md` (R1, R2, R4, R5, R7, R8, R10), `references/patterns.md` (FB1–FB8) |
| Tool | `scripts/balance_cues.py` where code can run. Companion slot: none yet (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/balance-note.md`, `assets/evidence-inventory.md` |
| Input | The draft or request, the supplied material (label, study, results tables, registry data), the reader, market and use from intake |
| Governance | TR-H1, TR-H3, TR-H6, TR-H7, TR-H11, TR-H12 |

## What counts as the other side

From the supplied material only, for the product, population and use the draft
discusses:

- side effects and adverse events, in each group where there is a comparator
- serious adverse events, deaths, and any warning the label or study puts first
- discontinuation, and discontinuation because of side effects, in each group
- limitations the source states: design (open-label, single-arm, short follow-up),
  population (who was excluded), a primary endpoint that was missed, an effect that
  faded, data still immature
- for a payer or value story: persistence, dropout and the assumptions the value figure
  depends on, where the material gives them

Which of these are material is the medical reviewer's call, not yours (TR-H6). By
default, carry what the source itself puts forward: the label's warnings and most common
side effects, the study's serious adverse events and discontinuations due to adverse
events, and the authors' stated limitations.

## Guard (while drafting)

1. **List the benefit statements the draft will make** and, beside each, the risks,
   discontinuations and limitations the material gives for the same product and use.
   Use the evidence inventory (`assets/evidence-inventory.md`) for anything leaving the
   company.
2. **If the material holds no safety or limitation data**, do not draft a benefits-only
   piece. Ask for the label or results, or leave a visible gap where the risks will go:
   `[GAP: not supplied — side effects and discontinuations for <product, study> — supply
   the label or the safety table]`.
3. **Put the risk with the benefit.** In the body, near the claim it qualifies, in words
   the reader of the benefit will also read. A footnote, an appendix, a back page or "see
   prescribing information" can add detail; it does not replace the main risks in the
   body (R2, R4).
4. **Give comparable depth.** If the benefit has a figure, the main risk has its figure,
   for both groups where the source has both. If the benefit gets a headline, the main
   risk gets more than a fragment in small type.
5. **Say what the data show, not how reassuring they are.** Replace "safe", "well
   tolerated", "no side effects", "favorable safety profile" with the rates. Where the
   source itself uses such a phrase, quote it and attribute it ("the authors described
   it as well tolerated"), and give the figures beside it (R5, R7).
6. **Keep balance inside the piece.** Do not plan safety for "a separate slide deck",
   "the next email" or "the medical team's version". Each piece the reader may see on its
   own carries its own balance.

## Repair (existing draft)

1. **Count.** Where code can run, use `scripts/balance_cues.py draft.txt` to list benefit,
   risk and reassurance wording and benefit lines with no risk nearby. It finds words,
   not meaning: read the whole draft as well.
2. **Pair each benefit** with what the material gives on its risks and limitations.
   Classify: risk present and near; risk present but only in a footnote or another
   piece; risk missing from the draft but in the material; risk data not supplied.
3. **Fix:** add the missing risks and limitations from the material, in plain words and
   with figures; move footnoted main risks into the body; replace reassurance with data;
   leave gaps where the material is missing.
4. **Never delete or soften silently.** Every addition, move and rewording appears in the
   balance note.

## "Keep it positive"

Decline the part that removes or hides risks, in one plain sentence: a reader who later
finds a side effect or a dropout rate that was left out stops trusting the whole piece,
and your review process will ask for it anyway. Then help with what is legitimate: lead
with the best supported benefit, keep the risk wording short and accurate, cut hedging
the material does not require. If "the PI" is meant as the prescribing information, say
that it adds detail but does not take the main risks out of the body. If it means a
principal investigator, the piece still carries its own balance.

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether each statement matches its source is `grounded-statements`. Harms given for one
  arm only is described there; here, the question is whether harms appear at all and with
  comparable weight.
- How a figure is framed (relative only, axes, certainty wording for efficacy) is
  `honest-framing`. Reassuring wording about safety is this task.
- Whether a dose, warning or interaction statement matches the label is
  `patient-safety`. A side effect described in the input about a real patient goes to
  `patient-safety` and your safety reporting procedure.
- Whether the piece meets a code or regulation is for your promotional or medical review
  process. This task says what was added and what is open.
