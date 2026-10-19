# A1 Authorization and register tracking

Framework task: DH-03.03.3.2, Part A, task A1. Replaces the earlier "Regulatory Pathway Success Monitoring", "Watch a register" and "Read register changes" sections.

## What this task delivers

A dated view, per jurisdiction in the plan, of where the product and its comparables stand on the register; what has changed since a baseline; how the person's open submissions sit against the review clocks (regulation clock, MDUFA goal, observed performance, kept apart); and which register obligations apply (EUDAMED, FDA registration and listing, Swiss registration, GB CE acceptance dates). It answers "where are we on authorization and registration, and what has moved?"

Why it matters: a pathway plan is built on facts that move: a comparable's clearance, a notified body timeline, a EUDAMED module going mandatory, a recognition date in GB. A plan that is not checked against the registers can be wrong without anyone noticing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.2 Part A, Authorization and register tracking |
| Workflow | The steps below |
| Knowledge | `references/review-clocks.md`; `references/register-obligations.md`; the pathway strategy (from the pathway and classification skill) if the conversation holds one |
| Tools | `regulatory-dh.list_jurisdictions` (free), `get_register_deltas` (or its alias `get_deltas`, never both), `get_market_status`, `get_authorization`, `search_devices`; `watch_register` described only; `scripts/review_clock.py` (optional) |
| Prompt | This guide |
| Template | `assets/register-tracking-output.md` |
| Input | The request and its context: product and comparables (references preferred), target jurisdictions, baseline (an earlier run, the strategy's assumptions, or "as of" a date), the person's open submissions with dates and hold days, EU devices with first-placed dates |
| Governance | `references/governance.md` |

## Read the request

- **What to track.** The person's product (references: K, DEN or P number, Basic UDI-DI) and the comparables from the strategy. If the conversation holds A2 precedents from the pathway and classification skill, take the references from there.
- **Baseline.** An earlier run of this task or of A2 (saved output), or the plan's stated assumptions. Without a baseline, the output is a snapshot and says so.
- **Own submissions.** For each open FDA submission: route, submission date, sponsor hold days so far, any additional-information request date. These are the person's records; they never go into a library call.
- **EU devices.** First date placed on the market, and whether registered in the EUDAMED UDI/device module.
- **Mode.** A direct question gets short mode.

## Workflow

### Step 1. Know what the library can see

Call `regulatory-dh.list_jurisdictions` (free). Record per target jurisdiction: loaded or not, count, last load date. UK registrations, Swiss devices and EU decision dates are not in the library; say so once.

### Step 2. Read the change log

Call `regulatory-dh.get_register_deltas` once per scope in the plan, with `since` set to the baseline date (`{"product_code": "QVO", "since": "2026-01-01", "jurisdiction": "US"}`). If it returns "no watch is registered for this scope; the change log has not started", report that the library's log has not started for that scope (a fact about the log, not the market) and go to Step 3. Do not call `get_deltas` as well: it is the same tool.

If the person wants future changes logged, say that `regulatory-dh.watch_register` exists, that the log starts only once a watch is set, and that the decision to set one is theirs. This skill does not set it.

### Step 3. Compare snapshots

For each reference in the plan, call `regulatory-dh.get_market_status` with `reference` and, where status or dates matter, `regulatory-dh.get_authorization`. Compare with the baseline field by field: authorized per jurisdiction, status, decision date, class, product code. Report only what changed, with the retrieval date of both reads. Where two rows conflict for one product (a known pitfall), quote both and say "check the register". New comparables: if the plan named a manufacturer, `regulatory-dh.search_devices` with that name shows decisions after the baseline date.

### Step 4. Review clocks for the person's open submissions

For each open submission, compute calendar days since submission. Lay beside it, each labeled (`references/review-clocks.md`):
- the regulation clock (De Novo 120 days from acceptance, RP US-11; PMA 180 days from filing, RP US-14);
- the MDUFA goal in FDA days (RP US-46 to US-48), and FDA days only if the person gave sponsor hold days;
- FDA's observed average total days for the route (RP US-58, RP US-61), the figure calendar days can be set against;
- for a De Novo with an open additional-information request, the 180-day withdrawal rule and its date (RP US-13).

With code execution, `scripts/review_clock.py` does this from the person's data. A clock is a fact: state it without pressure words, and never say FDA is "late" on one file; goals apply to a share of submissions.

### Step 5. Register obligations

For each jurisdiction in the plan, the obligations that apply, from `references/register-obligations.md`:
- **EU:** EUDAMED UDI/device registration: devices first placed before 28 May 2026 by 28 November 2026 on the Commission timeline (JX-39); devices first placed on or after 28 May 2026 before the first unit (JX-40). Vigilance and clinical investigation modules not yet live, no date (RP EU-38). Legacy-device transition dates and conditions where the person relies on them (RP EU-21 to EU-24).
- **US:** annual registration and listing between 1 October and 31 December (JX-29, JX-30); fee USD 13,785 in FY 2027 (RP US-55).
- **GB:** MHRA registration (RP UK-01); CE acceptance to 30 June 2030 for MDR devices (RP UK-03); indefinite recognition is a proposal (RP UK-05).
- **Switzerland:** Swissmedic product registration from July 2026 with a six-month transitional period (JX-42).

State each as the rule and the person's status as they gave it. Do not decide compliance.

### Step 6. What it means for the pathway

Close with the consequence for the plan, conditional and sourced: a new 510(k) in the person's code adds a predicate candidate (route to A2 of the pathway and classification skill); a GB recognition change would move the GB step; a EUDAMED gap blocks placing units. No prediction.

## Build the output

Follow `assets/register-tracking-output.md`. Answer first: what changed and which clock or obligation decides the next move. Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every register fact has its source and retrieval date; every rule its row.
- An empty change log is reported as a log fact; changes come from compared snapshots with both dates.
- Calendar days, FDA days and observed averages are labeled and never mixed.
- No compliance verdict; obligations are stated against the person's own status.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Tracking only. Safety records are A2; whether the strategy is working is B1; changing the pathway goes back to the pathway and classification skill.
- No watch is set by this skill. No submission is filed or amended.
- Drugs, biologics and wellness apps are out of scope.
