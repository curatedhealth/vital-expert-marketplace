# B1 Pricing and message review

Framework task: DH-02.01.3.2, Part B, task B1. Replaces the old "Price miss owner" section and the pass rules for pricing and messages.

## What this task delivers

A review draft that says, against rules the person set before looking at the results: whether pricing is holding (from A1), whether the live messages are safe and supported (from A2), and, where the person tracks them, whether message results moved; for each miss, whether the corridor or the deal looks off, the owner the person named, the next deal or message the corrected rule should apply to, and the work that responds.

Why it matters: without written rules, every review reopens what "good" means. A discount can be a failing corridor or a single bad deal; a flagged claim can be a one-off or a pattern in the template. The review separates them.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.2 Part B, Pricing and message review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/realized-price-rules.md`; `references/claim-rules.md`; the corridor and message map from the sibling skill if they exist |
| Tools | A2's tools if no claims audit exists; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/pricing-review-output.md` |
| Input | The request and its context; the person's pass rules, thresholds and named owners; A1 and A2 results; any message results the person tracks (for example win rates or response rates) |
| Governance | `references/governance.md`; people set rules and name owners |
| Catalogue job | none. Rules, thresholds and owners are the person's. |

## The rule that shapes this task: people judge

The person writes the pass rules, in their words and numbers, and names the owner of each. The model checks results against those rules, separates corridor problems from deal problems, and lays out options. It never sets a threshold, never decides what counts as a miss, never names an owner the person has not named, and never judges a person or a team. If asked to propose rules, it may, each marked "proposed" with the fact behind it, and does not apply them until the person confirms. Message KPIs (win rate, response rate, recall) are not sourced; they are the person's.

## Workflow

### Step 1. Gather the evidence

Use A1 (deal table) and A2 (claims audit). If either is missing and needed, run it first in short mode. A review on pricing alone is possible and says that messages were not reviewed, and the reverse.

### Step 2. Write the pass rules with the person

Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Corridor holding | "At least 8 in 10 new deals inside the corridor" | A1 positions |
| Discount discipline | "No deal more than 25 percent below list without approval" | A1 discounts |
| Message safety | "No Stop flag live in any market" | A2 flags |
| Message support | "Every number on the payer deck has a passage" | A2 evidence checks |
| Message result | The person's KPI and source | The person's data |

Write the rules back for confirmation before checking anything. A rule without a number is a summary, not a verdict.

### Step 3. Check each rule

Mark each rule pass, miss or not measurable `[GAP]`, with the number behind it and its date.

### Step 4. Corridor or deal?

For each pricing miss, lay out both readings with the facts that favor each, without choosing: many deals below the floor across reps, segments or markets points toward the corridor; a few deals with a shared feature (one segment, one channel, one partner) points toward the deal. German statutory prices after year one are payer-set (DE1, DE9) and belong to dh-access-and-value. For each, name the next deal the corrected rule would apply to, if the person gives the pipeline.

### Step 5. Message misses

For each Stop or unsupported claim still live, name where it runs, the rows, and whether the same wording sits in a template used elsewhere (a pattern) or in one asset. Message results the person tracks are reported against their rule; causes are hypotheses, each with what would confirm it. A message result is never evidence of clinical effect.

### Step 6. Route the response

| Miss | Responding work |
|---|---|
| Corridor looks off | Price corridor evidence (pricing-and-value-proposition, task A2), then the pricing owner |
| Deal looks off | The person's deal approval process and pricing owner |
| Discount tied to referrals or volume, free units | Compliance or legal owner, with CP rows |
| Claim flagged Stop or unsupported | Regulatory or legal owner; value messages (pricing-and-value-proposition, task B1) |
| Payer-set price or payer contract | dh-access-and-value (coding-pricing-and-contract-monitoring) |

Name the owner the person gave. If none, write "owner not named" and ask.

## Build the output

Follow `assets/pricing-review-output.md`. Short mode: verdict per rule, the corridor-or-deal reading for the main miss, the message misses, owners, the one decision needed.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it and its date.
- Causes are hypotheses, labeled.
- Corridor changes, discount policy, claim wording and anything a payer sets stop for their owners.
- Count the words in short mode.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No forecast of prices or message results.
- No verdict on people or teams.
- No clearance of claims.
