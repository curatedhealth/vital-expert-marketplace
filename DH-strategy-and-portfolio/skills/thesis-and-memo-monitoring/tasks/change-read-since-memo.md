# A2 Change read since the memo

Framework task: DH-DIL.4.2, Part A, task A2. Carries the old tool skill "Read company changes" (`diligence-dh.get_deltas`) as it serves a thesis.

## What this task delivers

A dated read of what changed since the memo date: in the company's record (authorizations, studies, safety events, SEC filings), in the library's evidence maturity for the company, and in the deal rules the memo flagged (HSR, EU and Swiss screening, Companies House). Each change carries its event date, source and retrieval date; each rule change its instrument and date. The read says plainly what the library cannot see, and quotes the change log's start and last sweep beside every "no change recorded". It answers "has anything moved that our memo rests on?"

Why it matters: a memo fact can stop being true without anyone touching the memo. The library's change log filters on event dates and began on 12 October 2026 in the saved run, so a quiet result can mean "nothing in the log" rather than "nothing happened"; the read must say which.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who re-reads and checks |
| Skill | DH-DIL.4.2 Part A, Change read since the memo |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 2 to 6 (section 6: company status, DL-135 to DL-168); rows DL-002, DL-005, DL-006, DL-016, DL-018 to DL-024, DL-036, DL-041 to DL-054, DL-074, DL-075, DL-081, DL-082, DL-085, DL-113 (DOI 10.1038/s41746-023-00836-5) |
| Tools | `diligence-dh.list_sources` (free; needs a live check); `diligence-dh.get_deltas`; `diligence-dh.get_funding_signals`; `diligence-dh.get_evidence_maturity`; `diligence-dh.build_company_profile` (memo dated before the log began); `scripts/thesis_check.py` |
| Prompt | This guide |
| Template | `assets/change-read-output.md` |
| Input | The request and its context: the memo date, the companies (exact references), the memo's fact base or an earlier saved run, the deal rules the memo flagged |
| Governance | `references/governance.md`; companies described by their record only |
| Catalogue job | none started (old menu: `market-screen` for Read company changes; steps not saved, needs a live check) |

## Read the request

- **Since when.** The memo date, or the earlier run's date. If not given, ask; never pick one.
- **Companies.** Exact references, up to 12 per `get_deltas` call.
- **Earlier run.** The memo's fact base or saved outputs. Without one, a rerun gives a baseline, not a change; say so.
- **Rules.** The regimes the memo flagged (from `investment-memo-and-decision-record` A2, or the person).

## Workflow

### Step 1. Perimeter (free)

Call `diligence-dh.list_sources {}` (needs a live check). Note what is not loaded (Companies House, Zefix, private rounds) and any load date after the memo date.

### Step 2. Record changes since the memo date

Call `diligence-dh.get_deltas {companies: ["<exact names>"], since: "<memo date, YYYY-MM-DD>"}`. Report each change with its event date, type and URL. For every "no change recorded", quote the log: first entry, last sweep, and "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at". If the memo date is earlier than the log's first entry, flag T5, say plainly that the log cannot show the period from the memo date to 12 October 2026, and go to Step 3 for that company: offer its dated primary filings and authorization records for that period instead of reporting "no change". Never use `commercial-dh.get_deltas` (it drops the log block; register C12). Never call `watch_companies`.

### Step 3. Filings and authorizations by date (always for funding; for the record when T5)

Call `diligence-dh.get_funding_signals {company}` and compare counts by type and the latest date with the memo's run. Report new rows by type, date and URL. A new 8-K is opened at its URL to see its item (no item number is stored); Item 1.01, 2.01 and 1.05 are the ones a thesis usually rests on (DL-020, DL-022, DL-024). Where T5 applies, also call `diligence-dh.build_company_profile {company}` and compare authorizations and Form D rows by decision or filing date with the memo's fact base. Never infer financial health, runway or intent from a filing or its absence. Where the latest filing predates the memo, name the latest 8-K by date with its URL and write: 'Current company status [GAP]: the item of the latest 8-K (DATE) is not stored; open it on EDGAR.' Never infer the status from the date.

### Step 3a. Company status (every A2 answer)

Follow `references/monitoring-signals.md` section 6. Where the assistant can open the filing or register, quote the item and date: 8-K Items 1.03 and 1.03(b) (DL-136, DL-137), 2.01 (DL-138), 3.01 (DL-139, DL-140), 5.01 (DL-141); Form 25 (DL-142 to DL-145); Form 15 (DL-146 to DL-149); Companies House `company_status` (DL-157 to DL-164); German insolvency notices (DL-165 to DL-168). Say what the form does not mean (Form 25 or Form 15 is not dissolution, DL-144, DL-149). Otherwise list the exact filings to open and write "Company status [GAP]: not read". Never take status from press or memory. For automated EDGAR reads, ask which User-Agent contact the person's organization uses (DL-153); never put the person's email address or name into a request and never invent a contact.

### Step 4. Evidence maturity (if an assumption rests on it)

Call `diligence-dh.get_evidence_maturity {company}`. Compare score and components with the memo's run only if the rubric version matches; otherwise "not comparable (T4)". Report the component that moved and its input. This is the library's convention, not evidence quality.

### Step 5. Rule changes since the memo date

From `monitoring-signals.md` section 4, list the dated changes after the memo date that touch a regime the memo flagged, each with instrument, date and status on the pages read (for example "Updated HSR form vacated 12 February 2026; FTC accepts the prior form; appeal pending (DL-051, DL-053)"). List scheduled changes not yet reached as "scheduled". Whether a change affects the holding is for the owner the person names for legal or compliance.

### Step 6. Hypotheses and the register run

For each change, one line on which assumption it could touch, labeled "hypothesis for review" (`monitoring-signals.md` section 5). With code execution and an assumption register, run `python3 scripts/thesis_check.py --register REGISTER.csv --as-of DATE --deltas D.json --funding F.json --maturity M.json` and carry its values into the read; do not recount by hand.

## Build the output

Follow `assets/change-read-output.md`. Answer first: whether anything in the record or the rules moved since the memo date that touches the thesis, with the log caveat. Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every change has its event date, source and retrieval date; every rule change its instrument and status.
- The log start and last sweep appear wherever "no change recorded" is reported; T5 is stated where it applies.
- No inference about results, finances, intent or market status.
- The company status line is present: quoted from a filing or register read, or "[GAP]: not read" with the filings to open.
- No "no change" for any part of the period before 12 October 2026.
- `python3 scripts/thesis_check.py --words ANSWER.md` prints "within the short-mode cap".
- Evidence maturity carries its rubric version; [PAPER] rows carry their DOI.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Market and pipeline movement beyond the held company: `pipeline-and-market-monitoring` (this pack).
- Reimbursement changes: `dh-access-and-value` coverage-strategy-and-access-rate-monitoring.
- Device register changes and what they mean for the pathway: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
