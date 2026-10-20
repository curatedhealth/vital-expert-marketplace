# Real-world evidence and digital endpoints inside a review

Interpretive reference. CV rows are in `CLINICAL_STUDY_AND_RWE.md`, ES rows in `EVIDENCE_SYNTHESIS_METHODS.md`, all read 19 October 2026. FDA guidance is nonbinding except where it restates law; ICH guidelines bind only as each region adopts them (research file header). These sources set required elements and definitions; they do not set accuracy thresholds, sample sizes or effect sizes for digital endpoints (research file scope note). Those stay the person's.

Use this file when the review includes real-world data studies, registry or claims analyses, or outcomes captured by apps, wearables or sensors. Designing a new RWE study or instrumenting an endpoint for a new trial belongs to clinical study design (DH-01.02.1); this file is for appraising what is already published or held.

## 1. Definitions

| Term | Definition | Row |
|---|---|---|
| Real-world data (RWD) | Data on patient health status or care delivery, routinely collected from a variety of sources | CV73 |
| Real-world evidence (RWE) | Clinical evidence on use and potential benefits or risks derived from analysis of RWD | CV73 |
| Device RWD sources | EHRs, claims, product and disease registries, and data from DHTs; RWD can support RCTs, single-arm, observational and hybrid designs | CV89 |
| Registry | An organized system collecting standardized data for a population defined by a disease, condition or exposure | CV84 |
| Non-interventional study | Product used in routine practice, not assigned by protocol | CV74 |
| Digital health technology (DHT) | A system using computing platforms, connectivity, software and/or sensors for health care and related uses | CV43 |
| BioMeT (V3 paper) | Connected products that process mobile-sensor data with algorithms into measures of behavioral or physiological function [PAPER] doi 10.1038/s41746-020-0260-4 | CV156 [PAPER] doi 10.1038/s41746-020-0260-4 |

## 2. Is the RWD fit for purpose? Name the framework you apply

The research file records that the frameworks use different words. Pick the one that matches the decision and say which.

| Framework | Reliability | Relevance | Rows |
|---|---|---|---|
| FDA EHR and claims guidance, drugs and biologics (July 2024) | Accuracy, completeness, traceability | Data on key variables (exposures, outcomes, covariates) and enough representative patients | CV78, CV79 |
| FDA CDRH device RWE guidance, final 18 December 2025 (supersedes 31 August 2017) | Accrual, quality, integrity | Availability, timeliness, generalizability; linkage may fill gaps | CV88, CV91, CV92 |
| ICH E6(R3) Annex 2 (Step 4 on 3 June 2026; EU effective 15 January 2027) | Accuracy, completeness, provenance, traceability | Key data elements available | CV2, CV23 |

Appraisal questions to put to each RWD study, each tied to its row:

1. Did the sponsor do and report a relevance and reliability assessment, with limitations (device guidance)? (CV90)
2. Are key variables given a conceptual definition and an operational definition, and was the operational definition validated (sensitivity, specificity, PPV, NPV against a reference standard)? (CV80, CV81)
3. Is provenance traceable, for example by audit trail? (CV82)
4. For claims data: is continuity of coverage and of care addressed? (CV83)
5. Were protocol and analysis plan finalized before outcome data were seen, and does the report say so? (CV75, CV94)
6. Is the protocol posted publicly (ClinicalTrials.gov or ENCePP) and, in the EU, registered in the HMA-EMA Catalogue of RWD studies? (CV77, CV108)
7. Was data linkage prespecified, with how inconsistencies are resolved? (CV24)
8. For a registry reused: does consent cover the use? (CV85)
9. For a causal question: was target trial emulation considered (EMA reflection paper, adopted 17 March 2025, scope non-interventional studies only)? (CV104, CV105, CV107)
10. Can patient-level data be submitted if a regulator asks (drug submissions)? (CV76)

The answers are the person's appraisers' to give; the model lays out the passage for each question with its locator, or `[GAP]` where the paper is silent.

Risk of bias for comparative RWD studies uses ROBINS-I (ES-75 [PAPER] doi 10.1136/bmj.i4919, ES-164); low risk for confounding is exceptional (ES-79); uncontrolled before-after designs usually rate serious or critical (ES-78); certainty for sound non-randomized evidence is generally low (ES-100). STROBE is a reporting guide for cohort, case-control and cross-sectional studies, not an appraisal tool; its item wording was not read [PAPER] doi 10.1371/journal.pmed.0040296 (CV123 [PAPER] doi 10.1371/journal.pmed.0040296).

## 3. Is the digital endpoint validated? Name the framework you apply

| Framework | Steps | Rows |
|---|---|---|
| FDA DHT guidance, final December 2023 | Verification: the measured parameter (for example acceleration) is measured accurately and precisely. Validation: the DHT appropriately assesses the clinical event or characteristic in the proposed population. Required whether or not the DHT is a device; not the Quality System Regulation terms. | CV42, CV46, CV47 |
| V3 (Goldsack et al. 2020, a peer-reviewed framework, not FDA policy) [PAPER] doi 10.1038/s41746-020-0260-4 | Verification (bench, sensor against reference), analytical validation (algorithm in human participants, usually by its developer), clinical validation (meaningful clinical state in the context of use, cohorts with and without the phenotype, usually by the sponsor) | CV155 [PAPER] doi 10.1038/s41746-020-0260-4, CV157 [PAPER] doi 10.1038/s41746-020-0260-4, CV158 [PAPER] doi 10.1038/s41746-020-0260-4, CV159 [PAPER] doi 10.1038/s41746-020-0260-4 |

The two map roughly but are not identical, and V3 is not an FDA requirement (research "Changes and conflicts").

Appraisal questions for a study that used a digital endpoint:

1. Was V&V shown in the population studied, not only in healthy volunteers? Algorithms valid in healthy people may fail in patients (the shuffling-gait example). (CV48)
2. Which V&V evidence exists: reference comparisons, placement or interference, calibration, cross-model consistency, remote versus clinic? (CV49)
3. Is the endpoint defined precisely: assessment type, timing, tool, and how repeated measures combine? (CV55)
4. For a novel endpoint: does it reflect how a patient feels, functions or survives, and is the effect meaningful to patients? (CV56)
5. Was the same collection method used in all arms? Is a non-inferiority margin justified with similar DHT measurements? (CV58)
6. Were usability evaluations done in the trial population? (CV51)
7. Late-phase trials: is the estimand described under ICH E9(R1), with a plan for missing data? (CV59, CV33, CV34, CV41)
8. Decentralized elements: did the protocol fix which visits were site, remote or the participant's choice? Letting participants choose can bias results. (CV67)

Usability or engagement data are not clinical evidence of benefit; report them as what they are.

## 4. Reporting guidelines a review checks included studies against

| Study type | Guideline | Row |
|---|---|---|
| Randomized trial | CONSORT 2025, 30 items, supersedes CONSORT 2010 [PAPER] doi 10.1136/bmj-2024-081123; outcome specification includes variable, metric, aggregation and time point | CV110 [PAPER] doi 10.1136/bmj-2024-081123, CV113 [PAPER] doi 10.1136/bmj-2024-081123 |
| Trial of an AI intervention | CONSORT-AI, 14 items added to CONSORT 2010 (parent now superseded) [PAPER] doi 10.1136/bmj.m3164 | CV118 [PAPER] doi 10.1136/bmj.m3164, CV119 [PAPER] doi 10.1136/bmj.m3164 |
| Prediction model, regression or machine learning | TRIPOD+AI, 27 main items, supersedes TRIPOD 2015 [PAPER] doi 10.1136/bmj-2023-078378 | CV124 [PAPER] doi 10.1136/bmj-2023-078378 |
| Observational study | STROBE, 22 items, reporting guide only [PAPER] doi 10.1371/journal.pmed.0040296 | CV123 [PAPER] doi 10.1371/journal.pmed.0040296 |
| Trial registration | Registered at or before first patient consent (ICMJE); WHO TRDS 24 items; US law within 21 days of first enrollment | CV132, CV138, CV141 |

A reporting checklist says what a paper reports, not how good the study is (ES-04 for PRISMA; CV123 [PAPER] doi 10.1371/journal.pmed.0040296 for STROBE).

## 5. What the library can and cannot give here

- `literature.find_trial` links a paper to its ClinicalTrials.gov entry; the record's own `trial_ids` stays empty (`tools.md`, register N8).
- The library holds no RWD catalogue (HMA-EMA catalogues, ENCePP), no device registry and no DHT validation dataset `[GAP]`. Ask the person for the study's RWD assessment and V&V reports.
