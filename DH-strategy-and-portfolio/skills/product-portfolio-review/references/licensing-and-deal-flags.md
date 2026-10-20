# Licensing, competition and company status flags for portfolio items

Interpretive reference. Rules cite SP rows in `strategy-and-portfolio-sources.md` and DL rows in `diligence-research.md` (both read 20 October 2026). These are facts to flag for the person's legal owner. The model never says a license, an agreement or a deal is exempt, safe, lawful, notifiable or clear.

How to cite in an answer: name the source a reader can open, in plain words with its date, then the row id (for example "Regulation (EU) 2026/877 of 16 April 2026 (SP-135)", "Pear 8-K, 7 April 2023 (SP-156)"); never a row id alone. A row the research file marks as an inference carries "(inference)" every time it is cited. Rows marked [WF] say so when applied.

## 1. When this applies

An item in the product portfolio is in-licensed, out-licensed, co-developed, partnered or acquired, or the person asks "build, partner or buy". Each such item carries a flag block in A1 and an open item in B2 for the owner the person names for legal, or owner not named.

## 2. Rules to flag, with dates

| Topic | Fact | Source and rows |
|---|---|---|
| EU technology transfer block exemption: old regulation | Regulation 316/2014 expired on 30 April 2026. Any text citing it as current is out of date. | Regulation (EU) No 316/2014, its own expiry clause, SP-134 |
| New TTBER | Commission Regulation (EU) 2026/877 of 16 April 2026: in force 1 May 2026, expires 30 April 2038. | Regulation (EU) 2026/877, SP-135 |
| Market share conditions | Competitors: "the combined market share of the parties does not exceed 20 % on any relevant market"; non-competitors: "the market share of each of the parties does not exceed 30 % on any relevant market". | Regulation (EU) 2026/877, SP-136 |
| Transition | Agreements in force on 30 April 2026 that met the old rules but not the new ones: Article 101(1) does not apply from 1 May 2026 until 30 April 2027. A license signed on or after 1 May 2026 is not one of them. | Regulation (EU) 2026/877, SP-137 |
| Scope | Technology rights include supplementary protection certificates for medicinal products (SP-138); technology pools are outside the regulation (SP-140); data licensing can fall within it where the data qualifies as an existing technology right such as production know-how (SP-142). | Regulation (EU) 2026/877 and the Commission's explanatory note of 16 April 2026, SP-138, SP-140, SP-142 |
| Hardcore restriction (competitors) | Restricting a party's own R&D is hardcore unless indispensable to protect licensed know-how. | Regulation (EU) 2026/877, SP-139 |
| Guidelines | New Technology Transfer Guidelines (C/2026/2323), OJ 21 April 2026, replace the 2014 Guidelines. | SP-141 |
| US agencies | DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property, 12 January 2017, listed with no withdrawal notice (SP-147): no presumption that IP creates market power; licensing generally procompetitive (SP-143). | DOJ/FTC Guidelines, 12 January 2017, SP-143, SP-147 |
| US safety zone | Absent extraordinary circumstances, no challenge where the restraint is not facially anticompetitive and the parties hold no more than 20% of each relevant market significantly affected (SP-144); for R&D markets, four or more independent entities with the assets and incentive for substitute R&D (SP-145). Outside the zone is not presumed unlawful (SP-146). | DOJ/FTC Guidelines, 12 January 2017, SP-144 to SP-146 |
| SEC exhibits (a listed party) | Material contracts not in the ordinary course are filed as exhibits (SP-130), including a license the business depends on to a material extent (SP-131); specific terms may be redacted if not material and customarily private (SP-132); filed with the 10-Q or 10-K for the period (SP-133). | Regulation S-K Item 601, SP-130 to SP-133 |
| SEC current report | A listed company reports a material definitive agreement under 8-K Item 1.01 (DL-020, DL-021), generally within four business days (DL-019). | SEC Form 8-K instructions, DL-019 to DL-021 |
| Health data in the deal | Where the license, partnership or acquisition moves health data (for example patient data used to train or update a model, or data licensed as know-how, SP-142): GDPR Article 9(1) prohibits processing health, genetic and biometric data unless an Article 9(2) ground applies (DL-101); a party must name its Article 9(2) ground for each processing purpose (DL-101, inference); member states may add conditions (DL-105); large-scale processing of these categories requires a data protection impact assessment (DL-106). | Regulation (EU) 2016/679 (GDPR), DL-101, DL-105, DL-106 |

### The competitor test and the threshold, side by side

Which share condition applies depends on whether the parties compete. When a candidate in-license and an item already on the person's list address the same indication (for example Somryst, a CBT-I insomnia product, beside an own insomnia DTx), list the overlap and ask whether the parties compete; that answer selects the 20% combined or the 30% per-party condition (SP-136). Then put each threshold beside the person's figure, without leaning either way:

| Condition | Threshold | Your figure | For your legal owner |
|---|---|---|---|
| Parties are competitors (Regulation (EU) 2026/877, SP-136) | combined share at most 20% on any relevant market | your combined share, or "not given" | relevant market and shares are theirs to define |
| Parties are not competitors (same) | each party at most 30% on any relevant market | each party's share, or "not given" | same |
| US safety zone (DOJ/FTC Guidelines, 12 January 2017, SP-144) | parties at most 20% of each relevant market significantly affected | your share, or "not given" | outside the zone is not presumed unlawful (SP-146) |

What the model writes: the rule, its instrument and date, each threshold beside the person's figure, the overlap that bears on the competitor test, every flag the rows above support (GDPR where health data moves), and the deal facts the person has not given (relevant market, shares, whether the parties compete, agreement date, any health data moved). What it never writes: whether the agreement is exempt, inside a safety zone, or needs no review, or whether a share is "close to" or "safely under" a threshold. Market definition and shares are the person's or their legal owner's, never the model's.

## 3. Company status of a named counterparty

The library stores no status field: it does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Wherever an output names a licensor, licensee, partner, target, or a company the person says they hold, add a status line built from the company's own filings or register:

| Source | What it shows | What it does not mean | Rows |
|---|---|---|---|
| 8-K Item 1.03 | Bankruptcy or receivership: proceeding, court, date; a later 1.03(b) when a plan is confirmed | A first 1.03 with no later (b) report means the outcome is still open on EDGAR | DL-136; DL-137 (inference) |
| 8-K Item 2.01 | Completion of an acquisition or disposition: closing, not signing | A signing alone is Item 1.01 | DL-138 |
| 8-K Item 3.01 | Exchange deficiency notice, delisting application, or voluntary withdrawal or transfer | A deficiency notice is not yet a delisting; a 3.01 can mean a transfer, not distress | DL-139 (inference); DL-140 |
| 8-K Item 5.01 | Change in control: who, when, basis, percentage | | DL-141 |
| Form 25 | Exchange delisting; effective 10 days after filing; does not end Section 12(g) or 15(d) reporting | Not dissolution; after a merger it signals the old shares were converted, not that the business failed | DL-142 (inference); DL-143 to DL-145 |
| Form 15 | SEC reporting suspended; after a merger the successor files it | Not dissolution: the company stopped SEC reporting, not existing | DL-146; DL-147 (inference); DL-148; DL-149 (inference) |
| Companies House `company_status` | Twelve values, among them active, dissolved, liquidation, administration | "Active" can hide a pending strike-off | DL-157, DL-158; DL-159 (inference); DL-160 to DL-162; DL-163 (inference); DL-164 |
| German insolvency notices | Official site insolvenzbekanntmachungen.de | Notices are deleted after set periods, so no hit today does not prove no past insolvency | DL-165; DL-166 (inference); DL-167; DL-168 (inference) |
| FDA registration and listing | Who lists a device today (establishment, owner/operator, listing date) | Not a record of a sale or of who holds the rights; the 510(k) or De Novo page names the applicant at clearance or grant | SP-165 to SP-169 |

Steps:
1. Read the company's filings from the most recent backward, not only from the start of the period asked. A bankruptcy, acquisition, delisting or deregistration dated before the period governs the company's status within it (DL-136 to DL-149).
2. Where a row below covers the company, quote it with the filing's name and date. Where the assistant can open the filing or register itself, quote the item and its date. Otherwise write "Company status [GAP]: not read" and list the exact filings to open, most recent first.
3. State a product's current FDA listing holder separately from the company that was authorized.
4. Where the person says they hold a stake in, or a license from, a company whose filings show a change in control or a chapter 11 sale process, say the holding or the rights are unconfirmed until the person's own records are read.
5. Never infer status from press, memory or the date filings stopped. Requests to outside sites never carry the person's email address or name; EDGAR asks automated clients to declare a User-Agent contact (DL-153, [WF]): ask which contact the person's organization uses, or list the filings to open. A deeper status or profile goes to `company-and-evidence-assessment` (this pack).

### Status read on 20 October 2026 (SEC rows [WF]; FDA rows from openFDA registration and listing)

| Company | What its own filings or records state | What they do not show |
|---|---|---|
| Pear Therapeutics, Inc. (EDGAR CIK 1835567) | Pear 8-K filed 7 April 2023, Item 1.03: on 7 April 2023 Pear and Pear US filed chapter 11 in the US Bankruptcy Court for the District of Delaware, case no. 23-10429 (SP-156). Same 8-K: about 170 employees (92% of full-time staff) terminated, a transition team of about 15 kept (SP-158); Item 7.01: a section 363 bidding and auction process, no buyer named; "Holders of the Company's equity securities will likely be entitled to little or no recovery" (SP-159). Pear 8-K filed 10 April 2023, Item 3.01: Nasdaq staff gave notice of delisting because of the chapter 11 filing; trading suspended 19 April 2023; Pear did not appeal (SP-160). Form 25-NSE filed by Nasdaq, 2 May 2023, is the last filing; no Form 15 and no 8-K after 10 April 2023 (SP-155). | No SEC filing names a buyer of Somryst, reSET or reSET-O (SP-161); the court sale orders were not read. No 1.03(b) plan confirmation appears on EDGAR, so the outcome is open there (DL-137, inference). Form 25 is not dissolution (DL-144). |
| Akili, Inc. (EDGAR CIK 1850266; Akili Interactive Labs, Inc. is its wholly owned subsidiary, not a former name, SP-148) | Akili 8-K, 29 May 2024, Item 1.01: merger agreement with Virtual Therapeutics Corporation and Alpha Merger Sub, Inc.: cash tender offer at $0.4340 per share, then a merger with Akili surviving as a wholly owned subsidiary (SP-150). Akili 8-K, 2 July 2024, Items 2.01 and 5.01: the offer was completed on 2 July 2024, a change in control occurred, and Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation (SP-151); Item 3.01: Akili asked Nasdaq to file Form 25 and said it intends to file Form 15 (SP-152). Form 25-NSE filed by Nasdaq, 2 July 2024 (SP-153; form body not readable). Form 15-12G, 12 July 2024, about 1 holder of record (SP-154). After that, only third-party SC 13G/A filings (last 13 November 2024, SP-154). | Form 15 is not dissolution (DL-149, inference); after a merger, Form 25 signals the old shares were converted (DL-142, inference). The filings do not show any outside holder's position after the merger. |
| Big Health | EDGAR name lookup and Form D full-text search returned no entity: not shown as an SEC filer (SP-162, [WF]). FDA establishment BIG HEALTH INC, registration 3024442350, Newport Beach, active, registration year 2026; lists SleepioRx (K233577) and DaylightRx Treatment (K233872) (SP-163). | Status in any company register: not read `[GAP]`. |
| Aidoc Medical Ltd. | EDGAR name lookup returned no entity (SP-162, [WF]). FDA establishment AIDOC MEDICAL LTD., registration 3014938447, Tel Aviv-Yafo, active, registration year 2026, 25 device listings (SP-164). | Status in the Israeli company register: not read `[GAP]`. |

Any other company: "Company status [GAP]: not read", with the filings to open.

## 4. Library facts on a candidate product

A candidate's public authorization comes from the library (`regulatory-dh.search_devices`, or the identity block of `commercial-dh.generate_report`) with reference, decision date and retrieval date. Use FDA words: a 510(k) is "cleared", a De Novo "granted", a PMA "approved". State the company that was authorized and the company that lists the product today as two separate facts:

| Product | Authorized to (FDA record) | Listed today by (FDA registration and listing, read 20 October 2026) |
|---|---|---|
| Somryst | 510(k) K191716, applicant Pear Therapeutics, Inc., received 26 June 2019, decision 23 March 2020, substantially equivalent, regulation 882.5801, product code QVO (FDA 510(k) record, SP-165) | NOX MEDICAL, registration 3007389703, Reykjavik, Iceland, owner/operator Nox Medical; listing created 18 December 2024; names "Somryst" and "Somryst - CBT - I" (SP-167) |
| EndeavorRx | De Novo DEN200026, requester akili interactive labs, inc. (FDA De Novo record, SP-166) | "AKILIINTERACTIVE Labs, Inc. C/O Virtual Therapeutics", registration 3013341423, Kirkland, WA; a second listing cites K231337, created 25 June 2024 (SP-168) |
| reSET; reSET-O | De Novo DEN160018; 510(k) K173681 (resolved to Pear Therapeutics, Inc. in the library's saved output, 19 October 2026) | HARVEST BIO LLC, registration 3033280591, Middletown, CT; both listings created 14 November 2024 (SP-169) |

The library's saved output for Somryst (`examples/live/generate_report_somryst_commercial.json`, retrieved 19 October 2026) resolves the product to Pear Therapeutics, Inc. and stores a "latest 8-K" of 10 April 2023; Pear's EDGAR record shows a later Form 25-NSE of 2 May 2023 (SP-155), so the library's latest 8-K is not the latest filing. Reimbursement `[GAP]` (no reimbursement source loaded).

Whether rights to a product are available, held or encumbered is not in any library or FDA record `[GAP]`. A listing holder is the establishment that lists the device with FDA; the listing is not the sale record. For an in-license candidate whose authorized company went through chapter 11 (Somryst), the counterparty is unconfirmed: the authorized company filed chapter 11 with a section 363 sale process (Pear 8-K, 7 April 2023, SP-156, SP-159), and another company lists the device today (SP-167). Ask the person who they are negotiating with, and route the sale record (court case 23-10429) to the owner the person names for legal.
