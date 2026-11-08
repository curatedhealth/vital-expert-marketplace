# Rendered example: business update repair (sourced draft)

Invented teaching case only. Shape of a full bundle after `grounded-statements` repair: fixed
text, claim cards for invented figures, gap list, repair note, check-line stamp. Nothing invented
to fill gaps.

## Material supplied (excerpt)

Finance slide export, 30 September 2026: Q3 net sales USD 142M (vs USD 138M Q3 prior year);
operating margin 18.2% (vs 17.5%). No market-share figures. No patient numbers.

## Original draft (errors)

"Revenue grew 12% YoY to USD 158M. We now hold 24% market share in EU5. Enrollment in the
pivotal trial reached 4,200 patients."

## Fixed draft (person-facing)

> Q3 net sales were **USD 142M**, up from **USD 138M** in Q3 last year (**about 2.9%**).
> Operating margin was **18.2%** versus **17.5%** in the prior-year quarter.
>
> Market share in EU5: [GAP: not supplied — sales operations or IQVIA extract].
> Trial enrollment: [GAP: not supplied — clinical operations tracker].

## Claim cards (shared `../../templates/claim-card.md`)

### Claim 1
- **Draft:** "Revenue grew 12% YoY to USD 158M."
- **Supplied:** USD 142M vs USD 138M (~2.9%).
- **Status:** unsupported
- **Action:** Replaced with supplied figures; removed 12% and 158M.

### Claim 2
- **Draft:** "24% market share in EU5."
- **Supplied:** (silent)
- **Status:** invented
- **Action:** Removed; gap left — not estimated.

### Claim 3
- **Draft:** "Enrollment … 4,200 patients."
- **Supplied:** (silent)
- **Status:** invented
- **Action:** Removed; gap left.

## Repair note (`templates/repair-note.md`)

Grounding: what I changed and left open (draft, not yet reviewed)

Based on: finance slide export, 30 September 2026.

Changed
1. Three factual sentences replaced or removed; growth rate recomputed only from supplied
   pair (142 vs 138).

Left open
1. EU5 share and trial enrollment — ask clinical ops / sales analytics; do not guess.

Next step: leadership review; run `claim-assessment` when VERIFY is connected.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. EU5 market share — not in material — next: Sales operations / data vendor
2. Pivotal trial enrollment — not in material — next: Clinical operations

Not yet checked
- Tool-checked faithfulness (RAGAS) — not run; method-only pass
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / grounded-statements: not tool-checked (offline tools) · fabrication: 3→0 invented facts; figures: 1 recomputed from supply
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
True · fabrication: 3 unsupported facts removed (not tool-checked)
True · numbers: 1 growth rate aligned to supplied USD pair (not tool-checked)
```
