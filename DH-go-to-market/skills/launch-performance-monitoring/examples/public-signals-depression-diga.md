# Worked example: A1 public launch signals, depression DiGA cohort (Germany)

Run on live library data on 19 October 2026. Trimmed outputs are in `examples/live/`. The request is a test prompt; products are described only by what their records state.

## Request

"We sell deprexis in Germany. What has changed among the depression DiGA since 1 January 2026, and which clocks should the field team know about?"

## Calls made

| # | Tool | Arguments | Counted | Saved as |
|---|---|---|---|---|
| 1 | `commercial-dh.list_commercial_dh_sources` | none | free | `live/commercial_sources.json` |
| 2 | `commercial-dh.get_deltas` | `{reference: "deprexis", since: "2026-01-01"}` | yes | `live/get_deltas_runs.json` |
| 3 | `market-access-dh.find_scheme_precedents` | `{scheme: "DE_DIGA", indication: "F32", limit: 10}` | yes | `live/precedents_de_diga_f32.json` |
| 4 | `commercial-dh.get_launch_sequence` | `{reference: "deprexis", peers: ["Selfapys Online-Kurs bei Depression", "Novego: Depressionen bewältigen", "elona explore – für die mentale Gesundheit", "HelloBetter"], route_hypothesis: "okp_compulsory"}` | yes | `live/launch_sequence_runs.json` (run 4) |

## Answer (short mode)

**Answer.** The library cannot show changes since 1 January 2026: its change feeds returned no events, and the Market Access feed is not available (`[GAP]`). None of the seven depression DiGA the library returned was listed after 1 January 2026; the most recent, elona explore (02373), was listed provisionally on 18 February 2025 and the library copy retrieved 15 October 2026 still reads "vorläufig aufgenommen" with no end date. Today's run is your baseline for the next comparison.

**Cohort (DiGA directory, library copy)**

| Product (DiGA-ID) | Status (source wording) | Listed | Source, retrieved |
|---|---|---|---|
| deprexis (00450) | dauerhaft aufgenommen | 20 February 2021 | diga.bfarm.de/de/verzeichnis/00450, 15 October 2026 |
| elona explore (02373) | vorläufig aufgenommen | 18 February 2025 | diga.bfarm.de/de/verzeichnis/02373, 15 October 2026 |
| My7steps App (01786) | dauerhaft aufgenommen | 17 February 2023 | diga.bfarm.de/de/verzeichnis/01786, 15 October 2026 |
| elona therapy Depression (01254) | dauerhaft aufgenommen | 26 December 2022 | diga.bfarm.de/de/verzeichnis/01254, 15 October 2026 |
| edupression.com (01815) | dauerhaft aufgenommen | 26 December 2022 | diga.bfarm.de/de/verzeichnis/01815, 15 October 2026 |
| Novego (01110) | dauerhaft aufgenommen | 10 October 2021 | diga.bfarm.de/de/verzeichnis/01110, 15 October 2026 |
| Selfapy (00876) | dauerhaft aufgenommen | 16 December 2020 | diga.bfarm.de/de/verzeichnis/00876, 15 October 2026 |

**Clocks and moved rules for the field**
- Provisional listing runs for trial up to twelve months (CP-DE-13); the library's scheme rule adds "exceptionally 24". For elona explore the library stores no end date `[GAP]`: check the BfArM entry before the field says anything about its status.
- A DiGA must stay ad-free and its data may not be used for advertising (PC-DE-15, PC-DE-16).
- HWG: a change by the law of 26 June 2026 is noted but not yet documented in the text read; launch material approved earlier should go back to its owner for a check (research file, Changes and conflicts).
- EUDAMED: actor data changes within one week (CP-EU-11).

**Gaps.** No change feed `[GAP]`; DiGA transitions before 15 October 2026 not stored; status after Selfapy's 11 April 2022 and Novego's 9 October 2023 changes not stated `[GAP]`; "HelloBetter" returned six DiGA-IDs under one name and is left out until you name the product.

**Record.** Library copy, retrieved 15 and 16 October 2026; confirm on the BfArM page before external use. Draft, AI-assisted, uncleared. Nothing here describes any peer's uptake or results.

## What the skill added over the raw tools

- The empty change feed is reported as a gap with the feed status, not as "no change".
- A baseline is saved so the next run can show real differences.
- A provisional listing past the twelve-month rule is reported as stated facts plus a check, without inferring an extension or a deletion.
- Clocks are tied to what the field says, with rows.
