# Task: explain and route

Explain scope and route to the next skill.

## Formula

| Slot | In this task |
|---|---|
| Worker | Cross-functional MLR coordinator. Does not approve copy and does not sign for the company. |
| Workflow | Follow the steps below; stop when the output asset is filled. |
| Skill | MLR-0.0 Capability map |
| Knowledge | `references/knowledge.md`, `references/failure-modes.md` |
| Tool | No required tool. Optional catalogue via `mlr_list_rulesets_offline.py`. |
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

`scripts/check_forbidden_phrases.py`

## Steps

1. Follow the skill Instructions for this task.
2. Fill the output asset.
3. Stop.

## Output

The full `../../../templates/capability-map-card.md` — all 11 skill rows (this skill included) and the whole "Will never" block (TEH-RDY-039) — then the route for this request and the closing line.
