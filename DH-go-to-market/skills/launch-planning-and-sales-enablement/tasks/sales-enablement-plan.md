# B1 Sales enablement plan

Framework task: DH-02.01.1.1, Part B, task B1. Replaces the earlier "Sales leave-behind" and "Enablement roster" sections. Catalogue job on the library: `sales-leave-behind` (the one-call option for the research step; the leave-behind itself is still built here from approved claim ids).

## What this task delivers

Three things the field needs before go-live, each a draft for the person: (1) the leave-behind and the objection responses, both built only from claim ids on the approved list (A2), with any required section or objection that has no approved claim marked `[GAP]`; (2) the enablement roster: every role that will use it, who briefs them and when, and any role that will not be briefed, with the reason; (3) the field activities in the plan that stop for the compliance or legal owner, with the elements the rows set. It answers "what do our people hand over, who has to be able to deliver it, and what must not happen in the field?"

Why it matters: the leave-behind is promotional labeling the moment it accompanies the product (PC-US-02), and every free item, sample, speaker fee or partner commission is a potential inducement (CP-US-01, CP-US-08). Enablement done well is the launch claim list delivered by people who were briefed on it, with no activity that a compliance owner has not seen.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.1 Part B, Sales enablement plan |
| Workflow | The steps below |
| Knowledge | `references/enablement-rules.md`; `references/claim-rules.md`; A2 approved claim list; A1 prerequisites |
| Tools | `scripts/claim_screen.py` (checks the leave-behind and objection responses against the approved ids); optional research inputs `commercial-dh.generate_commercial_brief`, `commercial-dh.get_pricing_corridor`, `commercial-dh.audit_claims` (directly or through the catalogue job); `analytics.rice` or `analytics.mcda` only to rank options the person scored; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/sales-enablement-output.md` |
| Input | The request and its context: the approved claim list with ids, audience and format of the leave-behind, the roles that will use it, briefers and dates the person sets, planned field activities (samples, training, speaker programs, patient support, partners), the owners |
| Governance | `references/governance.md`; people decide content, roster and dates; compliance or legal owner decides on field activities |
| Catalogue job | `sales-leave-behind` (start_job returns the method and tool names; it does not write the leave-behind). Runs brief, price corridor and claim labels as research. Behavior and pitfalls: `references/tools.md`; live run: `examples/live/job_sales_leave_behind_K191716.json` |

## Read the request

- **Approved claims.** Required. If there is no approved list, run A2 first or mark every content section `[GAP]`. A claim on a "proposed" list is not approved.
- **Format and audience.** One format (one-pager or short deck) and one audience role per leave-behind (old task rule). HCP, payer and consumer versions are separate pieces with separate rules.
- **Roles.** Field, medical, access, customer success, partners: take the person's list.
- **Briefers and dates.** The person's. Never pick a date or a briefer.
- **Field activities.** Ask what the plan includes beyond briefing: samples, demo units, loaner devices, training events, consultants or speakers, patient support tools, reseller or referral partners, co-marketing.
- **Objections.** Ask which objections the field hears (for example "is there evidence", "who pays", "how does it fit our workflow"). Use the person's wording.
- **Pass rule.** For example "every customer-facing role briefed before first call". Ask; never set one.
- **Owners.** In the person's words, or "owner not named".

## Workflow

### Step 1. Build the leave-behind from approved ids only

Lay out the sections the person wants (for example indication, how it works, evidence, access route, safety information, contact). Fill each only with approved claim ids, quoted exactly. Any required section with no approved claim is `[GAP]`; no new claim is written here (old task rule). Required statements that come with the content stay with it: material study limits and unfavorable findings (PC-US-31), the labeled indication for payer pieces (PC-US-46), the DiGA pre-use information duty for a DiGA's own materials (PC-DE-17). With code execution, run `scripts/claim_screen.py --claims APPROVED.csv --text LEAVE_BEHIND.txt` to catch any sentence that is not an approved claim and any risk word.

One-call option: if the person wants the connector's research behind the piece, run the catalogue job `sales-leave-behind` (or its three calls directly): `commercial-dh.generate_commercial_brief` with `reference` (FDA submission number for US products), `commercial-dh.get_pricing_corridor` with `reference`, and `commercial-dh.audit_claims` with `reference` and the approved claims only. Treat everything it returns as research, never as leave-behind text. Pitfalls from the live run (`references/tools.md`): the brief in JSON is about 379,000 characters; claim labels say `exceeds_record` even for an on-label claim because no intended purpose is stored; corridor rows carry no product name, so a price row whose `source_url` is not the product's own record is dropped; a DiGA listing is not printed beside `no_authorization_on_file` although the job says it is. Leave the payer argument out if the person has not named one: a typed placeholder is counted as "attested".

### Step 1b. Objection responses from approved claims only

Method, not a sourced rule. For each objection the person names, write: the objection in their words; the approved claim id or ids that answer it, quoted exactly; the required statements that travel with that claim (as in step 1); and, if no approved claim answers it, `[GAP]` with "route to the claims owner for a new claim through A2". Never write a new claim, a comparison or a number in a response. An objection that can only be answered with an unapproved or uncleared use goes to authorized personnel and is identified as such (PC-US-92 [INDUSTRY]). An objection about price or coverage gets no figure unless the approved list holds one; payer amounts are Market Access's subject. Run `scripts/claim_screen.py` on the response text only, as on the leave-behind (the objection line is the person's question and would be flagged as not approved).

### Step 2. Build the roster

For each role: what it will use, who briefs it, the date the person set, and the format. A role that will not be briefed is recorded with the reason (old task rule). A file in a shared folder is not a briefing. Product training for HCPs follows the [INDUSTRY] code rows the person adopts (PC-US-91, PC-EU-18). Off-label questions route to authorized personnel (PC-US-92 [INDUSTRY]).

In every table, tag [INDUSTRY] or [WF] next to each row id that carries it (for example "PC-US-94 [INDUSTRY]"). Never write a tag without its row id.

### Step 3. Check the pass rule

If the person gave a pass rule, check the roster against it: met, missed, or not yet known, with the role. Without a rule, report the roster without a verdict.

### Step 4. Lay out the field activities that stop

For each planned activity, find its line in `references/enablement-rules.md` section 2 and list the elements the rows set (for example, for a reseller paid per sale: signed writing, at least one year, compensation set in advance at fair market value and not tied to referral volume, CP-US-09). Write the open questions for the compliance or legal owner. Never say the activity is protected or allowed. In Germany, gifts are banned except listed cases (PC-DE-06) and DiGA prescription steering is barred (CP-DE-06).

### Step 5. Rank only what the person scored

If the person wants to choose between enablement options (formats, channels, partners), ask them for criteria, weights and scores, then call `analytics.rice` or `analytics.mcda` with their numbers. Report the result as their ranking. Never score.

### Step 6. Stops and owners

List the stops: material approval (regulatory or legal owner), each field activity in step 4 (compliance or legal owner), any payer piece (accountable owner, Market Access). Name the owners the person gave, or "owner not named".

## Build the output

Follow `assets/sales-enablement-output.md`. Answer first: whether the leave-behind can be built from the approved list (and which sections are `[GAP]`), how many roles are briefed on the person's dates, and which activities stop. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every sentence on the leave-behind and in each objection response maps to an approved claim id; the piece is labeled "draft for approval by OWNER".
- Connector research (brief, corridor, labels) is cited as research with its tool name, never pasted as leave-behind text.
- Every date and briefer is the person's.
- No field activity is called protected, compliant or allowed.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Approving material: the person's regulatory or legal owner.
- Contracts with partners, resellers and health systems: the person's legal owner; this task lays out elements only.
- Payer materials and prices: Market Access.
- Measuring whether briefings happened and claims were used after go-live: the sibling skill, launch performance monitoring.
