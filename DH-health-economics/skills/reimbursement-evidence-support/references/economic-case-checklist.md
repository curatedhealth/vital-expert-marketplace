# Economic case checklist (A2)

The items A2 checks a model, a budget impact analysis (BIA) and their reporting against. Each item carries the body it belongs to, the row it rests on, and the field in a model description that answers it. `scripts/model_check.py` applies the same items to a JSON description of the person's model. All rows read 19 October 2026; not owner-reviewed.

Statuses (see `gap-rules.md`): **shown**, **not shown**, **departure** (the model does something else than the rule; justified or not is for the body and the owner), **`[GAP]`** (the person's material does not say), **not applicable**.

An item is never "met by the product". It is shown, or not, in the material supplied.

## NICE routine use (body code NICE_ROUTINE)

| Item | What to look for | Row | Field |
|---|---|---|---|
| N1 Reference case | A reference-case analysis exists; non-reference analyses are separated and justified | `HE-035` | `reference_case` |
| N2 Evaluation type | Cost-utility or cost-comparison analysis | `HE-073`, `HE-039` | `evaluation_type` |
| N3 Cost perspective | NHS and PSS | `HE-037` | `cost_perspective` |
| N4 Productivity | Excluded from the reference case | `HE-038` | `productivity_in_base` |
| N5 Time horizon | Stated and justified as long enough for all important differences | `HE-040` | `horizon_years`, `horizon_justified` |
| N6 Health effects | QALYs, EQ-5D for adults, reported by patients (or carers) | `HE-043`, `HE-044` | `outcome_measure`, `utility_instrument`, `utility_reporter` |
| N7 Value set | Topic launched after 27 August 2026: UK 5L value set, 3L mapped with DSU/EEPRU, no 3L utilities in sensitivity analyses. Earlier topics: 5L mapped to 3L | `HE-058`, `HE-060`, `HE-061`, `HE-062`, `HE-063` | `value_set`, `topic_launched` |
| N8 Mapping | If mapped, declared as a departure, function described and fit shown | `HE-045` | `mapping` |
| N9 Discounting | 3.5% a year on costs and health effects (1.5% only under all three PMG36 criteria) | `HE-047`, `HE-048` | `discount_costs`, `discount_effects` |
| N10 Results | ICER and expected net health benefit reported | `HE-041` | `results_reported` |
| N11 Switching values | For rapidly iterating technologies, threshold analysis with a switching value | `HE-077` | `rapidly_iterating`, `switching_value_reported` |

## NICE early use (NICE_EARLY): all NICE_ROUTINE items, plus

| Item | What to look for | Row | Field |
|---|---|---|---|
| E1 Purpose | Addresses unmet need, likely value for money, and names the key drivers of decision uncertainty | `HE-068` | `early_use_objectives` |
| E2 Approach | Simplified approach declared (existing model, simplified model, or intermediate outcomes with threshold analysis) | `HE-069` | `simplified_approach` |
| E3 Deviations | Deviations from the reference case justified and discussed with NICE early | `HE-070` | `deviations_discussed` |
| E4 Evidence window | Each uncertainty named for evidence generation can be resolved within 3 years of publication | `HE-072` | `uncertainties_resolvable_3y` |

## NICE Evidence Standards Framework (ESF)

| Item | What to look for | Row | Field |
|---|---|---|---|
| S13 Expected impacts | Health, cost and resource impacts against standard or current care | `HE-086` | `expected_impacts_vs_current_care` |
| S17 BIA present | A budget impact analysis | `HE-087` | `bia.present` |
| S17b BIA content (tiers B and C) | Target population and uptake; technology and implementation costs (purchase, updating, maintenance, staffing, training, IT); comparator costs; relevant indirect costs | `HE-088` | `bia.population`, `bia.uptake`, `bia.technology_costs`, `bia.implementation_costs`, `bia.comparator_costs`, `bia.indirect_costs` |
| S17c UK costs | Costs relevant to the UK, NHS and PSS resources | `HE-089` | `bia.cost_country` |
| S18 Cost-effectiveness | Needed only for "higher financial risk" technologies; whether that applies is the commissioner's and the owner's judgment, not yours. If needed: cost-utility, or cost-consequences where QALYs are not possible | `HE-090`, `HE-091` | `higher_financial_risk`, `evaluation_type` |

Tier A, B or C is decided from the intended purpose (`HE-082` to `HE-084`); the early deployment subset omits S17 and S18 (`HE-092`).

## HAS (HAS)

| Item | What to look for | Row | Field |
|---|---|---|---|
| F1 Perspective | Collective; a healthcare-system perspective justified | `HE-103` | `cost_perspective` |
| F2 Evaluation type | Cost-utility when quality of life is an important consequence | `HE-104` | `evaluation_type` |
| F3 Discounting | Horizon over 12 months: 2.5% (falling after 30 years to a 1.5% floor) | `HE-105` | `discount_costs`, `discount_effects`, `horizon_years` |
| F4 Utilities | EQ-5D-5L with the French value set in force | `HE-106` | `utility_instrument`, `value_set` |
| F5 Results | Frontier, ICER or net benefit, and expenditure transfers between funders | `HE-107` | `results_reported` |

## IQWiG (IQWIG)

| Item | What to look for | Row | Field |
|---|---|---|---|
| G1 Perspective | SHI-insured community (wider perspectives separately) | `HE-110` | `cost_perspective` |
| G2 Discounting | 3% base; 0% and 5% sensitivity | `HE-111` | `discount_costs`, `discount_sensitivity` |
| G3 BIA | At least 3 years, with and without the product | `HE-112` | `bia.horizon_years` |

## ICER-PHTI (ICER_PHTI)

| Item | What to look for | Row | Field |
|---|---|---|---|
| P1 Budget impact first | BIA as the primary economic measure, 1-year horizon, 2-to-5-year scenarios where offsets come later | `HE-121`, `HE-122` | `bia.present`, `bia.horizon_years`, `bia.scenarios` |
| P2 Perspectives | DHT user and payer or plan sponsor | `HE-123` | `bia.perspectives` |
| P3 Clinical anchor | Comparative clinical effectiveness | `HE-115` | `comparative_effectiveness_source` |

## BIA good practice (any body; [PAPER] Sullivan et al. 2014, DOI 10.1016/j.jval.2013.08.2291, abstract only)

| Item | What to look for | Row | Field |
|---|---|---|---|
| B1 Elements | Eligible population, current and expected treatment mix, cost of each mix, condition-related cost changes | `HE-019` | `bia.population`, `bia.mix_before_after` |
| B2 Local data | The decision maker's own population | `HE-021` | `bia.cost_country` |
| B3 Scenarios | Alternative scenarios chosen from the decision maker's perspective | `HE-022` | `bia.scenarios` |
| B4 Validation | At least face validity with decision makers and verification of the calculations | `HE-023` | `bia.validated` |
| B5 Reporting | Enough detail for another modeler to replicate | `HE-024` | `bia.replicable` |

## CHEERS 2022 reporting (any economic evaluation; [PAPER] Husereau et al. 2022, DOI 10.1177/23814683211061097)

Report each item as reported or not reported. Never total them into a score: CHEERS has no validated scoring system (`HE-005`).

| Item | Row | Field (`cheers.`) |
|---|---|---|
| 4 Health economic analysis plan, and where available | `HE-006` | `item4` |
| 8 to 10 Perspective, horizon, discount rate, each with its reason | `HE-007` | `item8_10` |
| 15 Dates of resource quantities and unit costs, currency and conversion year | `HE-008` | `item15` |
| 16 Model described, why used, public availability | `HE-009` | `item16` |
| 17 Analytic, extrapolation and validation methods | `HE-010` | `item17` |
| 19 and 20 Distributional effects; uncertainty methods | `HE-011` | `item19_20` |
| 21 and 25 Patient, public and stakeholder engagement and its effect | `HE-012` | `item21_25` |
| 24 Effect of discount rate and time horizon | `HE-013` | `item24` |
| 27 and 28 Funding, funder's role, conflicts of interest | `HE-014` | `item27_28` |

## Inputs that rest on studies

The clinical effect, utilities and resource use inside a model rest on studies. For each study the person names: resolve it (`literature.get_record`), report design and CEBM level "from design only", check retraction and currency, and check each key result with Verify against a results passage (`tools.md`). A trial-based economic evaluation is labeled "rct" by the library from its title; the label says nothing about the economic analysis.

For a systematic search or a review of the clinical evidence, point to dh-clinical-validation `literature-and-real-world-evidence-review`. Where the body requires a systematic review of clinical evidence (NICE: protocol-driven review, `ES-127`, `ES-128`; EU JCA search rules, `ES-155`, `ES-156`), say whether the person's material shows one; do not run it here.
