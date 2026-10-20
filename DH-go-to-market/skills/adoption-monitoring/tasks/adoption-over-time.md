# A2 Adoption and penetration over time

Framework task: DH-02.02.4.2, Part A, task A2. Replaces register task CF-12.02.02.4.2.2 "Adoption score".

## What this task delivers

Adoption, penetration and old-step use computed period by period, by site and role, from the person's own roster and usage file, every rate with its numerator and denominator; window adoption against the person's rule if set; activity after training month by month; maintenance if the person sets a horizon; and the eligible users not yet trained. It answers "how many trained users do the task in production, how many eligible users, over time, and is the old step still used?"

Why it matters: a single adoption figure hides the two things that decide what to do: whether trained users kept doing the task after the first weeks (training knowledge can decay, CS78) and whether the old step is still in use beside the new one. Audit and feedback needs data over a specified period (CS44).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.2 Part A, Adoption and penetration over time |
| Workflow | The steps below |
| Knowledge | `references/adoption-metrics.md` sections 2, 5 and 7; the rule from A1 |
| Tools | `scripts/adoption_over_time.py` (local). No library call: the person's data never goes to the connector |
| Prompt | This guide |
| Template | `assets/adoption-over-time-output.md` |
| Input | The request and its context: the adoption rule (A1), roster (`user_id, role, site, eligible, trained_date`), usage log (`user_id, date, kind` with kind `task` or `old_step`), the as-of date, the grouping, the period |
| Governance | `references/governance.md`; roles, sites and pseudonymous ids only; no clinical or payment claim from usage |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Rule.** From A1. Without a task event there is nothing to count. Without a window and share there is no verdict, only numbers.
- **Files.** Ask for the roster and the usage log in the columns above, or tables in the message. If the person's log has another shape, map it and say how. If names appear, replace them with ids before computing and say so.
- **Grouping and period.** Site, role, or both; month or week. Default: site, month; say so.
- **As-of date.** Default to the date of the conversation and say so.
- **Mode.** Short for a direct question; full for an audit and feedback pack.

## Workflow

### Step 1. Take the data

Check it (the script lists these): usage for ids not on the roster; task events before the training date; task events with no training date; duplicate ids. Each is a data check for the person, not a silent fix.

### Step 2. Compute

With code execution:

`python3 scripts/adoption_over_time.py ROSTER.csv USAGE.csv --as-of YYYY-MM-DD --by site [--period week] [--window W --rule-share S] [--maintenance-months M]`

Pass `--window` and `--rule-share` only with the person's values. Without code execution, compute the same by hand using the definitions in `references/adoption-metrics.md` section 7.

### Step 3. Report the numbers

Per group, the latest period first: adoption (adopted/trained), penetration (active/eligible), active/trained, old-step users, eligible but not trained. Then the trend: the period where adoption or penetration changed most, with both numbers. Name the definition used for each metric and its row (CS34 or CS28 for adoption; CS39 for penetration). Report old-step users who also did the task in the same period (working in both) separately from old-step-only users; it is a signal for the "workflow wrong" hypothesis, not a cause.

### Step 4. Check against the rule, if set

Window adoption against the person's share: met or missed, with numerator and denominator; users whose window has not elapsed are counted apart. Without a rule: "no rule set".

### Step 5. After-training activity and maintenance

Report the month-by-month share of adopters still doing the task, labeled "usage, not a measure of training retention" (section 5). If the person set M, report maintenance with the script's 30-day look-back stated.

### Step 6. What it means for the person

Two or three consequences, conditional, from the numbers and rows. For example: "At South, 6 of 11 trained nurses have done the task once, and 7 people used the old step this month; the old step has not stopped." "Adoption among trained is 14 of 15 at North while 3 eligible users are not trained; penetration among eligible (14 of 18) is the figure to feed back to the site." No cause is stated; causes are hypotheses for B1.

## Build the output

Follow `assets/adoption-over-time-output.md`. Answer first: the latest adoption and penetration per group with denominators, and the rule verdict if set. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rate has numerator and denominator and names its definition.
- No verdict without the person's rule.
- Sites are not averaged into one figure that hides a site.
- No cause stated; no clinical or payment meaning given to usage.
- No names; the data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Measurement only. Classifying a miss and the follow-up are B1. Training coverage is the sibling skill's A2.
- Patient-level outcomes (PHQ-9, GAD-7, PAM; CS89 to CS95) belong to DH-02.02.3.x.
