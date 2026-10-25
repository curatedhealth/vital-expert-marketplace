# Tool calls

## Companion slot

`decision_export` (0.3.2+) returns the canonical stored record; prefer it over inferring from status alone.

`decision_status` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_status

Arguments: session_id.

Returns: stages, open_stage, rigor, decision_type, options, required_stages_unmet, daii_valid, complete_with_gaps, leverage, persistence. Prefer these over trusting a single stage flag.

Pitfall: daii_filled / stage complete flags can be stale. Cross-check options count for widen. Role-only names are not met.

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Prefer | required_stages_unmet, daii_valid, complete_with_gaps. |
| Widen flag vs options | Cross-check stored options (≥3). |
| Role-only name | Mark that item not met. |
| Brief ✓/✗/? marks | Evidence only, not a score. |
