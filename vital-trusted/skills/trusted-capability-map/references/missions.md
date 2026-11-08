# Missions (CF02 map)

TRUSTED is a capability map (CF02), not a single task skill. Missions below are the
stable intents a buyer or steward routes through this map. Each mission lands on one or
more CF04 skills.

| Mission id | Intent | Primary skills | Autonomy |
|---|---|---|---|
| M-ROUTE | Explain TRUSTED / pick a skill | trusted-capability-map | Auto: route table. HITL: letter on/off. |
| M-INTAKE | Gather context before drafting | trusted-intake | Auto: ask missing fields. HITL: confirm audience/market. |
| M-BUILD | Draft under active letters | letter Build skills (12) | Auto: apply hard rules. HITL: never invent; stop on safety/ethics gates. |
| M-CHECK | Score a finished draft | trusted-check + letter skills | Auto: checklist. HITL: present options; no clearance. |
| M-PROVE-OFFLINE | Fact-check / source / confidence / cite without a Verify key | Prove skills + `tools/` | Auto: offline suite. Label **not tool-checked**. |
| M-PROVE-LIVE | Same with live fetch/currency | Prove skills + TRUSTED Prove live MCP (`trusted-prove`) | Auto: call live tools. HITL: never clear for external use. |

## Offline vs live Prove

| Path | When | Tools | Label |
|---|---|---|---|
| Offline | No `vvfy_` key / air-gapped | `plugin/vital-trusted/tools/*` | Every support status and score line: **not tool-checked** |
| Live | Key pasted into vital-trusted | qualify_source, check_currency, ingest_document, plus offline suite for structure | Tool statuses allowed only when the tool ran |

See `../../connectors.md` and Prove skills' `references/without-verify.md`. The `vital-verify` plugin is retired.
