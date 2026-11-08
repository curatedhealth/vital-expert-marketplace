# Check-line stamp

Every skill ends with one stamp line the person can paste into a work record.

## Offline / method

```text
TRUSTED / <skill-id>: not tool-checked (offline tools) · <optional count summary>
```

Via: `python tools/stamp_check_line.py --mode offline --skill <skill-id>`

## Live Prove

```text
TRUSTED / <skill-id>: tool-checked via Prove live MCP · <optional count summary>
```

Via: `--mode verify`

## Letter summary (trusted-check)

When aggregating letters:

```text
T · substance: pass|flag|gap · … 
R · claims/label: …
…
D · work-record: …
Stamp: TRUSTED / trusted-check: <tool-checked|not tool-checked>
```
