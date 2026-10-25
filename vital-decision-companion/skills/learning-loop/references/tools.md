# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage (learning_loop)

Arguments: session_id, stage learning_loop. Required: payload.review_date, payload.success_signal, payload.authored_by. Optional: probability (0–1), key_assumptions, what_happened, outcome_vs_process, lessons, assumption_to_change.

Do not send `expected_outcome` together with `success_signal` — `expected_outcome` is an alias of `success_signal` and they collide.

Returns: complete true only when review_date, success_signal, and authored_by are present. Otherwise gaps name the missing fields, or `refused:` when authored_by is missing or an AI value.

Pitfall: Omitting authored_by refuses the call. Sending both success_signal and expected_outcome collides.

## Also named

- `decision_attach_notes` (retro narrative)
- `decision_status`

## Connector version

| Condition | What to do |
|---|---|
| Alias collision on expected_outcome | Send `success_signal` only. |
| Gap `role_only_name` | Ask who is recording the review. |
| Retro results | Merge via run_stage with outcome_vs_process, lessons, assumption_to_change; plus an owner note. |
