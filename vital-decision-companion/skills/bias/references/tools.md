# Tool calls

## Companion slot

`decision_bias_check` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_bias_check

Arguments: optional decision_type, optional session_id.

Returns: risks (id, name, types, countermeasure) and draft true.

Pitfall: Saying "no material bias" is a clearance the tool does not return.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
