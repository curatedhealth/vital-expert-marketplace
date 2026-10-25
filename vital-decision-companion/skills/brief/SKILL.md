---
name: brief
description: "This skill should be used when the user asks to \"Compile what we stored into a draft brief.\", \"Don't sign the brief or add a signature block.\", \"The brief is still a draft until a person owns it.\". Do not use it to sign the brief, clear the decision, or fill a gap with prose."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_build_brief when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-7.1"
  register_code: "DC-7.1"
  framework_path: "Decision Companion > Brief"
  family: "record"
  worker: "Decision coach (drafter)"
  pack: vital-decision-companion
  version: 0.3.6
  route:
    - "compile what we stored"
    - "don't sign the brief"
    - "brief is still a draft"
    - "no prose we did not store"
    - "gaps stay visible"
    - "compile and stop"
    - "worksheet into a brief"
    - "unsigned decision record"
    - "leave the choice line blank"
    - "draft brief only"
---

# Brief

Method DC-7.1. Primary tool `decision_build_brief`. Store a missing field as `[GAP]` in the payload; say "not given yet" to the person.

## How to do this work

Compile what was stored. Refuse to sign. A brief with no human choice is still a draft. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Compile the draft | The person wants the stored session in one brief. | `tasks/compile.md` |

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

- Call decision_build_brief with session_id.
- A complete stage is rendered from its stored payload. An incomplete stage is the line [GAP].
- Do not rewrite a [GAP] into a plausible paragraph.
- watermark SIMULATED means practice. Say so at the top.
- The brief is a draft. It is not a signature and it is not clearance.
- Compile when the person asks, or when every stage required by the confirmed rigor is complete or explicitly skipped.

Primary tool: `decision_build_brief`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: The open stage, if the person wants to continue. Otherwise stop.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/compile.md` | Compile the draft |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
