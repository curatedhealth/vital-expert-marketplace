---
name: usecase-library
description: "Walks FOCUSED use-case cards without inventing case facts. Use when they ask for a worked example or UC card. Do not treat teaching material as live input."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-8.1"
  register_code: "DC-8.1"
  framework_path: "Decision Companion > Use-case library"
  family: "library"
  worker: "Decision coach (examples)"
  pack: vital-focused
  version: "0.5.4"
  route: "show me uc01; walk uc02; vendor card uc05; don't invent uc03; gold example only; which gold card fits; read the beats; unknown card stays empty; use the library not our session; teaching card"
---

# Use-case library

Method DC-8.1. Primary tool `decision_usecase_card`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** any. Worked examples show the seven steps (Frame, Options, Criteria, Unknowns, Score, Examine, Decide) in practice.

## How to do this work

Walk the beats of one gold card. Refuse to invent UC03 or to copy the example's choice onto the person's session. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Walk one gold card | The person names UC01, UC02, or UC05, or asks which card fits. | `tasks/walk.md` |

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

- Gold ids are UC01, UC02, and UC05. Any other id returns card null and the gold set.
- Walk beats in order. One beat, then a question.
- The card's decision_type and rigor are applied to the session only when session_id is passed and those fields are still empty.
- Do not treat a beat as the person's choice.
- leverage_packages name other connectors. This skill does not call them.
- Playbook content version is 2026-10-26.2.

Primary tool: `decision_usecase_card`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: where-to-start if they want a real session, using the card only as the walk.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/walk.md` | Walk one gold card |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill usecase-library`
