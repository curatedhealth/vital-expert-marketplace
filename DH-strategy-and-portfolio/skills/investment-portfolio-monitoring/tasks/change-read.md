# A2 Change read

Framework task: DH-DIL.3.2, Part A, task A2. Reuses the read call of the old "DH Diligence Read company changes" tool skill (`diligence-dh.get_deltas`; old boundary: "What the store recorded for the watch since a date. State when the watch has no later sweep. Do not invent an event."). The old "Watch companies" write call is never made.

## What this task delivers

For each holding on the person's list: what the library's change log recorded since the person's date, the window that answer actually covers (log start, last sweep), flags against the person's list (window before the log, not read, owner not named, reread date missing or reached), and, where the person has an earlier saved run, the field changes between that run and a rerun of the comparison or the funding signals. Each change is reported as returned, with event date and source. No judgment of what a change means.

Why it matters: the saved runs of 19 October 2026 answered "no change recorded" for windows starting 1 January 2025 and 1 January 2026, while the log began on 12 October 2026. Read without its window, that answer says more than it can.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound |
| Skill | DH-DIL.3.2 Part A, Change read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md`; `references/tools.md`; `references/company-status.md`; rows DL-135 to DL-168, DL-005, DL-006, DL-019 to DL-024, DL-095 to DL-097, DL-129, DL-133 |
| Tools | `diligence-dh.get_deltas`; optional reruns of `diligence-dh.compare_portfolio` and `diligence-dh.get_funding_signals`; `scripts/portfolio_watch.py deltas` and `diff` |
| Prompt | This guide |
| Template | `assets/change-read-output.md` |
| Input | The request and its context: the holdings list (holding, library reference, since, owner, reread date), the read date, the person's earlier saved runs if any, the watch rules from A1 if any |
| Governance | `references/governance.md`; no `watch_*` call; no meaning read into a change |
| Catalogue job | none (`market-screen`, named in the old change-read file, belongs to `pipeline-and-market-monitoring`, this pack) |

## Read the request

- **Holdings list.** If the person gives names only, ask for the since date and owner per holding, or use one since date they state for all. Never choose a since date.
- **Library references.** Exact legal names resolve best ("Akili Interactive Labs, Inc."). A name that fails is "lookup missed".
- **Read date.** The "as of" date for reread flags: the person's, or today's date stated as such.
- **Earlier runs.** A diff needs the person's saved earlier output with the same company list; a different list is compared only where companies overlap.
- **Confidential holding data.** Kept apart, labeled, never sent to the library.

## Workflow

### Step 1. Read the change log

`diligence-dh.get_deltas {companies: [up to 12 references], since: "<the person's date>"}`. If holdings have different since dates, group them by date (one call per date) or use the earliest date and say so. Save each response.

### Step 2. Run the holdings check

`python3 scripts/portfolio_watch.py deltas HOLDINGS.csv DELTAS1.json [DELTAS2.json] --as-of YYYY-MM-DD`. Report the table: holding, window asked, library answer, window covered by the log, owner, reread date, flags W1 to W6, and the limits as returned.

### Step 2b. The window before the log began (W1)

When a holding's window starts before the change log began (12 October 2026 in the saved runs), say so first and never report "no change" for the span before the log. The library holds the CIKs and form types it lists only: a parent, successor or listed registrant (other CIK) and forms such as 15-12G, 25-NSE or SC 13D may be missing. Before suggesting a rerun, check saved `get_funding_signals` output for the holding (`references/tools.md`) and report its SEC date range as "filings in the store up to DATE (latest filing in the store, not a statement about the company today)". For Pear: none after 10 April 2023. Then offer the holding's dated primary filings and authorization records for the uncovered span, and name EDGAR company search as the person's direct read.

### Step 2c. Status of each holding

Run the status step in `references/company-status.md` for every holding: the script prints the reminder. Where the filings or register can be opened (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices), quote form, item, date and URL with the read date and what the form does not mean (a Form 15 or 25 is not dissolution, DL-144, DL-149). Otherwise write status "`[GAP]`: not read" and list those filings to open, for each CIK and any listed parent or successor. For a US holding, also list a bankruptcy party search in the PACER Case Locator (DL-154 to DL-156; PACER needs the person's own account) among the records to open. Never take status from press or memory. Requests to SEC carry only a User-Agent contact the person's organization gives (DL-153, [WF]), never the user's email address or name; with no contact given, list the filings instead.

### Step 3. Report changes as returned

For each recorded change: type, event date, source and retrieval date. For a new 8-K, open the filing before naming the item (DL-019 to DL-024). For a new authorization, use the register's word, never "approved" for a 510(k) (DL-128). The shape of a response with changes is not yet seen in a saved output (needs a live check): report fields as returned.

### Step 4. Diff against the earlier run (only if the person has one)

Rerun `diligence-dh.compare_portfolio` with the same list, save it, and run `python3 scripts/portfolio_watch.py diff EARLIER.json LATER.json`. Report field changes as printed. A score change may come from the rubric; send score drift to `evidence-maturity-monitoring` (this pack). For filings, rerun `get_funding_signals` and compare counts by type and the latest date with the earlier run.

### Step 5. What the library cannot read

Name the holdings and signals outside the library (UK filings, the HHS breach portal, private rounds) and say the person reads them directly. If the person brings a portal entry, report its fields as they give them (DL-097).

## Build the output

Follow `assets/change-read-output.md`. Answer first: what changed, for which holdings, in which window, and the flag that most limits the read. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every "no change recorded" carries its window (log start, last sweep); no span before the log began is reported as "no change", and each W1 holding gets its dated primary filings instead.
- Every holding has a status line: a filing or register read with its date, or "`[GAP]`: not read" with the filings to open.
- No 0, none or country was written for a field the record lacks.
- The words were counted with the script and are at or under 450 in short mode.
- Every change is as returned, with event date, source and retrieval date; nothing is read into it.
- Counts and flags come from the script; nothing is scored.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Changes for companies that are not holdings: `pipeline-and-market-monitoring` (this pack).
- What a regulatory change means for a holding's product: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Whether a reported breach or deal raises a legal question: the owner the person names for legal or compliance questions (or owner not named).
