# B Size and store the trial

Framework task: 4.3 Trial Design, Part B.

## What this task delivers

The trial's worth (the outcome's value range) against its cost to run (a range), a check that the design is complete, and the trial stored on the brief.

Why it matters: a test that can cost more than the worst case it protects is a decision in its own right; the owner should see it before it starts (method.md X8, X12).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 4.3, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X8, X12) |
| Tools | `scripts/trial_check.py`; `trial_note` |
| Template | "Worth and cost" section of the report |
| Input | The design from Part A; the value range |
| Governance | `references/governance.md` |

## Workflow

1. **Value range**: take it from *Value-at-Stake Sizing* (low, likely, high, unit, basis). If none, ask for it in the person's terms; never supply it.
2. **Cost to test** (question 6): low, likely, high, unit, basis, from the person. A point is refused.
3. **Check** with `scripts/trial_check.py`: missing parts, ranges, target direction; it notes when the cost-to-test high end is above the value low end (H). Read the notes to the owner; change nothing.
4. **Store** with `trial_note` if a brief is open: outcome, value, cost to test, measure (name, baseline, owner). The target, stop rule and hypothesis stay in the report; say so.
5. **After the trial** (if the person brings a result): place it against the target ("target reached" or "not reached") and hand it to the owner for *Value Realization*. Never call it a success.

## Boundaries

- The script's cost-versus-value note is a reading, not a verdict.
- Never store a trial with a missing measure owner or baseline; the tool refuses it, and the report names the gap.

## When you are unsure

If value and cost are in different currencies or measures, ask the person to express both in one unit before reading the trade-off. A per-year value against a one-off cost may be read directly, saying so.
