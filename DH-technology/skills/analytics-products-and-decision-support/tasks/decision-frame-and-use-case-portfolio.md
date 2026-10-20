# A1 Decision frame and use-case portfolio

Framework task: DH-05.01.3.1, DH-05.01.3.2, DH-05.02.3.1, DH-05.03.1.1 and DH-05.03.1.2, Part A, task A1. Carries the old tasks "Decision frame", "Question list", "Frame review" (DH-05.01.3.1.1 to .3), "Solution shape", "Method match", "Analysis boundary" (DH-05.01.3.2.1 to .3), "Decision product user", "Product bet", "Discovery evidence" (DH-05.02.3.1.1 to .3), "Analytics portfolio list", "Roadmap slice", "Portfolio change" (DH-05.03.1.1.1 to .3), "Use case value", "Priority rule" and "Priority decision" (DH-05.03.1.2.1 to .3).

## What this task delivers

For one analytics request: the decision frame (decision maker, choice, the two actions, the analysis not done), the questions that change the action with their data or `[GAP]`, the solution shape and the method route, the bet with its metric and the discovery evidence, and a value-case sheet with the person's current cost and its source or `[GAP]`. For a set of use cases: the analytics portfolio list with now, next and later, and the rank on the person's own rule with the tie points. It answers "what decision would this change, what is it worth on our numbers, and where does it sit against the others?"

Why it matters: the old method was blunt, "Do not start with a dataset" and "Do not write a value case with no source for the current cost". An analytics product built before the decision is named has no outcome to measure later, and a value case with a borrowed saving puts the model's number in the team's budget.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-analytics-lead` (old DH-05.01.3 and DH-05.02.3.1); `chief-digital-health-officer` (old DH-05.03.1.1 and DH-05.03.1.2). Work as an analytics product analyst who frames and computes on the person's numbers |
| Skill | Analytics products and decision support, Part A, Decision frame and use-case portfolio |
| Workflow | The steps below |
| Knowledge | `references/value-case-and-prioritization.md`; rows DA-02, DA-10 to DA-12, DA-15, CS13, CS38, CS63; `references/governance.md` |
| Tools | `analytics.rice` or `analytics.mcda` (only on the person's scores); `analytics.scenario-modeler` (only on the person's inputs); `scripts/metric_check.py rank`, `words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/decision-frame-and-use-case-portfolio-output.md` |
| Input | The request and its context: the decision maker and choice, the user and the moment they decide, the current tool, the observed step, cost and benefit inputs with sources, the use-case list, the priority rule with the date it was written, scores and who scored them, capacity, the period |
| Governance | `references/governance.md`; the person decides |
| Catalogue job | none (no analytics-product job in `list_jobs_2026-10-19.json`; call the calculators directly) |

## Read the request

- One request or a set? One request runs steps 1 to 5. A set of use cases runs step 6 (and steps 1 to 5 only for the ones the person asks about).
- Is a decision named? If the request starts from a dataset ("we have all this claims data, what can we do with it"), ask for the decision maker and the choice first; write "decision not given" and stop the frame there.
- Is AI involved? NIST AI RMF rows apply only where the analytic uses AI (DA-02: voluntary, not sector-specific).
- Which market? Cost elements from the NICE Evidence Standards Framework (CS63) are NHS context; say so outside the NHS.

## Workflow

### Step 1. Decision frame (old DH-05.01.3.1)

Write back, in the person's words: the decision maker, the choice they have, what they do if the answer is yes and if it is no, and the analysis not done because it does not change the choice. Missing elements are "not given". If the person cannot name an action, say so and stop: "Frame not confirmed: no action named (old DH-05.01.3.1.3)". For an AI use case add two lines: intended purpose and deployment setting (NIST AI RMF 1.0, January 2023, MAP 1.1, DA-10) and the non-AI alternative considered (MANAGE 2.1, DA-15), each in the person's words or "not given".

### Step 2. Question list

List the few questions whose answers change the action. For each: the data that can answer it (the person's sources) or `[GAP]`, ordered so a gap early stops later work. Write the risks that will not or cannot be measured as their own line (MEASURE 1.1, DA-12), where AI is involved.

### Step 3. Solution shape and method route (old DH-05.01.3.2)

Name the shape the decision maker will use (table, dashboard, one number, model, embedded recommendation), its grain and refresh, and the shape considered and rejected. Name the first output the decision maker will see. Name what the solution will not decide and which outputs are descriptive. Route the method: statistical, causal or machine learning methods are `data-preparation-and-analytics-methods` (this pack); a predictive model is `clinical-ml-model-development-and-validation` (this pack). Never default to a model.

### Step 4. Bet and discovery evidence (old DH-05.02.3.1)

Write the bet: what the user will do in the product that they cannot do in the current tool, the metric that will show they did it (never page views), the comparison and window, and the smallest version. Record the discovery evidence the person gives: users spoken to, the moment watched, the step they cannot do today, quoted. If the person did not watch the moment, write "discovery evidence: step not observed" and stop the bet, as the old method requires. A stakeholder interview is recorded as an interview, not as an observation.

### Step 5. Value case (old DH-05.03.1.2.1)

Fill the value-case sheet: the decision and user, the current cost (time, errors or money) with its source, the expected change as the person's range or `[GAP]`, and the implementation cost elements as "not given" until supplied (Proctor 2011, CS38, DOI 10.1007/s10488-010-0319-7; NICE ESF standard 17, CS63, NHS context). No benchmark, typical saving or return comes from the model: no source in this skill gives one. If the person gives inputs and asks for arithmetic, call:

```
analytics.scenario-modeler {parameters: {<the person's names and values>}, formula: "<their formula, ** for powers>", periods: <n>, aggregate: "sum"}
```

Report each period and the total as "arithmetic on your inputs, not a forecast". A value case that needs QALYs or payer cost-effectiveness routes to `dh-access-and-value` economic-model-development.

### Step 6. Portfolio and rank (old DH-05.03.1.1 and DH-05.03.1.2.2 to .3)

Write the analytics portfolio list for the person's period: product, decision served, owner (or owner not named), now, next or later, the dependency that holds a later item, and the people the now items need. Flag as facts: an item with no decision; every item marked now; an item added while capacity is unchanged and nothing was delayed.

Ranking: write the person's priority rule back verbatim with the date it was written. If the rule is not given, nothing is ranked. With the person's scores, check them with `python3 scripts/metric_check.py rank --input SCORES.json` (stops on proposed scores; flags RICE confidence given as a fraction; prints tie points for weighted scores), then call:

```
analytics.rice {initiatives: [{id, reach, impact, confidence: <whole percent>, effort}, ...]}
analytics.mcda {alternatives: [{id, scores: {...}}], criteria_weights: {...}}
```

Confirm the library values match the script. Show the use case the rule placed last. Report the rank as "arithmetic on your scores, not a decision", with the tie points from the script. If the rule changed after the rank was seen, both ranks and both dates go in the record. What was funded, who decided and the value case for each one taken are recorded as the person states them; a funded use case with no value case is flagged as a fact.

## Build the output

Follow `assets/decision-frame-and-use-case-portfolio-output.md`. Answer first: the decision and the two actions as the person stated them (or "decision not given"), the first gap that stops later work, the value-case status (current cost sourced or `[GAP]`), and, for a set, the order on the person's rule with the closest tie point. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/metric_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The decision, actions, bet, inputs, rule, scores and funding are the person's, and the record says so.
- No benchmark, saving, return or target came from the model.
- Nothing proposed was ranked; the rule was written before the rank.
- Every statement about what would change the order comes from the script or shown arithmetic.
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- `python3 scripts/metric_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The method behind an analysis: `data-preparation-and-analytics-methods` (this pack).
- Payer economics: `dh-access-and-value` economic-model-development.
- The company's own medical products and programs as a product portfolio: `dh-strategy-and-portfolio` product-portfolio-prioritization.
- Measuring the bet after launch: `analytics-adoption-and-impact-monitoring` (this pack).
