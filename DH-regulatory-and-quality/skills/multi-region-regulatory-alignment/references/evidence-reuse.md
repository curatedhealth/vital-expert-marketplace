# Evidence reuse across regions

Interpretive reference. `MR-`, `JX-` rows: `multi-region-sources.md`. `US-`, `EU-`, `UK-`, `IM-`, `CH-` rows: `pathways-submissions-sources.md`. Read on 19 October 2026. Never state the text of an ISO or IEC standard: those texts are paywalled and no row quotes them.

## 1. IMDRF documents and their reported adoption

IMDRF documents are harmonized principles, not regulations; each regulator decides whether and how to implement them (JX-04, JX-06). Adoption below is what members self-reported in IMDRF N84 Edition 2 (1 September 2025), read from the column positions of the layout PDF (JX-06 to JX-11, JX-14). Self-reporting is a claim by the regulator, not a finding; "partly implemented" means modified or narrower (JX-07).

| Document | What it gives | Implemented (as reported) | Partly | Not implemented | Rows |
|---|---|---|---|---|---|
| N12 SaMD risk categorization (2014) | Categories I to IV from seriousness and significance | Australia, Brazil, China, EU, Russia, Singapore, Switzerland, USA (Saudi Arabia as observer) | Canada, Japan, South Korea, UK (Argentina) | none listed | JX-01 to JX-03, JX-08 |
| N41 SaMD clinical evaluation (2017) | Valid clinical association, analytical validation, clinical validation | Australia, Brazil, China, EU, Singapore, Switzerland, USA (Saudi Arabia) | Canada, Japan, Russia, South Korea, UK | Argentina | JX-04, JX-05, JX-09 |
| N47 essential principles (Edition 2, 2024) | Safety and performance principles | Australia, Brazil, China, EU, Japan, Russia, South Korea, Singapore, Switzerland (Argentina) | Canada, UK, USA (Saudi Arabia) | none listed | JX-10 |
| N56 clinical evaluation (2019) | Device clinical evaluation | Australia, Brazil, China, EU, Russia, Singapore, Switzerland, USA | Canada, Japan, South Korea (Saudi Arabia) | UK (Argentina) | JX-14 |
| RPS N9 nIVD submission Table of Contents (Edition 4) | A shared dossier structure | Brazil, Canada, China, Singapore, USA | Russia, South Korea | Australia, EU, Japan, Switzerland, UK (Argentina) | JX-11 |

What this means in practice:

- **N41 travels.** The EU's MDCG 2020-1 builds MDSW clinical evidence on the same three components (valid clinical association, technical performance, clinical performance) and takes its definition of technical performance from N41 (EU-32, EU-33, IM-03). A clinical evaluation organized on N41 serves the EU and the regulators that report implementing N41, subject to each one's own rules.
- **The Table of Contents does not travel to Europe.** Health Canada has adopted the IMDRF ToC for new and amended Class II, III and IV license applications (guidance of 25 November 2025) (JX-12, JX-13). The EU, UK, Switzerland, Japan and Australia report not implementing it (JX-11). The EU file follows MDR Annex II and III (section 3 below).
- **N12 is shared vocabulary.** Use it to frame the classification argument, then classify under each region's own rules (`jurisdiction-requirements.md` section 1).
- IMDRF N81 (2025) on characterizing medical device software is cited by MDCG 2019-11 rev.1; whether it replaces parts of N12 was not checked `[GAP]` (IM-04).

## 2. Foreign clinical data

| Regulator | Rule | Conditions to plan for | Rows |
|---|---|---|---|
| US FDA (21 CFR 812.28) | Accepts data from a well-designed, well-conducted investigation outside the US for an IDE, 510(k), De Novo, PMA or HDE. | Good clinical practice, including independent ethics committee review before the study and informed consent; FDA able to validate the data, by inspection if needed; a statement that the studied device is identical to the subject device, or a description of differences; waivers can be requested; records kept 2 years after the decision. Data not meeting the conditions may still be accepted if FDA believes it credible and subjects were protected. | JX-15, JX-16, JX-17, JX-18, JX-19, JX-20 |
| EU MDR (Annex XIV Part A section 3) | Clinical evaluation may rely on data from a device shown to be equivalent. | Technical (including software algorithms), biological and clinical characteristics similar enough that there is no clinically significant difference in safety and performance; sufficient access to the equivalent device's data. Quoted from the MDR as originally published; later amendments were not compared line by line. | JX-21, JX-22, JX-23, JX-24 |
| EU MDR (Article 61, Annex XIV) | Clinical evidence must be sufficient; the manufacturer specifies and justifies its level and plans the evaluation (clinical evaluation plan with outcome parameters and a clinical development plan including PMCF). | Region-specific documents, see section 3. | EU-17, EU-18, EU-20 |
| Australia TGA | Clinical investigations outside Australia must follow the Declaration of Helsinki and should follow ICH GCP and ISO 14155:2020 (guidelines V3.1, June 2022). | Name the GCP basis of each study. | JX-25 |
| Health Canada | Device clinical investigations done in Canada or other countries are summarized; real-world data from other jurisdictions, including post-market studies, is expected. Sponsors state whether data are disaggregated by sex, gender, age, race and ethnicity, and justify if not. | Plan the disaggregation statement from the start. | JX-26, JX-27 |
| Great Britain, Switzerland, Brazil, Japan | Foreign clinical data rules were not read. | `[GAP]` | Not sourced |

## 3. One technical file, regional additions

There is no single dossier every regulator accepts. The reusable core is the content: device description, software verification and validation, risk management, clinical evaluation. The wrapper and some content are regional.

| Region | Format or structure | Regional additions to plan | Rows |
|---|---|---|---|
| US | eSTAR, mandatory for 510(k) (from 1 October 2023) and De Novo (from 1 October 2025); current eSTAR 7.1 includes the human factors content guidance effective 1 August 2026. Software documentation level Basic or Enhanced by the risk of the software functions in the context of intended use; Enhanced generally for class III. | Documentation level justification; 812.28 statements for foreign studies; predicate comparison for a 510(k). | US-25, US-26, US-27, US-28, US-29, US-36, US-37, US-39, JX-18 |
| EU | MDR Annex II sections (description and specification; information supplied; design and manufacturing; GSPRs; benefit-risk and risk management; verification and validation), including the class and the justification for the classification rules, and software V&V. Annex III post-market surveillance plan and PSUR or PMS report. | Clinical evaluation plan and report under Annex XIV; PMS plan; classification justification under Annex VIII. | EU-13, EU-14, EU-15, EU-16, EU-20 |
| Canada | IMDRF Table of Contents for Class II, III and IV applications. | Disaggregation statement; QMS certificate (MDSAP per the MDSAP site). | JX-12, JX-13, JX-27, MR-05 |
| Switzerland | Follows MDR classification; certificate from an EU notified body accepted if equivalence is credibly demonstrated. | Swiss product registration. | CH-01, MR-20, JX-42 |
| Great Britain | Under CE acceptance, the EU file; under UKCA, UK MDR 2002 with a UK approved body above class I. | GB classification under MDD-derived rules; MHRA registration. | UK-03, UK-14, UK-15, UK-01 |
| Australia | Comparable overseas regulator evidence plus Australian requirements. | Same-device statement; audit readiness; Australian requirements covered in any MDSAP audit used. | MR-10, MR-11, MR-36 |
| Brazil, Japan | Dossier structure not read. | `[GAP]` | Not sourced |

## 4. How to word a reuse claim

- Say "reusable, subject to [regulator]'s conditions", never "accepted". Acceptance is the regulator's decision.
- Name the condition that carries the risk: for 812.28, GCP and data validation; for EU equivalence, data access; for TGA, same device and audit.
- A self-reported IMDRF adoption is "reported as implemented in N84", never "required by".
