# Execution and reporting: interpretive reference

What a study execution record must be able to show, and how a result is reported against it. Every rule names its row; quotes are in the `*-sources.md` files (read 19 October 2026).

## 1. What must be fixed, and when

| Item | Rule | Row |
|---|---|---|
| Study type | Declared HETE or exploratory a priori. | HE-026 (DOI 10.1002/pds.4297) |
| Protocol and analysis plan (drugs and biologics, FDA) | Finalized and shared with FDA before the prespecified analyses; revisions date-stamped with a rationale for each; FDA must be confident data sources and analyses were not chosen to favor a conclusion. | CV75 |
| Protocol and analysis plan (devices, FDA CDRH, final 18 December 2025) | Finalized before reviewing outcome data and before the analyses; the submission states whether that was done; protocol developers should not have access to outcome results while writing it. | CV94, CV88 |
| Public posting (HETE) | Protocol and analysis plan posted on a public registration site before analysis. | HE-027 (DOI 10.1002/pds.4297) |
| Public posting (FDA, non-interventional drug studies) | Post protocols publicly, for example on ClinicalTrials.gov or ENCePP. | CV77 |
| EU registration (medicines, non-interventional studies) | Register in the HMA-EMA Catalogue of RWD studies with protocol and report; register data sources and update them if older than 12 months. | CV108 |
| Data linkage | Prespecified in the protocol, including how inconsistencies are resolved. | CV24 |
| Relevance and reliability assessment (devices) | The sponsor conducts it and, when submitted, FDA reviews it; limitations discussed. | CV90 |
| Feasibility assessment (EMA) | Recommended before the protocol; does not replace protocol and analysis plan. | CV106 |

**The test A2 applies.** The latest of protocol final, analysis plan final and (for HETE) public registration must be earlier than the first date anyone on the study team accessed outcome data. If the person cannot date first outcome access, that is the gap that matters most: write "first outcome access not dated `[GAP]`; prespecification cannot be shown".

## 2. Changes after the plan was fixed

- Every revision carries a date stamp and a reason (CV75).
- Results are published with a statement of conformance to, or deviation from, the analysis plan (HE-028).
- In systematic reviews, changes to protocol methods are declared and their impact explored with sensitivity analyses where possible (ES-40, ES-41). This is review method, applied here by analogy; say so if cited.
- Analyses of subgroups are reliable only if pre-specified before results were seen (ES-87).
- A change made after outcome access is not forbidden; it is a deviation, and the study reports it as one. It cannot be described as prespecified.

## 3. Data provenance and handling

- Traceability (audit trail) establishes provenance (CV82). In trials using computerized systems, audit trails are not disabled and timestamps are unambiguous, for example UTC (CV14).
- Data curation and transformation are documented, including changes to conform to standards and their impact (CV87). Study data from RWD in covered FDA drug submissions use the FDA Data Standards Catalog formats unless waived (CV86).
- Sponsors of drug marketing applications must be able to submit patient-level data for RWD analyzed, and should secure agreements with data owners (CV76).
- For DHT-collected data in trials, the first durable electronic repository holds the source data (CV60). Applied to an observational study, ask where app data first land and whether that store has an audit trail.

## 4. When the study is really a trial

If people are prospectively assigned to the product to study a health outcome, it is a clinical trial (CV133). Then: registration at or before first patient consent for ICMJE journals (CV132); for US applicable device clinical trials, registration within 21 days after first enrollment (CV141, CV142) and results within 1 year of primary completion (CV145); in the EU, results summary within one year of end of trial with a lay summary (CV152) for trials under the Clinical Trials Regulation. Trial execution belongs to dh-clinical-development `decentralized-trial-operations` (DH-01.02.3.1); point there.

## 5. Reporting the result

- STROBE (22 items; 18 common, 4 design-specific: items 6, 12, 14, 15) is the reporting guide for cohort, case-control and cross-sectional studies; it is not a quality appraisal tool (CV123, [PAPER] von Elm et al. 2007, DOI 10.1371/journal.pmed.0040296). STROBE item wording is not sourced `[GAP]`: name the item numbers only.
- If the result feeds an economic evaluation, CHEERS 2022 applies: 28 items (HE-002); state the analysis plan (HE-006), funding and the funder's role, and conflicts (HE-014). CHEERS is not a score (HE-005).
- AI tools are not authors; their use is disclosed (CV131). In EU JCA dossiers, every AI-assisted step is documented and no step is fully automated without a responsible human (ES-169, ES-170).
- Authors address methodological criticism publicly (HE-030, recommendation 6).

## 6. What a result can carry

- Non-randomized evidence starts at low GRADE certainty (ES-90); certainty is rated per outcome (ES-96); GRADE is judgment, not a score (ES-94). The rating is the person's or the HTA body's.
- Uncontrolled before-after designs are usually at serious or critical risk of bias (ES-78). A historical control period compared with a post-launch period carries the same concern for anything that changed over time; say so as a question for the rigor check (DH-01.07.3.2), not as a verdict.
- NICE uses no precise threshold (HE-049); the PMG36 and PMG48 ranges conflict for HealthTech (HE "Changes and conflicts" 1). A real-world cost result is never described as "cost-effective"; that conclusion is the HTA body's.
- Outcome tracking for a single customer is dh-go-to-market; outcome-linked payment is dh-access-and-value `outcomes-contract-monitoring`. Neither is outcomes research evidence.
