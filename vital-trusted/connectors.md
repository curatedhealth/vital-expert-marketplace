# Connectors

Offline first. Every TRUSTED skill runs from its method, references, templates and the plugin `tools/` suite. No live connector is required.

When a personal `vvfy_` key is pasted into this pack (`userConfig.verify_key`), Prove skills may call the **TRUSTED Prove live tools** over MCP. The wire URL remains `https://mcp.vital.expert/api/mcp/verify` (existing keys and metering). In this pack the MCP server id is `trusted-prove`.

**Do not install a separate `vital-verify` plugin.** That buyer pack is retired (8 November 2026).

| Connector / tool | Use for | Never for |
|---|---|---|
| Offline `tools/split_claims.py` | Splitting text into checkable claims with offsets | Deciding support |
| Offline `tools/claim_structure.py` + `passage_support.py` | Local claim-vs-passage structural and overlap checks | World-truth; remote search |
| Offline `tools/score_source_offline.py` + `identify_source_id.py` | Scoring / parsing identifiers when fields are supplied by hand | Fetching a URL or DOI |
| Offline `tools/faithfulness.py` + `stamp_check_line.py` | Counts, local faithfulness, check-lines | Pretending a live tool run |
| Offline `tools/format_citation.py` + `render_report.py` | Citations and report shapes from known fields/findings | Clearing a record |
| Live `qualify_source` | Resolving a DOI/PMID/URL/catalogue/document id into an admitted source | Inventing a source the caller did not name |
| Live `check_currency` | Retraction / correction / supersession / withdrawal signals | Grading claim support |
| Live `ingest_document` | Storing passages the caller may process | Shared index of third-party full text without attestation |
| Live `extract_claims` / `check_claim` / `verify_text` | Live claim split and passage support when a key is present | Replacing offline method when the key is absent |
| Live `build_citation` / `generate_report` / `build_evidence_table` / `build_record` | Live citation and export after findings exist | Clearing without a named human |
| Live `my_usage` | Remaining counted calls | Changing a finding |

## Rules

1. Anything that needs live data is a connector call and must be cited with access context.
2. Anything that runs offline is a script under `tools/` (or a skill `scripts/` wrapper).
3. When the key is absent, Prove skills still run and every result is labeled **not tool-checked**.
4. Never simulate a live tool status as if it were tool-returned (TR-H4).
5. One buyer pack: **vital-trusted**. Live tools attach here; there is no second method pack.

## Gaps

- No connector for company SOP stores or approved label databases.
- Patient-level identifiers are refused; de-identified or fictional inputs only.
- Currency of a hand-supplied source without `check_currency` is "not checked".
