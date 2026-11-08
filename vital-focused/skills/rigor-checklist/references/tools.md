# Tools - rigor

## Default (no MCP)

| Action | CLI (from plugin `tools/`) |
|---|---|
| Start / load session | `session_init.py`, session JSON path |
| Patch stage fields | `session_patch_stage.py` |
| Options / matrix | `session_set_options.py`, `session_set_matrix.py` |
| Score ±10 | `score_tradeoff_offline.py` |
| Worksheet / brief | `render_worksheet.py`, `render_brief.py` |
| Gaps | `structural_decision_checks.py` |
| Handoff packet only | `format_handoff_packet.py --target navigator|verify` |
| Stamp | `stamp_focused_line.py --mode local --skill rigor-checklist` |

Say whether the model should **run** or **read** each CLI. Handle CLI errors without inventing data.

## Optional MCP (keys present + person asked)

- Decision Companion special services: cloud sync / export / `my_usage` with `vdec_`
- Navigator sealed tools with `vont_` after packet
- Verify claim tools with `vvfy_` after packet

Full tool names when calling MCP, e.g. `Decision Companion:decision_score` only on the opt-in path.
