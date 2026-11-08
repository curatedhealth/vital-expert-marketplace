# Tools — citation-and-record

## Offline

| Tool | Path | Purpose |
|---|---|---|
| format_citation | `tools/format_citation.py` | Chicago / Vancouver / APA-ish lines from fields |
| render_report | `tools/render_report.py` | Brief / overview / evidence-table from local templates |
| stamp_check_line | `tools/stamp_check_line.py` | Record stamps |

Templates live under `tools/templates/` and skill `templates/`.

```bash
python3 tools/format_citation.py --title "..." --authors "Doe J" --year 2021 --style chicago
python3 tools/render_report.py --template verify-brief --input claims.json
```

## Live

`build_citation` / `generate_report` / `build_record` on VERIFY when connected. Clearance filing that needs a live record stays VERIFY-only.
