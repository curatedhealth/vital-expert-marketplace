# Worked example: A3 Market intelligence map, digital therapeutics for insomnia, US and Germany

Built on 20 October 2026 from library outputs saved on 19 October 2026 and the research rows read on 20 October 2026 (`named-company-status.md`, `market-intelligence-rules.md`). No live call was made; the connector was unavailable. Revised 20 October 2026 to add the current Somryst holder, Pear's filings, Big Health's FDA listings, the DiGA directory counts and the Medicare payment rule.

**Request.** "We're a pharma BD team looking at prescription digital therapeutics for insomnia in the US and Germany. Map the ecosystem for us: who buys, who pays, who the peers are, what rules matter. And how big is the market?"

---

**Answer.** Payers, peers and rules hold records in both markets; buyers stay empty until you name who adopts and contracts. The saved screen has no indication field, so you decide which peers belong. No source gives a market size, and the library's sort is not a ranking, so no leader is named.

| Lane | Entry (record as stated) | Source | Date |
|---|---|---|---|
| Buyers | [GAP]: not given. Who prescribes, adopts and contracts in each market? | your request | 20 October 2026 |
| Payers, DE | somnio: permanent DiGA listing ("dauerhaft aufgenommen"), listed 22 October 2020, identifier 00508 | VITAL library map_money_flow {reference: "somnio"}, saved 19 October 2026 | 19 October 2026 |
| Payers, DE | Whole directory, not insomnia only: 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted; refused products not named | BfArM DiGA page, as of 9 September 2026 (DE32, DE34) | 9 September 2026 |
| Payers, US | Medicare codes G0552 to G0554 pay only for devices under 21 CFR 882.5801; Somryst's 510(k) states 882.5801, SleepioRx's not read. Payment not stated | Federal Register, 9 December 2024 (US7); FDA 510(k) record K191716 (SP-165) | 20 October 2026 |
| Peers, US | Somryst: 510(k) K191716, cleared 23 March 2020 (a clearance, not "approval", DL-128). Applicant: Pear Therapeutics, Inc. Current FDA listing holder: Nox Medical, listing created 18 December 2024 | FDA 510(k) record (SP-165); FDA registration and listing (SP-167) | 20 October 2026 |
| Peers, US | Pear Therapeutics: chapter 11 filed 7 April 2023, outcome open on EDGAR (DL-137 (inference)); Nasdaq delisting notice 10 April 2023; last filing Form 25-NSE, 2 May 2023, not dissolution (DL-144) | Pear 8-K, 7 April 2023 (SP-156); Pear 8-K, 10 April 2023 (SP-160); EDGAR record (SP-155); all [WF] | 20 October 2026 |
| Peers, US | Big Health Inc: SleepioRx (510(k) K233577, product code QVO, as Somryst) and DaylightRx listed with FDA; no SEC registrant found. Store: Daylight, Sleepio; evidence maturity 56 (rubric v1) | FDA registration and listing (SP-163); EDGAR lookup (SP-162 [WF]); VITAL library screen_commercial_peers, saved 19 October 2026 | 20 October 2026 |
| Rules | EHDS applies from 26 March 2027; secondary use, including algorithm training, from 26 March 2029 | EHDS Regulation (EU) 2025/327 (SP-068, SP-071, SP-072) | 20 October 2026 |
| Rules | HSR, CFIUS, DOJ bulk data, HIPAA breach and GDPR Article 9 health data facts; whether any applies is for the owner you name for legal questions | DL-044 to DL-106 | 20 October 2026 |

**Coverage.** Buyers: your input only. Payers: DE_DIGA store "partial" (82 listings, 19 October 2026; not reconciled with BfArM's 62); CMS rows are code-level; absence from the store is not absence from a scheme. Peers: the store "covers only the companies the store holds, not the market"; other German sleep DiGA need a directory search. Rules: no device or DiGA rules here; device status and pathway go to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

**Gaps that matter.** Who buys (not given). Who bought Pear's products: named only in court sale orders (case 23-10429), not read. Status: [GAP]: not read for Nox Medical and somnio's maker.

**Decisions for you.** Which peers belong in your insomnia map, which buyers to add, and who clears this record.

Full version on request.

Calls made (all saved on 19 October 2026, none live): `market-access-dh.list_schemes {}`; `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 10}`; `commercial-dh.screen_commercial_peers {segment: "dtx", name: "Somryst", limit: 3}`; `commercial-dh.map_money_flow {reference: "somnio", user, buyer, payer}`. Research rows read 20 October 2026, no call.

Market intelligence map draft. Records only; no market size, share or segment choice. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

What the example shows (outside the answer): the buyers lane stays a gap rather than a guess; the Somryst row gives the applicant at clearance and today's FDA listing holder as two facts; Pear's status comes from its own 8-Ks, each with what it does not mean; the DE34 counts and US7 sit in the payer lanes with their limits; market size and a leader are declined in one line.
