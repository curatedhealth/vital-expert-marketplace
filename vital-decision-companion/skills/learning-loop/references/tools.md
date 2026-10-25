# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage learning_loop, payload.review_date, payload.success_signal.

Returns: complete true only when both fields are present. Otherwise gaps name the missing fields.

Pitfall: A relative date such as "next quarter" is stored only if the person said it. Do not convert it to a calendar day they did not choose.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
