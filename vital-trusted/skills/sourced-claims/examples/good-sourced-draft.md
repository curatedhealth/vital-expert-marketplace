# Rendered example: payer slide claims after citation repair (sourced draft)

Invented teaching case ("Brand A", trials fictional). Fixed bullets, source note,
reference list, claim and source cards, gap list, check-line stamp. Citations name
supplied documents; they do not prove world-truth.

## Material supplied (excerpt)

ORION-4 registry report (internal, 30 June 2026 data cut): 1,850 adults; hospital
admission 12.0% Brand A vs 20.0% standard care (adjusted HR 0.60, 95% CI 0.48–0.75).
Company press release 14 March 2026 (announced topline only; no rates). No competitor
trial PDF.

## Fixed bullets (person-facing)

> - In the supplied ORION-4 registry (n=1,850; cut-off 30 June 2026), 12.0% of patients
>   on Brand A were admitted to hospital within 12 months versus 20.0% on standard care
>   (adjusted HR 0.60, 95% CI 0.48 to 0.75) (ORION-4 registry report, internal).
> - The company announced topline ORION-4 results on 14 March 2026; rates in this slide
>   come from the registry report you supplied, not the press release.
> - Versus Competitor B: [GAP: no head-to-head or indirect comparison study supplied —
>   next: supply study or remove comparison].

## Source note (`templates/source-note.md`, short header)

Sourced claims: what I cited, weakened, or left open (draft, not yet reviewed)

Based on: ORION-4 registry report (internal, 30 June 2026); press release 14 March 2026;
payer audience; Germany.

Cited from supplied material
1. Admission rates and HR — ORION-4 registry report, pages 12–14.
2. Announcement date only — press release 14 March 2026 (no efficacy numbers on that doc).

Weakened or removed
1. "Studies show fewer admissions" — replaced with named registry and figure.
2. "Leading treatment in class" — no source supplied; removed.

Next step: medical and market access review; substantiation on file per company process.

## Reference list (`templates/reference-list.md`, excerpt)

1. ORION-4 registry report, data cut-off 30 June 2026 (internal; supplied in conversation).
2. Brand A company press release, 14 March 2026 (supplied PDF; topline announcement only).

## Claim cards (shared `../../templates/claim-card.md`)

### Claim 1
- **Statement:** 12.0% vs 20.0% admissions; HR 0.60 (95% CI 0.48–0.75).
- **Passage:** ORION-4 registry report, §3.2, table 4 (supplied).
- **Status:** attributed to supplied passage (not world-truth verified here).

### Claim 2
- **Statement:** Company announced ORION-4 topline 14 March 2026.
- **Passage:** Press release headline and date (supplied).
- **Status:** attributed to supplied passage.

## Source cards (shared `../../templates/source-card.md`)

### Source 1
- **Document:** ORION-4 registry report (internal).
- **Can carry for payer:** observational efficacy rates with limitations stated; not
  registration-quality alone without reviewer sign-off.
- **Not checked:** current SmPC alignment (not tool-checked).

### Source 2
- **Document:** Press release 14 March 2026.
- **Can carry:** announcement timing; cannot carry numeric efficacy without full report.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. Competitor B comparison — no study supplied — next: Supply comparative evidence or drop claim

Not yet checked
- Whether registry report is the version approved for external payer use
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / sourced-claims: not tool-checked (offline tools) · claims: 3 cited, 1 gap; vague: 2 repaired; press release: not used for rates
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Sourced · every claim: 3 factual claims carry named source or gap, 1 gap open (not tool-checked)
Sourced · source type: press release not used for efficacy figures (not tool-checked)
Sourced · citations: 2 findable references from supplied docs (not tool-checked)
```
