# B Score current and required

Framework task: 3.1 Strategic Readiness, Part B.

## What this task delivers

Every named scorer's Current and Required score, 1 to 10, for every capability, given alone before discussion; computed into each capability's gap and outcome-weighted gap.

Why it matters: the gap is only honest if people say where they are before hearing where the boss thinks they are. Weighting by outcomes keeps the room from fixing the gap that is easiest to see rather than the one that holds back what matters (method.md I3, I5).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 3.1 Strategic Readiness, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (I3, I5) |
| Tools | `scripts/readiness_check.py` |
| Prompt | This guide |
| Template | `assets/capability-score-sheet.md` |
| Input | Capabilities and their outcome links (Part A); attested opportunity scores |
| Governance | `references/governance.md` |

## Workflow

1. **Name the scorers** in one question, with the sheet. People who know the work and people who own the outcomes; the owner scores too.
2. **Send the sheet** ([assets/capability-score-sheet.md](../assets/capability-score-sheet.md)); returned privately; revealed together.
3. **Check the set**: every scorer, both criteria, every capability, whole numbers 1 to 10. A missing cell is not filled; ask once or compute without that scorer, named.
4. **Compute** with `scripts/readiness_check.py`: capabilities, scores, the attested outcome scores, the links, the owner's id. Do not use the connector's gap tool for this; it weights every capability 1. If priorities are not attested, or the person gives outcome scores without saying they were attested, use them as given (O) and label the weights "provisional". Show an owner's view only when the owner is named among the scorers.
5. **Show the group's register first**, the owner's after.

## Boundaries

- Never score or suggest a score.
- A direct weight on a capability (instead of the outcome cascade) needs the owner's reason, recorded.

## When you are unsure

If only one person scores, the result is indicative; say so and continue.
