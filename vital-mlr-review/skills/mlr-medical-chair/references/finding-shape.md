# Medical finding shape

```json
{
  "rule_id": "US-PROMO-MED-001",
  "claim_span": "exact words from the draft",
  "severity": "critical|major|minor|info",
  "rationale": "why this fails the medical standard; cite source_ref",
  "source_ref": "SRC-US-02",
  "applies_to": ["US"],
  "fail_close": true,
  "chair": "medical",
  "gap": null
}
```

Severity guide: **critical** = inconsistent with labeled indication/safety or invented figure;
**major** = fair-balance or comparative evidence gap; **minor** = clarity; **info** = note for board.
