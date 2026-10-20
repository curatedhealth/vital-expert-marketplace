# Worked example: A2 threat model and SBOM check, then B1 vulnerability response (illustrative)

**Inputs.** Illustrative files written for this skill on 20 October 2026, labeled illustrative in their first line: `sample-data/threats_illustrative.csv`, `sample-data/sbom_illustrative.csv`, `sample-data/kev_illustrative.csv` (a stand-in for the person's own export of the CISA KEV catalog), `sample-data/data_classes_illustrative.csv`. Component names and vulnerability ids are placeholders, not real software or real CVEs. The person's read date: 20 October 2026. The person's support horizon: 31 December 2030. Design version: 2.3. The person's request: "Here is our threat register and SBOM for the glucose companion app. Where are we open, and what do we do about the KEV hit in our TLS library?" The person named Dana Ruiz as the security risk acceptor and gave no other owner.

**Calls.** No library call was needed for A2. The connector was disconnected during this build; the B1 authorization step is shown from a saved output (`live/get_authorization_K191716.json`, retrieved 19 October 2026) to show the call's shape only.

## Script runs

```
python3 scripts/secdesign_check.py threats --file examples/sample-data/threats_illustrative.csv
Covered 1, accepted 2, open 2.
  TH-02 phone app to cloud API: open (T2)
  TH-04 cloud admin console: accepted, T3 acceptance has no named person; T4 no reopen condition
  TH-05 update server to app: open (T2); T5 design version not given
Note: rows cite 2 design versions (2.2, 2.3)

python3 scripts/secdesign_check.py sbom --file examples/sample-data/sbom_illustrative.csv --as-of 2026-10-20 --kev examples/sample-data/kev_illustrative.csv --support-horizon 2030-12-31
  example-tls-lib 3.0.2: S5 end of support 7 September 2027 before your horizon; S7 ILL-VULN-002 in your KEV export
  example-ble-stack 5.1: S6 "no longer maintained"; S4 end of support 30 June 2026 on or before the read date
  example-json-parser 2.9: S1 manufacturer not given; S3 end-of-support date not given
  example-mobile-os 14: S5 end of support 31 December 2026 before your horizon
  example-chart-widget 1.4: S1 release date not given; S6 "abandoned"; S4 end of support 1 May 2025; S7 ILL-VULN-009 in your KEV export
Flag counts: S1 2, S3 1, S4 2, S5 2, S6 2, S7 2
```

## The answer (short mode, A2 then B1)

**Answer.** Your register holds five threats on five hops: one covered, two accepted, two open (phone app to cloud API, and update server to app). Two components were past end of support on 20 October 2026 (example-ble-stack, example-chart-widget), and two carry ids that appear in your KEV export (ILL-VULN-002 in example-tls-lib, ILL-VULN-009 in example-chart-widget). The model is not dated to one design version (rows cite 2.2 and 2.3).

**Open and accepted threats**

| Id | Hop | Status | What is missing | Rows |
|---|---|---|---|---|
| TH-02 | phone app to cloud API | open | a control (FDA category) or a named acceptance | FDA premarket cybersecurity guidance, 3 February 2026 (EN-051, EN-057) |
| TH-05 | update server to app | open | a control or acceptance; design version | FDA premarket guidance (EN-050 supply chain and update; EN-057) |
| TH-04 | cloud admin console | accepted by "team" | a named acceptor and a reopen condition | old task DH-04.02.2.1.3 |
| TH-03 | cloud API to EHR | accepted by Dana Ruiz | none (reopen condition stated) | old task DH-04.02.2.1.3 |

**SBOM facts.** Level of support and end-of-support date per component are what FDA asks the SBOM to carry (FDA premarket cybersecurity guidance, 3 February 2026, EN-054); KEV vulnerabilities should be designed out of the device (EN-052), and CISA says to use KEV as an input to prioritization (CISA KEV page, read 20 October 2026, EN-080 [WF]). Your 31 December 2030 horizon is yours; three components end support before it.

**B1, ILL-VULN-002 in example-tls-lib 3.0.2.** Reachable: not given; ask. Options: patch (fixing version not given), mitigate (control not given), or accept (acceptor and expiry yours). If the product is a device, section 524B asks for out-of-cycle patches as soon as possible for critical vulnerabilities that could cause uncontrolled risks (21 USC 360n-2, EN-044). FDA's 2016 postmarket guidance asks, as an enforcement policy and not a statutory deadline, for customer communication within 30 days and a distributed fix within 60 days where risk is uncontrolled (FDA postmarket cybersecurity guidance, 28 December 2016, EN-066, EN-067). Your classification: not given. Whether the risk is controlled and whether anything is reportable route to `dh-regulatory-and-quality` audit-capa-and-complaints.

**For you to decide:** controls or named acceptances for TH-02 and TH-05; the acceptor for TH-04; the response and classification for both KEV hits; the plan for the two components past end of support.

**Calls made:** none for A2; connector unavailable during this build. Full version available on request (FDA views mapping, data-class flags, testing evidence).

Threat model draft for the owner. AI-assisted. Clears it: owner not named (you named Dana Ruiz as risk acceptor, not as the person who clears this draft). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Authorization call shape (saved output, not part of the answer above)

`regulatory-dh.get_authorization {reference: "K191716"}` returned Somryst, FDA 510(k), decision date 23 March 2020, product code QVO (library, retrieved 19 October 2026). For a product the person names, the decision date sits beside the 524B effective date, 90 days after 29 December 2022 (29 March 2023, computed from EN-046), for the regulatory owner. The record says nothing about the product's security and is not linked to the illustrative files.

## Word count

`python3 scripts/secdesign_check.py words` on the answer section above: 346 words, within the short-mode cap (checked 20 October 2026).
