# A1 Outcome attainment tracking

Framework task: DH-03.01.1.2, Part A, task A1. Replaces the earlier "Outcomes Achievement Monitoring" section.

## What this task delivers

Attainment per measure and per patient against the contract's own rules, the attainment rate against the contract's threshold, and the payment effect, computed from the person's data. It supports both patient-level all-or-nothing rules (the ACCESS pattern) and population-average rules. It answers "where do we stand against our outcomes contract, and what would it pay today?"

Why it matters: under an all-or-nothing rule one missing value is one lost success, and near a threshold one patient can change the payment. Tracking that only reports average improvement hides both.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.2 Part A, Outcome attainment tracking |
| Workflow | The steps below |
| Knowledge | `references/attainment-rules.md` (the two rule families, ACCESS rules, the German component); `references/outcomes-contracting-sources.md` |
| Tools | `scripts/attainment.py`; no library call (the library holds no contract data, and patient data never goes into one) |
| Prompt | This guide |
| Template | `assets/outcome-attainment-tracking-output.md` |
| Input | The request and its context; the contract's rules (measures, targets, threshold, missing-data rule, payment link); the person's de-identified patient data or per-measure counts |
| Governance | `references/governance.md`; the contract's rules decide; attainment is not clinical evidence |

## Read the request

- **The rules.** Ask for the contract's rules in the person's words: measures and targets, patient-level or population-level, threshold, what happens to missing values and dropouts, windows, payment link. If the contract is an ACCESS participation, the CMS rules apply and are in `references/attainment-rules.md`; confirm the track. For ACCESS, also ask for (a) every required measure on the track, including submission-only measures such as PGIC on BH, and (b) the reason for each unalignment, because relocation and ineligibility leave the denominator while self-initiated unalignment stays (OC "ACCESS: PGIC, submission-only measure, Table 5"; OC "ACCESS: denominator exclusions"). If either is missing, list it as an open item that can change the rate, and give the rate both ways. If the contract is silent on a case, ask; do not choose.
- **The data.** De-identified patient rows (one row per patient, baseline and final per measure, status) or aggregated counts. Do not ask for names or identifiers. If only aggregates are given, compute what they allow and say what needs patient rows.
- **Interim or final.** An interim count is a position, not a result. Say which it is.

## Workflow

### Step 1. Write the rules back

Put the rules into a table (measure, target, applies if, window, self-report allowed, missing treated as, lost in denominator, threshold, payment). Mark every rule "as you gave it" or "ACCESS rule, row". Mark cases the contract leaves open `[GAP]` and ask. Get confirmation before computing.

### Step 2. Prepare the data

Map the person's columns to `patient_id`, `status`, and `<measure>_baseline`, `<measure>_final`, optional `<measure>_final_day` and `<measure>_self_report`. Check for impossible values (scores outside the instrument range, final days before baseline) and ask about them rather than dropping rows.

### Step 3. Compute

With code execution, write the rules into a JSON in the shape of `examples/bh_rules_access_style.json` (patient level) or `examples/bh_rules_population.json` (population level) and run `python3 scripts/attainment.py patients.csv rules.json`. Without it, compute by hand:

- **Patient level.** For each patient and measure: met, not met, missing (baseline, final, out of window, self-report not allowed) or not applicable. For ACCESS BH, a baseline under 10 takes the control target (final under 10), not "not applicable"; in the rules JSON this is `"target_below": {"type": "final_below", "value": 10}`. If the person's contract drops the measure instead, run it both ways and say whether the result changes. A patient succeeds only if every required measure is met. Rate = successes / denominator, with dropouts in or out as the contract says.
- **Population level.** For each measure, the mean change among patients with valid data, compared with the target; count the missing.

### Step 4. The payment effect

Apply the contract's payment link to the rate. For the ACCESS pattern: full payment at or above the threshold; below it, rate / threshold of full payment, reduction capped at the contract's cap (50 percent in ACCESS). State it as "what the rules would pay on this data", never as what will be paid. For ACCESS dollars, apply the factor to the Medicare portion (80 percent of the allowed amount; BH initial $144), not to the allowed amount: earned = factor x $144, of which $72 was the withhold (OC "ACCESS: Medicare portion and payment basis"). Patients with fewer billed months accrue less; say so. If a second adjustment exists (ACCESS substitute spend), say it is not computed here unless the person gives the data, and that only the larger adjustment applies.

### Step 5. Distance to the threshold

State how many patients separate the rate from the threshold in each direction ("one more failure puts the rate at 45 percent and the factor at 90 percent"). This is arithmetic on the current denominator, not a forecast.

### Step 6. Hand off

Missing values and dropouts go to A2 for their effect. Verdicts against the person's review rules go to B1.

## Build the output

Follow `assets/outcome-attainment-tracking-output.md`. Answer first: the attainment rate against the threshold, the payment factor the rules give, the dollars on the Medicare-portion basis for ACCESS, and the distance to the threshold. Short mode then gives the per-measure table, open items and the record line; the rules list and the per-patient table go in full mode.

## Before you hand it over

- Every rule is the contract's (as given) or a cited public rule the contract uses.
- Every number comes from the person's data through the stated computation.
- Interim results are labeled interim.
- Attainment is described as attainment under the contract, not as clinical effect.
- Patient-level rows stay in the conversation; any record holds aggregates only.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No imputation of missing values; no dropping of patients the contract keeps.
- No forecast of the final rate.
- Drugs, biologics and wellness apps are out of scope.
