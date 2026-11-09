# Task DC-2.2 Ask about a missing option

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (option list). Does not choose the option and does not sign. |
| Workflow | Read the warning, ask the person for the missing option, store only what they say, stop. |
| Skill | DC-2.2 Widen options |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_widen_options`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_widen_options` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps with the plugin's local tools, or by hand when they cannot run. Do not label the reply. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Read the warning aloud in plain words.
2. If doing nothing is missing, ask it directly, as its own question: "What else could you do, including doing nothing?" Never ask a yes/no question about adding an option. Store an option only if the person names it.
3. If only two options exist and they are opposites (yes or no), say in plain words that a yes-or-no frame often hides a better path, without naming example options, and ask: what else could we do?
4. Only after the direct question above has been asked and answered, ask the vanishing options question once: if every option on the list disappeared, what would you do? It never replaces the direct question.
5. Do not invent an option to clear the warning. If the person says there is none, record that answer as a note.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
