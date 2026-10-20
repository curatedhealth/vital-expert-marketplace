# Worked example: option landscape and choice for a pediatric ADHD digital therapeutic

Runs A1 and B1 of `strategic-vision-and-options` on saved live library data (19 October 2026), the company status rows of the research pass (read 20 October 2026, SP-148 to SP-169) and an illustrative set of the person's scores. The connector was disconnected on 20 October 2026, so no new library call was made; every library fact below comes from `examples/live/partner_profile_akili.json`. The scores and weights in `examples/live/option_scores_illustrative.json` are ILLUSTRATIVE, typed for this example; they are not any company's real scores, and the vision sentence is invented.

## Request (A1)

"We have an ADHD franchise and want a prescription digital therapeutic our franchise can offer to children in the US. Options on the table: build it ourselves, co-develop with a partner, or in-license something already cleared, for example Akili's EndeavorRx. I read Akili was bought last year. Lay out the options and what the record shows."

## Calls (from saved outputs)

| Step | Call | Saved file | Retrieved |
|---|---|---|---|
| A1 step 6 | `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}` | `examples/live/partner_profile_akili.json` | 19 October 2026 |
| A1 steps 6 and 7 | `python3 scripts/options_check.py facts --profile examples/live/partner_profile_akili.json` | script output, below | 20 October 2026 |
| B1 steps 2 and 3 | `python3 scripts/options_check.py rank --input examples/live/option_scores_illustrative.json` | script output, below | 20 October 2026 |
| B1 step 3 check | `analytics.mcda` arithmetic, as reproduced on `examples/live/mcda_partner_options.json` (values 77.5, 63.75, 62.5 match) | `examples/live/mcda_partner_options.json` | 19 October 2026 |

`analytics.mcda` was not called on the illustrative ADHD scores (connector disconnected): **needs a live check** that the library returns 78.75, 65 and 58.75 and a 400 for the unscored option.

## Script output: candidate facts and status

```
Company: Akili Interactive Labs, Inc. (library, retrieved 19 October 2026)
Identifiers: EUDAMED_SRN US-MF-000048993; SEC_CIK 0001741200

| Product | Reference | Pathway in words | Product code | Decision date | Source |
|---|---|---|---|---|---|
| EndeavorOTC | K233496 | 510(k) cleared | QFT | 14 June 2024 | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K233496 |
| EndeavorRx | K231337 | 510(k) cleared | QFT | 13 December 2023 | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K231337 |
| EndeavorRx | DEN200026 | De Novo granted | QFT | 15 June 2020 | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm?id=DEN200026 |

Registered studies: 10 in total, 3 linked by brand, 6 by indication only (registry records, not results).
Evidence maturity (library convention, not an evidence verdict): 100 (90 of 90 assessable points), rubric v1 (7 October 2026), excluded: reimbursement, jurisdiction_breadth.
Form D filed 9 June 2021: amount as stored USD 110,000,007. A Form D shows no valuation or investor names (DL-016; DL-018, an inference); the amount may be stale (DL-006).
Form D filed 23 May 2018: amount as stored USD 55,000,010. A Form D shows no valuation or investor names (DL-016; DL-018, an inference); the amount may be stale (DL-006).
Private rounds: [GAP] (no funding source licensed; register C2).
Reimbursement: [GAP] in this call; reimbursement status is dh-access-and-value coverage-pathway-and-access-strategy.

Company status as read in the research pass (20 October 2026; the library stores no status field):
- Akili, Inc. (EDGAR CIK 1850266; Akili Interactive Labs, Inc. is its wholly owned subsidiary, not a former name) (Akili, Inc. EDGAR submissions record, read 20 October 2026, SP-148 [WF]).
- Akili 8-K, 29 May 2024: Item 1.01 merger agreement with Virtual Therapeutics Corporation, tender offer at $0.4340 per share (SP-150 [WF]). Signing, not closing (SEC Form 8-K instructions, DL-138).
- Akili 8-K, 2 July 2024: Item 2.01 offer completed 2 July 2024; Item 5.01 change in control, Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation; Item 3.01 Nasdaq asked to file Form 25 (SP-151, SP-152 [WF]).
- Akili Form 25-NSE, 2 July 2024, filed by Nasdaq; body not readable (SP-153 [WF]). Form 25 concerns the listing only (SEC Rule 12d2-2, DL-144); after a merger it signals converted shares, not failure (DL-142, inference).
- Akili Form 15-12G, 12 July 2024 (SP-154 [WF]): SEC reporting stopped; not dissolution (SEC Rule 12h-3, DL-149, inference). No later Akili filing will disclose a license or deal.
- EndeavorRx: De Novo DEN200026 requester akili interactive labs, inc. (FDA De Novo record, SP-166); listed now by "AKILIINTERACTIVE Labs, Inc. C/O Virtual Therapeutics", Kirkland, WA, registration year 2026 (FDA registration and listing database, read 20 October 2026, SP-168). The listing holder is not proof of who can grant a license.
- Virtual Therapeutics Corporation: Company status [GAP]: not read (no row).
- The library profile carries CIK 0001741200; the status above is for the listed entity, CIK 1850266. Say which entity each fact belongs to.
- Status is as of 20 October 2026; a later filing can change it. In the answer, name the option this status blocks and what would unblock it (option-frameworks.md section 5).
```

## A1 short answer (400 words by `options_check.py words`)

**Answer.** Your opportunity is a prescription digital therapeutic for children with ADHD in the US: three options plus business as usual. EndeavorRx is De Novo granted, but its maker Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation on 2 July 2024, not last year, so the in-license option cannot be scored on counterparty terms until you confirm which legal entity holds the authorizations and would grant the license.

**Opportunity (your words):** "a prescription digital therapeutic our ADHD franchise can offer to children in the US". Proposed: WHO axis "digital health interventions" (WHO Classification of digital interventions, 2023, SP-056); Oslo type product innovation (Oslo Manual, 2018, SP-038). TRL not proposed: state of your own technology not given.

**Options**

| Option | What must be true (your words) | Facts that bear on it | Source and rows |
|---|---|---|---|
| Business as usual | not given | Outcome if current arrangements continue (UK public-sector guidance) | HM Treasury Green Book, 5 February 2026, SP-093 |
| Build in house | not given | No cleared product of yours in the request | none |
| Co-develop with a partner | not given | Partner not named | none |
| In-license EndeavorRx | not given | Blocked: licensor's legal entity not confirmed (status below) | SP-151, SP-168 |

**Candidate**

| Product | Authorization | Listed now by | Source and rows |
|---|---|---|---|
| EndeavorRx | De Novo granted 15 June 2020 (DEN200026); 510(k) cleared 13 December 2023 (K231337) | Akili Interactive Labs c/o Virtual Therapeutics, Kirkland, WA | library, retrieved 19 October 2026; FDA registration and listing, read 20 October 2026, SP-168 |
| EndeavorOTC | 510(k) cleared 14 June 2024 (K233496) | not in the rows read | library, retrieved 19 October 2026 |

**Company status.** Akili, Inc. signed a merger agreement with Virtual Therapeutics Corporation (Akili 8-K, 29 May 2024, SP-150 [WF]); the offer completed and control changed on 2 July 2024 (Akili 8-K, 2 July 2024, Items 2.01 and 5.01, SP-151 [WF]); Nasdaq filed Form 25 the same day (SP-153 [WF]) and Akili filed Form 15 on 12 July 2024 (SP-154 [WF]). Form 25 concerns the listing only (DL-144); Form 15 means reporting stopped, not dissolution (DL-149, inference). No Akili filing will disclose a future license. Virtual Therapeutics: Company status [GAP]: not read.

**For your legal owner:** DOJ/FTC IP Licensing Guidelines, 12 January 2017: safety zone at no more than 20% of each relevant market (SP-144, SP-147). Your share: not given. Conclusion for the owner you name, or owner not named.

**Gaps:** licensor's legal entity (not given); Virtual Therapeutics status (not read); pivotal study behind DEN200026 (decision summary not read); what must be true per option (not given).

**Calls made:** connector unavailable on 20 October 2026; saved `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}` of 19 October 2026; status from research rows SP-148 to SP-168. Full version with the landscape tables on request.

Option landscape draft. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Script output: ranking on the person's scores

```
Scored by: Portfolio steering group, scoring session of 14 October 2026

Arithmetic on the person's scores, not a decision (EVIDEM weighted sum, 0 to 4).
| Option | Value | Contributions |
|---|---|---|
| In-license a cleared product | 78.75 | capital_need_avoided 7.5; control_of_roadmap 3.75; evidence_in_hand 25; speed_to_first_use 20; strategic_fit 22.5 |
| Co-development partnership | 65 | capital_need_avoided 7.5; control_of_roadmap 7.5; evidence_in_hand 12.5; speed_to_first_use 15; strategic_fit 22.5 |
| Build in house | 58.75 | capital_need_avoided 2.5; control_of_roadmap 15; evidence_in_hand 6.25; speed_to_first_use 5; strategic_fit 30 |
| Acquire a company | not ranked | not scored on capital_need_avoided |

Swap points (weight on one criterion at which two adjacent options tie; other weights rescaled in proportion). Facts about the person's weights, not advice:
- In-license a cleared product and Co-development partnership tie when the weight on control_of_roadmap is 0.452 (yours: 0.15).
- Co-development partnership and Build in house tie when the weight on control_of_roadmap is 0.244 (yours: 0.15).
- Co-development partnership and Build in house tie when the weight on speed_to_first_use is 0.086 (yours: 0.2).
- Co-development partnership and Build in house tie when the weight on strategic_fit is 0.44 (yours: 0.3).

Tie scores for Acquire a company (not ranked; not scored on capital_need_avoided). Sum on the criteria scored: 77.5. Arithmetic on the person's scores; the missing score is the person's and is never filled in.
- ties In-license a cleared product (78.75) at a capital_need_avoided score of 0.5 (0 to 4); any higher score puts it above.
- already at or above Co-development partnership (65) with any score from 0.
- already at or above Build in house (58.75) with any score from 0.
TOP NOT SETTLED: an unranked option's tie score with first place lies inside the 0 to 4 scale. Do not say first place holds; say which empty cell decides the top.

Every criterion is read as higher-is-better (register C17): name criteria so a higher score is better.
```

## Request (B1)

"Our vision: 'Every child in our ADHD franchise has a cleared digital therapy option by the end of 2028.' Our steering group scored the options (attached). Rank them and tell us how solid the order is, and what industry success rate should we assume?"

## B1 short answer (354 words by `options_check.py words`)

**Answer.** On your steering group's scores, in-licensing ranks first (78.75), co-development second (65), build third (58.75). The top is not settled: acquisition, unscored on capital need avoided, sums 77.5 on the other four criteria and passes in-licensing at any score above 0.5 of 4, so that empty cell decides first place. Decision not given.

**Vision and objectives.** Vision as written. Objective "offer a cleared digital therapy in the US": specific yes; measurable not given; achievable and realistic not given; time-limited yes (end of 2028). SMART is UK public-sector guidance used as a checklist (HM Treasury Green Book, 5 February 2026, SP-092).

**Ranking on your scores** (arithmetic on your scores, not a decision)

| Option | Value | Largest contributions | Not ranked |
|---|---|---|---|
| In-license a cleared product | 78.75 | evidence in hand 25; strategic fit 22.5; speed 20 | |
| Co-development partnership | 65 | strategic fit 22.5; speed 15 | |
| Build in house | 58.75 | strategic fit 30; control of roadmap 15 | |
| Acquire a company | 77.5 on four criteria | evidence in hand 25; strategic fit 22.5 | ties first at capital need avoided 0.5; above co-development and build at any score |

**Swap points (computed):** in-license and co-development tie if the weight on control of roadmap rises from 0.15 to 0.452; co-development and build tie if strategic fit rises from 0.3 to 0.44, control of roadmap from 0.15 to 0.244, or speed falls from 0.2 to 0.086. Your call whether those weights are firm.

**Sensitivity.** No cost or benefit inputs given, so no scenario or tornado run; every parameter would need your own range.

**Benchmarks.** 13.8% of drug development programs reached approval, 2000 to 2015, path-by-path method (Wong, Siah and Lo 2019, SP-082, SP-085, DOI 10.1093/biostatistics/kxx069). It covers drugs; no sourced rate exists for digital therapeutics [GAP]. Context only, never your probability.

**Decision record:** decision, decider, date, dissent and conditions not given; ask.

**Open items:** capital need avoided score for acquisition (owner not named, date not given); the licensor's legal entity for EndeavorRx (owner not named).

**Calls made:** connector unavailable on 20 October 2026; ranking and tie scores from `scripts/options_check.py rank` on the illustrative scores; the same arithmetic matched a saved `analytics.mcda` call. Full version on request.

Vision and option record draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What the example shows

- The model never names the winner, and it does not say the order holds while one empty cell can change first place: the tie score is computed from the person's scores.
- Company status is quoted from Akili's own filings by name and date, with what each form does not mean; the press remark is checked against the record and its date corrected.
- The status is tied to the option it blocks (in-licensing) and to what would unblock it (the licensor's legal entity).
- The authorization holder and the current FDA listing holder are stated separately.
- The success rate asked for is quoted with its method and population and refused as the person's probability.
- The record line is the very last line; the calls list and the offer of the full version come before it.
