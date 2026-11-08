# Check-line stamp

Every skill close should emit one pasteable line for the work record.

```bash
python3 tools/stamp_check_line.py --skill <skill-id> --extra "gaps=N checks=M"
```

## Offline shape

```text
DD / <skill-id>: offline · UNSIGNED · <optional count summary> · not Marketplace Done
```

Modes: `offline` (default) · `method` (scripts ran) · `assemble` (IR only).
