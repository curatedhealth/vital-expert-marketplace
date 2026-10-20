# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_rice`). Counted calls draw on the library key's monthly allowance.

This is a method pack: no customer-success suite or catalogue job exists (`find_job {query: "implementation deployment customer"}` returned no match). The skill runs on the person's own site data, which never goes into a library call. The library adds field safety events for the product, ranking calculators for repairs the person scored, literature and Verify checks, and the record. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. Several calls first returned 503 or 502 ("Nothing was counted") and succeeded on retry: retry once, then say the library did not answer.

## analytics.rice (counted), B1

- Arguments: `initiatives`, each with `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`.
- Pitfall: `confidence` must be a percent (0 to 100). Passing 0.5 returned confidence 0.005 and scores a hundred times smaller, with no warning (`examples/live/rice_repairs.json`). Passing 50 returned confidence 0.5 and score = reach x impact x confidence / effort (for example 1600 x 0.5 x 0.5 / 2 = 200).
- The method citation the tool returns is a company blog (Intercom, 2016), not a primary source; describe RICE as a prioritization convention the person chose.
- No robustness view. State what change in the person's numbers would swap the top two.

## analytics.mcda (counted), B1 alternative

- Arguments: `alternatives` (id plus scores 0 to 4) and `criteria_weights` (sum to 1). Returns weighted sum / 4 x 100 with contributions. Every criterion is higher-is-better; no robustness view (measured in the sibling build, `customer-implementation-planning/examples/live/mcda_rollout_options.json`).

## regulatory-dh.search_safety_events (counted), A1 optional

- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction`, `since`, `limit`.
- Live calls: `{manufacturer: "Philips", since: "2026-01-01", jurisdiction: "US", limit: 5}` returned one Class II recall (EPIQ Elite ultrasound software, 7 August 2026) and MAUDE counts for codes OLX, MLO and QIH with no stated link to the query; `{manufacturer: "Masimo", since: "2025-01-01", limit: 5}` returned no recalls and MAUDE counts for code OLW (`examples/live/safety_events.json`). Store retrieval date 13 October 2026; `source_url` is the openFDA API endpoint, not the recall record.
- Report events by their record only. A recall is not evidence about deployment quality; no events is not evidence of no events; MAUDE counts are reports per product code, all manufacturers unless the code is the product's.

## verify.qualify_source and verify.check_claim (counted)

- Use when the person wants a published definition or finding checked. Sequence: `qualify_source {doi}` then `check_claim {claim, passage: {text, locator}, source}` with a passage you have read.
- `qualify_source {doi: "10.1007/s10488-010-0319-7"}` (Proctor) returned tier "gold", retraction "none".
- `check_claim` returned "supported" for the CS39 penetration claim with its passage (100 percent overlap), and also "supported" (38 percent overlap) for a distorted claim using licenses sold as the denominator and inferring clinical effectiveness (`examples/live/verify_proctor.json`, register N3). Read the passage yourself; accept only a same-direction statement.
- `qualify_source` on the NICE ESF page returned "inadmissible, no provenance" (register C1); cite official guidance from the research rows.

## literature.search_literature (counted), optional

- Live call returned five records on implementation outcomes; three had empty excerpts and a brief report was labeled `systematic_review` (`examples/live/literature_search.json`). Published deployments are context, never targets for this customer.

## agent-pack.list_experts and agent-pack.download_agent

- `download_agent {expert: "digital-adoption-lead"}` returned the expert with this competency's three old tasks (Deployment check, Site score, Deployment repair) among 67 skill entries. Its stop rules are the source of `governance.md`.

## verify.build_record (counted)

- Needs a human `cleared_by.name`; with "Claude" it refused. Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `watch_*` tools; `market-access-dh.*` (outcome payments and listings are Market Access's); `commercial-dh.*`.

## Local helper

- `scripts/implementation_outcomes.py SITES.csv --as-of YYYY-MM-DD [--milestones FILE.csv]` (no connector). Columns and formulas in its header. Tested on 19 October 2026 on the illustrative files in `examples/sample-data/`; output in `examples/outcomes_run_2026-10-19.md`.
