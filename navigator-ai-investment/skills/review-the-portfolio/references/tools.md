# Connector tools used by the Organizational Learning skills

Inputs read from the connector code at commit e23025f6e on the owner checkout (M). All need an open brief (`brief_id`). Checked live on 19 October 2026 (M, `eval-runs/LIVE_CONNECTOR_CHECK_2026-10-19.md`).

## value_range (already in use from Value-at-Stake Sizing)

- Stores the declared range: low, mid, high, unit, basis, measures (each with a baseline and an owner). The hosted path now keeps the fields (tools session build record).

## realized_value

- Input: `{"brief_id": "...", "realized": 1.1}`. Places the number against the stored range: below, inside or above. Returns `chooses: false`. Missing range or number: place "[GAP]".
- Pitfall: it does not check that the outcome was achieved, the unit, the period or the source. The skill checks those first (`scripts/realization_check.py` (in track-value-realized)).

## review_trace

- Input: `{"brief_id": "...", "activities": [{"id": "...", "decision": "stop" | "keep" | "fix", "reason": "...", "outcome_id": "...", "scale_note": "..."}]}`. Refuses a decision outside the three or no reason; "traces to none" when no outcome; a scale note on stop or fix is dropped with a gap.

## rescore_note

- Input: `{"brief_id": "...", "steward": "name, role"}`. Records who may re-score; `scores_changed: false`. Re-scoring itself is people scoring again with *Outcome Prioritization*.

## readiness_check

- Input: `{"brief_id": "...", "factors": [{"name": "...", "score": 1-10}]}`. Refuses an empty list, a nameless factor, a score outside whole numbers 1 to 10. Returns `index: null`.

## scaling_plan

- Input: `{"brief_id": "...", "payload": {"activity": "<id marked keep>", "what": "...", "owner": "...", "order": ["...", "..."]}}`. Refuses an activity not marked keep, or a missing what, owner or order.
