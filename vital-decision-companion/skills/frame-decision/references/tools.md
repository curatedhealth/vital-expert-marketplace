# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage

Arguments: session_id, stage how_to_decide, payload.statement, payload.goal, payload.rigor (decide_quickly | tradeoff | dig_deep | full_process). Optional, stored as given: decider, deadline, core_issue, consequence, reversibility, authority_mode, criteria, values, assumptions.

Returns: complete true when statement, goal, and rigor are present. Otherwise gaps: "how_to_decide required fields missing" (v0.1 does not name the field). In v0.1 a rigor in the payload sets the session rigor.

Pitfall: Sending rigor before the person confirms it overwrites the session rigor with your suggestion.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_classify`
- `decision_rigor_guide`

These tools stay on their own connector. This skill does not reimplement them.
