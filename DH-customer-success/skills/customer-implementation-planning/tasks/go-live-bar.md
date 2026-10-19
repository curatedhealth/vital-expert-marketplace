# B1 Go-live bar and rollout decision

Framework task: DH-02.02.1.1, Part B, task B1. Replaces the old register task "Go-live bar" (CF-12.02.02.1.1.3). The old one-line pass rule and miss owner become Steps 4 and 5.

## What this task delivers

A go-live bar for each site: the items that must be true to call the site live, the evidence that will show each, the pass rule the person sets, the site approver, the owner of any miss, and, where the person is choosing how to roll out, a ranking of the options they scored. It answers "when can we call this site live, who says so, and do we start with a pilot?"

Why it matters: the register's rule is plain: do not call a site live because the contract started. The sibling monitoring skill checks each site against this bar, so a bar without evidence types cannot be checked later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.1 Part B, Go-live bar and rollout decision |
| Workflow | The steps below |
| Knowledge | `references/go-live-bar-elements.md`; A1 scope and measures; A2 sequence |
| Tools | `analytics.mcda` (counted, optional, Step 6); `verify.build_record` (counted, when it leaves the conversation) |
| Prompt | This guide |
| Template | `assets/go-live-bar-output.md` |
| Input | The request and its context: the day-one workflow, the users who must complete a real task, the data that must be present, the site approver, the pass rule, rollout options and the person's scores |
| Governance | `references/governance.md`; the bar and the decision are the person's and the site's; a go-live plan issued to a health system stops for the accountable owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: the site decides it is live

The model drafts the bar, lays out the sourced candidates and checks it is checkable. The person and the site set it; the site approver agrees it is met. The model never declares a site live, ready or safe, and never ranks rollout options the person did not score.

## Read the request

- **Day-one workflow and users.** From A1. Without them there is no bar; ask.
- **Their bar, if any.** Take it as written. If none, offer the candidates G1 to G10 in `go-live-bar-elements.md` as a "starting list".
- **Pass rule.** For example "every item has evidence seen" or "all except G10". Ask.
- **Site approver and owners.** Ask.
- **Rollout options and scores.** Only if they are deciding pilot versus all sites.
- **Mode.** Short for a direct question; full for a go-live criteria document.

## Workflow

### Step 1. Draft the bar

Write each item the person keeps as a testable statement with the evidence that will show it (task log, data check, signed agreement, training record by role, silent-mode summary). Use the register's three items first: named users complete one real task in the day-one workflow; the data the workflow needs is present; the site approver is named.

### Step 2. Check each item is checkable

Each item needs an evidence type that someone other than the project plan can show. A status field in the plan is not evidence (register rule of the sibling Deployment check). Items about people name roles, never named staff performance.

### Step 3. Add the market items

From A2: the signed data agreement before data flows (G3: CS96 or CS110); for an NHS deploying organization, its own clinical risk assessment and the developer's DCB0129 evidence (G9: CP-UK-09, CP-UK-10, guidance pages; CS71 [WF]). Label each "required by row" or "candidate".

### Step 4. The pass rule (formerly "pass rule")

Write the person's rule back. If they have none, ask; offer the register's own phrasing as an option to adopt: "a pass only when each bar item has evidence". Without a rule, the bar has no verdict.

### Step 5. Owners of a miss (formerly "miss owner")

For each item, the owner if it is not met at the planned date. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Add what happens on a miss, in the person's words (for example "site stays in limited launch"); the model does not choose.

### Step 6. Rollout option (optional)

If the person is choosing between rollout options (for example two pilot clinics then the rest, all sites at once, by region), lay out the sourced facts per option: staged scale-up from pilots (CS47); trialability includes undoing after a small test (CS5); complexity across NASSS domains (CS51), if the person rated it. Ask for criteria phrased so higher is better, weights summing to 1, and 0 to 4 scores. Write them back. Call `analytics.mcda {alternatives: [{id, scores}], criteria_weights}`. Report each option's value and contributions, and the smallest weight change that flips the top two (work it out from the contributions). Describe the result as "the ranking of your scores", never as a recommendation.

### Step 7. After go-live

Name the reporting the site and company agreed: usage against the expected usage profile, anonymized aggregate outcomes, performance changes (CS61, CS62). This is what the sibling monitoring skill will read.

### Step 8. Stops

List what stops: issuing the go-live plan to the health system (accountable owner, worker stop rule); any statement to the customer that a site is live or ready; clinical risk acceptance (the deploying organization's); clinician-facing training (editorial holder). If asked for wording to the site, write only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/go-live-bar-output.md`. Answer first: the bar in a table with evidence types, the pass rule, and the site approver, or what is missing to set them. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every bar item is the person's or labeled "starting list" or "candidate".
- Every item has an evidence type other than a plan status field.
- No site is called live; no date proposed.
- Any ranking is of the person's scores, with the flip point.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Setting the bar. Checking a site against it is the sibling skill (DH-02.02.1.2).
- No legal sign-off on agreements; no clinical safety sign-off.
- Outcome-linked payments to or from the customer are Market Access (outcomes-contract-monitoring).
