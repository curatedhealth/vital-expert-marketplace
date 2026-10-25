---
name: gather-intelligence
description: "This skill should be used when the user asks to \"What do we already know about this award?\", \"What is still unknown, and leave it unknown?\", \"Don't fill the unknown from memory.\". Do not use it to fetch literature, invent a market fact, or call Navigator or Verify itself."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_attach_notes when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-3.1"
  register_code: "DC-3.1"
  framework_path: "Decision Companion > Gather intelligence"
  family: "gather-intelligence"
  worker: "Decision coach (notes)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "what do we already know"
    - "what is still unknown"
    - "don't fill the unknown"
    - "attach this note"
    - "share is a gap"
    - "this note is a draft"
    - "knowns and unknowns"
    - "fact that would change our mind"
    - "no literature search here"
    - "don't invent the rate"
---

# Gather intelligence

Method DC-3.1. Primary tool `decision_attach_notes`. Leave a missing field as `[GAP]`.

## How to do this work

Write down what the person already knows and what would change their mind. Refuse to fill an unknown with a fact from memory. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Attach knowns and unknowns | The person stated a fact or an open question. | `tasks/notes.md` |
| Stop at the note | The person asks for a search, a score, or a claim check. | `tasks/boundary.md` |

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

- Notes source is owner, participant, or draft. Any other source is refused.
- A draft source is stored with draft true. Say the note is a draft.
- The stage completes only when payload has knowns and unknowns.
- An unknown stays [GAP] until the person or a handed-off tool supplies it.
- This skill does not call catalogue, literature, trials, or label connectors.
- When the person needs a score, name the handoff-navigator skill. When they need a claim checked, name handoff-verify.

Primary tool: `decision_attach_notes`. Also named, and not copied: `decision_run_stage`, `decision_handoff_navigator`, `decision_handoff_verify`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: handoff-verify or handoff-navigator when asked; otherwise premortem or tradeoff.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/notes.md` | Attach knowns and unknowns |
| `tasks/boundary.md` | Stop at the note |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
