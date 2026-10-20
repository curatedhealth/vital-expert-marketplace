# B1 Pipeline review

Framework task: DH-DIL.1.2, Part B, task B1. New judgment task of the competency; it turns the old "state when the watch has no later sweep" boundary into a review the person can repeat.

## What this task delivers

A review draft: the person's triggers written back, each pipeline entry marked "needs a look", "no trigger met" or "not measurable" against those triggers using the A1 and A2 facts, and for each entry that needs a look the owner the person names, the work it routes to and the reread date the person sets. It answers "which entries in our pipeline need a look, and who looks?"

Why it matters: a change read is only useful if someone decides what it means for each target. Written triggers, owners and reread dates make the next review repeatable and keep the decision with the person.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.2 Part B, Pipeline review |
| Workflow | The steps below |
| Knowledge | A1 and A2 output; `references/monitoring-signals.md`; `references/gap-rules.md` |
| Tools | A1 and A2 tools if no read exists; `scripts/monitor_helpers.py` |
| Prompt | This guide |
| Template | `assets/pipeline-review-output.md` |
| Input | The request and its context; the pipeline list (company, stage, the person's triggers, owner, reread date); A1 and A2 results |
| Governance | `references/governance.md`; people set triggers, owners and dates; no investment advice |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the triggers (for example "any new FDA authorization", "any new Form D or 8-K", "any new safety record", "a rule change for EU targets"), names the owner of each entry and sets the reread date. The model checks the A1 and A2 facts against those triggers and routes the work. It never sets a trigger, a date or an owner the person has not given, never ranks the pipeline, and never says what to do about a target. If asked to propose triggers, each is marked "proposed" with the record type behind it and is not applied until the person confirms.

## Workflow

### Step 1. Gather the reads

Use the A1 and A2 reads the person brings into this request, and the A3 check if the pipeline rests on an ecosystem map. If there are none, run A1 (and A2 if the triggers include rule or screen changes) in short mode for the pipeline's companies and the person's date. Say what was not read.

### Step 2. Write the triggers and entries back

Number the person's triggers in their words. List each pipeline entry with its stage, owner and reread date as given ("owner not named", "reread date not given" where missing).

### Step 3. Check each entry

For each entry and trigger: met (the change, event date, source), not met (with the log caveat if the read is "no change recorded"), or not measurable `[GAP]` (the source is not loaded, the name did not resolve, the "since" date is before the log began). For a "since" date before 12 October 2026, offer the dated filings and authorization records for the uncovered part (A1 step 4) instead of "not met". An entry is "needs a look" only if a trigger the person wrote is met.

### Step 3b. Company status

Each entry carries one status line from the A1 status step (`monitoring-signals.md` section 5): the status as a primary filing or register entry states it, with form or item, date and source, or "Status: [GAP]: not read" with the exact filings to open. Never infer status from press, memory, a quiet log or a missing filing (for example a company whose latest filing in the store is old). A status is never a trigger unless the person writes one.

### Step 4. Route each entry that needs a look

| Trigger met | Responding work |
|---|---|
| New authorization, study or safety record | `company-and-evidence-assessment` (this pack) for the record; `evidence-maturity-monitoring` (this pack) for the evidence over time; regulatory consequences to `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| New Form D, 8-K or other filing | `funding-and-portfolio-comparison` (this pack) to read the filing; for a holding, `investment-portfolio-monitoring` (this pack) |
| A change that may touch the thesis or a memo | `thesis-and-memo-monitoring` (this pack) |
| A rule change for the deal's jurisdiction | the owner the person names for legal or compliance questions, with the rows from A2 |
| A reimbursement or listing change | `dh-access-and-value` coverage-pathway-and-access-strategy |

### Step 5. Owner and reread date

For each entry that needs a look: the owner the person named, what the look is (the routed work), and the reread date the person set. Never supply either; write "not given" and ask.

### Step 6. Re-run

Say what to rerun at the reread date: the same `get_deltas` call with the new "since" date (the date of this read), the same screen arguments, and the rule list after this date.

## Build the output

Follow `assets/pipeline-review-output.md`. Short mode: triggers, one status line per entry, the entries that need a look with owner, routed work and reread date, the entries not measurable, the one decision the person needs to make, and the record line. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Triggers, owners and reread dates are the person's, and the output says so; proposals are labeled.
- Every "met" cites the change, its date and its source; every "not met" on a quiet log carries the log caveat.
- No ranking of the pipeline, no recommendation to act, no valuation, no intent read into a change.
- Each entry has a status line from a primary record, or "Status: [GAP]: not read" with the filings to open.
- Word count run (`scripts/monitor_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model checks and routes; it does not decide what to do about a target.
- No watches; no forecast of when a target will file or close.
