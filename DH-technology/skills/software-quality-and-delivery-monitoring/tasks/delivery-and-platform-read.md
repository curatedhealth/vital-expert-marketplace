# A2 Delivery and platform read

Framework task: DH-04.03.3.2 with DH-04.03.1.2 and DH-01.06.4.2, Part A, task A2. Carries the old tasks "DH-04.03.3.2.1 Deploy frequency and failure", "DH-04.03.3.2.2 Skipped stage check", "DH-04.03.1.2.1 Capacity evidence", "DH-04.03.1.2.2 First-failure review", "DH-04.03.1.2.3 Region and residency check" and "DH-01.06.4.2.1 Platform Performance Monitoring" as steps, plus the SBOM end-of-support read and the public recall read.

## What this task delivers

Over a period the person states: deploys, rollbacks, failed health checks and reverted clinical defects counted from the release log; releases that skipped a required stage and whether the exception was recorded at the time; scale claims against the latest measurement; saturation against the component the design named; live store regions against the placement table; SBOM components past end of support or no longer maintained, and any CVE ids found in a KEV list the person supplies; and public recall records of comparable software in the period. It answers "what happened in our delivery and on our platform in this period, against our own lists?"

Why it matters: FDA's Change Control inspection area checks that changes are evaluated before implementation (QS34); vulnerabilities in CISA's KEV catalog should be designed out (EN-052); a cloud provider holding ePHI is a business associate wherever it stores it [WF] (EN-032, EN-034). No source sets a target for any of these measures, so the read is facts against the person's lists, never a rating.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `digital-health-product-manager` (old DH-04.03.3.2.x and DH-04.03.1.2.x); `ai-ml-governance-director` (old DH-01.06.4.2.1). Work as a delivery and platform analyst who reads the person's logs |
| Skill | DH-04.03.3.2 Part A, Delivery and platform read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` sections 2 to 5; the research files |
| Tools | `scripts/delivery_check.py releases`, `capacity`, `residency`, `sbom`; `regulatory-dh.list_jurisdictions` and `regulatory-dh.search_safety_events` (step 6); `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/delivery-and-platform-read-output.md` |
| Input | The request and its context: the period and read date, the release log, the required stage list, the capacity record, the placement table and live regions, the SBOM, a KEV list the person downloaded (optional), the comparable products or manufacturers to search |
| Governance | `references/governance.md`; thresholds and readings are the person's |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Period and read date.** Both needed for steps 1 and 5. If missing, ask; never default to today.
- **Required stages.** The person's list (old rule: compare release records with the stage list). If none, ask; without it, skips cannot be read.
- **Benchmarks.** If the person cites an industry benchmark or asks for "an acceptable rate", say no source in this skill sets one, show the arithmetic on their log, and leave the reading to them.
- **Short or full.** "How did our releases go last quarter?" is short mode. "Full delivery and platform read" is full mode.

## Workflow

### Step 1. Deploys and failures (old 3.2.1)

Run `python3 scripts/delivery_check.py releases --log R.csv --required STAGES --from DATE --to DATE`. Report deploys kept, rollbacks and failed health checks separately from releases the person marked as a reverted clinical defect (old rule: separate a failed health check from a reverted clinical defect), the stage that caught each failure or "caught in production" (R3), and caught-at not given (R4). The percentage the script prints is arithmetic on the log, never a rate to compare. Old rule: a green dashboard is not reported as zero failures.

### Step 2. Skipped stages (old 3.2.2)

From the same run: R1 releases that skipped a required stage; R2 skips with no exception recorded at the time. Old rule: an unrecorded skip is not treated as a hotfix. Changes evaluated before implementation is the FDA inspection area's purpose (QS34); state it as context, not as a finding.

### Step 3. Capacity and first failure (old 1.2.1, 1.2.2, 06.4.2.1)

Run `python3 scripts/delivery_check.py capacity --file K.csv`. Show measured against design as arithmetic, with the measurement date and environment. K1: a cloud quota is not a load test. K2: no measurement. K3: saturation on a component other than the one the design named; old rule: show it, never hide it; whether the design note is corrected is the person's.

### Step 4. Region and residency (old 1.2.3)

Run `python3 scripts/delivery_check.py residency --file P.csv`. Y1 live region differs from design; Y2 a replica outside the design region; Y3 backup region not given or outside (old rule: never assume a backup stays in the primary region). For ePHI, note the BAA and risk analysis rows [WF] (EN-032 to EN-034). Whether a location is permitted is for the owner the person names; GDPR transfer rules are not in the sources (`[GAP]`); route to `cybersecurity-and-privacy-by-design` (this pack).

### Step 5. SBOM end of support and known vulnerabilities

Run `python3 scripts/delivery_check.py sbom --file S.csv --as-of DATE [--kev KEV.csv]`. S1 support fields missing, S2 support level outside FDA's three values, S3 no longer maintained or abandoned (EN-054), S4 past end of support with the days counted from the person's read date (a fact, not urgency), S5 a CVE id the person listed that appears in the KEV list they supplied (EN-052; CISA's use of KEV [WF], EN-080). Name vulnerabilities by their public identifiers only. The 524B patch cadence (EN-044) and the postmarket enforcement-policy clocks (EN-066, EN-067, not statutory) are context; controlled or uncontrolled risk and patch priority route to `security-and-privacy-operations-monitoring` (this pack).

### Step 6. Public recall records in the period

Call `regulatory-dh.list_jurisdictions {}` once, then `regulatory-dh.search_safety_events {manufacturer: "<stored spelling>" or product_code: "<code>", jurisdiction: "US", since: "<period start the person gave>", limit: 10}`. For the UK, `{product: "software", jurisdiction: "UK"}` returns MHRA alerts with gov.uk links. Quote title, date and class as the record states them; drop rows matched only on title words; never judge relevance; an empty result is not evidence of safety (`references/tools.md`). Reportability routes to `dh-regulatory-and-quality` audit-capa-and-complaints.

## Build the output

Follow `assets/delivery-and-platform-read-output.md`. Answer first: the counts from steps 1 and 2, the capacity and residency flags, the SBOM components past end of support or in the supplied KEV list, and any recall records in the period. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No threshold, benchmark tier or rating; percentages are arithmetic on the person's log.
- No exploit detail; CVE ids only.
- Recalls quoted as stored, with no relevance judgment.
- `python3 scripts/delivery_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Vulnerability response and patch priority: `security-and-privacy-operations-monitoring` (this pack).
- Model performance and drift: `model-performance-and-drift-monitoring` (this pack).
- Interface failures with EHRs: `integration-quality-monitoring` (this pack).
- Misses, owners and the release gate: task B1 of this skill.
