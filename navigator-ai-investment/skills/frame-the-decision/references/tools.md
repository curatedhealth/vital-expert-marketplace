# Connector tools used by this competency

Connector: VITAL Ontology Navigator (`vital-ontology-navigator`). Names below are the connector's; your assistant may prefix them. Counted calls draw on the monthly allowance of the key; free calls do not. Check `my_usage` (free) before a run: when the allowance is used up, only free calls and a few recommendation tools still answer.

Behavior below was established by read-only lanes on the connector's code on 19 October 2026 (M), not by live calls. [CHECK on the first live test run]

## decide_start (counted)

- Arguments: `title` (use the accepted decision statement), `intent` (`decision` for the full pass from Direction to Organizational learning; `direction` for this stage only), optional `context` object.
- Returns: `brief_id` and the template suite. Pass `brief_id` on every later call.
- Pitfalls: an empty intent does not open a brief; an unknown intent is refused. A brief opened with `direction` cannot be compiled into a record on its own: the compile requires a final result (Proceed, Investigate first, Handle it internally), which Direction does not produce. This skill therefore never calls `decide_build_record`; it drafts the contract in the conversation.

## methods_nav_compute (counted)

- Arguments for sizing: `template_id` `nav.sizing`; `items` `[{"item_id": "decision"}]`; `scores` one cell per scorer per criterion: `{"scorer_id": "...", "item_id": "decision", "criterion_key": "stakes" | "reversibility" | "commitment_horizon" | "functions_involved", "value": 1-10}`; optional `owner_scorer_id` (must be one of the scorers).
- Returns: `result` (group composite and per-criterion view), `owner_view`, `sensitivity`, `trace` (with an input fingerprint). All numbers come back as strings.
- Rules the engine enforces: whole numbers 1 to 10; every scorer who appears must have every cell; reversibility counts inverted (11 minus the score).
- Pitfalls: the tool description says it returns `result_hash`; the code returns `trace.inputs_hash` instead (lane finding, reported to the improvement register). Do not cite a result hash. The value-driver scoring template is not reachable through this tool; do not call it with `nav.value_drivers`.

## catalogue_search (counted)

- Arguments: `pillar` `VD`; `level` 1, 2 or 3; `query` words from the goal; optional `limit` 1 to 25, `mode` (default fusion). Status defaults to Active.
- Returns rows with a spoken label (the row's name) and its code. Use the name; put the code in brackets only if needed.
- Pitfalls: do not pass `function` for the value driver pillar; it removes every row. Draft value themes are hidden by default; do not ask for them unless the person does.

## catalogue_list_children (counted)

- Arguments: the parent row's `id` (not its code) and the pillar.
- Returns the child rows one level down, through the catalogue's link tables.
- Pitfalls: a code such as "VD-01" is not looked up; search first, then pass the returned `id`. Seven level 3 drivers have no parent and never appear here.

## my_usage (free)

- Returns calls used, the monthly cap and the plan. Use it before a scoring run so a run does not stop half way.
