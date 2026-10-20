# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Behavior measured in live calls on 19 October 2026 on a 2025 systematic review of fully automated digital CBT for insomnia (doi 10.1038/s41746-025-01514-4) and related records; trimmed outputs in `examples/live/`. The full measurement of every literature tool, including design-label errors, is in the sibling skill's `references/tools.md`; the points that matter here are below. Register items (C, N) refer to the Digital Health connector improvement register.

## verify.check_currency (counted)

- `doi`, `pmid`, `pmcid`, `catalogue_id`, `record` or `url` (a URL alone returns "not checked").
- Measured: the 2025 review returned `current: true`, `retracted/corrected/superseded/withdrawn: false`, `notices: ["crossref"]`. Wakefield 1998 (10.1016/S0140-6736(97)11096-0) returned `retracted: true`, `current: false`, with no notice id or date.
- Pitfall: "current" means not retracted, corrected, superseded or withdrawn in Crossref. It does not mean the review's search is up to date: the same review searched to 31 March 2024 and newer trials cite it. Never report "current" as currency of the evidence. `notices` lists the source checked, not notices found.

## literature.check_retraction (counted)

- `doi` or `record`. Measured: Wakefield 1998 "retracted", notice 10.1016/s0140-6736(10)60175-4, 6 February 2010; the Chen 2025 RCT "none". Source checked: Crossref only.
- Use it rather than `check_currency` when the notice and date are needed. Word a clean result "no retraction found in Crossref on DATE" (ES-123).

## literature.find_related (counted)

- `record`, `direction` (cites, cited_by, similar), `limit` 1 to 50.
- Measured `cited_by` on the 2025 review, limit 8, via Semantic Scholar: a 2026 preliminary RCT, a 2026 pilot non-randomized trial, a 2026 network meta-analysis of digital therapeutics for sleep quality, a 2026 review of wearable digital therapeutics, and off-topic items (chronic pancreatitis, wildfire survivors). Authors and venue empty; no total count, so "8 returned" is not "8 exist". Design labels outside the `classify_study` list appeared (`nonrandomized_trial`, `narrative_review`).
- Use it as a new-study signal: list items dated after the review's last search, then pass them to screening. Year-only dates cannot be placed against a search date in the same year.

## literature.search_literature (counted)

- Measured with `filters={"designs": ["systematic_review","meta_analysis"], "date_from": "2020-01-01"}`, limit 6: six reviews, one off topic (non-digital), one record with two authors listed twice. Useful to find newer or competing reviews; not a systematic search (no CENTRAL or Embase, see `literature.list_sources`).

## literature.get_record (counted)

- Measured on the 2025 review by DOI: six sources, PMCID PMC11903857 (absent in the search record), abstract excerpt with results. The search date, registration, reviewer numbers and risk-of-bias tool were read from the Europe PMC full text, not from the library (`examples/live/passages_2026-10-19.json`).

## literature.grade_evidence (counted)

- Measured: the 2025 review got CEBM level 1, marked provisional ("assumes randomized trials; included-study design not established"); a conference abstract labeled meta-analysis by title got level 1 not provisional (register N8). A CEBM level says nothing about how well a review was done; AMSTAR 2 does that (A2).

## verify.qualify_source then verify.check_claim (counted)

- Measured on the Chen 2025 RCT: `qualify_source` gold, current. `check_claim` with an exact results sentence returned "unsupported" for a correct same-direction claim (29% overlap) and "unsupported" for the reversed claim (15%), not "contradicted" (register N3). The citation inside named the publisher as author (C18).
- Rule: your reading of the passage decides; record the tool's status beside it.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `watch_*` tools: not called. A change watch on literature does not exist in the library on 19 October 2026 `[GAP]` (see BUILD_NOTES); A1 is run on request.
- `regulatory-dh.search_safety_events`: device adverse-event signals belong to dh-regulatory-strategy.

## Catalogue job

- None for this competency. `evidence-table` (available, find_job "evidence-table") builds a new table; it does not check currency or appraise a review.
