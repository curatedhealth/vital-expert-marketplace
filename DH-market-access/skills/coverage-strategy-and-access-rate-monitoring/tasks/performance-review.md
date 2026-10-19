# B1 Performance review

Framework task: DH-03.01.4.2, Part B, task B1. Replaces the earlier "pass rule" and "miss owner" sections.

## What this task delivers

A review draft that says, market by market, whether the coverage strategy is working against the rules the person set: on track, at risk, or missed; where in the path it stalls; who the person says owns each miss; and which piece of work should respond. It answers "is our coverage strategy working, and what do we do about the markets that are not?"

Why it matters: without written rules, every review reopens what "good" means and the loudest explanation wins. Rules set before the numbers arrive make the review fair, repeatable and fast.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; the access strategy if one exists (its gates); `references/lapse-signals.md`; `references/uptake-measures.md` |
| Tools | A1's tools if no status run exists; `scripts/access_funnel.py` (optional) |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's pass rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the pass rules, in their own words and numbers, and names the owner of each. The model checks results against those rules, finds where the path stalls, and lays out options. The model never sets a threshold, never decides what counts as a miss, and never names an owner the person has not named. If asked to propose rules, it may, each marked "proposed" with the fact behind it, and it does not apply them until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (coverage status and clocks) and A2 (uptake funnel) from the conversation. If either is missing and needed, run it first in short mode. A review on coverage alone is possible and says that uptake was not reviewed.

### Step 2. Write the pass rules with the person

For each market, ask for two or three rules, each with a number and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Coverage | "Permanent DiGA listing before the trial extension runs out" | A1 status and clock |
| Activation | "At least 8 in 10 prescriptions become an activated code" | A2, stage 2 to 4 |
| Persistence | "3 in 4 still active at week 4" | A2, stage 4 to 5 |
| Reach | "1,000 activated patients a quarter by the second year" | A2, stage 4 |

Where the strategy (from the coverage pathway skill) set gates, start from those. Write the rules back for confirmation before checking anything. A market without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the number behind it. For a temporary route (a DiGA trial, the PECAN year, a NICE evidence period), also state how much of the coverage period is left, counted as in A1, because it bounds every response. A market is "on track" if every rule passes, "missed" if any rule misses, "at risk" if every rule passes but a clock from A1 is close to a threshold the rule depends on. With code execution, `scripts/access_funnel.py --rules` does the uptake rules.

### Step 4. Find the stall point

For each missed market, name the first stage where a rule missed. That is where the response goes. A miss early (no listing, no prescriptions) is a different problem from a miss late (patients stop using it).

### Step 5. Lay out hypotheses, not causes

For each stall point, list the possible reasons as hypotheses to test, each with what would confirm it. Draw them from the access mechanics (`references/access-after-listing.md`): for example, for low activation in Germany, prescriptions not forwarded to the fund (80 to 90 percent of DiGA e-prescriptions in a pilot were never forwarded), or the approval route needing proof of indication no older than four weeks. Never state a cause the data does not show.

### Step 6. Route the response

Map each stall point to the work that responds, without choosing for the person:

| Stall point | Responding work |
|---|---|
| Coverage not obtained or at risk | Coverage pathway mapping and access strategy (the coverage pathway skill, tasks A2 and B1) |
| Prescribed but not activated | Benefit design (the coverage pathway skill, task B2) |
| Activated but not used | Product and engagement work, outside this pack |
| Evidence clock at risk | Evidence generation, outside this pack |

Name the owner the person gave. If no owner was named, say "owner not named" and ask.

## Build the output

Follow `assets/performance-review-output.md`. Short mode for a direct question: the verdict per market, the stall point, the owner, and the one decision needed. Full mode for a review meeting adds the rule table, evidence and hypotheses.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it.
- Causes are hypotheses, labeled.
- Pricing or contract changes, external wording and board reporting stop for the accountable owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of when a market will recover.
- Drugs, biologics and wellness apps are out of scope.
