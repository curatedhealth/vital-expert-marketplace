# Worked example: "Is somnio reimbursed, and where?"

Real library data, retrieved by `search_listings` and `generate_report` on 19 October 2026. Shown so the model sees the shape of a good answer, not to be reused as current fact.

## What the tools returned (abridged)

- `list_schemes`: 16 schemes. DE_DIGA 82 listings, partial, loaded 15 October 2026. BE_MHEALTH 33 listings, partial. UK_NICE_EVA 15, partial. FR_PECAN 2, FR_LATM 2, IE_HSE_CGM 12, gold. FR_LPPR, UK_NICE_NHAP, AU_MSAC, CH_BAG, ES_REDETS, FI_DIGIHTA, SE_TLV hold none.
- `search_listings` "somnio": one row. DE_DIGA, status `permanent`, status_raw "dauerhaft aufgenommen", DiGA-ID 00508, PZN 16898724, listed_on 2020-10-22, ends_on null, price 224.99 EUR, manufacturer mementor DE GmbH, indications include F51.0 and G47.0 (ICD-10-GM), source https://diga.bfarm.de/de/verzeichnis/00508, retrieved 15 October 2026.
- `generate_report` memo: DE_DIGA permanent; all other schemes "[GAP]"; history starts at the 15 October 2026 snapshot; earlier transitions `[GAP]`.

## The answer the skill should give

**Answer.** somnio, an insomnia app by mementor DE GmbH, is permanently listed in the German DiGA directory (DiGA-ID 00508), so it is prescribable and paid by statutory health insurance in Germany, as of the library's 15 October 2026 load. The library finds it in no other scheme, but for most of those schemes that reflects what the library holds, not a decision.

**Status by scheme.**

| Scheme | Country | Kind | Status (source wording) | What it means | Since | Clock or next event | Price stated | Source, retrieved | Library coverage |
|---|---|---|---|---|---|---|---|---|---|
| DE_DIGA | DE | listing | permanent ("dauerhaft aufgenommen") | On the DiGA list permanently; prescribable and reimbursed | 22 October 2020 | No end date stated `[GAP]` | 224.99 EUR as stated in the record | diga.bfarm.de/de/verzeichnis/00508, 15 October 2026 | partial, 82 listings |

Also checked: 15 other schemes; see gaps.

**What the gaps mean.**

- Covered, product absent: Belgium mHealth (33 listings), NICE early value assessment (15), NICE HealthTech guidance (2), France PECAN (2), France LATM (2), Ireland CGM (12), CMS remote monitoring and digital mental health codes. somnio is not in the library's copy of these; for the partial schemes the copy may be incomplete. Check the authority before concluding.
- Not covered: France LPPR, NICE NHAP, Australia MSAC, Switzerland MiGeL, Spain RedETS, Finland Digi-HTA, Sweden TLV. The library holds no listings here, so it cannot answer.
- Field missing: the German record states no end date, and the library's history starts at its 15 October 2026 snapshot, so whether somnio passed through a provisional phase is `[GAP]`.

**What this implies (advisory).** In Germany the access question is uptake, not listing: prescribing and onboarding belong to Benefit Design (task B2). Outside Germany, the library gives no basis for a coverage claim.

**Sources and record.** 1. BfArM DiGA directory, somnio, https://diga.bfarm.de/de/verzeichnis/00508, retrieved 15 October 2026. These facts rest on the library's copy of the register; confirm them on the BfArM page before external use. Record: not cleared, draft.

**The same answer in short mode** (for "is somnio reimbursed outside Germany? quick"): somnio is permanently listed in the German DiGA directory (DiGA-ID 00508, since 22 October 2020; library load of 15 October 2026). The library finds it in no other scheme, which is a gap in the library, not a decision: several European schemes are only partly loaded or not loaded at all. Cite it as a German precedent, after checking the BfArM page. Want the full scheme-by-scheme view, or comparable insomnia products in other schemes?

## Why this is a good answer

It answers first. It translates "dauerhaft aufgenommen" into what it means. It reports the price as the record states it, not as current. It splits the 15 misses into two different situations instead of 15 identical `[GAP]` lines. It does not say "not reimbursed in France".
