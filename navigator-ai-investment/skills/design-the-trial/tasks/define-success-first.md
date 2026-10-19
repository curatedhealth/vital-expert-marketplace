# A Define success before the start

Framework task: 4.3 Trial Design, Part A.

## What this task delivers

The hypothesis, the one measure (name, unit, today's level with source, owner), the target and date set by the owner, the failure signal, the stop rule, the time limit and the exit condition.

Why it matters: a pilot judged after the fact finds a reason to continue. Writing success and failure down first is what makes it a test (method.md X8, X9).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 4.3, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X8, X9, X10) |
| Tools | `scripts/trial_check.py` |
| Template | `assets/trial-design-sheet.md` |
| Input | Option and result; the outcome and its measure |
| Governance | `references/governance.md` |

## Workflow

1. **Check the option qualifies** (X10). If the result is "Handle it internally", there is no AI trial; say so.
2. **Hypothesis** (question 2): one sentence, "if we [change], then [measure] moves from [baseline] toward [target] for [party], without [harm]". Built from the person's words; marked proposed until they accept.
3. **Measure and baseline** (question 3): take the outcome's measure from *Outcome Discovery* if it exists. Baseline with source and date (M), or a gap: a trial without a baseline measures nothing; measuring it becomes the trial's first job.
4. **Target and date** (question 4): the owner's number (O). Never propose one. Check the direction with the script.
5. **Failure signal and stop rule** (questions 5 and 5b): the failure signal is what shows it is not working (judged at the exit); the stop rule is what ends it at once. Add, and say so, the proposed standing rule (pending the owner's ruling): any failure reaching a patient, clinician or regulator stops it; the owner may waive it with a recorded reason.
6. **Time limit and exit condition**: from the person; if not given, ask within question 4's turn as "by when".

## Boundaries

- No benchmark targets; no "typical pilot" figures.
- One success measure. Secondary measures are listed as watched, not as success.

## When you are unsure

If the owner wants "see how it goes", explain in one line that without a target the trial cannot fail and so cannot inform the scale decision, and ask for one number.
