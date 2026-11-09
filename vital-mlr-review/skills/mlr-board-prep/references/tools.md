# Tools: mlr-board-prep

## Offline first
Hybrid B default: run local CLIs under `plugin/vital-mlr-review/tools/` and `scripts/`.
Exit 0 = pass; 1 = hard rule error. Soft issues → flags / [CHECK] / [GAP].
Label **not tool-checked** when live MCP keys (`vmlr_`, `vvfy_`) are absent (MLR-H4).

| Tool | Path | Use for | Never for |
|---|---|---|---|
| `mlr_build_prep_record_offline.py` | `tools/mlr_build_prep_record_offline.py` | Named-human prep record | AI as cleared_by |
| `stamp_ready_line.py` | `tools/stamp_ready_line.py` | Closing stamp line | Approval language |

### Where the offline prep record is written (TEH-RDY-023)
`mlr_build_prep_record_offline.py` (and `mlr_build_prep_record` in `tools/runtime.py`) writes `ready-sessions/<record_id>.ready.json` under the **current working folder**. There is no environment variable or argument for the output folder; to choose where the file lands, run the tool from that folder. The record also returns `local_path`. These files are local run output and are git-ignored by `mcps/mlr_review/.gitignore` (`ready-sessions/`).

## Live connectors (optional)
When `vmlr_` is present, MCP tools on server `vital-mlr-review` may mirror the offline CLIs.
When `vvfy_` is present, VERIFY handoff may be tool-checked. Never invent tool fields.
Always use fully qualified `vital-mlr-review:<tool>` names if calling MCP.

Qualified MCP names for this skill (call only when the key is present; otherwise run offline and label **not tool-checked**):
- `vital-mlr-review:mlr_build_prep_record` — primary
- `vital-mlr-review:mlr_validate_packet` — owned by another skill or connector; not reimplemented here

## Invocation rule
Offline first. Stamp every user-facing close with `python tools/stamp_ready_line.py --skill mlr-board-prep --status <status>`.
Written 8 November 2026 (READY world-class content uplift).
