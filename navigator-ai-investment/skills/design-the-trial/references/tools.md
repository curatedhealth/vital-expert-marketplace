# Connector tools used by the Execution skills

Connector: VITAL Ontology Navigator (`vital-ontology-navigator`). Your assistant may prefix the names. Counted calls draw on the key's allowance; check `my_usage` (free) first. Inputs below read from the connector code at commit e23025f6e on the owner checkout (M) and the tools session's build record. [CHECK on the live run: the new tools were not yet visible on Cowork's connector list on 19 October 2026]

All of them need an open brief (`brief_id` from `decide_start`). Without one, nothing is stored and the report carries the plan.

## sequence_check

- Input: `{"brief_id": "...", "steps": [{"id": "j1", "depends_on": "j0" | null, "capacity": "..."}]}`. `depends_on` is one step id.
- Refuses: an empty list; a step whose dependency is not placed earlier in the list; a step with no capacity. Stores the list; does not rank.
- Pitfall: one dependency per step. A step with several predecessors goes after all of them in the list, with the last one named; the report lists the rest. `scripts/delivery_check.py` checks every dependency.

## delegation_place

- Input: `{"brief_id": "...", "items": [{"id": "j1", "choice": "people_only" | "agent_with_review" | "agent", "regulated": true | false, "oversight_owner": "role", "context_of_use": "...", "review_on": "...", "review_question": "..."}]}`.
- Refuses: no choice; a choice outside the three; regulated work not people only (unless an exception is recorded in the person's words); no oversight owner. A missing review date or question is stored as a gap.
- Returns `decides: false`. Never speak the codes; say "people only", "agent with review", "agent".

## trial_note

- Input: `{"brief_id": "...", "payload": {"outcome": "...", "value": {"low", "mid", "high", "unit", "basis"}, "cost_to_test": {"low", "mid", "high", "unit", "basis"}, "measure": {"name", "baseline", "owner"}}}`.
- Refuses: no outcome; either range missing a field or a point; a measure without name, baseline and owner. Stores `declares_success: false`.
- Pitfall: the tool stores no target, stop rule, hypothesis or time limit. They live in the trial design report.

## methods_capability_gap

- Now runs the engine's 1 to 10 gap, but passes no outcome links, so every capability is weighted 1 (M). For an outcome-weighted register use *Strategic Readiness*' local script.

## Not available

- No tool for capability development plans or for the context-of-use statement: both live in the report.
- The operational maturity assessment is not built (pending owner rulings).
