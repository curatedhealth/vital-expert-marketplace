# Connector tools used by the Intelligence Core skills

Connector: VITAL Ontology Navigator (`vital-ontology-navigator`). Your assistant may prefix the names. Counted calls draw on the key's monthly allowance; check `my_usage` (free) first. Behavior below comes from the cluster 3 inputs lane on the connector's code, 19 October 2026 (M), not from live calls. [CHECK on the first live test run]

## methods_nav_compute (counted): option scoring

- Payload: `{"template_id": "nav.options", "items": [{"item_id": "o1"}, {"item_id": "base", "is_baseline": true}, ...], "scores": [{"scorer_id": "...", "item_id": "o1", "criterion_key": "outcome_fit" | "cost" | "time" | "reversibility" | "risk" | "governance_burden", "value": 1-10}, ...], "owner_scorer_id": "..."}`; optional `weight_adjustments` with a reason each.
- Refuses: no baseline ("this template needs a baseline option ... mark one item with is_baseline: true"); a non-whole or out-of-range score; a missing cell; a weight change without a reason.
- Returns per option: composite, median, rank, ties, disagreement by criterion; owner's view; sensitivity (scorer drop, weights ±20%); indicative under three scorers; the unadjusted result when weights changed.
- Pitfall: the baseline is ranked like any option. Present it as the reference line (method.md I7) and re-read the leader among the other options; the local script does this.

## methods_capability_gap (counted): do not use for the outcome-weighted gap

- It scores current against required, 1 to 10, but passes no outcome links, so every capability is weighted 1. Use `scripts/readiness_check.py`, which applies the engine's own formula with the outcome weights. If you do call it, label the result "unweighted".
- It refuses rows carrying the old 0 to 5 fields ("The 0 to 5 calculator is not this tool").

## catalogue_search, chain_trace (counted): capabilities and outcome links

- Capability candidates: search the capability pillar at the audience's level with words from the top outcomes. [CHECK pillar code and levels on the live run]
- `chain_trace` from a mission-level outcome lists linked capabilities and use cases (level 3 only); an outcome with no capability is a named gap, not a score.

## opportunity_recommend (counted): candidate opportunities

- Stage `options` with a hint (words from the top outcomes) returns up to 10 library rows across outcome levels, plus six standing labels: Do nothing · Do it internally · Fund · Build the basis first · Defer · Support and do not automate. An empty hint returns a gap.
- The rows are candidates the person may add to the shortlist. The tool does not recommend a VITAL service, and neither do you.

## portfolio_place (counted): stores, does not compute

- Takes `brief_id` and `candidates` (each with `outcome_id`, `governance_burden`, optional `quadrant`); stores the caller's quadrant or "[GAP]". Pass the bucket computed by `scripts/placement_check.py`. It does not place anything itself.

## decide_run_stage, decide_build_record (counted)

- The options stage accepts any payload and checks nothing; a memo flag notes a missing do-nothing option. The record's numbered keys differ from the canon sections; the report follows the canon (section 4 gaps, 5 options, 6 recommendation). The record compiles only with a result of exactly Proceed, Investigate first or Handle it internally, owned by a named scorer.

## Not available

- The investment grid is not a connector tool: use `scripts/placement_check.py`.
- No Gate 3 (two signatures) function: that is cluster 6.

## my_usage (free)

Calls used, monthly cap and plan.
