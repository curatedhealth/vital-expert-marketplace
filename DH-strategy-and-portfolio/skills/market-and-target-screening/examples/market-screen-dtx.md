# Worked example: A1 market screen, digital therapeutics, US and EU

Built on 20 October 2026 from live library outputs saved on 19 October 2026 by earlier builds (the connector was not available on 20 October 2026; origins in `examples/live/README.md`). The request and the person are illustrative; the company rows are as the library returned them. A rerun on a live connector should repeat steps 1 and 4, which need a live check.

**Request.** "We're building a long list of prescription digital therapeutics companies, US and EU. Who's on record, and how big is this market?"

**Calls (as saved).**
1. `commercial-dh.list_commercial_dh_sources {}` (stand-in for `diligence-dh.list_sources`, which was not saved; same census), 19 October 2026.
2. `diligence-dh.screen_market {segment: "dtx", jurisdiction: "EU", limit: 10}`, 19 October 2026.
3. `diligence-dh.screen_market` through `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 10}` (all jurisdictions), retrieved 19 October 2026 18:58 UTC.
4. Script: `python3 -I scripts/screen_helpers.py table examples/live/screen_market_dtx_via_peer_screen.json`.

---

## Answer (short mode)

The library's store matched 18 `dtx` companies; the ten shown all carry `country: US` as stored, and the EU screen returned one company (Novasight, Ltd., Israel). The EU result is a coverage limit, not a small market: DiGA makers are not returned. No source gives a market size, so none is given.

**Long list (as of 19 October 2026; order is the library's sort by evidence maturity score, then name, not a ranking of targets)**

| Company | Products (as stored) | Authorizations | Studies | Safety records | Evidence maturity (rubric v1) |
|---|---|---|---|---|---|
| Akili Interactive Labs, Inc. | EndeavorOTC; EndeavorRx | 3 | 10 | 0 | 100 |
| Appliedvr, Inc. | EaseVRx; RelieVRx; RelieVRx (Pico G3) | 3 | 5 | 1 | 100 |
| Click Therapeutics, Inc. | CT-132; Motivista (CT-155) | 2 | 14 | 0 | 89 |
| Luminopia, Inc. | Luminopia; Luminopia One | 4 | 3 | 0 | 89 |
| Swing Therapeutics, Inc. | Stanza | 1 | 5 | 0 | 78 |
| Cognifisense, Inc. | VRNT | 2 | 2 | 0 | 67 |
| Nightware, Inc. | NightWare Kit (with Apple devices, as stored) | 1 | 4 | 0 | 67 |
| Pear Therapeutics, Inc. | reSet; reSET-O; Somryst | 3 | 3 | 2 | 67 |
| Better Therapeutics | BT-001 | 1 | 5 | 0 | 56 |
| Big Health, Inc. | Daylight; Sleepio | 2 | 4 | 0 | 56 |
| Novasight, Ltd. (EU screen) | CureSight-CS100 | 2 | 5 | not in saved output | 56 |

**Coverage.** "This screen covers only the companies the store holds, not the market": 2,205 companies, segment `dtx` only, jurisdictions CA, EU, TW, US. Not loaded: Companies House, Zefix, the DiGA directory feed, NICE, private funding.

**Gaps that matter.**
1. German DiGA makers: not covered. The DiGA directory publishes listings (DE30) but not refused applicants (DE32).
2. Eight more matches not shown (`limit: 10`).
3. Evidence maturity is the library's convention, not a rating; funding did not track a similar score [PAPER] (DL-117, DOI 10.2196/37677).

**Status (as read on 20 October 2026, `named-company-status.md`).** Akili (registrant Akili, Inc., SP-148): merger with Virtual Therapeutics completed with a change in control (Akili 8-K, 2 July 2024, SP-151); Form 15, 12 July 2024, which is not dissolution (SP-154; DL-149 (inference)). Pear: chapter 11 (Pear 8-K, 7 April 2023, SP-156); Nasdaq delisting notice (Pear 8-K, 10 April 2023, SP-160); Form 25-NSE, 2 May 2023, not dissolution (SP-155, DL-144). Big Health: no SEC registrant found (SP-162). SEC rows are [WF]. Current FDA listing holders: EndeavorRx, Akili Interactive Labs c/o Virtual Therapeutics (SP-168); Somryst, Nox Medical (SP-167); reSET and reSET-O, Harvest Bio (SP-169). Others: [GAP]: not read; filings to open on request (A2).

**Decisions for you.** For a short list, give your criteria and pass rules (B1), and who clears this record.

Full version on request.

Calls made: listed above (two counted screen calls, one free perimeter call).

Market screen draft. Order is the library's sort, not a ranking. No market size. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## Notes for the builder

- No SEC contact was given for this run, so no EDGAR page was opened in it (DL-153 [WF]). Status for Akili, Pear and Big Health comes from the research rows read on 20 October 2026 (`references/named-company-status.md`); the other companies stay "[GAP]: not read". Status is never taken from press or memory.
- The safety records count for Pear Therapeutics, Inc. (2) matches the two Class II recalls of 7 June 2021 listed by `compare_portfolio` for reSET and reSET-O. The example does not interpret them.
- With `--min-authorizations 2` (an illustrative rule, not the person's) the script marks 7 of the 10 US rows as passing; the answer above applies no rule because none was given.
