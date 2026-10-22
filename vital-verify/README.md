# VITAL Verify

Install **VITAL Verify** from `curatedhealth/vital-expert-marketplace`, then paste a **per-user** `vvfy_` key. The key is not in this pack. Do not share one key across people — usage and abuse tracing are per key.

Invite / free beta: **100 counted tool calls lifetime** per personal key (locked 20 October 2026). `my_usage` and `build_citation` are free. Pro pricing comes later.

The connector is `https://mcp.vital.expert/api/mcp/verify`. Do not add a second connector.
If **vital-trusted** is already installed, it uses this same connector — paste the `vvfy_`
key there and skip installing this pack only for tools.

Seven skills: source grading, claim decomposition, support decision, currency check, honesty, escalation, and the record. Pick the one that matches the question. A missing field stays missing. A record with no human name is a draft.

## Happy path (customer model — required)

Verify does **not** auto-admit a loose URL list. That is intentional: it keeps fetch cost and exposure on sources the model explicitly qualifies.

**Design-partner script (must run once):** install **vital-trusted** → paste your personal `vvfy_` → `qualify_source` → `check_claim` → `my_usage`.

1. `qualify_source` with the identifier (DOI, PMID, URL, catalogue id, or ingested `document_id`) and the user `question`.
2. If the source is admitted, `check_claim` with the **admitted source object** plus a **quoted passage** (and locator).
3. `build_citation` for the reference line (free, not counted).
4. Use `my_usage` when you need remaining calls.

**Pasted text:** call `verify_text` with `sources: [{ "text": "…", "locator": "…" }]`. Verify auto-ingests that text for your tenant (7-day retention, label "supplied by you, provenance not checked", tier bronze). Internal ingest/qualify are not billed separately — one `verify_text` is one counted call.

`check_claim` with a passage alone → `not_checked` / reason `source not admitted` (it does not auto-ingest).  
`verify_text` with no admitted source and no paste → findings stay `not_checked`; faithfulness is `null` when every claim is `not_checked`.

Method skills still run when the key is absent; label the work **not tool-checked**.

Method version: `2026-10-22.1`.

## Publish to the buyer marketplace (operators)

Skills in this pack are a git symlink to `mcps/verify/manifest/skills`. Do **not** copy this folder with `rsync -a`, `cp -R`, Finder Compress, or `git archive` of the plugin alone — those ship a broken link and buyers install with zero skills.

Stage a materialised copy (no commit/push):

```bash
mcps/verify/scripts/sync-plugin-to-marketplace.sh --dest /path/to/vital-expert-marketplace
```

The script fails unless `vital-verify/skills` is a real directory with exactly seven `SKILL.md` files. Commit and push in the marketplace repo only after that gate passes.
