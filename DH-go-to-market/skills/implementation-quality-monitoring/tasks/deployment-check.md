# A1 Deployment check

Framework task: DH-02.02.1.2, Part A, task A1. Replaces the old register task "Deployment check" (CF-12.02.02.1.2.1) and takes the evidence steps of "Site score" (CF-12.02.02.1.2.2).

## What this task delivers

For each site, the go-live bar item by item, with the evidence seen (and its id), evidence described but not shown, items with no evidence, and items that slipped past the date the site agreed; optionally, field safety events for the product since go-live. It answers "did this site really meet its go-live bar, on evidence?"

Why it matters: the register's rule is that a site does not pass on the project plan's status field, and a site is not live because the contract started. A bar checked on evidence is what lets the person tell a deployment problem from a product problem later (CS32).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.2 Part A, Deployment check |
| Workflow | The steps below |
| Knowledge | `references/deployment-evidence.md`; `references/go-live-bar-elements.md` |
| Tools | `regulatory-dh.search_safety_events` (counted, optional, Step 5) |
| Prompt | This guide |
| Template | `assets/deployment-check-output.md` |
| Input | The request and its context: the bar for each site (from the planning skill or the person), the evidence they hold with ids, the agreed go-live date, the as-of date |
| Governance | `references/governance.md`; no statement to the customer that a site is live |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. post-market-watch also reads safety events but sets a watch; it is not called. |

## Read the request

- **The bar.** Per site. If none exists, there is nothing to check against: offer the candidates in `go-live-bar-elements.md` as a starting list for the planning skill, and stop the check.
- **Evidence.** What they can show, with an id per item. Ask for extracts, not patient records; records about people are by role.
- **Agreed go-live date and as-of date.** Default the as-of date to the conversation date and say so.
- **Their rule for missing evidence.** Ask whether missing evidence counts as not met. Offer the register's starter rule ("mark missing evidence as failed, not as unknown-pass") for them to adopt.
- **Data before the agreement.** If data flowed before the written agreement, ask whether it was real personal data or test data; record the answer as the person's statement, not as evidence seen.
- **Mode.** Short for one site; full for a portfolio.

## Workflow

### Step 1. Lay the bar out per site

One row per bar item, using the person's wording. Add the evidence type each item needs (`deployment-evidence.md` section 3).

### Step 2. Classify the evidence

For each item: seen (with the person's evidence id), described, status field only, or none (`deployment-evidence.md` section 2). A status field in the plan or a tracker is never evidence (register rule). Check that a data agreement's signature date is earlier than the first data flow (G3: US CS96, EU CS110, UK and other markets `[GAP]`; cite only the row for the site's market).

### Step 3. Apply their rule, if any

With their rule, mark each item met or not met. With the register starter rule adopted, missing evidence is not met. Without a rule, no verdict: "no rule set".

### Step 4. Slippage

For each item and for go-live, days between the agreed date and the date met (or the as-of date if open). Show any re-baselined date beside it, never instead (register rule: do not rescore after go-live). With the milestone file, `scripts/implementation_outcomes.py` computes this (A2).

### Step 5. Field events (optional)

If the person asks, call `regulatory-dh.search_safety_events {manufacturer or product: "<theirs>", since: "<go-live date>", limit: 10}`. Read `references/tools.md` first. Report events only by their record; say the link is the openFDA API; no events is not evidence of no events. A recall is a fact the person may weigh for a limited launch, not a finding about the deployment.

### Step 6. What it means for the person

Two lines from the rows, conditional. Example: "Clinic B's training record is described, not seen; under the rule you adopted, G5 is not met, so the site is not past its bar."

## Build the output

Follow `assets/deployment-check-output.md`. Answer first: per site, how many bar items have evidence seen, which do not, and the go-live slippage. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every "met" rests on evidence seen and the person's rule.
- No status field counted as evidence.
- No staff named; records by role.
- No statement that a site is live; the site approver agrees the bar is met.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checking evidence against the bar. Setting the bar is the planning skill (DH-02.02.1.1). Outcomes in numbers are A2; repairs are B1.
- No legal judgment on agreements and no clinical safety sign-off.
