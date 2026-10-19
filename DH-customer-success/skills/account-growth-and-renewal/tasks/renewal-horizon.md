# A1 Renewal horizon

Framework task: DH-02.02.2.1, Part A, task A1. Replaces the earlier "Renewal horizon" section (CF-12.02.02.2.1.1).

## What this task delivers

A dated list of the accounts whose renewal falls inside the person's horizon, with days to renewal, the readiness verdict on the person's own rule, the facts behind each verdict, what the account agreed to see and whether it has been seen, and the contract and data points the renewal has to cover. It answers "which renewals are coming up, and which accounts are ready to talk about growth?"

Why it matters: an account with an open implementation has not yet had the chance to see a clinical or service result, because implementation outcomes come first (CS32 [PAPER], DOI 10.1007/s10488-010-0319-7). A renewal that adds a module or a data flow also reopens the BAA or processor contract (CS96, CS108). Seeing both before the conversation changes what is offered.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.1 Part A, Renewal horizon |
| Workflow | The steps below |
| Knowledge | `references/renewal-facts.md`; `references/starter-rules.md` (SR1 to SR4); `references/gap-rules.md` |
| Tools | `scripts/renewal_metrics.py horizon` (local); no library call |
| Prompt | This guide |
| Template | `assets/renewal-horizon-output.md` |
| Input | The request and its context: the account file or list (account, contract id, renewal date, value, go-live, open implementation items, agreed outcomes and what has been seen, market), the as-of date, the horizon, the person's readiness rule |
| Governance | `references/governance.md`; the person sets the horizon and the readiness rule |
| Catalogue job | none. The horizon runs locally on the person's account file (`scripts/renewal_metrics.py`). |

## The rule that shapes this task: readiness is the person's rule

No source defines readiness to renew or expand. The person states the rule. If they have none, offer SR3 and SR4 ("open implementation bar means not ready"; "no expansion proposal to an account that missed go-live") labeled "register starter rule, yours to adopt", and apply them only after a yes. Without a rule, show the facts and leave the readiness column blank.

## Read the request

- **As-of date and horizon.** Ask for both. The register's example horizon was 120 days (SR1); offer it only as their choice.
- **Account file.** A CSV or a pasted table. Needed fields: account id, contract id, renewal date. Useful: value before renewal, go-live, open implementation items, market, agreed outcomes, result seen. Map the person's column names; do not ask them to rename.
- **Readiness rule.** Ask once. Offer SR3 and SR4 as above.
- **Markets.** US, EU, Germany (DiGA), England (NHS): they decide which facts in `renewal-facts.md` apply.
- **Mode.** Short for "which renewals are coming up"; full for a renewal pipeline document.

## Workflow

### Step 1. Fix the window

Write back the as-of date, the horizon in days and the end date, in full. Count days to renewal to the as-of date.

### Step 2. List the renewals

With code execution, write the person's definitions to a JSON file (`as_of`, `horizon_days`, and `not_ready_if` rules if they adopted a rule, each `{field, op, value}` with op `eq`, `ne`, `gt`, `lt` or `in`) and run:

`python3 scripts/renewal_metrics.py horizon ACCOUNTS.csv DEFINITIONS.json`

The script lists accounts with a renewal date after the as-of date and on or before the window end, applies the person's rule, names the rule hit per account, and flags open accounts whose renewal date has already passed. Without code execution, do the same by hand and show the count.

### Step 3. Readiness facts per account

For each account in the window, write the facts that bear on the person's rule: go-live (yes, no, not recorded), open implementation items, and what the account agreed to see against what it has seen. Where an NHS commissioner agreed an expected usage profile at commissioning (CS61), name it as the account's yardstick; for an NHS account with none recorded, "usage profile not recorded `[GAP]`"; for other or unknown markets, leave CS61 out. If a usage figure is quoted, ask its denominator (CS27, CS39). Keep "value unseen" separate from "implementation not complete" (CS32).

### Step 4. Points the renewal must cover

From `references/renewal-facts.md`, list only the points that apply to the account's market and to what may change at renewal:

- Any added module, site or data flow: does the BAA cover the new use (CS96, CS97)? For EU accounts, the Article 28 contract and sub-processors (CS108, CS107)?
- An account that may not renew: the return or destroy duty for PHI (CS100), and the controller's delete-or-return choice in the EU (CS109).
- German DiGA user terms: no opaque or auto-renewing offers (PC-DE-17). The negotiated reimbursement amount is Market Access's subject (CP-DE-08).
- NHS: DTAC is reviewed in procurement and the form changed in 2026 (CP-UK-01, CP-UK-04); framework entry limits (CP-UK-12).
- US customers billing DMHT codes: any free device can remove their billing basis (CP-US-59); route to A2.

In short mode, list only points tied to an account in the window; put the others in one line offering the full version.

### Step 5. Say what it means for the person

Two or three lines, from the facts only. Examples: "Two of three renewals in the window are not ready on your rule, both for open implementation items; a growth offer to them would break the rule you adopted (SR3)." "ACC-08's renewal date passed on 31 August 2026 and the file still says open: the record needs checking before it is counted anywhere."

## Build the output

Follow `assets/renewal-horizon-output.md`. Answer first: how many renewals fall inside the window, which are ready on the person's rule, and the nearest renewal date. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The as-of date, horizon and readiness rule are the person's and the output says so.
- No account is called healthy, at risk or likely to renew; only "ready" or "not ready" on the person's rule, or no verdict.
- Every fact about contracts or data carries its row id; every unknown is `[GAP]`.
- No urgency language; days to renewal are facts.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The list and readiness only. Offers are A2; risk notes and actions are B1; renewal rates after the fact are the sibling skill (`expansion-and-renewal-monitoring`).
- Outcome tracking with the customer is the Customer Health skill (`outcome-tracking-and-customer-health`). Where payment depends on outcomes, the contract is Market Access's (`outcomes-contract-monitoring`).
- No legal reading of the person's contracts: the skill lists the points; the legal owner reads the contract.
