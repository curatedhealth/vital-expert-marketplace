# CHEERS 2022 completeness check (sourced items only, no score)

| Item | Topic | Row | Status | Where (line: text) |
|---|---|---|---|---|
| 4 | Health economic analysis plan | HE-006 (DOI 10.1177/23814683211061097) | not found: person checks |  |
| 8 | Perspective | HE-007 (DOI 10.1177/23814683211061097) | text found: person confirms | 11: The perspective is the NHS. |
| 9 | Time horizon | HE-007 (DOI 10.1177/23814683211061097) | text found: person confirms | 11: The time horizon is three years because the trial followed patients for one year. |
| 10 | Discount rate | HE-007 (DOI 10.1177/23814683211061097) | text found: person confirms | 11: Costs and QALYs are discounted at 3.5% a year.<br>23: One-way sensitivity analysis varied every input by plus or minus 20 percent; a scenario with a 1.5% discount rate is also shown. |
| 15 | Currency, price date and conversion | HE-008 (DOI 10.1177/23814683211061097) | text found: person confirms | 15: Costs are in GBP.<br>23: At 20,000 GBP per QALY the model shows that SleepWell is cost-effective, which proves its value to the NHS. |
| 16 | Rationale and description of model | HE-009 (DOI 10.1177/23814683211061097) | text found: person confirms | 11: A three-state Markov model (insomnia, remission, relapse) with yearly cycles.<br>27: The model is available on request under a confidentiality agreement. |
| 17 | Analytics and assumptions | HE-010 (DOI 10.1177/23814683211061097) | text found: person confirms | 17: ## Validation<br>19: The model was validated by two sleep physicians who reviewed the structure and the inputs. |
| 19 | Characterizing distributional effects | HE-011 (DOI 10.1177/23814683211061097) | not found: person checks |  |
| 20 | Characterizing uncertainty | HE-011 (DOI 10.1177/23814683211061097) | text found: person confirms | 23: One-way sensitivity analysis varied every input by plus or minus 20 percent; a scenario with a 1.5% discount rate is also shown. |
| 21 | Approach to engagement | HE-012 (DOI 10.1177/23814683211061097) | not found: person checks |  |
| 24 | Effect of uncertainty | HE-013 (DOI 10.1177/23814683211061097) | text found: person confirms | 23: One-way sensitivity analysis varied every input by plus or minus 20 percent; a scenario with a 1.5% discount rate is also shown. |
| 25 | Effect of engagement | HE-012 (DOI 10.1177/23814683211061097) | not found: person checks |  |
| 27 | Source of funding | HE-014 (DOI 10.1177/23814683211061097) | text found: person confirms | 27: The study was funded by SleepWell Health Ltd. |
| 28 | Conflicts of interest | HE-014 (DOI 10.1177/23814683211061097) | not found: person checks |  |

Items 1, 2, 3, 5, 6, 7, 11, 12, 13, 14, 18, 22, 23, 26: [GAP] item wording not in the research file; check them against the CHEERS 2022 checklist (DOI 10.1177/23814683211061097).

# Reference-case check: NICE

| Element | Rule as written | Row | Status | Where (line: text) |
|---|---|---|---|---|
| Discount rate | 3.5% a year for costs and effects | HE-047 | stated: person confirms it matches | 11: Costs and QALYs are discounted at 3.5% a year. |
| Perspective on costs | NHS and PSS | HE-037 | not found: person checks |  |
| Outcome measure | QALYs; EQ-5D preferred in adults | HE-043 | stated: person confirms it matches | 11: Costs and QALYs are discounted at 3.5% a year.<br>15: The utility gain of 0.02 comes from the trial's EQ-5D-3L data, valued with the Dolan 1997 UK 3L tariff.<br>23: At 20,000 GBP per QALY the model shows that SleepWell is cost-effective, which proves its value to the NHS. |
| UK 5L value set (new topics) | UK 5L value set for all adult reference-case utilities (PMG51) | HE-058 | not found: person checks |  |
| 3L value set used | New topics: map 3L to the UK 5L set; no 3L utilities in sensitivity or scenario analyses | HE-060, HE-061 | check against the row | 15: The utility gain of 0.02 comes from the trial's EQ-5D-3L data, valued with the Dolan 1997 UK 3L tariff. |
| 1.5% discount rate | Non-reference-case 1.5% only if all three criteria are met | HE-048 | check against the row | 23: One-way sensitivity analysis varied every input by plus or minus 20 percent; a scenario with a 1.5% discount rate is also shown. |
| Time horizon | Long enough to reflect all important differences in costs or outcomes | HE-040 | check against the row | 11: The time horizon is three years because the trial followed patients for one year. |
| Default ranges | Plus or minus 20 percent defaults are not the modeler's ranges; justify each range and run one-way analysis on net benefit | tools.md (tornado pitfall) | check against the row | 23: One-way sensitivity analysis varied every input by plus or minus 20 percent; a scenario with a 1.5% discount rate is also shown. |
| Productivity costs | Excluded from the reference case; may be shown separately | HE-038 | check against the row | 15: Productivity gains from fewer sick days are included in the base case. |
| Threshold stated | PMG48 states GBP 20,000 and 20,000 to 30,000 (HE-074); PMG36 states 25,000 to 35,000 (HE-050, HE-051): open conflict; NICE uses no precise maximum (HE-049) | HE-049, HE-050, HE-051, HE-074 | check against the row | 23: At 20,000 GBP per QALY the model shows that SleepWell is cost-effective, which proves its value to the NHS. |
| Verdict wording | No precise maximum; acceptability is the committee's judgment | HE-049 | check against the row | 23: At 20,000 GBP per QALY the model shows that SleepWell is cost-effective, which proves its value to the NHS. |
| Old manual title | PMG36 is now 'NICE technology appraisal and highly specialised technologies guidance: the manual' | HE-033 | no text found |  |
| Early value assessment name | EVA is now early-use HealthTech guidance (PMG48 section 3) | HE-067 | no text found |  |

A line found is a candidate for the person to confirm; 'not found' means check the document. No score or total is given (HE-005, DOI 10.1177/23814683211061097).
