# A2 Screening, extraction and appraisal

Framework task: DH-01.02.4.1, Part A, task A2. Replaces the old *Open a literature record*, *Deduplicate records*, *Classify a study*, *Link a trial*, *Grade evidence*, *Check a retraction*, *Find related records*, and the appraisal parts of *Digital Endpoint Instrumentation* and *Signal Detection Analysis*.

## What this task delivers

From the person's search results: deduplicated records grouped into studies, screening run to the target body's reviewer rule, an extraction sheet per study, the risk-of-bias tool chosen per result with the passages reviewers need, every design checked against the paper (not the library label), trial registrations linked, retractions checked, and RWD or digital-endpoint studies laid against the sourced fitness questions. It answers "which studies are in, what do they report, and what could bias each result?"

Why it matters: duplicates counted twice inflate an effect; a conference abstract labeled a meta-analysis can jump an evidence hierarchy (measured 19 October 2026, `tools.md`); a retracted paper in a dossier is a credibility failure (ES-119). The reviewer rules are mandatory in several bodies (ES-57, ES-59, ES-139).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.4.1 Part A, Screening, extraction and appraisal |
| Workflow | The steps below |
| Knowledge | `references/review-rules-by-body.md` section 4; `references/appraisal-and-certainty.md` sections 1 to 4; `references/rwe-and-digital-endpoints.md` sections 2 to 4; ES-20 [PAPER] doi 10.1136/bmj.n160 to ES-23, ES-54 to ES-61, ES-69 to ES-82, ES-119 to ES-125, ES-139 to ES-144, ES-163, ES-164; CV73 to CV94, CV42 to CV64, CV155 [PAPER] doi 10.1038/s41746-020-0260-4 to CV159 [PAPER] doi 10.1038/s41746-020-0260-4 |
| Tool | `literature.deduplicate`, `literature.get_record`, `literature.classify_study` (draft only), `literature.find_trial`, `literature.check_retraction`, `literature.grade_evidence` (draft only); `scripts/prisma_flow.py` on the screening log |
| Prompt | This guide |
| Template | `assets/screening-and-appraisal-output.md` |
| Input | The protocol (criteria, target body), exported records or the screening log, the reviewers' names, full texts or the parts the person can share |
| Governance | `references/governance.md`; every include, exclude and risk-of-bias judgment is the reviewers' |
| Catalogue job | none |

## Read the request

- **Target body.** It sets the reviewer rule and the risk-of-bias tool for RCTs (RoB 2 for Cochrane-style, RoB 1 for a JCA, ES-163). Ask if not named.
- **What the person has.** Records to deduplicate, a screening log to check, full texts to extract, or a single paper to appraise. Run only the steps that fit.
- **Reviewers.** Names or roles as the person gives them, for the reviewer rule and the AI-use table. "Owner not named" if absent.
- **RWD or digital endpoints.** If a study uses registry, EHR, claims or sensor data, the fitness questions in `rwe-and-digital-endpoints.md` apply on top of risk of bias.

## Workflow

### Step 1. Deduplicate and group into studies

1. Call `literature.deduplicate(records=[...], identifiers=[...])` on the person's records, or ask for their software's export. Record the merge rule per merge for PRISMA-S item 16 (ES-31).
2. Key every record on DOI or PMID, not the library `record_id`, which changed between search and get_record on 19 October 2026 (`tools.md`).
3. Group reports into studies (ES-22, ES-56). The library does not do this: on 19 October 2026 a secondary analysis stayed separate from its parent trial. Use registry ids, authors, recruitment dates and sample sizes as the person's reviewers decide.

### Step 2. Screening to the body's rule

1. State the rule: Cochrane (one person at title/abstract acceptable, two independent at full text), NICE (more than one on all records), IQWiG (two at all steps), rapid (dual at least 20% of abstracts) (ES-57, ES-58, ES-112, ES-129, ES-139).
2. If the person has a screening log, run `python3 scripts/prisma_flow.py LOG.csv --rule <body>` (add `--jca` for a JCA). Report the counts, any failed reconciliation line, missing decisions, full-text exclusions without reasons, and reviewer shortfalls exactly as printed.
3. Never change a decision. A row the script flags goes back to the reviewers.

### Step 3. Check every design against the paper

For each included report:

1. `literature.get_record(doi=...)` for identifiers and the open-access link.
2. Optionally `literature.classify_study(record=...)` for a draft label. Write the label with its `decided_by` basis, then the design from the paper's methods or registry. On 19 October 2026 a conference abstract titled "pooled analysis" was labeled `meta_analysis` "by title" and a secondary analysis of an RCT was `other` (`tools.md`, register N8).
3. Record `design_basis` in the extraction sheet: "methods section", "registry entry", or "library label (unchecked)".
4. Flag conference abstracts and preprints in the row (ES-53).

### Step 4. Link registrations

For every trial, `literature.find_trial(record=...)`. Example measured: the Chen 2025 RCT linked to NCT04069247 while its record's `trial_ids` was empty. Compare registered and reported outcomes for the "selection of the reported result" domain (ES-71); the comparison is the reviewers'.

### Step 5. Check retractions

`literature.check_retraction(doi=...)` for every included report, at inclusion and again at any update (ES-119, ES-120). The library checks Crossref only; write "no retraction found in Crossref on DATE". A retracted or expression-of-concern paper goes to the reviewers with the notice (ES-121, ES-125).

### Step 6. Extraction sheet

One row per study result: study, reports, design and basis, population, intervention, comparator, outcome, time point, participants, effect, measure, interval, source locator (section, table or page). Outcome data are extracted by two people independently in Cochrane (MECIR C46, ES-59); rapid reviews use one extractor and a checker (ES-113). Fill only from passages the person or the paper supplies; empty is `[GAP]`.

### Step 7. Risk of bias, laid out for the reviewers

1. Pick the tool by checked design and body (`appraisal-and-certainty.md` section 1).
2. For each result, list the domains (RoB 2: ES-71; ROBINS-I: ES-75 [PAPER] doi 10.1136/bmj.i4919) and, under each, the exact passage from the paper with its locator that bears on it, or "No information" (ES-72).
3. Leave the judgment column for the reviewers. A proposal, if the person asks for one, is labeled "proposed" and names the domain logic (overall = least favorable domain, ES-74; ROBINS-I critical means no synthesis, ES-77).
4. `literature.grade_evidence` is not a risk-of-bias tool; do not use its level here.

### Step 8. RWD and digital endpoints (when present)

For RWD studies, name the framework (FDA EHR and claims, FDA device RWE of 18 December 2025, or ICH E6(R3) Annex 2) and lay out the ten appraisal questions with passages (`rwe-and-digital-endpoints.md` section 2; CV79, CV90 to CV94, CV23). For digital endpoints, name FDA DHT or V3 and lay out the eight questions (section 3; CV46 to CV59, CV155 [PAPER] doi 10.1038/s41746-020-0260-4 to CV159 [PAPER] doi 10.1038/s41746-020-0260-4). Answers are the appraisers'.

### Step 9. AI-use log

Add every AI-assisted action in this task to the AI-use table (deduplication, label drafts, screening suggestions, extraction drafts) with the responsible human. Mandatory for a JCA (ES-169, ES-170); PRISMA asks for automation tools (ES-08, ES-09).

## Build the output

Follow `assets/screening-and-appraisal-output.md`. Answer first: how many studies are in, the problems in the log or table, and the one decision the reviewers must make next. Then the flow counts, the study grouping, the design-check table, the risk-of-bias layout and the AI-use table.

## Before you hand it over

- No include, exclude or risk-of-bias judgment is written as the model's.
- Every design shows its basis; every library label is marked as a draft.
- Every effect has a locator; every "supported" rests on a passage read in the same direction (register N3).
- Retraction checks name the source (Crossref) and the date.
- Counts come from the script output, not re-typed.
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- Not the reviewers' decisions: the model checks rules, lays out passages and computes counts.
- Appraising a published systematic review (AMSTAR 2) belongs to `evidence-quality-and-signal-monitoring`.
- Adverse-event signals for a marketed device (MAUDE, field safety notices) belong to dh-regulatory-strategy; this task appraises studies.
- Whether a DHT is a device is dh-regulatory-strategy's (CV45).
