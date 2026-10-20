# A2 Risk-share options

Framework task: DH-03.01.1.1, Part A, task A2. Replaces the earlier "Risk-Sharing Model Design" section.

## What this task delivers

The risk-share designs that fit the person's market and measures, each with how it pays, what it puts at risk, what it needs in data, and the known problems recorded for that kind of design. It answers "which ways of sharing risk are open to us, and what does each one cost and demand?"

Why it matters: a design chosen for its headline (pay for outcomes) can carry an administration bill larger than the value at stake, or a rule that turns missing data into lost payment. The OECD records both. Seeing the payment arithmetic side by side before negotiating changes what a team offers.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.1 Part A, Risk-share options |
| Workflow | The steps below |
| Knowledge | `references/risk-share-models.md` (OECD taxonomy and problems, German 20 percent component, ACCESS withhold); `references/outcomes-contracting-sources.md` |
| Tools | `scripts/payment_scenarios.py`; `analytics.budget-impact-model` (only on the person's inputs; see the known 422 error in `references/tools.md`) |
| Prompt | This guide |
| Template | `assets/risk-share-options-output.md` |
| Input | The request and its context; market and payer; A1 measures if run; the person's amount per patient, patient numbers and cost inputs if they want arithmetic |
| Governance | `references/governance.md`; every share, threshold and price is the person's; arithmetic is a hypothesis |

## Read the request

- **Market and payer**, as in A1. Germany carries a legal floor; ACCESS carries fixed CMS rules; other payers are open negotiation.
- **What is already fixed.** For a DiGA, any agreed price; for ACCESS, the track. Fixed terms are facts, not options.
- **Whether they want numbers.** Ask for their amount per patient, the attainment rates they want to test, and for budget impact their population, current mix and uptake. Never supply these yourself.

## Workflow

### Step 1. Place the request in the taxonomy

Name the kinds that apply (OECD): financial (not linked to performance) and performance-based (patient-level payment-by-result, population-level coverage with evidence development, conditional treatment continuation). Say the OECD paper covers medicines and is used here as lessons.

### Step 2. State the fixed rules for the market

- **Germany.** At least 20 percent of the negotiated DiGA amount must be outcome-dependent since 1 January 2026. The framework agreement still says "can" and sets no method; how AbEM feeds the component is not set; no arbitration ruling was found; payer and industry both flag the timing mismatch with AbEM data from 15 April 2027. Volume discount from 1 January 2027 is a separate, financial lever. Fund-level deals run under § 140a.
- **United States (ACCESS).** Annual allowed amount by track; the payment factor applies to the Medicare portion, 80 percent of the allowed amount (BH initial $144 of $180), never to the allowed amount; 50 percent of the Medicare portion withheld (BH initial $72) (OC "ACCESS: Medicare portion and payment basis"); full payment at 50 percent attainment; proportional below, reduction capped at 50 percent; substitute-spend cut capped at 25 percent, larger of the two applies; the care organization is the payee.
- **Other markets.** No outcome-linked payment for digital products was sourced; say so.

### Step 3. Lay out the options

For each design that fits, one row: how it pays, what share is at risk, the attainment rule it implies (patient level or population level), the data it needs, and the known problems from `references/risk-share-models.md` (burden, recouping, informative data, aggregation into evidence, CED track record). Include a financial-only option where the person's measures fail the data test; it is a legitimate answer.

### Step 4. Show the payment arithmetic (when the person gives numbers)

Write the person's designs and attainment rates into a JSON file in the shape of `examples/access_bh_designs.json` and run `python3 scripts/payment_scenarios.py designs.json`. Show what each design pays per patient at each attainment rate and what is lost. Without code execution, compute the same by hand: withhold design factor = 1 at or above threshold, else max(1 minus cap, attainment / threshold); fixed-plus-outcome factor = (1 minus outcome share) plus outcome share times the outcome part. For ACCESS, the base is the Medicare portion (BH initial $144), not the allowed amount. Label the table "hypothesis on your inputs".

### Step 5. Budget impact (only on the person's inputs)

If asked, call `analytics.budget-impact-model {eligible_population, current_mix: [{name, share, annual_cost_per_patient}], new_treatment_annual_cost_per_patient, uptake_curve}` with the person's numbers. If it returns an error (observed 422 on 19 October 2026), compute by hand and say the tool did not answer. Label every result "hypothesis on your inputs", show every input beside it, and never turn it into a price.

### Step 6. Name what the choice turns on

Two or three facts that would make one option clearly better: for example, "if AbEM PROMs are the only outcome data, a German outcome component tied to them cannot pay out before 2027"; "under an all-or-nothing patient rule, dropouts count as failures, so completeness becomes part of the price".

## Build the output

Follow `assets/risk-share-options-output.md`. Answer first: the options that fit, the fixed rule that constrains them, and what the choice turns on. Then the option table and, if numbers were given, the scenario table.

## Before you hand it over

- Every fixed rule cites its row.
- Every number in the arithmetic is the person's or a labeled public anchor (ACCESS parameter, German floor).
- Arithmetic is labeled a hypothesis; no option is called likely to be accepted.
- Choosing a design, any share or threshold, and any wording for a payer stop for the accountable owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model lays out options; it does not choose one or set its terms.
- No price for the person's product; no forecast of payment or uptake.
- Drugs, biologics and wellness apps are out of scope.
