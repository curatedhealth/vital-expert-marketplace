# B1 Performance review

Framework task: DH-03.01.2.2, Part B, task B1. Replaces the earlier "coding and pricing pass rule" and "coding and pricing miss owner" sections.

## What this task delivers

A review draft that says, per contract or route, whether coding, pricing and the contract perform against the rules the person set: on track, at risk, or missed; the stall point; the owner the person named; hypotheses to test; and which work responds, including a route back to coding strategy and contracting (DH-03.01.2.1). It answers "are our codes, prices and contracts working, and what do we do about the ones that are not?"

Why it matters: without written rules, every review argues about what "good" means. Rules set before the numbers arrive make the review fair and repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/contract-measures.md`; `references/publication-cycles.md` |
| Tool | A1 tools if no change run exists; `scripts/contract_performance.py --rules` |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the rules, in their own words and numbers, and names an owner for each. The model checks results against those rules, finds the stall point and lays out options. It never sets a threshold, never decides what counts as a miss, and never names an owner. If asked to propose rules, each is marked "proposed" with the fact behind it, and is not applied until confirmed.

## Workflow

### Step 1. Gather the evidence

Use A1 (changes and clocks) and A2 (contract measures). If either is missing and needed, run it first in short mode. A review on A2 alone says that rule changes were not reviewed.

### Step 2. Write the rules with the person

For each contract, ask for two to four rules, each with a number and an owner. Offer this shape, filled with their words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Claims | "Denials stay under 5 percent of submitted claims" | A2 denial rate |
| Price | "We realize at least 98 percent of the agreed amount" | A2 realization |
| Volume | "We know before we cross 3,000 units" | A2 volume tier |
| Outcome | "We earn at least 80 percent of the outcome component" | A2 attainment |
| Rules | "No code we bill is changed by a final rule without a plan" | A1 |

Write the rules back for confirmation before checking anything. A contract without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark pass, miss, or not measurable `[GAP]`, with the number behind it. With code execution, `scripts/contract_performance.py data.csv --rules rules.json` does the claims, price and outcome rules. A contract is "on track" if every rule passes, "missed" if any misses, "at risk" if every rule passes but an A1 change or clock bears on a rule (for example a proposed rule affecting a billed code, a tier within reach, the end of a maximum-amount window).

### Step 4. Find the stall point

Name the first missed stage in this order: coding and claims, price realization, volume, outcome component. A miss at claims is a different problem from a missed outcome component.

### Step 5. Hypotheses, not causes

For each stall point, list possible reasons as hypotheses, each with what would confirm it, drawn from sourced mechanics: for a US denial rate, billing conditions such as one practitioner per 30 days, the 2 to 15 versus 16 to 30 day alternatives, or the established-patient rule (US4, US11, US13, US15), with the OIG finding on incomplete RPM components as background (MO4); for a DMHT denial rate (G0552 to G0554), the device classification, the biller incurring the device cost and the behavioral health plan of care (US17, US18); US19 is about G0552 pricing, not denials, and is not a cause of denials; for German realization below agreed, a group maximum reduction above 10,000 codes (DE15); for an ACCESS outcome miss, the all-or-nothing rule per patient and lost-to-follow-up patients staying in the denominator (outcomes file). Never state a cause the data does not show.

### Step 6. Route the response

| Stall point | Responding work |
|---|---|
| Codes changed or billing conditions not met | Coding pathway map, DH-03.01.2.1 A1 |
| Price below agreed or rules changed the price | Price evidence, DH-03.01.2.1 A2 |
| Terms no longer fit (tiers, outcome definition) | Contract negotiation preparation, DH-03.01.2.1 B1 |
| Outcome component missed | Outcomes contract work, DH-03.01.1 |
| Billing operations | The person's revenue cycle team, outside this pack |

Name the owner the person gave. If none, write "owner not named" and ask.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: verdict per contract, stall point, owner, and the one decision needed.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites its number.
- Causes are hypotheses, labeled.
- Price, contract and billing changes, and any external wording, stop for the accountable owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of recovery or of a final rule.
- Drugs, biologics and wellness apps are out of scope.
