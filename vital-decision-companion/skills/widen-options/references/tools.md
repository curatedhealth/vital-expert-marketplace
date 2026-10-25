# Tool calls

## Companion slot

`decision_widen_options` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_widen_options

Arguments: session_id, options: [{name, optional id, optional notes}].

Returns: options list and warnings (too few options, missing do-nothing, missing do-it-internally). Warnings also appear on `decision_run_stage` for widen_options.

## decision_run_stage (widen_options)

Optional payload fields: options, vanishing_options_answer, opportunity_cost, outside_view.

## Connector version

| Condition | What to do |
|---|---|
| Gap `too_few_options` | Say how many of 3 are present. Ask for another option. Do not invent one. |
| Status shows widen incomplete with ≥3 options | Call `run_stage widen_options {options}` once (stage-flag stale). |
| Widening answers given | Store via run_stage fields vanishing_options_answer, opportunity_cost, outside_view. |
