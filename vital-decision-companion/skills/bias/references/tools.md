# Tool calls

## Companion slot

`decision_bias_check` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_bias_check

Arguments: optional decision_type, optional session_id.

Returns: matched bias items (draft). May include stages[] and contested. On unknown_decision_type, returns valid_types — ask the person.

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Gap / code `unknown_decision_type` | Read valid_types; ask which type. |
| Pack returns stages[] and contested | Prefer tool items; keep contested label. |
| Empty card for a known type | Say the card has no entry for that type, not that no bias applies. |
