---
name: widen-options
description: "This skill should be used when the user asks to \"We only have two options. What is the warning?\", \"Add do nothing to the list we already named.\", \"What about doing it internally, if we say so?\". Do not use it to add an option the person did not say, to rate the list, or to pick a winner."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_widen_options when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-2.1"
  register_code: "DC-2.1"
  framework_path: "Decision Companion > Widen options"
  family: "widen-options"
  worker: "Decision coach (option list)"
  pack: vital-decision-companion
  version: 0.3.0
  route:
    - "we only have two options"
    - "add do nothing"
    - "doing it internally"
    - "don't invent a third option"
    - "widen the list we named"
    - "the favorite is not the list"
    - "fewer than three choices"
    - "store only what we said"
    - "an option is missing"
    - "missing option yourself"
---

# Widen options

Method DC-2.1. Primary tool `decision_widen_options`. Leave a missing field as `[GAP]`.

## How to do this work

Keep the list wide. Refuse to invent a third option to silence a warning. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Store the named options | The person named the options in their own words. | `tasks/store.md` |
| Ask about a missing option | The tool returned a warning that the list is narrow. | `tasks/warning.md` |

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

- Pass options as a list of objects with name. Empty names are refused.
- Warnings, not errors: fewer than 3 options; do-nothing missing; do-it-internally missing.
- If a warning is present, ask the person for that option. Do not insert one.
- The stage is complete when the stored list has at least three options.
- Ids may be omitted. The tool assigns opt-1 and onward.
- This skill does not rate and does not rank.

Primary tool: `decision_widen_options`. Also named, and not copied: `decision_run_stage`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: gather-intelligence when the rigor requires it; otherwise tradeoff or make-decision.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/store.md` | Store the named options |
| `tasks/warning.md` | Ask about a missing option |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
