# Tool calls

## Companion slot

`decision_daii_plan` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_daii_plan

Arguments: session_id, roles: {decide, advise, inform, implement}. Values are display names.

Returns: roles and gaps. Empty decide is a gap.

Pitfall: Filling Decide with "the model" or "Decision Companion" fails the human-author rule.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_run_stage`

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Gap `role_only_name` on Decide | Ask who the person is. |
| Advise / Inform / Implement as role-only | Allowed only if the person insists; say unverified. |

