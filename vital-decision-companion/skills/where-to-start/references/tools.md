# Tool calls

## Companion slot

`decision_start` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_start

Arguments: title (required), intent (one of quick, tradeoff, deep, full, classify_first), optional context.practice.

Returns: session_id, template, stage labels, persistence, durable_connected, watermark. Without intent: opened false and template_menu.

Pitfall: A missing title raises empty title. A missing intent does not open a session.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_status`
- `decision_run_stage`

These tools stay on their own connector. This skill does not reimplement them.
