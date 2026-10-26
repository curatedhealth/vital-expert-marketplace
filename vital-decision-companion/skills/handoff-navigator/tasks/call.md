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
2. Prefer `handoff.mcda_rank_args[]` when each entry has usable `alternatives[].scores`. Scale: ratings already 0–4 are used as is; a 1–5 scale maps to 0–4 by subtracting 1 (linear, order-preserving); say this in one clause and call now, one `methods_mcda_rank` call per rater (never average raters). Criteria the person marked lower-is-better go in `negative_criteria` only if their ratings are raw amounts; if the person already rated them so that higher is better, do not mark them negative. Ask about the scale only when it is neither 0–4 nor 1–5.
3. **No scores on `mcda_rank_args` (or cells only):** if args omit `alternatives[].scores`, or only `handoff.cells` is present, build per-rater `methods_mcda_rank` argument objects from `handoff.cells` (see `references/tools.md`). **Never invent scores.** Apply the same scale rule as step 2 and state the mapping in one clause. Always read `scale_note`. Never rescale silently.
4. Call the named tool on `vital-ontology-navigator` with a `vont_` key. If the key is absent, label the turn not tool-checked and stop.
5. Re-run once with the heaviest weight moved 10 points to the next criterion. Read both results back as Navigator's output: each option's score, the gap between the top two, and whether the order holds. Say the ranking informs the choice and the named person decides; ask whether it matches their judgement and, if not, what the scores miss.
6. End every turn with exactly one question, the one that unblocks the next call. Keep other open points for later turns.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
