# Appraising a published review, real-world data and digital signals

Interpretive reference. ES rows are in `EVIDENCE_SYNTHESIS_METHODS.md`, CV rows in `CLINICAL_STUDY_AND_RWE.md`, read 19 October 2026. Ratings and fitness decisions are the appraisers'. The full RWD and digital endpoint appraisal method, with all questions, lives in the sibling skill `literature-and-real-world-evidence-review` (`references/rwe-and-digital-endpoints.md`); the core is restated here so this skill stands alone.

## 1. AMSTAR 2 (Shea et al. 2017) [PAPER] doi 10.1136/bmj.j4008

- 16 items; overall confidence rests on weaknesses in critical domains (ES-105 [PAPER] doi 10.1136/bmj.j4008).
- Default critical domains (ES-106): item 2 protocol registered before the review began; item 4 adequacy of the literature search; item 7 justification for excluding individual studies; item 9 risk of bias of included studies; item 11 appropriateness of meta-analytical methods; item 13 risk of bias considered when interpreting results; item 15 presence and likely impact of publication bias.
- The list is advisory: appraisers decide which items matter most for the reviews at hand (ES-109). Record the list used.
- Overall confidence (ES-107): High, at most one non-critical weakness; Moderate, more than one non-critical weakness; Low, one critical flaw with or without non-critical weaknesses; Critically low, more than one critical flaw, and the review should not be relied on.
- Never combine item ratings into a score (ES-108).
- Shea et al. 2017: "If no information is provided to rate an item, the review authors should not be given the benefit of doubt and the item should be rated as a “No.”" and "We have provided a “partial Yes” response in some instances" (raw epmc_PMC5833365, read 19 October 2026; quoted verbatim, not yet an ES row: add it as an ES row before relying on it as a rule; ES-105 [PAPER] doi 10.1136/bmj.j4008). Which items offer "Partial yes" is in the checklist, not the article text [GAP]: read the AMSTAR 2 checklist (BMJ supplementary or amstar.ca) before telling an appraiser a "Partial yes" is invalid on a given item. The wording of the other nine items was not quoted in the rows read [GAP]. `scripts/review_check.py amstar2` applies the overall rule to the appraisers' ratings and lists "Partial yes" items for the appraisers without counting them.

PRISMA 2020 is not an appraisal tool: a review that reports well can still be done badly (ES-04). Use PRISMA items only to find where in the paper the AMSTAR 2 evidence sits (for example item 6 for sources and dates, item 16b for excluded studies, item 24 for registration; ES-06, ES-13, ES-15).

### Where to look for each critical domain

| AMSTAR 2 item | Look for (PRISMA item, row) | Related sourced rule |
|---|---|---|
| 2 Protocol registered before | Item 24 registration and amendments (ES-15) | Cochrane recommends PROSPERO (ES-39) |
| 4 Search adequacy | Items 6 and 7 sources, dates, strategies (ES-06, ES-07); PRISMA-S (ES-25 [PAPER] doi 10.1186/s13643-020-01542-z to ES-31) | Two or more databases; registers; grey literature; reference lists (ES-45 to ES-48) |
| 7 Exclusions justified | Item 16b excluded studies with reasons (ES-13) | JCA exclusion list (ES-162) |
| 9 Risk of bias of included studies | Item 11 tool, reviewers, independence (ES-10) | RoB 2 or RoB 1 for RCTs, ROBINS-I for non-randomized (ES-69 to ES-77, ES-163, ES-164) |
| 11 Meta-analysis methods | Item 13d model, heterogeneity, software (ES-11) | When not to pool, I-squared bands (ES-83 to ES-88) |
| 13 Risk of bias in interpretation | Discussion and certainty (ES-12, ES-14) | GRADE per outcome (ES-89 to ES-99) |
| 15 Publication bias | Item 14 reporting-bias methods (ES-12) | GRADE publication bias domain (ES-91) |

## 2. Real-world data quality: name the framework

| Framework | Reliability | Relevance | Rows |
|---|---|---|---|
| FDA EHR and claims, drugs and biologics (July 2024) | Accuracy, completeness, traceability | Key variables available; enough representative patients | CV78, CV79 |
| FDA CDRH device RWE, final 18 December 2025 | Accrual, quality, integrity | Availability, timeliness, generalizability | CV88, CV91, CV92 |
| ICH E6(R3) Annex 2 (EU effective 15 January 2027) | Accuracy, completeness, provenance, traceability | Key data elements available | CV2, CV23 |

Core checks, each tied to its row: a relevance and reliability assessment with limitations (CV90); conceptual and operational definitions with validation metrics (CV80, CV81); traceability (CV82); continuity of coverage and care for claims (CV83); protocol and analysis plan fixed before outcomes were seen (CV75, CV94); prespecified linkage (CV24); registry consent (CV85); catalogue registration in the EU, with data-source entries updated if older than 12 months (CV108).

## 3. Digital signal validity: name the framework

| Framework | Steps | Rows |
|---|---|---|
| FDA DHT guidance (final December 2023) | Verification of the measured parameter; validation that the DHT assesses the clinical event or characteristic in the population; required whether or not the DHT is a device | CV42, CV46, CV47 |
| V3 [PAPER] doi 10.1038/s41746-020-0260-4, not FDA policy | Verification, analytical validation, clinical validation | CV155 [PAPER] doi 10.1038/s41746-020-0260-4, CV157 [PAPER] doi 10.1038/s41746-020-0260-4 to CV159 [PAPER] doi 10.1038/s41746-020-0260-4 |

Core checks: validation in the population actually studied, since algorithms valid in healthy people may fail in patients (CV48); the types of V&V evidence (CV49); precise endpoint definition (CV55); meaningfulness of a novel endpoint (CV56); same collection method in all arms (CV58); usability in the trial population (CV51). The sources set no accuracy threshold for a digital measure (research file scope note): any threshold is the person's and is written as theirs.

Adverse-event signals from a marketed device (MAUDE, field safety notices, MHRA alerts) are not this skill's; they belong to dh-regulatory-strategy.
