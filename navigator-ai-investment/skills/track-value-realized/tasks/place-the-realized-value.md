# B Place the realized value

Framework task: 5.1 Value Realization, Part B.

## What this task delivers

The realized figure (measured, sourced, in the range's unit and period), whether it counts (only if every outcome it depends on is achieved), its place against the declared range, and what else changed that could explain it.

Why it matters: the decision declared a range; the organization learns only if it compares like with like and sees what else moved (method.md L3, L4, L5).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 5.1, Part B |
| Knowledge | `references/method.md` (L3 to L5) |
| Tools | `scripts/realization_check.py`; `realized_value` |
| Template | `assets/realization-report.md` |
| Input | Declared range; outcome statuses (Part A) |

## Workflow

1. **Ask for the realized figure** (question 4), as measured, with source, date, unit and period. An estimate is recorded as an estimate and not counted.
2. **Check and place** with the script. If any outcome is not achieved: "not counted (unmet realizes zero); measured figure [x] shown for reference". Otherwise below, inside or above. Never describe where a not-counted figure would sit against the range.
3. **Store** with `realized_value` only a counted figure, if a brief is open.
4. **What else changed** (question 5): other programs, market shifts, staffing, seasonality, in the person's words (O).
5. **Hand on** to *Portfolio Review*: the outcome statuses and the placement.

## Boundaries

- No "success", "paid off" or "proven".
- No re-forecast of the range here; a new range is a new decision.

## When you are unsure

If the realized figure is per quarter and the range per year, ask which period to compare; do not annualize yourself.
