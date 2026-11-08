# Rendered example: UK HCP email repair (sourced draft)

Invented teaching case only ("Product Z"). Shape of a full bundle after `market-rules-and-data`
repair: jurisdiction named, statements list, market note, gap list, check-line stamp.

## Context

- **Jurisdiction:** United Kingdom (ABPI Code 2024 applies as usual practice).
- **Reader:** Hospital doctors (promotional email).
- **Material supplied:** US slide deck text pasted into draft ("FDA-approved", no PI link);
  draft job code typed as "TBC"; patient surname in case vignette.

## Fixed email excerpt (person-facing)

> Subject: Product Z — updated efficacy summary for hospital use (UK)
>
> [Body uses only claims supported by the UK SmPC excerpt the person supplied.]
>
> Product Z (INN placeholder per SmPC) is indicated for …
>
> **Prescribing information:** [GAP: single-click PI link or full PI text — supply from your
> approval system]
>
> **Date created or last revised:** [GAP: not supplied — supply from MLSR]
>
> **Adverse events:** Adverse events should be reported. Reporting forms and information can
> be found at https://yellowcard.mhra.gov.uk/. Adverse events should also be reported to
> [GAP: company reporting line — supply from medical information]
>
> **Job code:** [GAP: approved job code — supply from promotional review]

Case vignette: generalized to "a hospital patient" — identifiers removed (see privacy note).

## Statements list (`templates/statements-list.md`, UK)

| Statement | Status |
|---|---|
| Prescribing information (Cl. 12) | GAP — person must supply link or text |
| Date of preparation / revision (Cl. 12.4) | GAP |
| Adverse event reporting (Cl. 12.6) | Wording in place; company line GAP |
| Non-proprietary name with brand (Cl. 12.4) | From supplied SmPC excerpt |
| Job / material code | GAP |
| Black triangle if required | [CHECK] — confirm with PI |

## Market note (`templates/market-note.md`, short header)

Market and statements (draft, not yet reviewed)

Written for: **United Kingdom**, hospital doctors, promotional email, from supplied SmPC
excerpt and US deck (US-only claims removed).

Changed for the market
1. "FDA-approved" removed — wrong jurisdiction for UK readers; replaced with UK marketing
   authorization wording only where SmPC supports it.

People
Personal identifiers removed from the case vignette; details not repeated in this note.

Next step: your promotional review process for the UK before send.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. PI link or embedded PI — UK MLSR — next: Supply from approval system
2. Job code — next: Supply from promotional review
3. Company adverse-event reporting line — next: Medical information
4. Date of preparation — next: Supply from MLSR

Not yet checked
- Whether black triangle applies — confirm on PI
```

## Privacy note (`templates/privacy-note.md`)

One case vignette held a patient surname and ward; both were removed from the draft output.
Whether the vignette may be used at all is for your privacy function.

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / market-rules-and-data: not tool-checked (offline tools) · jurisdiction: US→UK; statements: 4 gaps; privacy: 1 vignette scrubbed
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Market · jurisdiction: 1 US-only approval phrase removed for UK (not tool-checked)
Market · statements: 4 expected items open (not tool-checked)
Market · privacy: 1 identifiable vignette generalized (not tool-checked)
```
