# A1 Signal quality check

Framework task: Part A, task A1. Replaces the old task DH-01.08.4.2.1 Horizon Signal Quality Monitoring.

## What this task delivers

For a signal log the person keeps (from `horizon-scanning-and-technology-evaluation` A1 or their own): each signal checked against the person's quality checks (or the proposed checks Q1 to Q8, labeled), a sample of signals reread on the record to see whether they still say what the log says, the leads logged as signals, the duplicates, the drafts logged as final, and the candidates for false positives by the person's definition. It answers "are the signals in our map good enough to act on, and which are noise?"

Why it matters: a map that mixes records, press items and opinions cannot be trusted or updated. Checking each entry against stated checks, and rereading a sample, shows which entries carry weight and which need their record read first.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`), as bound to DH-01.08.4.2 in the old skill |
| Skill | DH-01.08.4.2 Part A, Signal quality check |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 1, 2 and 5 (SP-004, SP-005, SP-009, SP-015; US-21, US-25; UK-04; SP-124); `references/company-status.md` for signals about a named company (section 6: status already read, SP-148 to SP-169) |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_devices`; `regulatory-dh.get_pathway_precedents`; `literature.search_literature` (reread by DOI; `literature.get_record` needs a live check); `diligence-dh.get_deltas` for company signals; `scripts/foresight_check.py` |
| Prompt | This guide |
| Template | `assets/signal-quality-output.md` |
| Input | The request and its context: the signal log (CSV columns in `scripts/foresight_check.py`, or a table), the person's checks and false-positive definition, the scan's saved outputs and perimeter, the read date |
| Governance | `references/governance.md`; the checks and pass rule are the person's |
| Catalogue job | none (`examples/live/list_jobs_2026-10-19.json` lists no signal monitoring job) |

## Read the request

- **The log.** Rows with source type, URL, event date. Without a log, ask for it; never rebuild one from memory.
- **Checks.** The person's. If none: propose Q1 to Q8 (`monitoring-signals.md` section 2), labeled "proposed checks", and ask which they adopt. Results are reported either way, marked "against proposed checks" until confirmed.
- **False positive.** The person's definition. If none: "proposed false positive" candidates only.
- **Reread sample.** All signals if few; otherwise the ones the person names, or those the log marks as acted on. Ask; never pick by importance alone.
- **Read date.** Today's date unless the person gives another.

## Workflow

### Step 1. Run the checker

With code execution, run `python3 scripts/foresight_check.py --log LOG.csv --as-of YYYY-MM-DD`. Take Q1 (lead, not signal), Q2 (date missing), Q3 (source missing) and the owner and reread flags from its output. Without code execution, apply the same checks by hand.

### Step 2. Checks the script cannot make

- **Q4 limits:** does each signal say what its record does not show (for example a clearance says nothing on AI use or PCCP; the FDA AI list is not comprehensive, US-25)?
- **Q5 duplicates:** the same product under different spellings or makers ("BriefCase-Triage", "Aidoc Medical , Ltd." versus "Briefcase-Triage", "Aidoc Medical Ltd."); match on identifiers.
- **Q6 signal versus trend:** an entry that is an interpretation ("AI triage is accelerating") is a trend logged as a signal.
- **Q8 status:** a draft, pilot or announcement logged as final (the FDA AI lifecycle guidance is draft, US-21; MHRA PCCP draft guidance announced, not published, UK-04; IDAP pilot closed, SP-124).

### Step 3. Reread the sample (Q7)

Perimeter first: `regulatory-dh.list_jurisdictions {}`; compare with the scan's saved perimeter and say if a source was newly loaded. Reread each sampled signal at its record: `regulatory-dh.search_devices {query: <identifier or name>, jurisdiction}`; `get_pathway_precedents {product_code}` for counts; `literature.search_literature` by title or DOI. Report "on DATE the log read X; on reread the record reads Y". Example from saved data: EU "Stroke Triage App" (ORTEC B.V.) read "No longer placed on the EU market" on 14 October 2026; a log entry saying it was on the market fails Q7. An EU status has no date in the library; write "as read on the retrieval date". For a company signal, call `diligence-dh.get_deltas` with the log caveat (began 12 October 2026) and add the company status line (`company-status.md`). Never call a `watch_*` tool.

### Step 4. Leads and false positives

List every Q1 lead with the record that would confirm it. A lead that the reread confirms becomes a signal with the record's date; one that it does not stays a lead. False positives: by the person's definition, or "proposed false positive" with the failed check. Do not judge a signal's importance to the person's strategy.

## Build the output

Follow `assets/signal-quality-output.md`. Answer first: how many signals pass the checks (theirs or proposed), how many are leads, what the reread changed, and the check that fails most often. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Checks are labeled as the person's or "proposed checks".
- Every reread states both readings with dates; no "still holds" from an empty log or a press item.
- Leads are separate from signals; drafts are not logged as final.
- Every named company carries the company status line: the status already read for Akili, Pear, Big Health and Aidoc (`company-status.md` section 6, for example "Aidoc: no SEC registrant found, EDGAR search, 20 October 2026 (SP-162) [WF]; FDA establishment registration active for 2026 (SP-164)"), or "Status: [GAP]: not read" with the filings to open.
- Every fact names its source in plain words with its date, then the row id; never a row id alone. No reread date or owner supplied; rows with no owner (O1) and reread dates earlier than the read date (O3) are listed as facts.
- [PAPER] rows carry their DOI; [WF] rows say so.
- The record line is the very last line of the answer; the calls list and the one-line offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Building or extending the scan: `horizon-scanning-and-technology-evaluation` A1 (this pack).
- Whether past calls and selections held up: A2. Review against the pass rule: B1.
- What a register change means for a pathway: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
