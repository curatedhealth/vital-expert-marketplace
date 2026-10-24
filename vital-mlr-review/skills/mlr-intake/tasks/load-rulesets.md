# Task: load rulesets

List and load rulesets for named markets.

## Formula

| Slot | In this task |
|---|---|
| Worker | MLR intake coordinator. Does not approve copy and does not sign for the company. |
| Workflow | Follow the steps below; stop when the output asset is filled. |
| Skill | MLR-0.1 Intake |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | `vital-mlr-review:mlr_intake`, `vital-mlr-review:mlr_list_rulesets`, `vital-mlr-review:mlr_get_ruleset`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. Imperative instructions. |
| Template | `assets/worksheet-output.md` |
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

1. Call `vital-mlr-review:vital-mlr-review:mlr_list_rulesets` filtered by audience/channel (free).
2. For each requested jurisdiction, note `full` vs `stub`.
3. Call `vital-mlr-review:vital-mlr-review:mlr_get_ruleset` with `jurisdictions[]` + audience + channel so `global` plus each market pack load together.
4. Show the user: pack ids, hashes, stub `[GAP]`s, and that chairs must use these `check_prompt`s — not invent other countries' procedures.
5. Hand off to chair skills or to `mlr-compile` if findings already exist.

## Never

- Substitute a full US pack when EU/UK/DE/CH was requested.
- Claim the ruleset "clears" the copy.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
