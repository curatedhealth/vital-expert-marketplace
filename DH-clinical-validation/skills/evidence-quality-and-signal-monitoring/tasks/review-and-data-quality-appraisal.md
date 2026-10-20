# A2 Review and data quality appraisal

Framework task: DH-01.02.4.2, Part A, task A2. Replaces the validity half of the old *Digital Signal Detection Monitoring* ("watch whether digital-signal detection is valid enough to use as evidence").

## What this task delivers

One of three appraisals, laid out for the person's appraisers:

1. **A published systematic review**, against AMSTAR 2: the seven critical domains (or the appraisers' own list), the passage in the paper that bears on each item with its locator, and, once the appraisers rate the items, the overall confidence by the published rule, never a summed score.
2. **A real-world data source or study**, against a named reliability and relevance framework (FDA EHR and claims, FDA device RWE, or ICH E6(R3) Annex 2).
3. **A digital signal or endpoint** (a wearable or app measure used as evidence), against FDA DHT verification and validation or V3.

It answers "how far can we rely on this review, data source or digital measure?"

Why it matters: a review with more than one critical flaw "should not be relied on" (ES-107); a reporting checklist is not a quality check (ES-04); and the RWD frameworks use different words, so the framework must be named (research "Changes and conflicts").

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI/ML Governance Director (`ai-ml-governance-director`) |
| Skill | DH-01.02.4.2 Part A, Review and data quality appraisal |
| Workflow | The steps below |
| Knowledge | `references/review-and-data-quality.md`; ES-04 to ES-16, ES-105 [PAPER] doi 10.1136/bmj.j4008 to ES-109; CV23, CV42 to CV59, CV73 to CV94, CV155 [PAPER] doi 10.1038/s41746-020-0260-4 to CV159 [PAPER] doi 10.1038/s41746-020-0260-4 |
| Tool | `literature.get_record` (identifiers, open-access link); `scripts/review_check.py amstar2`; `verify.qualify_source` then `verify.check_claim` only for a finding the person wants to state |
| Prompt | This guide |
| Template | `assets/appraisal-output.md` |
| Input | The review's full text (or DOI with open access), or the RWD study and its data documentation, or the DHT validation reports; the decision the evidence serves; the appraisers' item ratings when they have them |
| Governance | `references/governance.md`; ratings and fitness decisions are the appraisers' |
| Catalogue job | none |

## Read the request

- **What is being appraised.** A review, an RWD source, or a digital measure. Run only the matching branch.
- **Full text.** AMSTAR 2 cannot be done from an abstract; if only the abstract is available, say which items cannot be assessed.
- **Critical items.** Default seven (ES-106); the appraisers may change them for this purpose (ES-109). Ask, and record the list used.
- **Framework for RWD or DHT.** Ask which applies (drug or device, US or EU). If unknown, lay out all three RWD frameworks side by side and let the person choose.

## Workflow

### Branch 1: published review (AMSTAR 2)

1. `literature.get_record(doi=...)` for the PMCID and open-access link; read the methods and results from Europe PMC or the publisher.
2. For each critical domain, find the passage, using the PRISMA item as a map (`review-and-data-quality.md` table): registration (item 24), sources and strategies (items 6 and 7), excluded studies with reasons (item 16b), risk-of-bias tool and reviewers (item 11), meta-analysis model and heterogeneity (item 13d), risk of bias in interpretation and certainty (items 15, 22), publication bias (item 14). Quote it with its locator, or write "not reported in the paper (looked in: ...)".
3. Example measured (2025 dCBT-I review, full text, 19 October 2026): registered on PROSPERO (CRD42024526617); PubMed, CENTRAL, Embase and PsycINFO searched to 31 March 2024; two authors screened and extracted independently; RoB 2 used (3 low, 19 some concerns, 7 high); random effects with I-squared 91% for insomnia severity; Egger's test reported; no GRADE or certainty statement, no grey literature and no excluded-studies list with reasons found by text search (`examples/live/passages_2026-10-19.json`). These are passages, not ratings.
4. Hand the layout to the appraisers. When they return ratings, write them to a CSV (item, rating) and run `python3 scripts/review_check.py amstar2 RATINGS.csv [--critical ...]`. Report the critical flaws, non-critical weaknesses, "Partial yes" items left to the appraisers, and the overall confidence by the rule (ES-107). Never a total (ES-108).
5. A library CEBM level for the review is not an AMSTAR 2 rating (`tools.md`).

### Branch 2: real-world data source or study

1. Name the framework (person's choice) and list its reliability and relevance dimensions (CV79, CV91, CV92, CV23).
2. Lay out the core checks with the passage or document for each: relevance and reliability assessment with limitations (CV90); conceptual and operational definitions and their validation metrics (CV80, CV81); traceability (CV82); continuity of coverage and care for claims (CV83); protocol and analysis plan fixed before outcomes (CV75, CV94); linkage prespecified (CV24); registry consent (CV85); EU catalogue registration and source update within 12 months (CV108).
3. Answers are the appraisers'; empty is `[GAP]`.

### Branch 3: digital signal or endpoint

1. Name the framework: FDA DHT (verification and validation, CV46) or V3 (verification, analytical validation, clinical validation, CV155 [PAPER] doi 10.1038/s41746-020-0260-4 to CV159 [PAPER] doi 10.1038/s41746-020-0260-4). They are not identical; V3 is not FDA policy.
2. Lay out the checks with the report or passage for each: validation in the studied population (CV48), evidence types (CV49), endpoint definition (CV55), meaningfulness for novel endpoints (CV56), same method across arms (CV58), usability in the population (CV51).
3. Any accuracy threshold is the person's; the sources set none.

## Build the output

Follow `assets/appraisal-output.md`. Answer first: for a review, the critical domains with a passage and those without, the overall confidence if the appraisers have rated, and the one decision next; for RWD or a digital measure, the framework named, the checks with evidence and those with gaps, and the decision next.

## Before you hand it over

- No item rating, overall confidence or fitness verdict is written as the model's.
- Every item points to a passage with a locator or says where you looked.
- The critical-item list used is stated.
- No summed score.
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- Risk of bias of primary studies inside a new review is the sibling skill's A2.
- Whether a DHT is a device, and device V&V for a submission, belong to dh-regulatory-strategy.
- Appraisal of an economic model belongs to dh-health-economics.
