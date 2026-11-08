# MCP opt-in (vital-mlr-review + vital-verify)

Default `.mcp.json` is `{}` so buyers run offline-only with local `tools/` + `rulesets/`.

To enable connectors when you need metering, a durable cloud prep record, or live VERIFY, replace `.mcp.json` with:

```json
{
  "mcpServers": {
    "vital-mlr-review": {
      "type": "http",
      "url": "https://mcp.vital.expert/api/mcp/mlr-review"
    },
    "vital-verify": {
      "type": "http",
      "url": "https://mcp.vital.expert/api/mcp/verify"
    }
  }
}
```

Paste personal `vmlr_` / `vvfy_` keys when the host prompts.

Stamp `READY` / tool-checked only after a live `vmlr_` tool returns in-session. VERIFY live proof is optional; `mlr-verify-handoff` never implies VERIFY ran without `vvfy_`. Offline work stays labeled `READY-local` · `not tool-checked` · `not metered`.
