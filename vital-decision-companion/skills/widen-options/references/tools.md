# Tool calls

## Companion slot

`decision_widen_options` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_widen_options

Arguments: session_id, options: [{name, optional id, optional notes}].

Returns: options with ids, warnings. The tool does not return a winner.

Pitfall: Sending a string instead of a list of objects raises empty names.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_run_stage`

These tools stay on their own connector. This skill does not reimplement them.
