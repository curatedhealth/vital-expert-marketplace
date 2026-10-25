---
name: usecase-library
description: "This skill should be used when the user asks to \"Show me UC01, the competitive launch card.\", \"Walk UC02 beat by beat.\", \"Open the vendor card UC05.\". Do not use it to invent a fourth card or to treat the example as the person's decision."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_usecase_card when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-8.1"
  register_code: "DC-8.1"
  framework_path: "Decision Companion > Use-case library"
  family: "library"
  worker: "Decision coach (examples)"
  pack: vital-decision-companion
  version: 0.3.6
  route:
    - "show me uc01"
    - "walk uc02"
    - "vendor card uc05"
    - "don't invent uc03"
    - "gold example only"
    - "which gold card fits"
    - "read the beats"
    - "unknown card stays empty"
    - "use the library not our session"
    - "teaching card"
---

# Use-case library

Method DC-8.1. Primary tool `decision_usecase_card`. Store a missing field as `[GAP]` in the payload; say "not given yet" to the person.

## How to do this work

Walk the beats of one gold card. Refuse to invent UC03 or to copy the example's choice onto the person's session. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Walk one gold card | The person names UC01, UC02, or UC05, or asks which card fits. | `tasks/walk.md` |

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
- **Plain language (DC-H8).** Speak stage labels. Keep stage ids, tool names, field names and codes in the payload and out of the reply. Never say to the person: `[GAP]` (say "not given yet"), a tool name such as `decision_run_stage` or `methods_mcda_rank` (say "the companion" or "Navigator's ranking"), a code such as `role_only_name` (say "that's a group, not a person"), `stage_order` ("an earlier step isn't finished"), `cell_replaced` ("that rating replaced the earlier one"), "watermark SIMULATED" ("this is a practice session"), "skill", "not tool-checked" ("nothing has been saved"), or a stage id such as `make_decision`. When a refusal, gap or warning carries `message_for_person`, say that sentence (you may lightly adapt it, keeping its meaning). When `message_for_person` is absent (connector 0.3.1), translate the code with this list. Never print the code itself.
- **One question means one ask (DC-H9).** End the turn with at most one question. "Who rates Cost, and did they score privately?" is two asks; so is "who, and is it Agency A?". Ask the one that unblocks the next store and keep the rest for later turns.
- **Merge, never replace (DC-H10).** To update a stage, send only the changed fields. Never send `replace: true` unless the person explicitly asks to wipe and rewrite that stage.
- **Fix it now when the fix is mechanical (DC-H11).** When the connector returns a code whose fix uses only what the person already said (for example `rigor_unchanged` → resend as `change_rigor {to, by, reason}`; `invalid_cell` on `score` → resend with `value`), resend in the same turn and say what changed. Ask only for input that is genuinely missing.
- **No completed guesses (DC-H12).** Never fill in what the person did not say. A date without a year, or a month, season or phrase ("end of March", "Q1") used as a deadline or review date, is asked about before it is stored as a date. A first name only for a person field is stored exactly as said (for example "Tom"), marked as name incomplete, and asked about once; never completed and never dropped. An option that does not match a stored one is asked about.
- **Report only what came back (DC-H13).** Say something is saved, recorded or on file only after a tool result shows it. On a refusal, change the input (when DC-H11 applies) or ask; never resend the same call unchanged. When no connector is present, say plainly that nothing has been saved and what the person should record.
- **Optional fields never block (DC-H14).** Reasons, confidence, trade-offs and other optional fields are invited once, never required. Read back and store what the person gave; an optional field that is still missing stays "not given yet".

Skill-specific:

- Gold ids are UC01, UC02, and UC05. Any other id returns card null and the gold set.
- Walk beats in order. One beat, then a question.
- The card's decision_type and rigor are applied to the session only when session_id is passed and those fields are still empty.
- Do not treat a beat as the person's choice.
- leverage_packages name other connectors. This skill does not call them.
- Playbook content version is 2026-10-24.1.

Primary tool: `decision_usecase_card`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: where-to-start if they want a real session, using the card only as the walk.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/walk.md` | Walk one gold card |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
