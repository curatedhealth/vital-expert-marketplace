# Go-live bar: candidate items, limited launch and reporting after go-live

Interpretive reference for task B1 (and copied into the sibling monitoring skill, which checks a site against the bar). Rows: `CS` from `customer-success-research.md`, `CP-UK` from `channels-partners-research.md`.

The bar is the person's and the site's. The items below are candidates with their source, offered as a starting list labeled "starting list". None is a requirement unless its row says it is one for that market.

## 1. The register's go-live method

From the old Go-live bar task (CF-12.02.02.1.1.3):
- Name the users who must complete one real task.
- Name the data that must be present.
- Name who at the site agrees the bar is met.
- Do not call a site live because the contract started.

## 2. Candidate bar items with sources

| # | Candidate item | Evidence that would show it | Source |
|---|---|---|---|
| G1 | The day-one workflow is configured and named users completed one real task in it | Task log for named roles (not named staff scores) | Register method; CS20 (planning goals defined in advance) |
| G2 | The data the workflow needs is present and flows as mapped | Data flow map and a check of the fields in the data dictionary | CS64 |
| G3 | The written data agreement for the market is signed before data flows | Signed BAA (US) or Article 28 contract (EU) | US: CS96. EU: CS110, CP-EU-04. UK and other markets: `[GAP]`; cite only the rows for the site's market. |
| G4 | User roles and access match job need | Role list against the access set | US: CS103, CS104 (HIPAA). Other markets: `[GAP]`; cite only the rows for the site's market. |
| G5 | The site's users were trained on what the product does, its outputs and limitations, and training matches what was validated | Training record by role; the company's training approach | CS58, CS65, CS80 |
| G6 | Local performance was observed in silent mode before use in care, where the site chose it | Silent-mode summary | CS60 |
| G7 | The expected usage profile and the reporting plan (usage, anonymized aggregate outcomes, performance changes) are agreed | The agreed profile and reporting schedule | CS61, CS62 |
| G8 | Load testing shows the product performs at the expected scale | Load test summary | CS66 |
| G9 | NHS England: the deploying organization did its own clinical risk assessment and has the developer's DCB0129 evidence | DCB0160 assessment; manufacturer's findings | CP-UK-09, CP-UK-10, CP-UK-06 (guidance pages, not the standard); CS71 [WF] |
| G10 | A pilot-site statement is available, if the site wants one: acceptable to users, performed as intended, integrated, no unintended harm, used as expected (who, how, how long) | The statement | CS59 |

## 3. Limited launch and staged scale-up

- ERIC's staged scale-up: start with pilots or demonstrations, then roll out system-wide (CS47).
- Trialability includes being able to undo the implementation after a small test (CS5).
- The choice between rollout options is the person's. If they score options, `analytics.mcda` ranks their scores (see `tools.md`).

## 4. After go-live: the agreed reporting

NICE ESF standard 16: the company and evaluator agree a plan to report usage against the expected usage profile agreed at commissioning, plus anonymized aggregate outcomes (CS61), and for products that change, how and when performance changes are reported and to whom (CS62). The sibling skill (implementation quality monitoring) measures against this.

## 5. Who agrees the bar is met

The site approver the person names. The model never declares a site live; the vendor's implementation team does not either, by the worker's own stop rules (does not own or execute a go-live).
