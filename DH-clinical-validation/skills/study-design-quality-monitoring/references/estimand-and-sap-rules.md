# Estimand and statistical analysis plan rules

Interpretive reference shared with the sibling design skill; used here by A1 to check that the estimand and SAP items are present, never to choose them. ICH E9(R1), the estimands addendum, was adopted on 20 November 2019 (CV31). The FDA DHT guidance says late-phase trials should use the E9(R1) estimand framework (CV59). These rows define what must be specified and the options; which option fits the clinical question is the decision of the person and the owner they name for statistics.

## 1. The five estimand attributes

| Attribute | Source wording | Rows |
|---|---|---|
| Treatment condition | "The treatment condition of interest and, as appropriate, the alternative treatment condition to which comparison will be made" | CV33 |
| Population | "The population of patients targeted by the clinical question." | CV33 |
| Variable (endpoint) | "The variable (or endpoint) to be obtained for each patient that is required to address the clinical question." | CV33 |
| Intercurrent events and their handling | Remaining intercurrent events are handled by strategy (treatment policy, hypothetical or while on treatment, among others). | CV34 |
| Population-level summary | "a population-level summary for the variable should be specified, providing a basis for comparison between treatment conditions" | CV34 |

Intercurrent events occur after treatment starts and affect the interpretation or existence of the measurements, for example stopping treatment or using another therapy (CV32).

## 2. The strategies for an intercurrent event

| Strategy | What it means | Rows |
|---|---|---|
| Treatment policy | The event is irrelevant; the value is used whether or not it occurred. | CV35 |
| Hypothetical | The value the variable would have taken had the event not occurred. | CV36 |
| Composite variable | The event is informative about outcome and is built into the variable. | CV37 |
| While on treatment | Only response before the event is of interest. | CV38 |
| Principal stratum | The target population is the stratum in which the event would (or would not) occur. | CV39 |

For a digital product, candidate intercurrent events include stopping use of the app, starting another treatment, and device or connectivity failure. Which events matter and which strategy answers the question are the person's decisions; the model lists events the person names and the strategies, with what each would mean for the claim.

## 3. What the protocol and SAP must prespecify

| Rule | Rows |
|---|---|
| The protocol defines a primary estimand matching the primary objective; protocol and SAP prespecify the main estimator aligned with it and a sensitivity analysis for its assumptions. | CV40 |
| Missing data are defined relative to a specific estimand. | CV41 |
| Have a plan to reduce missing data; collect reasons for missing COA data to inform sensitivity analyses. | CV59, PE-21 |
| SPIRIT items: statistical methods including harms (27a), who is in each analysis and in which group (27b), handling of missing data (27c), additional analyses (27d), sample size with all assumptions (19), interim analyses and stopping guidelines (28b). | SP-27a, SP-27b, SP-27c, SP-27d, SP-19, SP-28b |
| CONSORT 2025 will later ask the report to define who is in each analysis and how missing data were handled (items 21b, 21c) and to report changes after the trial started, with reasons (item 10). | CV112, CV114 |
| For RWE studies supporting FDA decisions, finalize protocol and SAP before prespecified analyses; date-stamp revisions with their rationale (drugs, CV75); for devices, finalize before reviewing outcome data (CV94). | CV75, CV94 |

## 4. Design cautions specific to digital measures

| Caution | Rows |
|---|---|
| Use the same data collection method in all arms. | CV58 |
| Non-inferiority may be inappropriate when the comparator's effect was not established with similar DHT measurements; the margin then cannot be defined. Consult FDA before a non-inferiority trial with decentralized elements. | CV58, CV72 |
| Letting participants choose remote or site assessment can bias results; fix the modality in the protocol. | CV67 |
| A reviewer will later judge each result on five RoB 2 domains: randomization, deviations from intended interventions, missing outcome data, measurement of the outcome, selection of the reported result. Designing against them (concealed allocation, blinded assessors, retention, prespecification) is the person's choice; naming them is a planning aid, not a risk-of-bias assessment. | ES-71, ES-70 |

## Not sourced here (the named owner's)

Sample size formulas, power, alpha and multiplicity rules, estimator choice (for example mixed models or multiple imputation), non-inferiority margins, interim analysis boundaries and minimal important differences for named instruments. Each is `[GAP]` in this skill: the owner the person names for statistics, or owner not named supplies it, and the output records it as theirs.
