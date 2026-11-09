# Task: load rulesets

List and load rulesets for named markets.

## Formula

| Slot | In this task |
|---|---|
| Worker | MLR intake coordinator. Does not approve copy and does not sign for the company. |
| Workflow | Follow the steps below; stop when the output asset is filled. |
| Skill | MLR-0.1 Intake |
| Knowledge | `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Default: `python ../../tools/mlr_intake_offline.py` (+ list/get ruleset offline CLIs). Optional live `vital-mlr-review:mlr_intake` when `vmlr_` present; see `references/tools.md` / `without-connector.md`. |
| Prompt | Use only fields the person supplied or the tool returned. Imperative instructions. |
| Template | `../../templates/` Output cards (see SKILL.md) |
| Input | The person's words, prior packet fields, and tool results in this conversation. |
| Governance | MLR-H1–H8, `references/governance.md`. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vmlr_` connected | Call primary tools with `vital-mlr-review:tool_name` from `references/tools.md`. |
| `vmlr_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |
| `vvfy_` (when named) | Call `vital-verify:tool_name`. Do not add a second claim checker. |

## Scripts

`scripts/check_jurisdictions.py`, `scripts/check_forbidden_phrases.py`

## Steps

0. Run this task only after the person has named markets. If none are named, go back to `collect-context.md` step 3a — do not list available jurisdictions.
0b. Run steps 1–4 only when audience and channel are also supplied (or explicitly derived from supplied evidence, said so). Otherwise write "rule pack binds once audience and channel are supplied" per supplied market (only while one of them is missing — once both are supplied, report the tool's binding or its specific gap, such as `[GAP] no rule pack for intent <intent> in <market>`, TEH-RDY-052), ask for them, and stop (TEH-RDY-043).
1. Call `vital-mlr-review:mlr_list_rulesets` filtered by audience/channel (free).
2. For each requested jurisdiction, note `full` vs `stub`.
3. Call `vital-mlr-review:mlr_get_ruleset` with `jurisdictions[]` + audience + channel so `global` plus each market pack load together.
4. Show the user: pack ids, hashes, stub `[GAP]`s, and that chairs must use these `check_prompt`s — not invent other countries' procedures.
5. Hand off to chair skills or to `mlr-compile` if findings already exist.

## Never

- Substitute another market's full pack (for example a US pack) for a market the person requested.
- Claim the ruleset "clears" the copy.
- List or suggest specific jurisdictions from the registry when the person named none.

## Output

Match `../../templates/` Output cards (see SKILL.md). Then the closing line.
