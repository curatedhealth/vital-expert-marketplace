# Board pack shape

1. **Header:** artefact id/version, jurisdictions, audience, channel, product name.
2. **Authorized use map:** per-market label ref or `[GAP]`.
3. **Ruleset coverage:** full / stub / missing per market (from intake, or the packet's own supplied `ruleset_ids`); with both supplied, the binding or the specific gap intake returned (TEH-RDY-052); with audience or channel not supplied: "rule pack binds once audience and channel are supplied" (TEH-RDY-043).
4. **Chair summaries:** Medical · Legal · Regulatory (decision + top findings).
5. **Conflicts:** from `mlr_compile_checklist` slots.
6. **VERIFY notes:** admitted / not tool-checked / unverifiable omitted.
6b. **Residuals:** each residual with its acceptance exactly as the packet records it — "accepted by <name as recorded>" or "[GAP] no named human acceptance recorded" (TEH-RDY-053).
7. **Ask of the committee:** revise / gate / proceed to human SOP (never “approve via AI”).
8. **Liability line.**
