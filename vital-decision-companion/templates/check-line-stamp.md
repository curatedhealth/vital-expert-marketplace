# Check-line stamp

Every skill ends with one stamp line.

```bash
python tools/stamp_focused_line.py --mode local --skill <skill-id>
python tools/stamp_focused_line.py --mode method --skill <skill-id>
python tools/stamp_focused_line.py --mode synced --skill <skill-id>
```

Modes: `local` (FOCUSED-local) · `method` / `offline` (not tool-checked) · `synced` (Decision MCP special service).
