# B1 Partner and initiative prioritization

Framework task: DH-02.01.4.1, Part B, task B1. Replaces the register tasks "Rank scored options" (CF-12.02.01.4.1.4, `analytics.mcda`) and "Rank initiatives" (CF-12.02.01.4.1.5, `analytics.rice`), catalogue jobs `partner-prioritization` and `partnership-screen`.

## What this task delivers

A prioritization draft: the person's partner options ranked by the connector on the person's criteria, scores and weights, with the weight changes that would flip the order; or the person's channel initiatives ranked by RICE on their reach, impact, confidence and effort; then the order in which things must be settled by dependency, and the stops. It answers "which partner or initiative first, on our own scores, and what has to happen before what?"

Why it matters: partner choices lock in data flows, exclusivity and compensation for at least a year (a personal services safe harbor needs a term of at least 1 year, CP-US-09). Writing the scores down before choosing makes the choice reviewable and shows where it is fragile.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.1 Part B, Partner and initiative prioritization |
| Workflow | The steps below |
| Knowledge | A1 channel map and A2 term lists if present; `references/channel-rules.md`; `references/fraud-and-abuse-stops.md` |
| Tools | `diligence-dh.build_company_profile` and `commercial-dh.screen_commercial_peers` (counted, only when the options come from research); `analytics.mcda` (counted); `analytics.rice` (counted); `scripts/rank_check.py` (optional) |
| Prompt | This guide |
| Template | `assets/prioritization-output.md` |
| Input | The request and its context: the options or initiatives, the criteria and weights, the person's scores (or RICE inputs), the accountable owner |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides |
| Catalogue job | `partnership-screen` when the options come from research (dossier, peer screen, then a rank of the person's scores); `partner-prioritization` when the person already holds the option list (mcda or rice). Live run and pitfalls: `examples/live/job_partnership_screen.json`, `references/tools.md` |

## The rule that shapes this task: people score

The person chooses the criteria, sets the weights and scores each option, or gives reach, impact, confidence and effort for each initiative. The model lays out the sourced facts per option so the scoring is informed, runs the ranking, and shows where the order is fragile. It never scores, never fills a missing number, and never calls an option "recommended". If asked for a proposal, it may write one labeled "proposed", with the facts behind it.

## Read the request

- **Partner options or initiatives?** Options compared on several criteria go to MCDA. Initiatives with reach, impact, confidence and effort go to RICE. If unclear, ask which.
- **Criteria.** Ask. Offer names only as examples phrased so that higher is better (the connector treats every criterion that way): "buyer access", "compliance fit", "implementation capacity", "strategic alignment".
- **Scores and weights.** 0 to 4 per criterion; weights summing to 1. For RICE: reach (the person's unit and period), impact 0.25, 0.5, 1, 2 or 3, confidence as a percent, effort in the person's unit.
- **Owner.** Who decides; "owner not named" if not given.
- **Mode.** Short for a direct question; full for a decision paper.

## Workflow

### Step 0. Options from research (only if the person asks)

If the person names a company and a segment but has no option list, run the catalogue job `partnership-screen` (or its calls directly): `diligence-dh.build_company_profile` with `company` (exact legal name or an FDA submission number), then `commercial-dh.screen_commercial_peers` with `segment` (one of the loaded segments, for example `dtx`) and `limit`. The candidate options are the companies those calls return; label each "from the dossier" or "from the peer screen". Describe each only by what its record states (products, authorizations with dates and source URLs, studies and how they are linked, gaps). The peer screen orders by evidence maturity score only, not by fit; say so. Its device and listing lookups use the company name and returned no match for any of five peers in the live run, so read authorizations from the profile, not from the screen (`references/tools.md`). The person then chooses the options and scores them; nothing from research becomes a score. The job also names `analytics.segmentation`, which the connector does not expose: no cluster is produced, and the output says "[GAP] segmentation: tool not exposed".

### Step 1. Lay out the facts per option

For each option, list the sourced facts that bear on the criteria, from A1 and A2 or `references/channel-rules.md`, each with its row: for example, "behavioral health practices can bill G0552 only if they bear the device cost (CP-US-59)", "an NHS reseller on a Dynamic Purchasing System can join at any time; other frameworks cannot add suppliers (CP-UK-12)". Mark fraud-and-abuse triggers on any option (they do not change the score; they stop for the owner). Facts only, no scores.

### Step 2. Collect and confirm the person's numbers

Write back the score table (or RICE table) and the weights for confirmation. A missing score stops the ranking for that option; say which, and leave that option out of the call (the connector refuses the whole call with HTTP 400 if any option lacks a score, although the job says the option is left blank). Check: scores within 0 to 4, weights sum to 1, impact is one of the five allowed values, confidence given as a percent (80, not 0.8).

### Step 3. Rank

MCDA: call `analytics.mcda` with `alternatives` (`id`, `scores`) and `criteria_weights`. Report each value (0 to 100) and the largest contribution.

RICE: call `analytics.rice` with `initiatives` (`id`, `reach`, `impact`, `confidence` as a percent, `effort`). Report each score. If the response shows confidence divided by 100 again (for example 0.008 for 80), say the scores are scaled and recompute with the script.

With code execution, save the call and response as JSON and run `python3 scripts/rank_check.py FILE`. It recomputes the values, flags input problems, and for MCDA gives the weight on each criterion at which adjacent options swap. Report the smallest change that flips the top two in plain words.

If the call fails with HTTP 503, retry once after a pause; nothing is counted. A bare HTTP 400 usually means a missing score.

### Step 4. Sequence by dependency

Write what must be settled before what, with the reason and row. Typical links: fraud-and-abuse clearance of the compensation model before the partner agreement (`fraud-and-abuse-stops.md`); BAA or processor terms before any data flows (CP-US-46, CP-EU-02); FDA registration and listing, UDI and EUDAMED actor registration before a partner places the device (CP-US-72, CP-US-75, CP-EU-10); DTAC before NHS procurement (CP-UK-01). No dates and no urgency. Legal clocks are facts.

### Step 5. Stops and the owner

List what stops: the partner decision itself; every fraud-and-abuse trigger; counterparty wording; exclusivity or revenue share presented as the company's position. Name the owner as the person gave them, or "owner not named".

## Build the output

Follow `assets/prioritization-output.md`. Answer first: the order the person's scores produce and how robust it is, then the first dependency. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every score, weight and RICE input is the person's, and the output says so; options from research are labeled by source and carry no score until the person gives one.
- The ranking is described as the result of their scores, never as a recommendation.
- RICE confidence was sent as a percent; scores checked.
- Every fact has a row; fraud-and-abuse triggers are stops, not score penalties.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Ranking and sequencing only; the choice is the owner's.
- No revenue or cost estimates: the rows hold none. A revenue criterion is scored from the person's own figures.
- Payer pricing and reimbursement are Market Access.
- Drugs, biologics and wellness apps are out of scope.
