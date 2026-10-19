# A2 Decision tracking

Framework task: DH-03.01.3.2, Part A, task A2.

## What this task delivers

A dated table of decisions: the person's own submissions (status, decision, date, the clock now running) and comparable products on the same route (what was decided, when, where it is published), with the bodies' official outcome figures as context and a plain statement of what each body does not publish. It answers "what happened to our submission, and what happened to others like it?"

Why it matters: a submission's status moves on clocks the company does not control: a three-month BfArM decision window, a one-month objection window, a 10-day HAS contradictory phase, a PECAN year that starts a filing clock. Comparable decisions show which routes and claims have held, and the official figures show where files commonly stop. Neither is a forecast.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.2 Part A, Decision tracking |
| Workflow | The steps below |
| Knowledge | `references/decision-sources.md`; `references/access-monitoring-sources.md`; `references/hta-submissions-sources.md` |
| Tools | `market-access-dh.list_schemes` (free), `find_scheme_precedents`, `search_listings`, `get_reimbursement_status`, `get_status_history`; `scripts/decision_tracker.py` (optional); `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/decision-tracking-output.md` |
| Input | The request and its context: the person's submissions (body, route, dates, letters received), the product's indication, comparables they care about |
| Governance | `references/governance.md` |

## Read the request

- **Own submissions.** For each: body, route, filing date, completeness confirmation date, any letter received, the decision and its date. The person's own documents are the source; the library sees only published listings. A submission still in review is invisible to the library.
- **Comparables.** Named products, or "similar products" by indication. Ask for the indication in the register's terms if needed (ICD-10-GM for DiGA).
- **Mode.** "What happened to X" is short mode. A quarterly review pack is full mode.

## Workflow

### Step 1. Know what the library can see

Call `market-access-dh.list_schemes` (free). Note per scheme `listing_count`, `last_load` and `posture`. FR_LPPR held no rows on 19 October 2026, and UK_NICE_NHAP none; say so once.

### Step 2. The person's own submissions

Build the table from the person's documents. For each, state the clock that applies, from `references/submission-checklists.md`: BfArM decision three months from a complete file, extendable by three (`DE21`); objection within one month of notification (`DE24`); PECAN opinion 60 days from a complete file, 30 days to supply missing items (`FR14`); HAS 10-day contradictory phase (`FR19`); after a PECAN decision, 6 months to file LPPR or 9 for LATM (`FR14`); NICE scoping about 10 weeks, assessment 12 to 30 weeks (`UK5`). Count from the dates the person gives; a date they do not give is `[GAP]`. If the product is listed, call `get_reimbursement_status` (`reference`, `scheme`) to confirm the published status and its retrieval date.

### Step 3. Comparable decisions

Call `find_scheme_precedents` on the same scheme, narrowed by `indication` (DE_DIGA: ICD code such as `F51` or `F32`). For each row: product, status, `status_raw`, listing date, stated end date, source and retrieval date. Then apply these checks, which the library does not do for you (`references/tools.md`):
- **A stated end date in the past with a provisional status** (for example a PECAN year that has ended) means the stored status may be stale. Say "the stated end date passed on DATE; check the Journal officiel or HAS for the outcome". Never infer the outcome.
- **NICE rows are guidance documents.** Count renumbered guidance once (HTE8 is HTG675). A title saying "early-use" with a stored status of permanent: read it as early use (`UK6`) and say "check the guidance".
- **Deleted DiGA can lack indications** and drop out of an indication search; say the comparable set may be incomplete.
- With code execution, `scripts/decision_tracker.py <saved JSON files> --as-of DATE` builds the table and the flags.

### Step 4. Official figures as context

From `references/decision-sources.md`, give the body's figures with their period: BfArM as of 9 September 2026 (254 applications; 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted) (`DE33`, `DE34`); GKV trial outcomes to 31 December 2025 (`DE-1`, `DE-6`); CNEDiMTS 2025 rates (`FR21` to `FR24`); NICE early-use rules and examples (`EN-1` to `EN-6`). Say how to read them (withdrawals exceed refusals; categories are not a partition) and that they are not the person's odds.

In short mode, give only the figures for the body and question asked, in two or three lines. Offer the trial outcomes (DE-1, DE-6) and named cases (FR-5, FR-6) in one line rather than printing them.

### Step 5. What is not published

State per body what the person cannot see and must not infer: BfArM does not name applicants or refused products (`DE32`) and refusals are not announced in the Federal Gazette (`DE31`); actual BfArM review days are not published; NICE has published no re-evaluation outcome for HTG675 (`EN-6`); HAS opinions exist but the library holds no CNEDiMTS opinions and no LPPR rows.

### Step 6. What it means for the person

Close with consequences stated as conditions: "if BfArM's three-month window from your completeness confirmation of DATE passes without a decision, the extension rule (`DE21`) applies; ask BfArM for the reason"; "if the PECAN decision lands, the 6-month LPPR clock starts that day (`FR14`)". No prediction.

## Build the output

Follow `assets/decision-tracking-output.md`. Answer first: the person's open decisions and their clocks, then the comparables in one table, the official context in two or three lines, and what is not published.

## Before you hand it over

- Every decision has a source (the person's document or a library row) and a date.
- No outcome inferred from a passed end date or from absence.
- Official figures carry their period and the "context, not odds" line.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No legal reading of a refusal or an objection; point to counsel and the body.
- No watch registration unless the person asks (the coverage monitoring skill covers `watch_scheme`).
- Drugs, biologics and wellness apps are out of scope.
