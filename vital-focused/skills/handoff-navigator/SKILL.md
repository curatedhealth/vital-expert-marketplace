---
name: handoff-navigator
description: "Builds a Navigator handoff packet for optional sealed scores (FOCUSED step S). Use when they ask for a governed/sealed score. Do not claim a sealed result without vont_."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-9.1"
  register_code: "DC-9.1"
  framework_path: "Decision Companion > Handoff to Navigator"
  family: "handoff"
  worker: "Decision coach (navigator handoff)"
  pack: vital-focused
  version: "0.5.4"
  route: "score this on navigator; weighted rank elsewhere; hand the cells across; speak approach; don't compute mcda here; navigator packet; ontology score not ours; call navigator next; no rank in the companion; methods stay on navigator"
---

# Handoff to Navigator

Method DC-9.1. Primary tool `decision_handoff_navigator`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** S Score ("How do your options compare on your own weights, and does the top-ranked option still come first if one priority moves by up to 10 points?").

## How to do this work

Optional extra. Use this skill only when the person asks for the score on Ontology Navigator; otherwise `decision_score` on the Decision Connector adds up the same weights and ratings. Hand the cells across. Speak Approach. The Navigator stage id stays options. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Build the packet | The person asked for the score on Ontology Navigator and the cells are already stored. | `tasks/packet.md` |
| Call Navigator | The packet is ready and `vont_` is connected. | `tasks/call.md` |

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

- Call decision_handoff_navigator first. called_navigator is false. This connector does not call Navigator over HTTP.
- Speak Approach. suggested_stage_entry is options. compile_key is 4_options.
- Then call the named tool on vital-ontology-navigator: decide_start or a methods_* tool.
- methods_mcda_rank receives the same human cells, one call per rater.
- Without a vont_ key, say the shared tool is not connected.
- People supply scores. The coach does not.

Primary tool: `decision_handoff_navigator`. Also named, and not copied: `decide_start`, `methods_odi_score`, `methods_opportunity_score`, `methods_mcda_rank`, `methods_nav_compute`, `methods_scenario`, `methods_risk_tornado`, `methods_capability_gap`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision once a person states a choice. The rank is an input, not the choice.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/packet.md` | Build the packet |
| `tasks/call.md` | Call Navigator |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill handoff-navigator`
