# Worked example: A1 integration point map for a computerized behavioral therapy app

Run on 20 October 2026. The library calls are live (`examples/live/connector_calls_2026-10-20.json`); the team, product and log are illustrative (`evals/files/handoff_log_illustrative.csv`), written for this example and not a real company.

**Request (illustrative):** "We are building a prescription CBT app for substance use, modeled on reSET, release 2.0. Design review 3 is the next go or no-go. Map who has to hand what to whom before it. Attendees: Dr Lena Kraus (clinical science), Priya (software lead), Amira (regulatory). Our log is attached."

---

**Answer.** Six integration points feed the work up to the design review 3 go or no-go; 4 rest on sourced anchors, 2 are the team's own. Four have gaps: the journaling-feature impact assessment has no owner, the review input pack has no named receiver, and two late paths are missing. One function that sends work into this review, the wellness feature team, is not on the attendee list you gave; that difference is yours to resolve (PL1).

**Reference product, as stored.** reSet, DEN160018, De Novo granted (raw code DENG) 14 September 2017, class 2, product code PWE, regulation 882.5801 (retrieved 13 October 2026). The record holds no special controls; the work products come from the 882.5801 special controls (TM120 to TM122). Whether your app falls under 882.5801 is a question for `dh-regulatory-and-quality` regulatory-pathway-and-classification.

| # | Work product | Sender | Receiver | Blocked decision | Anchor and rows | Gaps |
|---|---|---|---|---|---|---|
| 1 | Validated therapy model specification | Clinical science (Dr Lena Kraus) | Software (Priya) | SRS freeze | Model validated as implemented (TM120) | none |
| 2 | SRS and SDS traced to the model, V&V | Software (Priya) | Clinical science (Dr Lena Kraus) | Design review 3 | Software shows it implements the model (TM121); review checks verification data (PL4) | none |
| 3 | Reward rule (drug screen result gates reward) | Clinical science | Software (Priya) | Reward module verification protocol | The team's own | late path [GAP] |
| 4 | Impact assessment: journaling feature on the device function | Wellness feature team | Device software (Priya) | Design validation sign-off | Other-function impact documented as design validation (PL25, PL27; FDA guidance, nonbinding, pre-QMSR wording read as ISO 13485 7.3.7, PL12) | owner not named |
| 5 | Summary of clinical testing for physician labeling | Clinical science | Regulatory (Amira) | Labeling freeze | Physician labeling includes it (TM122) | late path [GAP] |
| 6 | Design review 3 input pack | Software (Priya) | Review attendees | Design review 3 | The team's own; waits on 2 and 4 | receiver not named [GAP] |

**Public events, as you asked.** The library holds two FDA recall rows for product code PWE dated 7 June 2021 (reSET and reSET-O, Class II): "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results." The library row states no cause beyond that; FDA's recall page was not read `[GAP]`. Whether it bears on your product is yours to judge; point 3 is on your map because your log shows the rule moving from clinical science to software.

**Stops.** The review outcome, the attendee list and point 4's owner are yours. Design review records go to `dh-regulatory-and-quality` design-controls-and-risk-management.

**Record:** "Integration map draft. AI-assisted." Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made:** `regulatory-dh.search_devices {query: "Pear Therapeutics", jurisdiction: "US"}`; `regulatory-dh.get_authorization {reference: "DEN160018"}`; `regulatory-dh.search_safety_events {product_code: "PWE"}`; `python3 scripts/handoff_log.py check handoff_log_illustrative.csv --as-of 2026-10-20` (output in `examples/live/check_illustrative_2026-10-20.md`).

---

Word count of the answer above, without the calls list and the table's anchor column (the source column): 437, counted at build with a whitespace split.
