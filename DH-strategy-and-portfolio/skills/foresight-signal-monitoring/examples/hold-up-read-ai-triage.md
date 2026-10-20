# Worked example: A2 hold-up read and B1 review (illustrative log, saved live data)

Built on 20 October 2026. The foresight log is illustrative (`examples/sample-data/foresight_log_illustrative.csv`, see its README); the records it points to are real and saved in `examples/live/` (19 October 2026 calls) or cited in the research rows (Pear and Aidoc status read 20 October 2026, SP-155 to SP-164). The connector was disconnected during the build; no new call was made.

**Request.** "Here is our foresight log (attached). As of today, which of our calls and technology selections held up by our own rules? Our pass rule is 'hit share at least 60 percent and no leads logged as signals'."

**Steps run.** `python3 scripts/foresight_check.py --log examples/sample-data/foresight_log_illustrative.csv --as-of 2026-10-20 --pass-rule "hit_share >= 0.6 and leads == 0" --if-confirmed "F5=miss;F7=miss"`; records read from the saved outputs listed under Calls made and the status rows.

---

## Answer (short mode)

**Answer.** By your recorded outcomes, 2 of 3 resolved selections are hits (67 percent), but your pass rule is not met because one press item (F2) is logged as a signal. Two proposed outcomes await you: F5 a miss, and F7 a miss on the "filing" part of your rule. If you confirm both, the hit share becomes 1 of 4 (25 percent; script output).

| Id | Call or selection | Your rule | Record now | Outcome | Flags |
|---|---|---|---|---|---|
| F4 | QAS decisions in 2026 exceed 2025's 15 | Count at 31 December 2026 | 10 decisions to 16 September 2026 | Open: horizon not reached | none |
| F5 | FDA AI lifecycle guidance final by 30 September 2026 | Final on FDA's page by the horizon | Still draft on 19 October 2026 (US-21) | Proposed miss | R2, O3 |
| F6 | Shortlist ORTEC Stroke Triage App | Still on the EU market | "No longer placed on the EU market", EUDAMED, retrieved 14 October 2026 | Miss (yours) | none |
| F7 | Partner with Pear (reSET) | Still operating and filing | Last filing a Form 25-NSE, 2 May 2023 | Recorded hit; proposed miss | R5 |
| F8 | Briefcase-Triage in the EU pilot | Still on the EU market | "On the EU market", Basic UDI-DI 7290018052BC.TRGSU, retrieved 14 October 2026 | Hit (yours) | O1, O3 |

**F7 on the record.** Pear filed chapter 11 on 7 April 2023, case no. 23-10429, District of Delaware (Pear 8-K, filed 7 April 2023, Item 1.03; SP-156 [WF]). Nasdaq gave notice of delisting on 10 April 2023 (Pear 8-K, filed 10 April 2023, Item 3.01; SP-160 [WF]). No filing follows the Form 25-NSE of 2 May 2023, and there is no Form 15 (Pear EDGAR record; SP-155 [WF]). "Filing" is not met before your 1 September 2024 horizon. "Operating" is not resolvable: chapter 11 is not liquidation (DL-136) and the court records were not read. reSET is listed with FDA today by Harvest Bio LLC (FDA registration and listing; SP-169), which is not the sale record.

**Limits.** The change log behind your F7 hit began 12 October 2026 (R5).

**Company status.** Aidoc Medical Ltd.: no SEC registrant found (EDGAR search, 20 October 2026; SP-162 [WF]); FDA establishment registration active for 2026 (SP-164). ORTEC B.V.: Status: [GAP]: not read.

**For you to confirm.** F5 and F7 as misses. F8 owner: owner not named; who owns it? Reread dates for F5 (15 October 2026) and F8 (1 October 2026) are earlier than the read date.

**Calls made** (saved 19 October 2026): regulatory-dh.get_pathway_precedents {product_code: "QAS", jurisdiction: "US"}; regulatory-dh.search_devices {query: "Briefcase" / "stroke", jurisdiction: "EU"}; diligence-dh.get_deltas {companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}; diligence-dh.get_funding_signals {company: "Pear Therapeutics, Inc."}. Connector unavailable on 20 October 2026; saved outputs and status rows used.

Full version available on request (adds the signals F1 to F3, the counts table and the B1 review with miss owners).

Hold-up read draft for the owner. Outcomes by your rules; no benchmark. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## Checks made on this example

- Word count of the answer section (from "**Answer.**" to the record line, calls list excluded) with `scripts/foresight_check.py --words`: 449 words, within the short-mode cap (run 20 October 2026).
- Script output matches the table: F2 Q1 Q2 Q3; F5 R2 O3; F7 R5; F8 O1 O3; hit share 2 of 3; pass rule not met; with `--if-confirmed "F5=miss;F7=miss"`, 1 of 4 (25%), still not met.
- Record facts trace to `examples/live/pathway_precedents_QAS_2026-10-19.json`, `search_devices_eu_2026-10-19.json`, `funding_signals_pear.json` (the two newest stored filings are the 8-Ks of 7 and 10 April 2023), `diligence_deltas_Akili_Pear.json`, row US-21 in `references/ai-ml-regulation-research.md`, rows SP-155, SP-156, SP-160, SP-162, SP-164, SP-169 in `references/strategy-and-portfolio-sources.md`, and DL-136 in `references/diligence-research.md`.
- No reread date, owner or threshold supplied; F8's missing owner is kept. The record line is the very last line of the answer.
