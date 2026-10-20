# Model build rules

Sourced rules for framing, building and reporting an economic model of a digital health technology, with their row ids in `health-economics-methods-research.md` (HE- rows). ISPOR rows are [PAPER] rows read at abstract level only: cite the row id and the DOI whenever an answer relies on one, and say "abstract only".

## 1. Specify the technology and the decision

| Rule | Row |
|---|---|
| CHEERS 2022 covers e-health and other processes of care, and medical devices; it replaces CHEERS 2013. [PAPER] DOI 10.1177/23814683211061097 | HE-001, HE-004 |
| For patient-facing digital interventions, the ISPOR Digital Health SIG framework PICOTS-ComTeC specifies 9 domains (population, intervention, comparator, outcome, timing, setting, communication, technology, context) and 32 optional subcategories. SIG report, not a task force report. [PAPER] Zrubka et al. 2024, DOI 10.1016/j.jval.2024.01.009 (from the Europe PMC index, read 19 October 2026; the research file row has no DOI), abstract only | HE-032 |
| State whether a health economic analysis plan was developed and where it is available (CHEERS item 4) | HE-006 (DOI 10.1177/23814683211061097) |
| State perspective, time horizon and discount rate, each with the reason (CHEERS items 8 to 10) | HE-007 (DOI 10.1177/23814683211061097) |
| Choose the reference case of the body that will decide: `reference-cases.md` | HE-035 and the rows there |

## 2. Choose the form of analysis

| Situation | Form the source names | Row |
|---|---|---|
| NICE appraisal or HealthTech routine use | Cost-utility (fully incremental) or cost-comparison | HE-039, HE-073 |
| Similar benefit at similar or lower cost than NICE-recommended comparators | Cost-comparison | HE-042, HE-056, HE-076 |
| NICE early-use HealthTech | Simplified model, reuse of existing models, or intermediate outcomes with threshold analysis | HE-069 |
| NICE ESF, any tier | Budget impact analysis (standard 17) | HE-087 |
| NICE ESF, higher financial risk | Cost-utility, or cost-consequences where QALYs are not possible (standard 18) | HE-090, HE-091 |
| ICER-PHTI review of a DHT | Budget impact first, 1-year horizon, payer and user perspectives | HE-121, HE-122, HE-123 |
| IQWiG evaluation | Evaluation plus mandatory BIA of at least 3 years | HE-112 |
| A budget impact analysis of any kind | Outside CHEERS; use BIA guidance (ISPOR BIA II) | HE-003, HE-018 (DOI 10.1177/23814683211061097 and 10.1016/j.jval.2013.08.2291) |

Model type (decision tree, state-transition, discrete event simulation) follows the ISPOR-SMDM series (HE-015, DOI 10.1016/j.jval.2012.06.012, abstract only). The series' detailed recommendations are not sourced `[GAP]`: describe the type the person chose and why (CHEERS item 16, HE-009, DOI 10.1177/23814683211061097); do not cite a rule for choosing one.

## 3. Build the budget impact analysis

| Rule | Row |
|---|---|
| Key elements: eligible population size, current treatment mix and expected mix after introduction, cost of each mix, changes in condition-related costs | HE-019 (DOI 10.1016/j.jval.2013.08.2291) |
| Use a simple cost calculator where possible; a cohort or patient-level model only when population, severity or treatment-pattern change cannot be captured credibly | HE-020 (DOI 10.1016/j.jval.2013.08.2291) |
| Inputs reflect the specific decision maker's population | HE-021 (DOI 10.1016/j.jval.2013.08.2291) |
| Sensitivity analysis means alternative scenarios chosen from the decision maker's perspective | HE-022 (DOI 10.1016/j.jval.2013.08.2291) |
| Minimum validation: face validity with decision makers and verification of the calculations | HE-023 (DOI 10.1016/j.jval.2013.08.2291) |
| Report inputs and calculations in enough detail for another modeler to replicate | HE-024 (DOI 10.1016/j.jval.2013.08.2291) |
| ESF standard 17 content (tiers B and C): target population and uptake; all direct technology and implementation costs (purchase, updating, maintenance, staffing, training, supporting IT); comparator direct costs; relevant indirect costs; UK costs relating to NHS and PSS | HE-088, HE-089 |
| AMCP draft: dynamic population, horizon typically 1 to 3 years, PMPM and total; modifiable electronic model with unlocked inputs | HE-138, HE-139 (draft) |

## 4. Collect the inputs

- Each input carries its source kind: the person's own figure (their data or assumption), a published study (with DOI, qualified through Verify), a real-world evidence study, or a value set. Never an input from memory.
- Clinical effect and utility inputs that need a literature review come from the dh-clinical-development skill `literature-and-real-world-evidence-review` (its method, its grading). This skill records the input and its source; it does not repeat the review.
- Report dates of resource quantities and unit costs, the currency, and the year of any conversion (CHEERS item 15, HE-008, DOI 10.1177/23814683211061097).
- Utilities: the value set the decision-maker requires (`reference-cases.md`: UK 5L under PMG51, French 5L at HAS, EQ-5D-5L preferred at ICER). Value sets anchor full health at 1 and dead at 0 (HE-126).
- Real-world evidence used to test a hypothesis: declared as hypothesis-evaluating in advance, protocol and analysis plan registered before analysis, conformance reported, tested in a different data source where feasible (HE-025 to HE-029). [PAPER] DOI 10.1002/pds.4297.
- Patient, public or stakeholder engagement in the design, and what difference it made (CHEERS items 21 and 25, HE-012, DOI 10.1177/23814683211061097).

## 5. Run and report

| Rule | Row |
|---|---|
| ICER = expected additional total cost / expected additional QALYs versus alternatives; show expected net health benefit as well | HE-041 |
| Where NICE modifiers apply, net health benefit at £25,000 and £35,000, with and without QALY weighting | HE-052 |
| Describe the model and why it was used, and whether and where it is publicly available (CHEERS item 16) | HE-009 (DOI 10.1177/23814683211061097) |
| Describe analytic and extrapolation methods and how the model was validated (CHEERS item 17) | HE-010 (DOI 10.1177/23814683211061097) |
| Describe distributional effects and the methods used to characterize uncertainty (CHEERS items 19 and 20) | HE-011 (DOI 10.1177/23814683211061097) |
| Report how uncertainty affects the findings, including discount rate and time horizon (CHEERS item 24) | HE-013 (DOI 10.1177/23814683211061097) |
| Funding, funder's role and conflicts of interest (CHEERS items 27 and 28) | HE-014 (DOI 10.1177/23814683211061097) |
| Non-technical description open to anyone; technical documentation openly or under IP-protecting agreements, at the modelers' discretion (ISPOR-SMDM 7, abstract only) | HE-016 (DOI 10.1016/j.jval.2012.04.012) |
| Switching value: the input value that would change the decision at a given threshold (PMG48) | HE-077 |
| Value of information: values reducing decision uncertainty through new evidence (abstract only; DOI 10.1016/j.jval.2020.01.001) | HE-031 |

## 6. Arithmetic used by the scripts

Stated so another modeler can replicate it (HE-024, DOI 10.1016/j.jval.2013.08.2291). The formulas are plain arithmetic; the research rows name the measures (HE-041, HE-052) but do not print formulas, so the formula lines below carry no row id.

- Discounted value in year index t (t = 0 for the first year): value / (1 + r) ** k, with k = t, or k = t + 1 if the person discounts the first year. The timing convention is the person's; IQWiG states discounting "after year 1" (HE-111). Other bodies' conventions are `[GAP]`.
- ICER: reported as a ratio only in the north-east (more cost, more QALYs) or south-west (less cost, fewer QALYs) quadrant, always with the quadrant named. A dominant or dominated result is reported as such, not as a negative ratio.
- Net health benefit at threshold L: dQALY minus dCost / L. Net monetary benefit: L x dQALY minus dCost. Both use the person's L.
- Budget impact per year: population x uptake x (new cost minus weighted current-mix cost plus condition-related cost change), undiscounted; displacement in proportion to current shares unless the person states otherwise. Whether a body requires a discounted BIA is `[GAP]`.
- Fully incremental analysis (HE-039): order by cost, drop strictly dominated options, drop extendedly dominated options, compute each ICER against the previous option on the frontier.

## 7. What never enters a model from this skill

A threshold the person did not choose, a utility, cost or effect from memory, a comparator price turned into the person's price, or a value set the decision-maker does not use.
