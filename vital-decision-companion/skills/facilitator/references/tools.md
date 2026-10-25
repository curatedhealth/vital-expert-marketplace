# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage, payload. Choice payloads include authored_by as a human name.

Returns: complete, gaps. An AI author on a choice returns a gap and does not store the choice.

Pitfall: Calling Navigator or Verify from this skill skips the handoff skills.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_start`

These tools stay on their own connector. This skill does not reimplement them.
