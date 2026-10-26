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
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_handoff_navigator` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_handoff_navigator` with the session id (skip if the packet is already in this conversation). If any cell has a null or role-only rater, stop and ask only: who gave those ratings? Do not raise anything else in that turn (missing cells and the scale come later). If `rater_issues[]` lists only `cell_missing`, name the missing cells and ask once whether to rate them or leave those alternatives out of that rater's call; never fill a value.
2. Prefer `handoff.mcda_rank_args[]` when each entry has usable `alternatives[].scores`. Scale check: if the ratings are already 0–4, or the person already chose a mapping earlier in this conversation, apply it and make one `methods_mcda_rank` call per entry this turn (never average raters). If no mapping has been chosen, show the args in full (one compact table per rater: alternatives × criteria with the stored values, unscaled, plus weights and which criteria are costs), ask the one mapping question, and call after the answer. A summary such as "two raters, three options" is not showing the args.
3. **No scores on `mcda_rank_args` (or cells only):** if args omit `alternatives[].scores`, or only `handoff.cells` is present, build per-rater `methods_mcda_rank` argument objects from `handoff.cells` (see `references/tools.md`). **Never invent scores.** Show the built args, ask the one scale-mapping question (for example 1–5 → 0–4), and say this order: build and show args → ask mapping → call only after they answer. Make no `methods_mcda_rank` call until the person answers. Always read `scale_note`. Never rescale silently.
4. Call the named tool on `vital-ontology-navigator` with a `vont_` key. If the key is absent, label the turn not tool-checked and stop.
5. Read the result back as Navigator's output. Say that the ranking informs the choice and that the named person still decides.
6. End every turn with exactly one question, the one that unblocks the next call. Keep other open points for later turns.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
