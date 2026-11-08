---
name: gather-intelligence
description: "Records knowns, unknowns, and a disconfirming question (FOCUSED step U). Use when they ask what is known or still unknown. Do not invent facts from memory."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-3.1"
  register_code: "DC-3.1"
  framework_path: "Decision Companion > Gather intelligence"
  family: "gather-intelligence"
  worker: "Decision coach (notes)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "what do we already know; what is still unknown; don't fill the unknown; attach this note; share is a gap; this note is a draft; knowns and unknowns; fact that would change our mind; no literature search here; don't invent the rate"
---

# Gather intelligence

Method DC-3.1. Primary tool `decision_attach_notes`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** U Unknowns ("What do we know, and what is still unknown?").

## How to do this work

Write down what the person already knows and what would change their mind. Refuse to fill an unknown with a fact from memory. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Attach knowns and unknowns | The person stated a fact or an open question. | `tasks/notes.md` |
| Stop at the note | The person asks for a search, a score, or a claim check. | `tasks/boundary.md` |

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

- Notes source is owner, participant, or draft. Any other source is refused.
- A draft source is stored with draft true. Say the note is a draft.
- The stage completes only when payload has knowns and unknowns.
- An unknown stays in the unknowns list (never filled) until the person or a handed-off tool supplies it.
- This skill does not call catalogue, literature, trials, or label connectors.
- When the person needs their own weights and ratings added up, name the tradeoff skill (`decision_score`). Only if they ask for a sealed score on Ontology Navigator, name handoff-navigator. When they need a claim checked, name handoff-verify.

Primary tool: `decision_attach_notes`. Also named, and not copied: `decision_run_stage`, `decision_handoff_navigator`, `decision_handoff_verify`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: handoff-verify when asked; otherwise premortem or tradeoff-score.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/notes.md` | Attach knowns and unknowns |
| `tasks/boundary.md` | Stop at the note |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill gather-intelligence`
