# B1 Impact review and miss owners

Framework task: DH-05.02.3.3.3, DH-05.03.1.3.3, DH-05.02.2.2.3, DH-05.02.1.3.3, DH-05.03.2.2.3 and DH-05.03.2.3.3, Part B, task B1. Carries the old tasks "Bet review" (DH-05.02.3.3.3), "Review outcome" (DH-05.03.1.3.3), the follow-up halves of "Cadence break" (DH-05.02.2.2.3), "Support after the session" (DH-05.02.1.3.3), "Campaign result" (DH-05.03.2.2.3) and "Champion load" (DH-05.03.2.3.3), and the pass-rule and miss-owner steps of the monitoring framework as steps 1 and 4.

## What this task delivers

For each unit under review (adoption stage, report, bet metric, agreement, certified metric, publish right, champion seat): the person's pass rule, the result against it from A1 and A2, met, missed or not measurable, and for every miss the owner the person names and the date it will be rechecked, or "stopped". Then the decisions the review surfaces, each with its facts, all left to the person: keep, change the insertion, or stop the product; reset a target or rule; instrument a metric; decertify; remove a right; replace a champion; follow up with non-completers. It answers "by our own rules, what missed, who owns each miss, and what do we have to decide?"

Why it matters: the old tasks were explicit: "Do not keep a product whose outcome was not measured", "Do not leave the product on the list with no outcome", "Do not end enablement at the session". A review that names owners the team never named, or decides keep or stop from a partial read, says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-analytics-lead` (old DH-05.02.3.3.3); `chief-digital-health-officer` (old DH-05.03.1.3.3); `clinical-content-product-manager` (old DH-05.02.2.2.3); `ai-ml-governance-director` (old DH-05.02.1.3.3, DH-05.03.2). Work as a review analyst who checks against the person's rules |
| Skill | Analytics adoption and impact monitoring, Part B, Impact review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/adoption-measurement.md`; `references/impact-and-governance-checks.md`; `references/governance.md` |
| Tools | None beyond A1 and A2. `analytics.mcda` or `analytics.rice` only if the person scores follow-up options and asks for a rank; `scripts/adoption_check.py words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/impact-review-and-miss-owners-output.md` |
| Input | The request and its context: A1 and A2 outputs or the person's files and read date, the pass rules, owners, recheck dates and follow-up rules the person sets, any scores for follow-up options |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the rules, names the owners, sets the recheck dates and decides what a miss leads to. The model reads the results against the rules and writes them down. It never decides keep, change or stop, never names an owner the person has not named, never sets a recheck date, never closes a miss on its own, and never judges an individual. Where a rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the pass rules

Write each rule back verbatim, numbered, with the date it was written: for adoption, the stage, denominator and level the person counts as met; for reports, what counts as on time and fresh; for the bet, the change against the comparison that counts as met, written before the read; for agreement, what the person reads as a signal; for governance, what must hold. A unit without a rule: "pass rule not given `[GAP]`"; report its values but mark nothing met or missed. A rule written after the result was seen is recorded with both dates and flagged.

### Step 2. Read each unit against its rule

From A1 and A2, or by running the script on the person's files: met, missed or not measurable, with the flag behind each "not measurable" (A1 no denominator, O1 no comparison, O3 users not given, "not instrumented"). Check that the signal measures what the rule says: a rate over attendees against a rule about people in scope is "not comparable"; say so. A product with low adoption and an outcome read is reported with both, and with the fact that a failed deployment is separated from an ineffective product (Proctor 2011, CS32, DOI 10.1007/s10488-010-0319-7).

### Step 3. Miss owners and recheck dates

For each missed unit: the owner the person named (or "owner not named"; ask), the recheck date they set (or "not given"; ask), or "stopped" if they stopped the unit. A recheck date earlier than the read date is stated as a fact, never as urgency. A miss stays open until the person closes it with evidence. For enablement misses, the follow-up owners follow the old method: the owner for a broken metric, the owner for a wrong filter, and how a user reaches them (old DH-05.02.1.3.3); the follow-up for non-completers (old DH-05.03.2.2.3); the replacement for a champion who left (old DH-05.03.2.3.3); for a missed report, who was told and the next issue date (old DH-05.02.2.2.3). Each name is the person's.

### Step 4. Rank follow-ups only if the person scored them

If the person scores follow-up options and asks for a rank, call `analytics.mcda {alternatives, criteria_weights}` or `analytics.rice {initiatives}` on their scores only (confidence as a whole percent), and report the result as "arithmetic on your scores, not a decision" (saved behavior: `mcda_enablement_options.json`, `rice_percent_confidence.json`, 19 October 2026; register C17). Proposed scores are never ranked.

### Step 5. What the person must decide

List the decisions the review surfaces, each with the facts behind it: keep, change the insertion, or stop the product (old DH-05.02.3.3.3; old DH-05.03.1.3.3: choose one, name the owner, update the analytics portfolio list); whether a product whose outcome was not measured is instrumented before the next review ("Do not keep a product whose outcome was not measured"); whether a target or rule is reset (with the date the new rule is written, so later reads use it); whether a changed metric is decertified; whether a right is removed; whether a champion is replaced. Propose nothing unless asked; label any proposal "proposed". The update to the analytics portfolio list goes to `analytics-products-and-decision-support` (this pack).

## Build the output

Follow `assets/impact-review-and-miss-owners-output.md`. Answer first: counts of units met, missed and not measurable against the person's rules, the misses by name, how many have an owner and a recheck date, and the flag that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, owners, recheck dates and follow-ups are the person's, and the record says so.
- No verdict on the product; no keep, change or stop; no miss closed by the model; no individual judged.
- Units without a rule are not marked met or missed; rules written after the result carry both dates.
- The review is labeled "impact review draft for the owner".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- `python3 scripts/adoption_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Redesigning the product, the metric or the insertion point: `analytics-products-and-decision-support` (this pack).
- Any wording for executives, staff at large or customers: stops for the owner the person names.
- People and performance matters: stop for the owner the person names for people matters.
