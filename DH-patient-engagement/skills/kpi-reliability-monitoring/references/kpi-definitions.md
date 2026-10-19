> Shared origin: built in the DH-02.03.3.1 skill build (engagement-kpi-dashboards/references/kpi-definitions.md), 19 October 2026, copied unchanged below this line.

# KPI definitions for patient engagement

Interpretive reference for A1 and B1 (and, copied, for the reliability skill). It says what a KPI card must hold, which published definitions exist for each KPI family, and where frameworks overlap. No KPI carries a target here: targets and thresholds come from the person.

## The KPI card

A card is complete when another analyst could recompute the number from the source without asking anyone.

| Field | What it holds | Why | Source |
|---|---|---|---|
| Decision | The decision the KPI serves, and who takes it | A KPI with no decision is not shown | Register method CF-12.02.03.3.1.1 (old skill: "Name the decision the KPI serves") |
| Numerator | The event or state counted, with its minimum count and window | The rule must be explicit to be recomputed | Register method |
| Denominator | The population divided by, named as a population (all eligible, all enrolled, enrolled long enough to be observed) | A count without a denominator is not a rate; reach uses a valid denominator, not volunteers who indicate interest | CS27, KX8 |
| Period | Start and end dates, or a rolling window and its anchor | The same formula over different periods gives different numbers | Register method |
| Grain | The unit and level (program, site, week) | Different grains count different units | Register method ("the grain (account, site, week)") |
| Source | The table or file the events come from | "Do not add a KPI with no source table" | Register method |
| Missing-data rule | How blanks, invalid dates and missed assessments are handled | FDA asks that missing data be avoided and its reasons collected (PE-21); an unstated rule hides the choice | PE-21 |
| Definition source | The framework the KPI follows (for example RE-AIM reach) | Adoption, reach and penetration carry different published definitions; pick one per metric and name it | CS research "Changes and conflicts" |
| Threshold and its owner | The person's threshold, if any, and who set it | People decide thresholds | Governance |
| KPI not shown | One KPI considered and left off, and why | Register method ("Name a KPI you will not show, and why") | Register method |

The card format that `scripts/engagement_kpis.py` reads is in the script header and in `examples/sample-data/kpis.json`.

## Published definitions by KPI family

Use these as the menu. The person picks; the card names the row.

| KPI family | Published definition | How it is computed | Rows |
|---|---|---|---|
| Reach | The absolute number, proportion and representativeness of individuals willing to participate | Participants divided by all eligible people (valid denominator, not volunteers who indicate interest); compare participants with non-participants or the target population | CS22, CS27, KX8 |
| Adoption (settings and staff) | RE-AIM: number, proportion and representativeness of settings and delivery staff willing to start. Proctor: intention, initial decision or action to try; also called uptake | Settings that participate divided by settings approached; staff who participate divided by staff invited | CS24, CS28, CS34 |
| Penetration | Integration of a practice within a setting | Eligible persons who use the service divided by all eligible; or providers delivering divided by providers trained or expected to deliver | CS39 |
| Implementation and fidelity | RE-AIM: at setting level, delivery as intended, consistency, time and cost; at individual level, patients' use of the intervention. Proctor fidelity: implemented as prescribed or intended | Percent of "perfect" delivery completed; adaptations; cost | CS25, CS29, CS37 |
| Maintenance and sustainability | RE-AIM: institutionalization at setting level; at individual level, effects 6 or more months after the last contact. Proctor: maintained within ongoing operations | Program still running 6 or more months after study funding or support ends | CS26, CS30, CS40 |
| Engagement (use) | Extent of usage (amount, frequency, duration, depth) and a subjective experience (attention, interest, affect) | Usage from automated records (logins, page views); experience from self-report | PE-105, KX6 |
| Effective engagement | Enough engagement with the intervention to achieve intended outcomes, rather than simply more | The person sets the dose (for example a number of modules within a window); the numerator counts people reaching it; the denominator keeps only people observed for the full window | PE-104, KX7 |
| Attrition | Dropout attrition (lost to follow-up) and nonusage attrition (stopped using) are different | Curves over time, relative risk of stopping, usage half-life (`attrition-curves.md`) | PE-101 to PE-103, KX1 to KX5 |
| Patient activation (PAM) | Four stages from believing the patient role matters to staying the course under stress; PAM-13 keeps the 22-item properties | Instrument score; level cut points are not public in the sources read `[GAP]`; PAM scoring is licensed (CS research "Not sourced") | PE-98 to PE-100, CS94, CS95 |
| Patient-reported outcomes | A PRO comes directly from the patient; one of four COA types | Instrument score; measurement properties judged with COSMIN (see the reliability skill) | PE-11, PE-12, PE-93 to PE-96 |
| Usage against a commissioned profile (England) | NICE ESF Standard 16: report ongoing usage against an expected usage profile agreed at commissioning, plus anonymized aggregate outcomes | The profile is agreed with the commissioner, not set here | CS61 |

## Where frameworks overlap

- Proctor's sustainability maps to RE-AIM maintenance; Proctor's penetration is similar to reach; adoption is defined in both with different units (CS research "Changes and conflicts"). One definition per KPI, named on the card.
- RE-AIM's "E" was "efficacy" in 1999 and is now "Effectiveness (or Efficacy)" including negative effects, quality of life and economic outcomes (CS21, CS23). Effectiveness is an outcome, not an engagement KPI: it belongs to the clinical evidence owner, and this skill does not compute it.
- Implementation outcomes are preconditions for clinical or service outcomes, so a failed deployment must be separated from an ineffective product (CS32). A low engagement KPI says nothing on its own about whether the product works.

## What a KPI cannot show

- Engagement, uptake or reach is not clinical evidence. A rise in effective engagement does not show a clinical benefit; that needs a study design the KPI does not have.
- A KPI computed on people who chose to take part says nothing about those who did not (KX5: dropout may introduce selection bias).
- A single value hides who it counts. Two cards can give nearly the same percentage over different people (see the reliability skill's worked example, where 23.4 percent and 23.5 percent come from different denominators).

## Outcome-linked KPIs

Where payment depends on an outcome (for example a CMS model that counts missing measures as non-attainment and keeps lost-to-follow-up patients in the denominator, CS87), the KPI is a contract term: point to Market Access (`outcomes-contract-monitoring`). This skill can compute the person's internal view of such a measure, labeled "internal view, not the payer's calculation".
