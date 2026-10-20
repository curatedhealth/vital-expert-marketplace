# Worked run: A1, B1 and B2 on an illustrative product portfolio

Built 20 October 2026 while the library connector was disconnected. The four programs, their criteria, weights, scores, capacity and decisions are ILLUSTRATIVE inputs written for this build (`examples/sample-data/`), not any company's data or judgment. The one public-record item, Somryst, comes from saved library output (`examples/live/generate_report_somryst_commercial.json`, retrieved 19 October 2026). Computations come from `scripts/portfolio_rank.py` (`examples/live/portfolio_rank_runs_output.md`); the `analytics.mcda` call itself needs a live check, and the script reproduced the tool's formula exactly on a saved live response (77.5, 63.75, 62.5).

## The request (illustrative)

"Programs A to D are asking our Q1 portfolio board for funding. We are also weighing in-licensing the Somryst asset as Program E. Build the choice list, rank A to D on our scores, and draft the record once we decide." Forum and period given: "Q1 portfolio board"; period "next two quarters". Owner for legal: not named.

## A1 Choice list (short mode)

**Answer:** Q1 portfolio board, next two quarters: 4 items ready, 1 not ready. The gap that blocks most: Program E has no stage gate record, and its counterparty is unconfirmed.

| Item | Ask | Stage (yours) | Stage gate record | Key facts | Gaps | Source |
|---|---|---|---|---|---|---|
| A insomnia DTx label expansion | continue | post-market | Gate 4, 2 September 2026 | Pivotal readout in hand | none named | your records |
| B anxiety DTx pivotal study | continue | pivotal planning | Gate 3, 15 July 2026 | Protocol draft | regulatory route `[GAP]` | your records |
| C clinician dashboard add-on | continue | build | Gate 2, 1 August 2026 | Not a device in your statement | device status is the developer's call (NHS AI and Digital Regulations Service, SP-129) | your records |
| D pediatric ADHD prototype | delay | concept | Gate 1, 10 June 2026 | TRL 3 "Experimental proof of concept", proposed (Horizon Europe 2026-2027 Annex XV, SP-029; NASA 7 to 9 assume space and flight, SP-035) | evidence plan not given | your records |

**Not ready:** Program E (in-license Somryst): no stage gate record; route to `dh-clinical-development` clinical-product-lifecycle-and-stage-gates.

**Program E facts:** Somryst, 510(k) K191716, cleared to Pear Therapeutics, Inc., 23 March 2020 (FDA 510(k) record, SP-165). Listed with FDA today by Nox Medical, since 18 December 2024 (FDA registration and listing, read 20 October 2026, SP-167). Who holds the rights: `[GAP]`. Reimbursement `[GAP]`.

**Company status, Pear Therapeutics (SEC filings, [WF]):** Pear 8-K, 7 April 2023: chapter 11 in the District of Delaware, case 23-10429 (SP-156), section 363 sale process, no buyer named (SP-159). Pear 8-K, 10 April 2023: Nasdaq delisting notice (SP-160). Form 25-NSE, 2 May 2023, the last filing (SP-155). No SEC filing names a buyer of Somryst (SP-161). Form 25 is not dissolution (DL-144). Pear may no longer hold Somryst: who are you negotiating with?

**Licensing flags for the owner you name for legal (owner not named):** E and A both address insomnia: do the parties compete? That selects the condition (Regulation (EU) 2026/877 of 16 April 2026, SP-136):

| Condition | Threshold | Your figure |
|---|---|---|
| Competitors | combined share at most 20% on any relevant market | not given |
| Non-competitors | each party at most 30% on any relevant market | not given |
| US safety zone (DOJ/FTC Guidelines, 12 January 2017, SP-144) | at most 20% of each relevant market significantly affected | not given |

The transition to 30 April 2027 covers only agreements in force on 30 April 2026, so not a new license (SP-137). If patient data moves, GDPR Article 9 is flagged (DL-101, DL-105, DL-106). Not given: relevant market, shares, competitor status, data moved. No conclusion on exemption.

Want the full version with the deal facts table?

**Record:** Choice list draft. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 Rule and ranking (short mode)

**Your rule (confirmed before ranking):** unmet need 0.30, evidence readiness 0.25, regulatory path clarity 0.15, strategic fit 0.20, capacity fit 0.10 (4 = least capacity used); decision rule "continue in rank order until the named capacity is used"; capacity 14 FTE, next two quarters.

| Rank | Item | Value | Largest contribution |
|---|---|---|---|
| 1 | A insomnia DTx label expansion | 85.00 | evidence readiness (25.00) |
| 2 | B anxiety DTx pivotal study | 72.50 | unmet need (30.00) |
| 3 | C clinician dashboard add-on | 65.00 | evidence readiness (18.75) |
| 4 | D pediatric ADHD prototype | 60.00 | unmet need (30.00) |

EVIDEM weighted sum on your weights and scores; arithmetic, not a decision (SP-080, [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016).

**Closest call:** C stays above D unless unmet need rises from 0.30 to 0.36 (`swap`). At the capacity line, B (72.50) and C (65.00) differ by 7.50; one point on unmet need is worth 25 x 0.30 = 7.50, so B's need score falling from 4 to 3, or C's rising from 2 to 3, ties them (`swap --scores`). A test of your scores, not a proposal.

**Double counting, for you to decide:** capacity fit is scored and capacity is also the cut. B scores 1 of 4 on capacity fit, which costs it 7.50 points against a top score (3 points x 25 x 0.10), and its 7 FTE then count again at the 14 FTE line (ISPOR MCDA Report 2, Marsh et al. 2016, SP-077, [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016). Keep both, or drop one?

**Implied by your rule:** A (5 FTE) and B (7 FTE) fit in 14 FTE; C (3 FTE) would take the total to 15 and is the first item past the capacity. Your rule places D last.

**Record:** Ranking draft. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B2 Decision record (short mode, after the illustrative forum)

**Answer:** Q1 portfolio board, decider as you named, date as you gave it: continue 3 (A, B, C), delay 1 (D). Capacity: continue items use 15 of your 14 FTE; C is the first item past it. Open item that blocks most: the capacity overrun has no owner.

| Item | Rank | Implied by your rule | Decision (yours) | Reason where they differ |
|---|---|---|---|---|
| A | 1 | continue | continue | n/a |
| B | 2 | continue | continue | n/a |
| C | 3 | delay (past capacity) | continue | reason not given; ask |
| D | 4 | delay | delay | n/a |

**Open items:** capacity overrun on C, owner not named, blocks C's start, reread date not given. Program E stays off the list until a stage gate record and the legal owner's view exist.

**Record:** Decision record draft for the owner. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made: none live (connector disconnected 20 October 2026). Library facts from `examples/live/generate_report_somryst_commercial.json` (19 October 2026). Company status and listing holder from the research rows read 20 October 2026 (SP-155 to SP-167). Ranking, swap points, one-point score changes and capacity from `scripts/portfolio_rank.py` on `examples/sample-data/`.
