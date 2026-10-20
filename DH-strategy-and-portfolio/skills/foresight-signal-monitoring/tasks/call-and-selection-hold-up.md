# A2 Call and selection hold-up read

Framework task: Part A, task A2. Replaces the old tasks DH-01.05.3.2.1 Foresight Prediction Quality Monitoring and DH-01.08.1.2.1 Technology Selection Quality Monitoring.

## What this task delivers

For each past foresight call and each technology selection in the person's log: the call or selection as made, its date, the person's resolution or hold-up rule, what the record shows now (with identifier, date and retrieval date), and a proposed outcome by the person's rule (hit, miss, open, void, or not resolvable), with what the record cannot measure. Counts by the person's outcomes follow, with the denominator stated. It answers "which of our calls came true by our own rules, which selections still meet our test, and which cannot be judged from the record?"

Why it matters: "our foresight was right" is easy to claim and hard to check. A read against rules written before the outcome, on dated records, separates what was right from what was lucky, unresolved or unmeasurable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Compliance Officer (`chief-compliance-officer-digital-health`), as bound to DH-01.05.3.2; Technology Selection Quality Monitoring came from DH-01.08.1.2 (`behavior-change-designer`). Better-fitting experts are proposed in the build notes, not bound |
| Skill | DH-01.05.3.2 and DH-01.08.1.2 Part A, Call and selection hold-up read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 3 to 6; `references/company-status.md` (DL-135 to DL-168; status already read for Akili, Pear, Big Health and Aidoc, SP-148 to SP-169) |
| Tools | `regulatory-dh.search_devices`; `regulatory-dh.get_pathway_precedents`; `regulatory-dh.search_safety_events` (only where a rule names recalls); `diligence-dh.get_deltas`; `diligence-dh.get_funding_signals` (only to find a filing URL); `scripts/foresight_check.py` |
| Prompt | This guide |
| Template | `assets/hold-up-read-output.md` |
| Input | The request and its context: the foresight log (calls and selections with made-on dates, horizon dates, resolution or hold-up rules, any recorded outcomes), the read date, the scan's saved outputs |
| Governance | `references/governance.md`; rules and outcomes are the person's; no person is scored |
| Catalogue job | none |

## Read the request

- **Calls and selections.** From the log. Each needs a date it was made and, for a call, a horizon date.
- **Rules.** The person's resolution rule per call and hold-up rule per selection. Missing: "not resolvable: rule not given"; propose a rule only if asked, labeled "proposed", not applied until confirmed.
- **Read date.** Today unless given.
- **"How accurate are we?"** Counts by their outcomes; no benchmark exists (`monitoring-signals.md` section 6).

## Workflow

### Step 1. Run the checker

Run `python3 scripts/foresight_check.py --log LOG.csv --as-of YYYY-MM-DD`. Take R1 (rule not given), R2 (horizon passed, outcome not recorded), R3 (outcome without evidence), R4 (data error) and R5 (outcome rests on the change log before it began) from its output.

### Step 2. Read the record for each call

For each call whose horizon has passed, or that the person asks about: read the record the rule names. Counts: `regulatory-dh.get_pathway_precedents {product_code}` (QAS: 15 decisions in 2025; 10 in 2026 to 16 September 2026; a partial year does not resolve a year-end call). Clearances: `regulatory-dh.search_devices`. Rules: the research rows (the FDA AI lifecycle guidance was still draft on 19 October 2026, US-21; a call that it would be final by 30 September 2026 is a proposed miss by that rule). Write "proposed outcome by your rule", the evidence, and the date read.

### Step 3. Read the record for each selection

Apply the person's hold-up rule (`monitoring-signals.md` section 4). Saved examples: EU "Briefcase-Triage" still "On the EU market" (retrieved 14 October 2026); ORTEC "Stroke Triage App" "No longer placed on the EU market" (retrieved 14 October 2026). Where a rule rests on the maker still existing, add the company status line (`company-status.md`): for Akili, Pear Therapeutics, Big Health and Aidoc, the status already read (section 6), cited by filing name and date with the row id after it; for any other company, "Status: [GAP]: not read" with the filings to open. Name the newest stored filings by type and date as the first to open, and ask the person to open them or give a contact for EDGAR requests (never invent one, DL-153). State a product's current FDA listing holder apart from the company that was authorized.

Example, Pear Therapeutics, Inc. (rule "partner still operating and filing", horizon 1 September 2024). The two newest stored filings (`examples/live/funding_signals_pear.json`) are the 8-Ks of 7 April 2023 and 10 April 2023, and both are read: chapter 11 filed 7 April 2023 in the US Bankruptcy Court for the District of Delaware, case no. 23-10429, with about 170 employees (92% of full-time staff) terminated and a section 363 sale process (Pear 8-K, filed 7 April 2023, Items 1.03, 2.05, 7.01; SP-156, SP-158, SP-159 [WF]); Nasdaq delisting notice of 10 April 2023, trading suspended 19 April 2023 (Pear 8-K, filed 10 April 2023, Item 3.01; SP-160 [WF]); last filing a Form 25-NSE of 2 May 2023, no Form 15 and no 8-K after 10 April 2023 (Pear EDGAR record; SP-155 [WF]). Read each part of the rule: "filing": no Pear filing after 2 May 2023 on EDGAR, before the 1 September 2024 horizon; "operating": an Item 1.03 is not liquidation (DL-136), no later Item 1.03(b) report is on EDGAR (DL-137) (inference), and the court records were not read, so not resolvable from what was read. Proposed outcome by your rule: miss (the "filing" part is not met), for the person to confirm against their recorded "hit". reSET is listed with FDA today by Harvest Bio LLC (listing created 14 November 2024; SP-169), which is not the sale record and not a statement about Pear. `diligence-dh.get_deltas` "no change recorded" for Pear says nothing before 12 October 2026 (R5). Performance in the person's own use needs their data.

### Step 4. What the record cannot measure

List calls and selections whose rule needs adoption, uptake, revenue, clinical effect or user satisfaction: "not measurable from the record; needs your data". Never fill them from press.

### Step 5. Counts

From the script: counts by kind and the person's recorded outcomes, and the hit share with its denominator (open and void outside it). Proposed outcomes from Steps 2 and 3 are shown beside the recorded ones and are not counted until the person confirms them; what would change if they were confirmed is computed with `--if-confirmed "F5=miss;F7=miss"`, never estimated. No accuracy benchmark exists; never compare.

## Build the output

Follow `assets/hold-up-read-output.md`. Answer first: per kind, how many hit, missed, are open, or cannot be resolved, the proposed outcomes awaiting the person's confirmation, and the limit that most affects the read (a log that began 12 October 2026, an unread company status). Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every outcome is the person's or "proposed outcome by your rule", with evidence and read date.
- No call resolved before its horizon; no resolution from an empty log, press or memory.
- Company status line present for every selection that rests on a company, from the status already read or "[GAP]: not read" with the newest stored filings named; current FDA listing holder stated apart.
- No reread date, owner or threshold supplied; every owner gap (O1) kept; log-owner conflicts (O4) shown with both names.
- Every fact names its source in plain words with its date, then the row id; [WF] and (inference) labels every time.
- No benchmark and no score of any person or team.
- The record line is the very last line of the answer; the calls list and the one-line offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Signal quality: A1. Pass rule, miss owners and feedback: B1.
- Investment holdings or targets: `investment-portfolio-monitoring`, `pipeline-and-market-monitoring` (this pack).
- Partner health: `dh-go-to-market` channel-and-partnership-monitoring.
