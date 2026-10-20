# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DA, US, EU, UK, IM, CV or TM row states it | The fact, the source name and date in plain words, then the row id ("Test data should generally come from sites different from those used to develop the model (FDA AI-enabled device software functions draft guidance, January 2025, DA-41)") | None |
| Draft or proposal | FDA AI-enabled device software functions draft (January 2025, still draft on 19 October 2026); IMDRF N93 draft; FDA request for comment FDA-2025-N-4203 | "The January 2025 draft recommends ... (draft, not for implementation; DA-35, US-21)" | Never "FDA requires"; plan on the final text when it is issued |
| Voluntary framework | NIST AI RMF, NIST AI 600-1, GMLP, transparency principles | "NIST AI RMF 1.0, January 2023, voluntary (DA-02)" | A checklist, never a duty |
| Law with a moved date | EU AI Act Articles 10 to 15 and 72 | "Applies from 2 August 2028 for AI in Annex I devices, as amended by Regulation (EU) 2026/1744 (DA-67, EU-19)" | State the act that set the date |
| Written for another product type | EMA reflection paper (medicines) used for a device | "EMA reflection paper, final 9 September 2024, written for medicinal products (DA-68); used here as context" | Say so each time |
| Summarized read | The row is [WF] (ISO abstracts DA-22, DA-23; Finlayson DA-93; IMDRF IM-02 to IM-04) | "ISO/IEC 42001 abstract page [WF] (DA-22)" | Name only; no clause content |
| Published method | The row is [PAPER] | The row id and its DOI at first use; in a table, the DOI in the Rows cell | State the paper's own population and method |
| Not in the sources | An AUROC, sensitivity, calibration, drift or fairness threshold; a minimum test-set size; an acceptable missing-data share; a dose or engagement target; RL or bandit design rules; CLAIM 2024 item text; ISO 42001 clause text | "Not in this skill's sources `[GAP]`" | The person, or the owner they name, supplies it; never fill it |

## Library facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "K261317: 510(k) Substantially Equivalent, 14 May 2026, product code QAS (library, retrieved 19 October 2026)" |
| A record lacks a field (AI use, PCCP, validation data, intended use) | "Listed; the record does not state FIELD `[GAP]`"; never infer it |
| No record found | "No record in the loaded sources `[GAP]`; a missing record is a coverage limit, not evidence that none exists" |
| A tool with no saved output | "needs a live check" |

## The person's facts

| Situation | How to word it |
|---|---|
| No intended use, or "clinical decision support" with no decision named | "Intended use not given" or "decision not named `[GAP]`"; the model is not validated against it |
| No acceptance criterion, operating threshold or fairness criterion | "Not given"; values are reported, nothing is marked met or not met |
| Criteria labeled proposed | "Not applied: proposed criteria are never used to mark a result" |
| A population in the intended use absent from the test set | "POPULATION: not validated `[GAP]`" |
| A date, data cut, threshold, version or status not given | "Not given"; ask. Never fill |
| A vendor or press performance figure the person brings | "From you (vendor or press claim, not checked against a primary record)" |

## Never

- Never supply a threshold, acceptance criterion, fairness tolerance, test-set size or engagement target.
- Never present a draft guidance or proposed rule as a requirement.
- Never call a model "validated", "safe", "fair" or "ready"; report what was measured against the person's criteria.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "FDA AI-enabled device software functions draft guidance, January 2025 (DA-39)". Never a row id alone. A [WF] row adds "[WF]"; a [PAPER] row adds its DOI at first use.

| Rows | Cite as |
|---|---|
| DA-01 to DA-16 | NIST AI 100-1, AI Risk Management Framework 1.0, January 2023 (voluntary) |
| DA-17 to DA-21 | NIST AI 600-1, Generative AI Profile, July 2024 (voluntary) |
| DA-22, DA-23 | ISO abstract pages, read 20 October 2026 [WF] |
| DA-24 to DA-29 | WHO, Ethics and governance of AI for health, 28 June 2021 (publication page and news release) |
| DA-30 to DA-34 | WHO, Guidance on large multi-modal models (news release 18 January 2024; page dated 25 March 2025) |
| DA-35 to DA-46 | FDA, AI-Enabled Device Software Functions draft guidance, January 2025 (draft) |
| DA-47 to DA-50, DA-54 to DA-63, DA-65 | Regulation (EU) 2024/1689 (AI Act) |
| DA-51 to DA-53, DA-64, DA-66, DA-67 | Regulation (EU) 2026/1744 (Digital Omnibus on AI), 8 July 2026 |
| DA-68 to DA-75 | EMA reflection paper on AI in the medicinal product lifecycle, final, 9 September 2024 |
| DA-76 to DA-79 | PROBAST+AI, Moons et al. 2025, DOI 10.1136/bmj-2024-082505 |
| DA-80 to DA-84 | DECIDE-AI, Vasey et al. 2022, DOI 10.1136/bmj-2022-070904 |
| DA-85, DA-86 | CLAIM 2024, Tejani et al. 2024, DOI 10.1148/ryai.240300 |
| DA-87 to DA-90 | Sahiner et al. 2023, DOI 10.1259/bjr.20220878 |
| DA-91, DA-92 | Davis et al. 2017, DOI 10.1093/jamia/ocx030 |
| DA-93 | Finlayson et al. 2021, DOI 10.1056/NEJMc2104626 [WF] |
| DA-113 to DA-115 | Rajkomar et al. 2018, DOI 10.7326/M18-1990 |
| DA-116 to DA-120 | Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9 |
| US-01 to US-14, US-36 | FDA PCCP final guidance, 18 August 2025 |
| US-19 to US-22, US-37, US-38 | FDA AI lifecycle draft guidance, 7 January 2025 (draft); CDRH FY 2027 A-list |
| US-29, UK-09, UK-10, IM-01 | GMLP guiding principles (FDA, Health Canada, MHRA 2021; IMDRF final January 2025) |
| US-30, US-31 | PCCP guiding principles, October 2023 |
| US-32, US-33 | Transparency guiding principles, June 2024 |
| US-39 | FDA request for comment FDA-2025-N-4203 (not guidance) |
| EU-05, EU-17 to EU-19 | Regulation (EU) 2024/1689 Article 43(4); Regulation (EU) 2026/1744 |
| IM-04 | IMDRF N93 draft, 7 April 2026 [WF] |
| CV118 to CV121 | CONSORT-AI, Liu et al. 2020, DOI 10.1136/bmj.m3164 |
| CV122 | SPIRIT-AI, Rivera et al. 2020, DOI 10.1136/bmj.m3210 |
| CV124 to CV128 | TRIPOD+AI, Collins et al. 2024, DOI 10.1136/bmj-2023-078378 |
| TM30 | TIDieR checklist (EQUATOR Network file) |
| TM38 | TIDieR-PHP, Campbell et al. 2018, DOI 10.1136/bmj.k1079 |
| TM66 to TM73, TM76 | MOST, Collins, Kugler and Gwadz 2016, DOI 10.1007/s10461-015-1145-4 |
| TM74, TM75 | Guastaferro and Collins 2021, DOI 10.1177/26334895211054363 |
| TM77 to TM90 | Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8 |
| TM141 to TM143 | FDA De Novo decision summary DEN200026 (EndeavorRx) |
| Library facts | "library, retrieved 19 October 2026" plus the record number |
