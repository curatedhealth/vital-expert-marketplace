# Tool calls

## Companion slot

`decision_premortem` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_premortem

Arguments: session_id, hypotheses: `[{failure, early_signal, mitigation, owner, raised_by}]`. Optional (0.3.2+): `remove_index` or `replace_index` (+ hypothesis), each with `by` (a person). Never send `recommendation`.

Returns: stored hypotheses. Per-index refusals may include `recommendation_refused` or AI/role-only on raised_by/owner.

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Per-index refusal | Resend the batch without the refused item and tell the person. |
| Whole-batch drop (refusal code may read "a") | Same: drop the bad item and resend. |
| Wrong / blank row the coach created | Offer `remove_index` with `by` = the person; never remove without their say. |
| `unknown_fields` warning | Drop the unknown key; resend or ask. |
| Never | Send `recommendation`. |
