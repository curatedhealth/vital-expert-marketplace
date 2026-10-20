# Worked example: A1 authorization and register tracking for a CBT-I app

Run on 19 October 2026. Library data are live (trimmed in `live/monitoring_calls_2026-10-19.json` and `live/insomnia_cbt_calls_2026-10-19.json`, evidence class M). The person's own submissions and EU devices are an **invented sample** (`person_sample_2026-10-19.json`) standing in for a buyer's records; no real product is described by them.

## The request

"We filed a 510(k) for our CBT-I app on 15 June 2026 (41 days on hold with us so far) and a De Novo for a relapse-prevention module on 2 March 2026 (60 days on hold; FDA asked for more information on 20 July 2026). Our CBT-I app is CE marked and on the EU market since September 2025; a teens version since July 2026. Neither is in EUDAMED yet. What changed for Sleepio and Somryst since our strategy, and where do we stand?"

## Calls made

| # | Call | Arguments | What came back |
|---|---|---|---|
| 0 | `regulatory-dh.list_jurisdictions` (free) | none | US 1,226 authorizations, 892 safety events; EU 3,142, no decision dates; UK alerts only; CH not loaded |
| 1 | `regulatory-dh.get_register_deltas` | `{"product_code": "QVO", "since": "2026-01-01", "jurisdiction": "US"}` | No rows: "no watch is registered for this scope; the change log has not started" |
| 2 | `regulatory-dh.get_market_status` | `{"reference": "K233577"}` | Sleepio®: US true, EU false, UK and CH [GAP] |
| 3 | `regulatory-dh.search_devices` | `{"query": "Big Health", "jurisdiction": "all"}` | Sleepio® K233577 (5 August 2024), Daylight K233872 (30 August 2024); no later decision |
| 4 | `regulatory-dh.get_market_status` | `{"name": "somnio"}` | Two rows, EU true and EU false |
| 5 | `regulatory-dh.get_authorization` | `{"reference": "PP12257SOMNIO57"}` | somnio: EU, class IIa, "On the EU market", no decision date |

`get_deltas` was called once separately to confirm it is the same tool (its response names itself `get_register_deltas`); in a real run call one or the other. Clock and EUDAMED lines from `scripts/review_clock.py` on the invented sample: `review_clock_sample_2026-10-19.txt`.

## The answer (short mode)

**Answer.** No register change found for Sleepio® or Somryst since their decisions in 2024 and 2020; the library's change log for code QVO has not started, so this rests on a fresh read, not a log. On your side, the De Novo's open information request is the clock that decides the next move, and the EU CBT-I app has a EUDAMED registration rule to meet.

**Status**

| Item | Status per record | Changed? | Source, retrieved |
|---|---|---|---|
| Sleepio® K233577 | 510(k), decided 5 August 2024; US authorized, EU not in the library's copy | No new decision for Big Health after 30 August 2024 | FDA via library, 13 October 2026 |
| Somryst K191716 | 510(k), decided 23 March 2020 | Snapshot only | FDA via library, 13 October 2026 |
| somnio | EU class IIa, on the EU market | Two conflicting market rows; check EUDAMED | EUDAMED via library, 14 October 2026 |

**Your open reviews**

| Submission | Calendar days | FDA days (your hold days) | Reference figures |
|---|---|---|---|
| 510(k), filed 15 June 2026 | 126 | 85 | MDUFA goal 90 FDA days for 95% (RP US-46); observed average total 141 to 144 days, FY 2023 to FY 2025 (RP US-58) |
| De Novo, filed 2 March 2026 | 231 | 171 | MDUFA goal 150 FDA days (RP US-47); observed average total 248 to 278 days (RP US-61); information request of 20 July 2026: withdrawn if not fully answered within 180 days, that is by 16 January 2027 (RP US-13) |

The goals apply to a share of submissions, not to each file.

**Register duties**

- EU CBT-I app, first placed September 2025, not registered: register in the UDI/device module within 12 months of the notice; the Commission timeline gives 28 November 2026 (JX-39).
- EU teens version, first placed July 2026, not registered: registration must precede placing the first unit (JX-40). This is a rule question for your regulatory owner.
- US: annual registration and listing between 1 October and 31 December (JX-29).

**Gaps.** No change log until a watch is set (your decision; `watch_register` exists). UK registrations and Swiss devices not loaded; Sleepio® absent from the library's EU copy is not proof it is not CE marked.

**Record.** Tracking snapshot as of 19 October 2026. No compliance verdict. Owner not named: who owns the De Novo response and EUDAMED registration? Uncleared.

(Under 450 words. Full version on request.)
