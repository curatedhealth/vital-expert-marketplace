---
name: premortem
description: "Captures failure hypotheses and early signs before locking a choice (FOCUSED step E). Use when they ask what could go wrong. Do not give advice disguised as a premortem."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-4.2"
  register_code: "DC-4.2"
  framework_path: "Decision Companion > Pre-mortem"
  family: "make-decision"
  worker: "Decision coach (failure hypotheses)"
  pack: vital-focused
  version: "0.5.4"
  route: "look wrong in six months; capture the failure hypothesis; early signal for this failure; don't turn this into advice; keep the embarrassing failure; mitigation in our words; before we treat it as final; ways this fails; six month lookback; store the hypotheses and stop"
---

# Pre-mortem

Method DC-4.2. Primary tool `decision_premortem`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** E Examine ("How does this sit with your gut, what could go wrong, and who disagrees?").

## How to do this work

Ask what would make this decision look wrong in six months. Refuse to convert the list into advice. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Capture the hypotheses | The person is looking at how the choice could fail. | `tasks/capture.md` |

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

- Ask for failure, early signal, and mitigation. Leave a missing field out (never store [GAP]).
- Store the list with decision_premortem. Do not rank the hypotheses.
- Dig deep and full process require this list before the choice is treated as final.
- A hypothesis the person regrets saying stays on the list.
- The list does not set chosen_option.
- Six months is the prompt. If the person names another horizon, use theirs.

Primary tool: `decision_premortem`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: bias-card, then make-decision.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/capture.md` | Capture the hypotheses |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill premortem`
