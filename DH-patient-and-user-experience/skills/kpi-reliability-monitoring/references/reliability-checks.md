# KPI reliability checks

Interpretive reference for every task in this skill. It lists what makes a KPI trustworthy as a measurement: a complete card, a dashboard that uses the card's formula, data whose gaps are known, a number that recomputes, and, for questionnaire-based KPIs, published measurement properties. No check carries a pass mark for the KPI's value: thresholds come from the person.

## 1. Card quality checks

Run by `scripts/kpi_definition_check.py cards`. A **fail** means the card cannot be recomputed as written. A **check** needs the person's reading. Neither is a verdict on the number.

| Check | Fail or check when | Source |
|---|---|---|
| Decision named | No decision | Register method CF-12.02.03.3.1.1 |
| Numerator stated | No event or formula | Register method |
| Denominator stated | No population: a count, not a rate | Register method; CS27 |
| Denominator valid | Reach or penetration not divided by all eligible people; a denominator of people who downloaded, signed up or showed interest | CS27, CS39, KX8 |
| Period stated | No dates and no rolling window | Register method |
| Grain stated | No unit or level | Register method |
| Source table stated | No source ("Do not add a KPI with no source table") | Register method |
| Missing-data rule stated | No rule for blanks, invalid dates or missed assessments | PE-21 |
| Definition source named | No framework named, where adoption, reach and penetration differ by framework | CS research "Changes and conflicts" |
| Window matches denominator | A numerator window (for example 56 days from start) with a denominator that includes people observed for less | CS27 (valid denominator), PE-104 |
| Attrition type named | A retention or attrition KPI that does not say dropout or nonusage | PE-102 |
| Stopped rule stated | A retention or attrition KPI without the days without use that mean "stopped" | PE-101 to PE-103 |
| Instrument measurement properties | A questionnaire-based KPI with no named evidence of reliability, validity or measurement error | PE-93 to PE-96, KX9, KX10 |
| Threshold owner named | A threshold with no one named as having set it | People decide |

The keyword rules in the script (for example "retention", "reach", "downloaded") only raise checks; read the card before reporting one.

## 2. Formula drift

From the register's method (old CF-12.02.03.3.2.2): "Find a KPI whose dashboard formula is not the card"; "Do not treat a renamed KPI as the same formula."

| Finding | Rule |
|---|---|
| Match | Numerator, denominator, period, grain, source and missing-data rule identical |
| Drift | Any of those differs; report field by field, card against dashboard |
| Grain differs | The two numbers count different units and cannot be compared directly (register: "Name the grain if it differs") |
| Renamed, same formula | Report as renamed; confirm with the card owner before treating them as one |
| On the dashboard, no card | No card, no agreed definition; the KPI is not recomputable as agreed |
| On a card, not on the dashboard | Report; the person decides whether it should be shown |

Nearly equal values do not mean the same KPI. In the worked example the card gives 23.4 percent (11 of 47) and the dashboard 23.5 percent (16 of 68): different people, different denominators.

## 3. Missing and inconsistent data

Run by `scripts/kpi_definition_check.py missing`. Report every count; impute nothing.

- Blank ids, dates or event types; invalid dates; exact duplicates.
- Events after the as-of date; events before a person's start event; people with events but no start event.
- Events per month: a month with no events can be a feed outage rather than a change in behavior; the file alone cannot tell them apart.
- FDA asks that missing COA data be avoided and its reasons collected to inform sensitivity analyses (PE-21). Reasons come from the person.
- Where a payer model fixes the rule (for example CMS ACCESS counts a missing valid measure as non-attainment and keeps patients lost to follow-up in the denominator, CS87), that rule belongs to the contract: point to Market Access.

## 4. Recomputation

From the register's method (old CF-12.02.03.3.2.1): "Recompute the formula from the source table. Compare it with the number on the dashboard." "Do not trust the dashboard number without a recomputation."

| Step | Rule |
|---|---|
| Same rules | Recompute with the card's numerator, denominator, period and the dashboard's as-of date, using `scripts/engagement_kpis.py` |
| Compare three ways | Value, numerator and denominator separately; a matching value with different counts is a mismatch |
| Difference | Report the absolute difference in the KPI's units and in counts; the acceptable difference is the person's |
| Explain only with evidence | Name the field that differs (drift), the rows excluded (missing data) or the refresh time (stale); otherwise "unexplained" |
| Dashboard definition | If the dashboard's own definition is available, recompute it too: if it reproduces the dashboard number, the gap is drift, not a pipeline fault |

## 5. Questionnaire-based KPIs (COSMIN)

COSMIN rates each measurement property result sufficient (+), insufficient (-) or indeterminate (?), and grades the quality of the evidence with a GRADE approach (PE-94). Its published criteria for "sufficient" are:

| Property | COSMIN criterion for sufficient | Row |
|---|---|---|
| Content validity | The most important property: items relevant, comprehensive and comprehensible for the construct and population | PE-93 |
| Structural validity | CFI or TLI above 0.95, or RMSEA below 0.06, or SRMR below 0.08 | PE-96 |
| Internal consistency | Structural validity evidence and Cronbach's alpha at least 0.70 per unidimensional scale or subscale | PE-95 |
| Reliability | ICC or weighted kappa at least 0.70 | PE-95 |
| Measurement error | SDC or LoA smaller than the MIC | PE-96 |
| Criterion validity | Correlation with a gold standard at least 0.70, or AUC at least 0.70 | KX9 |
| Construct validity (hypotheses testing) | Result in accordance with a hypothesis defined in advance; no hypothesis defined gives an indeterminate rating | KX10 |

The COSMIN Risk of Bias checklist rates study quality on a four-point scale whose labels were changed: "excellent" became "very good", and "good" and "poor" became "adequate" and "inadequate"; the worst score counts (PE-97).

How to use it:

- These are COSMIN's criteria for rating published evidence, which the person may adopt for their KPI. The model lays out which criteria the named evidence meets; whether that is enough for the KPI's use is the person's decision.
- A KPI built on an instrument's change score (for example "PAM change of 4 points") also needs a meaningful change definition: FDA's draft PFDD Guidance 4 describes a meaningful score difference and asks for a well-justified anchor (PE-19, PE-20, draft). PAM level cut points and scoring are not in the sources `[GAP]` and PAM is licensed (CS research "Not sourced").
- The instrument's published evidence is not evidence about the person's own data. Reliability in the person's population needs their own analysis.

## 6. What a reliability check cannot show

- A complete, recomputable KPI can still be the wrong KPI for the decision; that is the person's judgment (A1 of the sibling skill).
- A reliable engagement KPI is still not clinical evidence.
- A drift finding says the two formulas differ; it does not say which one is right. The card owner decides.
