# Check-line stamp

Every skill ends with one stamp line the person can paste into a work record.

CLI: `python tools/stamp_check_line.py` (from the plugin root, or with the tools path).

## Offline / method

```text
TRUSTED / <skill-id>: not tool-checked (offline tools) · <optional count summary>
```

Via:

```bash
python tools/stamp_check_line.py --mode offline --skill <skill-id>
python tools/stamp_check_line.py --mode offline --skill <skill-id> --extra "2 claims · gaps open"
```

Modes: `offline` · `local` · `method` · `verify`.

## Live Prove

```text
TRUSTED / <skill-id>: tool-checked via Prove live MCP · <optional count summary>
```

Via: `--mode verify --skill <skill-id>`

## Letter summary (trusted-check)

When aggregating letters, emit one line per active letter plus a closing stamp:

```text
T · substance: pass|flag|gap · …
R · claims/label: …
U · balance/framing: …
S · patient-safety: …
E · responsible: …
D · work-record: …
Stamp: TRUSTED / trusted-check: <tool-checked|not tool-checked>
```

Via:

```bash
python tools/stamp_check_line.py --letter-lines --mode offline \
  --letter 'T|grounded/sourced|flag|causal verb' \
  --letter 'R|claims/label|flag|press not substantiation' \
  --letter 'U|balance/framing|flag|absolute rates missing' \
  --letter 'S|patient-safety|pass|no treatment advice' \
  --letter 'E|responsible|pass|no PHI' \
  --letter 'D|work-record|gap|uncleared draft'
```

`--mode verify` sets the closing stamp to `tool-checked`; any other mode sets `not tool-checked`.

Letter codes: **T** Tangible · **R** Rule-compliant · **U** Unbiased · **S** Safe · **E** Ethical · **D** Defensible (True sits under T/Prove companions in the summary table).

`trusted-check` Output cards name this CLI; Build/Prove skills use the single-line `--mode` form.
