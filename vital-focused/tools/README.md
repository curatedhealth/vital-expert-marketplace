# FOCUSED offline tools

Deterministic Decision-connector replacement helpers. **No network imports.**

Run from this directory:

```bash
python3 -m unittest test_tools_suite.py -q
python3 session_init.py --root ../../../../../focused-sessions
```

| CLI | Purpose |
|---|---|
| `session_init.py` | Create `*.focused.json` |
| `session_patch_stage.py` | Merge stage payload |
| `session_set_options.py` | Store options |
| `session_set_matrix.py` | Store criteria / ratings |
| `score_tradeoff_offline.py` | Weighted totals + ±10 robustness |
| `render_worksheet.py` / `render_brief.py` | Markdown with `[GAP]` |
| `structural_decision_checks.py` | Missing frame/options/weights |
| `format_handoff_packet.py` | Navigator/Verify packet only |
| `stamp_focused_line.py` | `FOCUSED-local` / synced / method stamps |

Default session path: `./focused-sessions/<session_id>.focused.json` relative to the host cwd.
