# Tool calls

## Companion slot

`decision_attach_notes` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_attach_notes

Arguments: session_id, stage, notes, source (owner, participant, or draft).

Returns: stored_length and draft. The note text is stored on the stage.

Pitfall: Putting a model summary in notes with source owner records the model as the owner.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_run_stage`
- `decision_handoff_navigator`
- `decision_handoff_verify`

These tools stay on their own connector. This skill does not reimplement them.
