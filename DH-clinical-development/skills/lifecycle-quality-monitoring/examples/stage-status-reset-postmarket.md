# Worked example: A2 stage status read with post-market inputs (illustrative log, live register data, 20 October 2026)

**Request (illustrative product, real register records):** "Here is our gate log for our substance-use CBT app with contingency management (`examples/live/gate_log_illustrative.csv`, illustrative). Read stage status as of today. We will sit in the same FDA product code as reSET (PWE); what does the register show after market that our Design verification stage should take in? Owner: Ana Ruiz."

---

**Answer.** As of 20 October 2026, Feasibility (open 251 days) and Design verification (open 97 days) both hold missing or in-progress items, and Design verification started on 15 July 2026 while two Feasibility items were still open (flag F4). The register holds a Class II recall dated 7 June 2021 in product code PWE, quoted below as the record states it; whether it bears on your Design verification stage is your call.

**Stage table (script output)**

| Stage | Owed | Accepted | Missing | In progress | Days open | Flags |
|---|---|---|---|---|---|---|
| Concept | 2 | 2 | 0 | 0 | 36 (closed) | F1 |
| Feasibility | 3 | 1 | 1 | 1 | 251 | F3, F4, F5 |
| Design verification | 3 | 2 | 1 | 0 | 97 | F2, F5 |

**Flags that matter**

- Concept, program theory: accepted with no evidence reference (F1). A status with nothing behind it does not show the record (PL9).
- Feasibility, study report against criteria and usability formative findings: next stage started while open (F4). Repeating a phase is preferable to automatic progression while uncertainties remain (TM3, DOI 10.1136/bmj.n2061). Usability findings: owner not named (F3).
- Design verification, system test report: accepted with no named decider or date (F2). Unresolved anomalies list: missing, no reread date (F5); the list is a named submission element (PL20).

**Post-market inputs, product code PWE (recall records retrieved 16 October 2026; MAUDE counts retrieved 13 October 2026)**

| Date | Event | Record summary (as stated) | Stage you named |
|---|---|---|---|
| 7 June 2021 | FDA recall, Class II, reSET and reSET-O mobile apps | "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results." | Design verification, as named in your request; whether it reopens is your call. Context if you change the software: a software change is a design change (CH9) |

MAUDE, PWE: 2 reports (2022: 1, 2025: 1); reports, not confirmed events. The record does not state the recall's root cause or fix; none is inferred. Whether a change in your product needs a submission: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. Recall follow-up records: `dh-regulatory-and-quality` audit-capa-and-complaints.

**Gaps.** No lifecycle measures set yet (A1); counts are not judged. Reread dates not given for two items; asked.

**Record.** Stage status read draft for Ana Ruiz. AI-assisted. Clears it: Ana Ruiz. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made (live, counted):** `regulatory-dh.get_authorization {reference: "DEN160018"}`; `regulatory-dh.find_predicates {product_code: "PWE"}`; `regulatory-dh.search_safety_events {product_code: "PWE"}`. Saved in `examples/live/regulatory_records_2026-10-20.json`. Script: `python3 scripts/gate_log_check.py examples/live/gate_log_illustrative.csv --as-of 2026-10-20 --events examples/live/regulatory_records_2026-10-20.json --product reset` (output in `examples/live/gate_log_with_pwe_events.md`). The person's product name was not sent to the library.
