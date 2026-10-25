# Tool calls

## Companion slot

`decision_handoff_navigator` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_handoff_navigator

Arguments: session_id for the packet. Navigator tools keep their own arguments. Cells must already be human-authored.

Returns: handoff.product ontology-navigator, key_prefix vont_, spoken_layer Approach, suggested_stage_entry options. Prefer `handoff.mcda_rank_args[]` when present (one `methods_mcda_rank` call per rater). Otherwise build from `handoff.cells`, `scale`, and `scale_note`. Always read `scale_note`. Stop if `rater_issues[]` is present or any cell has a null or role-only rater.

Pitfall: A second MCDA written in prose splits the formula from methods_mcda_rank. Never rescale silently.

## Building the methods_mcda_rank call

When `mcda_rank_args[]` is absent, map the stored matrix from `handoff.cells` without changing any value:

| Decision Companion | methods_mcda_rank |
|---|---|
| each option (id, name) | `alternatives[]`: `{id, name, scores: {criterion: value}}` |
| each criterion weight | `criteria_weights`: `{criterion: weight}` (Navigator normalises) |
| a criterion where less is better (cost, risk, time) | list it in `negative_criteria` |

Scale check before the call. `methods_mcda_rank` accepts EVIDEM scores 0 to 4 only and returns a [GAP] for anything else. Read `scale_note`. If the person rated on another scale (the Playbook grid uses 1 to 5), stop and ask how they want to map it to 0–4. Record their answer. Never rescale silently, and never round a value.

Several raters: one call per rater. Do not average raters here. Or open the governed Navigator flow (`decide_start`, then `decide_attach_scores` per rater) where release and dissent are recorded.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`.

## Connector version

| Condition | What to do |
|---|---|
| `handoff.mcda_rank_args[]` present | One `methods_mcda_rank` call per entry. |
| Only `handoff.cells` | Build calls from the table above. |
| `rater_issues[]` or null/role-only rater | Stop and ask who rated. |
| Always | Read `scale_note`; person chooses 0–4 mapping. |

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
