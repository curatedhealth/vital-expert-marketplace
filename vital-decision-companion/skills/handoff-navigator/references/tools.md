# Tool calls

## Companion slot

`decision_handoff_navigator` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_handoff_navigator

Arguments: session_id for the packet. Navigator tools keep their own arguments. Cells must already be human-authored.

Returns: handoff.product ontology-navigator, key_prefix vont_, spoken_layer Approach, suggested_stage_entry options.

Pitfall: A second MCDA written in prose splits the formula from methods_mcda_rank.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decide_start`
- `methods_odi_score`
- `methods_opportunity_score`
- `methods_mcda_rank`
- `methods_nav_compute`
- `methods_scenario`
- `methods_risk_tornado`
- `methods_capability_gap`

These tools stay on their own connector. This skill does not reimplement them.
