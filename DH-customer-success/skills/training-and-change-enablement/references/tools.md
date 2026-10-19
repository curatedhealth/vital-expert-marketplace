# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_mcda`). Counted calls draw on the library key's monthly allowance.

This is a method pack: Customer Success has no library suite of its own. The competency runs on the person's own training records and the sourced references. The library adds a ranking calculator for enablement options the person scored, literature checks for the method papers, field safety events for the person's product, and the record. The person's training log never goes into a library call. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

## analytics.mcda (counted), B1

- Arguments: `alternatives` (each `id` plus `scores`, a map of criterion to number) and `criteria_weights` (the person's weights; they should sum to 1).
- Observed: method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)". Each `value_estimate` is the weighted sum of score divided by 4, times 100; `contributions` break it down by criterion. Three enablement options scored on four criteria returned 80, 60 and 55 (`examples/live/mcda_enablement_options.json`).
- Pitfalls: every criterion is treated as higher-is-better (`negative_criteria` came back empty and the schema has no field to set it); name criteria so higher is better ("effort avoided", not "effort"). No robustness view is returned (register C17). Compute swap points by hand: for options X above Y and criterion c, find the weight on c, with the other weights rescaled in proportion, at which the two values are equal. The QMS design skill in the quality pack ships `mcda_swap.py`, which produced `examples/live/mcda_swap_points.md` for the worked example.
- Ranks only what the person scored. Never fill a score.

## verify.qualify_source then verify.check_claim (counted), A1 when a method claim leaves the conversation

- `qualify_source {doi}` rated both method papers "gold": Proctor et al. (10.1007/s10488-010-0319-7) and ERIC (10.1186/s13012-015-0209-1).
- `qualify_source {url: "https://www.fda.gov/media/80481/download"}` (FDA human factors guidance) returned tier "inadmissible", "no provenance" (register C1). Do not spend calls checking FDA, NICE or statute rules; cite their rows, which carry URL, quote and read date.
- `check_claim` argument shape that works: `claim {text}`, `passage {text, locator}` quoted from the paper, and `source {source_id: DOI, tier, source_type: "literature", code: DOI}`. With `source {doi}` only, it returned "unverifiable" ("No admissible source was available") three times.
- Critical pitfall (register N3): with the Proctor penetration passage it returned "supported" (100 percent overlap) both for the correct claim and for a claim with numerator and denominator swapped. "Supported" proves word overlap only. Accept a check only when you have read the passage and it states the claim in the same direction, with the same numerator and denominator.
- The returned citation has title null, no authors, year null, "Unknown (n.d.)". Build citations from `literature.get_record` instead.
- Three calls returned "could not answer this call (503). Nothing was counted." Retry once; if it fails again, cite the row and say the check was not run.

## literature.get_record (counted)

- `{doi: "10.1007/s10488-010-0319-7"}` returned PMID 20957426, PMCID PMC3068522, eight authors, venue, year 2010, design "other" (confidence 0.3). The research row calls it Proctor 2011; cite by DOI and avoid a year conflict.

## regulatory-dh.search_safety_events (counted, optional), A1

- Use only to see whether field events for the person's own product or manufacturer touch the trained task. Arguments: at least one of `manufacturer`, `product`, `product_code`; optional `jurisdiction`, `since`, `limit`.
- Observed: `{product: "remote monitoring", jurisdiction: "US", since: "2025-01-01", limit: 5}` returned nothing ("absence from the store is not evidence of absence"). `{product: "insulin", ...limit: 10}` returned 6 recalls, one duplicated per product line; summaries state software defects (for example a decimal separator not recognized when the user changes phone region settings).
- Pitfalls: no field states a use error, the corrective action, or whether training or labeling was part of a correction; `source_url` is the openFDA API endpoint, not the recall record (register P1). Describe each event only by what its summary states. Never infer that training caused or would prevent an event.

## agent-pack.list_experts and agent-pack.download_agent

- `list_experts {query: "adoption"}` returned six experts including the Digital Adoption Lead (`digital-adoption-lead`, the worker for this skill) and the Digital Adoption Manager (`digital-adoption-manager`). Both downloads carry the six old register tasks of this competency and its sibling (`examples/live/agent_pack_*.json`).
- The Lead's stop rules are a source for `governance.md`. Offer the download only when the person wants the role on their own assistant.

## verify.build_record (counted)

- Needs `clearances` with a human `cleared_by.name`. With the name "Claude" it refused: "build_record refuses a record without a human cleared_by.name".
- Call it only when an output leaves the conversation and the person names who clears it.

## Not used here

- `analytics.rice`: B1 uses the person's criteria through `analytics.mcda`; RICE needs reach, impact, confidence and effort numbers the person rarely holds for training options. Use it only if the person asks and supplies every number.
- `watch_*` tools.

## Local helper

- `scripts/session_coverage.py` (no connector) on the person's training log. Tested on 19 October 2026 on `examples/sample-data/illustrative_sessions.csv` (illustrative, written for this example); output in `examples/sample-data/run_site_role.txt`.
