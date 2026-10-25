# Tool calls

## Companion slot

`decision_classify` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_classify

Arguments: statement (required), optional session_id, optional confirmed, confirmed_by.

Returns: draft type and rigor suggestion. Session decision_type is set only when confirm fields are accepted (or via run_stage with decision_type and type_confirmed_by).

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Host has confirmed / confirmed_by | Call `decision_classify {confirmed:true, confirmed_by}`. |
| Host lacks confirm fields but run_stage accepts decision_type | `run_stage how_to_decide {decision_type, type_confirmed_by}`. |
| Neither path available | Owner note "Type confirmed: <type> by <name>". Say bias card is unfiltered. |
| Claim type is set | Only when decision_status shows a non-null decision_type. |
