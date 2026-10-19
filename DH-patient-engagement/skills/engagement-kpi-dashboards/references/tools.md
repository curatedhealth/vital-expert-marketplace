# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `verify_qualify_source`). Counted calls draw on the library key's monthly allowance. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This is a method pack. The work runs on the person's own event data and the sourced references. The library adds literature search and Verify when a published definition must be cited, a ranking calculator for options the person scored, and the record. The person's events, ids and KPI values never go into a library call.

## literature.search_literature (counted)

- Arguments: `query`; optional `limit` (1 to 50), `filters`, `sources`.
- Observed: `{query: "nonusage attrition digital health app engagement usage half-life", limit: 5}` returned 5 of 14 merged records from PubMed, Europe PMC, OpenAlex and Crossref, each with DOI, design label, design confidence and per-source retrieval time.
- Pitfalls seen:
  - Design labels are guesses with a confidence: a paper titled "A Systematic Review and Thematic Synthesis" came back as `narrative_review` (0.68); a 2026 PLOS Digital Health paper came back `other` (0.3) with an empty excerpt.
  - `trial_ids` was empty on the record labeled `rct` (register N8).
  - bioRxiv has no keyword search; the warning says so.
- Use it in A1 only when the person wants a published definition or a comparable program's engagement measure. A published figure from another program is context, never a target.

## verify.qualify_source then verify.check_claim (counted)

The working sequence for citing a published definition:

1. `verify.qualify_source {doi, question}`. Observed: Eysenbach 2005 (`10.2196/jmir.7.1.e11`) tier gold, status current, PMID 15829473; COSMIN guideline (`10.1007/s11136-018-1798-3`) tier gold, status current.
2. `verify.check_claim {claim: {text}, passage: {text, locator}, source: <the whole object qualify_source returned>}`, with a passage you have read in the reference file.

Pitfalls seen:

- Passing `source: {doi: "..."}` returned `unverifiable`, "No admissible source was available". Pass the object `qualify_source` returned (`source_id`, `tier`, `code`, `official_url` and the rest); then the same claim returned `supported`.
- Direction is not checked (register N3): for the usage half-life passage, the claim "Eysenbach recommends reporting a usage half-life" returned `supported` (62 percent overlap) and its negation "Eysenbach advises against reporting a usage half-life" returned `partial` (56 percent overlap). Accept a claim only when you have read the passage and it states the claim in the same direction.
- The citation block came back with DOI, PMID and authors empty and year null, although `qualify_source` held them (register C18). Cite from the reference row instead.
- On the first attempt of the day, `qualify_source`, `check_currency` and `search_literature` returned 503 ("could not answer this call. Nothing was counted"); `qualify_source` and `search_literature` worked when retried later (`check_currency` was not retried). Retry once; if it fails again, cite the reference row and say Verify was not reached.

## analytics.rice (counted)

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`. Every number is the person's.
- Pitfall seen: `confidence` must be a percentage (0 to 100). Given 0.8 it divided again by 100 and returned scores 100 times too small (1.088 instead of 108.8); given 80 it returned 108.8. The schema does not say this. Pass the person's confidence as a percentage and check one score by hand (reach times impact times confidence divided by effort).
- The method citation returned is an Intercom blog post (McClure 2016), not a primary source; the response also carries an unrelated note about public registers and price figures.
- In B1 it ranks dashboard or KPI options only when the person supplied every number. Never fill a number for them.

## analytics.mcda (counted, not called in this build)

Ranks options the person scored on a 0 to 4 scale with their weights. Measured in sibling builds: every criterion is treated as higher-is-better, and no robustness view is returned (register C17). Use it in B1 instead of RICE when the person scores on criteria rather than reach, impact, confidence and effort.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "analytics"}` returned two experts: the Data & Analytics Lead (`data-analytics-lead`), this skill's worker, and the Data Visualization Specialist (Health) (`data-visualization-specialist-health`).
- `download_agent {expert: "data-analytics-lead"}` returned 84,013 characters: a system prompt and 101 bound skill methods, including the six register tasks this pack replaces (KPI definition, Dashboard slice, Tracking job, KPI recomputation, Formula drift, KPI repair). Its stop rules are the source of `governance.md`. Its list of bound competencies does not include DH-02.03.3.1 or DH-02.03.3.2 (register C14). Offer the download only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. Observed: with the name "Claude" it refused ("build_record refuses a record without a human cleared_by.name").
- Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `find_job {query: "engagement KPI dashboard"}` returned no job: the library has no hosted job for this competency.
- `watch_*` tools.
- Market access, regulatory and commercial suites: not needed to define or compute engagement KPIs.

## Local helper

- `scripts/engagement_kpis.py` (no connector): `kpis` computes the person's KPI cards from their event file; `attrition` computes nonusage attrition curves (raw and Kaplan-Meier), usage half-life, relative risk by group and dropout per follow-up wave. Tested on 19 October 2026 on the illustrative files in `examples/sample-data/` (outputs saved next to them).
