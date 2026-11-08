---
name: assign-daii
description: "Assigns Decide, Advise, Inform, and Implement to named people (FOCUSED step F). Use when they ask who decides vs advises or to set DAII roles. Do not name the AI as Decide."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-5.1"
  register_code: "DC-5.1"
  framework_path: "Decision Companion > DAI-I"
  family: "implement"
  worker: "Decision coach (roles)"
  pack: vital-focused
  version: "0.5.4"
  route: "who decides in the words of the room; who advises; who must be informed; four roles; don't put a model in decide; empty role stays empty; assign the names we gave; dai-i card; informed is not the decider; refuse an ai decider"
---

# DAI-I

Method DC-5.1. Primary tool `decision_daii_plan`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** F Frame ("What exactly are we deciding, who decides, and by when?").

## How to do this work

Write the names the person said into the four roles. Refuse to put a model in Decide. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Assign the four roles | The person named who decides, advises, inputs, or must be informed. | `tasks/assign.md` |

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

- roles.decide must be a display name the person gave. An empty decide returns the gap decide role empty.
- When reading advise/inform/implement, accept a string or `{name, status}`; print unverified_person entries as "<name> (unverified, role not person)".
- Do not assign ai, model, or assistant to any role.
- Do not invent a job title. If they gave a name, use the name. If they gave none, write owner not named and ask.
- Advise, Inform, and Implement may be empty. Say they are empty.
- Call decision_run_stage on implement with the same roles after the person confirms.
- The implement stage completes when roles.decide is non-empty.

Primary tool: `decision_daii_plan`. Also named, and not copied: `decision_run_stage`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: learning-loop when the rigor requires it; otherwise brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/assign.md` | Assign the four roles |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill assign-daii`
