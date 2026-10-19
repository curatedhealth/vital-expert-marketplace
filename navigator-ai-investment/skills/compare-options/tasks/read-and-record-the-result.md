# C Read and record the result

Framework task: 3.2 Option Comparison, Part C.

## What this task delivers

Decision Record sections 5 and 6: the options considered with their scores against the reference lines, where the room split, whether the ranking holds, the owner's view; then the owner's result (Proceed, Investigate first or Handle it internally), the option it applies to, and the route (what happens next).

Why it matters: the owner must see the trade-off, not a winner. "The calculator does not choose the result" (method.md I2).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 3.2 Option Comparison, Part C |
| Workflow | The steps below |
| Knowledge | `references/method.md` (I2, I3, I7, I10) |
| Tools | The result of Part B; `decide_run_stage` if a brief is open |
| Prompt | This guide |
| Template | `assets/options-report.md` |
| Input | The computed result |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Show the ranking against the reference lines

| Rank | Option | Outcome fit | Cost | Time | Reversibility | Risk | Governance burden | Composite | Against do nothing | Against do it internally |
|---|---|---|---|---|---|---|---|---|---|---|

Baselines appear below as reference rows. Group averages, computed, scored in the room.

### Step 2. Read the trade-off

For each option, one line: where it wins (usually outcome fit) and where it pays (cost, time, risk, burden). Every "best", "leads", "heaviest" or "most" claim is checked against all rows, reference lines included; the script prints the best and worst row per criterion. If an option sits below doing nothing, say which criteria carry doing nothing (it is cheap, fast and reversible by construction) and what the option buys on outcome fit. If no option clears both reference lines, say so plainly; it is a finding, not a failure.

### Step 3. Disagreement and sensitivity

Spread of 3 or more on any criterion: name both ends, ask the minority holder for one line (session question 5), record it. Sensitivity: what was tested (each scorer left out; each weight down and up 20%), whether the leader changed, and whether any option crosses a reference line (from above to below doing nothing or doing it internally, or the reverse). With one option there is no leader to change; report only the crossings. Ties named as ties.

### Step 4. The owner's view, after

The owner's own ranking, where it differs. Not reconciled.

### Step 5. The owner's result

Ask the owner once: "Which result do you choose: Proceed, Investigate first or Handle it internally, and with which option?" Record exactly one of the three, the option, the owner's reason in their words and the route (next step and who leads it). If the owner is absent: "Result pending: [owner]", with the question. Never preselect.

### Step 6. Hand on

Carry the options (not the baselines) with their outcome fit and governance burden to *Portfolio Placement*. Each option's AI involvement level stays open for the process owner.

## Boundaries

- No "the clear winner", "we recommend". The ranking informs; the owner chooses.
- Gate 3 (the record signed by two people, one the owner) is taken when the record is completed, not here.

## When you are unsure

If the owner asks what you would choose, say the result is theirs and offer the one-line trade-off for each option instead.
