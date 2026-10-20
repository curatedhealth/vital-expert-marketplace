# A2 Open dependency log

Framework task: DH-01.01.3.1, Part A, task A2. Replaces the earlier "Open dependency" section (DH-01.01.3.1.2).

## What this task delivers

A log of work products that have been asked for and not yet received by the named receiver: what, asked on which date, owed by whom, due when, which decision waits, which other open items it waits on, and what the receiving team will do if it is late. Open items are listed in dependency order, so the person sees which item unblocks which. Clocks that the sources set (DiGA, Pre-Sub minutes, ePA updates) are stated with their instrument.

Why it matters: an open dependency without a late path leaves the receiving team waiting with no plan, and a dependency nobody logged surfaces only when the decision is due.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.1 Part A, Open dependency log |
| Workflow | The steps below |
| Knowledge | `references/handoff-rules.md`; rows CV29 (dependencies among critical-to-quality factors), PL41, PL80, PL82, PL89, PL91, PL95 (sourced clocks), PL25 and PL29 (impact assessments as owed records), CS42 (milestones in a blueprint) |
| Tools | `scripts/handoff_log.py check` on the person's log |
| Prompt | This guide |
| Template | `assets/open-dependency-log-output.md` |
| Input | The request and its context: A1's map or the person's list, the person's log (CSV or table), names, dates |
| Governance | `references/governance.md`; owners, dates and late paths are the person's |
| Catalogue job | none |

## Read the request

- **The items.** Each work product owed, in the person's words. If an A1 map exists, start from its open points.
- **Dates.** Asked on, due on, received on. A date the person does not give stays `[GAP]`; never estimate one.
- **People.** Who owes it and who receives it, in the person's words.
- **The waiting decision.** What cannot be decided until it arrives.
- **Late path.** What the receiving team will do if it is late. If the person does not know, ask the receiving function; do not supply one.

## Workflow

### Step 1. Build or read the log

Use the person's log, or build one from their list with the columns in `scripts/handoff_log.py` (id, work_product, category, ctq, sender_function, receiver_function, receiver_named, owner_owes, asked_on, due_on, received_on, received_by, blocked_decision, depends_on, late_path, look_again_on). Category and the CTQ mark are the person's.

### Step 2. Check it

Run `python3 scripts/handoff_log.py check LOG.csv --as-of YYYY-MM-DD` with today's date. It lists every record with days open, the missing fields printed `[GAP]`, open items in dependency order, unknown ids in `depends_on`, and any circular wait. Without code execution, do the same by hand.

### Step 3. Add sourced clocks where they create a dependency

Only where the person's situation triggers them, and with the instrument:

- DiGA trial listing: extension request at least three months before the trial period ends, once, by up to 12 months (PL82); everything except the study in place at application (PL80); certificates no older than 12 months on submission (PL91); ePA specification updates within six months of publication (PL89); significant changes notified (PL95).
- FDA Pre-Sub: the submitter's minutes within 15 days of the meeting (PL41).
- Multiple function products: an impact assessment owed for each other function, and again when an other function changes (PL25, PL29).

A clock is a fact, never pressure. State it, state whether it applies, and place the item in dependency order.

### Step 4. Late path for each open item

For each open item, show the late path the person gave. Missing late paths are listed together for the person to fill. If asked to propose one, offer it labeled "proposed", built only from the person's own facts (for example a version of the work product they already hold), and do not write it into the log until confirmed. No source sets late paths.

### Step 5. Dependency order

List the open items so that each comes after the open items it waits on (the script's order). Where two items wait on each other, say so and ask the person which goes first. Do not reorder by how late an item is.

## Build the output

Follow `assets/open-dependency-log-output.md`. Answer first: open items, how many lack an owner or a late path, the first item in dependency order, and the decisions waiting. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No open item is dropped, merged or renamed; the work product keeps the person's name.
- Every missing owner, date, receiver or late path is visible as `[GAP]` or "owner not named".
- Clocks carry their row and instrument and are stated as facts.
- Order is by dependency, not urgency.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Scoring received, late and open over a period, and assigning repairs: integration and handoff monitoring (DH-01.01.3.2).
- DiGA application content and timing decisions: `dh-access-and-value` coverage-pathway-and-access-strategy (listing) and `dh-regulatory-and-quality` regulatory-pathway-and-classification (device questions). This task only places the clock in the log.
- Change control records for a changed other function: `dh-regulatory-and-quality` document-and-change-control.
