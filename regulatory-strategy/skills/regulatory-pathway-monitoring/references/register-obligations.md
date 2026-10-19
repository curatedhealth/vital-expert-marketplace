# Register obligations and change-tracking sources

Interpretive reference for task A1. Row prefixes as in `review-clocks.md`. All rows read 19 October 2026.

## EUDAMED

| Fact | Row |
|---|---|
| Four modules mandatory since 28 May 2026: actor registration, UDI/device registration, notified bodies and certificates, market surveillance. | RP EU-36; JX-36 |
| Trigger: Commission Decision (EU) 2025/2371, published 27 November 2025, starting the six-month transition under Regulation (EU) 2024/1860. | RP EU-37; JX-37 |
| Each EUDAMED obligation applies six months after the functionality notice. | RP EU-39 |
| Devices first placed on the market before 28 May 2026 and still being placed: register in the UDI/device module within 12 months of the notice; the Commission timeline gives 28 November 2026. | JX-39, JX-41 |
| Devices first placed on the market on or after 28 May 2026: register before placing the first unit. | JX-40 |
| Vigilance and post-market surveillance, and clinical investigation modules: still in development; mandatory on release with no voluntary period. No date published. | RP EU-38; JX-38 |
| The EUDAMED Q&A is not formally endorsed by the Commission. | multi-region "Changes and conflicts" |

So for every EU device the person markets, A1 asks: when was it first placed on the market, and is it registered in the UDI/device module? `scripts/review_clock.py` applies the two rules above to the person's list.

## EU legacy devices (MDR transition)

- Legacy devices with valid MDD certificates: until 31 December 2027 (class III, most IIb implantables) or 31 December 2028 (other IIb, IIa, class I sterile or measuring) (RP EU-21, RP EU-22).
- Software self-certified under the MDD before 26 May 2021 that needs a notified body under the MDR (for example up-classified by Rule 11): until 31 December 2028 (RP EU-23).
- Only if the manufacturer had an MDR QMS, applied to a notified body by 26 May 2024 and signed a written agreement by 26 September 2024, with no significant design or intended-purpose change (RP EU-24). These dates have passed; a product that missed them cannot use the extension (RP "Changes and conflicts").

## United States

| Obligation | Rule | Row |
|---|---|---|
| Initial registration | Within 30 days of starting a covered operation; list devices then. | JX-28 |
| Annual registration and listing | Every fiscal year between 1 October and 31 December; listings confirmed even with no change. | JX-29, JX-30 |
| Changes | Within 30 days. | JX-31 |
| Lapse | "Failed to register" or "failed to list" status. | JX-32 |
| Fee | Establishment registration USD 13,785 in FY 2027. | RP US-55 |

## Great Britain

- Devices must be registered with the MHRA (RP UK-01). Registration data are not in the library (MHRA PARD has no API).
- CE acceptance end dates as in `review-clocks.md` (RP UK-02 to UK-04). Indefinite recognition was consulted on, outcome not published (RP UK-05; MR-24).
- Post-market surveillance rules in force since 16 June 2025 (RP UK-08).

## Switzerland

- Product registration with Swissmedic from July 2026 with a six-month transitional period (JX-42; RP CH-08). MedDO Art. 108(2), consolidated 1 July 2026 (same fedlex URL as MR-20, read 19 October 2026, raw file research_reg4/raw/ch_meddo_2026.txt): "For devices, systems and procedure packs placed on the market on or after 1 July 2026, registration with Swissmedic in accordance with Article 17 paragraph 5 must be completed by 31 December 2026." Art. 108(3): devices placed earlier (from 26 May 2021) must register "without delay" if a serious incident, field safety corrective action or trend must be reported. A general deadline for devices already on the Swiss market before 1 July 2026 is not stated in this article `[GAP]`.
- The library holds no Swiss device data (swissdamed is web-only).

## Canada (if the person holds a license)

- Annual signed license statement before 1 November; failure allows cancellation (JX-33, JX-34). New or modified QMS certificates to Health Canada within 30 days (JX-35).

## Where changes appear (to check by hand; the library does not watch these)

| Source | What it shows | Row |
|---|---|---|
| FDA guidance search | Sorted by issue date; email alerts | CHG-01, CHG-02 |
| CDRH guidance agenda | Published each fiscal year; A-list priority, not binding | CHG-03, CHG-04 |
| FDA MDUFA reports | Quarterly performance | RP US-64 |
| MDCG endorsed documents | Current, ongoing and obsolete guidance; not legally binding | CHG-09, CHG-10 |
| EUDAMED news | Module announcements | CHG-11 |
| MHRA guidance finder | Most recently updated, alerts and feed | CHG-12 to CHG-14 |
| Swissmedic and FOPH | Updated documents, RSS; MedDO revisions | CHG-15, CHG-16 |

No regulator states a fixed update cadence except CDRH's annual agenda (multi-region "Not sourced").
