# B1 Evidence outcome review

Framework task: DH-01.07.1.2, Part B, task B1. Replaces the earlier "Access outcome definition", "Access score" and "Access miss" sections, which are now steps 2, 3 and 4.

## What this task delivers

A review draft that says, body by body, whether the evidence and economic case achieved the outcomes the person set: met, missed or not measurable; the score, if the person gave a formula; for each miss, the first point in the evidence chain where it failed, the owner the person named, hypotheses drawn from what the decision said, and the work that responds. It answers "did our evidence deliver what we needed from these decisions, and what do we do where it did not?"

Why it matters: without outcomes written before the decisions arrive, every review redefines success after the fact. A miss placed at the right point in the chain (clinical effect, utilities and costs, model, reporting, obligation) sends the fix to the right work instead of to the loudest explanation.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.2 Part B, Evidence outcome review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; the gap plan from `reimbursement-evidence-support` if present; `references/decision-evidence-sources.md`; `references/methods-changes.md` |
| Tools | A1's tools if no decision log exists; `scripts/decision_evidence_log.py --share` for a collected-over-asked score only if the person chooses it; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/outcome-review-output.md` |
| Input | The request and its context; the person's outcome definitions, scoring formula and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set outcomes, formulas and owners |
| Catalogue job | None |

## The rule that shapes this task: people judge

The person defines the outcomes, in their own words and numbers, chooses any scoring formula, and names the owner of each. You check results against those definitions, compute only with their formula, find the stall point and lay out options. You never set an outcome, a threshold or a weight, never decide what counts as a miss, and never name an owner the person did not name. If asked to propose outcomes, you may, each marked "proposed" with the fact behind it, and you do not apply them until the person confirms. A comparable product's decision is never an outcome to hit.

## Workflow

### Step 1. Gather the evidence

Use A1 (what each decision said) and A2 (obligations, methods, study currency) from the conversation. If A1 is missing, run it in short mode. A review without A2 is possible and says that obligations and methods were not checked.

### Step 2. Define the outcomes with the person (formerly "Access outcome definition")

For each body, ask for two or three outcomes, each with what would show it and an owner. Offer this shape, filled with the person's words:

| Outcome type | Example in the person's words | Shown by |
|---|---|---|
| Decision on the evidence | "NICE recommends for routine use at re-evaluation" | A1 category, verbatim |
| Economic case accepted | "The committee names no new uncertainty in our cost model" | A1 uncertainties |
| Evidence obligation | "All 11 outcomes in recommendation 1.2 collected before the review point" | A2 obligations table |
| Claim scope | "No claimed effect struck in the DiGA directory" | A1, directory entry (`DE-24`) |
| Methods current | "Model uses the value set NICE requires for our topic" | A2 methods table (`HE-058`, `HE-063`) |

Write the outcomes back for confirmation before checking anything. A body without outcomes gets a factual summary and no verdict.

### Step 3. Check and score (formerly "Access score")

Mark each outcome met, missed or not measurable `[GAP]`, with the quote or fact behind it. A body is "on track" if every outcome is met, "missed" if any is missed, "at risk" if all are met but an A2 window or obligation the outcome depends on is open. If the person gave a formula (for example collected over asked, or a weighted sum of their own scores), compute it with their formula and show the arithmetic; label it their score. Never invent a formula; with none, give the verdicts only.

### Step 4. Name the miss and its owner (formerly "Access miss")

For each missed outcome, name the first point in the evidence chain where it failed, in this order: scope facts, clinical effect, utilities and costs, model and its assumptions, reporting, evidence obligation. Name the owner the person gave; if none, "owner not named" and ask.

### Step 5. Hypotheses, not causes

For each miss, list possible reasons as hypotheses, each labeled "hypothesis" with what would confirm it. Draw them from what the decision said (A1 quotes) and the sourced methods, never from memory. For example: a committee that "did not agree that there was enough evidence to extrapolate the data to 3 years" points to a horizon or extrapolation hypothesis; a model that "assumes ... clinically equivalent" without direct evidence points to the comparative-effect link. Never state a cause the quotes do not show.

### Step 6. Route the response

| Stall point | Responding work |
|---|---|
| Clinical effect or comparator evidence | Study design: dh-clinical-validation `study-protocol-and-endpoint-design`; review: dh-clinical-validation `literature-and-real-world-evidence-review`; evidence plan: `reimbursement-evidence-support` B1 |
| Utilities, costs, model assumptions | `reimbursement-evidence-support` A2 and B1; model build: the pack's economic modeling competency (DH-01.07.2) |
| Evidence obligation not collected | The pack's outcomes research competency (DH-01.07.3) |
| Status, clocks, resubmission, price | dh-market-access |

Name the owner the person gave for each.

## Build the output

Follow `assets/outcome-review-output.md`. Short mode for a direct question: the verdict per body, the miss and its stall point, the owner, the one decision needed. Full mode adds the outcome table, the score arithmetic, the hypotheses and the routing.

## Before you hand it over

- Every outcome, formula and owner is the person's, and the output says so.
- Every verdict cites the quote or fact behind it.
- Causes are hypotheses, labeled.
- Responses to a body, appeals and resubmissions stop for the owner.
- Short mode counted: 450 words or fewer.
- Record line present.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of a re-evaluation or a decision.
- Uptake and outcome-contract attainment are not evidence outcomes here; outcomes contracts belong to dh-market-access (`outcomes-contract-monitoring`).
