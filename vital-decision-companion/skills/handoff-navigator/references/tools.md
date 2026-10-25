# Tool calls

## Companion slot

`decision_handoff_navigator` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_handoff_navigator

Arguments: session_id for the packet. Navigator tools keep their own arguments. Cells must already be human-authored.

Returns: handoff.product ontology-navigator, key_prefix vont_, spoken_layer Approach, suggested_stage_entry options. In v0.1 summary_markdown carries only the title, so build the Navigator call from the stored session yourself.

Pitfall: A second MCDA written in prose splits the formula from methods_mcda_rank.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

## Building the methods_mcda_rank call

Map the stored matrix, without changing any value:

| Decision Companion | methods_mcda_rank |
|---|---|
| each option (id, name) | `alternatives[]`: `{id, name, scores: {criterion: value}}` |
| each criterion weight | `criteria_weights`: `{criterion: weight}` (Navigator normalises) |
| a criterion where less is better (cost, risk, time) | list it in `negative_criteria` |

Scale check before the call. `methods_mcda_rank` accepts EVIDEM scores 0 to 4 only and returns a [GAP] for anything else. If the person rated on another scale (the Playbook grid uses 1 to 5), stop and ask how they want to map it. For example, 1–5 can map to 0–4 by subtracting 1. Record their answer. Never rescale silently, and never round a value.

Several raters: methods_mcda_rank takes one score per cell. Do not average raters here. Either send one rater's cells per call, or open the governed Navigator flow (`decide_start`, then `decide_attach_scores` per rater) where release and dissent are recorded.

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
