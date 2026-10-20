# A2 Statistical and causal analysis plan

Framework task: DH-05.01.1 Statistical Modeling & Inference, Part A, task A2. Carries the old tasks "DH-05.01.1.1.1 Causal question", "DH-05.01.1.1.2 Design choice", "DH-05.01.1.1.3 Estimate record", "DH-05.01.1.2.1 Model target", "DH-05.01.1.2.2 Fit and check", "DH-05.01.1.2.3 Model limit", "DH-05.01.1.3.1 Uncertainty question", "DH-05.01.1.3.2 Posterior or interval" and "DH-05.01.1.3.3 Sensitivity of the prior".

## What this task delivers

The question written before the method (treatment or exposure, outcome, population, the decision it changes, confounders seen and unseen, the estimand attributes); the design the data can support, or a refusal of the causal claim with what will be estimated instead; for a regression, the target, unit of row, predictors used and not used, the use, the sample and the check; for an uncertainty question, the quantity, the person's threshold and prior with its source, the posterior or interval computed, and the result under each alternative prior the person names; and the estimate record (estimate, interval, sample, the assumption that would reverse the decision, data and code version). It answers "what exactly are we estimating, can our data support it, and how sure are we?"

Why it matters: an observational association reported as an effect, or a prior nobody can cite, moves decisions the data cannot carry. The old tasks put it plainly: "Do not call an observational association an effect" and "Do not hide the result that reverses the decision."

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-healthcare-researcher` (old DH-05.01.1.1.1 to DH-05.01.1.3.3). Work as a statistician who writes the question and the plan before any estimate |
| Skill | DH-05.01.1 in this competency, Part A, Statistical and causal analysis plan |
| Workflow | The steps below |
| Knowledge | `references/analysis-methods.md` sections 1 to 5; rows CV31 to CV41, CV73 to CV75, CV88, CV89, DA-121 to DA-131, DA-132, DA-137, DA-139 |
| Tools | `scripts/prep_check.py bayes`; optional `literature.get_record` for a method paper the person names; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/statistical-and-causal-analysis-plan-output.md` |
| Input | The request and its context: the question, the data (A1 handoff or the person's description), whether assignment was randomized, the outcome, the covariates, the person's threshold, prior and alternatives, the decision rule, the data version |
| Governance | `references/governance.md`; the question, design, prior, threshold and decision rule are the person's |
| Catalogue job | none |

## Read the request

- **The decision.** What the answer will change, and who decides. If not given, ask.
- **Assignment.** Randomized by the person, a natural experiment, or routine-practice rows only. This fact decides what can be claimed.
- **Product type.** Drug or biologic, device, or an analytics model with no regulated use: it decides which FDA guidance applies (covariates DA-121 and Bayesian drug draft DA-129 are drug documents; Bayesian device guidance DA-126 is the device document). Label anything else context.
- **Numbers.** The threshold, the prior and its source, the decision probability: the person's or "not given". Never fill.

## Workflow

### Step 1. The question (old "Causal question", "Model target", "Uncertainty question")

Write the question in the person's words, then the five estimand attributes (CV33, CV34): treatment and comparator, population, variable, how intercurrent events are handled (treatment policy, hypothetical, composite, while on treatment, principal stratum; CV35 to CV39), population-level summary. ICH E9(R1) is a trial addendum; for observational analytics it is a checklist and labeled so. Name one confounder the data hold and one they do not (old task). For a regression: outcome, unit of row, predictors used and those left out with the reason, and the use (description or prediction).

### Step 2. The design the data can support (old "Design choice")

State the assignment fact. With randomization, an effect estimate is supported by design; adjustment for prognostic covariates and strata is prespecified before unblinding, and an unadjusted primary analysis is acceptable (DA-122 to DA-125; drug guidance, context for devices). With routine-practice rows only, a causal claim stands only if the person names the design and its assumptions; no source row in this skill gives those assumptions (`[GAP]`). If the design cannot support a causal claim, refuse it in one sentence and say what is estimated instead (an association, adjusted for the covariates named). For a submission-grade RWE study, the protocol and analysis plan are finalized before the analysis (CV75, drugs; CV88 and CV89 for devices) and the study design routes to `dh-clinical-development` study-protocol-and-endpoint-design.

### Step 3. Fit, check and limit (old "Fit and check", "Model limit")

Record the fitting sample and, for prediction, the stated holdout; the assumption checked (linearity, separation, leakage) that would invalidate the use; and the metric matching the use, chosen before seeing results (old task). For a measure the analytics team will publish, describe scoring direction (DA-137) and note that descriptive statistics show data exist but are not evidence of reliability or validity (DA-139; CMS, context). Write where the model must not be used (population or period outside the sample, decisions it must not drive) and who may promote it: the person named, or owner not named. If the person names a method paper, read it with `literature.get_record {doi}` and quote only what a passage states.

### Step 4. Uncertainty and the prior (old "Posterior or interval", "Sensitivity of the prior")

For a rate with a beta prior, run `python3 scripts/prep_check.py bayes --successes K --n N --prior A B [--alt-prior A2 B2 ...] --threshold T --decision-prob C` with the person's numbers. Report the posterior mean, the equal-tailed interval at the level the person names (`--interval`; the script prints the level it used), the probability of crossing the person's threshold, and whether the person's rule gives the same answer under every prior. If it does not, keep both results and say which prior reverses it (old task). A prior must have a source the person can cite; if not, write "prior source not given" and ask. For a device study, the prior and model are prespecified and agreed with FDA and operating characteristics are evaluated (DA-127, DA-128; final, 5 February 2010). For a drug or biologic, the January 2026 draft frames success as Pr(d > a) > c and allows calibration to type I error (DA-130, DA-131, draft). The two are not cross-applied. Other models (hierarchical, continuous outcomes): the person's software output is reported as given; the skill does not refit it.

### Step 5. Estimate record (old "Estimate record")

Estimate, interval, sample, the breaking assumption, the data version (from A1) and the code reference. A point estimate alone is not recorded.

## Build the output

Follow `assets/statistical-and-causal-analysis-plan-output.md`. Answer first: what can be claimed from this design (effect or association), the estimate with its interval as computed, and whether the person's decision holds under every prior they named. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The question and estimand come before any method; the design fact (randomized or not) is stated.
- No causal word for an association; refusals say what is estimated instead.
- Priors, thresholds and decision probabilities are the person's; the script computed every posterior figure.
- Drug documents are labeled drug documents; drafts say "draft".
- `python3 scripts/prep_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Trial protocols, sample size and trial estimands for a regulatory study: `dh-clinical-development` study-protocol-and-endpoint-design.
- Real-world evidence reviews: `dh-clinical-development` literature-and-real-world-evidence-review.
- Economic models: `dh-access-and-value` economic-model-development.
