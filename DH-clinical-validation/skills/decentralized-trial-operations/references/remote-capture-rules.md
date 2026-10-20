# Remote data capture: the rules and where they come from

Interpretive reference for task A2. Rows are in `clinical-study-and-rwe-research.md`.

## 1. What a DHT is in a trial

- FDA: a DHT is a system using computing platforms, connectivity, software and/or sensors for health care and related uses. CV43
- ICH E6(R3): a data acquisition tool takes data from a human, a machine such as a wearable, or a computer system (glossary); a DHT that acquires participant data for a trial is a data acquisition tool (Annex 2). CV15, CV20
- FDA DHT guidance does not decide whether a DHT is a device, nor how to develop or validate clinical outcome assessments. Device status goes to dh-regulatory-strategy; COA development goes to the study design skill. CV45

## 2. Fit for purpose: verification, validation, usability

| Element | Rule | Row |
|---|---|---|
| Fit for purpose | The level of validation is sufficient to support the use, including interpretability of the data, considering form (design) and function (purpose in the trial). | CV44 |
| Verification (FDA) | The measured parameter (for example acceleration, temperature, pressure) is measured accurately and precisely. | CV46 |
| Validation (FDA) | The DHT appropriately assesses the clinical event or characteristic in the proposed participant population. Required whether or not the DHT is a device. | CV46 |
| Not QSR terms | These terms are not the Quality System Regulation definitions. | CV47 |
| Staging and population | V&V may move from bench to healthy volunteers to the study population; an algorithm valid in healthy people may fail in patients (shuffling gait example). | CV48 |
| Evidence types | Comparison with reference measurements; placement and interference effects; remote versus clinic differences; and others listed in the row. | CV49 |
| Reuse | V&V data from manufacturers, labeling or other FDA submissions by right of reference may be leveraged. | CV50 |
| Usability | Usability evaluations show the trial population can use the DHT as intended without errors; FDA calls them critical. | CV51 |
| Specifications | Sponsors set minimum technical and performance specifications (accuracy, precision, reliability) and may name models or versions. | CV52 |
| Design controls | For a DHT used only in investigations for remote data collection, FDA does not intend to assess design-control compliance when the recommended V&V is done; this does not apply outside investigations. | CV63 |
| Qualification | DDT or MDDT qualification is voluntary and separate from a marketing submission; program details not sourced. | CV64; details `[GAP]` |

**Two vocabularies.** FDA uses two steps (verification, validation). V3 [PAPER] (Goldsack 2020) uses three: verification, analytical validation, clinical validation (CV155 to CV159 (V3, DOI 10.1038/s41746-020-0260-4)). They map roughly but are not identical, and V3 is not an FDA requirement. Name which one you apply.

## 3. Endpoints and analysis (only as they touch operations)

- DHT endpoint definitions state assessment type, timing, tool and how repeated assessments combine. CV55
- A DHT replicating an existing measurement may not need a new endpoint justification but still needs V&V. CV57
- Same collection method in all arms; non-inferiority may be inappropriate if the comparator effect was not established with similar DHT measurements. CV58
- Late-phase trials use the E9(R1) estimand framework; plan to reduce and handle missing data. Missing data are defined relative to an estimand. CV59, CV41
- Endpoint choice itself is the study design skill's work.

## 4. Source, data flow and records

| Element | Rule | Row |
|---|---|---|
| Source data | For data collected from participants through DHTs, FDA treats the first durable electronic data repository as the source; it does not intend to inspect individual devices when data and metadata transfer securely. | CV60 |
| Data management plan | Includes data origin and flow from all sources to the sponsor, remote acquisition methods and data service providers. | CV68 |
| Data flow overview | All parties have an overview of the data flow (a diagram in the protocol is highly recommended); data acquisition tools are configured and validated for intended use; data and metadata both move (EU paper). | CV102 |
| Visit records | Visit type, location, date and data originator. | CV69 |
| Participant-entered endpoint data | Minimize the risk of erroneous entry on primary, key secondary or safety endpoints (EU paper). | CV103 |
| Audit trail and timestamps | Audit trails not disabled; interpretable; unambiguous timestamps (for example UTC). | CV14 |

## 5. Safety data from DHTs

- A safety monitoring plan in the protocol says how abnormal DHT measurements are reviewed and managed; FDA generally does not expect continuous monitoring by investigators. CV62
- Annex 2: DHT safety data reach the investigator in a relevant, meaningful and manageable way. CV26

## 6. Access and consent

- Bring your own device needs a sponsor-provided option. CV53
- Consent explains who may access DHT data, including under terms of service. CV61

## 7. Contingency

- A contingency plan covers malfunction of a digital tool for critical-to-quality elements (EU paper). Medical devices used follow MDR or IVDR (the paper says so; the MDR requirements themselves are not sourced here). CV99

## What the sources do not set

No accuracy threshold, agreement statistic, wear-time minimum, data completeness level or usability pass rate. These are the person's acceptance criteria. Published validation studies are evidence the person may rely on only after the passage is read in the same direction as the claim (register item N3).
