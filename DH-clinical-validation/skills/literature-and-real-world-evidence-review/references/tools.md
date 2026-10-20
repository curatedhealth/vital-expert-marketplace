# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `literature_search_literature`). Counted calls draw on the library key's monthly allowance; `literature.list_sources` is free. Behavior below was measured in live calls on 19 October 2026 with a digital CBT for insomnia question; trimmed outputs are in `examples/live/`. Register items (C, N) refer to the Digital Health connector improvement register.

## literature.list_sources (free)

- No arguments. Measured: loaded PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv/medRxiv, ClinicalTrials.gov, Semantic Scholar, Unpaywall. Gaps (not queried): Consensus, Cochrane Library (so CENTRAL), PROSPERO, Embase, Scopus, Web of Science.
- Consequence: the library cannot run the CENTRAL or Embase searches Cochrane names (ES-44) or the MEDLINE plus CENTRAL floor of the EU JCA (ES-151, ES-155). It can run PubMed (MEDLINE) and candidate-finding. Say so in every A1 output: the library is a candidate finder and a test bed for strings, not the review's search.

## literature.search_literature (counted)

- `query` (required), `limit` 1 to 50, `filters` {`date_from`, `date_to`, `designs[]`, `species`, `language`}, `sources[]`.
- Measured: "digital cognitive behavioral therapy for insomnia app randomized controlled trial", limit 8: 32 hits, 29 after merge, 8 returned. Sources answered: PubMed, Europe PMC, OpenAlex, Crossref, bioRxiv (bioRxiv has no keyword search; only the last 30 days). Semantic Scholar and ClinicalTrials.gov did not answer this call.
- Off-topic records ranked in: a depression-after-brain-injury preprint, a non-digital single-session CBT-I trial (2015), and the RESiLIENT depression trial.
- Excerpts empty on 7 of 8 records. `trial_ids` empty on every RCT (register N8).
- One record (the RESiLIENT insomnia secondary analysis) was in `records` but missing from the `results` summary list.
- With `filters.designs=["systematic_review","meta_analysis"]` and `date_from="2020-01-01"`, limit 6: 24 hits, 18 after merge; one non-digital network meta-analysis; one record listed two authors twice ("Suonaa Lee", "Eun Min Lee").
- The tool takes a plain query, not a Boolean strategy with field tags. It does not show the strategy as run per source, so it cannot meet PRISMA-S item 8 ("copied and pasted exactly as run", ES-28). Use it to test terms and find candidates; run the review's strategies in the databases themselves.

## literature.get_record (counted)

- One of `doi`, `pmid`, `pmcid`, `openalex_id`.
- Measured: DOI 10.1038/s41746-025-01514-4 returned six sources and an abstract excerpt with results. PMCID PMC13671329 returned the DOI and PMID that the search record lacked, under a different `record_id` (search `bbbe2d70...`, get_record `4641c102...`).
- Pitfall: `record_id` is not stable between search and get_record. Key your log on DOI or PMID, not on `record_id`.
- Excerpts may be empty (7 of 8 in the measured search) or stop before results (register N8, reported by an earlier build; not re-measured here). Results passages come from the paper; Europe PMC full text or abstract is a primary read.

## literature.deduplicate (counted)

- `records[]` and/or `identifiers[]` (DOI or PMID strings).
- Measured: 6 inputs to 4 outputs; merged the two Sakata records by PMCID and the Chen DOI and PMID by DOI. Merge rule and crosswalk given per merge.
- It merges records of the same report. It does not link a secondary analysis to its parent trial (RESiLIENT stayed as two papers), which is correct for records (ES-22) but means study-level grouping is the reviewers' job (ES-56). Merged input records came back with design null and authors empty.
- Report the deduplication method and software for PRISMA-S item 16 (ES-31): "VITAL library deduplicate (identifier match: DOI, PMID, PMCID)" plus the reviewers' visual check (ES-54).

## literature.classify_study (counted): design-label errors (register N8)

- `record` (required). Returns design (rct, cohort, case_control, systematic_review, meta_analysis, preprint, other), confidence and `decided_by`.
- Measured errors:
  - A conference abstract titled "POOLED ANALYSIS OF TWO RANDOMIZED, DOUBLE- BLIND, SHAM-CONTROLLED TRIALS" (publication type `openalex:conference-abstract`) labeled `meta_analysis`, 0.78, `decided_by` "title:meta-analysis", although the title does not contain that word.
  - A secondary analysis of a randomized trial labeled `other`, 0.3, "no decisive metadata or text cue".
  - A preliminary RCT labeled `rct` from the title word "randomized" while PubMed's publication type did not say RCT. The label happens to fit; its basis is a title word.
  - `find_related` returned labels outside this list (`nonrandomized_trial`, `narrative_review`).
- Rule: every design in the review comes from the paper's methods or the registry entry. Record the basis in the evidence table (`design_basis`). A library label is a draft.

## literature.grade_evidence (counted): grades follow the label (register N8)

- `record` or `records`, `question_type`, `standard` (`cebm2011` default, or `grade`, always draft).
- Measured, CEBM 2011, treatment: RCT level 2; conference abstract level 1 and not marked provisional (confidence 0.78); a real systematic review level 1 marked provisional (0.546, "included-study design not established"); the secondary analysis `[GAP]`.
- Measured, `standard="grade"`: per record, "high" from design rct and from design meta_analysis, all five downgrade and three upgrade factors null, "draft scaffold".
- Rules: CEBM levels are not GRADE certainty and are not in any HTA rule read for this skill. GRADE certainty is per outcome across the body of evidence (ES-96), not per record; the tool's GRADE output is only the starting level (ES-90) for a reviewer to work from.

## literature.check_retraction (counted)

- `doi` or `record`. Measured: Wakefield 1998 (10.1016/S0140-6736(97)11096-0) returned "retracted", notice 10.1016/s0140-6736(10)60175-4, date 6 February 2010, from Crossref. The Chen 2025 RCT returned "none".
- `sources_checked` was Crossref only. Retraction display is inconsistent across sources (ES-123); report "no retraction found in Crossref on DATE".

## literature.find_trial (counted)

- `record` or `nct_id`. Measured: the Chen 2025 RCT linked to NCT04069247 (completed; sponsor Chinese University of Hong Kong) via PubMed's secondary id; one other registration citing the paper as background was not linked.
- Use it in A2 for every RCT, because `trial_ids` on records is empty.

## literature.find_related (counted)

- `record`, `direction` (cites, cited_by, similar), `limit`. Measured `cited_by` on the 2025 review, limit 8, via Semantic Scholar: a 2026 RCT, a 2026 pilot trial, two 2026 reviews, and off-topic papers (chronic pancreatitis review, wildfire survivors). Authors and venue empty; no total count.
- Use it for forward citation searching (PRISMA-S item 5, ES-27), then screen.

## literature.build_evidence_table (counted)

- `records[]`, `passages{record_id: text}`, `question{population, intervention, comparison, outcome}`, `question_type`, `standard`.
- Measured with four rows: the results sentence of the Chen RCT was placed in both `population` and `effect`; intervention, comparator and outcome `[GAP]`; a second Chen row (PMID only) was kept as its own row (duplicate not detected); the retracted paper was flagged; `question_match` was 3 on three rows and 2 on the retracted paper, with no explanation; citations carried no authors.
- Rule: use it only as a scaffold. The B1 table is built from the reviewers' extraction, then checked with `scripts/check_evidence_table.py`.

## literature.build_citation (counted)

- `record`, optional `passage`. Measured: complete Chicago string with authors and DOI when the authors are passed in; no volume, issue or article number.

## literature.generate_report (counted)

- Templates memo, identity, evidence, grade, citation. Measured `memo` on two records without passages: every evidence field `[GAP]`; references without authors or DOI. Not used for outputs.

## verify.qualify_source then verify.check_claim (counted)

- `qualify_source(doi, question)` rated the Chen RCT "gold", status current, score 78.
- `check_claim(claim, passage{text, locator}, source)` with the exact results sentence: a claim restating that finding in the same direction returned "unsupported" (29% overlap); the reversed claim also returned "unsupported" (15%), not "contradicted". In earlier builds an aim-only passage returned "supported" (register N3).
- The citation inside `check_claim` named the publisher as author, gave "January 1, 2025" as the date and empty identifiers (register C18).
- Rule: the decision is yours from reading the passage. Record the tool status beside your reading; accept a finding only if the passage states it in the same direction. Use `literature.build_citation` for citations.
- `verify.verify_text` with bare DOIs returns unverifiable (register C18); not used.

## verify.check_currency (counted)

- Measured on the 2025 review: `current: true`, `notices: ["crossref"]`. On Wakefield 1998: `retracted: true`, no notice id or date. "Current" here means not retracted, corrected, superseded or withdrawn in Crossref; it says nothing about whether a review's search is up to date. Currency of reviews is the sibling skill's task.

## verify.build_record (counted)

- Needs a named human in `cleared_by`; refuses a tool or model name. Call it only when an output leaves the conversation and the person names who clears it.

## Catalogue job

- `evidence-table` ("Evidence table for a product's claims", available, price hypothesis USD 49, owner Access and Reimbursement Lead) was found with `find_job("evidence-table")`; the query "evidence table literature review" found nothing. Its tool list includes `verify.verify_text`, which fails on DOIs (C18). Not started in this build. B1 names it as an option for the person; its output still goes through B1's checks.
