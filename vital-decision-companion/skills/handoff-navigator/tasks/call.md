# Task DC-7.1 Call the Navigator tool

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (handoff). Does not choose the option and does not sign. |
| Workflow | Build the packet, map the cells, check the scale, call the Navigator tool, read the result, stop. |
| Skill | DC-7.1 Handoff to Navigator |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_handoff_navigator`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_handoff_navigator` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_handoff_navigator` with the session id.
2. Read the stored options, criteria, weights, and ratings from the session (`decision_status`, or the cells the person confirmed in this conversation). Map them as in `references/tools.md`.
3. Check the rating scale. If it is not 0 to 4, ask the person how to map it and record the answer before calling `methods_mcda_rank`.
4. Call the named tool on `vital-ontology-navigator` with a `vont_` key. If the key is absent, label the turn not tool-checked and stop.
5. Read the result back as Navigator's output. Say that the ranking informs the choice and that the named person still decides.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
