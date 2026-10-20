# Appraising a published review, real-world data and digital signals

Interpretive reference. ES rows are in `EVIDENCE_SYNTHESIS_METHODS.md`, CV rows in `CLINICAL_STUDY_AND_RWE.md`, read 19 October 2026; section 15 ES rows (ES-171 to ES-234) read 20 October 2026. Ratings and fitness decisions are the appraisers'. The full RWD and digital endpoint appraisal method, with all questions, lives in the sibling skill `literature-and-real-world-evidence-review` (`references/rwe-and-digital-endpoints.md`); the core is restated here so this skill stands alone.

## 1. AMSTAR 2 (Shea et al. 2017) [PAPER] doi 10.1136/bmj.j4008

- 16 items; overall confidence rests on weaknesses in critical domains (ES-105 [PAPER] doi 10.1136/bmj.j4008).
- Default critical domains (ES-106): item 2 protocol registered before the review began; item 4 adequacy of the literature search; item 7 justification for excluding individual studies; item 9 risk of bias of included studies; item 11 appropriateness of meta-analytical methods; item 13 risk of bias considered when interpreting results; item 15 presence and likely impact of publication bias.
- The list is advisory: appraisers decide which items matter most for the reviews at hand (ES-109). Record the list used.
- Overall confidence (ES-107; Box 2 wording ES-226, ES-227): High, no or one non-critical weakness, "an accurate and comprehensive summary"; Moderate, more than one non-critical weakness but no critical flaw; Low, one critical flaw with or without non-critical weaknesses, "may not provide an accurate and comprehensive summary"; Critically low, more than one critical flaw, "should not be relied on". Multiple non-critical weaknesses may justify moving Moderate down to Low; that is the appraisers' call (ES-227).
- Never combine item ratings into a score (ES-108).
- Missing information is rated No, never given the benefit of the doubt; "Partial yes" marks partial adherence (ES-208).
- Response options, from the AMSTAR 2 checklist (ES-209): "Partial yes" only on items 2, 4, 7, 8, 9; "No meta-analysis conducted" only on items 11, 12, 15; item 9 also "Includes only NRSI" or "Includes only RCTs" for one of its two parts; every other item is Yes or No. `scripts/review_check.py amstar2` rejects any other rating, lists "Partial yes" items without counting them as No, and applies the overall rule.

### 1a. The 16 items (checklist supplement to Shea et al. 2017, ES-210 to ES-225 [PAPER] doi 10.1136/bmj.j4008)

| Item | Asks | Options | Critical by default | Row |
|---|---|---|---|---|
| 1 | Question and inclusion criteria include PICO | Yes, No | | ES-210 |
| 2 | Methods set in a protocol before the review; deviations justified. Partial yes: written protocol with question, search, criteria, risk-of-bias plan. Yes: also registered, synthesis and heterogeneity plans | Yes, Partial yes, No | Yes | ES-211 |
| 3 | Selection of study designs explained | Yes, No | | ES-212 |
| 4 | Comprehensive search. Partial yes: at least 2 databases, keywords or strategy, justified restrictions. Yes: also reference lists, registries, experts, grey literature, search within 24 months of completion | Yes, Partial yes, No | Yes | ES-213 |
| 5 | Study selection in duplicate (or at least 80% agreement on a sample) | Yes, No | | ES-214 |
| 6 | Data extraction in duplicate | Yes, No | | ES-215 |
| 7 | Excluded studies listed (Partial yes) and each exclusion justified (Yes) | Yes, Partial yes, No | Yes | ES-216 |
| 8 | Included studies described: PICO and design (Partial yes); also setting and follow-up (Yes) | Yes, Partial yes, No | | ES-217 |
| 9 | Satisfactory risk-of-bias technique, RCTs and NRSI parts | Yes, Partial yes, No, Includes only | Yes | ES-218 |
| 10 | Funding sources of included studies reported | Yes, No | | ES-219 |
| 11 | Appropriate meta-analysis methods | Yes, No, No meta-analysis conducted | Yes | ES-220 |
| 12 | Impact of risk of bias on the pooled estimate assessed | Yes, No, No meta-analysis conducted | | ES-221 |
| 13 | Risk of bias accounted for in interpretation | Yes, No | Yes | ES-222 |
| 14 | Heterogeneity explained and discussed | Yes, No | | ES-223 |
| 15 | Publication bias investigated and its impact discussed | Yes, No, No meta-analysis conducted | Yes | ES-224 |
| 16 | Review authors' conflicts and funding reported | Yes, No | | ES-225 |

Ratings are the appraisers'. The table says what each item asks and which options exist; it never rates.

PRISMA 2020 is not an appraisal tool: a review that reports well can still be done badly (ES-04). Use PRISMA items only to find where in the paper the AMSTAR 2 evidence sits (for example item 6 for sources and dates, item 16b for excluded studies, item 24 for registration; ES-06, ES-13, ES-15).

### Where to look for each critical domain

| AMSTAR 2 item | Look for (PRISMA item, row) | Related sourced rule |
|---|---|---|
| 2 Protocol registered before | Item 24 registration and amendments (ES-15) | Cochrane recommends PROSPERO (ES-39) |
| 4 Search adequacy | Items 6 and 7 sources, dates, strategies (ES-06, ES-07); PRISMA-S (ES-25 [PAPER] doi 10.1186/s13643-020-01542-z to ES-31) | Two or more databases; registers; grey literature; reference lists (ES-45 to ES-48) |
| 7 Exclusions justified | Item 16b excluded studies with reasons (ES-13) | JCA exclusion list (ES-162) |
| 9 Risk of bias of included studies | Item 11 tool, reviewers, independence (ES-10) | RoB 2 or RoB 1 for RCTs (RoB 1 seven domains and criteria, ES-171 to ES-187), ROBINS-I for non-randomized (ES-69 to ES-77, ES-163, ES-164); AMSTAR 2 item 9 asks about allocation concealment, blinding, sequence and selective reporting for RCTs (ES-218) |
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
