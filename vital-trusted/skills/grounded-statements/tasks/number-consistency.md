# Task TR-5.1.2 Number consistency

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | List every figure, match it to its source, check arithmetic and expression |
| Skill | TR-5.1.2 |
| Knowledge | `references/method-standards.md` / `references/knowledge.md` (R1–R3), `references/failure-modes.md` / `references/knowledge.md` (N1–N8, B1–B6) |
| Tool | `scripts/extract_numbers.py`, `scripts/risk_metrics.py` where code can run. Companion slot: VERIFY `check_claim` via `claim-assessment` |
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
   comparable (quarter with quarter, year to date with year to date). Say percentage
   points for changes in share ("share rose 2 percentage points, from 10% to 12%", which
   is a 20% relative rise). Keep currency and units consistent. Totals should add up to
   their parts, or say why not (rounding).
3. **For comparative binary outcomes, give both absolute and relative effects** where
   the material provides the arm rates, with the comparator's rate. If only a relative
   figure is supplied, state it as relative and mark the absolute as a gap
   (`references/method-standards.md` / `references/knowledge.md` R1, R2).
4. **Say percentage points for differences between percentages.** 20% to 10% is a 10
   percentage point reduction and a 50% relative reduction.
5. **Keep precision honest.** Do not add decimals the source does not have, and do not
   round in a direction that flatters the result.
6. **Compute only from supplied values**, and show the inputs. A derived figure (for
   example an NNT) is labeled as derived, with its inputs, so a reviewer can redo it.

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
   denominator); convert "% reduction" to percentage points where it describes an
   absolute difference; add the absolute figure where the material supports it; mark the
   rest as gaps.

## Check line

See `templates/check-line.md`.

## Boundaries

- Do not recalculate a statistic the source reports from its own model (for example an
  adjusted hazard ratio) from raw counts and present yours as a correction. Raw and
  adjusted figures differ for legitimate reasons. Flag a mismatch and ask.
- Do not judge whether an effect is clinically meaningful; that is the reviewer's call.

## Execution card

- Input: prior task output or intake pack
- Atom: (none unless named)
- Tool: skill scripts and/or plugin `tools/` as listed in references/tools.md
- Template: files under `templates/`
- Output: this task's deliverable only
- Check: required fields present; no invented figures; check-line stamped
- Human: gates in governance.md if this task surfaces a release decision
