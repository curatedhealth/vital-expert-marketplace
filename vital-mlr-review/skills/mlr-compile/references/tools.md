# Tools: mlr-compile

## Offline first
Hybrid B default: run local CLIs under `plugin/vital-mlr-review/tools/` and `scripts/`.
Exit 0 = pass; 1 = hard rule error. Soft issues → flags / [CHECK] / [GAP].
Label **not tool-checked** when live MCP keys (`vmlr_`, `vvfy_`) are absent (MLR-H4).

| Tool | Path | Use for | Never for |
|---|---|---|---|
| `mlr_validate_packet_offline.py` | `tools/mlr_validate_packet_offline.py` | Packet schema | Board ownership |
| `mlr_compile_checklist_offline.py` | `tools/mlr_compile_checklist_offline.py` | Open-item checklist | Hiding gaps |
| `mlr_align_claims_offline.py` | `tools/mlr_align_claims_offline.py` | Align pass | Clearance |
| `mlr_get_packet_schema_offline.py` | `tools/mlr_get_packet_schema_offline.py` | Schema dump | Live MCP require |
| `stamp_ready_line.py` | `tools/stamp_ready_line.py` | Closing stamp line | Approval language |

## Live connectors (optional)
When `vmlr_` is present, MCP tools on server `vital-mlr-review` may mirror the offline CLIs.
When `vvfy_` is present, VERIFY handoff may be tool-checked. Never invent tool fields.
Always use fully qualified `vital-mlr-review:<tool>` names if calling MCP.

## Invocation rule
Offline first. Stamp every user-facing close with `python tools/stamp_ready_line.py --skill mlr-compile --status <status>`.
Written 8 November 2026 (READY world-class content uplift).
