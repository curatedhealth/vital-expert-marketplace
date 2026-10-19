# B1 Review and correction plan

Framework task: DH-02.02.3.2, Part B, task B1. Replaces the earlier "Unsupported note owner" section and the one-line pass rule and miss owner rule.

## What this task delivers

A review draft that says whether thresholds and sent notes meet the review rules the person set, where they do not, what corrections could respond (withdraw a note, correct a figure, add a signal from stored data, restore or confirm a target), how the person scores those corrections, and who owns each one and which forum will see it. It answers "what do we fix in our value reporting, and who owns it?"

Why it matters: the register's rule is "Do not leave an unsupported note in the account record". A correction without an owner and a forum tends not to happen; a correction that changes the data to fit the note makes the problem worse.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.2 Part B, Review and correction plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/value-evidence-rules.md`; `references/governance.md` |
| Tools | `analytics.rice` or `analytics.mcda` (counted) only for corrections the person scored; A1 and A2 tools if no run exists; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/review-and-correction-output.md` |
| Input | The request and its context: A1 and A2 results, the person's review rules, named owners, scores if ranking is wanted |
| Governance | `references/governance.md`; people set rules, choose corrections and name owners |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people decide, the data does not move

The person writes the review rules, chooses each correction and names its owner and forum. The model checks results against the rules, lays out options with their basis, ranks only what was scored, and labels suggestions "proposed". A correction never edits a signal row to match a note, and never eases a target to turn an account green.

## Workflow

### Step 1. Gather the evidence

Use A1 and A2 from the conversation. If either is missing and needed, run it first in short mode. A review on one of them says what was not reviewed.

### Step 2. Write the review rules with the person

Ask for one or two rules per area, each with a number or condition. Offer this shape, filled with the person's words:

| Rule type | Example shape (their words and numbers) | Checked against |
|---|---|---|
| Note backing | "No note sent with a value that differs from its row" | A2 statuses |
| Narrative | "No result sent without a signal row" (register rule) | A2 unsupported |
| Wording | "No effect or saving wording in any customer note" | A2 wording flags |
| Target change | "Any eased target is recorded with a reason before results are read" | A1 changes |
| Coverage | "Every outcome share has a completeness signal for every account" | A1 missing data |

Write the rules back for confirmation. An area without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule met, missed, or not measurable `[GAP]`, with the count or the note ids behind it. Never average areas into one score.

### Step 4. Corrections

For each miss, list correction options with their basis, labeled "proposed":

- Unsupported or differing note: withdraw it, or send a correction with the row value; or, if the claim matters to the customer, add the signal from data the product stores and report it from the next period (register rule: "State whether the note is withdrawn or the signal is added").
- Effect, saving or comparison wording: route to the person's regulatory or legal owner; draft a replacement sentence with only traceable figures, labeled "draft for the owner".
- Eased target that turned accounts green: record the reason and decision date, or restore the previous value; the person decides.
- Missing data: confirm the field is stored (CS64) or the report is received.

Hypotheses for any miss are labeled, with what would confirm each. No judgment of the note's author.

If the person wants an order, ask for scores (Reach, Impact, Confidence, Effort for `analytics.rice`; or 0 to 4 criteria and weights for `analytics.mcda`). For RICE, pass confidence as a percent (80, not 0.8); the tool divides a fraction by 100 again (`references/tools.md`). Check the order by hand. Never score for them.

### Step 5. Owner, forum and date

For each correction, record the owner the person names, the forum that will see it, and the date of the correction as they set it. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. No dates proposed by the model.

### Step 6. Stops

State what stops for the accountable owner: any correction or retraction sent to a customer; any effect, cost or comparison wording; any outcome tied to payment (Market Access `outcomes-contract-monitoring`); any statement that a customer realized value outside the person's rule. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/review-and-correction-output.md`. Answer first: which rules miss, the corrections chosen or to choose, the owners, and the one decision needed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, choice, score, owner and date is the person's, and the output says so.
- Every verdict cites the count or note ids behind it.
- No correction edits data or eases a target; hypotheses labeled; no judgment of people.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not send, clear claims, or judge people.
- No renewal, churn or revenue forecast (not sourced).
- Payment-linked outcomes, claims clearance and pricing belong to other packs and owners.
