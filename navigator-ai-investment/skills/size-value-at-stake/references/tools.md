# Connector tools used by this competency

Connector: VITAL Ontology Navigator (`vital-ontology-navigator`). Your assistant may prefix the names. Counted calls draw on the key's monthly allowance; check `my_usage` (free) first. Behavior below was established by read-only lanes on the connector's code on 19 October 2026 (M), not by live calls. [CHECK on the first live test run]

## catalogue_search (counted)

- Arguments: `pillar` `VD`; `level` 1, 2 or 3; `query` words from the decision and goal; optional `limit` 1 to 25. Status defaults to Active.
- Returns rows with a spoken label (the row's name) and code.
- Pitfalls: do not pass `function` for this pillar; it removes every row. Draft themes are hidden by default. Level 3 rows carry no value dimension of their own; use the parent lever's and say "inherited".

## catalogue_list_children (counted)

- Arguments: the parent row's `id` (not its code) and the pillar.
- Returns child rows one level down.
- Pitfalls: a code is not looked up; search first, pass the `id`. Seven level 3 drivers have no parent and never appear here; they can be found by search.

## value_range (counted)

- Arguments: `brief_id`, and the range inside `payload`: `{"low": ..., "mid": ..., "high": ..., "unit": "...", "basis": "...", "drivers": [...], "measures": [...]}`.
- Refuses: a missing low, mid or high; low equal to high ("A point estimate is refused"); missing unit or basis; any measure without a baseline and an owner.
- Stores the range as the brief's value at stake (Decision Record section 2).
- Pitfalls: the hosted connector path keeps only `brief_id` and `payload`; fields sent at the top level (as the tool's published schema shows) are dropped before the rule runs. Always nest them in `payload`. Reported to the improvement register. Without an open brief there is nowhere to store the range; it lives in the report.

## bridge_for_driver and bridge_explain (counted)

- Arguments: a level 3 driver `id` (`bridge_for_driver`), or `driver_id` for a plain-language path (`bridge_explain`).
- Returns linked outcomes and measures for that driver.
- Pitfalls: only level 3 links are read today; for a level 1 or 2 driver the call returns nothing useful. The edge label in the result uses a retired name; say "contributes to". An empty result reads "[GAP] No junction rows found": say "the library links no outcome to this driver yet".

## Not available: driver scoring

The value-driver comparison template exists in the engine but cannot be run by `methods_nav_compute` today (LANE). Use `scripts/value_check.py drivers`, or lay the scores out as a table.

## my_usage (free)

Calls used, monthly cap and plan.
