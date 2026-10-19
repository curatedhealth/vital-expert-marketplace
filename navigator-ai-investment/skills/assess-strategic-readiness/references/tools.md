# Connector tools used by the Intelligence Core skills

Connector: VITAL Ontology Navigator (listed as `Ontology_Navigator` or `vital-ontology-navigator`, depending on the install; tool names are the same). Your assistant may prefix the names. Counted calls draw on the key's monthly allowance; check `my_usage` (free) first. Behavior below comes from the cluster 3 inputs lane on the connector's code, 19 October 2026 (M), not from live calls. [CHECK on the first live test run]

## methods_nav_compute (counted): option scoring

- Payload: `{"template_id": "nav.options", "items": [{"item_id": "o1"}, {"item_id": "base", "is_baseline": true}, ...], "scores": [{"scorer_id": "...", "item_id": "o1", "criterion_key": "outcome_fit" | "cost" | "time" | "reversibility" | "risk" | "governance_burden", "value": 1-10}, ...], "owner_scorer_id": "..."}`; optional `weight_adjustments` with a reason each.
- Refuses: no baseline ("this template needs a baseline option ... mark one item with is_baseline: true"); a non-whole or out-of-range score; a missing cell; a weight change without a reason.
- Returns per option: composite, median, rank, ties, disagreement by criterion; owner's view; sensitivity (scorer drop, weights ±20%); indicative under three scorers; the unadjusted result when weights changed.
- Pitfall: the baseline is ranked like any option. Present it as the reference line (method.md I7) and re-read the leader among the other options; the local script does this.
- Pitfall (live, 19 October 2026): the hosted engine call returned an error three times. When it fails, compute with the skill's local script and say once, in a clause, that the connector could not compute; the result is the same formula.

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

- Takes `brief_id` and `candidates` (each with `outcome_id`, `governance_burden`, optional `quadrant`); stores the caller's quadrant or "[GAP]". Pass the bucket computed by `scripts/placement_check.py` (in place-the-portfolio). It does not place anything itself.

## decide_run_stage, decide_build_record (counted)

- The options stage accepts any payload and checks nothing; a memo flag notes a missing do-nothing option. The record's numbered keys differ from the canon sections; the report follows the canon (section 4 gaps, 5 options, 6 recommendation). The record compiles only with a result of exactly Proceed, Investigate first or Handle it internally, owned by a named scorer.

## Storing scores on a brief (decide_attach_scores, then decide_release_scores)

Checked live on 19 October 2026 (M). Only when a brief is open and named people gave the scores.

- `decide_attach_scores`: `{"brief_id", "stage", "scores": {"cells": [ ... ]}}`. Each cell needs `item_id`, `criterion`, `value` (whole number 1 to 10), `rater_id` (the person's name), `rater_role` (`decision_owner`, `participant` or `facilitator`), `source` (`owner` or `participant`), `scale` (`"1-10"`) and `submitted_at` (time stamp). The connector names a missing field one at a time; fill them all at once.
- Never attach a cell a named person did not give. Since build 5b1220dc1 the connector also refuses an AI name and the old rows shape (M, recheck 19 October 2026). `simulated` is stored only on a brief marked as a test.
- Each person's cells are added as they come in. The same person scoring the same stage twice is refused unless the call carries `replace` (top-level, with `by`, a person's name, and `reason`); the earlier cells are kept in the brief's history.
- Then `decide_release_scores` with `released_by` (a named person), once every scorer has submitted. Without a name nothing is released, and the record shows the stage as unreleased.
- Never show the field names to the person.

## Not available

- The investment grid is not a connector tool: use `scripts/placement_check.py` (in place-the-portfolio).
- No Gate 3 (two signatures) function: that is cluster 6.

## my_usage (free)

Calls used, monthly cap and plan.
