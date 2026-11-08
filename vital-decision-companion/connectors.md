# Connectors (optional)

FOCUSED coaching, local session, score, and brief run with **no keys**.  
Default install ships an empty `.mcp.json`. Add servers only when you need the service below.

## Decision Companion (`vdec_`) - special services only

| Use for | Never for |
|---|---|
| Cloud durable session sync / export when the person asks | Everyday Frame→Decide coaching |
| `my_usage` / seat telemetry | Replacing local `score_tradeoff_offline.py` |
| Optional publish of a finished local session | Inventing stage fields the person did not supply |

Recipe - add to `.mcp.json`:

```json
"vital-decision-companion": {
  "type": "http",
  "url": "https://mcp.vital.expert/api/mcp/decision-companion",
  "headers": { "Authorization": "Bearer ${user_config.decision_key}" }
}
```

## Ontology Navigator (`vont_`) - sealed / governed scores

| Use for | Never for |
|---|---|
| `decide_*` / `methods_*` after `format_handoff_packet.py` | Ordinary local weighted score |
| ODI, tornado, capability gap when the person asks | Naming a winner for the person |

## Verify / TRUSTED Prove (`vvfy_`) - claim checks

| Use for | Never for |
|---|---|
| `qualify_source` then `check_claim` on supplied passages | Filling unknown facts from memory |
| Evidence admission the person requested | Replacing FOCUSED examine skills |

## Domain MCPs

Literature, trials, labels, HTA, commercial, and peers stay on their own connectors. FOCUSED may **name** them; it does not embed their clients.

## OAuth (platform - not in this pack)

Live MCP OAuth for Decision / Navigator / Verify is **parallel platform work**. Until that ships, optional connectors still use Bearer `userConfig` keys when the person opts in. Coaching never requires a key. Plan: `mcps/decision_companion/OAUTH_CONNECTORS_PLATFORM_PLAN_2026-11-08.md`.

