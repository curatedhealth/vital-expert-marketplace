# Data requirements: cohort, definitions, features, splits and handoff

Interpretive reference for A1 and B1. Every rule carries the row it came from in `data-and-ai-research.md` (DA), `clinical-study-and-rwe-research.md` (CV) or `patient-engagement-equity-research.md` (PE); the row holds the URL, the verbatim quote and the read date. Market tags: [US], [EU], [INTL] (published method or community standard). A rule from one market used for another is labeled "context". No row sets a count, a missingness cutoff or a sample size; those are the person's.

## 1. Cohort rule and definitions

| Rule | Source and date | Rows |
|---|---|---|
| Write a conceptual definition (clinical criteria) for the population, exposure, outcome and covariates, then an operational definition (often a code algorithm) derived from it | FDA RWD guidance on EHR and claims data (drugs and biologics), July 2024 [US] | CV78, CV80 |
| An operational definition's accuracy is measured against a reference standard with sensitivity, specificity, PPV and NPV; these quantify misclassification | Same guidance [US] | CV81 |
| Reliability means accuracy, completeness and traceability; relevance means data on the key variables and enough representative patients | Same guidance [US] | CV79 |
| Traceability (for example an audit trail) establishes where a data point came from | Same guidance [US] | CV82 |
| Claims-based cohorts address continuity of coverage (enrollment and disenrollment) and continuity of care | Same guidance [US] | CV83 |
| Using an existing registry requires that its consent covers the proposed use, or re-consent | FDA registries guidance, December 2023 [US] | CV85 |
| The initial population is the cohort the denominator is selected from; the developer specifies codes and sequencing; the denominator is described in words, not codes, with age, setting, diagnosis, procedures and time interval | CMS Measures Management System Hub, read 20 October 2026 [US, quality measures; context elsewhere] | DA-133, DA-134 |
| In OMOP, an observation period is the span in which events are recorded, and absence of a record means the event did not occur in that span: the basis for denominators and completeness | OHDSI CDM v5.4 specification page, community standard [INTL] | DA-105 |
| Each OMOP person_id is a distinct person; linkage that identifies persons is done before loading | Same page, community standard [INTL] | DA-106 |
| The unit of a row (patient, encounter, device-day) is named in the cohort rule | Old task DH-01.04.4.1.1 (method, not a source row) | none |

What this means for A1: the cohort rule names population, time window, care setting, exclusions and unit of row (old task), each exclusion as a step with a count (script `cohort`). A count that rises after a linkage step (flag C1) is reported as a fact; DA-106 says linkage comes before the person table is written.

## 2. Features

| Rule | Source and date | Rows |
|---|---|---|
| Data governance covers preparation operations (annotation, labeling, cleaning, updating, enrichment, aggregation), assumptions, availability, bias examination and data gaps | EU AI Act Article 10(2), Regulation (EU) 2024/1689 [EU; applies to high-risk systems from 2 December 2027 (Annex III) or 2 August 2028 (Annex I), DA-67] | DA-47 |
| Examine biases, especially where outputs feed future inputs | EU AI Act Article 10(2)(f) [EU] | DA-48 |
| Special-category data for bias detection: only when other data, including synthetic or anonymized data, will not do, with safeguards; now Article 4a (Article 10(5) deleted by Regulation (EU) 2026/1744); no new duty to detect bias | EU AI Act Article 4a as inserted by the Digital Omnibus [EU] | DA-51, DA-52, DA-53 |
| Label bias: the outcome is ascertained differently across groups; feature bias for predictors | Paulus and Kent 2020 [PAPER] [INTL] | DA-120, DOI 10.1038/s41746-020-0304-9 |
| Label bias also arises where groups were systematically misdiagnosed | Rajkomar et al. 2018 [PAPER] [INTL] | DA-115, DOI 10.7326/M18-1990 |
| A covered entity must make reasonable efforts to identify patient care decision support tools that use race, color, national origin, sex, age or disability inputs, and to mitigate the risk of discrimination; compliance date 300 days after 5 July 2024 | 45 CFR 92.210 (eCFR, read 19 October 2026) [US] | PE-113, PE-114, PE-115 |
| Describe how missing data were handled | TRIPOD+AI item 11 (Collins et al. 2024) [PAPER] [INTL] | CV126, DOI 10.1136/bmj-2023-078378 |
| Missing data are defined relative to a specific estimand | ICH E9(R1), adopted 20 November 2019 [INTL] | CV41 |
| Plan in advance how a decision rule behaves when a tailoring variable is missing | Nahum-Shani et al. 2018 [PAPER] [INTL] | TM89, DOI 10.1007/s12160-016-9830-8 |
| A feature known only after the outcome, or not available at decision time, is not used | Old task DH-01.04.4.1.2 (method, not a source row) | none |

What this means for A1: each feature is written so it can be rebuilt (name, source field, window relative to the index time, missing-value code, available at decision time). The script `features` flags windows ending after the index time (F3), features not available at decision time (F5) and features derived from the outcome (F7) as candidates to refuse; the person refuses. It flags inputs that measure a 92.210 characteristic (F6); whether the person's organization is a covered entity and how risk is mitigated is for the owner the person names for legal matters, or owner not named.

## 3. Data splits

| Rule | Source and date | Rows |
|---|---|---|
| The draft proposes describing how development data were split into training, tuning, tuning evaluation and other subsets | FDA AI-enabled device software functions draft guidance, January 2025, not for implementation [US] | DA-35, DA-40 |
| The draft proposes that test data be independent (for example from different sites) and sequestered; leakage between validation and development data creates uncertainty about true performance | Same draft [US] | DA-39 |
| The draft proposes that test data generally come from sites different from those used for development | Same draft [US] | DA-41 |
| An early train-test split, before normalization or other aggregate processing, is strongly encouraged | EMA reflection paper on AI in the medicinal product lifecycle, final, adopted 9 September 2024 [EU, medicinal products; context for devices] | DA-68, DA-74 |
| The hold-out test set is used once; an updated model needs a new independent test set | Same paper [EU] | DA-73 |
| Use "internal testing" (held-out subset of training data) and "external testing" (completely external dataset) rather than "validation" | CLAIM 2024 update (Tejani et al. 2024) [PAPER] [INTL] | DA-86, DOI 10.1148/ryai.240300 |
| Identify differences between development and evaluation data in setting, eligibility, outcome and predictors | TRIPOD+AI item 16 [PAPER] [INTL] | CV128, DOI 10.1136/bmj-2023-078378 |
| Training, validation and testing data are relevant, sufficiently representative and, as far as possible, free of errors and complete; they reflect the geographical, contextual, behavioral or functional setting of use | EU AI Act Article 10(3) and 10(4) [EU] | DA-49, DA-50 |

What this means for A1: the script `split` counts patients and sites per subset and flags patients in more than one subset (S1) and sites shared between development and test (S2). Both are facts; whether the split fits the intended use is the person's.

## 4. Handoff, provenance and standards

| Rule | Source and date | Rows |
|---|---|---|
| FAIR: 15 principles under Findable, Accessible, Interoperable, Reusable; R1.1 a clear usage license, R1.2 detailed provenance, R1.3 community standards; FAIR is a guide, not a standard | Wilkinson et al. 2016 [PAPER] [INTL] | DA-99, DA-100, DA-101, DOI 10.1038/sdata.2016.18 |
| Document data curation and transformation (audit trails, quality control) and changes made to conform to standards, with their impact | FDA RWD data standards guidance, December 2023 (drug submissions) [US; context for devices] | CV87 |
| Absent a waiver, study data derived from RWD in covered drug submissions use the formats in the FDA Data Standards Catalog | Same guidance [US] | CV86 |
| For medicinal product trials, the pre-processing pipeline and all models are frozen and documented in the statistical analysis plan before database lock | EMA reflection paper, 2024 [EU] | DA-71 |
| Give details of data and code availability | TRIPOD+AI items 18e and 18f [PAPER] [INTL] | CV128, DOI 10.1136/bmj-2023-078378 |
| OMOP CDM is an open community data standard; OHDSI standardized vocabularies are central; v5.5 is the version OHDSI names as current | OHDSI documentation, read 20 October 2026, community standard [INTL] | DA-102, DA-103, DA-104 |
| DARWIN EU data partners standardize data to the OMOP common data model | EMA DARWIN EU page, read 19 October 2026 [EU] | CV109 |
| USCDI is a standardized set of data classes and elements for exchange; 45 CFR 170.213 adopts v1 (adoption expired 1 January 2026) and v3; v5 (16 July 2024), v6 (24 July 2025) and v7 (23 July 2026) are published versions, not certification requirements until a rule adopts them; enforcement discretion applies to certain v3 elements | ONC USCDI page and eCFR, read 20 October 2026 [US] | DA-107 to DA-112 |
| The handoff names the dataset version, the cohort rule, the missingness that remains and who may change the cohort rule; no dataset is handed over without a version | Old task DH-01.04.4.1.3 (method, not a source row) | none |

What this means for A1: the handoff is a versioned record (version, cohort rule, feature list with refused features, split counts and flags, remaining missingness per feature, provenance and license, who may change the rule). FAIR and OMOP are named as a guide and a community standard; USCDI versions are stated with their certification status kept apart from publication.
