# Task: write medical findings

Emit medical chair packet JSON.

## Formula

| Slot | In this task |
|---|---|
| Worker | Medical reviewer (host-reasoner). Does not approve copy and does not sign for the company. |
| Workflow | Follow the steps below; stop when the output asset is filled. |
| Skill | MLR-M.1 Medical chair |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | `vital-mlr-review:mlr_get_ruleset`, `vital-mlr-review:mlr_align_claims`; see the companion slot |
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

`scripts/check_finding_shape.py`, `scripts/check_forbidden_phrases.py`

## Steps

1. Follow the skill Instructions for this task.
2. Fill the output asset.
3. Stop.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
