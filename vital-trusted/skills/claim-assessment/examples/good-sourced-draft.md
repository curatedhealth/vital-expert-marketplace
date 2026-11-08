# Good example: claim cards against a registry (offline)

**Context:** Market access; Germany; product approved; payer deck draft. VERIFY key absent — **not tool-checked**.

**Draft sentence:** "Velostra cuts heart failure admissions by 40% in NORLA."

**Passage (supplied):** "Hospital admission for heart failure within 12 months occurred in 12.0% of patients on Velostra and 20.0% of patients on standard care (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75)."

## Claim card #1

```text
┌─ Claim #1 ─────────────────────────────────────────
│ Claim:     Velostra cuts heart failure admissions by 40% in NORLA
│ Status:    Partly found — relative reduction ~40% from rates 12% vs 20%, but draft says "cuts" (causal) and omits both rates and HR
│ Passage:   "12.0% … Velostra and 20.0% … standard care (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75)"
│ Locator:   supplied registry summary
│ Action:    Rewrite — use both rates + adjusted HR; observational wording; not "cuts"
│ Label:     not tool-checked
└────────────────────────────────────────────────────
```

## Evidence table (excerpt)

| # | Claim | Status | Passage | Action |
|---|---|---|---|---|
| 1 | cuts … by 40% | Partly found | 12% vs 20%; HR 0.60 | Rewrite |

## Gap list

1. Causal verb "cuts" — not in passage — Rewrite to association language (ABPI 6.1 / IFPMA 4.2).

## Stamp

```text
TRUSTED / claim-assessment: not tool-checked (offline tools) · 1 claim · 0 found · 1 partly · gaps open
```

**Why it works:** Atomic claim, quoted passage, plain-language status, explicit rewrite action, offline label, no invented certainty. Substantiation for external use remains a human/MLR step (IFPMA 4.3).
