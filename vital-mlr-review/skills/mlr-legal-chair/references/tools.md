# Tools: mlr-legal-chair

## Offline first
Hybrid B default: run local CLIs under `plugin/vital-mlr-review/tools/` and `scripts/`.
Exit 0 = pass; 1 = hard rule error. Soft issues → flags / [CHECK] / [GAP].
Label **not tool-checked** when live MCP keys (`vmlr_`, `vvfy_`) are absent (MLR-H4).

| Tool | Path | Use for | Never for |
|---|---|---|---|
| `check_finding_shape.py` | `scripts/check_finding_shape.py` | Finding object shape | Clinical dose calls |
| `check_forbidden_phrases.py` | `scripts/check_forbidden_phrases.py` | Never-approve phrases | Approving |
| `stamp_ready_line.py` | `tools/stamp_ready_line.py` | Closing stamp line | Approval language |

## Live connectors (optional)
When `vmlr_` is present, MCP tools on server `vital-mlr-review` may mirror the offline CLIs.
When `vvfy_` is present, VERIFY handoff may be tool-checked. Never invent tool fields.
Always use fully qualified `vital-mlr-review:<tool>` names if calling MCP.

Qualified MCP names for this skill (call only when the key is present; otherwise run offline and label **not tool-checked**):
- `vital-mlr-review:mlr_get_ruleset` — primary

## Invocation rule
Offline first. Stamp every user-facing close with `python tools/stamp_ready_line.py --skill mlr-legal-chair --status <status>`.
Written 8 November 2026 (READY world-class content uplift).
