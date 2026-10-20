# Worked example: delivery and platform read, then release gate review (illustrative logs, live recall records)

Runs A2 and B1 of `software-quality-and-delivery-monitoring`, with the A1 trace that B1 draws on. Every file in `examples/sample-data/` is ILLUSTRATIVE: typed for this example; "GlucoStep" and "CardioTrack" are invented products, the people named are invented, and the CVE ids (CVE-2099-nnnnn) and the KEV list are deliberately fictional. The recall records come from a saved live library output of 19 October 2026 (`examples/live/safety_events_QRX_2026-10-19.json`, copied from the dh-regulatory-and-quality build). The connector was disconnected on 20 October 2026, so no new library call was made.

## Requests

A2: "Read date 20 October 2026. Here are our release log, capacity record, placement table and SBOM for GlucoStep, plus the KEV list I downloaded. Our required stages are build, test, review, release. How did 1 July to 30 September 2026 go, and anything public on similar app recalls in that window?"

B1: "Candidate 3.2.1-rc2. Here is our miss log with our rules. Review the misses: what failed, who owns it, can it pass our gate?"

## Calls

| Step | Call | Saved file or output | Date |
|---|---|---|---|
| A1 steps 2 to 4 (for B1) | `python3 scripts/delivery_check.py trace --hazards examples/sample-data/hazards_illustrative.csv --cases examples/sample-data/cases_illustrative.csv --candidate 3.2.1-rc2` | below | 20 October 2026 |
| A2 steps 1 and 2 | `python3 scripts/delivery_check.py releases --log examples/sample-data/releases_illustrative.csv --required build,test,review,release --from 2026-07-01 --to 2026-09-30` | below | 20 October 2026 |
| A2 step 3 | `python3 scripts/delivery_check.py capacity --file examples/sample-data/capacity_illustrative.csv` | below | 20 October 2026 |
| A2 step 4 | `python3 scripts/delivery_check.py residency --file examples/sample-data/residency_illustrative.csv` | below | 20 October 2026 |
| A2 step 5 | `python3 scripts/delivery_check.py sbom --file examples/sample-data/sbom_illustrative.csv --as-of 2026-10-20 --kev examples/sample-data/kev_list_illustrative.csv` | below | 20 October 2026 |
| A2 step 6 | `regulatory-dh.list_jurisdictions {}`; `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` | `examples/live/list_jurisdictions_2026-10-19.json`; `examples/live/safety_events_QRX_2026-10-19.json` | 19 October 2026 |
| B1 step 2 | `python3 scripts/delivery_check.py misses --file examples/sample-data/misses_illustrative.csv --as-of 2026-10-20` | below | 20 October 2026 |

The saved QRX call carried no `since` filter; its newest recall row is dated 27 May 2026, so no stored row falls inside the period. A live rerun with `since: "2026-07-01"` **needs a live check**.

## Script output

```
Release candidate: 3.2.1-rc2. Hazards from your risk file; cases from your test records.
| Hazard | Item | Class (yours) | Cases | Levels | Flags |
|---|---|---|---|---|---|
| HZ-01 Advised dose too high after unit conversion error | SI-01 | C | TC-10, TC-11 | system, unit | none |
| HZ-02 Stale glucose value shown as current | SI-02 | B | TC-20, TC-21 | unit | T2 |
| HZ-03 Alert not delivered when app is in background | SI-07 | A | none | none | T1 |
| HZ-04 Data loss on sync conflict | SI-06 | not given | TC-40, TC-41 | integration, system | T6 |

| Case | Hazards | Spec | Expected | Build | Result | Waiver | Flags |
|---|---|---|---|---|---|---|---|
| TC-10 | HZ-01 | SRS-4.2 | Dose shown equals reference table value for 40 unit pairs | 3.2.1-rc2 | pass | not given | none |
| TC-11 | HZ-01 | SRS-4.2 | Conversion function returns mmol/L value to 1 decimal | 3.2.1-rc2 | pass | not given | none |
| TC-20 | HZ-02 | SRS-5.1 | Works correctly | 3.2.1-rc2 | pass | not given | T5 |
| TC-21 | HZ-02 | SRS-5.3 | Timestamp label updates within 1 second of new value | 3.2.0 | pass | not given | T3 |
| TC-40 | HZ-04 | SRS-7.2 | Conflicting edits resolved by server timestamp | 3.2.1-rc1 | fail | not given | T3, T4 |
| TC-41 | HZ-04;HZ-09 (not in hazard list: HZ-09) | SRS-7.3 | No record lost after 500 simulated conflicts | 3.2.1-rc1 | pass | Re-run waived by owner; sync code unchanged since rc1 | none |

Hazards: 4; flags T1 1, T2 1, T6 1. Cases: 6; flags T3 2, T4 1, T5 1.
T2 lists hazards whose only cases are unit-level; whether they exercise the hazard is yours to judge. Repeat or waive T3 cases is your decision. No coverage figure is a rule unless you set one.

Period: 1 July 2026 to 30 September 2026. Required stages (yours): build, test, review, release.
| Release | Date | Build | Stages run | Skipped | Exception | Recorded on | Outcome | Clinical defect | Caught at | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| R-31 | 2 July 2026 | 3.1.6 | build;test;review;release | none | not given | not given | deployed | no | not given | none |
| R-32 | 20 July 2026 | 3.1.7 | build;test;release | review | hotfix | 20 July 2026 | deployed | no | not given | R1 |
| R-33 | 5 August 2026 | 3.2.0 | build;test;review;release | none | not given | not given | rolled_back | yes | production | R3 |
| R-34 | 6 August 2026 | 3.2.0-h1 | build;release | test, review | hotfix | not given | deployed | no | not given | R1, R2 |
| R-35 | 14 September 2026 | 3.2.0-h2 | build;test;review;release | none | not given | not given | failed_health_check | no | release | none |
| R-36 | 15 September 2026 | 3.2.0-h2 | build;test;review;release | none | not given | not given | deployed | no | not given | none |

Releases in period: 6. Deployed and kept: 4; rolled back: 1; failed health check: 1; releases you marked as a clinical defect: 1.
Arithmetic on your log: rolled back or failed 2 of 6 (33%). No source sets a rate; the reading is yours.
Flags: R1 2, R2 1, R3 1. An unrecorded skip (R2) is not treated as a hotfix.

Scale claims against your measurements. Ratio = measured / design (arithmetic, not a verdict).
| Unit | Design number | Measured | Ratio | Measured on | Environment | Kind | First-failure (design) | Saturated | Flags |
|---|---|---|---|---|---|---|---|---|---|
| Sync requests per minute | 12000 | 9100 | 0.76 | 30 September 2026 | production | production peak | Sync API pods | Database connections | K3 |
| Concurrent clinician sessions | 800 | 800 | 1.00 | 12 June 2026 | staging | quota | Web gateway | not given | K1 |
| Bolus calculations per minute | 3000 | not given | n/a | not given | not given | not given | Calculation service | not given | K2 |

Flags: K1 1, K2 1, K3 1. A quota is not a load test (K1). Saturation on a component the design did not name is shown, not hidden (K3); whether the design note changes is yours.

Live placement against your placement table.
| Store | Data class | Design region | Live region | Replicas | Backup | Flags |
|---|---|---|---|---|---|---|
| Patient readings DB | ePHI | us-east | us-east | us-east | us-west | Y3 |
| Audit log store | ePHI | us-east | us-east | not given | us-east | none |
| Analytics warehouse | de-identified | eu-central | eu-central | eu-central;us-east | not given | Y2, Y3 |

Flags: Y2 1, Y3 2. A region difference is a fact; whether it is permitted (BAA, transfer rules) is for the owner you name (cybersecurity-and-privacy-by-design, this pack).

Read date: 20 October 2026. Fields: FDA premarket cybersecurity guidance (EN-054). KEV list: supplied by you, 2 ids.
| Component | Version | Supplier | Support level | End of support | CVE ids (yours) | Flags |
|---|---|---|---|---|---|---|
| Mobile OS runtime | 17.5 | Apple Inc. | maintained | not given | not given | S1 |
| Local database library | 3.39.2 | SQLite Consortium | maintained | 31 December 2027 | CVE-2099-00017 | none |
| Charting library | 4.1.0 | not given | abandoned | 30 June 2025 | not given | S3, S4 (477 days before the read date) |
| Cloud sync SDK | 2.8 | ExampleCloud Ltd | end of life | 31 March 2026 | CVE-2099-00042;CVE-2099-00043 | S2, S4 (203 days before the read date), S5 (CVE-2099-00042) |
| TLS library | 3.0.13 | OpenSSL Project | maintained | 7 September 2026 | not given | S4 (43 days before the read date) |

Components: 5. Flags: S1 1, S2 1, S3 1, S4 3, S5 1.
Dates and matches are facts. Whether a risk is controlled or uncontrolled, and the patch priority, are yours (security-and-privacy-operations-monitoring, this pack).

Read date: 20 October 2026. Rules, owners and recheck dates are yours.
| Id | Unit | Element | Your rule | Result | Blocks release | Owner | Recheck | Status | Build | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| G-01 | HZ-02 trace | Validation case on candidate build | Every hazard has a passing case on the candidate build | fail | yes | Maya Okafor | 27 October 2026 | open | 3.2.1-rc2 | none |
| G-02 | TC-40 | Integration test result | All integration cases pass | fail | not given | owner not named | not given | open | 3.2.1-rc1 | G2, G3, G6 |
| G-03 | Release R-34 | Required stages run | No release skips test or review unless the hotfix exception is recorded the same day | fail | no | Jonas Weber | 1 October 2026 | open | 3.2.0-h1 | G5 |
| G-04 | Sync API component | Failure mode documented | not given | not read (no rule) | not given | owner not named | not given | open | 3.2.1-rc2 | G1 |
| G-05 | Charting library | End of support | No component past end of support at release | fail | no | Maya Okafor | not given | stopped | 3.2.1-rc2 | none |
| G-06 | PR-103 | Validation miss accepted | Accepted misses name the acceptor | pass | not given | Jonas Weber | not given | closed | 3.2.1-rc2 | G4 |

Against your rules: pass 1, fail 4, not measured 0; elements without a rule: 1 (not marked pass or fail). Flags: G1 1, G2 1, G3 1, G4 1, G5 1, G6 1.
No overall verdict and no go or no-go: the gate decision is yours, recorded against the build id with a named acceptor.
```

## A2 short answer (384 words by `delivery_check.py words`)

**Answer.** From 1 July to 30 September 2026 your log holds 6 releases: 4 deployed and kept, 1 rolled back (R-33, which you marked as a clinical defect, caught in production) and 1 failed health check (R-35, caught at release). Two releases skipped required stages: R-32 skipped review under a hotfix recorded the same day; R-34 skipped test and review with no exception recorded at the time, so it is not treated as a hotfix. On the platform, sync saturated the database rather than the component your design named, one scale figure rests on a quota, and two stores have a replica or backup outside the design region. Three SBOM components are past end of support at your read date of 20 October 2026, and one of your listed CVE ids is in the KEV list you supplied.

**Delivery.** Rolled back or failed: 2 of 6 releases (33%), arithmetic on your log; no source sets a rate, so the reading is yours.

**Platform**

| Item | Fact | Source (row) |
|---|---|---|
| Sync requests per minute | Peak 9,100 against design 12,000 (0.76) on 30 September 2026; saturation on database connections, not the sync API pods your design named | your capacity record |
| Clinician sessions | 800 is a staging quota, not a load test | your capacity record |
| Patient readings DB (ePHI) | Backup in us-west, design region us-east | HHS OCR cloud guidance, read 20 October 2026 (EN-034 [WF]) |
| Analytics warehouse | Replica in us-east, design region eu-central; backup not given | your placement table |

Whether a location is permitted is for the owner you name; GDPR transfer rules are not in this skill's sources [GAP].

**SBOM** (fields per FDA premarket cybersecurity guidance, 3 February 2026, EN-054)

| Component | Fact |
|---|---|
| Charting library | Abandoned; end of support 30 June 2025 (477 days before your read date) |
| Cloud sync SDK | "End of life" is not an FDA support value; end of support 31 March 2026 (203 days); CVE-2099-00042 is in your KEV list |
| TLS library | End of support 7 September 2026 (43 days) |

KEV entries should be designed out (EN-052). Patch priority is yours: `security-and-privacy-operations-monitoring` (this pack).

**Recall records.** The saved QRX search holds no recall dated inside your period; a rerun with since 1 July 2026 needs a live check. No result is evidence of safety.

**Calls made.** `delivery_check.py releases`, `capacity`, `residency`, `sbom`; `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` (saved output, retrieved 19 October 2026; connector unavailable 20 October 2026).

Full version available: release table, rules behind the read.

**Record.** Delivery and platform read draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 short answer (369 words by `delivery_check.py words`)

**Answer.** Against your rules for 3.2.1-rc2, read on 20 October 2026: 1 element passed, 4 failed and 1 cannot be read because it has no rule. One failure blocks release by your statement (G-01, HZ-02 has no passing case on the candidate build); 2 of 4 failures have an owner and a recheck date, one has an owner and was stopped, and one has neither. The flag that most limits the review: G-02 (TC-40 failed on rc1) has no owner, no recheck date and no statement on whether it blocks release. No go or no-go is given here.

**Your rules (verbatim)**
1. Every hazard has a passing case on the candidate build.
2. All integration cases pass.
3. No release skips test or review unless the hotfix exception is recorded the same day.
4. No component past end of support at release.
5. Accepted misses name the acceptor.
Sync API "failure mode documented": pass rule not given [GAP]; not marked pass or fail.

**Failed elements**

| Unit | Element | Blocks release (yours) | Owner (yours) | Recheck |
|---|---|---|---|---|
| G-01 HZ-02 trace | Validation case on candidate build | yes | Maya Okafor | 27 October 2026 |
| G-02 TC-40 | Integration test result | not given | owner not named | not given |
| G-03 Release R-34 | Required stages run | no | Jonas Weber | 1 October 2026, earlier than the read date and still open (a fact) |
| G-05 Charting library | End of support | no | Maya Okafor | stopped |

**Limits.** G-06 is closed with no closing evidence recorded. TC-40 ran on rc1, not the candidate (A1 flag T3). HZ-02's only cases are unit-level, and TC-20 expects "works correctly" (A1 flags T2, T5).

**For you to decide.** Go or no-go for 3.2.1-rc2 while G-01 is open and blocking by your rule; whether G-02 blocks release, who owns it and when it is rechecked; the evidence that closes G-06; a rule for the sync API failure-mode element, written before it is scored. Your gate record names the build id and the acceptor; a chat approval is not a record (old task rule, kept as your choice to confirm).

**Calls made.** `delivery_check.py misses --as-of 2026-10-20`; A1 flags from `delivery_check.py trace --candidate 3.2.1-rc2`. No library call.

Full version available: results table, follow-ups, gate record.

**Record.** Release gate review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What this example shows

- Counts and percentages are arithmetic on the person's log; no rate, tier or threshold is supplied.
- An unrecorded skip is reported as such, not as a hotfix; saturation on a component the design did not name is shown.
- SBOM dates are facts against the person's read date; KEV matching uses only the list the person supplied, and vulnerabilities are named by identifier.
- The saved recall search is reported with its own limit (no `since` filter), and the rerun is marked "needs a live check".
- B1 writes the rules back verbatim, reads nothing without a rule, keeps owners and recheck dates as the person set them, and leaves go or no-go with the person.
