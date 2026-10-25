# Task DC-7.1 Call the Navigator tool

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (handoff). Does not choose the option and does not sign. |
| Workflow | Build the packet, prefer mcda_rank_args or build from cells, ask scale mapping, then call Navigator, stop. |
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

1. Call `decision_handoff_navigator` with the session id. Stop if `rater_issues[]` is present or any cell has a null or role-only rater.
2. Prefer `handoff.mcda_rank_args[]` when present: one `methods_mcda_rank` call per entry after any scale check the args still need.
3. **Cells only (v0.2):** build the per-rater `methods_mcda_rank` argument objects from `handoff.cells` (see `references/tools.md`), **show them to the person**, and ask the one scale-mapping question (for example 1–5 → 0–4). Say this order explicitly: build and show args → ask mapping → call only after they answer. Make no `methods_mcda_rank` call until the person answers. Always read `scale_note`. Never rescale silently.
4. Call the named tool on `vital-ontology-navigator` with a `vont_` key. If the key is absent, label the turn not tool-checked and stop.
5. Read the result back as Navigator's output. Say that the ranking informs the choice and that the named person still decides.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
