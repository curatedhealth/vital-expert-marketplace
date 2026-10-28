# Task DC-4.6.1 Ask the gut check

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (gut check). Does not choose the option and does not sign. |
| Workflow | Show the computed view when the connector has it, ask the gut check in its own turn, stop. |
| Skill | DC-4.6 Gut check |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_status`; optional `decision_run_stage` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5, DC-H17, DC-H20. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call tools as in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Check that the grid is complete: options, what matters with weights, and the person's own ratings. If it is not, go back to the trade-off skill; do not ask the gut check on a half-filled grid.
2. With the connector: make sure the computed view and its robustness check have been shown (DC-H19, via the trade-off and Navigator hand-off skills). Then ask, as the only question in the reply: **"How does that computed result sit with your gut?"**
3. Without the connector: ask, as the only question in the reply: **"Weighing your own ratings by what matters most to you, which option comes out ahead, and does that match your gut?"** Do not compute the answer for them.
4. Read the reaction back in the person's words. If it names a mismatch, go to `tasks/mismatch.md` next turn. If gut and priorities agree, the next question is the key-assumption check for that option ("What has to be true for this to work, and has anyone checked it?").
5. Never ask "Which option are you leaning toward?" or "Which option do you choose?" in the same reply as the gut check.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
