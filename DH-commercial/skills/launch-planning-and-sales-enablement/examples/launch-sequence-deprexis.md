# Worked example: A1 launch sequence and readiness, deprexis (Germany, Switzerland)

Run on live library data on 19 October 2026. Trimmed outputs are in `examples/live/`. The request is a test prompt, not from GAIA AG; the product and its peers are described only by what their records state.

## Request

"Quick one: where does deprexis stand against the other depression DiGA on launch timing, and what would have to be in place for a Swiss launch under compulsory insurance?"

## Calls made

| # | Tool | Arguments | Counted | Saved as |
|---|---|---|---|---|
| 1 | `commercial-dh.list_commercial_dh_sources` | none | free | `live/commercial_sources.json` |
| 2 | `market-access-dh.find_scheme_precedents` | `{scheme: "DE_DIGA", indication: "F32", limit: 10}` | yes | `live/precedents_de_diga_f32.json` |
| 3 | `commercial-dh.get_launch_sequence` | `{reference: "deprexis", peers: ["Selfapys Online-Kurs bei Depression", "Novego: Depressionen bewältigen", "elona explore – für die mentale Gesundheit", "HelloBetter"], route_hypothesis: "okp_compulsory"}` | yes | `live/launch_sequence_runs.json` (run 4) |

An earlier attempt with the names "HelloBetter Depression", "selfapy" and "Somryst" returned deprexis only and no line for the missing peers (run 1). Step 2 exists to avoid that.

## Answer (short mode)

**Answer.** deprexis (DiGA-ID 00450) is permanently listed in the German DiGA directory ("dauerhaft aufgenommen"), listed on 20 February 2021, per the library copy retrieved 15 October 2026. Among the depression DiGA the library returned, Selfapy listed earlier (16 December 2020); Novego (10 October 2021) and the elona products followed. For Switzerland, no sourced rule in this skill covers launch prerequisites, and the library holds no Swiss product records: the Swiss route is only your hypothesis, and a German listing does not imply a Swiss phase.

**Sequence (Germany, DiGA directory)**

| Event | Date | Product (DiGA-ID) | Source, retrieved |
|---|---|---|---|
| Listed | 16 December 2020 | Selfapys Online-Kurs bei Depression (00876), comparable | diga.bfarm.de/de/verzeichnis/00876, 15 October 2026 |
| Listed | 20 February 2021 | deprexis (00450) | diga.bfarm.de/de/verzeichnis/00450, 15 October 2026 |
| Listed | 10 October 2021 | Novego: Depressionen bewältigen (01110), comparable | diga.bfarm.de/de/verzeichnis/01110, 15 October 2026 |
| Changed | 11 April 2022 | Selfapy; status after the change not stated `[GAP]` | diga.bfarm.de/api/diga-vz/media/2118, 16 October 2026 |
| Changed | 9 October 2023 | Novego; status after the change not stated `[GAP]` | diga.bfarm.de/api/diga-vz/media/2792, 16 October 2026 |
| Listed | 18 February 2025 | elona explore (02373), provisional, comparable | diga.bfarm.de/de/verzeichnis/02373, 15 October 2026 |

"HelloBetter" returned six listings with different DiGA-IDs under one name; they are left out until you say which HelloBetter product is the peer.

**Prerequisites**

| Market | Prerequisite | Row | Your status |
|---|---|---|---|
| Germany | Prescription or fund-approval route; no prescription steering deals with physicians | CP-DE-01, CP-DE-06 | not stated |
| Germany | DiGA ad-free; data not used for advertising; no opaque offers | PC-DE-15 to PC-DE-17 | not stated |
| EU | EUDAMED actor and device registration, mandatory since 28 May 2026 per the Commission | CP-EU-10, CP-EU-12, CP-EU-15 | not stated |
| Switzerland | Not in this skill's sources | none | `[GAP]` |

The library's CH_BAG record states MiGeL position 40.01.01.00.1, valid from 1 July 2026, is a class position for interactive CBT digital applications in depression and names no product. That is a library record, not a launch rule.

**First in the dependency chain.** For any EU market, EUDAMED registration precedes placing on the market (CP-EU-10). For Switzerland, the first step is a sourced reading of Swiss rules by your regulatory owner.

**Gaps.** Swiss rules and records `[GAP]`; DiGA transition history before 15 October 2026 `[GAP]` (day-zero snapshot only); status after two peer changes `[GAP]`.

**Record.** Library copy of the registers, retrieved 15 and 16 October 2026; confirm on the BfArM page before external use. Draft, AI-assisted, uncleared.

Word count of the answer above, without the calls list and the source column: under 450 (checked by script on 19 October 2026).

## What the skill added over the raw tools

- Exact peer names first, so the sequence call did not drop peers silently.
- Merged "HelloBetter" products separated by DiGA-ID instead of reported as one product.
- Prerequisites with rows beside the dates, and no Swiss rule invented where the research is silent.
- The connector's readiness count was not called: the person asked for timing and Swiss prerequisites, and the count would not have answered either (`references/tools.md`).
