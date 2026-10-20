# B1 Performance review

Framework task: DH-03.03.1.2, Part B, task B1. Replaces the earlier "AI/ML regulatory readiness pass rule" and "AI/ML regulatory readiness miss owner" sections.

## What this task delivers

A review draft that says, against the rules the person set, whether the AI device's regulatory work is on track, at risk or missed: readiness before filing, and change control and monitoring after authorization. It names the first point where it stalls, the owner the person gave, labeled hypotheses for why, and the piece of work that responds, routed back to the pathway and change control competency (DH-03.03.1.1) where the fix is a route, plan or submission change.

Why it matters: without written rules, every readiness review reopens what "ready" means, and the loudest view wins. Rules set before the evidence arrives make the review fair and repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/readiness-requirements.md`; `references/post-market-expectations.md` |
| Tools | A1 and A2's tools if no runs exist; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's pass rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the pass rules, in their own words and numbers, and names the owner of each. The model checks results against those rules, finds where it stalls, and lays out options. The model never sets a threshold, never decides what counts as a miss, and never names an owner the person has not named. If asked to propose rules, it may, each labeled "proposed" with the fact behind it, and it does not apply them until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (completeness) and A2 (changes, monitoring, events) from the conversation. If either is missing and needed, run it in short mode first. A review on readiness alone is possible and says that post-market tracking was not reviewed.

### Step 2. Write the pass rules with the person

For each area, ask for one to three rules with a number or condition and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Readiness | "No missing item in the US rows before the Pre-Sub" | A1 status counts |
| AI Act | "All EU-R11 items present before the notified body reviews the technical file" (the obligations apply from 2 August 2028, as set by Regulation (EU) 2026/1744) | A1 EU rows |
| Change control | "Every logged change sorted 'in the PCCP as described' with all protocol steps evidenced" | A2 table 1 |
| Monitoring | "Each applicable expectation has a plan, data and owner" | A2 table 2 |
| Safety | "Every comparable recall reviewed by the risk owner within the period we set" | A2 table 3 |

Write the rules back for confirmation before checking. An area without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the evidence behind it. An area is "on track" if every rule passes, "missed" if any rule misses, "at risk" if every rule passes but an applicable date or clock the rule depends on is near on the person's own definition of near. Dates are stated as facts, never as pressure.

### Step 4. Find the stall point

For each missed area, name the first step in the chain where a rule missed (for example: route undecided, then PCCP scope open, then Pre-Sub not asked; or change logged, then protocol step not evidenced). That is where the response goes.

### Step 5. Lay out hypotheses, not causes

For each stall point, list possible reasons as hypotheses, each with what would confirm it, drawn from the references: for example, a file planned against the superseded 2 August 2027 date [AI EU-32]; a PCCP drafted before the 18 August 2025 reissue [AI US-01] (the 4 December 2024 document was final guidance, not a draft; never call it a draft); acceptance criteria never set because the Modification Protocol was treated as optional [AI US-05]; monitoring planned only to the draft lifecycle guidance [AI US-37]. Never state a cause the evidence does not show.

### Step 6. Route the response

| Stall point | Responding work |
|---|---|
| Route, class or AI Act scope undecided | Pathway map (DH-03.03.1.1, task A1) |
| PCCP incomplete, or a change outside the plan that should be planned | Change control plan (DH-03.03.1.1, task A2) |
| Filing order or agency interaction | Submission plan (DH-03.03.1.1, task B1) |
| Quality-system evidence, CAPA, reportability | Quality pack, outside this skill |
| Model performance analysis | Data science pack, outside this skill |

Name the owner or role the person gave, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: verdict by area, the stall point, the owner, the one decision needed, at most three hypotheses (one line each, with what would confirm it) and routing in one line per area. No explanation of what the missing items are unless asked. Full mode adds the rules table, results and evidence.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the evidence behind it.
- Causes are hypotheses, labeled.
- Filing, regulator-facing wording and reportability stop for the accountable owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of a review outcome or a recovery date.
- Drugs, biologics and wellness apps are out of scope.
