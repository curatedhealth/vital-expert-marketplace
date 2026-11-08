# Rendered example: source card + currency not checked + stamp

Invented teaching case. Market-access draft cites one journal article and one press release.
VERIFY key absent — **not tool-checked**. Offline `score_source_offline.py` used for axes.

## Source card — primary (journal)

```text
┌─ Source card ──────────────────────────────────────
│ Title:     Outcomes after Velostra in NORLA (registry)
│ Publisher: Example Cardiology Journal
│ URL:       https://example.org/norla-velostra (teaching URL)
│ Kind:      Peer-reviewed journal article (registry analysis)
│ Can carry: Methods, rates, adjusted HR for admissions endpoint
│ Cannot:    Causal “cuts” language; label claims; other markets
│ Strength:  Observational registry; funded by Example Pharma
│ Currency:  Publication year 2023 — **currency not tool-checked**
│ Score:     Relevance 4 · Authority 4 · Currency 3 · Independence 2 ·
│            Traceability 4 · Total 17/25 (offline rubric)
│ Label:     not tool-checked
└────────────────────────────────────────────────────
```

## Source card — secondary (press)

```text
┌─ Source card ──────────────────────────────────────
│ Title:     Company press: “40% fewer admissions”
│ Publisher: Example Pharma IR
│ Kind:      Company press release
│ Can carry: Company messaging only — not substantiation for external HCP use
│ Cannot:    Stand alone as evidence for a claim (IFPMA 4.3 / ABPI 6.2)
│ Currency:  Dated 2024-03-01 — **currency not tool-checked**
│ Score:     Relevance 3 · Authority 2 · Currency 3 · Independence 1 ·
│            Traceability 2 · Total 11/25
│ Label:     not tool-checked
└────────────────────────────────────────────────────
```

## What the skill did

1. Qualified each URL/kind before any claim check.
2. Marked currency as not tool-checked (no live `check_currency`).
3. Downgraded press release for independence; kept journal for rates/HR only.
4. Did not invent a “strong evidence” verdict from the score total alone.

## Stamp

```text
TRUSTED / source-assessment: not tool-checked (offline tools) · 2 sources · currency not tool-checked · gaps open
```

**Why it works:** Separate cards, explicit can/cannot, offline score with axes, currency honesty, press release not treated as substantiation.


## Currency block (explicit)

```text
Currency: not tool-checked — publication year taken from citation metadata only.
Re-check with live check_currency when Prove MCP is connected.
```

## Method note

This example is a teaching fixture for known-answer evals. Names (Velostra, NORLA, Example Pharma) are fictional. Prefer shared cards under `../../templates/` when rendering scannable packs. Stamp lines match `templates/check-line-stamp.md`.
