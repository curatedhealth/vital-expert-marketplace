# Worked example: A2 vulnerability read and B1 review (illustrative)

**Inputs.** Illustrative files written for this skill on 20 October 2026, labeled illustrative in their first line: `sample-data/vulns_illustrative.csv` and `sample-data/controls_illustrative.csv`. Component names and vulnerability ids are placeholders, not real software or real CVEs. The person's read date: 20 October 2026. The person's windows: critical 30 days, high 90 days. The person's pass rule for closures: "patched means the fixed version is deployed; accepted means a named acceptor and an unexpired date". The person's request: "Where is our backlog against our windows, what did we really close, and who owns the misses? Any recalls in insulin apps we should know about?" The person named Priya N. as owner of encryption controls and gave no other owner or recheck date.

**Calls.** The connector was disconnected during this build; the recall step is shown from a saved output, `live/safety_events_insulin_us.json` (`regulatory-dh.search_safety_events {product: "insulin", jurisdiction: "US", since: "2025-01-01", limit: 10}`, retrieved 19 October 2026, trimmed by the build that saved it).

## Script run

```
python3 scripts/secops_check.py vulns --file examples/sample-data/vulns_illustrative.csv --as-of 2026-10-20 --windows "critical=30,high=90"
Open and reachable: 3
- V-02 ILL-VULN-011 cloud admin console 2.3, high, 111 days since 1 July 2026: V2 past your high window by 21; V5 under review with no action
- V-01 ILL-VULN-002 example-tls-lib 3.0.2, critical, 61 days since 20 August 2026: V2 past your critical window by 31; V4 KEV in your file
- V-08 ILL-INT-008 cloud admin console 2.2, critical, 22 days since 28 September 2026: inside your critical window
Open, reachability not stated: V-03 (example-ble-stack). Stated not reachable: 1.
Closed: V-05 patched, no deployed version (evidence: merged pull request 412), V7; V-06 deployed 2.3 on 20 May 2026; V-07 acceptance expired 30 September 2026, V8
Class with the most reachable items: dependency (3); exposed admin 2
```

## The answer (short mode)

**Answer.** Three reachable vulnerabilities are open; two are past your windows (V-01 critical, 61 days against 30; V-02 high, 111 days against 90). V-03 is not aged because its reachability is not stated. Against your closure rule, two of three closed items miss: V-05 has no deployed version, and V-07's acceptance expired on 30 September 2026. Dependency is the class with the most reachable items (3).

**Misses against your rules**

| Unit | What missed | Fact behind it | Owner | Recheck date |
|---|---|---|---|---|
| V-01 | critical window | 61 days since intake; KEV in your file, catalog entry not checked | owner not named | not given |
| V-02 | high window | 111 days, still "under review" with no action | owner not named | not given |
| V-05 | closure evidence | merged pull request 412, no deployed version: proposed reopen, your call | owner not named | not given |
| V-07 | closure evidence | acceptance by Dana Ruiz expired 30 September 2026 | owner not named | not given |

**Limits.** V-03 cannot be aged until reachability is stated. For V-01, KEV is an input to prioritization (CISA KEV page, read 20 October 2026, EN-080 [WF]); the catalog entry itself is the record to check (EN-081 [WF]). Your windows are yours; FDA's 30 and 60 days apply only to uncontrolled risk as a 2016 enforcement policy, not statute (FDA postmarket cybersecurity guidance, 28 December 2016, EN-066, EN-067).

**Proposed engineering change** for the dependency class (yours to accept): a dependency update step in each release, so components are refreshed before they reach the backlog; the SSDF names preventing recurrence (NIST SP 800-218, February 2022, EN-040).

**Recalls in insulin apps.** Three full records in the saved read: Insulet Corporation, Omnipod 5 iOS App, Class II, 23 May 2025 (decimal separator not recognized); Tandem Diabetes Care, t:slim X2 with mobile app, Class II, 3 July 2025 (pairing and display defect with right-to-left languages); Tandem Diabetes Care, Tandem Mobi, Class I, 6 October 2025 (false vibration motor failure). None of the three summaries names a security cause; a missing record is a coverage limit, not evidence that none exists.

**For you to decide:** owners and recheck dates for all four misses; renew or end V-07's acceptance; reopen V-05; reachability for V-03.

**Calls made:** `regulatory-dh.search_safety_events` (saved output, retrieved 19 October 2026); connector unavailable during this build. Full version available on request (control matrix read, residual-risk notes, all classes).

Security and privacy review draft for the owner. AI-assisted. Clears it: owner not named (you named Priya N. for encryption controls only). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Word count

`python3 scripts/secops_check.py words` on the answer section above: 358 words, within the short-mode cap (checked 20 October 2026).
