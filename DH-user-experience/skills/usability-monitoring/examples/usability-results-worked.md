# Worked example: A1 usability results by task

Run on 19 October 2026. The log and SUS answers are illustrative files written for this example (`sample-data/usability_log_illustrative.csv`, `sample-data/sus_illustrative.csv`) and labeled so. The script outputs are saved beside them (`sample-data/log_summary_output.txt`, `sample-data/sus_output.txt`). The source checks are real library calls (`live/qualify_source_sus.json`, `live/check_claim_sus.json`).

**Request (illustrative):** "Here's our validation test log for the dose-check app, build 3.1, ward nurses and pharmacists. We marked T1 to T3 as critical and assigned severity ourselves. Our minimum is 15 per group. Summarize it and give us the SUS against the digital health benchmark."

**Calls and runs**

1. `python3 scripts/usability_log.py log examples/sample-data/usability_log_illustrative.csv --min-per-group 15`
2. `python3 scripts/usability_log.py sus examples/sample-data/sus_illustrative.csv`
3. `verify.qualify_source {doi: "10.2196/37290", question: "What is the mean System Usability Scale score of digital health apps?"}`: tier gold, current, retraction status none.
4. `verify.check_claim` with the claim "The mean SUS score across the collected digital health apps was 76.64", the passage from row UX-M-09, and the full record from step 3 as `source`: supported. Passage read: same direction.

## Answer (short mode)

**Use errors occurred on all three critical tasks you marked, and both groups are below your minimum of 15.** T2 (enter weight-based dose) has 2 use errors in 14 ("entered mg instead of mg/kg"), 1 participant who did not complete and returned to the paper chart, and 1 difficulty, all marked serious by you. T1 (confirm patient identity) has 1 use error ("selected adjacent patient in list"); T3 (acknowledge allergy alert) has 1 ("dismissed alert without reading"). All seven non-success rows on T1 to T3 come from pharmacists (P11 to P14).

| Task | Critical (yours) | Use errors | Returned to old step | Severity as you assigned |
|---|---|---|---|---|
| T1 Confirm patient identity | yes | 1 of 14 | 0 | serious 1 |
| T2 Enter weight-based dose | yes | 2 of 14 | 1 | serious 4 |
| T3 Acknowledge allergy alert | yes | 1 of 14 | 0 | serious 1, not assigned 1 |
| T4 Review potassium trend | no | 0 of 14 | 2 | minor 3 |

**Test conditions (validation):** nurses 8 and pharmacists 6, against your 15 and FDA's 15 per distinct population (UX-US-35): not met. No employees and no think-aloud flagged (UX-US-38, UX-US-40). Final UI, realistic conditions and training timing are not stated in the log (UX-US-34, UX-US-41); please confirm.

**Flag:** T3, participant P13, has a difficulty with no severity assigned. It is not treated as minor.

**SUS:** mean 75.18 (SD 7.17) overall; nurses 74.06, pharmacists 76.67. Context only, not a target: the digital health app mean was 76.64 (SD 15.12) across 117 scores (UX-M-09, checked against the paper through Verify); the general benchmark cited is 68 (SD 12.5) (UX-M-08). SUS does not measure use error.

**Open questions:** Was the UI final for build 3.1? How long after training did testing start? Which severity applies to T3/P13?

**Record:** Results summary on your log. Counts only; no verdict. Uncleared. AI-assisted.

The full version adds the non-success rows by severity with notes, and the full condition table.

## What this example shows

- Severity, criticality and the minimum were the person's; the script counted and flagged.
- The FDA 15-per-population figure was given as a fact beside the person's own rule, not as a verdict.
- The benchmark was used as context and checked through the two-step Verify sequence that works.
