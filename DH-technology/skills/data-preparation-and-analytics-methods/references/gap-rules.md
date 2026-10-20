# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DA, CV, TM or PE row states it | The fact, the source name and date in plain words, then the row id ("Test data generally come from sites different from those used for development, as the FDA AI-enabled device software functions draft guidance of January 2025 proposes (DA-41, draft)") | None |
| Draft | FDA AI-enabled device software functions draft (DA-35 to DA-46); FDA Bayesian drug draft (DA-129 to DA-131) | "the draft proposes", plus "(draft)" after the row | Never "FDA requires" |
| Future application date | EU AI Act Articles 10 to 15 (DA-47 to DA-63) | State the application date as amended (2 December 2027 Annex III; 2 August 2028 Annex I; DA-67) | Never "applies now" |
| Other market used as context | EMA reflection paper for a device; FDA drug guidance for a device or an analytics model; CMS measure rules outside quality measures | "(EMA, medicinal products; context for your device)" | Say whose rule it is |
| Published method | [PAPER] row | The row id and the DOI of that row's own paper | State the paper's own limits where the row gives them |
| Community standard | [SPEC] rows DA-102 to DA-106 (OHDSI) | "OHDSI community standard" | Never "regulation" |
| Summarized read | [WF] rows DA-22, DA-23, DA-93 | "(ISO/IEC 42001 public page, DA-22 [WF])" | Say the quote is close but not script-checked; no clause text from ISO standards |
| Old method step | A rule taken from an old task (cohort, feature, handoff, causal, regression, Bayesian, prediction, recommendation, forecast tasks) | "(old task DH-05.01.2.3.1, method)" | Never presented as a regulator's rule |
| Not in the sources | Any threshold (missingness, sample size, AUROC, calibration, fairness tolerance, posterior probability for success, forecast accuracy, alpha), causal method assumptions, forecasting methods, ISO clause text, CLAIM item list, OMOP v5.5 field rules | "Not in this skill's sources `[GAP]`" | The person supplies it or it stays a gap |

## Library facts

| Situation | How to word it |
|---|---|
| A library design label | "library label, checked against the paper: ..." (register N8) |
| A check_claim status | The tool status beside your own reading of the passage (register N3) |
| A field the saved record lacks | "not stored"; never 0 or none |
| A tool with no saved output for this use | "needs a live check" |

## The person's facts

| Situation | How to word it (script flag) |
|---|---|
| Cohort step without a rule or count | "rule not given" (C2), "count not given" (C3); a rising count is a fact (C1) |
| Feature missing a source field, window or missing code | "not given" (F1, F2, F4) |
| Feature known after the index time, unavailable at decision time or derived from the outcome | "candidate to refuse; your decision" (F3, F5, F7) |
| Input measuring a 45 CFR 92.210 characteristic | "identify and mitigate duty for a covered entity (PE-113); for your legal owner" (F6) |
| Patient or site in development and test | Stated as a fact (S1, S2) |
| Rows that are not held out | Left out of every figure (H1) |
| Threshold not given | "threshold not given"; no sensitivity, specificity, PPV or NPV (H2) |
| A group with only one outcome class in held-out rows | AUROC not computable, stated as a fact (H3); event counts are shown for every group and their sufficiency is the person's call |
| Outcome rates differ between groups | DA-119 stated; criterion choice is the person's (H4) |
| No holdout periods, interval missing, forecast not beating the naive baseline | FC1, FC2, FC3 as facts |
| A date, data cut, threshold, prior or status not given | "Not given"; ask. Never fill |

## Never

- Never supply or endorse a threshold, a prior or a target.
- Never call a dataset fit, compliant or valid, or a model ready.
- Never call an association an effect when the design cannot support it.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. Every fact names its source and date in plain words, with the row id after it; never a row id alone. A [WF] row adds "[WF]"; a [PAPER] row adds its own DOI at first use; a draft row adds "draft".

| Rows | Cite as |
|---|---|
| DA-01 to DA-16 | NIST AI 100-1, AI Risk Management Framework 1.0, January 2023 (voluntary) |
| DA-17 to DA-21 | NIST AI 600-1, Generative AI Profile, July 2024 |
| DA-22, DA-23 | ISO/IEC 42001 (18 December 2023) and ISO/IEC 23894 (6 February 2023) public pages [WF] |
| DA-24 to DA-29 | WHO, Ethics and governance of AI for health, 28 June 2021 (publication page and news release) |
| DA-30 to DA-34 | WHO guidance on large multi-modal models, 18 January 2024 (page dated 25 March 2025) |
| DA-35 to DA-46 | FDA AI-enabled device software functions draft guidance, January 2025 (draft, not for implementation) |
| DA-47 to DA-50, DA-54 to DA-63, DA-65 | EU AI Act, Regulation (EU) 2024/1689, Articles 10, 12 to 15 and 72 |
| DA-51 to DA-53, DA-64, DA-66, DA-67 | Digital Omnibus, Regulation (EU) 2026/1744 |
| DA-68 to DA-75 | EMA reflection paper on AI in the medicinal product lifecycle, adopted 9 September 2024 |
| DA-76 to DA-79 | PROBAST+AI, Moons et al., BMJ 2025, DOI 10.1136/bmj-2024-082505 |
| DA-80 to DA-84 | DECIDE-AI, Vasey et al., BMJ 2022, DOI 10.1136/bmj-2022-070904 |
| DA-85, DA-86 | CLAIM 2024 update, Tejani et al., Radiol Artif Intell 2024, DOI 10.1148/ryai.240300 |
| DA-87 to DA-90 | Sahiner et al., Br J Radiol 2023, DOI 10.1259/bjr.20220878 |
| DA-91, DA-92 | Davis et al., JAMIA 2017, DOI 10.1093/jamia/ocx030 |
| DA-93 | Finlayson et al., NEJM 2021, DOI 10.1056/NEJMc2104626 [WF] |
| DA-94 to DA-98 | Kahn et al., eGEMs 2016, DOI 10.13063/2327-9214.1244 |
| DA-99 to DA-101 | FAIR principles, Wilkinson et al., Sci Data 2016, DOI 10.1038/sdata.2016.18 |
| DA-102 to DA-106 | OHDSI OMOP CDM documentation, read 20 October 2026 (community standard) |
| DA-107 to DA-112 | ONC USCDI page and 45 CFR 170.213 (eCFR), read 20 October 2026 |
| DA-113 to DA-115 | Rajkomar et al., Ann Intern Med 2018, DOI 10.7326/M18-1990 |
| DA-116 to DA-120 | Paulus and Kent, npj Digit Med 2020, DOI 10.1038/s41746-020-0304-9 |
| DA-121 to DA-125 | FDA covariate adjustment guidance (drugs and biologics), May 2023 |
| DA-126 to DA-128 | FDA Bayesian statistics in medical device clinical trials, 5 February 2010 |
| DA-129 to DA-131 | FDA Bayesian methodology draft (drugs and biologics), January 2026 (draft) |
| DA-132 to DA-140 | CMS Measures Management System Hub, read 20 October 2026 |
| CV31 to CV41 | ICH E9(R1) estimands addendum, adopted 20 November 2019 |
| CV73 to CV77 | FDA RWE considerations guidance (drugs and biologics), August 2023 |
| CV78 to CV83 | FDA RWD guidance on EHR and medical claims data (drugs and biologics), July 2024 |
| CV84, CV85 | FDA registries guidance, December 2023 |
| CV86, CV87 | FDA RWD data standards guidance, December 2023 |
| CV88, CV89 | FDA CDRH RWE device guidance, 18 December 2025 |
| CV109 | EMA DARWIN EU page, read 19 October 2026 |
| CV124 to CV128 | TRIPOD+AI, Collins et al., BMJ 2024, DOI 10.1136/bmj-2023-078378 |
| TM30 | TIDieR checklist, EQUATOR Network file, read 20 October 2026 |
| TM66 to TM69 | MOST, Collins, Kugler and Gwadz 2016, DOI 10.1007/s10461-015-1145-4 |
| TM74, TM75 | Guastaferro and Collins 2021, DOI 10.1177/26334895211054363 |
| TM77 to TM90 | Nahum-Shani et al., Ann Behav Med 2018, DOI 10.1007/s12160-016-9830-8 |
| PE-113 to PE-115 | 45 CFR 92.210 (eCFR, read 19 October 2026) |
| Library facts | "library, retrieved 19 October 2026" plus the record identifier |
