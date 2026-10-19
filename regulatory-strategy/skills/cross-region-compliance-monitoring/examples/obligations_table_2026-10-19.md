# Obligations table: worked run (19 October 2026)

Input: `examples/markets_example.json` (markets from the live market matrix for Brainomix 360 e-ASPECTS; dates and the GB, CA and CH entries are example inputs a person would give, not facts about Brainomix).

```
python3 scripts/obligations_table.py examples/markets_example.json
```

Obligations as of 19 October 2026. Dates restate sourced rules; each is a prompt to check, not a finding.

| Market | Obligation | Date or window | Status as of | Legal status | Basis (row) |
|---|---|---|---|---|---|
| US | Annual establishment registration and confirmation of every device listing, even with no changes | 1 October 2026 to 31 December 2026 | window open; closes in 73 days | in force | JX-29, JX-30; lapse puts the establishment in 'failed to register' or 'failed to list' status (JX-32) |
| US | Annual establishment registration fee (FY 2027 rate, applies from 1 October 2026) | with the annual registration | amount USD 13,785 per US-55 | in force | US-55 |
| US | Update registration information after any change | within 30 days of the change | event-driven | in force | JX-31 |
| EU | Register the device in the EUDAMED UDI/device module (device first placed before 28 May 2026, units still being placed) | 28 November 2026 | 40 days from the as-of date | in force | JX-39 (Commission timeline), JX-41 (Regulation (EU) 2024/1860, 12 months from the notice of 27 November 2025, JX-37) |
| EU | Use EUDAMED actor, UDI/device, certificate and market surveillance modules | mandatory since 28 May 2026 | in force | in force | JX-36 |
| EU | EUDAMED vigilance/PMS and clinical investigation modules | [GAP] no date published; mandatory on release with no voluntary period | check | in force | JX-38 |
| GB | Placing CE-marked (EU MDR) devices on the GB market accepted until | 30 June 2030 | 1350 days from the as-of date | in force | UK-03, MR-23 |
| GB | Register the device with the MHRA | [GAP] no date or renewal cycle in the research | check | in force | UK-01 |
| GB | Indefinite recognition of EU MDR/IVDR CE marking | consultation 16 February to 10 April 2026; outcome not published | proposal only; the end dates above remain law | proposal | UK-05, UK-06, MR-24 |
| CA | Annual signed statement confirming or updating each medical device license | before 1 November 2026 | 13 days from the as-of date | in force | JX-33; if not filed the Minister may cancel the license (JX-34) |
| CA | Send a copy of a new or modified QMS certificate to Health Canada | 1 April 2026 | date passed 201 days ago: confirm what was filed | in force | JX-35 |
| CA | QMS certificate expiry: the date on the certificate, at most three years after issue | no later than 2 March 2029 | 865 days from the as-of date; read the certificate | in force | MR-04 |
| CH | Register products with Swissmedic: devices placed on the market on or after 1 July 2026 (MedDO Art. 108(2)) | 31 December 2026 | 73 days from the as-of date | in force | JX-42, JX-43 |
| CH | Register products with Swissmedic: devices placed from 26 May 2021 (from 26 November 2017 under former MedDO Art. 22a) and before 1 July 2026 (MedDO Art. 108(3)) | without delay once a serious incident, FSCA or trend must be reported; no other date in the text [GAP] | condition | in force (condition) | JX-43 |
| CH | Recognition basis: a declaration of conformity under Swiss or EU law | current law | in force | in force | MR-19, MR-20 |
| CH | Recognition of FDA-authorized devices | ordinance changes being drafted; no in-force date | not available today | draft policy | MR-21, MR-22 |
| AU | ARTG registration and annual duties | [GAP] not in the research | check | not sourced | none |
| AU | MDSAP reports count only if Australian requirements were audited | with each audit | condition | in force (condition) | MR-36 |
