# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage learning_loop, payload.review_date, payload.success_signal, payload.authored_by (person). Optional and stored as given: payload.expected_outcome, payload.probability, payload.key_assumptions.

Returns: complete true only when review_date, success_signal, and authored_by are present. Otherwise gaps: "learning_loop required fields missing" (v0.1 does not name the field), or "refused: …" when authored_by is missing or an AI value.

Pitfall: Omitting authored_by makes v0.1 refuse the call with an AI-authored message even when no choice is being stored. Always send the person's name.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_attach_notes`
- `decision_status`

These tools stay on their own connector. This skill does not reimplement them.
