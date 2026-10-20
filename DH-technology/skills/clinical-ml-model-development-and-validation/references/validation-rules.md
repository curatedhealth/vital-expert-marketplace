# Validation rules for a clinical model

What the sourced rows say about writing the intended use, locking the data, naming the metrics, recording the result, and promoting or pulling back a model. Every rule carries its row id; the rows (URL, verbatim quote, read date) are in `DATA_AND_AI.md` (DA), `AI_ML_REGULATION.md` (US, EU, UK, IM), `CLINICAL_STUDY_AND_RWE.md` (CV) and `THERAPEUTIC_MECHANISM_AND_TRANSLATION.md` (TM). Nothing here sets a threshold: no source in this skill sets an AUROC target, a sensitivity floor, a calibration tolerance, a drift threshold or a fairness tolerance (DATA_AND_AI.md, "Not sourced"). Those are the person's.

## 1. Status of each source: draft, final, voluntary

| Source | Status as read | Rows | How to use it |
|---|---|---|---|
| FDA, Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations | Draft guidance issued 7 January 2025; still draft on 19 October 2026; on CDRH's FY 2027 A-list as a final guidance it intends to publish | DA-35, US-19, US-21, US-22 | A proposal. Say "the January 2025 draft recommends"; never "FDA requires" |
| FDA, PCCP final guidance for AI-enabled devices | Final, reissued 18 August 2025 | US-01 to US-14, US-36 | Device questions route to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| FDA request for comment on real-world performance and drift (FDA-2025-N-4203) | A request for comment, not guidance | US-39 | Context only |
| GMLP guiding principles | IMDRF final document, January 2025 (FDA restatement; IMDRF PDF not fetched) | US-29, UK-09, UK-10, IM-01 | Principles, not requirements |
| IMDRF N93, Technical Framework for AI Life Cycle Management | Draft dated 7 April 2026 [WF] | IM-04 | Draft; say so |
| EU AI Act Articles 10, 12 to 15, 72 | Law; Chapter III Sections 1 to 3 apply from 2 August 2028 for AI in MDR or IVDR devices (Annex I) and 2 December 2027 for Annex III systems, as amended by Regulation (EU) 2026/1744 | DA-47 to DA-67, EU-17 to EU-19 | Give the date with the act that set it; the 2024 text's dates (2 August 2026 and 2 August 2027) are replaced (DA conflicts 3) |
| EMA reflection paper on AI in the medicinal product lifecycle | Final, adopted by CHMP 9 September 2024 | DA-68 to DA-75 | Written for medicines; say so when used for a device |
| NIST AI RMF 1.0 and NIST AI 600-1 | Voluntary, not sector-specific | DA-01 to DA-21 | A checklist, never a requirement |
| ISO/IEC 42001 and 23894 | Abstract pages only [WF]; no clause text read | DA-22, DA-23 | Name only; give no requirement from them |
| WHO ethics and governance of AI for health (2021); WHO LMM guidance (page dated 25 March 2025) | Publication pages and news releases only | DA-24 to DA-34 | Principles; full text not read |
| TRIPOD+AI, PROBAST+AI, DECIDE-AI, CLAIM 2024, CONSORT-AI, SPIRIT-AI | Published reporting or appraisal guidelines [PAPER] | CV118 to CV128, DA-76 to DA-86 | Cite with the DOI of each paper |

## 2. Name the data subset, not the word "validation"

"Validation" means different things across sources (DA conflicts 5): NIST uses the ISO 9000 sense, confirmation by objective evidence that requirements for a specific intended use are met (DA-06); EMA uses "validation" for tuning data and "test" for the hold-out set; CLAIM 2024 asks authors to use "internal testing" and "external testing" and to say "reference standard", not "ground truth" (Tejani et al. 2024, DOI 10.1148/ryai.240300, DA-86); the FDA draft uses "tuning" and "test" for development and "validation" for performance validation. In every answer, name the subset: training, tuning, internal test, external test (site), external test (time).

## 3. Intended use comes first

- Name the user, the input, the output, the decision the output may support, the decision it must not make, and the population (old task DH-01.04.3.1.1). A model whose intended use is "clinical decision support" with no decision named is not validated (same task).
- NIST MAP 1.1: intended purposes, context-specific laws and norms, and deployment settings are understood and documented (DA-10). MAP 2.2: knowledge limits and how output is used and overseen by humans are documented (DA-11).
- TRIPOD+AI items 3b and 3c: target population, intended purpose in the care pathway, intended users; known health inequalities between sociodemographic groups (Collins et al. 2024, DOI 10.1136/bmj-2023-078378, CV125).
- WHO principle 2: designers should satisfy regulatory requirements for safety, accuracy and efficacy for well-defined use cases or indications (WHO news release, 28 June 2021, DA-26).
- An AI-enabled device software function implements one or more models to achieve its intended purpose (FDA draft, January 2025, DA-36). Whether a product is a device is the developer's call with `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## 4. Lock the data before the run

| Rule | Row |
|---|---|
| Describe how development data were split into training, tuning, tuning evaluation and other subsets, and which activity used each (draft) | DA-40 |
| Say whether test data are independent (for example from different sites) and sequestered from developers; leakage between validation and development data creates uncertainty about true performance (draft) | DA-39 |
| Test data should generally come from sites different from those used to develop the model (draft) | DA-41 |
| Split train and test early, before normalization or other aggregate processing (EMA, medicines) | DA-74 |
| The hold-out test set is used once; a new independent test set is needed to repeat the test for an updated model (EMA, medicines) | DA-73 |
| For high-impact uses such as a primary endpoint, test on prospectively generated data (future calendar time) from a representative setting (EMA, medicines) | DA-72 |
| Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible free of errors and complete in view of the intended purpose (EU AI Act Article 10(3), law, applies from 2 August 2028 for Annex I devices) | DA-49, DA-67 |
| Data sets reflect the geographical, contextual, behavioral or functional setting of intended use (Article 10(4)) | DA-50 |
| Data governance covers design choices, collection and origin, preparation (annotation, labelling, cleaning, updating, enrichment, aggregation), assumptions, availability, bias examination, bias measures and data gaps (Article 10(2)) | DA-47, DA-48 |
| Special-category data for bias detection: Article 10(5) deleted; the same conditions now sit in Article 4a, which creates no duty to detect bias; the exact start date of Article 4a is an open reading point | DA-51 to DA-53; DA conflicts 1 |
| Name the source, the inclusion rule and the count; state how the test data differ from training (site or time); name a population in the intended use that is absent and mark it `[GAP]` (old task DH-01.04.3.1.2) | old task |
| Justify study size separately for development and evaluation; describe missing-data handling; identify differences between development and evaluation data in setting, eligibility, outcome and predictors (TRIPOD+AI items 10, 11, 16) | CV126, CV128 |
| Describe how the reference standard was set and its uncertainty (draft) | DA-42 |

Data preparation, cohort rules and data quality checks themselves belong to `data-preparation-and-analytics-methods` and `data-quality-monitoring` (this pack).

## 5. Name the metrics before the run

- Report the metric named before the run, on the locked dataset; do not add a metric after the run to improve the story (old task DH-01.04.3.1.3).
- TRIPOD+AI item 12e: specify all measures and plots, with rationale, for discrimination, calibration and clinical utility; item 15: the model output and the rationale for any threshold (CV127).
- NIST MEASURE 1.1: start with the most significant risks; document risks that will not or cannot be measured (DA-12). MEASURE 2.1: test sets, metrics and tools are documented (DA-13).
- EU AI Act: levels of accuracy and the relevant accuracy metrics are declared in the instructions for use (Article 15(3), DA-62); instructions state accuracy, robustness and cybersecurity tested and validated, and circumstances that may affect them (Article 13(3)(b)(ii), DA-56); when appropriate, performance for specific persons or groups (Article 13(3)(b)(v), DA-57). Law; applies from 2 August 2028 for Annex I devices (DA-67).
- The values (an AUROC floor, a sensitivity at a threshold, a calibration range) are the person's. The model writes "not given" and asks; it never supplies one.

## 6. Subgroups and fairness

- Good overall performance can mask poor performance in subgroups (FDA draft, DA-43); bias control includes representativeness for development, testing and monitoring and subgroup evaluation (DA-38).
- NIST names three bias categories: systemic, computational and statistical, and human-cognitive; each can occur without discriminatory intent (DA-08).
- Fairness criteria (Rajkomar et al. 2018, DOI 10.7326/M18-1990, DA-113 to DA-115; Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-116 to DA-120): equal outcomes, equal performance and equal allocation; equal sensitivity (equal opportunity), equalized odds, predictive parity; statistical parity is the least rigorous. Label bias arises where the outcome is differentially ascertained across groups (DA-115, DA-120).
- **Impossibility.** For any single threshold, a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119). When the person's criteria conflict, state this row and ask which criterion fits the decision (DA conflicts 7). Fairness concerns apply specifically to polar decisions such as allocating scarce resources (DA-116).
- TRIPOD+AI item 14: describe approaches used to address fairness and their rationale (CV127).
- Fairness tolerances are the person's; none is sourced. Governance controls, bias questions and 45 CFR 92.210 duties for patient care decision support tools belong to `responsible-ai-governance` (this pack).

## 7. Appraisal and reporting checklists

| Checklist | What it is | Rows (DOI) |
|---|---|---|
| TRIPOD+AI | 27 main items, 52 subitems, for prediction models using regression or machine learning; supersedes TRIPOD 2015 | CV124 to CV128 (DOI 10.1136/bmj-2023-078378) |
| PROBAST+AI | Development part (16 signalling questions, quality) and evaluation part (18, risk of bias); four domains each; yes or probably yes means low concern; supersedes PROBAST-2019 | DA-76 to DA-79 (DOI 10.1136/bmj-2024-082505) |
| DECIDE-AI | Early-stage live clinical evaluation of AI decision support: 17 AI-specific items (28 subitems), 10 generic; report changes during the study, user agreement and variation, errors, usability and learning curves | DA-80 to DA-84 (DOI 10.1136/bmj-2022-070904) |
| CLAIM 2024 | Imaging AI; each item answered Yes, No or Not Applicable; item list in a supplement not read | DA-85, DA-86 (DOI 10.1148/ryai.240300) |
| CONSORT-AI, SPIRIT-AI | Trials of AI interventions and their protocols | CV118 to CV122 (DOI 10.1136/bmj.m3164; DOI 10.1136/bmj.m3210) |

A checklist item answered "No" is a fact about the record, not a verdict on the model. Clinical study design for an AI intervention routes to `dh-clinical-development` study-protocol-and-endpoint-design.

## 8. Transparency

- The FDA draft offers an example model card (Appendix E) as a possible format (draft, DA-46). FDA, Health Canada and MHRA transparency principles (June 2024) build on GMLP principles 7 and 9 (US-32, US-33).
- WHO principle 3: sufficient information is published or documented before design or deployment (DA-27).

## 9. Promotion and pull-back

- A promotion rule names the stages (experiment, validation, production), the record each stage requires (dataset version, metric, approver), and who can promote and who cannot; never promote from a notebook path (old task DH-01.04.2.1.1).
- A run record names the code version, the data version, the metric on the holdout, the approver (or "not approved") and the run id; never overwrite a previous run's metric (old task DH-01.04.2.1.2).
- A drift watch names the input or outcome watched, the threshold, who is paged and what they may do (retrain, roll back, or stop the decision); never watch a metric the product does not log (old task DH-01.04.2.1.3). The threshold is the person's.
- Why watch: input data drift between development and deployment (draft, DA-37); performance may change with populations, disease patterns or data drift, and automation may hide it (draft, DA-45); the draft recommends a postmarket performance monitoring plan within the quality system (DA-44, US-37), generally not required for a 510(k) unless a special control (US-38). Drift types and responses: Sahiner et al. 2023 (DOI 10.1259/bjr.20220878, DA-87 to DA-90); calibration drift (Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-91, DA-92).
- EU AI Act: automatic event logs over the lifetime (Article 12(1), DA-54) that support post-market monitoring (Article 12(2), DA-55); post-market monitoring collects and analyzes performance data over the lifetime (Article 72(2), DA-65); Commission guidance with a template by 2 September 2027 (Article 72(3) as amended, DA-66).
- NIST MEASURE 3.1 and MANAGE 4: track risks on intended versus actual performance; document response, recovery and post-deployment monitoring plans (DA-14, DA-16).
- GMLP principle 10: deployed models are monitored and retraining risk is managed (UK-10).
- Retraining a cleared or approved device: whether the change fits an authorized PCCP (Description of Modifications, Modification Protocol, Impact Assessment, US-03 to US-06) or needs a new submission is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. EU counterpart: pre-determined changes under Article 43(4) (EU-05).
- In a pivotal trial of a medicine, incremental learning is not accepted and models are frozen in the statistical analysis plan before database lock (EMA, DA-70, DA-71).

## 10. Generative and large multi-modal models

If the model is generative: NIST AI 600-1 (July 2024) names twelve risks, including confabulation and human-AI configuration (DA-17 to DA-21); its standing after the revocation of EO 14110 was not checked (DATA_AND_AI.md, "Not sourced"). WHO's LMM guidance flags automation bias and recommends independent post-release audits for large-scale deployment (DA-30 to DA-34, publication page and news release only).
