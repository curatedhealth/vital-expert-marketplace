# Responsible AI rules: what the sources say, row by row

Source: the research files copied unchanged in this folder (read 19 and 20 October 2026). Interpretive reference for A1, A2 and B1. Every line carries its row. In answers, cite each fact by source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite"). A fact not in a row is `[GAP]`.

Row prefixes: DA (`data-and-ai-research.md`), AI US, AI EU, AI UK, AI IM (`ai-ml-regulation-research.md`; written with "AI" in front so they never collide with other files' US or UK rows), PE (`patient-engagement-equity-research.md`), UX-US (`ux-accessibility-usability-research.md`), EN (`engineering-interop-security-research.md`), CP-UK (`channels-partners-launch-research.md`), CV (`clinical-study-and-rwe-research.md`).

## 1. Standing of each source (say it every time a source is applied)

| Source | Standing on 20 October 2026 | Rows |
|---|---|---|
| NIST AI RMF 1.0 (NIST AI 100-1, January 2023) | Voluntary, non-sector-specific; review expected no later than 2028 | DA-01 to DA-03 |
| NIST AI 600-1 Generative AI Profile (July 2024) | Companion resource to the RMF, written under EO 14110; its standing after the revocation of EO 14110 was not checked `[GAP]` | DA-17, research file "Not sourced" |
| ISO/IEC 42001:2023 and ISO/IEC 23894:2023 | Public abstract pages only [WF]; 42001 specifies requirements for an AI management system, 23894 is guidance. No clause text is given or quoted | DA-22, DA-23 |
| WHO Ethics and governance of AI for health (28 June 2021) | WHO guidance; six principles read from the publication page and news release only | DA-24 to DA-29 |
| WHO guidance on large multi-modal models (18 January 2024; page dated 25 March 2025) | WHO guidance; recommendations to governments, companies and providers; whether the 2025 page changed content was not checked | DA-30 to DA-34 |
| FDA draft "Artificial Intelligence-Enabled Device Software Functions" (7 January 2025) | **Draft, not for implementation.** Still draft on 19 October 2026; on CDRH's FY 2027 A-list as a final guidance it intends to publish | DA-35, AI US-19 to AI US-22 |
| FDA Clinical Decision Support Software guidance (29 January 2026) | Final guidance; supersedes the 6 January 2026 issue | UX-US-64 |
| FDA, Health Canada and MHRA transparency principles (June 2024) and GMLP principles (27 October 2021; IMDRF final January 2025) | Guiding principles | AI US-29, AI US-32, AI US-33, AI UK-09, AI UK-10, AI IM-01 |
| EU AI Act, Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 (8 July 2026, in force 27 July 2026) | Law. High-risk duties in Chapter III Sections 1 to 3 (Articles 9 to 15) apply from 2 December 2027 (Annex III systems) and 2 August 2028 (Annex I systems, which include MDR and IVDR devices) | AI EU-17 to AI EU-19, DA-67 |
| MDCG 2025-6 / AIB 2025-1 FAQ (June 2025) | Not legally binding; its 2 August 2027 date is superseded by 2 August 2028 | AI EU-25, AI EU-32 |
| EMA reflection paper on AI in the medicinal product lifecycle (adopted 9 September 2024) | Final reflection paper; for AI used in medicinal product development | DA-68 |
| 45 CFR 92.210 (Section 1557 rule) | Law for covered entities; paragraphs (b) and (c) apply within 300 days of 5 July 2024 | PE-113 to PE-115 |
| 45 CFR 170.315(b)(11) decision support interventions (ONC HTI-1) | Certification criterion for certified health IT; in the eCFR on 19 October 2026 | UX-US-54 to UX-US-59 |
| ONC HTI-5 proposed rule (29 December 2025, 90 FR 60970) | **Proposed only.** Would remove source-attribute and intervention risk management requirements; not final | UX-US-60, UX-US-61 |
| GDPR, Regulation (EU) 2016/679 | Law | EN-108 to EN-113 |
| DCB0129 and DCB0160 (England) | Information standards under section 250 of the Health and Social Care Act 2012; read through NHS guidance pages, not the specification text | CP-UK-05 to CP-UK-11 |
| TRIPOD+AI (Collins et al., BMJ 2024) | Reporting guideline [PAPER], DOI 10.1136/bmj-2023-078378 | CV124 to CV128 |

The FDA AI-enabled device draft and the HTI-5 proposal are never presented as requirements. Write "the FDA draft of 7 January 2025 recommends" and "HTI-5 proposes".

## 2. A1: the system, the decision, the harm and the groups

| What the map holds | As the source states it | Rows |
|---|---|---|
| Intended purpose, beneficial uses, laws and norms, deployment setting documented | NIST MAP 1.1 | DA-10 |
| Knowledge limits and how output is used and overseen by humans documented | NIST MAP 2.2 | DA-11 |
| Risks that will not or cannot be measured are documented | NIST MEASURE 1.1 (basis for marking an unseen group `[GAP]` in the record, not dropping it) | DA-12 |
| Three bias categories: systemic, computational and statistical, human-cognitive; each can occur without discriminatory intent | NIST AI RMF | DA-08 |
| Seven trustworthiness characteristics, including "fair with harmful bias managed" | NIST AI RMF | DA-05 |
| Label bias: an outcome differentially ascertained across groups; feature bias for predictors | Rajkomar 2018, DOI 10.7326/M18-1990 (DA-115); Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9 (DA-120) | DA-115, DA-120 |
| Fairness concerns apply to polar decisions such as allocating scarce resources | Paulus and Kent 2020 | DA-116 |
| Target population, intended purpose in the care pathway and intended users; known health inequalities between sociodemographic groups | TRIPOD+AI items 3b, 3c | CV125 |
| Predictive decision support: intended use, population, users, decision-making role (informs, augments, replaces) | 45 CFR 170.315(b)(11) | UX-US-57 |
| Tasks, situations or populations where users are cautioned against use; known risks and limits | 45 CFR 170.315(b)(11) | UX-US-58 |
| Covered entity: reasonable efforts to identify patient care decision support tools that use race, color, national origin, sex, age or disability as inputs, and to mitigate the risk of discrimination | 45 CFR 92.210 | PE-113 |
| Patient care decision support tool: any automated or non-automated tool used to support clinical decision-making | 45 CFR part 92 definition | PE-114 |
| Inclusiveness: design for the widest equitable use regardless of age, sex, gender, income, race, ethnicity and other characteristics | WHO principle 5 | DA-28 |
| Humans stay in control of health-care systems and medical decisions | WHO principle 1 | DA-25 |
| Generative AI: twelve named risks, including confabulation, harmful bias or homogenization, human-AI configuration, data privacy, value chain and component integration | NIST AI 600-1 | DA-19 to DA-21 |
| Automation bias by professionals and patients | WHO LMM guidance; FDA CDS guidance definition | DA-34, UX-US-72 |
| Software for patients or caregivers (not health care professionals) that supports or recommends meets the device definition; time-critical decisions do not meet CDS Criterion 4 | FDA CDS guidance, 29 January 2026 | UX-US-73, UX-US-66 |

Device status is never decided here: when a row such as UX-US-66 or UX-US-73 touches it, say so and route to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.

Whether the person's organization is a covered entity under Section 1557, a provider or deployer under the AI Act, or a developer of certified health IT is a legal question for the owner the person names for legal matters, or owner not named. The map lists the rule and asks.

## 3. A2: the subgroup test

### What a test is expected to document

| Item | As the source states it | Standing | Rows |
|---|---|---|---|
| Test sets, metrics and tools used during TEVV documented | NIST MEASURE 2.1 | Voluntary | DA-13 |
| Representative data for development, testing and monitoring; performance across subgroups of intended use | FDA draft, 7 January 2025 | Draft | DA-38 |
| Acceptable overall performance can mask lower performance in subgroups | FDA draft, 7 January 2025 | Draft | DA-43 |
| Test data independent (for example other sites) and sequestered; leakage creates uncertainty about true performance | FDA draft, 7 January 2025 | Draft | DA-39, DA-41 |
| Data split described (training, tuning, tuning evaluation, other subsets) | FDA draft, 7 January 2025 | Draft | DA-40 |
| Reference standard and its uncertainty described | FDA draft, 7 January 2025 | Draft | DA-42 |
| Bias examination for health and safety, fundamental rights and prohibited discrimination, especially where outputs feed future inputs | AI Act Art 10(2)(f) | Law, applies from the Chapter III dates | DA-48, DA-67 |
| Data sets relevant, sufficiently representative, as free of errors and complete as possible, with appropriate statistical properties for the intended persons or groups; reflect the geographical, contextual, behavioral or functional setting | AI Act Art 10(3), 10(4) | Law, Chapter III dates | DA-49, DA-50 |
| Instructions give performance for specific persons or groups, when appropriate | AI Act Art 13(3)(b)(v) | Law, Chapter III dates | DA-57 |
| Hold-out test set used once; a new independent test set for an updated model; early train-test split | EMA reflection paper (medicinal product lifecycle) | Final reflection paper | DA-73, DA-74 |
| "Reference standard", not "ground truth"; "internal testing" and "external testing" | CLAIM 2024, DOI 10.1148/ryai.240300 | Reporting guideline | DA-86 |
| Measures of discrimination, calibration and clinical utility; fairness approaches and rationale; the output and threshold rationale | TRIPOD+AI items 12e, 14, 15 | Reporting guideline | CV127 |
| Differences between development and evaluation data | TRIPOD+AI item 16 | Reporting guideline | CV128 |

The word "validation" means different things across these sources (research file "Changes and conflicts" 5): name the data subset, never rely on the word.

### Metric definitions (computed by `scripts/subgroup_check.py`)

| Term | As the source defines it | Rows |
|---|---|---|
| Three fairness axes | Equal outcomes, equal performance, equal allocation | DA-113 (Rajkomar 2018, DOI 10.7326/M18-1990) |
| Equal performance types | Equal sensitivity (equal opportunity); equal sensitivity and specificity (equalized odds); equal PPV (predictive parity) | DA-114 (same) |
| Statistical parity | Equal probability of positive classification across values of the protected attribute; the least rigorous notion | DA-117 (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9) |
| Equalized odds | Equal probability of correct classification conditional on outcome | DA-118 (same) |
| The impossibility result | For any single threshold, a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates | DA-119 (same) |
| The choice | Criteria are mutually incompatible; which one fits depends on the decision | DA-116 (same) |

Rule for answers: when outcome rates differ between groups and the person asks for both calibration and equal error rates, state DA-119 and ask which criterion fits the decision. Never report all metrics as pass or fail. No source sets a fairness tolerance (research file "Not sourced"): never supply one.

### Using special-category data to detect bias (EU)

- The omnibus deletes AI Act Article 10(5) and inserts Article 4a with the same conditions; older guidance citing "Article 10(5)" now points to Article 4a(1) (DA-51).
- Conditions: only if other data, including synthetic or anonymized data, will not do; re-use limits, pseudonymization, access controls, no transfer, deletion after correction, records of why (DA-52).
- Deployers of high-risk systems and providers or deployers of other AI systems may also do so under the same safeguards; no new duty is created (DA-53).
- The start date of Article 4a is an open reading point in the operative text read (research file "Changes and conflicts" 1): say so; never give a date.
- GDPR still applies: DPIA before processing likely to result in high risk (EN-111), with the content in Article 35(7) (EN-112); data protection by design and by default (EN-108, EN-109).

## 4. B1: release controls

| Control | As the source states it | Standing | Rows |
|---|---|---|---|
| Oversight measures commensurate with risk, autonomy and context; built in by the provider and/or implemented by the deployer | AI Act Art 14(3) | Law, Chapter III dates | DA-59 |
| Overseers aware of automation bias | AI Act Art 14(4)(b) | Same | DA-60 |
| Overseers can disregard, override or reverse output and interrupt to a safe state | AI Act Art 14(4)(d), (e) | Same | DA-61 |
| Accuracy levels and metrics declared in the instructions for use | AI Act Art 13(3)(b)(ii), 15(3) | Same | DA-56, DA-62 |
| Changes pre-determined at the initial conformity assessment listed in the instructions | AI Act Art 13(3)(c) | Same | DA-58 |
| Systems that keep learning after release reduce biased outputs feeding future inputs | AI Act Art 15(4) | Same | DA-63 |
| Automatic event logs over the lifetime; logs support risk identification, post-market monitoring and deployer monitoring | AI Act Art 12(1), 12(2) | Same | DA-54, DA-55 |
| Post-market monitoring collects and analyzes performance data over the lifetime; plan template due as Commission guidance by 2 September 2027 | AI Act Art 72(2), 72(3) as amended | Law; template date as amended | DA-65, DA-66 |
| AI literacy: measures to support staff AI literacy; no guaranteed level per person | AI Act Art 4 as amended | Law; Chapter I applied from 2 February 2025 | AI EU-14, AI EU-15, AI EU-20 |
| Health care professional can independently review the basis of non-device CDS recommendations; inputs explained; plain-language algorithm basis; knowns and unknowns shown | FDA CDS guidance, 29 January 2026, Criterion 4 | Final guidance (device boundary) | UX-US-65, UX-US-67 to UX-US-69 |
| Usability testing may be needed to show Criterion 4 is met | FDA CDS guidance | Final guidance | UX-US-71 |
| Plain-language source attributes for a limited set of users; flag missing attributes; user feedback captured and exported | 45 CFR 170.315(b)(11) | Certification criterion today; HTI-5 proposes removing source attributes and risk management (proposed only) | UX-US-55, UX-US-56, UX-US-59, UX-US-60 |
| Model card as a possible format for public summaries and labeling | FDA draft, 7 January 2025 | Draft | DA-46 |
| Transparency: appropriate information, including logic where available, clearly communicated | FDA, Health Canada and MHRA principles, June 2024 | Guiding principles | AI US-32, AI US-33 |
| Postmarket performance monitoring plan within the quality system | FDA draft, 7 January 2025 | Draft; plans generally not required for 510(k) unless a special control | DA-44, AI US-37, AI US-38 |
| Track existing, unanticipated and emergent risks against intended and actual performance in deployment | NIST MEASURE 3.1 | Voluntary | DA-14 |
| Risk treatments, response and recovery, communication plans documented and monitored; post-deployment monitoring plans | NIST MANAGE 4, 4.1 | Voluntary | DA-16 |
| Weigh viable non-AI alternatives | NIST MANAGE 2.1 | Voluntary | DA-15 |
| Continuous, transparent assessment during actual use | WHO principle 6 | WHO guidance | DA-29 |
| Deployed models are monitored and retraining risk is managed | GMLP principle 10 | Guiding principle | AI UK-10 |
| Early live evaluation of AI decision support: user agreement and reasons for variation; errors and malfunctions; usability and learning curves; modifications during the study | DECIDE-AI, DOI 10.1136/bmj-2022-070904 | Reporting guideline | DA-80 to DA-84 |
| Generative AI: governance, content provenance, pre-deployment testing, incident disclosure | NIST AI 600-1 | Companion resource | DA-18 |
| Large-scale LMM deployment: governments should introduce mandatory post-release auditing by independent third parties | WHO LMM guidance (a recommendation to governments, not a duty on the person) | WHO guidance | DA-33 |
| England: developer clinical risk management under DCB0129, deploying organization assessment under DCB0160; adopters should not adopt non-compliant technology | NHS guidance pages on DCB0129 and DCB0160 | Information standards | CP-UK-05 to CP-UK-10 |
| England: the manufacturer shares the DCB0129 Clinical Safety Case Report with the deploying organization; a Clinical Safety Officer is required (blog, not the standard) | AI and Digital Regulations Service blog | Blog; confirm against the specification | CP-UK-11 |
| Covered entity: mitigate the risk of discrimination from a tool's use | 45 CFR 92.210 | Law for covered entities | PE-113, PE-115 |

The blocking rule, the allowed difference, who may accept a difference and the written reason they give, the monitoring cadence, and release go or no-go are the person's. The sources above say what a control covers; none sets a number.

## 5. Dates that are often wrong

| Fact | Correct date and instrument | Rows |
|---|---|---|
| AI Act Articles 9 to 15 for MDR or IVDR devices (Annex I) | 2 August 2028, Regulation (EU) 2026/1744 (the 2024 text said 2 August 2027) | AI EU-19, DA-67, AI EU-14 |
| AI Act Articles 9 to 15 for Annex III systems | 2 December 2027, Regulation (EU) 2026/1744 (the 2024 text said 2 August 2026) | AI EU-19, DA-67 |
| Article 72(3) monitoring plan template | Commission guidance by 2 September 2027 (the 2024 text said implementing act by 2 February 2026) | DA-66, AI EU-35 |
| Special-category data for bias detection | Article 4a (Article 10(5) deleted); start date an open reading point | DA-51, research file conflict 1 |
| FDA AI-enabled device software functions guidance | Draft of 7 January 2025, still draft on 19 October 2026 | AI US-19, AI US-21 |
| FDA CDS guidance | 29 January 2026 (supersedes 6 January 2026) | UX-US-64 |
| 45 CFR 92.210(b), (c) | Within 300 days of 5 July 2024 | PE-115 |
| HTI-5 removal of DSI source attributes | Proposed 29 December 2025; not final | UX-US-60 |
| PROBAST-2019 | Superseded by PROBAST+AI (Moons et al., BMJ 2025, DOI 10.1136/bmj-2024-082505) | DA-78 |
