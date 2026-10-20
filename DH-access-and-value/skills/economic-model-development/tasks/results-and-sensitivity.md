# B1 Results and sensitivity

Framework task: DH-01.07.2.1, Part B, task B1. Replaces the old "Model result" section (CF-12.01.07.2.1.3), whose rule stays as Step 1: report a result only from inputs already shown.

## What this task delivers

The results of the person's model, written so the decision-maker can judge them: the base case with its quadrant, net benefit at the thresholds the person chose, which inputs drive the result and at what value each would change the decision (switching values), the scenarios the person chose, what the analysis cannot show, and the reporting items a reviewer will look for. The judgment of acceptability stays with the decision-maker; this task makes that judgment informed.

Why it matters: a single ICER invites a single verdict, and a single verdict hides the input that decides it. NICE asks for switching values for technologies that iterate fast (HE-077) and early-use assessments ask which uncertainties drive the decision (HE-068). A results section that names its drivers is the one that gets a recommendation with evidence generation instead of a rejection.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.1 Part B, Results and sensitivity |
| Workflow | The steps below |
| Knowledge | A2 output; `references/model-build-rules.md` section 5; `references/reference-cases.md` |
| Tools | `analytics.risk-tornado`; `analytics.scenario-modeler`; `verify.build_record`; `scripts/sensitivity_summary.py` |
| Prompt | This guide |
| Template | `assets/results-and-sensitivity-output.md` |
| Input | The request and its context; the A2 register and runs; the person's thresholds, ranges and scenarios; the person's named owner |
| Governance | `references/governance.md`; thresholds, ranges, scenarios and conclusions are the person's and the decision-maker's |
| Catalogue job | none |

## The rule that shapes this task: the decision-maker judges

The person chooses the thresholds results are shown against, the ranges and the scenarios. The model computes, ranks inputs by how much they move the result, and finds switching values. It never writes "cost-effective", "good value", "dominant therefore recommended" or any verdict. Where the person asks for one, say whose call it is (for NICE, no precise maximum, HE-049) and give the arithmetic.

## Workflow

### Step 1. Results from inputs already shown

Take the A2 run. If no run exists, run A2 first in short mode. Report the base case only from inputs the person can see: totals per arm, increments, the quadrant, the ICER where it is a meaningful ratio (HE-041), and net health benefit at each threshold the person gave. Where NICE modifiers apply, the source asks for net health benefit at £25,000 and £35,000 with and without QALY weighting (HE-052); for a HealthTech topic say that the severity modifier is not applied initially (HE-053, HE-075).

### Step 2. Thresholds, shown as written

If the person reports against a body's threshold, show it as the body writes it, with the version: for a NICE HealthTech topic, both PMG48's £20,000 to £30,000 (HE-074) and PMG36's £25,000 to £35,000 (HE-050, HE-051), labeled an open conflict; for ICER, the $100,000 to $150,000 benchmark range (HE-118); for ICER-PHTI, the 15% savings, 3:1 ROI and cost-neutral threshold prices (HE-124). For HAS, no threshold in the passages read (HE-107). Position the result against each with arithmetic only.

### Step 3. One-way sensitivity on net benefit

Ask the person for a low and high value per input, with the reason (a confidence interval, a published range, a plausible assumption). Then:
- With code execution, run `scripts/sensitivity_summary.py model.json`: inputs sorted by swing in net monetary benefit at the person's threshold, whether net benefit changes sign, the switching value where it does, and quadrant changes.
- Otherwise call `analytics.risk-tornado` with a net monetary benefit formula (for example `wtp * d_qaly - d_cost`), the person's `parameter_ranges` for every input, `periods`, `aggregate: "sum"`. Never tornado the ICER ratio: a negative incremental QALY flips the ratio and the tool ranks it as a small swing (`references/tools.md`). List parameters are skipped by the tool; give a scalar multiplier if uptake or a time profile must vary. Inputs without a range get plus or minus 20 percent by default: say so, or pass ranges.
An input without a range is listed as "no range given", never varied on an invented range.

### Step 4. Switching values

For each input whose range crosses zero net benefit, report the switching value at the person's threshold (HE-077): the input value at which net monetary benefit is zero. Where none crosses, say "no switch within the ranges given". A switching value is information for the decision-maker, not a target.

### Step 5. Scenarios the person chose

Run each scenario the person names (HE-022 (DOI 10.1016/j.jval.2013.08.2291): scenarios chosen from the decision maker's perspective) with `scenarios` in the script, or one `analytics.scenario-modeler` call per scenario. Always offer the discount rate and time horizon scenarios CHEERS item 24 asks about (HE-013, DOI 10.1177/23814683211061097), and the body's own sensitivity rules where they exist: IQWiG 0% and 5%, optionally 3% costs and 1.5% benefits (HE-111); NICE 1.5% only if all three criteria hold (HE-048); no 3L utilities in NICE sensitivity or scenario analyses for new topics (HE-061); ICER-PHTI 2 to 5 year horizons where offsets accrue later (HE-122).

### Step 6. Say what the analysis cannot show

- Probabilistic sensitivity analysis: no tool or script here runs one. Say it was not run `[GAP]`; the ISPOR-SMDM uncertainty report is sourced at abstract level only (HE-015, DOI 10.1016/j.jval.2012.06.012).
- Value of information: name it as the method for valuing further evidence (HE-031, [PAPER] Fenwick et al. 2020, DOI 10.1016/j.jval.2020.01.001, abstract only); not computed here.
- Distributional effects (CHEERS item 19, HE-011, DOI 10.1177/23814683211061097): described only if the person supplies subgroup inputs.
- Structural uncertainty beyond the scenarios run.

### Step 7. Point the evidence work

List the two or three inputs that decide the result, and for each the evidence that would narrow its range (a trial, real-world data, a utility study), as advisory lines. For a NICE early-use topic, the source asks that uncertainties be resolvable within 3 years of publication (HE-072). Evidence generation belongs to dh-access-and-value DH-01.07.3 (real-world-outcomes-research) and dh-clinical-development (literature-and-real-world-evidence-review); point there.

### Step 8. Reporting items

For a report or a submission annex, tick which CHEERS 2022 items the draft covers among those the research file holds (items 4, 8 to 10, 15 to 17, 19 to 21, 24, 25, 27, 28; HE-006 to HE-014), and say that the other items are not sourced here and must be checked against the checklist (DOI 10.1177/23814683211061097). Never give a CHEERS score (HE-005). The sibling skill economic-model-validity-monitoring runs the full check.

## Build the output

Follow `assets/results-and-sensitivity-output.md`. Short mode: base case and quadrant, net benefit at the person's thresholds, the top drivers with switching values, the gaps, the stop and the record line.

## Before you hand it over

- No sentence says or implies the technology is cost-effective, good value or recommended.
- Every range and scenario is the person's, labeled so; default ranges are flagged.
- The ICER appears only with its quadrant; no tornado on a ratio.
- Count the words in short mode.
- Results for an HTA body, a payer or a commissioner stop for the owner the person named, labeled "draft for the owner"; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- Acceptability, recommendation and price are never the model's call.
- Value messages built on results belong to dh-access-and-value DH-01.07.4 (value-narrative-and-dossier) and dh-go-to-market (pricing-and-value-message-monitoring) and stop for the person's accountable owner.
- Drugs, biologics and wellness apps are out of scope.
