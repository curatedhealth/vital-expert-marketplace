# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage (implement)

Arguments: session_id, stage implement. Required for complete: roles.decide (person). Optional: owner, first_milestone, review_date, review_trigger, communication_plan, key_actions, if_then_plans[] `{signal, owner, action}`, dependencies, resources, success_metrics.

Returns: complete when roles.decide is a named person. Warnings may include `optional_missing` for first_milestone and review_date — ask for them. Gap `role_only_name`: ask who the person is.

Pitfall: Completing on a decide name alone still leaves the plan thin for the person; ask for owner, milestone, and review trigger.

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Gap `role_only_name` | Ask for the person. Advise/Inform/Implement may keep role entries only if the person insists — say they stay unverified. When reading roles, accept string or `{name, status: "unverified_person"}`. |
| Warning `optional_missing` (first_milestone, review_date) | Ask for those fields. |
| if_then_plans | Send `[{signal, owner, action}]`. |
