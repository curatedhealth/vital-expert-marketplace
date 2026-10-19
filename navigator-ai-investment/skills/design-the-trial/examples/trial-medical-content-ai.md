# Worked example: trial design for the medical writing copilot

Constructed example continuing the earlier ones; illustrative. Checked with `scripts/trial_check.py`. [CHECK: replace with a live run]

## The session (turns condensed)

**Turn 1.** Picking up the CMO's result, Investigate first on the copilot, and the outcome "reduce writer time on routine label-driven updates" with its measure (writer hours per month, 300 today, team time log Q2 2026). We'll write down what success and stopping look like before anything starts, then size the trial. What do you expect the trial to show?

**Person.** That AI drafts cut writer hours without new compliance problems.

**Turn 2.** Recorded as the hypothesis (proposed): "If AI drafts routine label updates and writers review them, writer hours on these updates fall from 300 toward the target, without new compliance findings." Step 1 of 2. What result, by when, counts as success?

**Person (CMO).** 210 hours a month by week 12.

**Turn 3.** What would make you stop early?

**Person.** Any compliance finding traced to an AI draft.

**Turn 4.** Recorded; the proposed people-first rule also applies unless you waive it: any failure reaching a clinician or regulator stops the trial. Step 2 of 2. What does running the trial cost: low, likely, high, on what basis?

**Person.** 50, 80, 120 thousand euros: licence plus 10% of two writers.

## The full report (condensed)

**Summary.** A 12-week trial of AI-drafted label updates with writer review, testing whether writer hours fall from 300 to 210 a month without compliance findings. It stops at the first compliance finding traced to an AI draft. It costs 0.05 to 0.12 million euros to run, against a value at stake of 0.4 to 1.6 million euros a year.

| Hypothesis | Measure | Today | Target (set by) | Owner |
|---|---|---|---|---|
| AI drafts with writer review cut writer hours without new compliance findings | Writer hours on label updates (hours per month) | 300 (team time log, Q2 2026, M) | 210 by week 12 (CMO, O) | Head of Medical Writing |

Failure signal: any compliance finding traced to an AI draft, or hours not below 270 by week 8. Stop rule: first such finding; and any failure reaching a clinician or regulator. Exit: target reached for two consecutive months, or the stop rule fires.

Worth and cost: the cost-to-test high end (0.12 million) is well below the value low end (0.4 million a year). Estimated; not realized until measured.

Stored on a brief: no (connector tools not visible yet). Record: draft prepared with an AI assistant, 19 October 2026; uncleared draft: name the clearer.

## Why this is good

The target and the stop rule were set before the start, by the owner. The baseline has a source. The trial cannot be called a success, only placed against its target.
