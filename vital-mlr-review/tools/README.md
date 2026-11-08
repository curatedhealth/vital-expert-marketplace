# Offline READY tools

Non-generative CLIs mirroring MCP `mlr_*` tools, plus pre-chair helpers. Run from this directory:

```bash
python3 mlr_intake_offline.py --help
python3 channel_intent_gate.py --args-json '{"channel":"scientific_exchange","proactive_or_reactive":"proactive","offlabel_or_unlicensed":"yes"}'
python3 mlr_claims_matrix_offline.py --help
python3 check_isi_presence.py --text 'Efficacy headline. Important Safety Information...'
python3 stamp_ready_line.py --skill mlr-intake --letter-lines
```

| CLI | Role |
|---|---|
| `mlr_*_offline.py` (9) | MCP parity (except `my_usage`) |
| `channel_intent_gate.py` | Promo / scientific exchange / med_info structural gate |
| `mlr_claims_matrix_offline.py` | Claims matrix + align merge |
| `check_isi_presence.py` | ISI / fair-balance heuristic scan |
| `check_submission_pack.py` | Submission-pack completeness; refuses 2253 filing fields |\n| `stamp_ready_line.py` / `render_board_pack.py` / `structural_mlr_checks.py` | Shared stamps |

Tests: `python3 -m unittest test_offline_tools -v`  
Forbidden scan: `python3 ../scripts/scan_forbidden_in_examples.py`

See plugin `references/mcp-opt-in.md` for optional live connectors.
