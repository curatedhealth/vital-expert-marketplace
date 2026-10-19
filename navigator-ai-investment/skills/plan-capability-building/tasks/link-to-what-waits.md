# B Link the plan to what waits for it

Framework task: 4.2 Capability Build Planning, Part B.

## What this task delivers

The options and delivery steps that wait for each gap to close; gaps deliberately deferred, with reasons; and flags where an option needs a gap nobody plans to close.

Why it matters: "Build the basis first" only means something if the basis is planned. Linking each waiting option to a planned action makes the dependency visible to the owner (method.md X11).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 4.2, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X11) |
| Tools | `scripts/build_plan_check.py` |
| Template | "What waits" section of the report |
| Input | Plans from Part A; options and the gaps they need; delivery steps |
| Governance | `references/governance.md` |

## Workflow

1. **Link** each option's "needs closed first" gaps (from *Option Comparison*) and any delivery step that depends on a capability.
2. **Ask about deferrals** (question 5): a gap the owner chooses not to close now, with a reason in their words.
3. **Check** with the script: waiting options on unplanned gaps; top gaps with neither plan nor deferral.
4. **Hand on**: actions with owners and dates to the delivery plan as jobs, if the person wants them sequenced.

## Boundaries

- Deferral is the owner's choice; never suggest dropping a gap.

## When you are unsure

If no option waits on a top gap, say so: the gap matters to outcomes, but this decision does not depend on closing it.
