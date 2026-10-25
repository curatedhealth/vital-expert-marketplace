# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage make_decision, payload.chosen_option, payload.authored_by.

Returns: complete and gaps. The session choice stores option and authored_by.

Pitfall: Omitting authored_by lets the tool store owner. Ask for the name instead of relying on that default when the room has several people.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
