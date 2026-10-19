# B Score the options

Framework task: 3.2 Option Comparison, Part B.

## What this task delivers

Every named scorer's scores, 1 to 10, on the six criteria for every option and both baselines, given alone before discussion; computed into composites, the ranking among options, each option's distance from each reference line, the owner's view and the sensitivity check.

Why it matters: options are where advocacy is loudest. Private scores with equal weight, and a test of whether the leader survives one scorer leaving or a weight moving, keep the choice about the options rather than the room (method.md I3, I7).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 3.2 Option Comparison, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (I3, I7) |
| Tools | `methods_nav_compute` (`nav.options`); `scripts/options_check.py` |
| Prompt | This guide |
| Template | `assets/option-score-sheet.md` |
| Input | The shortlist (Part A) |
| Governance | `references/governance.md` |

## Workflow

1. **Name the scorers** in one question, with the sheet. The owner scores too.
2. **Send the sheet** ([assets/option-score-sheet.md](../assets/option-score-sheet.md)): baselines included, scored like the rest.
3. **Check the set**: every scorer, six criteria, every option and baseline, whole numbers 1 to 10. Nothing filled in.
4. **Compute.** With the connector: `methods_nav_compute`, template `nav.options`, both baselines flagged `is_baseline`. Locally: `scripts/options_check.py`, which gives the same composites and also re-reads the leader among options only. Use the script's presentation either way.
5. **Weights stay equal** unless the room asks to change one; then record the criterion, new weight and reason, and show the unadjusted result beside it. Never suggest a weight change to move the result.
6. **Show the group's result first**, the owner's after.

## Boundaries

- Never score, suggest a score, or "complete" a sheet.
- The baselines are scored, not assumed: doing nothing has a risk of its own.

## When you are unsure

If people ask what a criterion means, read the anchors on the sheet; do not add examples that lean toward an option.
