# A Check the outcomes

Framework task: 5.1 Value Realization, Part A.

## What this task delivers

For each outcome the declared value depends on: the target set before, the measured result with its source, and its status (achieved, not achieved, not measured).

Why it matters: value is proven at the bottom. An output that exists, or a number finance reports, does not show the outcome moved; only the measured result against the target does (method.md L1, L2).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 5.1, Part A |
| Knowledge | `references/method.md` (L1, L2) |
| Tools | `scripts/realization_check.py` |
| Template | "Outcomes" section of the report |
| Input | Outcomes, measures, targets set before |

## Workflow

1. **List the outcomes** the value depends on, with their targets (from discovery or the trial design). A target that was not set before is a gap; never set one now.
2. **Ask for each result** (question 2), then its source (question 3). A result without a source is "not measured".
3. **Compute status** with the script (direction-aware: a "reduce" target is met at or below it). If the direction was not stated, mark the assumed one as proposed and list it as a gap.
4. **Say it plainly**: "writer hours: 195 against a target of 210, achieved (time log, Q3 2027)".

## Boundaries

- Never move a target after the fact. If the person proposes a new target, record it as a new target for the next period, beside the original.
- A partial move toward the target is "not achieved", stated with the numbers.

## When you are unsure

If the outcome had several measures, the measure named at the decision governs; others are reported as watched.
