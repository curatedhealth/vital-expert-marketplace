# Metric definition, certification and publish rights

Interpretive reference for task A2. Each sourced rule carries its row; the research files in this folder hold the URL, verbatim quote and read date. Where this file states a step from the old framework tasks (DH-05.02.1.1, DH-05.02.1.2, DH-05.03.3), it says so.

## 1. The metric card

No official source governs internal analytics metrics or dashboards (`data-and-ai-research.md`, "Not sourced"). The closest primary structure is the CMS measure specification guidance for quality measures (CMS Measures Management System Hub, read 20 October 2026). It is applied here as a checklist for internal metrics and labeled so every time ("CMS quality-measure guidance, used as a checklist").

| Card element | What the source says | Source and rows |
|---|---|---|
| Purpose of a specification | "Specifications are instructions for how to build and calculate a measure" | CMS MMS Hub (DA-132) |
| Initial population | The cohort from which the denominator is selected | CMS MMS Hub (DA-133) |
| Denominator | The population evaluated, written in words, not codes; include age, setting, diagnosis, procedures, time interval | CMS MMS Hub (DA-134) |
| Numerator | The process, condition, event or outcome that satisfies the measure focus, with its time window if different | CMS MMS Hub (DA-135) |
| Stratification | Always consider social, economic and geographic strata; report unstratified and by each stratum | CMS MMS Hub (DA-136) |
| Scoring direction | Describe the scoring type and how to read it (higher or lower is better) | CMS MMS Hub (DA-137) |
| Evaluation areas | Importance, scientific acceptability, feasibility, usability and use | CMS MMS Hub (DA-138) |
| Reliability and validity | Descriptive statistics show data are available, not that they are reliable or valid | CMS MMS Hub (DA-139) |
| Maintenance (for CMS measures) | Annual update and comprehensive reevaluation every three years | CMS MMS Hub (DA-140); a CMS cycle, context only, never the person's review interval |

Old task method elements added to the card:
- Grain, formula and certified source tables; the metrics that must not be recomputed beside it (DH-05.02.1.1.1, "Do not leave the formula only in a dashboard").
- The entity and its key; the attributes allowed as filters; an attribute kept off the filters because it leaks or is unstable (DH-05.02.1.1.2, "Do not let every column become a filter").
- Version, and whether a change is a new version or a correction; who is told before a correction ships (DH-05.02.1.1.3, "Do not correct a formula silently").

`scripts/metric_check.py cards` prints flags K1 to K13 for missing elements. A flag is a fact against the checklist, not a verdict on the metric.

## 2. Data quality terms for the card's source

| Term | Meaning | Source and rows |
|---|---|---|
| Three categories, two contexts | Conformance, completeness, plausibility; verification and validation | Kahn 2016 (DA-94), DOI 10.13063/2327-9214.1244 |
| Conformance | Value, relational and computational conformance | Kahn 2016 (DA-95, DA-96) |
| Completeness | Presence of data attributes, not their values | Kahn 2016 (DA-97) |
| Plausibility | Uniqueness, atemporal and temporal | Kahn 2016 (DA-98) |
| Provenance and license | FAIR R1.1 usage license, R1.2 detailed provenance; FAIR is a guide, not a standard | Wilkinson 2016 (DA-100, DA-101), DOI 10.1038/sdata.2016.18 |

Running the checks on source data is `data-quality-monitoring` (this pack). This skill names on the card which checks the certified source must pass, as the person states them.

Where the source is an OMOP database: OMOP CDM is an open community data standard; OHDSI names v5.5 as current (DA-102, DA-103 [SPEC]); OBSERVATION_PERIOD defines when absence of a record means the event did not occur, which matters for denominators (DA-105 [SPEC]). Field-level rows come from the v5.4 page.

Where a metric uses USCDI elements: v7 was published 23 July 2026 (DA-108), v6 on 24 July 2025 (DA-109), v5 on 16 July 2024 (DA-110); 45 CFR 170.213 adopts v1 (adoption expired 1 January 2026) and v3 for certification (DA-111), with enforcement discretion for certain v3 elements (DA-112). "Published" and "required for certification" are kept apart.

## 3. Recomputing the dashboard number

Old task method (DH-05.02.1.2.2, "Do not add a local calculation that disagrees with the semantic layer"). `scripts/metric_check.py recompute` counts the denominator and numerator from the person's row-level file using the rules written on the card and sets the result beside the figure the dashboard shows. A difference is a fact: the dashboard formula, filters or refresh differ from the card until shown otherwise. Whether the difference matters is the person's rule; no source sets a tolerance.

## 4. Certification

Old task method (DH-05.03.3.1.1 and .2): the certification rule names the owner, formula, grain, source and the check (recomputation on a sample); a metric is "draft" until it passes; the certification record holds pass or refuse, date and certifier, and points at the semantic-layer definition. "Do not certify a metric with no owner." "Do not certify by adding the metric to a dashboard."

Rules:
- The certification rule and each decision are the certifier's, named by the person. The model writes the rule back, checks the card against it and drafts the record "for the certifier".
- A model-proposed rule is labeled "proposed" and is not applied until the person confirms it.
- Decertification when a formula changes (DH-05.03.3.1.3) and the periodic access review (DH-05.03.3.2.3) are run by `analytics-adoption-and-impact-monitoring` (this pack).

## 5. Templates

Old task method (DH-05.02.1.2.1 to .3): a template names its audience and decision, the certified metrics it may use and the fields the audience may filter; it shows an empty state when a filter returns nothing and names the owner who fixes a broken metric; a template no longer matching a decision is retired with the template that replaces it (or none) and who tells the audience. "Do not give a template raw tables when a certified metric exists." "Do not leave two templates for the same decision."

## 6. Publish rights and access

Old task method (DH-05.03.3.2.1 and .2): name the roles that may publish to the certified layer, the roles that may explore without publishing, and the data they may not export; record each publish (object, publisher, date, certified metrics only); refuse a publish that recomputes a certified metric locally.

Where the platform holds protected health information (US):

| Rule | Source and rows |
|---|---|
| Limit PHI to the minimum necessary for the purpose (not for disclosures to a provider for treatment) | HIPAA Privacy Rule, 45 CFR 164.502, eCFR read 19 October 2026 (CS103) |
| Identify which workforce classes need which PHI and limit access to match | 45 CFR 164.514 (CS104) |
| Routine, recurring disclosures (for example a scheduled data feed) need standard protocols limiting PHI | 45 CFR 164.514 (CS105) |
| Security Rule standards sit in 164.308, 164.310, 164.312, 164.314 and 164.316 | HIPAA Security Rule, eCFR read 20 October 2026 (EN-097) |
| Regular review of audit logs, access reports and incident tracking is required | HIPAA Security Rule, administrative safeguards, eCFR read 20 October 2026 (EN-101) |
| Unique user identification is required | HIPAA Security Rule, technical safeguards (EN-103) |
| The 2025 Security Rule NPRM is a proposal (6 January 2025), listed as a long-term action with final action shown as July 2027; the current rule remains in force | Federal Register, 6 January 2025 (EN-106); 2026 Unified Agenda (EN-107) |

Which roles get which rights is the person's. Security controls of the platform are `cybersecurity-and-privacy-by-design` (this pack). Whether an export is a permitted use or disclosure is for the owner the person names for privacy matters.

## 7. Analytics center of excellence

Old task method (DH-05.03.3.3.1 to .3): the charter names the decisions the CoE owns (certification, priority, standards), those it does not own (a product team's roadmap) and the seats; the decision log records each decision the charter allows with date, seats present, the standard or metric affected and who carries it out; a dispute names the charter line that applies and who resolves it if the charter does not. "Do not resolve a dispute by silence." The charter, seats and decisions are the person's; the model drafts headings labeled "proposed" only when asked.

## 8. What is not sourced

- Official governance for internal dashboards or KPIs outside quality measures: none `[GAP]`.
- Any tolerance for a recomputation difference, any data quality target, any certification threshold: none; the person's rule.
