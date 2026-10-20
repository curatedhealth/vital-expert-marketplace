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

`check_claim` with a passage alone → `unverifiable` by design.  
`verify_text` with a naive URL blob and no prior qualify → findings stay `unverifiable`. Prefer the qualify → check_claim loop unless the caller already has admitted sources / document ids.

Method skills still run when the key is absent; label the work **not tool-checked**.
