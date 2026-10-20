# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced, binding | A law row states it (AI Act, GDPR, 45 CFR 92.210, 45 CFR 170.315) | The fact, the source name and date in plain words, the row id after it, and the date the duty applies ("AI Act Article 14(4)(d) as amended by Regulation (EU) 2026/1744, applies to MDR devices from 2 August 2028 (DA-61, AI EU-19)") | Whether it binds the person is for the owner they name for legal matters, or owner not named |
| Sourced, voluntary | NIST AI RMF, NIST AI 600-1, WHO guidance, GMLP and transparency principles | "NIST AI RMF 1.0, January 2023, voluntary (DA-14)" | Never "required" |
| Draft or proposed | FDA AI-enabled device software functions draft (DA-35 to DA-46, AI US-19 to AI US-22, AI US-37, AI US-38); HTI-5 (UX-US-60, UX-US-61) | "The FDA draft of 7 January 2025, not for implementation, recommends ..."; "HTI-5 proposes ... (proposed only)" | Never a requirement; the current rule stays in force until a final rule says otherwise |
| Not binding | MDCG 2025-6 (AI EU-25 to AI EU-32) | "MDCG 2025-6, June 2025, not legally binding (AI EU-25)" | Its dates are superseded where AI EU-19 moved them |
| Summarized read | [WF] rows (DA-22, DA-23, DA-93, AI IM-02 to AI IM-04) | "(ISO/IEC 42001 public page, read 20 October 2026, DA-22 [WF])" | Say the quote is close but not script-checked; never give clause text |
| Published method | [PAPER] rows | The row id and the DOI at first use in prose; the DOI in the Rows cell of a table | The paper's own limits |
| Blog, not the standard | CP-UK-11 | "an AI and Digital Regulations Service blog states ... (CP-UK-11); confirm against the DCB0129 specification" | The specification text was not read |
| Not in the sources | Fairness tolerances, drift thresholds, AUROC targets, acceptable subgroup gaps (research file "Not sourced"); ISO/IEC 42001 and 23894 clause content; WHO full recommendation lists; NIST AI 600-1 standing after the revocation of EO 14110; US state AI laws; GDPR Article 22; the start date of AI Act Article 4a | "Not in this skill's sources `[GAP]`" | The person supplies it, or it stays a gap |

## The person's facts

| Situation | How to word it |
|---|---|
| Decision threshold, reference group, fairness criterion or allowed difference not given | "Not given"; ask. The script prints values without pass or fail |
| Dataset or model version not given | "Not given"; a test without both versions cannot be tied to a release |
| A group the person names that the data cannot show | "[GAP]: not visible in this data; not tested". Never report it as tested; never fold it into "other" |
| Rows without a group value | "group not recorded (n)"; reported as their own line, never dropped |
| Small group | Report the count and the 95% interval the script prints; never call it "too small" against a number the person did not set |
| Owner, acceptor, review date, monitoring cadence not given | "Owner not named" or "not given"; ask |
| A press or vendor claim ("our vendor says the model is unbiased") | "From you (vendor claim, not checked against the test data or a primary record)" |
| A date, data cut, threshold or status not given | "Not given"; ask. Never fill, and never use today's date as the data cut |

## Library facts

| Situation | How to word it |
|---|---|
| A safety search returns rows not about the named product or comparable devices | Exclude them and count them: "returned, not about these devices" |
| MAUDE counts | "reports, not confirmed events", per product code; never attributed to one manufacturer |
| A record field the library lacks | "not stored"; never 0 or none |
| A tool with no saved output | "needs a live check" |

## Never

- Never supply a fairness, drift or performance threshold, an allowed difference or a reference group.
- Never call a model fair, unbiased, safe, compliant or ready for release.
- Never present a draft or proposal as a requirement.
- Never average groups into one number and stop.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words with the row id after it; never a row id alone. A [WF] row adds "[WF]"; a [PAPER] row adds its DOI at first use (and in every table Rows cell). Where the row gives no publication date, use the date it was read.

| Rows | Cite as |
|---|---|
| DA-01 to DA-16 | NIST AI Risk Management Framework 1.0 (NIST AI 100-1), January 2023 |
| DA-17 to DA-21 | NIST AI 600-1 Generative AI Profile, July 2024 |
| DA-22 | ISO/IEC 42001:2023 public page, read 20 October 2026 [WF] |
| DA-23 | ISO/IEC 23894:2023 public page, read 20 October 2026 [WF] |
| DA-24 to DA-29 | WHO Ethics and governance of AI for health, 28 June 2021 (publication page and news release) |
| DA-30 to DA-34 | WHO guidance on large multi-modal models, 18 January 2024 (page dated 25 March 2025) |
| DA-35 to DA-46 | FDA draft guidance, AI-enabled device software functions, 7 January 2025 (draft) |
| DA-47 to DA-50, DA-54 to DA-63, DA-65 | EU AI Act, Regulation (EU) 2024/1689 |
| DA-51 to DA-53, DA-64, DA-66, DA-67 | Regulation (EU) 2026/1744 (Digital Omnibus), 8 July 2026 |
| DA-68 to DA-75 | EMA reflection paper on AI in the medicinal product lifecycle, adopted 9 September 2024 |
| DA-76 to DA-79 | PROBAST+AI, Moons et al., BMJ 2025, DOI 10.1136/bmj-2024-082505 |
| DA-80 to DA-84 | DECIDE-AI, Vasey et al., BMJ 2022, DOI 10.1136/bmj-2022-070904 |
| DA-85, DA-86 | CLAIM 2024 update, Tejani et al., Radiol Artif Intell 2024, DOI 10.1148/ryai.240300 |
| DA-87 to DA-90 | Sahiner et al., Br J Radiol 2023, DOI 10.1259/bjr.20220878 |
| DA-91, DA-92 | Davis et al., JAMIA 2017, DOI 10.1093/jamia/ocx030 |
| DA-93 | Finlayson et al., NEJM 2021, DOI 10.1056/NEJMc2104626 [WF] |
| DA-113 to DA-115 | Rajkomar et al., Ann Intern Med 2018, DOI 10.7326/M18-1990 |
| DA-116 to DA-120 | Paulus and Kent, npj Digit Med 2020, DOI 10.1038/s41746-020-0304-9 |
| AI US-19 to AI US-22, AI US-37, AI US-38 | FDA draft AI lifecycle guidance, 7 January 2025, and FDA guidance lists (content current 9 April 2026; FY 2027 A-list, 1 October 2026) |
| AI US-29, AI IM-01 | FDA GMLP page (IMDRF final document, January 2025) |
| AI US-32, AI US-33 | FDA, Health Canada and MHRA transparency principles, June 2024 |
| AI US-39 | FDA request for comment on real-world performance, docket FDA-2025-N-4203 (not guidance) |
| AI EU-01 to AI EU-16, AI EU-33, AI EU-34 | EU AI Act, Regulation (EU) 2024/1689 |
| AI EU-17 to AI EU-24, AI EU-35 | Regulation (EU) 2026/1744, 8 July 2026 |
| AI EU-25 to AI EU-32, AI EU-36 | MDCG 2025-6 / AIB 2025-1 FAQ, June 2025 (not legally binding) |
| AI UK-09, AI UK-10 | FDA, Health Canada and MHRA GMLP principles, 27 October 2021 |
| PE-113 to PE-115 | 45 CFR 92.210 and part 92 definitions (eCFR, read 19 October 2026) |
| UX-US-54 to UX-US-59 | 45 CFR 170.315(b)(11), ONC HTI-1 (eCFR, read 19 October 2026) |
| UX-US-60, UX-US-61 | ONC HTI-5 proposed rule, 29 December 2025, 90 FR 60970 (proposed only) |
| UX-US-64 to UX-US-73 | FDA Clinical Decision Support Software guidance, 29 January 2026 |
| EN-108 to EN-113 | GDPR, Regulation (EU) 2016/679 |
| CP-UK-01 to CP-UK-04 | NHS England DTAC guidance (AI and Digital Regulations Service, read 19 October 2026; DTAC refresh news, 4 March 2026) |
| CP-UK-05 | Health and Social Care Act 2012, section 250 |
| CP-UK-06 to CP-UK-10 | NHS AI and Digital Regulations Service pages on DCB0129 and DCB0160, read 19 October 2026 |
| CP-UK-11 | AI and Digital Regulations Service blog, read 19 October 2026 (not the standard) |
| CV124 to CV128 | TRIPOD+AI, Collins et al., BMJ 2024, DOI 10.1136/bmj-2023-078378 |
| Library facts | "library, retrieved 19 October 2026" plus the call and record (for example "FDA recall search for Aidoc, library, retrieved 19 October 2026") |
