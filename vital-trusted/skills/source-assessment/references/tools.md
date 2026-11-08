# Tools — source-assessment

## Offline

| Tool | Path | Purpose |
|---|---|---|
| identify_source_id | `tools/identify_source_id.py` | Parse DOI / PMID / URL shape (no fetch) |
| score_source_offline | `tools/score_source_offline.py` | Score from supplied metadata only |
| stamp_check_line | `tools/stamp_check_line.py` | Check-lines |

```bash
python3 tools/identify_source_id.py --text "https://doi.org/10.1000/xyz" --json
python3 tools/score_source_offline.py --title "..." --publisher "..." --year 2020 --json
```

## Live (VERIFY)

`qualify_source` (fetch + admit) and `check_currency` remain VERIFY-only. Offline scoring never pretends a fetch happened.
