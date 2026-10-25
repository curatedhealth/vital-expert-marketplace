---
name: handoff-verify
description: "This skill should be used when the user asks to \"Check this claim against the passage. Not here.\", \"Is this supported? Send it to Verify.\", \"Don't mark it supported in this skill.\". Do not use it to mark a claim supported, to grade a source, or to copy Verify's seven method skills."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_handoff_verify when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-9.2"
  register_code: "DC-9.2"
  framework_path: "Decision Companion > Handoff to Verify"
  family: "handoff"
  worker: "Decision coach (verify handoff)"
  pack: vital-decision-companion
  version: 0.3.0
  route:
    - "check this claim"
    - "is this supported"
    - "don't mark it supported"
    - "verify packet"
    - "passage is missing"
    - "claim check belongs to verify"
    - "hand the sentence across"
    - "no support status here"
    - "quote the passage or stop"
    - "verify decides support"
---

# Handoff to Verify

Method DC-9.2. Primary tool `decision_handoff_verify`. Leave a missing field as `[GAP]`.

## How to do this work

List the claims and the next tools. Refuse to decide support. Verify's skills do that work. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Build the packet | The person wants a claim checked. | `tasks/packet.md` |
| Call Verify | The packet is ready and `vvfy_` is connected. | `tasks/call.md` |

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

- Call decision_handoff_verify with session_id and the claims the person listed. called_verify is false.
- next_tools are qualify_source and check_claim. Call them on vital-verify, in that order.
- check_claim needs the admitted source object and a quoted passage. A passage the coach wrote does not count.
- Without a vvfy_ key, say Verify is not connected. Do not invent a status.
- Do not restate source grading, claim decomposition, currency, honesty, or the Verify record. Those skills live in vital-verify.
- An unverifiable sentence stays out of the brief. It is not replaced with a guess.

Primary tool: `decision_handoff_verify`. Also named, and not copied: `qualify_source`, `check_claim`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: brief, with unsupported sentences left out.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/packet.md` | Build the packet |
| `tasks/call.md` | Call Verify |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
