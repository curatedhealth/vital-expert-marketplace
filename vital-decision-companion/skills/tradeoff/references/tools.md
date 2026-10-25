# Tool calls

## Companion slot

`decision_tradeoff_matrix` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_tradeoff_matrix

Arguments: session_id, criteria, ratings. Each rating that carries authored_by must name a person.

Returns: criteria, ratings, winner null, shared_tool pointing at methods_mcda_rank on vital-ontology-navigator.

Pitfall: Computing a weighted sum in the reply invents a second MCDA.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `methods_mcda_rank`

These tools stay on their own connector. This skill does not reimplement them.
