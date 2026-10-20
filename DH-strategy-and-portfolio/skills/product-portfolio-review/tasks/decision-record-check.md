# A1 Decision record check

Framework task: DH-01.03.3.2, Part A, task A1. Replaces the old "Decision quality check" task (CF-12.01.03.3.2.1) and keeps its method: a pass has the rule, the rank, the decision and the person; a fail is a continue with no rule, or a stop with no record; name the forum to be scored; do not pass a decision that lives only in a slide.

## What this task delivers

For one named forum sitting: the pass rule as the person confirms it, and for each decision whether its record carries the rule, the rank, the decision and the person (decider and date), where the record lives, and pass or fail with the reason. It answers "can each of our decisions be audited?"

Why it matters: a decision that cannot be traced to a rule and a person cannot be scored in A2 or repaired in B1. The check separates "the decision may be right" from "the decision can be shown".

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.2 Part A, Decision record check (CF-12.01.03.3.2.1) |
| Workflow | The steps below |
| Knowledge | `references/review-signals.md` section 1; `references/gap-rules.md` |
| Tools | `scripts/forum_check.py records` and `words` |
| Prompt | This guide |
| Template | `assets/record-check-output.md` |
| Input | The request and its context: the forum and sitting, the decision log or minutes, where each decision is recorded, the person's pass rule |
| Governance | `references/governance.md`; the person sets the pass rule |
| Catalogue job | none. No catalogue job covers governance review (`references/tools.md`). |

## The rule that shapes this task: the person's pass rule, per decision

The pass rule is the person's. The old method's rule is offered as the default, labeled "proposed", and applied only once confirmed. Each decision is checked on its own; the result is never averaged into a forum score. A missing field is reported as missing, never filled.

## Workflow

### Step 1. Name the forum

Write back the forum and the sitting (date) as the person gives them. If not given, ask. Confirm it is the **product portfolio** forum (the company's own products and programs). Decisions about companies held as investments route to `investment-portfolio-monitoring` (this pack); if "portfolio" is ambiguous, ask which one first.

### Step 2. Confirm the pass rule

Offer the default (`review-signals.md` section 1) as "proposed": rule, rank, decision and person recorded; a continue with no rule fails; a stop with no record fails; a decision only in a slide fails. Ask whether the person adds conditions (for example the rule dated before the forum, the scores kept, dissent recorded) or drops any. Write the confirmed rule back. Without a confirmed rule, report the four fields per decision and give no pass or fail.

### Step 3. Read each decision record

From the person's log or minutes, for each decision: item, decision, the rule it names, its rank, decider, date, and where it is recorded. With code execution, put the log in the columns `item, decision, rule_ref, rank, decider, date, record_location` and run `python3 scripts/forum_check.py records LOG.csv`; without it, check by hand. Use only what the record states; if the person describes a decision that is not in a record, write "not in the record supplied". Where the recorded ranks and decisions in the log contradict each other (a lower-ranked item continued while a higher-ranked item was delayed or stopped), note it beside each decision as "rank order and decision differ; reason not in the record". It is a question for A2, not a pass or fail under the record check. The script prints this under "Rank order and decision" (in the evaluation log: COPD inhaler companion, rank 2, delay, while Diabetes coaching app, rank 3, continue). Also give the total capacity the recorded continue items use, if the log carries it, as a fact for A2.

### Step 4. Pass or fail, with the reason

Apply the confirmed rule. For each fail, give the reason in the rule's words ("continue with no rule", "stop with no record", "no decider named", "lives only in a slide"). Count passes and fails, and list each decision; never one average. In the illustrative log, 2 of 4 decisions passed: Program C failed as a continue with no rule, no rank and a record only in a slide; Program D failed as a stop with no record and no decider named (`examples/live/forum_check_runs_output.md`).

### Step 5. What A2 can and cannot score

List which decisions can be scored against the rule in A2 (rule named, scores in the record) and which cannot, and why. A decision without scores is "not recomputable" in A2.

## Build the output

Follow `assets/record-check-output.md`. Answer first: the forum, the pass rule as confirmed, passes and fails by count, and the fail that matters most for A2. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Before you hand it over

- The pass rule is the person's, confirmed; or no verdict is given.
- Each decision is reported separately with its reason; no average.
- Nothing is filled that the record does not state.
- Every contradiction between recorded rank and recorded decision is noted beside both decisions, as a question for A2.
- No product portfolio decision is mixed with an investment holding.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The check reads records; it does not say whether a decision was right.
- Writing a new decision record: `product-portfolio-prioritization` (this pack), task B2.
- No judgment of the people who took or recorded the decisions.
