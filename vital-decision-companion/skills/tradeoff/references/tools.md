# Tool calls

## Companion slot

`decision_tradeoff_matrix` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_tradeoff_matrix

Arguments: session_id, criteria `[{name, weight, direction}]`, ratings `[{option, criterion, value, rater}]`. Rater must name a person. Optional `scale` when not 1–5.

Returns: criteria, ratings, winner null, shared_tool pointing at methods_mcda_rank on vital-ontology-navigator. Per-cell gaps may include `invalid_cell`, `rater_missing`, `role_only_name`, `cell_replaced`.

Pitfall: Computing a weighted sum in the reply invents a second MCDA. Sending `score` instead of `value` rejects every cell.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`.

## Also named

- `methods_mcda_rank`

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Host accepts `scale` (v0.3) | Send `scale` only when the person declared a scale other than 1–5. |
| Host schema lacks `scale` (v0.2) | Tell the person ratings must use 1–5. Do not invent a rescale. |
| Gap `invalid_cell` / fields `['value']` | **Same turn:** resend corrected cells with `value` (not `score`). Tell which cell was fixed. Ask only if the value itself is unknown. |
| Gap `rater_missing` or `role_only_name` | Ask who rated the cell. Role titles are not enough. |
| Warning `cell_replaced` | Say the earlier cell was replaced and read the new value back. |
