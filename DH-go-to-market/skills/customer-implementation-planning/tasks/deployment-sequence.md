# A2 Deployment sequence and prerequisites

Framework task: DH-02.02.1.1, Part A, task A2. Replaces the old register task "Deployment sequence" (CF-12.02.02.1.1.2).

## What this task delivers

The deployment steps in dependency order, each with the owner the person named, the contract and data steps the sources require before personal data flows, training placed after the day-one workflow is configured, the steps that belong to the site rather than the vendor, the go-live date the site expects (or "unset"), and a list of conflicts in the person's own plan. It answers "in what order do we do this, and what has to be signed or set before the next step can start?"

Why it matters: a vendor may handle PHI only under a written business associate contract (CS96), and an EU processor only under a written Article 28 contract (CS110). Interface tests with live records or a silent-mode run on local data are data flows too. Training given before configuration decays before use (CS78).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.1 Part A, Deployment sequence and prerequisites |
| Workflow | The steps below |
| Knowledge | `references/deployment-prerequisites.md`; CS and CP rows in the two research files; A1 scope if present |
| Tools | `scripts/plan_sequence.py` (optional); `regulatory-dh.search_safety_events` (counted, optional, Step 6) |
| Prompt | This guide |
| Template | `assets/deployment-sequence-output.md` |
| Input | The request and its context: market, site type (for example NHS trust, US hospital, clinic group), the steps with owners, dependencies and dates, which steps move personal data, the scope from A1 |
| Governance | `references/governance.md`; contract terms stop for the legal or privacy owner; go-live plans issued to the customer stop for the accountable owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. post-market-watch also reads safety events but sets a watch; it is not called. |

## Read the request

- **Market and site type.** US (HIPAA), EU (GDPR), England NHS (DTAC, DCB0160), or several. Ask if unclear; the prerequisite set depends on it. Other markets: `[GAP]`.
- **The plan.** Steps, owners, dependencies, dates, as a table or a CSV in the columns `scripts/plan_sequence.py` reads (listed in its header). If they have no plan, build the step list from the register steps (access, configure, train, go-live) plus the market's prerequisites, with owners and dates left for them.
- **Data flows.** Which steps move personal data to the vendor: live interface tests, silent mode on local data, go-live, scale-up.
- **Mode.** Short for "check my plan"; full for a sequence document.

## Workflow

### Step 1. Add the prerequisite steps for the market

From `deployment-prerequisites.md` sections 2 to 4, add any missing gating steps, each marked "added: required by row X" or "added: option (row X)":
- US: business associate agreement with the elements in section 2 (CS96 to CS102); role-based access (CS104); routine disclosure protocol for scheduled feeds (CS105). Site-owned: workforce PHI and security training (CS82, CS83).
- EU: Article 28 contract with clauses (a) to (h), sub-processor authorization (CS106 to CS110, CP-EU-01 to CP-EU-09).
- England NHS: DTAC review by the buyer (CP-UK-01 to CP-UK-04; CS69 [WF]); the deploying organization's own clinical risk assessment and DCB0129 evidence from the manufacturer (CP-UK-06, CP-UK-09, CP-UK-10; CS71 [WF]). Note these rest on NHS England guidance pages, not the standards' texts.
- US hospital EHR context, where the person says it applies: SAFER Guides self-assessment as the hospital's step (CS72 to CS74).

### Step 2. Order the steps

With code execution, save the plan as CSV and run `python3 scripts/plan_sequence.py PLAN.csv`. It prints the dependency order, the longest chain of planned durations, and findings: unknown or circular dependencies, a step starting before its prerequisite finishes, training before configuration (S2), personal data before the agreement (S1), personal data before user roles and access are set (US: CS103, CS104; other markets `[GAP]`), missing owners and dates. Without code execution, do the same checks by hand.

### Step 3. Place training

Training starts after the day-one workflow is configured (S2, register rule) and matches the training that was validated (CS80). Training knowledge decays (CS78), so a long gap between training and go-live is a fact to show the person, not a verdict. Training content is DH-02.02.4.x.

### Step 4. Optional steps the site may choose

Silent mode on local data before use in care, where local data can change performance (CS60); staged scale-up from pilots (CS47). Show them as options with rows, labeled "option"; the choice is B1's and the person's.

### Step 5. Owners and dates

Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Steps the law gives to the site (for example the site's workforce training, the DCB0160 assessment) are shown as the site's. Dates are the person's; the go-live date is the site's or "unset".

### Step 6. Field events for the product (optional)

If the person asks whether anything in the field affects the go-live, call `regulatory-dh.search_safety_events {manufacturer or product: "<theirs>", since: "<date they choose>", limit: 10}`. Report each event by its record (title, date, class, summary), say the source link is the openFDA API, and that no events is not evidence of no events. Whether to hold go-live is the person's call.

### Step 7. What it means for the person

Two or three consequences from the rows, stated conditionally. Example: "If the interface test uses live records from 16 November and the BAA is signed on 20 November, PHI would reach the vendor before the written contract CS96 requires."

## Build the output

Follow `assets/deployment-sequence-output.md`. Answer first: the conflicts in the plan (or "none found by the checks"), then the order. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every added step names the row that requires it, or is labeled "option".
- No date or owner was invented.
- Contract elements are listed, never judged as met: that is the legal or privacy owner's.
- No personal data step precedes the written agreement in your own proposed order.
- No personal data step starts before user roles and access are set, and each depends on the access step (US: CS103, CS104; other markets `[GAP]`).
- If it goes to the customer, it is a go-live plan issued to a health system: stop for the accountable owner, ask who clears it, call `verify.build_record`.

## Boundaries

- Sequence and prerequisites only. Whether a contract meets the law is the legal or privacy owner's; clinical risk acceptance is the deploying organization's.
- Interface build is the Interoperability pack; training content is DH-02.02.4.x.
- Anything given free to the site or patients, and any payment tied to referrals or outcomes, stops for the compliance or legal owner (`deployment-prerequisites.md` section 7).
