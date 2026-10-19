# What each body asks of the evidence

Interpretive reference for A1 and B1. Every line cites a row in `hta-submissions-sources.md` (ids such as `DE10`) or a topic row in `requirements/<file>.md` (cited as file and topic). All rows were read on 19 October 2026 and are not yet owner-reviewed. Re-read the source before external use. Where a body's rule is not here, it is `[GAP]`.

## Germany: DiGA (BfArM, DiGAV as amended 27 January 2026)

**Version.** The DiGAV in force was last amended by the ordinance of 27 January 2026, in force 1 February 2026 (`DE1`). The BfArM guide is version 3.6 of 10 December 2025, older than that amendment (`DE2`; conflict note 5). Where the guide and the ordinance differ, cite the ordinance as the law and the guide as practice.

**Two effect types, and one is chosen per claim.**

| Effect type | What counts | Row |
|---|---|---|
| Medical benefit (medizinischer Nutzen) | Patient-relevant effect on health status, disease duration, survival or quality of life | `DE6` |
| Patient-relevant structure and process improvement (pSVV) | Nine named areas: care coordination, guideline alignment, adherence, access, patient safety, health literacy, patient autonomy, coping with daily life, reduced treatment burden | `DE7` |
| Not admissible for either | Staff workload and economic indicators | `DE8` |

Class IIb DiGA must show medical benefit; pSVV alone is not enough (`requirements/germany-diga.md`, "Evidence: higher risk").

**The study rules (DiGAV §§ 10 to 12), as checks.** `scripts/diga_study_rules.py` applies these mechanically to a study record.

| # | Rule | Row |
|---|---|---|
| G1 | A quantitative comparative study showing use beats non-use. Retrospective comparative studies, including intra-individual comparison, qualify; prospective studies are allowed. | `DE10` |
| G2 | Comparator is no treatment or treatment without a DiGA, reflecting real care; a permanently listed comparable DiGA may also serve. | `DE11` |
| G3 | Run in Germany, or transferability to German care shown. BfArM looks at comparable guidelines, comparable access and reimbursement, and validated questionnaire language versions. | `DE12`, `DE13` |
| G4 | Registered in a WHO ICTRP primary or partner registry; fully published online within 12 months of completion, to international reporting standards. | `DE14` |
| G5 | Since the 2026 amendment, studies collect accompanying data on duration and frequency of use. | `DE15` |
| G6 | Prospective comparative study required where no suitable retrospective data exist, and for medical benefit in higher-risk-class DiGA; a diagnostic component also needs a sensitivity and specificity study. | `DE16` |
| G7 | Patient group stated as ICD-10-GM codes, normally three digits; the listing applies only to those indications. | `DE9` |
| G8 | BfArM weighs positive and negative effects, indication, risk and alternatives, and may depart from the study rules where they are unsuitable. This is BfArM's discretion, never a plan. | `DE17` |

**Trial (provisional) listing.** Only low-risk-class DiGA qualify; up to 12 months (`DE19`). The application needs at least the results of a systematic data analysis of the DiGA's use (`DE18`) and an evaluation concept written by a manufacturer-independent institution to recognized scientific standards (`DE19`). BfArM's guide says the study protocol should be part of the concept, with a statistical analysis plan covering randomization, sample size, blinding, endpoints, primary analysis, multiplicity, missing data and dated pre-specification (`DE20`). A second trial listing is not allowed (`DE23`).

**What the application must say about the evidence.** Among 24 items: a plain-language PICO-style summary of the evidence, patient groups, the positive care effects split into the two types, the studies or systematic data analyses, diagnostic-accuracy studies, and the independent evaluating institution (`DE3`).

## France: CNEDiMTS (LPPR brand name, PECAN, LATM)

**Which route.** HAS names two main routes for digital medical devices: LPPR for therapeutic devices used by patients, LATM for telemonitoring (`FR1`). PECAN is one year of non-renewable early coverage pending LPPR or LATM (`FR12`). A device that is both therapeutic and telemonitoring needs two dossiers (`FR8`).

| Route | Evidence question | Scale or test | Rows |
|---|---|---|---|
| LPPR brand name | Expected benefit (SA), then, if sufficient, improvement in expected benefit (ASA) | SA is binary; ASA I major, II important, III moderate, IV minor, V none | `FR3`, `FR4`; `requirements/france-pecan-lppr-latm.md` "LPPR evidence: SA criteria", "ASA scale" |
| LPPR design | A double-blind RCT is the best evidence; other designs must be justified. No usable comparative study generally means no ASA. Comparator comes from the reference strategy and must be justified. | | `FR4`; requirements file "LPPR evidence: comparator", "comparative data" |
| LPPR digital points | For connected devices HAS expects the applicant to address algorithms that update | | requirements file "LPPR evidence: digital specifics" |
| PECAN | Two CNEDiMTS criteria: CE marking in the claimed indication, and presumed innovation (clinical benefit or care-organization progress) from first data, against relevant comparators, backed by ongoing studies expected to support the later LPPR or LATM opinion. ANS checks data protection, interoperability, security separately. | | `FR13` |
| LATM | Expected interest on clinical improvement, significant organizational gain, public-health interest; must beat conventional follow-up or equal or beat an already listed telemonitoring activity | | `FR17` |

**Organizational claims are the weak point.** CNEDiMTS reports that since the digital desk opened in 2023, companies struggle to evidence organizational impact, which most do not evaluate despite claiming it (`FR25`). An organizational claim without a measured organizational endpoint is "not shown".

## England: NICE HealthTech program (PMG48) and the Evidence Standards Framework

**No company submission.** For guidance started after 14 July 2025, companies do not file an evidence submission. NICE sends requests for information (mainly at scoping) and evidence requests (after the scope publishes) (`UK1`, `UK2`; conflict note 1). The task here is to be ready to answer those requests, not to write a dossier. Not answering does not drop the technology, but missing information may affect the recommendation (`UK4`).

**Economic models.** May accompany an evidence response but must be fully executable in standard software (Excel, DATA or TreeAge, R, WinBUGS) with full code access; a confidential-information checklist goes with every response (`UK3`).

**Guidance types.** Early use (conditional, fixed evidence period), routine use, existing use (`UK6`). For early use NICE tests whether key uncertainties can be resolved within a fixed 3-year period from publication (`UK7`). "Early value assessment" is legacy wording (conflict note 2).

**The ESF as the evidence yardstick.** The Evidence Standards Framework (ECD7, last updated 9 August 2022) classifies by intended purpose into tiers A, B and C; most regulated medical devices are tier C (`UK12`). 21 standards in 5 groups (`UK13`). A tier C technology that treats a condition needs one or more high-quality interventional studies in a UK-relevant setting (`requirements/uk-nice-nhs.md`, "ESF: tier C treat"). All tiers need real-world evidence that claimed benefits can be achieved in practice (same file, "ESF: all tiers").

**DTAC is not a NICE prerequisite.** The ESF says NHS use "may" need DTAC; PMG48 does not mention it (`UK14`; conflict note 3). DTAC is a commissioner and provider assurance tool (`UK15`, read through a summarizer: re-check before reuse).

## United States: only what is sourced

| Item | What it requires | Row |
|---|---|---|
| Medicare NCD request | A final letter titled "A Formal Request for a National Coverage Determination", with item description, target Medicare population, indications, supporting scientific evidence, FDA summaries or 510(k) predicates, FDA labeling and status, and the Part A or B benefit category | `US1` |
| TCET | FDA Breakthrough Devices in an existing Medicare benefit category; CMS cannot create benefit categories, so some digital devices cannot be covered | `US4` |
| Digital mental health codes | G0552 to G0554 pay only for devices cleared under 510(k) or De Novo and classified under 21 CFR 882.5801 (later fee schedule changes not checked) | `US7` |
| RAPID | Proposed only (notice of 11 August 2026; comments closed 13 October 2026); status after comments not checked | `US6` |

Commercial payer and PBM requirements, and the AMCP format, are `[GAP]`: not public in primary form, or not an official source (research file, "Not sourced").

## Reading a study against these rules

The literature tools give the design (`classify_study`), a CEBM level from that design (`grade_evidence`) and identifiers. They do not give country of conduct, comparator, registration, endpoints or effect size. Those come from the paper the person supplies. A rule the record cannot answer is `[GAP]` until the person shows the paper section, never "met".
