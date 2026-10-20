# A2 Model inputs and runs

Framework task: DH-01.07.2.1, Part A, task A2. Replaces the old "Model inputs" (CF-12.01.07.2.1.2), "Run a budget impact model" (CF-12.01.07.2.1.4) and "Run a launch price anchor" (CF-12.01.07.2.1.5) sections. Their rules stay as steps: list every input and leave a blank input blank; collect the population, the current mix, the new-treatment cost and the uptake curve from the buyer and show every input beside the net impact; collect the comparator cost, the incremental QALYs and the thresholds from the buyer, and the result is a ceiling, not a launched price.

## What this task delivers

An input register with the source and check status of every number, and deterministic runs on those numbers: budget impact, cost-utility or cost-comparison, and, only if asked, a value-based price ceiling. Each result sits beside its inputs, names the tool or script that computed it, and is labeled a hypothesis on the person's inputs.

Why it matters: a model is only as defensible as its least-checked input. A reviewer who finds one unsourced utility or one hidden default stops trusting every other number. A register with a source for every input, and arithmetic another modeler can replicate (HE-024, DOI 10.1016/j.jval.2013.08.2291), is what survives review.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.1 Part A, Model inputs and runs |
| Workflow | The steps below |
| Knowledge | `references/model-build-rules.md` sections 3 to 6; `references/reference-cases.md`; A1 output if it exists |
| Tools | `analytics.budget-impact-model`; `analytics.scenario-modeler`; `analytics.vba-price-anchor` (only if asked); `verify.qualify_source` and `verify.check_claim` for published inputs; `verify.build_record`; `scripts/he_model.py` |
| Prompt | This guide |
| Template | `assets/model-run-output.md` |
| Input | The request and its context; the A1 frame; the person's numbers (costs, effects, utilities, population, uptake, horizon, discount convention, thresholds) and the sources they cite |
| Governance | `references/governance.md` |
| Catalogue job | `budget-impact` for the budget impact run and `price-anchor` for the ceiling (both `available`; `start_job` returns the steps and runs nothing); none for cost-utility |

## Read the request

- **Which run?** "Budget impact", "what will it cost the plan", "net impact" is Step 4. "ICER", "cost per QALY", "cost-utility", "is it cost-saving" is Step 5. "How high can the price go", "value-based price" is Step 6. Several at once is fine.
- **Is there a frame?** If A1 has not run and the decision-maker is unknown, ask which body the model is for, or run with the person's stated perspective and discounting and say the reference case was not checked.
- **Which numbers are theirs?** Every number must come from the person or from a source they adopt. If the person asks the skill to "use typical values", decline that part and list the inputs needed.
- **Short or full?** A direct question gets short mode; a model report or technical appendix gets full mode.

## Workflow

### Step 1. Build the input register

One row per input: name, value, unit, year of the value, currency and conversion year (CHEERS item 15, HE-008, DOI 10.1177/23814683211061097), source kind (person's data, person's assumption, published study, real-world evidence, value set), source, check status. A blank input stays blank and is `[GAP]`; never put zero in its place without saying so. With code execution, the register's numbers go into the model JSON for `scripts/he_model.py` (see `examples/inputs/dcbti_model_illustrative.json`).

### Step 2. Check the published inputs

For each input from a paper: `verify.qualify_source` with the DOI, then `verify.check_claim` with the input as a claim, the verbatim passage (`text`, `locator`) and the full returned source object. Accept it only when you have read the passage and it states the figure in the same direction (register N3); a "partial" or "unsupported" leaves the input `[GAP]` with the reason. Cite from the `qualify_source` result (register C18). If the input needs a review or a pooled estimate, point to dh-clinical-validation (`literature-and-real-world-evidence-review`). For a real-world input, ask whether the study was declared hypothesis-evaluating with a registered protocol (HE-026, HE-027, DOI 10.1002/pds.4297).

### Step 3. Check the inputs against the reference case

Using the A1 frame or `reference-cases.md`: costs inside the stated perspective (for NICE, NHS and PSS, HE-037; productivity costs separate, HE-038); utilities from the value set the body requires (UK 5L under PMG51 for new NICE topics, HE-058; French 5L at HAS, HE-106); discount rate and convention as the person chose them with the body's rate beside it (NICE 3.5%, HE-047; HAS 2.5%, HE-105; IQWiG 3% after year 1, HE-111; ICER 3%, HE-117). A mismatch is reported, not corrected: the person decides.

### Step 4. Budget impact

1. Write the HE-019 (DOI 10.1016/j.jval.2013.08.2291) elements from the register: eligible population, current mix with shares and costs, new-treatment cost, uptake by year, condition-related cost change. For NICE ESF, add the HE-088 cost lines (purchase, updating, maintenance, staffing, training, IT).
2. Call `analytics.budget-impact-model` once with `eligible_population`, `current_mix`, `new_treatment_annual_cost_per_patient`, `uptake_curve`. On 19 October 2026 it returned HTTP 422 on every shape tried (register N5).
3. On 422, call `analytics.scenario-modeler` with the person's numbers and a formula such as `population * uptake * (new_cost - mix_cost + condition_change)`, `uptake` as a per-year list, `aggregate: "cumulative"`. Use `**`, never `^` (HTTP 400). With code execution, `scripts/he_model.py` gives the same table and the year-by-year inputs; in the live test both returned 65,000, 130,000 and 195,000 on the illustrative inputs.
4. Report each year's net impact beside its inputs, the horizon and the perspective, undiscounted unless the person or the body says otherwise. State the displacement assumption (proportional to current shares) for the person to confirm. Where the body names a horizon, say it: ICER-PHTI 1 year with 2 to 5 year scenarios (HE-122), IQWiG at least 3 years (HE-112), AMCP draft 1 to 3 years with PMPM (HE-138).

### Step 5. Cost-utility or cost-comparison

1. With code execution, run `scripts/he_model.py model.json`: totals per arm, discounted and undiscounted; incremental cost and QALYs; the quadrant; the ICER only where it is a meaningful ratio (HE-041); net health benefit and net monetary benefit at each threshold the person gave; a fully incremental analysis when there are more than two options (HE-039).
2. Without code execution, call `analytics.scenario-modeler` once per arm with per-year cost and QALY formulas discounted as `value / (1 + r) ** t`, then compute the increments in the conversation and show every line.
3. Cost-comparison (HE-042, HE-056): report the cost difference and the evidence the person cites for similar benefit; the benefit judgment is the decision-maker's.
4. No threshold given: report increments and the quadrant only; net benefit stays `[GAP]`.

### Step 6. Value-based price ceiling (only when asked)

Call `analytics.vba-price-anchor` with the person's `comparator_cost_per_patient`, `incremental_qalys` and `wtp_thresholds` as a plain list. Report each ceiling with its threshold and the fixed defaults (offset 0, units 1). Say that the tool's own citation names the old NICE manual title and is not a threshold source, that the ceiling is not a price, and that price positions stop for the owner the person names for pricing, or owner not named (dh-commercial pricing-and-value-proposition; payer prices dh-market-access coding-pricing-and-payer-contracting).

### Step 7. Verify the calculations

Where a tool and the script both ran, compare the numbers and say whether they match. Verification of the calculations is the BIA II minimum alongside face validity with decision makers (HE-023, DOI 10.1016/j.jval.2013.08.2291). If they differ, report both and the input that explains it; never pick one silently.

## Build the output

Follow `assets/model-run-output.md`. Short mode: the answer, the key inputs with sources, the results with tool names, the gaps, the record line.

## Before you hand it over

- Every number traces to the register, and every register row has a source kind; no input is from memory.
- Every result names the tool or script, its inputs and "hypothesis".
- The ICER is never shown without its quadrant; no result is called cost-effective.
- Count the words in short mode.
- If the output leaves the conversation, it stops for the owner the person named; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- No input is supplied by the model; "typical values" are declined and the needed inputs listed.
- A ceiling or a comparator price is never the person's price.
- Probabilistic sensitivity analysis is not run by any tool or script here; see task B1.
- Drugs, biologics and wellness apps are out of scope.
