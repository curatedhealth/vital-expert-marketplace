---
name: record-dissent
description: "This skill should be used when the user asks to \"Record that I disagree with this choice.\", \"Before we decide, does anyone object?\", \"Write down that nobody dissented, under my name.\". Do not use it to resolve the disagreement, to average views, or to change the choice."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_attach_notes when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-4.5"
  register_code: "DC-4.5"
  framework_path: "Decision Companion > Record dissent"
  family: "make-decision"
  worker: "Decision coach (dissent)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "record my dissent"
    - "does anyone object"
    - "nobody dissented"
    - "i disagree with the choice"
    - "minority view"
    - "disagree and commit"
    - "invite a dissent"
    - "devil's advocate"
    - "keep the objection on record"
    - "attest no dissent"
---

# Record dissent

Method DC-4.5. Primary tool `decision_attach_notes`. Leave a missing field as `[GAP]`.

## How to do this work

Invite dissent before the choice is final and keep it on record in the holder's words. Store dissent, or a named attestation that there is none, as a participant note on Make the decision. Never smooth a disagreement into consensus. Leave `[GAP]` rather than invent a holder or an objection.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Invite and capture dissent | Before or after the choice, someone may disagree. | `tasks/capture.md` |
| Attest no dissent | The person says nobody disagrees. | `tasks/attest.md` |

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

- Dissent is stored with decision_attach_notes on stage make_decision, source participant, text starting with "Dissent — holder: <name>".
- The holder's words are stored unchanged. Do not soften, summarise, or merge two people's objections.
- A dissent stays until the holder withdraws it. The decider may proceed; disagree and commit is recorded, not erased.
- No dissent is attested by a named person, not assumed from silence.
- For a governed record, name Navigator decide_record_dissent (vont_). This skill does not call it.

Primary tool: `decision_attach_notes`. Also named, and not copied: `decide_record_dissent`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision, or daii after the choice.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/capture.md` | Invite and capture dissent |
| `tasks/attest.md` | Attest no dissent |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
