---
name: record-dissent
description: "Invites and records disagreement in the person's words (FOCUSED step E). Use when they ask to capture dissent. Do not treat silence as consent."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-4.5"
  register_code: "DC-4.5"
  framework_path: "Decision Companion > Record dissent"
  family: "make-decision"
  worker: "Decision coach (dissent)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "record my dissent; does anyone object; nobody dissented; i disagree with the choice; minority view; disagree and commit; invite a dissent; devil's advocate; keep the objection on record; attest no dissent"
---

# Record dissent

Method DC-4.5. Primary tool `decision_attach_notes`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** E Examine ("How does this sit with your gut, what could go wrong, and who disagrees?").

## How to do this work

Invite dissent before the choice is final and keep it on record in the holder's words. Store dissent, or a named attestation that there is none, as a participant note on Make the decision. Never smooth a disagreement into consensus. Leave the field out ("not given yet") rather than invent a holder or an objection.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Invite and capture dissent | Before or after the choice, someone may disagree. | `tasks/capture.md` |
| Attest no dissent | The person says nobody disagrees. | `tasks/attest.md` |

## How deep to go

One worksheet. One question after it, when a person must answer. Then stop. Codes stay in the tool payload. Speak the stage label.

## Rules that hold for every task

<!-- shared:core:start -->
Hard rules (short core). Full DC-H1–H20 text: [`references/hard-rules.md`](references/hard-rules.md) - load when applying the decision-quality floor, connector repair, or closing sequence.

- **Person decides (DC-H3, H5, H17).** Never name a winner. Worksheets and scores are not the choice. `authored_by` is a human name. Never say what the numbers "support" or call an option best.
- **Only their material (DC-H1, H2, H12, H20).** No memory-fill. Teaching examples are never live input. Use the person's words only. Never describe stakes in words they did not use.
- **One question, then stop (DC-H9).** At most one ask per turn. Split compound asks across turns.
- **Honest tools (DC-H4, H13).** Prefer local session `tools/`. Without MCP do not invent session ids, scores, or Verify statuses. Say something is saved only after a tool result shows it. Stamp FOCUSED-local or not tool-checked.
- **Plain language (DC-H8, H15).** No tool names, stage ids, or `[GAP]` spoken to the person (say "not given yet"). Keep machinery backstage.
- **No clinical, legal, or regulatory advice (DC-H6).**
- **Gut check is its own turn.** Never combine it with a lean or choice question.
- **Decision-quality floor (DC-H16).** Before inviting the choice, follow the full checklist in `hard-rules.md`: frame, at least three options including nothing, evidence questions, weights and ratings, premortem, dissent, gut check alone, then lean, key assumption, choice. Pace and closing sequence live in the full file.
<!-- shared:core:end -->


Skill-specific:

- Dissent is stored with decision_attach_notes on stage make_decision, source participant, text starting with "Dissent, holder: <name>".
- The holder's words are stored unchanged. Do not soften, summarize, or merge two people's objections.
- A dissent stays until the holder withdraws it. The decider may proceed; disagree and commit is recorded, not erased.
- No dissent is attested by a named person, not assumed from silence.
- For a governed record, name Navigator decide_record_dissent (vont_). This skill does not call it.

Primary tool: `decision_attach_notes`. Also named, and not copied: `decide_record_dissent`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision, or daii after the choice.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/capture.md` | Invite and capture dissent |
| `tasks/attest.md` | Attest no dissent |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill record-dissent`
