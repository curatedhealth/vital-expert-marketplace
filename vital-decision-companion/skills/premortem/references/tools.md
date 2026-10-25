# Tool calls

## Companion slot

`decision_premortem` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_premortem

Arguments: session_id, hypotheses: `[{failure, early_signal, mitigation, owner, raised_by}]`. Never send `recommendation`.

Returns: stored hypotheses. Per-index refusals may include `recommendation_refused` or AI/role-only on raised_by/owner.

## Connector version

| Condition | What to do |
|---|---|
| Per-index refusal | Resend the batch without the refused item and tell the person. |
| Whole-batch drop (refusal code may read "a") | Same: drop the bad item and resend. |
| Never | Send `recommendation`. |
