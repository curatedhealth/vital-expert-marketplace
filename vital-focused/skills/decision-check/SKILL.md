---
name: decision-check
description: "Checks readiness from open gaps and unfinished steps before choice (FOCUSED step E). Use when they ask if they are ready to decide. Do not greenwash incomplete work."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-6.0"
  register_code: "DC-6.0"
  framework_path: "Decision Companion > Decision check"
  family: "brief"
  worker: "Decision coach (readiness check)"
  pack: vital-focused
  version: "0.5.4"
  route: "are we ready to decide; decision quality checklist; what is still missing; readiness check; before we commit; check the six elements; weakest link; quality check before the brief; did we consider enough options; is this decision ready"
---

# Decision check

Method DC-6.0. Primary tool `decision_status`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** E Examine ("How does this sit with your gut, what could go wrong, and who disagrees?").

## How to do this work

Check readiness against the Playbook's decision quality checklist before the brief or the choice. Mark each item met, not met, or not known, from stored fields and the person's answers only. Show the weakest of the six quality elements. Never compute a single quality score and never say the decision is good.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Run the checklist | Before the choice is recorded or the brief is compiled. | `tasks/check.md` |

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

- Read the session with decision_status. Mark an item met only when a stored field or the person's answer shows it.
- The Playbook checklist has five sections: framing, information, options, reasoning, action.
- Report counts per section and the items not met. The Playbook's thresholds are guidance, labeled as such; there is no validated single score.
- Name the weakest of the six decision quality elements: frame, alternatives, information, values and trade-offs, reasoning, commitment to action.
- This skill does not decide whether to proceed. The named person does.

Primary tool: `decision_status`. Also named, and not copied: `decision_build_brief`, `decision_rigor_guide`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: the skill for the weakest item, or brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/check.md` | Run the checklist |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill decision-check`
