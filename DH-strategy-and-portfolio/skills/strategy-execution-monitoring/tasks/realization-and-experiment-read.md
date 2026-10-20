# A2 Realization and experiment read

Framework task: DH-01.05.4.2 with DH-01.05.1.2 and DH-01.08.2.2, Part A, task A2. Carries the old tasks "DH-01.05.4.2.1 Strategy Realisation Monitoring", "DH-01.05.1.2.1 Opportunity Realisation Monitoring" and "DH-01.08.2.2.1 Experimentation Quality Monitoring".

## What this task delivers

As of a read date the person gives: each benefit's baseline, target and latest actual with its date, and the share of planned change; each milestone's status against its due date and evidence; each option test's plan elements and result, with the tests that cannot be read against a rule written before the start; and, for each partner, licensor or acquired company named in the strategy, what changed in its dated public record, with its company status line. Optional: the person's own benefit forecast rerun with their actuals. It answers "where do we actually stand, and what is the record behind it?"

Why it matters: progress reported from slides drifts from the register; a quiet partner record read as "no change" can hide a period the library never logged. The read keeps the person's numbers, their dates and the record's limits side by side.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `behavior-change-designer` (old DH-01.05.4.2.1 and DH-01.05.1.2.1); `ai-ml-governance-director` (old DH-01.08.2.2.1). Work as a strategy delivery analyst who reads data against the person's plan |
| Skill | DH-01.05.4.2 Part A, Realization and experiment read |
| Workflow | The steps below |
| Knowledge | `references/execution-frameworks.md` sections 2, 4 and 5; rows SP-096, SP-104, SP-105, SP-111 to SP-115, SP-148 to SP-176, DL-019 to DL-021, DL-135 to DL-168 |
| Tools | `scripts/execution_check.py benefits`, `milestones`, `experiments`; for named partners `diligence-dh.get_deltas` and `diligence-dh.build_company_profile`; optional `analytics.scenario-modeler` and `analytics.risk-tornado` on the person's forecast |
| Prompt | This guide |
| Template | `assets/realization-and-experiment-read-output.md` |
| Input | The request and its context: the read date, the benefits register, milestone log and experiment log (A1 or the person's CSVs), named partners and the period, the person's forecast formula and ranges if any |
| Governance | `references/governance.md`; no on-track verdict |
| Catalogue job | none |

## Read the request

- **Read date.** The person's. If not given, write "read date: not given" and ask; never assume today, and never supply one and then flag it.
- **Files.** Use the person's CSVs as given; never edit a value. Missing columns: "not given".
- **"Portfolio".** If the person asks how "the portfolio" is doing, ask whether they mean the product portfolio (`product-portfolio-review`, this pack) or an investment portfolio (`investment-portfolio-monitoring`, this pack) before reading anything.
- **Partners.** Exact legal names and the period. A press report the person cites is "from you (press claim, not checked)".

## Workflow

### Step 1. Benefits

Run `python3 scripts/execution_check.py benefits --register REG.csv --as-of DATE`. Report per benefit: baseline, target, actual with its date, share of planned change ((actual - baseline) / (target - baseline)), the person's rule and whether it is met, and flags E1 to E7. Counts: met, not met, not measurable. A benefit without baseline or target is not measurable; say which is missing.

### Step 2. Milestones

Run `python3 scripts/execution_check.py milestones --log LOG.csv --as-of DATE`. Report due, completed, evidence, elements of the person's pass rule that failed, recheck date, and flags M1 to M6. A milestone not yet due is "not yet due"; never failed early. For each milestone with a failed element, state from the log (the script prints it) which objective it serves and which milestones depend on it (objective and depends_on columns), as a fact, in the Answer paragraph (for example "M3, region South contract, serves O1; no milestone in the log depends on it").

### Step 3. Option tests and experiments

Run `python3 scripts/execution_check.py experiments --log EXP.csv`. Report each test's endpoint, rule, sample planned and actual, result as given, and flags X1 to X6. List the tests that cannot be read against a rule written before the start (old task: "list inconclusive tests"). A rule written after the start (X3) is reported as a fact; the result is not read against it as if it were prespecified. An early test was never meant to prove effectiveness (SP-115).

### Step 4. Named partners, licensors or acquired companies (library)

Call `diligence-dh.get_deltas {companies: ["<exact legal name>"], since: "<period start>"}`. Report changes by type with dates, and the log caveat (first entry 12 October 2026, last sweep, event-date filter). If the period starts before 12 October 2026, say the log cannot show it and call `diligence-dh.build_company_profile {company: "<exact legal name>"}` for the dated authorizations and filings in the period instead; never write "no change". Then the company status line (`execution-frameworks.md` section 5): for a company the research pass read, quote its filings by name and date with what each form does not mean; otherwise quote a filing or register read, or "Company status [GAP]: not read" with the filings to open. State the product's current FDA listing holder beside the authorization holder where a row gives it. If the profile's products do not match what the person says the partner supplies (for example a licensor named for a triage algorithm whose record lists only other products), say so as a fact and ask the person to confirm the counterparty's legal name on the contract. A press claim the person brings is answered from the record and its date corrected if the filings date it differently. A listed partner's material agreement changes appear on 8-K Item 1.01 (DL-020) or as 10-Q or 10-K exhibits (SP-130, SP-133). What a partner's change means for the agreement is for the owner the person names for legal matters, or owner not named.

### Step 5. Forecast rerun (only if the person gives a formula)

Run the person's benefit formula with their actuals through `analytics.scenario-modeler {parameters, formula, periods, aggregate}` (`**` for powers), and `analytics.risk-tornado` with the person's ranges for every parameter. Flag any default plus or minus 20 percent range as not theirs. If the person applies optimism bias (SP-096, UK public-sector guidance), keep their adjustment labeled as theirs. The rerun is a hypothesis on their numbers, never a target.

## Build the output

Follow `assets/realization-and-experiment-read-output.md`. Answer first: as of the read date, counts of benefits met, not met and not measurable against the person's rules; milestones with failed elements and the objective each serves; tests that cannot be read against a prior rule; and the partner record line with its status. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Values and counts come from the script output, not from memory or the person's slides.
- No overall on-track or off-track verdict; no kill or continue.
- "No change" never covers a period before 12 October 2026.
- The company status line is present for each named partner: quoted from a filing or register read (section 5 for companies the research pass read), or "[GAP]: not read" with the filings to open.
- Press claims are labeled as the person's, not as signals.
- `python3 scripts/execution_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; "(inference)" rows carry the label each time.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Partner and channel performance for one's own product: `dh-go-to-market` channel-and-partnership-monitoring.
- Customer value realization: `dh-go-to-market` value-realization-monitoring.
- Clinical study conduct behind a test: `dh-clinical-development` trial-operations-monitoring.
