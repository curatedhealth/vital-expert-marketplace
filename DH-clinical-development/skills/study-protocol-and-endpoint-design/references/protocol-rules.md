# Protocol rules for a digital health trial

Interpretive reference for A2 (and for the sibling monitoring skill's completeness check). The spine is SPIRIT 2025: 34 minimum items plus a schedule diagram, superseding SPIRIT 2013 (CV115) [PAPER] DOI 10.1136/bmj-2024-081477. Every item is addressed before ethics submission, and an item that does not apply is stated as not relevant, explicitly (CV117). Item wording is in `spirit-2025-checklist.md` (SP- rows). The table below adds what the digital, decentralized, AI and registration rows require on top of each item.

## Status of the GCP frame

| Fact | Rows |
|---|---|
| ICH E6(R3) principles and Annex 1: ICH Step 4 on 6 January 2025; EU effective 23 July 2025; FDA final guidance dated September 2025. | CV1, CV2, CV3 |
| Annex 2 (decentralized elements, pragmatic elements, real-world data): ICH Step 4 on 3 June 2026, CHMP adoption 25 June 2026, EU effective 15 January 2027. Whether FDA has published Annex 2 is not sourced `[GAP]`. | CV2, CV18, research file "Not sourced" |
| E6(R3) defines investigational products as drugs, medicines, medicinal products, vaccines and biologics; devices are not named. The device GCP standard (ISO 14155) is not read in this skill `[GAP]`. | CV4, research file "Not sourced" |
| E8(R1) (adopted 6 October 2021): quality by design, critical-to-quality factors identified prospectively and considered together. | CV27, CV28, CV29 |
| E6(R3) principles 6 and 7: quality built into design, fitness for purpose, processes proportionate to risk and to the importance of the data. | CV5, CV6, CV7 |

## Item-by-item additions

| SPIRIT item | Addition for digital health | Rows |
|---|---|---|
| 1b Structured summary | Include WHO Trial Registration Data Set items; the data set is version 1.3.1 with 24 items. | SP-1b, CV138 |
| 4 Registration | ICMJE: register at or before first patient consent; the date first submitted to the registry counts. Acceptable: a WHO ICTRP primary register with the 24-item data set, or ClinicalTrials.gov. US law for an applicable clinical trial: no later than 21 calendar days after the first participant is enrolled. ICMJE is the stricter rule. | SP-4, CV132, CV134, CV141, CV142, research file "Changes and conflicts" |
| 6 Data sharing | Trials enrolling from 1 January 2019 include a data sharing plan in the registration; the statement says whether IPD will be shared ("undecided" is not acceptable). | SP-6, CV135, CV136 |
| 8 Dissemination | US applicable clinical trials: results no later than 1 year after the primary completion date, with certified delays and good-cause extensions. EU CTR trials: results summary and lay summary within one year of the end of the trial in all Member States. WHO joint statement: 12 months for summary results, 24 months for publication, a funder pledge, not law. | SP-8, CV145, CV146, CV147, CV152, CV140 |
| 9b, 12 Comparator and design | Non-inferiority may be inappropriate when the comparator effect was not established with similar DHT measurements; consult FDA before a non-inferiority trial with decentralized elements. | SP-9b, SP-12, CV58, CV72 |
| 11 Patient and public involvement | New in 2025. Involve patients early (trust, recruitment, adherence, meaningful endpoints); involve intended users in designing computerized systems where relevant. | SP-11, CV116, CV30, CV10, CV25 |
| 13, 18 Setting and timeline with decentralized elements | Requirements are the same with or without decentralized elements. The protocol fixes which visits are at a site, which are remote, and which are the participant's choice, because free choice can bias results. Records capture visit type, location, date and data originator. Local health care providers do only tasks of routine practice. | SP-13, SP-18, CV66, CV67, CV69, CV70 |
| 13 EU applications | Summarize planned decentralized elements in the clinical trial application cover letter (EU recommendation paper Version 02, effective 29 October 2025, not legally binding); a decentralized element identified as critical to quality needs a risk-proportionate approach. | CV95, CV96, CV97 |
| 14a Eligibility with own devices | If participants may use their own DHT, sponsor-provided DHTs are offered so no one is excluded. | SP-14a, CV53 |
| 15a Intervention | For an AI intervention, state the algorithm version, input data handling and human-AI interaction (SPIRIT-AI, on the 2013 numbering). | SP-15a, CV119, CV120, CV122 |
| 16 Outcomes | Variable, metric, aggregation, time point; for DHT endpoints also tool, timing and combination of repeated assessments. See `endpoint-rules.md`. | SP-16, CV55 |
| 17 Harms | A safety monitoring plan states how abnormal DHT measurements are reviewed and managed; continuous monitoring by investigators is generally not expected. DHT safety data reach investigators in a manageable form. | SP-17, CV62, CV26 |
| 19 Sample size | All assumptions are stated. The numbers are for the owner the person names for statistics, or owner not named (B1). For a prediction model, justify size separately for development and evaluation. | SP-19, CV126 |
| 21 to 24 Allocation and blinding | Wording in SP-21a to SP-24c. Who is blinded matters for the outcome measurement bias domain a reviewer will later assess. | SP-21a to SP-24c, ES-71 |
| 25a Data collection | A DHT that acquires participant data is a data acquisition tool; give its V&V and specifications; minimize erroneous participant entry on primary, key secondary and safety endpoints. | SP-25a, CV20, CV46, CV52, CV103 |
| 25b Retention | List outcome data collected after discontinuation; plan to reduce missing data. | SP-25b, CV59, PE-21 |
| 26 Data management | Data management plan with data origin, flow, remote acquisition methods and data service providers (CV68); data flow overview, diagram recommended (EU, CV102); source data for DHT data is the first durable electronic repository (CV60); audit trails on and interpretable, timestamps unambiguous, for example UTC (CV14); computerized systems fit for purpose and validated before use, changes validated by risk (CV9, CV11, CV12, CV13); contingency plan for digital tool malfunction on critical-to-quality elements (CV99); data linkage prespecified with how inconsistencies are resolved (CV24). | SP-26 and the rows inline |
| 27a to 27d Statistics | The protocol defines a primary estimand; protocol and SAP prespecify the main estimator and a sensitivity analysis (B1). | SP-27a to SP-27d, CV40 |
| 29 Monitoring | New in 2025, replacing auditing. Monitoring considers decentralized settings; FDA recommends risk-based and centralized monitoring for missing, inconsistent and outlying data. | SP-29, CV116, CV17, CV71 |
| 32a Consent | Remote consent is possible; the investigator confirms identity. EU paper: real-time audio and video, identity checks both ways, on-site offered unless justified; the e-signed copy is downloadable and protected against modification. | SP-32a, CV16, CV100, CV101 |
| 32b, 33 Data use and confidentiality | Consent says who may access DHT data during and after the trial, and that terms of service may allow sharing outside it. | SP-32b, SP-33, CV61 |

## Trials with pragmatic elements or real-world data

| Rule | Rows |
|---|---|
| RWD used in a trial must be fit for purpose: reliability (accuracy, completeness, provenance, traceability) and relevance (key data elements available). Data may be primary (collected for the trial) or secondary use. | CV22, CV23 |
| For devices, FDA's RWE guidance of 18 December 2025 supersedes the 2017 one; relevance is availability, timeliness and generalizability; reliability is accrual, quality and integrity. Finalize the protocol and analysis plan before reviewing outcome data, and say so in the submission. | CV88, CV91, CV92, CV94 |
| Whether RWD collection on a marketed device needs an IDE depends on the facts; use in the normal course of practice likely does not. The owner the person names for regulatory status decides, or owner not named. | CV93 |
| The three frameworks word reliability differently; name the one applied. | research file "Changes and conflicts" |
| EMA's reflection paper (adopted 17 March 2025) covers non-interventional studies only; a feasibility assessment before the protocol is recommended; target trial emulation should be considered for causal questions. | CV104 to CV107 |

## US diversity action plans

Device sponsors must submit a diversity action plan in the IDE application, or in the 510(k), De Novo or PMA where no IDE is needed (PE-34); it states enrollment goals, their rationale and how they will be met (PE-31). The requirement applies to studies whose enrollment starts more than 180 days after FDA publishes the final guidance (PE-36); on 19 October 2026 the guidance page still lists the June 2024 document as a draft, "Not for implementation" (PE-41). Lay out these facts; whether a plan is needed for this study is the call of the owner the person names for regulatory status, or owner not named.

## Not sourced here

EU MDR clinical investigation requirements, ISO 14155, national ethics committee rules, IDE content, and the EU CTR date of application (research file "Not sourced"). Each is `[GAP]` with the owner the person names for regulatory status, or owner not named as the next step.
