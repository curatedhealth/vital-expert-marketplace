# A Sequence the jobs

Framework task: 4.1 Delivery and Oversight Planning, Part A.

## What this task delivers

The jobs that deliver the chosen option, each ending at a review, each with the capability it needs, what it waits for, and the capacity people state for it; in a valid order.

Why it matters: a plan whose steps have no gates cannot be overseen, and a plan with assumed capacity fails on the first busy month (method.md X1, X2, X7).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 4.1, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X1, X2, X7) |
| Tools | `scripts/delivery_check.py`; `sequence_check` to store |
| Template | "Jobs and order" section of the report |
| Input | The owner's result and option; capability gaps it needs closed |
| Governance | `references/governance.md` |

## Workflow

1. **Ask for the jobs** (question 2). Word each as what is delivered, ending at a review: "Tagged label-update content, reviewed on a sample". A job that is really a gap to close (from *Strategic Readiness*) comes first or goes to *Capability Build Planning*.
2. **Name the capability for each job**, before any role or agent type. If the person gives none, propose one from the job's wording, marked proposed. Restate a role named first: "content operations analyst" becomes the capability "structured content data and tagging", performed by that role.
3. **Ask what each job waits for** (question 3). Several predecessors are fine.
4. **Ask for capacity** (question 4): a role and share of time, or agent runs per period. Never fill it.
5. **Check** with `scripts/delivery_check.py`: missing predecessors, cycles, no capacity, performer before capability. Show the order.
6. **Store** with `sequence_check` if a brief is open: steps in the script's order; one dependency per step (the last predecessor); the report lists the rest.

## Boundaries

- No dates or durations you supply; any the person gives are theirs.
- No ranking of jobs by value; the order comes from dependencies.

## When you are unsure

If the person describes a project plan with dozens of tasks, ask them to group it into jobs that each end at a review; aim for 3 to 8 [H, skill practice].
