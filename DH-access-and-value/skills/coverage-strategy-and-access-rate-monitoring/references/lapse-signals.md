# Coverage clocks and lapse signals

What can change a product's coverage without anyone filing anything new, per country, and how to read each signal. Every row points to the sourced row in `access-monitoring-sources.md` (DE-, FR-, EN- numbers) or `access-after-listing.md`. Read on 19 October 2026; not yet owner-reviewed.

A signal is a reason to check, never a verdict. Say "the 12-month trial period has passed; check whether an extension was granted or a decision is pending", not "the listing has lapsed".

## Germany (DiGA)

| Signal | Clock | How to read it | Source |
|---|---|---|---|
| Trial period running | Up to 12 months from provisional listing | Normal. The permanent-listing evidence is due before the end. | DE-20, L-1 |
| Extension | One extension, up to 12 more months, applied for at least 3 months before expiry | If no extension was applied for in time, BfArM refuses it and deletes the DiGA at the end of the trial. | L-1 (DiGAV § 17) |
| Trial expired, decision pending | After 12 or 24 months | **Not a lapse.** The DiGA stays listed, prescribable and reimbursable until BfArM decides. | L-2 |
| Beyond 24 months | Legal maximum passed | Usually a court route or a pending decision (one trial ran 29 months; one deleted DiGA was re-listed by court order and deleted again). Check BfArM and court status before stating anything. | DE-7, Changes and conflicts 2 |
| In practice | Trials averaged 20 months to decision | Use as context for "how long until we know", not as a forecast. | DE-6 |
| Permanent with narrower scope | At the permanent decision | About one in five trial DiGA that became permanent did so with a narrower scope; unproven claimed effects are struck in the directory. Check the listed scope, not only the status. | DE-2, DE-24 |
| Deletion | BfArM decision, published with reasons, announced in the Bundesanzeiger (target quarterly) | Patients finish the current 30/60/90-day prescription, or up to 3 more months on a one-time licence; no repeat prescription after. Deleted DiGA are normally paid 0 euros from month 13. | L-3, L-4, DE-22, DE-23 |
| Price clock | Negotiated price applies from month 13 | Since 1 January 2026 at least 20 percent of the negotiated price depends on outcomes; from 1 January 2027 a volume discount applies above 3,000 units a year. | L-4, DE-19 |
| Outcome reporting | Permanent DiGA only; data from 1 July 2026, first report 15 April 2027 | Per-DiGA results are published once a DiGA reports at least 200 users in a quarter. No per-DiGA dropout data exists before then. | DE-16, DE-17, DE-18 |

## France (PECAN, LPPR, LATM)

| Signal | Clock | How to read it | Source |
|---|---|---|---|
| PECAN year | One year, not renewable | Coverage is temporary by design. | FR-1 |
| Filing for common law | 6 months (LPPR, DTx) or 9 months (LATM, remote monitoring) | The sources disagree on when the clock starts (PECAN decision, start of coverage, or the application). State which anchor you used. | FR-2, Changes and conflicts 5 |
| How PECAN ends | Listing, refusal, missed filing or withdrawal, expiry without decision, certification failure, safety withdrawal | Each end leads somewhere different; name which one applies. | FR-3 |
| Continuity of treatment | 6 months after coverage stops, or 45 days after a refusal, unless safety reasons | Patients already treated keep access for that period. | FR-3 |
| Refusal is not final | A refused PECAN product later obtained a favorable common-law opinion | Do not treat a PECAN refusal as the end of the route. | FR-5 |
| Common-law renewal | Several years, renewable, re-apply before the end | The statutory duration is not sourced. | FR-7 |
| LATM payment | Device fee varies with the average monthly active patient count in the indication | Volume across all manufacturers moves the tariff; no published count was found. | FR-8 |

## England (NICE early use, NHS)

| Signal | Clock | How to read it | Source |
|---|---|---|---|
| Evidence generation | About 3 years from guidance publication (some topics 2) | Use during the period is conditional on the planned evidence being generated. | EN-1, EN-4, EN-5 |
| Annual reporting | From 12 months | Company reports data collection to NICE each year. | access-after-listing.md (England) |
| Withdrawal grounds | Any time | Not available to the NHS, company unreachable, voluntary withdrawal, safety or regulatory concern, not engaging in evidence generation, or evidence cannot resolve the uncertainties. | EN-2 |
| Re-evaluation | At the end of evidence generation | For routine use; may be done as a technology appraisal. No early-use digital product was found to have completed re-evaluation by 19 October 2026. | EN-3, Not sourced |
| MedTech Funding Mandate | Support for about 3 years per technology | Exit schedule in the policy annex ([WF]). | EN-12 |

## Using the library for clocks

The library stores `listed_on` and, when the source states it, `ends_on`. For DiGA trial listings `ends_on` is empty, so count from `listed_on` and say so. `scripts/coverage_clocks.py` does the counting and flags the thresholds above. See `tools.md` for why `listed_on` on a permanent DiGA may be the first listing date, not the date it became permanent.
