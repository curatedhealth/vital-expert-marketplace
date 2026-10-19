# B1 Equity review and follow-up

Framework task: DH-02.03.4.2, Part B, task B1. Replaces the earlier "Equity follow-up" section (CF-12.02.03.4.2.3) and folds in the one-line pass rule and owner rule.

## What this task delivers

A review draft that says, subgroup by subgroup, whether the results meet the rules the person set, where they do not, whether the change or the measurement is the more likely reason (as hypotheses with what would confirm each), the follow-up options, the owner the person names, and the next period to score. It answers "which groups miss our rules, why might that be, who owns it, and when do we look again?"

Why it matters: a change that shipped is not a change that reached anyone. The register's rules: name the owner, state whether the change or the measurement was wrong, name the next period, and never close the question because the change shipped.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.2 Part B, Equity review and follow-up |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/equity-measures.md`; `references/equity-frames.md`; PE rows |
| Tools | `analytics.mcda` (counted) for follow-up options the person scored; A2's script if no comparison exists; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/equity-review-and-follow-up-output.md` |
| Input | The request and its context; the person's rules, owners and next period; A1 definition and A2 results |
| Governance | `references/governance.md`; people set rules, decide change versus measurement, name owners and periods |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people set the rules, the question stays open

The person writes the rules before the verdict. The model checks results against them, lays out hypotheses with what would confirm each, and labels suggestions "proposed". A follow-up is not closed because the change shipped. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Workflow

### Step 1. Gather the evidence

Use A1 and A2 from the conversation. If A2 is missing and the person has counts, run it first in short mode. Without a denominator, the review can only say "not measurable `[GAP]`".

### Step 2. Write the rules with the person

For each dimension, ask for one or two rules with a number and the comparison. Offer this shape, filled with the person's words:

| Rule type | Example shape (their words and numbers) | Checked against |
|---|---|---|
| Ratio | "Reach in each language group at least R times the English rate" (R is yours) | A2 ratio |
| Gap | "No age band more than D points below 45 to 64" (D is yours) | A2 difference |
| Representation | "Share of reached within S points of share of eligible" (S is yours) | A2 shares |
| Outcome | "Outcome rate among reached not more than X points below the reference" (X is yours) | A2 outcome |
| Completeness | "Language not recorded for under N percent of eligible" (N is yours) | A2 not-recorded share |

Write the rules back for confirmation. A dimension without rules gets a factual summary and no verdict. National figures and published results are context, never the rule.

### Step 3. Check each rule

Mark each rule met, missed, or not measurable `[GAP]` (suppressed cell, missing denominator, not recorded), with the number behind it. Say when an interval is wide enough that the result could sit either side of the rule; whether to act on it is the person's call.

### Step 4. Change or measurement: hypotheses

For each miss, lay out both kinds, each with what would confirm it:

- **Measurement.** The group field is not recorded for many (confirm from the not-recorded share); the denominator includes people the change could not reach (confirm from the eligibility rule); the record of use misses the path the group took (confirm from logging).
- **Change.** The change did not reach the step where the barrier sits (confirm from where in the funnel the group drops; PE-102 dropout versus nonusage); the change reached people but did not lead to the outcome (confirm from the outcome among reached; effective engagement, PE-104).

The person decides which it was. Never state a cause the data does not show.

### Step 5. Follow-up options and ranking

List options for each miss, labeled "proposed", for example fix the logging, adjust the change, add a path, ask a partner who can see the group (design skill A2). If the person wants a ranking, ask for criteria phrased as benefits, weights and 0 to 4 scores, then call `analytics.mcda` and report values and contributions. Never score for them.

### Step 6. Owner and next period

Record the owner of each follow-up and the next period the person will score (start and end dates). Missing: "owner not named" or "next period not set"; ask. No dates from the model, no urgency.

### Step 7. Stops

State what stops for the accountable owner: any claim that a gap is closed or a group reached, for publication or for a regulator, HTA body or payer; any Section 1557 compliance statement; DAP goal attainment for FDA; closing the follow-up while the rule misses. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/equity-review-and-follow-up-output.md`. Answer first: which subgroups miss the person's rules (with the numbers), the leading hypothesis to test for each, the owner and the next period. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, threshold, owner and period is the person's, and the output says so.
- Every verdict cites the number behind it; suppressed and unrecorded groups are "not measurable", not "met".
- Change and measurement hypotheses are labeled hypotheses with confirmations.
- The follow-up is open unless the person's rule is met and the person closes it.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checks and structures; does not judge teams or people, and makes no decision about any individual.
- Uptake or reach is not clinical evidence and not an outcome a payer pays on (dh-market-access).
- Accessibility conformance follow-up belongs to the dh-user-experience accessibility skills.
