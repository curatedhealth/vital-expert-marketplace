# Worked run: A1 decentralized trial setup (short mode)

Run on 19 October 2026 with live library calls. The trial described in the request is invented for this example; the comparable trials and their registration are live connector output (`examples/live/`).

## Request

"We are a DTx company running a 12-week randomized trial of our app for chronic low back pain, sites in Germany and the US. We want consent by video, a wrist sensor for daily steps as the primary endpoint, and participants choosing whether week-6 and week-12 assessments happen at site or at home. A local physio would do the week-6 range-of-motion test. What must be in place?"

## Calls made

| Call | Arguments | What came back |
|---|---|---|
| `literature.search_literature` | `{query: "decentralized randomized trial remote enrollment wearable digital health technology", limit: 5, filters: {date_from: "2022-01-01"}}` | 5 records of 15 merged; `trial_ids` empty on all, including an RCT; a scoping review labeled `systematic_review` |
| `literature.find_trial` | `{record: ACTIV-6 participant-experience paper, PMID 40599176}` | No linked registration |
| `literature.find_trial` | `{nct_id: "NCT04885530"}` | ACTIV-6 registration: COMPLETED, PHASE3; five linked publications, three preprints; no dates |
| `literature.find_trial` | `{record: ACTIV-6 JAMA Internal Medicine paper, PMID 40658388}` | Registration NCT04885530 found via `pubmed_secondary_id` |

## Answer (short mode)

**Framework.** If the app is investigated as a device, ICH E6(R3) does not name devices (CV4); ISO 14155 and EU MDR investigation rules are not sourced here `[GAP]`. The FDA DCT guidance (final, September 2024, CV65) and DHT guidance (final, December 2023, CV42) apply as recommendations; the EU paper on decentralized elements (Version 02, not legally binding, CV95) is context for the German sites.

**Two items to settle before the protocol draft.**

1. *Participant choice on the primary endpoint visits.* FDA says free choice between site and remote assessment may bias results (sicker participants may prefer remote visits) and the protocol must say which visits are site, remote or choice (CV67). Your plan leaves week 6 and week 12 to choice. Is that intended? The decision is yours.
2. *The physio's range-of-motion test.* Local providers may do only tasks within their normal practice that need no detailed protocol knowledge (CV70). If the test follows a protocol-specific method, the physio is trial personnel and needs trial training. Owner not named: who decides?

**What the plan must state** (draft for the owner, not protocol text):

- Video consent: identity confirmed (CV16); for Germany, real-time audio and video and a protected downloadable copy of the signed form (CV100, CV101); who can access sensor data, including under the vendor's terms (CV61).
- Wrist sensor: verification, validation in people with low back pain, and usability with the trial population (CV46, CV48, CV51); same method in both arms (CV58). Detail in A2.
- Monitoring plan covering home activities (CV17), with centralized checks for missing and outlying data (CV71); contingency if the sensor fails (CV99).
- EU application: decentralized elements summarized in the cover letter (CV97). US: if this is an applicable device clinical trial (CV142), registration within 21 days after first enrollment (CV141); ICMJE asks for registration before first consent (CV132).

**Comparable trial.** ACTIV-6 (NCT04885530) is a completed phase 3 decentralized trial with a published participant-experience paper (DOI 10.1017/cts.2025.69). The library links the registration from the JAMA paper, not from that paper. It is context, not a template.

**Gaps.** ISO 14155; EU national provisions appendix content; registration dates (the library returns none).

**Record.** Uncleared draft. Visit choices and owners are yours.

(Word count of the answer, without the calls table: about 380.)
