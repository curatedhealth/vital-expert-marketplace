# Worked example: A1 sample and A2 movement for an insomnia DTx in Germany

The product "SleepWell CBT" and all artifact texts in `examples/sample-data/` are illustrative, written for this build. The peer and listing facts are live library data from 19 October 2026 (`examples/live/`).

**Request:** "Our line for Germany is 'For adults with chronic insomnia: a digital CBT program your doctor can prescribe. Not a replacement for your clinician.' Check our website, app store page, physician leave-behind, partner brief and the trade-fair slide. Then tell me if anything moved with somnio, HelloBetter, Big Health or Akili since we set the line in January 2025."

**Calls and runs**

1. `scripts/positioning_check.py sample examples/sample-data/checkset.csv` (no library call; the copies stay local). Output: `positioning_sample_illustrative.md`.
2. `commercial-dh.list_commercial_dh_sources` `{}` (free): DE_DIGA 82 listings, last load 15 October 2026.
3. `diligence-dh.get_deltas` `{companies: ["Big Health, Inc.", "Akili Interactive Labs, Inc."], since: "2025-01-01"}`: no change recorded for both; log first entry 12 October 2026, last sweep 19 October 2026.
4. `market-access-dh.find_scheme_precedents` `{scheme: "DE_DIGA", indication: "F51", limit: 10}`: somnio (listed 22 October 2020), HelloBetter Schlafen (18 December 2022), somnovia (28 October 2024), all permanent.
5. `market-access-dh.get_status_history` `{reference, scheme: "DE_DIGA"}` for each of the three (added 19 October 2026 after grading): HelloBetter Schlafen permanent from 17 December 2024, BfArM notice 18; somnio and somnovia first-load snapshot only (`live/get_status_history_DE_DIGA_F51.json`).
6. `scripts/positioning_check.py peers-diff` on the two saved peer screens: the runs used different arguments, so no change is inferred (`peers_diff_2026-10-19.md`).

## Answer (short mode)

**Answer.** One of four in-market artifacts carries the line as written. The app store page and the leave-behind do not, and both carry wording the owner needs to see. Nothing in the library shows a peer change since January 2025, but its change log only began on 12 October 2026, so that is not evidence of no change.

| Artifact | Line | Top flag (row) |
|---|---|---|
| Website home page | Present | None |
| App store description | Absent (closest: "...digital CBT program for adults with chronic insomnia that your doctor can prescribe", similarity 0.54; "not a replacement" boundary missing) | "BfArM-approved" approval wording (PC-EU-11); "Clinically proven to cure insomnia in six weeks" device-indicating words (PC-UK-04) and certain-success impression (PC-DE-04) |
| Physician leave-behind | Absent | "sleep better, guaranteed"; "treats insomnia without side effects" (PC-DE-04); "monitors", "treats" (PC-UK-04) |
| Partner brief | Not measurable `[GAP]`: no copy supplied | |
| Trade-fair slide | Not scored: not in market | "Medical grade" would be wellness exit wording (PC-US-63) if used |

The app store page counts as promotional material (PC-UK-01). A listing is not evidence of effect, and "approved" must match what BfArM's decision states.

**Movement.** Listed insomnia DiGA unchanged in the library's copy: somnio, HelloBetter Schlafen and somnovia, all permanent (retrieved 15 October 2026). The library stores one status change for the three: HelloBetter Schlafen became permanent on 17 December 2024 (BfArM notice 18 of 2 January 2025), before the January 2025 positioning date. No other status change is stored `[GAP]`. Rule change after January 2025 that touches wording: none in this skill's sources for Germany; a 26 June 2026 change to the HWG is recorded but its content was not read `[GAP]`.

**Stop.** The app store and leave-behind claims go to the claims audit (DH-02.01.3.2), then to your regulatory or legal owner: owner not named. The leave-behind has no sampler named.

**Record.** Sample draft. Flags are signals, not verdicts. Uncleared.

## What this example shows

- Only in-market copies are scored; the slide draft is reported but not scored.
- The connector's change log limit is stated with "no change recorded".
- Flags name the row and quote the sentence; the model clears nothing.
