# B1 Performance review

Framework task: DH-03.01.1.2, Part B, task B1. Replaces the earlier "value-based contract pass rule" and "value-based contract miss owner" sections.

## What this task delivers

A review draft that says, contract by contract (or measure by measure), whether the outcomes contract is on track, at risk or missed against the review rules the person sets; where it stalls; who the person says owns each miss; the possible reasons, labeled as hypotheses; and where the response belongs, including back to contract design. It answers "is our outcomes contract working, and what do we do about it?"

Why it matters: the contract's payment rules say what the payer will pay; they do not say whether the arrangement is worth keeping, or whose work should respond. Without written review rules, a near-threshold result gets explained by whoever speaks first.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/attainment-rules.md`; `references/data-completeness.md`; the OECD and ISPOR rows in `references/outcomes-contracting-sources.md` |
| Tools | A1 and A2 (`scripts/attainment.py`) if not yet run |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's review rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners; contract changes stop for the owner |

## Read the request

- **Which contract and period.** One contract or several; interim or end of period.
- **Review rules and owners.** Whether the person already has them. If not, Step 2 writes them with the person; none are invented.
- **What evidence exists.** A1 and A2 runs in the conversation, or data to run them.
- **Audience and mode.** Short for a direct question; full for a review meeting. Board or payer use stops for the owner.

## The rule that shapes this task: people judge

The person writes the review rules in their own words and numbers and names an owner for each. The contract's payment threshold is one possible rule, not the only one. The model checks results against those rules, finds where the result stalls, and lays out options. It never sets a threshold, never decides what counts as a miss, and never names an owner the person has not named. If asked to propose rules, it marks each "proposed" with the fact behind it and does not apply it until confirmed.

## Workflow

### Step 1. Gather the evidence

Use A1 (attainment, payment factor, distance to threshold) and A2 (completeness, the two-way rate) from the conversation. If missing, run them first in short mode. A review without A2 says that completeness was not reviewed.

### Step 2. Write the review rules with the person

Offer this shape, filled in their words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Attainment | "At or above the contract threshold at each interim count" | A1 rate |
| Margin | "At least three patients above the threshold" | A1 distance |
| Completeness | "At least 9 in 10 aligned patients with a valid final value" | A2 |
| Economics | "Payment factor of at least 90 percent" | A1 payment effect |
| Data timeliness | "No baseline later than day 45" | A2 timing |

Write the rules and owners back for confirmation before checking anything.

### Step 3. Check each rule

Pass, miss, or not measurable `[GAP]`, each with the number behind it. On track if every rule passes; missed if any rule misses; at risk if every rule passes but the A1 distance to the contract threshold is within the margin the person set.

### Step 4. Find the stall point

Name the first place the result is lost, in this order: patients not baselined; baselined but lost to follow-up; final values missing or out of window; values present but targets not met. A loss in data is a different problem from a loss in outcome; A2's two-way rate shows which dominates.

### Step 5. Lay out hypotheses, not causes

For each stall point, list possible reasons as hypotheses, each with what would confirm it. Draw them from the mechanics in `references/`: for example, PROM items are voluntary with one reminder allowed, so low PROM completion may reflect the collection workflow rather than the product (OC Germany "AbEM: voluntary patient participation"); a measure that needs a non-self-reported value (ACCESS blood pressure) depends on a clinical encounter in the window. Never state a cause the data does not show.

When a population-average rule is met on completers, show a labeled sensitivity, not an imputation: the mean over all starters if non-completers had zero change, and the break-even mean change non-completers would need for the all-starter mean to reach the target. Label it "illustration, not an estimate". It is arithmetic on the person's numbers.

### Step 6. Route the response, including back to design

| Stall point | Responding work |
|---|---|
| Measure cannot be collected as written; window or self-report rule unworkable; value of information below cost | Contract design: DH-03.01.1.1, tasks A1 (measures) and B1 (terms), through the contract owner |
| Data lost between baseline and final | Data operations and patient follow-up, with the owner named |
| Data complete, targets not met | Product and clinical work, outside this pack; evidence questions to the clinical evidence owner |
| Rules or framework change (for example a German framework method for the 20 percent component, or a CMS threshold change) | Contract design, DH-03.01.1.1 task A2 |

Name the owner the person gave; if none, say "owner not named" and ask.

### Step 7. The worth-keeping question

Restate the ISPOR test for the person to judge: is the cost of collecting and reconciling the data justified by what the arrangement decides (OC Method guidance "ISPOR: when worth doing")? Give the facts the review produced (completeness effort, payment at stake). The person answers. This step appears in full mode only; in short mode, leave it out.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: the answer (verdict per rule with its number, the stall point, the one decision needed), one results table with the owner per rule, at most three hypotheses as open items, the record line. Full mode adds the rule table, evidence, the full hypotheses table, routing and the worth-keeping context.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it.
- Causes are hypotheses, labeled.
- Contract, risk-share or pricing changes, any wording for the payer, and board reporting stop for the accountable owner.
- Attainment is not presented as clinical evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of the final attainment or payment.
- Drugs, biologics and wellness apps are out of scope.
