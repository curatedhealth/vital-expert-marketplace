# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_mcda`). Counted calls draw on the library key's monthly allowance.

This is a method pack: there is no customer-success suite in the library and no catalogue job for implementation (`find_job {query: "implementation deployment customer"}` returned no match). The skill runs on the sourced references and the person's own plan. The library adds a ranking calculator for options the person scored, literature and Verify for published programs, field safety events for the product, and the record. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`. On that day several calls first returned 503 or 502 ("Nothing was counted") and succeeded on retry: retry once, then say the library did not answer.

## analytics.mcda (counted), B1

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number on the 0 to 4 scale) and `criteria_weights` (the person's, summing to 1).
- Returns "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)": `value_estimate` = weighted sum of score divided by 4, times 100, with `contributions` by criterion. Live call: three rollout options, weights 0.5, 0.3, 0.2; values 77.5, 62.5 and 40 (`examples/live/mcda_rollout_options.json`).
- Pitfalls: every criterion is treated as higher-is-better (`negative_criteria` came back empty and cannot be set), so name criteria as benefits ("staff capacity spared", not "staff burden"). No robustness view: work out by hand the weight change that would flip the top two, or use the QMS design skill's `mcda_swap.py` if installed. The response carries an unrelated note about price figures.
- Ranks only what the person scored. Never fill a score.

## literature.search_literature (counted), A1 optional

- Arguments: `query`, `limit`, optional `filters`.
- Live call: "implementation outcomes digital health technology deployment fidelity penetration", limit 5: five records (15 merged), three with an empty excerpt; a brief report described in its title as a "comparative conceptual analysis" was labeled `systematic_review` (confidence 0.6) (`examples/live/literature_search.json`). Do not rely on the design label; read the record.
- A title is not a finding. To use a statement from a paper: `verify.qualify_source {doi}` then `verify.check_claim` with a passage you have read.

## verify.qualify_source and verify.check_claim (counted)

- `qualify_source {doi: "10.1007/s10488-010-0319-7"}` (Proctor) returned tier "gold", retraction "none", date 2010-01-01 (online first; the research row cites the 2011 issue).
- `check_claim` with the research row's quoted passage returned "supported" (100 percent overlap). With a distorted claim (licenses sold as the denominator, plus "shows the product is clinically effective") and the same passage it also returned "supported" (38 percent overlap). The check rests on word overlap (register N3): accept "supported" only after reading that the passage states the claim in the same direction.
- The citation `check_claim` returns has no title, authors or year ("Unknown (n.d.)"); cite from `qualify_source` instead.
- `qualify_source {url: NICE ESF page}` returned "inadmissible", "no provenance" (register C1). Official guidance in this skill is cited from the research rows, which carry URL, quote and read date.

## regulatory-dh.search_safety_events (counted), A2 optional

- Use only to tell the person whether field safety events for their product or manufacturer exist before scheduling go-live; whether to proceed is theirs.
- Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction`, `since`, `limit`.
- Live calls: `{manufacturer: "Philips", since: "2026-01-01", jurisdiction: "US", limit: 5}` returned one Class II recall (EPIQ Elite ultrasound software, event date 7 August 2026) plus MAUDE counts for codes OLX, MLO and QIH with no stated link to the query; `{manufacturer: "Masimo", since: "2025-01-01", limit: 5}` returned no recalls and a MAUDE block for code OLW. `source_url` is the openFDA API endpoint, not the recall record; store retrieval date 13 October 2026.
- Describe each event only by its record. No events is not evidence of no events. MAUDE counts are reports, not confirmed events, and are not the manufacturer's own unless the code is the product's.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "adoption"}` returned six experts, including the Digital Adoption Lead (worker for this skill) and the Digital Adoption Manager ("Executes onboarding, training, and go-live jobs ... go-live checklists").
- `download_agent {expert: "digital-adoption-lead"}` returned 79,671 characters: system prompt, 67 skill entries (including this competency's three old tasks), 40 tool names. Its stop rules are the source of `governance.md`. Offer it only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With "Claude" it refused: "build_record refuses a record without a human cleared_by.name".
- Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `watch_*` tools; `market-access-dh.*` (payer and listing facts are Market Access's); `commercial-dh.*` (pricing and claims are Commercial's).
- `regulatory-dh.get_market_status`: device status is the regulatory owner's fact; ask the person.

## Local helper

- `scripts/plan_sequence.py PLAN.csv` (no connector). Columns in its header. Tested on 19 October 2026 on `examples/sample-data/deployment_plan.csv` (illustrative); output in `examples/plan_sequence_run.md`.
