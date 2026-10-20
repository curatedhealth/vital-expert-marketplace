# B1 Vision and option choice

Framework task: DH-01.05.1.1, Part B, task B1. Carries the old tasks "DH-01.05.1.1.2 Strategic Vision Articulation" and the decision half of "DH-01.05.1.1.3 Build-Partner-Buy Assessment".

## What this task delivers

The person's vision written back in their words with its objectives checked against the SMART elements (UK public-sector guidance, SP-092); their options ranked on their own criteria, weights and scores (`analytics.mcda` or `analytics.rice`), with the swap points that would change the order; a sensitivity run on their own inputs and ranges (`analytics.scenario-modeler`, `analytics.risk-tornado`); and a decision record of what they chose, who decided, dissent, conditions and open items. It answers "what is our vision, how do our options compare on our own terms, and what did we decide?"

Why it matters: MCDA is meant to help decision makers reach "their decision, not the tool's decision" (SP-080, ISPOR MCDA Report 2 [WF], DOI 10.1016/j.jval.2015.12.016). A rank produced from scores the model invented, or a success rate borrowed as the team's probability, puts the model's numbers in the team's mouth.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `chief-digital-health-officer` (old DH-01.05.1.1.2); `chief-compliance-officer-digital-health` (old DH-01.05.1.1.3). Work as a strategy analyst who computes on the person's numbers |
| Skill | DH-01.05.1.1 Part B, Vision and option choice |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/option-frameworks.md` sections 4, 7 and 8; rows SP-074 to SP-087, SP-088 to SP-098, SP-170 to SP-176; `references/governance.md` |
| Tools | `analytics.mcda` or `analytics.rice` (only on the person's scores); `analytics.scenario-modeler` and `analytics.risk-tornado` (only on the person's inputs and ranges); `verify.build_record` when the record leaves; `scripts/options_check.py rank`, `tornado`, `words` |
| Prompt | This guide |
| Template | `assets/vision-and-option-choice-output.md` |
| Input | The request and its context: the vision text, objectives and horizon, the options (A1), criteria, weights, scores and who scored them, inputs and ranges for sensitivity, the decision, decider, date, dissent and conditions |
| Governance | `references/governance.md`; the person decides |
| Catalogue job | none (`partner-prioritization` is scoped to partners and indications; call the calculators directly) |

## The rule that shapes this task: people decide

The vision, the criteria, weights, scores, ranges and the choice are the person's. The model writes them back, checks them, computes, and records. It never writes the vision for the person unless asked, and then labels each sentence "proposed"; it never ranks proposed scores; it never names the winner. When the arithmetic is close or the swap points sit near the person's weights, it says so as a fact and writes "your call".

## Workflow

### Step 1. Vision and objectives back

Write the vision verbatim. List each objective with the SMART elements present or "not given" (specific, measurable, achievable, realistic, time-limited; SP-092, UK public-sector guidance used as a checklist). The horizon is the person's; if not given, "not given". If asked for draft wording, offer it labeled "proposed", built only from the person's opportunity and objectives.

### Step 2. Check the scoring set

With code execution, put the person's set in the `rank` input shape and run `python3 scripts/options_check.py rank --input SCORES.json`. It stops if weights do not sum to 1 or scores are labeled proposed, lists options not scored on every criterion as "not ranked" and, for each, prints its sum on the criteria it was scored on and the score on each missing criterion at which it would tie each ranked option (arithmetic on the person's scores; the missing score is never filled in), and reminds that every criterion is read as higher-is-better (register C17). Write back criteria and weights, who scored and when. ISPOR good practice (SP-074 to SP-081 [WF]) is a checklist: criteria cover the decision, no double counting, preference independence, weighting method, consistency checks. Name what is missing; never fix it silently.

### Step 3. Rank what the person scored

Call `analytics.mcda {alternatives: [...], criteria_weights: {...}}` with the person's scores, or `analytics.rice {initiatives: [...]}` if they scored with RICE (confidence as a whole percent). Confirm the library values match the script ("analytics.mcda values match this arithmetic"). Report value and contributions, options not ranked and why with their tie scores, ties, and the swap points from the script. Never say first place holds while an unranked option's tie score lies inside the scoring scale; say instead which empty cell decides the top (for example "Acquire scores 77.5 on the four criteria scored; any capital need avoided score above 0.5 of 4 puts it first"). Label it "arithmetic on your scores, not a decision".

### Step 4. Stress-test the person's inputs

If the person gives a cost, benefit or value model for the options, run it with `analytics.scenario-modeler {parameters, formula, periods, aggregate}` (use `**` for powers) and `analytics.risk-tornado {..., parameter_ranges}` with the person's ranges for every parameter. Run `python3 scripts/options_check.py tornado --file SAVED.json` and report the flags: R1 default range not the person's, R2 list parameter skipped, R3 output changes sign, R4 ratio formula. Optimism bias: the Green Book asks appraisers to raise costs and timeframes and lower benefits (HM Treasury Green Book, 5 February 2026, SP-096). If the person asks for the standard uplift, quote the supplementary guidance table for the project type they name (`option-frameworks.md` section 4; software and ICT are "equipment/development": 54% duration and 200% capital expenditure upper bounds, 10% and 10% lower, SP-172, SP-173), the start-at-upper-bound and mitigation method (SP-175), its age (2003 PDF, 2002 data, SP-170) and that no bound exists for operating costs or benefits shortfall, where switching values are used instead (SP-176). All labeled UK public-sector guidance. The uplift applied and the project type are the person's.

If the person asks for an NPV or a probability but gives no model, write back the input sheet per option, each item "not given": costs and their timing, license fees or royalties, uptake, price, discount rate, the optimism bias uplift they choose, and any probability with its counting basis (path-by-path or phase-by-phase, Wong, Siah and Lo 2019, SP-085). Add the formula shape `analytics.scenario-modeler` takes (named `parameters`, a `formula` using `**` for powers and `t` for the period from 0, `periods`, `aggregate`), so the owner can fill it in one pass. Supply no number in it.

### Step 5. Benchmarks the person asks about

If the person asks for a success rate, quote it with its counting method, population and DOI (SP-082 to SP-087), say it covers drug programs, that no sourced rate exists for digital health or device programs `[GAP]`, and that it is context, never their probability. If the person supplies their own probability, it goes into their model labeled as theirs.

### Step 6. Decision record

Write the decision, decider, date, attendees, dissent and conditions as stated; "not given" where missing. Open items with the owner the person named (or owner not named) and the date they set (or "not given"). If the choice is a license or collaboration, carry the A1 licensing facts as items for the owner the person names for legal or competition matters. If the choice is an acquisition or investment, route the deal work to `investment-memo-and-decision-record` (this pack). Tracking the choice afterwards: `strategy-execution-monitoring` (this pack).

## Build the output

Follow `assets/vision-and-option-choice-output.md`. Answer first: the vision in one line as the person wrote it, the order of the options on their scores with the closest swap point and any unranked option's tie score (which empty cell decides the top), the input that moves the result most on their ranges, and the decision as stated (or "decision not given"). Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Vision, objectives, criteria, weights, scores, ranges and the decision are the person's, and the record says so.
- Nothing proposed was ranked; unscored options are listed as not ranked, with their tie scores from the script.
- Every statement about what would change the order is computed (script output or shown arithmetic), never estimated.
- Every fact names its source and date in plain words with the row id after it.
- No winner is named; no probability is the person's unless they gave it.
- Every default range in a tornado is flagged as not the person's.
- Green Book terms are labeled UK public-sector guidance.
- `python3 scripts/options_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Ranking the company's own products and programs against each other: `product-portfolio-prioritization` (this pack).
- Acquisition or investment decisions: `investment-memo-and-decision-record` (this pack).
- Health economic models behind a value input: `dh-access-and-value` economic-model-development.
- Any wording for a board, investors, partners or the press: stops for the owner the person names.
