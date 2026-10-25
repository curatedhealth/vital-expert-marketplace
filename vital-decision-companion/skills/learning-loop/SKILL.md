---
name: learning-loop
description: "This skill should be used when the user asks to \"When do we review this choice?\", \"What signal would change it, if we named one?\", \"Don't invent a KPI we never stated.\". Do not use it to invent a metric, a date, or a target."
license: "[CHECK] VITAL Decision Companion terms, to be set by the owner"
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_run_stage when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-6.1"
  register_code: "DC-6.1"
  framework_path: "Decision Companion > Learning loop"
  family: "learning-loop"
  worker: "Decision coach (review)"
  pack: vital-decision-companion
  version: 0.2.0
  route:
    - "when do we review"
    - "what signal would change it"
    - "don't invent a kpi"
    - "store the review date"
    - "learning loop only"
    - "signal stays a gap"
    - "revisit in ninety days"
    - "who owns the review"
    - "don't backfill a metric"
    - "capture the after-action"
---

# Learning loop

Method DC-6.1. Primary tool `decision_run_stage`. Leave a missing field as `[GAP]`.

## How to do this work

Capture the review the person named. Refuse to invent a KPI. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Store the review | The person named a review date or a signal. | `tasks/review.md` |

## How deep to go

One worksheet. One question after it, when a person must answer. Then stop. Codes stay in the tool payload. Speak the stage label.

## Rules that hold for every task

These apply on every Decision Companion skill. Plain words go to the person. Ids stay here.

- **Only stored material counts (DC-H1).** Fields come from the person or from a tool result in this conversation.
- **Teaching material is never input (DC-H2).** Names and figures in `examples/` and `references/patterns.md` are invented for shape. Do not copy them into a live answer.
- **A worksheet is not a decision (DC-H3).** A matrix, a bias card, a type draft, and a brief do not choose the option.
- **Never simulate the connector (DC-H4).** Without `vdec_`, run the method by hand, label the turn **not tool-checked**, and do not invent a session id, a Verify status, or a Navigator score.
- **A named person decides (DC-H5).** `authored_by` is a human name. Values `ai`, `model`, and `assistant` are refused on choice fields.
- **No clinical, legal, or regulatory advice (DC-H6).**
- **Ask for what changes the answer (DC-H7).**
- **Plain language (DC-H8).** Speak stage labels. Keep stage ids in the payload.

Skill-specific:

- The stage completes only when review_date and success_signal are both present.
- If either is missing, store nothing for that field and write [GAP].
- Dates are spoken in full, such as 24 October 2026.
- full_process requires this stage. Other levels may skip it only when the person says so.
- The signal is their words. Do not translate it into a target they did not set.
- This stage does not change chosen_option.

Primary tool: `decision_run_stage`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

Next skill: brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/review.md` | Store the review |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
