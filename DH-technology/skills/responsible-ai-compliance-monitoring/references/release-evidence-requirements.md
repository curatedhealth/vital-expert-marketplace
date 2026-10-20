# Release evidence requirements: what a responsible-AI release may need to hold, row by row

Source: the research files copied unchanged in this folder (read 19 and 20 October 2026). Interpretive reference for A1, A2 and B1. Every line carries its row, its standing and the date it applies. In answers, cite each fact by source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite"). A requirement not in a row is `[GAP]`.

Row prefixes: DA (`data-and-ai-research.md`), AI US, AI EU, AI UK, AI IM (`ai-ml-regulation-research.md`, written with "AI" in front so they never collide with other files' rows), PE (`patient-engagement-equity-research.md`), UX-US (`ux-accessibility-usability-research.md`), EN (`engineering-interop-security-research.md`), CP-UK (`channels-partners-launch-research.md`), CV (`clinical-study-and-rwe-research.md`).

**Required type.** Each item says what kind of evidence it takes: a **test** (a result on named data and a named model version), a **document** (a written record), a **control** (something in place and working, such as an override or a log), or a **policy**. A policy statement never stands in for a test (old task "Governance evidence": "do not accept a policy statement in place of the test").

**Standing.** Law (binds those it applies to, from its date), final guidance, certification criterion, information standard, voluntary framework, reporting guideline, draft (never a requirement), proposed rule (never a requirement), not legally binding FAQ.

## 1. Core items for any clinical AI release (voluntary frameworks and reporting guidelines)

| Item | Type | What the source states | Standing and date | Rows |
|---|---|---|---|---|
| C1 Intended purpose, users, setting, laws and norms | document | MAP 1.1 | NIST AI RMF 1.0, January 2023, voluntary | DA-10 |
| C2 Knowledge limits and how output is used and overseen by humans | document | MAP 2.2 | Same | DA-11 |
| C3 Risks that will not or cannot be measured (including groups the data cannot show) | document | MEASURE 1.1 | Same | DA-12 |
| C4 Test sets, metrics and tools documented | document | MEASURE 2.1 | Same | DA-13 |
| C5 Subgroup performance on the release model, by group, with the model and dataset versions | test | Old task "Bias test" (the bias test, the intended use and the human who can override, old "Governance evidence") | Pack rule from the old skill; sources in C6 and section 2 | DA-38, DA-43 (FDA draft), CV127 |
| C6 Fairness approach and rationale; performance measures (discrimination, calibration, clinical utility); threshold rationale | document | TRIPOD+AI items 12e, 14, 15 | Reporting guideline, Collins et al., BMJ 2024, DOI 10.1136/bmj-2023-078378 | CV127 |
| C7 Differences between development and evaluation data | document | TRIPOD+AI item 16 | Same | CV128 |
| C8 The human who can override the model, named in the person's words | control | Old task "Governance evidence"; WHO principle 1, humans remain in control | WHO guidance, 28 June 2021 | DA-25 |
| C9 Monitoring after release: intended against actual performance, emergent risks | document | MEASURE 3.1; MANAGE 4 and 4.1 | NIST, voluntary | DA-14, DA-16 |
| C10 Non-AI alternatives weighed | document | MANAGE 2.1 | NIST, voluntary | DA-15 |
| C11 Generative AI: governance, content provenance, pre-deployment testing, incident disclosure | document or test | Four considerations | NIST AI 600-1, July 2024; standing after EO 14110 revocation not checked `[GAP]` | DA-17, DA-18 |
| C12 Early live evaluation, if run: user agreement, errors and malfunctions, modifications during the study, usability | document | DECIDE-AI | Reporting guideline, DOI 10.1136/bmj-2022-070904 | DA-80 to DA-84 |

The ISO/IEC 42001 management system is named only from its public page [WF] (DA-22); no clause is listed as an evidence item because no clause text was read.

## 2. United States

| Item | Type | What the source states | Standing and date | Rows |
|---|---|---|---|---|
| US1 Inventory of patient care decision support tools that use race, color, national origin, sex, age or disability as inputs | document | Reasonable efforts to identify such tools | Law for Section 1557 covered entities; 92.210(b), (c) within 300 days of 5 July 2024 | PE-113 to PE-115 |
| US2 Mitigation of the risk of discrimination for each such tool | control | Reasonable efforts to mitigate | Same | PE-113 |
| US3 Predictive DSI source attributes: intended use, population, users, decision role, cautioned uses, known risks; flag when an attribute is not available | document | 45 CFR 170.315(b)(11) | Certification criterion for developers of certified health IT, in the eCFR on 19 October 2026; HTI-5 (29 December 2025) proposes removal, proposed only | UX-US-56 to UX-US-60 |
| US4 User feedback on decision support captured and exportable | control | 45 CFR 170.315(b)(11) | Same criterion | UX-US-55 |
| US5 Non-device CDS: inputs explained, plain-language algorithm basis and validation, knowns and unknowns in the output | document | Criterion 4 | FDA CDS guidance, 29 January 2026, final | UX-US-65, UX-US-67 to UX-US-69 |
| US6 Usability testing showing Criterion 4 is met, where needed | test | "may need to perform usability testing" | Same | UX-US-71 |
| US7 AI-enabled device: subgroup performance, representative data, independent test data, data split, reference standard, model card, postmarket performance monitoring plan | test and document | Recommendations | FDA draft, 7 January 2025, **draft, not a requirement**; still draft on 19 October 2026 | DA-35 to DA-46, AI US-19 to AI US-22, AI US-37, AI US-38 |

Whether the organization is a covered entity, a certified health IT developer, or a device manufacturer is for the owner the person names for legal matters, or owner not named. Device status routes to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. For an AI device file, `dh-regulatory-and-quality` ai-ml-readiness-monitoring checks the submission; this skill checks the responsible-AI evidence.

## 3. European Union

AI Act high-risk duties (Chapter III Sections 1 to 3) apply from 2 August 2028 to systems that are MDR or IVDR devices needing notified-body assessment (Annex I) and from 2 December 2027 to Annex III systems, as set by Regulation (EU) 2026/1744 (AI EU-19, DA-67). MDCG 2025-6 maps MDR class IIa, IIb and III software as high-risk (AI EU-27) but is not legally binding (AI EU-25). Before those dates the items below are "not yet applicable", with the date; whether a system is high-risk is not decided here.

| Item | Type | What the source states | Applies from | Rows |
|---|---|---|---|---|
| EU1 AI literacy measures for staff | control | Measures to support AI literacy; no guaranteed level per person | Chapter I applied from 2 February 2025 (as amended) | AI EU-14, AI EU-20 |
| EU2 Risk management system over the lifecycle | document | Article 9 | High-risk dates | AI EU-06, AI EU-19 |
| EU3 Data governance: design choices, origin, preparation, assumptions, availability, bias examination and measures, data gaps | document | Article 10(2) | High-risk dates | DA-47, DA-48 |
| EU4 Data sets relevant, representative, as free of errors and complete as possible; reflect the setting of use | test and document | Article 10(3), 10(4) | High-risk dates | DA-49, DA-50 |
| EU5 Special-category data used for bias detection only under the Article 4a conditions, with records of why | document | Article 4a (Article 10(5) deleted) | Start date an open reading point (research file conflict 1) | DA-51 to DA-53 |
| EU6 Automatic event logs over the lifetime | control | Article 12 | High-risk dates | DA-54, DA-55 |
| EU7 Instructions for use: accuracy and metrics, group performance when appropriate, data specifications, pre-determined changes | document | Article 13(3) | High-risk dates | DA-56 to DA-58 |
| EU8 Human oversight: commensurate measures, automation bias awareness, override and stop | control | Article 14 | High-risk dates | DA-59 to DA-61 |
| EU9 Declared accuracy; feedback-loop risk reduced for systems that keep learning | document and control | Article 15(3), 15(4) | High-risk dates | DA-62, DA-63 |
| EU10 Post-market monitoring system and plan (Commission template guidance due by 2 September 2027) | document | Article 72 | High-risk dates; template date as amended | DA-65, DA-66, AI EU-34 |
| EU11 DPIA before processing likely to result in high risk, with Article 35(7) content | document | GDPR Article 35 | GDPR applies now | EN-111, EN-112 |
| EU12 Data protection by design and by default | control | GDPR Article 25 | GDPR applies now | EN-108, EN-109 |

For a medical device, the AI Act elements may sit in the MDR or IVDR technical documentation and post-market surveillance (AI EU-29, AI EU-34). Device-file readiness: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.

## 4. England

| Item | Type | What the source states | Standing | Rows |
|---|---|---|---|---|
| UK1 Developer clinical risk management system, clinical risk assessment, evidence of effective risk management, findings presented to the adopter | document | DCB0129 | Information standard (Health and Social Care Act 2012 s250), read through NHS guidance pages | CP-UK-05 to CP-UK-08 |
| UK2 Clinical Safety Case Report shared with the deploying organization; a Clinical Safety Officer appointed | document | Blog statement, not the standard | Confirm against the DCB0129 specification | CP-UK-11 |
| UK3 Deploying organization's own clinical risk assessment and check of developer compliance | document | DCB0160 | Information standard | CP-UK-09, CP-UK-10 |
| UK4 DTAC completed for procurement (clinical safety, data protection, technical assurance, interoperability, usability and accessibility); refreshed form since 6 April 2026 | document | DTAC | Best practice guidance, "not legally required" | CP-UK-01 to CP-UK-04 |
| UK5 GMLP principle 10: deployed models monitored and retraining risk managed | document | GMLP | Guiding principle (FDA, Health Canada, MHRA) | AI UK-09, AI UK-10 |

## 5. AI used in medicinal product development (pharma sponsors)

| Item | Type | What the source states | Standing | Rows |
|---|---|---|---|---|
| P1 Models and pre-processing frozen and documented in the SAP before unblinding; no incremental learning in pivotal trials | document | EMA reflection paper | Final reflection paper, adopted 9 September 2024 | DA-70, DA-71 |
| P2 Prospective testing for high-impact uses; hold-out test set used once | test | Same | Same | DA-72, DA-73 |

## 6. Evidence that is not enough on its own

- A policy statement in place of a test (old task "Governance evidence").
- A test on a different model version than the release (old task "Release score": keep the record id; mark the version).
- A group unseen at test time presented as tested (old task "Release score"): it stays "not seen at test time, still not tested".
- An overall figure without groups (FDA draft subgroup masking, DA-43, draft; old task "Bias test").
- A draft or proposal cited as the requirement (FDA AI-enabled device draft; HTI-5).

## 7. Post-release signals the library can add

- Safety events for the person's AI device and comparable devices: `regulatory-dh.search_safety_events` (`references/tools.md`). Events are described only by what the record states; relevance to the person's model is the person's judgment.
- FDA's request for comment on measuring real-world performance and drift (docket FDA-2025-N-4203) is not guidance (AI US-39).
