# Data quality requirements: rules, runs, version comparison and repair

Interpretive reference for A1, A2 and B1. Every rule carries its row in `data-and-ai-research.md` (DA) or `clinical-study-and-rwe-research.md` (CV); the row holds the URL, the verbatim quote and the read date. Market tags: [US], [EU], [INTL]. [PAPER] rows carry their own DOI in the Rows cell. No row sets a limit, an acceptable error share, a drift threshold or a re-run cadence for a company's data; those are the person's.

## 1. The categories a rule belongs to (Kahn)

| Rule | Source and date | Rows |
|---|---|---|
| Three data quality categories (conformance, completeness, plausibility) and two assessment contexts (verification, validation) | Kahn et al. 2016 [PAPER] [INTL] | DA-94, DOI 10.13063/2327-9214.1244 |
| Conformance splits into value, relational and computational conformance | Same paper | DA-95, DOI 10.13063/2327-9214.1244 |
| Value conformance: data elements agree with prespecified constraints (types, domains, allowed values, formats) | Same paper | DA-96, DOI 10.13063/2327-9214.1244 |
| Completeness concerns whether data attributes are present, not their values | Same paper | DA-97, DOI 10.13063/2327-9214.1244 |
| Plausibility has uniqueness, atemporal and temporal subcategories | Same paper | DA-98, DOI 10.13063/2327-9214.1244 |
| Name the checks (unit of row, exclusion count, missingness of decision-time features, no outcome leak), set a fail for each, name the dataset version; a single completeness percentage is not the only check | Old task DH-01.04.4.2.1 (method, not a source row) | none |

How the script maps them: `value_conformance`, `relational_conformance`, `computational_conformance`, `completeness`, `plausibility_uniqueness`, `plausibility_atemporal`, `plausibility_temporal` follow DA-95 to DA-98. `leak` (a feature dated after the index time) and `row_count` (rows against the cohort rule) come from the old task and are labeled "the person's rule, outside Kahn". The context field (verification or validation, DA-94) is the person's.

## 2. Reliability and relevance of real-world data

| Rule | Source and date | Rows |
|---|---|---|
| Reliability means accuracy, completeness and traceability; relevance means data on the key variables and enough representative patients | FDA RWD guidance on EHR and claims data (drugs and biologics), July 2024 [US; context for devices and analytics] | CV78, CV79 |
| Operational definitions are validated against a reference standard with sensitivity, specificity, PPV and NPV, which quantify misclassification | Same guidance | CV81 |
| Traceability (for example an audit trail) establishes provenance | Same guidance | CV82 |
| Claims-based data address continuity of coverage and continuity of care | Same guidance | CV83 |
| Document data curation and transformations (audit trails, quality control) and changes made to conform to standards, with their impact | FDA RWD data standards guidance, December 2023 (drug submissions) [US; context] | CV86, CV87 |
| Risk-based monitoring with centralized monitoring to follow up missing, inconsistent and outlying data | FDA guidance "Conducting Clinical Trials With Decentralized Elements", September 2024 [US; trial context] | CV65, CV71 |

Kahn's validation context (DA-94) and the FDA accuracy measures (CV81) meet here: a validation check compares data with an external reference; the reference and the measure are the person's.

## 3. Dataset qualities and data governance (EU)

| Rule | Source and date | Rows |
|---|---|---|
| Training, validation and testing data are relevant, sufficiently representative and, as far as possible, free of errors and complete in view of the intended purpose | EU AI Act Article 10(3), Regulation (EU) 2024/1689 [EU] | DA-49 |
| Data sets reflect the geographical, contextual, behavioral or functional setting of use | EU AI Act Article 10(4) [EU] | DA-50 |
| Data governance covers preparation operations, assumptions, availability, bias examination and data gaps | EU AI Act Article 10(2) [EU] | DA-47, DA-48 |
| Articles 10 to 15 apply from 2 December 2027 (Annex III systems) and 2 August 2028 (Annex I systems, such as MDR and IVDR devices), as amended | Digital Omnibus, Regulation (EU) 2026/1744 [EU] | DA-67 |

## 4. Structure and denominators (OMOP)

| Rule | Source and date | Rows |
|---|---|---|
| OMOP CDM is an open community data standard; v5.5 is the version OHDSI names as current; field rules here come from v5.4 | OHDSI documentation, read 20 October 2026, community standard [INTL] | DA-102, DA-103 |
| An observation period is the span in which events are recorded; absence of a record means non-occurrence within it: the basis for completeness denominators | OHDSI CDM v5.4 page, community standard | DA-105 |
| Each person_id is a distinct person; linkage happens before loading | Same page | DA-106 |

What this means for a run: completeness of an event is read only inside the observation period; a uniqueness failure on person or encounter keys is resolved before any joined completeness is read.

## 5. Comparing versions and data drift

| Rule | Source and date | Rows |
|---|---|---|
| The draft names data drift (development inputs differing from deployment inputs) as a postmarket performance risk and proposes a postmarket performance monitoring plan | FDA AI-enabled device software functions draft, January 2025, not for implementation [US] | DA-35, DA-37, DA-44 |
| Data drift is a mismatch between training and clinical-use conditions; input data drift is also called covariate shift | Sahiner et al. 2023 [PAPER] [INTL] | DA-87, DA-88, DOI 10.1259/bjr.20220878 |
| Metrics start with the most significant risks; risks not measured are documented; test sets and tools are documented; existing and emergent risks are tracked against intended versus actual performance | NIST AI RMF 1.0, January 2023, voluntary [US] | DA-12, DA-13, DA-14 |
| Descriptive statistics show data are available but are not evidence of reliability or validity | CMS Measures Management System Hub, read 20 October 2026 [US, quality measures; context] | DA-139 |
| Quality measures have an annual update and a comprehensive reevaluation every three years | Same hub [US, quality measures; context only, not a cadence for company data] | DA-140 |

What this means for A2: `compare` prints row counts, missing shares, means, medians and category shares for two versions. A difference is a fact about the data. No row gives a drift threshold; what a shift means for model performance routes to `model-performance-and-drift-monitoring` (this pack).

## 6. Repairs and dataset versions

| Rule | Source and date | Rows |
|---|---|---|
| Name the owner; state whether the feature is removed or redefined; name the new dataset version; do not train on the failed version | Old task DH-01.04.4.2.3 (method, not a source row) | none |
| Run each check and keep the count; mark pass or fail; name a feature that failed the leak check; do not drop a failed feature quietly and report a pass | Old task DH-01.04.4.2.2 (method, not a source row) | none |
| The hold-out test set is used once; an updated model needs a new independent test set | EMA reflection paper on AI in the medicinal product lifecycle, adopted 9 September 2024 [EU, medicinal products; context] | DA-68, DA-73 |
| For medicinal product trials the pre-processing pipeline and models are frozen and documented in the analysis plan before database lock | Same paper | DA-71 |
| Provenance (R1.2) and a clear usage license (R1.1) travel with the data; FAIR is a guide, not a standard | Wilkinson et al. 2016 [PAPER] [INTL] | DA-99 to DA-101, DOI 10.1038/sdata.2016.18 |

What this means for B1: a redefined feature produces a new dataset version; if the earlier test set has already been used to evaluate a model, the EMA paper (context) asks for a new independent test set for the updated model. Whether that applies to the person's product is for the owner the person names.
