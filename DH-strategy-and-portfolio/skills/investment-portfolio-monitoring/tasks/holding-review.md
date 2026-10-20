# B1 Holding review

Framework task: DH-DIL.3.2, Part B, task B1. The judgment step of investment portfolio monitoring: the change read checked against the person's watch rules, with owners, follow-up questions and reread dates the person sets.

## What this task delivers

For each holding: each of the person's rules marked met, not met or cannot tell from the record, with the fact behind it; each flag or miss with the owner the person names; the question for the company drafted for that owner, built from the public record only; the transaction or data rule facts an event touches, with rows, routed to the owner the person names for legal or compliance questions (or owner not named); the reread date the person sets. If the person scores follow-up work, the order from `analytics.rice` on their numbers. Never a mark, a valuation or a hold or exit view.

Why it matters: a portfolio read is only as good as the follow-up it triggers, and the follow-up is the person's. Writing the rule, the fact, the owner and the date side by side keeps the review checkable without anyone scoring a company.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound |
| Skill | DH-DIL.3.2 Part B, Holding review |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 2 and 3; `references/company-status.md`; `references/governance.md`; rows DL-044 to DL-085 when an event touches them |
| Tools | Through A2; `analytics.rice` only on follow-up work the person scored; `verify.build_record` once a named person clears the record |
| Prompt | This guide |
| Template | `assets/holding-review-output.md` |
| Input | The request and its context: the person's watch rules (from A1 or stated), the A2 read, owners, reread dates, any follow-up items with the person's reach, impact, confidence and effort |
| Governance | `references/governance.md`; no investment advice; deal and data rules stop for the owner the person names for legal or compliance questions |
| Catalogue job | none |

## Read the request

- **Rules.** Without rules there is no review: "Watch rules not stated `[GAP]`"; offer A1. Take each rule verbatim and number it.
- **Read.** Use the A2 read of this request. If none, run A2 first.
- **Owners and dates.** The person's words. Missing: "owner not named" or "reread date not given"; ask.
- **Scores for follow-up work.** Only if the person gives reach, impact, confidence and effort. Confidence goes to the tool as a percent (80, not 0.8). Impact must be 0.25, 0.5, 1, 2 or 3; check before the call.

## Workflow

### Step 1. Check each holding against each rule

Mark: met, not met, or cannot tell from the record (with the reason: window before the log, source not loaded, item not read). When the person supplies information that meets a rule's trigger (for example a new investor), mark that rule "triggered (from the person, confidential)" for that holding, not "cannot tell". Never fill a gap with an assumption.

Before asking anyone to open a holding's filings since a date, check the saved funding signals (`references/tools.md`): if the store holds none after that date, say so ("none after 10 April 2023 in the store" for Pear) and point to EDGAR for other registrants. A rule about a holding's existence, listing or control is checked only through the status step (`references/company-status.md`): a filing or register read with its date, or "cannot tell: status `[GAP]`: not read" with the filings to open.

### Step 2. Each miss with its owner and block

For each "not met" or "cannot tell": the owner the person names, what the person must read or ask next, and the reread date they give. Sequence by dependency (an 8-K must be opened before its item can be judged), never by urgency.

### Step 3. Draft the question for the company (only if asked)

From the public record only: "Your 8-K of DATE (reference) reports ITEM; please share ...". Label it "draft for the owner". Declined wording for LPs, a board or a company still gets this facts-only version, labeled "draft for the owner": what was checked, source and date, what was not checked; no finding. No confidential material in a draft that may leave the firm unless the person says so.

### Step 4. Rules an event touches

If an event involves a new foreign investor, a sale, a data transfer or a breach, list the rule facts with rows and dates (`references/monitoring-signals.md` section 3; DL-086 to DL-098 for breaches). Route to the owner the person names for legal or compliance questions (or owner not named). Never say a deal or an event is clear or compliant.

### Step 5. Order follow-up work (only if the person scored it)

`analytics.rice {initiatives: [{id, reach, impact, confidence (percent), effort}]}`. Show the inputs beside the scores. The order ranks work, never holdings.

## Build the output

Follow `assets/holding-review-output.md`. Answer first: which holdings miss which rules, who owns each follow-up, and the stop that applies if any. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule is the person's, numbered and verbatim.
- Every owner and date is the person's or "not named" / "not given"; no coined role.
- Each holding's status is a filing or register read, or "`[GAP]`: not read".
- The words were counted with the script and are at or under 450 in short mode.
- No holding is scored, valued, marked or given a hold or exit view.
- Deal and data rule facts carry rows and dates and stop for the owner the person names for legal or compliance questions.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Whether the thesis behind a holding still holds: `thesis-and-memo-monitoring` (this pack).
- A fresh comparison or ranking of companies: `funding-and-portfolio-comparison` (this pack).
- Privacy and security compliance after a breach: `dh-cybersecurity` (old pack), heading DH-04.02.1 Compliance & Assurance, and the owner the person names for legal or compliance questions (or owner not named).
