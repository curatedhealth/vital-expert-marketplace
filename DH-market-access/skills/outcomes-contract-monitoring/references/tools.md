# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Behavior below was observed in live calls on 19 October 2026.

## The short version

Contract monitoring runs on the person's data and rules. The library holds no outcome-contract data, no AbEM results and no ACCESS participant results, so A1 and A2 make no library calls. The person's patient data never goes into a library call.

Observed:

- `market-access-dh.retrieve_guidance {query: "erfolgsabhängige Preisbestandteile DiGA outcome-based price component", limit: 5}` and `{query: "outcomes-based contract risk-sharing agreement digital health", limit: 5}`: no passage (`results: []`, `[GAP]`).
- `market-access-dh.list_schemes`: DE_DIGA holds 82 listings (loaded 15 October 2026); no scheme carries outcome-measurement or contract-attainment fields. Before 15 April 2027 there are no AbEM reports to load in any case (DE-18).
- `market-access-dh.find_scheme_precedents {scheme: "DE_DIGA", indication: "F32", limit: 10}`: depression DiGA with status and a `price` field. The field does not say whether it is a negotiated amount and shows no outcome component. Use only for context in B1, never as a comparator's attainment or terms.

## verify.build_record (counted)

- Needs a named human in `cleared_by`; refuses a missing name or a tool or model name. Use only when an output leaves the conversation. Do not put patient-level data in the record; put the aggregate results.

## verify.qualify_source and verify.check_claim

Not needed for monitoring on the person's data. If a review cites literature, use the sequence in the sibling skill (`outcomes-based-contracting/references/tools.md`): pass the full object from `qualify_source` as `source`, because `source: {doi}` alone returned unverifiable. Official documents (the CMS ACCESS PDF) are rated inadmissible, "no provenance"; cite rule facts to their row in `references/`.

## scripts/attainment.py (local, not a library call)

Computes completeness, per-measure and per-patient results, the attainment rate under the contract's rules and under the alternative treatment of missing data, and the payment factor. Tested on `examples/bh_cohort_illustrative.csv` with an ACCESS-style rules file, the same file with the person's below-10 rule, and a population-average rules file. A measure with `applies_if.baseline_min` uses `target_below` (for ACCESS BH, `{"type": "final_below", "value": 10}`) for a baseline under the cut-off; without `target_below` the measure is not required for that patient. The script does not model PGIC submission or denominator exclusions by unalignment reason; add a column or remove the patient by hand, and say so.

## Not used here

- `watch_*` tools.
- Any library call carrying patient data, contract terms or prices.
