# Tool calls

## Companion slot

`decision_build_brief` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_build_brief

Arguments: session_id.

Returns: brief_markdown, brief_structured, watermark null or SIMULATED.

Pitfall: Filling [GAP] from earlier chat messages that were never stored writes a brief the session does not hold.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
