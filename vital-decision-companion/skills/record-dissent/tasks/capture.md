# Task DC-4.5.1 Invite and capture dissent

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (dissent). Does not choose the option and does not sign. |
| Workflow | Invite one dissent, store it in the holder's words, stop. |
| Skill | DC-4.5 Record dissent |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_attach_notes`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_attach_notes` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Before the choice is recorded, invite dissent once: who sees it differently, and what would they say? Suggest the most junior voice speaks first, or that objections are written privately, so rank does not silence them.
2. If the room agrees fast on a high-consequence decision, ask one person to argue the strongest case against the leading option. Say this is a role, not their view.
3. For each dissent, ask for the holder's name and their words.
4. Call `decision_attach_notes` with `stage: make_decision`, `source: participant`, and `notes: "Dissent — holder: <name>. <their words>"`.
5. Read it back unchanged. Do not answer the objection on behalf of the room.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
