# Task DC-0.1 Open the session

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (session opener). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_start`, read the result, ask one question, stop. |
| Skill | DC-0.1 Where to start |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_start`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_start` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask for a title when the person did not give one.
2. Ask for an intent when the person did not name one. Offer the five intents.
3. Call `decision_start` with that title and intent.
4. Read `stages` and name the first open stage in spoken words.
5. Stop. Do not open a second stage in the same turn.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
