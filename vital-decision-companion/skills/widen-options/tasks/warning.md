# Task DC-2.2 Ask about a missing option

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (option list). Does not choose the option and does not sign. |
| Workflow | Read the warning, ask the person for the missing option, store only what they say, stop. |
| Skill | DC-2.2 Widen options |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_widen_options`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_widen_options` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Read the warning aloud in plain words.
2. If do nothing is missing, ask an open question: what happens if we do nothing for now? Never ask a yes/no question about adding an option. Store it only if the person names it.
3. If only two options exist and they are opposites (yes or no), say in plain words that a yes-or-no frame often hides a better path, and ask: what else could we do?
4. Ask the vanishing options question once: if every option on the list disappeared, what would you do?
5. Do not invent an option to clear the warning. If the person says there is none, record that answer as a note.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
