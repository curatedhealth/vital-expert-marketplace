# Rendered example: confidence card + counts + stamp

Invented teaching case after claim-assessment returned statuses on three atomic claims.
VERIFY key absent — faithfulness arithmetic from offline counts only.

## Counts (from claim-assessment)

| Status | n |
|---|---|
| supported / found | 1 |
| partial / partly found | 1 |
| unsupported | 1 |
| contradicted | 0 |
| unverifiable | 0 |
| out_of_scope | 0 (excluded from denominator) |

Faithfulness % = (1 + 0.5×1) ÷ (1+1+1) = 1.5/3 = **50%** (whole percent).

## Confidence card

```text
┌─ Confidence ───────────────────────────────────────
│ Faithfulness:  50%
│ Formula:       (supported + 0.5×partial) ÷ (supported+partial+unsupported+contradicted+unverifiable)
│ Counts:        1 found · 1 partly · 1 unsupported · 0 contradicted · 0 unverifiable
│ Excluded:      0 out_of_scope
│ Meaning:       Word overlap with supplied passages — **not** a truth verdict
│ Live tools:    not tool-checked (offline)
│ Gaps:          1 unsupported claim still open — do not clear the pack
└────────────────────────────────────────────────────
```

## Stamp

```text
TRUSTED / confidence-scoring: not tool-checked (offline tools) · faithfulness 50% · 3 in denominator · gaps open
```

**Why it works:** Shows arithmetic, excludes out_of_scope, labels offline, refuses to treat 50% as “medium confidence of truth,” leaves gaps open.


## What not to say

- Do not say “50% confident the claim is true.”
- Do not round away the half-credit on partial.
- Do not include out_of_scope in the denominator.
- Do not print a confidence line when no claim statuses exist yet — run claim-assessment first.

## Worked second pack (all found)

Counts: 4 found, 0 other → faithfulness **100%**. Still **not tool-checked** if offline; still not a world-truth score; clearance remains a human step.

```text
TRUSTED / confidence-scoring: not tool-checked (offline tools) · faithfulness 100% · 4 in denominator · no claim gaps · clearance separate
```

## Method note

This example is a teaching fixture for known-answer evals. Names (Velostra, NORLA, Example Pharma) are fictional. Prefer shared cards under `../../templates/` when rendering scannable packs. Stamp lines match `templates/check-line-stamp.md`.

Accessed teaching date: 8 November 2026. Pilot release_state — not Released.
## Checklist echo
- [x] Rendered card(s) present
- [x] Stamp present
- [x] Offline / not tool-checked labeled when applicable
- [x] Gaps left open (no fake clearance)

See also: skill `references/method.md` and `references/method-standards.md`.
