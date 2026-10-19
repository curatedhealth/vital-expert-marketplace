# A1 Public launch signals

Framework task: DH-02.01.1.2, Part A, task A1. Folds in the earlier tool skills "Watch a product" and "Read commercial changes".

## What this task delivers

A dated read of what public records show for the product and its peers since launch: listings, authorizations, status changes, provisional listings without stated end dates, and the clocks and moved rules that apply after go-live. Where the library has no change feed, the task builds one honestly: a saved baseline today, compared with the next run.

Why it matters: after launch, the competitive picture and the rules both move. A peer moves from provisional to permanent or is deleted; a CMS rule extends a code to a new device class (CP-US-62); an NHS form is replaced (CP-UK-04). The field needs to know which of these touches what it says. An empty feed read as "nothing changed" is the error this task exists to prevent.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.2 Part A, Public launch signals |
| Workflow | The steps below |
| Knowledge | `references/launch-clocks.md`; library records; `references/gap-rules.md` |
| Tools | `commercial-dh.list_commercial_dh_sources` (free), `commercial-dh.get_deltas`, `market-access-dh.find_scheme_precedents`, `commercial-dh.get_launch_sequence`; `verify.build_record` when a named person clears the output |
| Prompt | This guide |
| Template | Library events for the data; `assets/public-signals-output.md` for the answer |
| Input | The request and its context: product and identifiers, launch date, markets, peers, any earlier saved run |
| Governance | `references/governance.md` |
| Catalogue job | `product-watch`, without its `watch_product` step: this skill never sets a watch and runs `get_deltas` only. The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Product, identifiers and launch date.** The launch date is the person's; the window starts there.
- **Peers.** The person's, or comparables in the same scheme and indication (step 3), labeled comparables.
- **Earlier run.** If the person has a saved output from an earlier run of this task, ask for it: comparison is the only reliable change signal today.
- **Short or full.** "What changed" gets short mode; "competitive update for the board" gets full mode.

## Workflow

### Step 1. Know what the library can see (free)

Call `commercial-dh.list_commercial_dh_sources`. Note load dates and what is not loaded (UK registrations, Swiss records, DiGA history before the first snapshot).

### Step 2. Ask the change feed once

Call `commercial-dh.get_deltas` with `reference` and `since` set to the launch date. If events come back, report each with `what`, `event_date`, `observed_at`, `source_url` and the upstream tool. If nothing comes back, write "no change events available from the library `[GAP]`" with the feed status as returned (`references/tools.md`). Do not call it again with other spellings.

### Step 3. Get exact names for the cohort

Call `market-access-dh.find_scheme_precedents` with the scheme and an indication code or source-language term, limit 10. Note any provisional rows (trial end `[GAP]`), and any listing after the person's launch date.

### Step 4. Read the sequence and compare with the earlier run

Call `commercial-dh.get_launch_sequence` with the product (FDA number for US products) and up to ten exact peer names. Separate merged products by identifier. If the person supplied an earlier run, list every difference: new events, changed dates, peers that disappeared. If not, say "baseline recorded on DATE" and give the person the saved output to keep.

### Step 5. Clocks and moved rules

From `references/launch-clocks.md`, list the clocks and moved rules for the markets in scope, each with its row and instrument. Mark which ones touch the launch material or the field (for example, the 2026 patient engagement cap for a patient support program, CP-US-27).

### Step 6. Gaps

Classify gaps with `references/gap-rules.md`.

## Build the output

Follow `assets/public-signals-output.md`. Answer first: what changed (or that the library cannot show change), the clock that matters most, and what touches the field. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every event has its source and retrieval date and the line "library copy; confirm on the authority's page before external use".
- No statement about a peer's uptake, revenue, success or intent.
- An empty feed is reported as a gap, never as "no change".
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Do not register a watch (`watch_product`): watches are not separated per customer key (register N2).
- Payer status and price changes are Market Access's subject; this task reports listing events only as context for the field.
- Drugs and biologics are out of scope.
