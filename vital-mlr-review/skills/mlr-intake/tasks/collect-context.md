# Task: collect context

Collect markets, channel, artefact, authorized use.

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

1. Ask only for missing fields: `jurisdictions[]`, `audience`, `channel`, `artefact_version`, body or artefact id, `authorized_use_by_jurisdiction` (or single-market text), company SOP pointer if any.
2. If the user names one country, keep it as a one-element array — do not add US.
3. If the user says "global campaign" without markets, ask for the launch countries.
4. Call `vital-mlr-review:vital-mlr-review:mlr_intake` with the partial context when `vmlr_` is connected.
5. Report `missing_fields` and `ruleset_coverage` preview. Do not fill gaps with invented label text.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
