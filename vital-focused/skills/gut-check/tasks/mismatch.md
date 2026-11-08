# Task DC-4.6.2 Follow a mismatch

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (gut check). Does not choose the option and does not sign. |
| Workflow | Name the mismatch neutrally, ask what the scores miss, store only what the person changes, stop. |
| Skill | DC-4.6 Gut check |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_status`; optional `decision_run_stage` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5, DC-H17, DC-H20. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call tools as in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Say the mismatch neutrally, using only the person's inputs: "Your own weights and ratings, added up, put B top-ranked, mainly on the thing you weighted most." Never say which is right.
2. Ask one question: **"What do your scores miss?"**
3. If the person changes a weight or a rating, read it back and store it in the trade-off grid (the trade-off skill's call), then show the recomputed view through the connector.
4. If the person keeps their instinct, read their reason back in their words and move on. Their reason is stored only as they said it (DC-H20).
5. When the person states a lean, store `make_decision.lean {option, by}` with `decision_run_stage` when the connector supports it, then ask the key-assumption question. A lean never completes the decision.

## Output

Match `templates/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
