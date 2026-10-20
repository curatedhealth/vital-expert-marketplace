# Validity and reporting rules

Sourced rules for checking an economic model of a digital health technology: reporting completeness, validity, transparency, rule currency, and the evidence that monitoring compares the model against. Row ids refer to `health-economics-methods-research.md` (HE- rows, read 19 October 2026). ISPOR rows are [PAPER] rows read at abstract level only: cite the row id and the DOI and say "abstract only".

## 1. Reporting completeness: CHEERS 2022

[PAPER] Husereau et al. 2022, DOI 10.1177/23814683211061097 (also Value Health, DOI 10.1016/j.jval.2021.11.1351). CHEERS 2022 replaces CHEERS 2013, which should no longer be used (HE-001). 28 items in seven categories (HE-002). Covers e-health and devices (HE-004). Budget impact analyses are outside its scope (HE-003): check a BIA against section 3 below instead.

**Never a score.** "As there is no validated scoring system for the checklist, using it as a scoring tool could lead to misleading findings and is strongly discouraged" (HE-005, DOI 10.1177/23814683211061097). Report completeness item by item; no total, no percentage, no grade.

Items whose wording the research file holds:

| Item | What it asks | Row |
|---|---|---|
| 4 | Whether a health economic analysis plan was developed, and where available | HE-006 (DOI 10.1177/23814683211061097) |
| 8, 9, 10 | Perspective, time horizon, discount rate, each with the reason | HE-007 (DOI 10.1177/23814683211061097) |
| 15 | Dates of resource quantities and unit costs, currency, year of conversion | HE-008 (DOI 10.1177/23814683211061097) |
| 16 | Model described, why used, whether and where publicly available | HE-009 (DOI 10.1177/23814683211061097) |
| 17 | Analytic and extrapolation methods, approaches to validating the model | HE-010 (DOI 10.1177/23814683211061097) |
| 19, 20 | Distributional effects; methods to characterize uncertainty | HE-011 (DOI 10.1177/23814683211061097) |
| 21, 25 | Approach to engaging patients, public or stakeholders; what difference it made | HE-012 (DOI 10.1177/23814683211061097) |
| 24 | Effect of uncertainty, including discount rate and time horizon | HE-013 (DOI 10.1177/23814683211061097) |
| 27, 28 | Funding and the funder's role; conflicts of interest | HE-014 (DOI 10.1177/23814683211061097) |

Items 1 to 3, 5 to 7, 11 to 14, 18, 22, 23 and 26: wording not in the research file, and the Explanation and Elaboration report was not read. Mark them `[GAP]` and point to the checklist; never fill their wording from memory.

## 2. Validity: ISPOR-SMDM

| Rule | Row |
|---|---|
| The ISPOR-SMDM series has seven reports, including one on transparency and validation. Abstract only, DOI 10.1016/j.jval.2012.06.012 | HE-015 |
| Five validation types: face validity (experts evaluate structure, data sources, assumptions and results), verification or internal validity (coding accuracy), cross validity (comparison with other models of the same problem), external validity (model versus real-world results), predictive validity (model versus prospectively observed events). The last two are called the strongest. Abstract only, DOI 10.1016/j.jval.2012.04.012 | HE-017 |
| Non-technical description open to anyone; technical documentation openly or under IP-protecting agreements, at the modelers' discretion. Abstract only | HE-016 (DOI 10.1016/j.jval.2012.04.012) |

The series' detailed checklists (for example a model validation checklist) are not sourced (research file "Not sourced"): no item-level validation checklist may be cited.

## 3. Budget impact analyses: ISPOR BIA II

Abstract only, DOI 10.1016/j.jval.2013.08.2291.

| Rule | Row |
|---|---|
| Key elements: eligible population, current and expected treatment mix, cost of each mix, condition-related cost changes | HE-019 (DOI 10.1016/j.jval.2013.08.2291) |
| Simple cost calculator where possible | HE-020 (DOI 10.1016/j.jval.2013.08.2291) |
| Data reflect the specific decision maker's population | HE-021 (DOI 10.1016/j.jval.2013.08.2291) |
| Sensitivity analysis: alternative scenarios chosen from the decision maker's perspective | HE-022 (DOI 10.1016/j.jval.2013.08.2291) |
| Validation at minimum: face validity with decision makers and verification of the calculations | HE-023 (DOI 10.1016/j.jval.2013.08.2291) |
| Reporting detailed enough for another modeler to replicate | HE-024 (DOI 10.1016/j.jval.2013.08.2291) |
| NICE ESF standard 17 cost lines (tiers B and C) and UK NHS and PSS costs | HE-088, HE-089 |

## 4. Rule currency: texts that changed or conflict

Check every model against these before anything else. Each is a fact with its row, and the model's text is compared with it.

| What to look for in the model | Current position | Row |
|---|---|---|
| EQ-5D-3L tariff or 5L-to-3L mapping in a new NICE topic | UK 5L value set for adult reference-case utilities; 3L mapped to 5L with the DSU/EEPRU model; no 3L utilities in sensitivity or scenario analyses. Topics started before 27 August 2026 keep 5L-to-3L mapping | HE-058, HE-060, HE-061, HE-062, HE-063 |
| NICE threshold quoted as one number, or as a verdict | PMG36: £25,000 to £35,000; PMG48: £20,000 to £30,000; open conflict; no precise maximum | HE-049, HE-050, HE-051, HE-074 |
| "NICE health technology evaluations: the manual" | Retitled; HealthTech methods in PMG48 | HE-033, HE-034 |
| "Early value assessment" | Now early-use HealthTech guidance; old interim statement only for topics started before 14 July 2025 | HE-066, HE-067 |
| NICE budget impact test at £20 million | £40 million a year in any of the first 3 years since June 2025 | HE-055 |
| CHEERS 2013 cited | Replaced by CHEERS 2022 | HE-001 (DOI 10.1177/23814683211061097) |
| IQWiG efficiency frontier used to derive a price | Version 8.0 no longer extends the last segment for a price recommendation | HE-113 |
| AMCP Format 5.0 or the 6.0 draft cited as final | 6.0 released October 2026; only the March 2026 draft read | HE-131, HE-133 |
| ICER budget impact threshold applied to a DHT | The $821 million threshold applies to prescription drugs | HE-119 |
| 1.5% NICE discount in the reference case | Non-reference-case, only if all three criteria hold | HE-048 |
| Productivity costs in the NICE base case | Excluded from the reference case | HE-038 |

## 5. Monitoring: what the model is compared against

- External and predictive validity compare model results with real-world and prospectively observed results (HE-017, DOI 10.1016/j.jval.2012.04.012). The observed values are the person's data; the skill never estimates them.
- Real-world data used to test the model: declared hypothesis-evaluating or exploratory in advance (HE-026); protocol and analysis plan registered before analysis (HE-027); conformance or deviation reported (HE-028); a different data source from the one that generated the hypothesis where feasible (HE-029). [PAPER] DOI 10.1002/pds.4297, full text.
- NICE early-use guidance: uncertainties listed for evidence generation must be resolvable within 3 years of publication (HE-072); recommendations include use while evidence is generated (HE-071).
- Switching values (HE-077) are the monitoring trigger the person can set in advance: an observed value beyond a switching value changes the decision at that threshold.
- Uptake, persistence or outcome-contract attainment is not clinical evidence; a payment linked to outcomes is dh-market-access's outcomes-contract-monitoring.

## 6. What this skill never does with these rules

Score a model, certify it valid, declare it acceptable to a body, or rewrite the person's input without the person naming it as wrong.
