# Tool calls

## Companion slot

`decision_handoff_verify` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_handoff_verify

Arguments: session_id, claims. Prefer `claims[] {text, source_url, passage, raised_by}` when the person has them; plain strings otherwise.

Returns: handoff packet with `steps[]`. Follow steps: `qualify_source`, then `check_claim`. On `source_missing`, ask for the source. Never say supported without a qualified source and a check_claim result.

## Connector version

| Condition | What to do |
|---|---|
| Structured claims accepted | Send claims[] objects with text, source_url, passage, raised_by. |
| Strings only | Send claim strings; still follow qualify then check. |
| Gap `source_missing` | Ask for the source. Never say supported. |
