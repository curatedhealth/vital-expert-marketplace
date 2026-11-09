# Tools: mlr-channel-intent

## Offline first
Hybrid B default: run local CLIs under `plugin/vital-mlr-review/tools/` and `scripts/`.
Exit 0 = pass; 1 = hard rule error. Soft issues → flags / [CHECK] / [GAP].
Label **not tool-checked** when live MCP keys (`vmlr_`, `vvfy_`) are absent (MLR-H4).

| Tool | Path | Use for | Never for |
|---|---|---|---|
| `mlr_intake_offline.py` | `tools/mlr_intake_offline.py` | Read channel field from skeleton | Rewriting channel without human |
| `channel_intent_gate.py` | `tools/channel_intent_gate.py` | Classify intent from supplied fields; pass a named medium as `medium`; read `status` / `status_basis` (TEH-RDY-057/058); pass a described mix as `mixed_content` + `mixed_elements` and who will use it as `users`; read `mixed_content`, `provisional_label`, `questions` (TEH-RDY-061/062) | Reading a medium as an intent; using the bare `decision` as the answer's status |
| `stamp_ready_line.py` | `tools/stamp_ready_line.py` | Closing stamp line | Approval language |

## Live connectors (optional)
When `vmlr_` is present, MCP tools on server `vital-mlr-review` may mirror the offline CLIs.
When `vvfy_` is present, VERIFY handoff may be tool-checked. Never invent tool fields.
Always use fully qualified `vital-mlr-review:<tool>` names if calling MCP.

## Invocation rule
Offline first. Stamp every user-facing close with `python tools/stamp_ready_line.py --skill mlr-channel-intent --status <status>`.
Written 8 November 2026 (READY world-class content uplift).
