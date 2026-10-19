# B1 Expansion result review

Framework task: DH-02.02.2.2, Part B, task B1. Replaces the earlier "Expansion result" section (CF-12.02.02.2.2.3) and the old one-line pass rule and owner sections.

## What this task delivers

A review of growth offers in a period: each offer matched to a signed expansion, a refusal or still open, with contract ids; outcomes that are not signatures (meetings, verbal yes) shown apart; refusals and losses by recorded reason with where each routes; the person's rules checked; repairs labeled proposed, owned by the person they name, ranked only if the person scored them; and the stops. It answers "did our growth offers turn into signed expansions, and what do we fix?"

Why it matters: an offer refused because the account has not yet seen a result needs a different owner from one refused on price (SR21). A repair that adds a credit or a free module to win the account back is itself an offer with its own rules (`references/offer-rules.md`).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.2 Part B, Expansion result review |
| Workflow | The steps below |
| Knowledge | `references/reading-results.md`; `references/offer-rules.md`; `references/renewal-measures.md`; A2 output |
| Tools | `scripts/renewal_metrics.py expansion` (local); `analytics.mcda` or `analytics.rice` (counted, only on the person's scores); `verify.build_record` |
| Prompt | This guide |
| Template | `assets/expansion-result-review-output.md` |
| Input | The request and its context: the account file with offers and outcomes, the definitions (A1), the offer period, the person's rules (for example a minimum acceptance share), repairs the person is weighing with criteria, weights and scores, owners |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: a signature is a signature

Only what the person's definition counts as signed is an expansion. A meeting, a verbal yes or a proposal sent is not (SR22, if adopted). Results are checked against the person's own rules; without a rule, report the number and no verdict.

## Read the request

- **Offer period and definitions.** From A1, including `signed_values`, `refused_values`, `offer_open_values`.
- **Rules.** The person's rule for each figure.
- **Repairs.** What the person is weighing; scores and weights if they want a ranking.
- **Owners.** As the person names them.
- **Mode.** Short for "did the upsells convert"; full for an expansion review.

## Workflow

### Step 1. Match offers to outcomes

With code execution:

`python3 scripts/renewal_metrics.py expansion ACCOUNTS.csv DEFINITIONS.json`

It counts offers made, signed, refused and open, gives acceptance with its formula, lists refusals with their recorded reason, and lists outcomes outside the person's lists (for example "meeting held") as not signed. Without code execution, do the same by hand.

### Step 2. Reasons and where they route

For each refusal (and each loss from A2 if the person asks), write the recorded reason and route it from `references/reading-results.md`. Where the reason is an unseen result, name the owner the person gives (SR21, if adopted) and route to the Customer Health skills. Where payment depends on outcomes, route to Market Access (`outcomes-contract-monitoring`). Where the reason is price, the pricing owner. Hypotheses only on request, at most three, labeled, with what would confirm each.

### Step 3. Check against the person's rules

For each rule: the number, met or missed. Without rules, "no rule set" and ask once.

### Step 4. Repairs, labeled proposed

List the repairs the person named; add others only as "proposed", each tied to a reason. Any repair that is an offer element (credit, discount, rebate, free module or service, extended trial, anything for patients, fees to third parties, outcome terms) is run through `references/offer-rules.md`: the rows, the elements required, the facts missing, and "Stops for: [compliance or legal owner as named, or owner not named]". Never say it is protected.

### Step 5. Owners

One owner per repair, as the person names them, or "owner not named" and ask. Never suggest a job title.

### Step 6. Rank only what the person scored

If the person gives scores (0 to 4) and weights (summing to 1), call `analytics.mcda` with `alternatives` and `criteria_weights`; report values and contributions, and state any tie plainly (the connector does not). If they score by reach, impact, confidence and effort, use `analytics.rice`. Without scores, no ranking.

## Build the output

Follow `assets/expansion-result-review-output.md`. Answer first: offers signed out of offers made, acceptance with its formula, the refusals by reason, and which of the person's rules were missed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Only signatures are counted as expansions; other outcomes are listed apart.
- Every verdict comes from the person's rule.
- Reasons are as recorded; causes are hypotheses, labeled.
- Every repair the person did not name is labeled proposed; concessions stop for the compliance owner.
- Every score and weight is the person's; ties are stated.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Review of offers already made. Building the next offer is the sibling skill (`account-growth-and-renewal`, A2).
- Outcome and value tracking with the customer is the Customer Health skills.
- No price, no contract wording, no legal opinion.
