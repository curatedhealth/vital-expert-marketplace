# Task DC-2.1 Store the named options

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (option list). Does not choose the option and does not sign. |
| Workflow | Ask for the options, call `decision_widen_options`, store widening answers, confirm stage complete, stop. |
| Skill | DC-2.1 Widen options |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_widen_options`, `decision_run_stage`, `decision_status` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_widen_options` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask the person to name every option they are considering, in their words. Read the list back.
2. Call `decision_widen_options` with `options: [{name, notes}]` holding only those names. Never add an option to clear a warning.
3. Read each warning back in plain words. `too_few_options` means "2 of 3 options" (or fewer). Also: no do-nothing option, no do-it-internally option.
4. Ask one open widening question (never yes/no), chosen for what is missing; prefer the vanishing-options question first: What else could we do? What would we do if none of these were available (vanishing options)? What are we giving up by choosing any of these (opportunity cost)? Could we do two of these together? How have others in a similar situation decided (outside view)?
5. When the person answers a widening question, call `decision_run_stage` with `stage: widen_options` and `payload: {vanishing_options_answer}` or `{opportunity_cost}` or `{outside_view}` (and `{options}` when they named new ones). When they name a new option, also call `decision_widen_options` again with the full list.
6. Call `decision_status`. If widen is still incomplete with 3 or more options stored, call `decision_run_stage` once with `stage: widen_options` and `payload: {options}` so the stage completes.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
