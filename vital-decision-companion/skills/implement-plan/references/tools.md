# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage implement, payload.roles.decide (or a stored DAI-I decide). Optional, stored as given: owner, first_milestone, key_actions, communication_plan, review_date, review_trigger, dependencies, resources, success_metrics, if_then_plans.

Returns: complete true when a decide name is present. Otherwise gaps: "implement required fields missing".

Pitfall: The v0.1 connector completes implement on a decide name alone. A plan without an owner, milestone, and review trigger is still incomplete for the person; say which are missing.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_daii_plan`
- `decision_premortem`
- `decision_status`

These tools stay on their own connector. This skill does not reimplement them.
