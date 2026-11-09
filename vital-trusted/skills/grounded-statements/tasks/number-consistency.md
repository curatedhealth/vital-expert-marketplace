# Task TR-5.1.2 Number consistency

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | List every figure, match it to its source, check arithmetic and expression |
| Skill | TR-5.1.2 |
| Knowledge | `references/rules.md` (R1–R3), `references/patterns.md` (N1–N8, B1–B6) |
| Tool | `scripts/extract_numbers.py`, `scripts/risk_metrics.py` where code can run. `claim-assessment` compares claims with passages by hand |
| Prompt | This guide |
| Template | `templates/check-line.md`, `templates/repair-note.md` |
| Input | The draft and the supplied material (papers, reports, sales or finance data, notes) |
| Governance | TR-H1, TR-H3, TR-H7 |

## Guard (while drafting)

1. **Carry the frame with the number.** Every figure travels with what it describes:
   who or what, which period, out of how many, and the unit. "38%" alone is not a fact;
   "38% of patients in the treatment arm at week 24" or "net sales of CHF 4.2 million in
   Q3, 38% above Q3 last year" is.
2. **Business figures.** Keep actual, plan and forecast apart and labeled. Keep periods
   comparable (quarter with quarter, year to date with year to date). Give a change in
   share as the two figures ("share rose from 10% to 12%"), never as a percent change
   ("grew 20%"). If the person asks for the change, say it in percentage points, labeled
   as calculated from the two figures they supplied. Keep currency and units consistent. Totals should add up to
   their parts, or say why not (rounding).
3. **For comparative binary outcomes, give both arm rates** where the material provides
   them, with the comparator's rate, and any relative figure as the source reports it.
   If only a relative figure is supplied, state it as relative and mark the arm rates as
   a gap (`references/rules.md` R1, R2). Offer the difference between the rates; add it
   only if the person asks, labeled "calculated from the two figures you supplied".
4. **Use percentage points for any difference between percentages you are asked to
   give.** 20% to 10% is a 10 percentage point reduction, not a 10% reduction.
5. **Keep precision honest.** Do not add decimals the source does not have, and do not
   round in a direction that flatters the result.
6. **Compute only when asked, and only from supplied values.** A derived figure (for
   example an NNT) is labeled "calculated from the two figures you supplied", with its
   inputs, so a reviewer can redo it. Arithmetic on three or more supplied figures (a
   total, an average) is labeled "calculated from the figures you supplied". A label
   alone never makes an unrequested figure acceptable.

## Repair (existing draft)

1. **List every number** with its context. Where code can run, use
   `scripts/extract_numbers.py <draft.txt>`; otherwise make the list by hand.
2. **Match each to the source** and record: matches; differs; not in the material.
3. **Check internal consistency:** the same quantity stated twice with different values;
   subgroup counts that exceed the total; percentages that do not match their counts;
   time units that change between sections.
4. **Check comparative figures.** Where arm rates or counts are supplied, run
   `scripts/risk_metrics.py` (or do the arithmetic and show it) and compare against the
   draft's RR, RRR, ARR or NNT.
5. **Fix:** restore source values; add the missing frame (population, timepoint,
   denominator); where "% reduction" describes a difference between two percentages,
   replace it with both rates; add the arm rates where the material supplies them; offer
   any difference in points rather than adding it; mark the rest as gaps.

## Check line

See `templates/check-line.md`.

## Boundaries

- Do not recalculate a statistic the source reports from its own model (for example an
  adjusted hazard ratio) from raw counts and present yours as a correction. Raw and
  adjusted figures differ for legitimate reasons. Flag a mismatch and ask.
- Do not judge whether an effect is clinically meaningful; that is the reviewer's call.
