# Tool calls

## Companion slot

`decision_status` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_status

Arguments: session_id. Use it to confirm the grid is complete and to read the last computed view and robustness result before the gut check. Do not call it more than once every few turns (DC-H18).

## decision_run_stage (make_decision) — lean only

Optional: `lean: {option, by}` when the person states which option they lean toward. Never send `chosen_option` from this skill. Never send `replace: true`.

## Computed view

The computed view comes from Navigator `methods_mcda_rank`, reached through the trade-off and hand-off skills (DC-H19). This skill reads it; it never computes or re-orders options itself.
