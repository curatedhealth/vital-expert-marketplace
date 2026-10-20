# Indicators: activity results, attrition, support and partnership compliance

Interpretive reference for task A2 and B1. Computed by `scripts/engagement_monitor.py` from the person's own logs. Rows: PE-, CP-. No indicator has a sourced target; every pass rule is the person's.

## 1. Activity results (old task "Activity score", CF-12.02.03.2.2.2)

| Indicator | Definition | Rule kept or row |
|---|---|---|
| Result count per activity | Count of the action in the result definition, from the named record, in the period | Old method step 1 |
| Share of reached | Result count divided by the number the person says the activity reached | Computation only; the denominator is stated |
| Unscored activity | An activity with no record | Old rule: never scored as zero without saying the record was missing |
| Off-list claim | A claim used in the period that is not on the activity's allowed list, or any claim where no list exists | Old method step 3; goes to the review owner |
| Met or missed | Result against the person's own target | No target, no verdict |

## 2. Attrition (Eysenbach [PAPER], PE-101 to PE-103)

| Indicator | Definition |
|---|---|
| Attrition curve | Share of participants still active at each interval, among those observable for that long (started at least that many days before the as-of date) |
| Usage half-life | First interval at which half or fewer of the observable participants are still active |
| Dropout attrition | Share with follow-up not done (lost to follow-up), reported separately from nonusage (PE-102) |

"Active" follows the person's own definition of activity (for example "opened a session"). The script reads it from the last-active date the person supplies; say so.

## 3. Support to patients (elements for the compliance owner)

| Indicator | Definition | Row |
|---|---|---|
| Retail value per patient per calendar year | Sum of the retail values the person records | CP-US-27 (cap basis) |
| Patients above the cap figure | Patients whose yearly value exceeds the figure passed in; for 2026 OIG states $623 | CP-US-27 |
| Cash or cash equivalent items | Items the person marks as cash or cash equivalent | CP-US-26 |
| Items without a recorded recommendation | Items with no recorded recommendation by the patient's licensed professional | CP-US-26 |

These are elements of one safe harbor. A patient under the figure is not "protected"; a patient over it is not a finding of a violation. Both go to the compliance owner.

## 4. Partnership compliance [INDUSTRY]

| Indicator | Definition | Row |
|---|---|---|
| Support before a signed agreement, or none | First support date earlier than the agreement date, or no agreement | PE-71, PE-80 |
| Purpose not stated | Agreement without a stated purpose | PE-71 |
| Not disclosed | Support or contracted service not on the company's disclosure list | PE-75, PE-76, PE-82 |
| Disclosure period | ABPI: annual, full calendar year | PE-82 |

Apply a code's indicator only if the company is bound by that code; label each [INDUSTRY].

## 5. Published comparators

`literature.search_literature` can find published program or attrition studies. Use one only after reading the paper; a published rate is context, never a target, and attrition differs by condition and design.
