# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage (make_decision)

Arguments: session_id, stage make_decision, payload `{chosen_option, authored_by}` required. Optional: rationale, confidence_pct, saying_no_to, trade_offs. Do not send `confidence` (wrong name). Leave dissent to record-dissent.

Returns: complete when chosen_option and authored_by are present. Gaps may include `stage_order`, `unknown_option`, `role_only_name`.

Pitfall: Sending confidence instead of confidence_pct drops the number. Sending replace:true wipes prior merge fields.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`.

## Connector version

| Condition | What to do |
|---|---|
| Gap `stage_order` | Name unmet stages. Ask: complete them now, or skip with `skip {stage, by: <person>, reason}`? |
| Gap `unknown_option` | Call `decision_status`, read stored options, ask which name matches. |
| Gap `role_only_name` | Ask who the person is. Do not store a role title. |
| Field `confidence_pct` | Always this name. Never `confidence`. |
