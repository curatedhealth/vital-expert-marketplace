# Monitoring signals, foresight calls and technology selections

Interpretive reference for all three tasks. Rows: SP (`strategy-and-portfolio-sources.md`), US, EU, UK (`ai-ml-regulation-research.md`), DL (`diligence-research.md`). [PAPER] rows carry their DOI; [WF] rows are flagged each time.

## 1. What this monitoring is, in the sources

| Rule | Rows |
|---|---|
| Horizon scanning uses trusted sources, a defined scope and prespecified methods (NIHR IO summary of its paper; paper not read) | SP-004 |
| Records are triangulated and monitored to track technologies through the pipeline and trigger notifications | SP-005 |
| Early awareness methods run identification, filtration and prioritization, assessment, dissemination ([PAPER] Packer 2015, DOI 10.1017/S0266462315000100) | SP-009 |
| Reactive identification tends to catch devices only at or near approval ([PAPER] Ormstad 2023, DOI 10.1017/S0266462323002684) | SP-015 |
| UK public-sector guidance: a proposal moves through rationale, objectives, appraisal, monitoring, evaluation and feedback (ROAMEF); evaluation assesses an intervention after implementation and should be planned from the outset | SP-090, SP-091 |
| UK benefits guidance (written for commercial benefits): reports compare baseline, target and actuals; a first review at 12 months of contract delivery and at least every 12 months after | SP-104, SP-105 |
| MCDA results should be validated and consistency tested, for example by eliciting preferences more than once ([PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]) | SP-075, SP-081 |

How the skill uses it: A1 checks the identification and filtration steps (are the signals records, dated, sourced, deduplicated?); A2 is the evaluation step for past calls and selections; B1 is the feedback step, against the person's pass rule, back into `horizon-scanning-and-technology-evaluation` (this pack). The ROAMEF and benefits terms are UK public-sector guidance; when a company uses them, say so. The 12-month benefits review cadence (SP-105) is context for a UK government commercial contract, never the person's cadence; their reread dates are theirs.

## 2. Signal quality checks (proposed checks; the pass rule is the person's)

No source sets a signal quality standard or an acceptable false-positive rate. The checks below are "proposed checks" derived from the rows named; the person adopts, drops or adds to them and sets the pass rule.

| Check | What fails it | Basis |
|---|---|---|
| Q1 Record, not talk | Source is a press release, news item, vendor page or blank: a lead, not a signal | SP-004 ("trusted sources"); the research rules exclude news and vendor pages |
| Q2 Dated | No event date (decision, filing, publication or application date); a press or load date used instead | SP-005 (tracking needs dates); `tools.md` (the library filters on event dates) |
| Q3 Sourced | No URL or identifier to reopen the record | SP-005 (triangulation) |
| Q4 Limits stated | No line on what the record does not show (for example a clearance says nothing on AI use, PCCP or uptake) | US-25 (the AI list is not comprehensive); `tools.md` |
| Q5 Deduplicated on identifiers | Same product logged twice under different spellings | `tools.md` (names differ across registers) |
| Q6 Signal kept apart from trend | A trend or forecast logged as if it were a record | Pack rule: a trend is the person's interpretation |
| Q7 Still true on reread | The record now says something else (for example an EU row "No longer placed on the EU market") | SP-005 (records are monitored) |
| Q8 Status of rule signals | A draft, pilot or proposal logged as final | US-21 (lifecycle draft), SP-124 (IDAP pilot closed), UK-04 (MHRA PCCP draft not published) |

A false positive is what the person's definition says it is. If they gave none, list candidates as "proposed false positive" with the failed check.

## 3. Resolving a foresight call

- **The resolution rule is the person's,** written before the outcome is read ("count of 2026 QAS decisions exceeds 15 at 31 December 2026"). Without one, the call is "not resolvable: resolution rule not given"; the model may propose a rule, labeled "proposed", and does not apply it until confirmed.
- **What the record can resolve:** a clearance or listing exists by a date; a register status changed; a rule became final or applies from a date; a trial was registered; a company filed an 8-K item. Each with identifier and date.
- **What the record cannot resolve:** adoption, uptake, revenue, clinical effect, user satisfaction, whether a technology "won". Those need the person's own data or stay "not measurable from the record".
- **Horizon not reached:** the call is open, whatever the record shows so far (a partial-year count is not a resolution).
- **Change logs:** the regulatory change log returned "no watch is registered for this scope; the change log has not started" on 19 October 2026; the company change log began on 12 October 2026. A call made before the log began cannot be resolved from the log: read dated records (`search_devices`, `get_pathway_precedents`, filings) instead. "No change recorded" never resolves a call.
- **The outcome is the person's to record.** The model writes a "proposed outcome by your rule" with its evidence; the person confirms it.

## 4. Did a technology selection hold up?

The selection rule is the person's ("still on the EU market at reread", "partner still operating and filing", "no recall naming the product"). What the record can show:

| Question | Record | Rows or tools.md |
|---|---|---|
| Still placed on the EU market | EUDAMED status in `search_devices` ("On the EU market", "No longer placed on the EU market"), by Basic UDI-DI | `tools.md` |
| New US clearances or a new product code | `search_devices`, `get_pathway_precedents` | `tools.md` |
| Recall or alert naming the product | `search_safety_events` (check the filter matched the product; describe the record only) | `tools.md` |
| The maker still exists, was acquired, delisted, deregistered or is insolvent | The company's own filings or register (`company-status.md`); already read for Akili, Pear, Big Health and Aidoc (section 6) | DL-135 to DL-168; SP-148 to SP-164 |
| Who lists the product with FDA now | FDA registration and listing, stated apart from the company authorized (Somryst: Nox Medical; EndeavorRx: Akili c/o Virtual Therapeutics; reSET and reSET-O: Harvest Bio) | SP-165 to SP-169 |
| Performance in the person's own use | The person's data only | Not in the library |

Never call a selection "bad" or "good"; it met or did not meet the person's rule, on the record read, as of the read date. Where a rule has two parts joined by "and" ("still operating and filing"), read each part on its own record: a part the record answers is stated; a part it cannot answer stays "not resolvable from what was read"; the proposed outcome by the rule follows from both, and the person confirms it.

## 5. Dated changes since a scan (rules and programs)

Reuse the table in the sibling skill horizon-scanning-and-technology-evaluation (this pack), its horizon-methods reference, section 4; the rows are copied here so this skill stands alone: AI Act high-risk dates moved by Regulation (EU) 2026/1744 (EU-17 to EU-19, new prohibited points from 2 December 2026, EU-21); FDA AI lifecycle guidance still draft on 19 October 2026, on the FY 2027 A-list (US-21, US-22); MHRA PCCP draft guidance announced, not published (UK-04); AI Airlock phase 3 announced 6 October 2026 (UK-07); FDA TAP expanded 1 July 2026 (SP-122); RAPID announced 23 April 2026 (SP-123); IDAP pilot closed (SP-124); EHDS dates (SP-068 to SP-073); WHO strategy extended to 2027 (SP-066); TTBER 2026/877 from 1 May 2026 with transition to 30 April 2027 (SP-135, SP-137); ISO 56000:2020 withdrawn 23 January 2025 [WF] (SP-046).

## 6. Measures

- Counts by the person's outcomes: hit, miss, open, void, not recorded, per kind (signal, call, selection).
- Hit share = hits divided by (hits plus misses), with the denominator stated; open and void rows are outside it.
- Lead time (signal date to resolution date) only where both dates are records.
- No source sets an accuracy benchmark, a calibration score, a target hit rate or an acceptable false-positive rate: write "[GAP]: no benchmark in the sources" and never compare the person's log with one. Scoring rules for probabilistic forecasts are not sourced here; if the person uses one, the arithmetic is theirs and the method is labeled "your method".
