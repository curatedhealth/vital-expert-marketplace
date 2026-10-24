# Task: align chairs

Build conflict matrix across chairs and markets.

## Formula

| Slot | In this task |
|---|---|
| Worker | MLR compile lead. Does not approve copy and does not sign for the company. |
| Workflow | Follow the steps below; stop when the output asset is filled. |
| Skill | MLR-4.1 Compile |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | `vital-mlr-review:mlr_compile_checklist`, `vital-mlr-review:mlr_validate_packet`, `vital-mlr-review:mlr_get_packet_schema`; see the companion slot |
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

`scripts/validate_packet_shape.py`, `scripts/check_forbidden_phrases.py`

## Steps

1. Follow the skill Instructions for this task.
2. Fill the output asset.
3. Stop.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
