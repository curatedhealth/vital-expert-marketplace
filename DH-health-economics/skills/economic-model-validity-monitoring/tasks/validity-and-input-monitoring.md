# A2 Validity and input monitoring

Framework task: DH-01.07.2.2, Part A, task A2. Replaces the validity half of the old "Model validity check" section (CF-12.01.07.2.2.1) and adds the cost-effectiveness monitoring the competency title names. The old rule stays: check the inputs already shown; do not replace a buyer input.

## What this task delivers

Two things. **Validity:** which of the five validation types (face, verification, cross, external, predictive; HE-017, DOI 10.1016/j.jval.2012.04.012) the model has evidence for, and an independent recomputation of its reported numbers from its inputs. **Monitoring:** the model's key assumptions set beside the values the person has since observed, the base case re-run with those values, and which observed values have crossed a switching value at the person's threshold. The model is never declared valid or invalid; the evidence for each type is laid out.

Why it matters: a model built before launch rests on assumed uptake, assumed savings and trial utilities. Once real-world data arrive, the question changes from "was the model built right" to "does it still hold". The source calls external and predictive validity the strongest forms (HE-017, DOI 10.1016/j.jval.2012.04.012), and both need observed data the model never had.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.2 Part A, Validity and input monitoring |
| Workflow | The steps below |
| Knowledge | `references/validity-rules.md` sections 2, 3 and 5; `references/reference-cases.md` |
| Tools | `analytics.scenario-modeler`; `analytics.risk-tornado` (only to reproduce a reported tornado); `verify.qualify_source`, `verify.check_claim`, `verify.check_currency` for observed values from a published study; `verify.build_record`; `scripts/he_model.py`, `scripts/sensitivity_summary.py` |
| Prompt | This guide |
| Template | `assets/validity-monitoring-output.md` |
| Input | The request and its context; the model's inputs and reported results (file or table); validation evidence the person holds; the person's observed values with their source and period; the person's threshold and any monitoring triggers |
| Governance | `references/governance.md` |
| Catalogue job | none |

## Read the request

- **Validity, monitoring or both?** "Is our model valid", "will the reviewer trust it" is Steps 1 to 3. "Does the model still hold", "our real-world data are in", "re-run with actuals" is Steps 4 to 6.
- **Is the model available?** Recomputation needs the inputs and the structure. A summary allows only Steps 1 and 3; say so.
- **Observed values whose?** Each observed value needs its source, period and population. The skill never estimates one.
- **Short or full?** Direct question: short. Review pack: full.

## Workflow

### Step 1. Evidence per validation type

For each type in HE-017 (DOI 10.1016/j.jval.2012.04.012), record what the person or the document shows: face validity (who reviewed structure, data, assumptions and results; for a BIA, face validity with decision makers is the minimum, HE-023, DOI 10.1016/j.jval.2013.08.2291), verification (any coding check), cross validity (comparison with another model of the same problem the person names), external validity (comparison with real-world results), predictive validity (comparison with prospectively observed events). Mark each: evidence shown, claimed without evidence, or none `[GAP]`. Cite HE-017 as abstract only.

### Step 2. Recompute the reported numbers

With code execution, write the model's inputs into the `scripts/he_model.py` JSON format and run it; compare totals, increments, ICER or quadrant, net benefit and budget impact with the reported figures. Without code execution, rebuild the key arithmetic as one `analytics.scenario-modeler` formula per arm or per BIA (powers with `**`). Report match or difference for each number. A difference is a finding with the likely input or convention behind it (for example first-year discounting); never correct the model's number silently.

### Step 3. Transparency and replicability

Is a non-technical description available, and is technical documentation available openly or under agreement (HE-016, DOI 10.1016/j.jval.2012.04.012); is the BIA reported in enough detail to replicate (HE-024, DOI 10.1016/j.jval.2013.08.2291); does the document say whether the model is publicly available (CHEERS item 16, HE-009, DOI 10.1177/23814683211061097)? One line each.

### Step 4. Assumptions versus observed values

Table the model's key assumptions (from its inputs or the person's list) beside the observed value, its source, period and population. For an observed value from a published study, qualify the DOI and check the passage in the same direction (register N3), and run `verify.check_currency` before relying on it. For an observed value from real-world data, record whether the study was declared hypothesis-evaluating with a registered protocol (HE-026, HE-027; [PAPER] Berger et al. 2017, DOI 10.1002/pds.4297) and whether it used a different data source from the one behind the assumption (HE-029). Never mix a national average or another product's figure in as the person's observed value.

### Step 5. Re-run with observed values

Run each observed value, and all of them together, as scenarios: `scripts/sensitivity_summary.py` with a `scenarios` list, or one `analytics.scenario-modeler` call per scenario. Report increments, quadrant, ICER where meaningful and net benefit at the person's threshold beside the base case. Where the decision-maker is NICE, add one line with both written ranges as an open conflict (HE-074; HE-050, HE-051) and that NICE uses no precise maximum (HE-049). Where the observed values cover fewer years than the horizon, say so and propose (labeled "proposed") a scenario that holds them only for the observed period. In the illustrative run (`examples/monitoring-sleepwell-illustrative.md`), observed values moved the result from the dominant quadrant to north-east with ICER 2,283.

### Step 6. Triggers and switching values

If the person set monitoring triggers (for example a switching value from the build, HE-077), mark which observed values crossed them. If not, compute switching values on the person's ranges and say none are triggers until the person adopts them. A crossed trigger is a finding for the owner the person names for the decision (or owner not named), not a verdict.

## Build the output

Follow `assets/validity-monitoring-output.md`. Short mode: the answer, the validation evidence by type in one table, recomputation matches, the observed-value re-run, triggers crossed, gaps, record line.

## Before you hand it over

- No "the model is valid" or "the model is invalid"; evidence per type only.
- Every recomputed number names the script or tool; every observed value names its source and period.
- No input changed; differences reported.
- Count the words in short mode.
- Results for an HTA body, payer or commissioner stop for the owner the person named; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- Real-world study design and execution belong to dh-health-economics DH-01.07.3 (real-world-outcomes-research) and dh-clinical-validation (literature-and-real-world-evidence-review); outcomes-based payments to dh-market-access outcomes-contract-monitoring.
- Uptake or persistence is not clinical evidence.
- Drugs, biologics and wellness apps are out of scope.
