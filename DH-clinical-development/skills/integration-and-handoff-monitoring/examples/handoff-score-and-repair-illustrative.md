# Worked example: A2 handoff score and B1 repair list

Run on 20 October 2026. The log is illustrative (`evals/files/handoff_log_illustrative.csv`), written for this example and not a real company. The safety-event call is live (`examples/live/connector_calls_2026-10-20.json`). Script outputs: `examples/live/score_illustrative_2026-09-01_2026-10-15.md` and `examples/live/repair_illustrative_2026-10-20.md`.

**Request (illustrative):** "Score our handoffs for 1 September to 15 October 2026 with the rule we agreed (received by the named receiver, not sent). Then tell me what is still owed. Also, the reSET recall in 2021 was about a reward rule like our H3; does that tell us anything?"

---

## A2 output (short mode)

**Answer.** Under your rule (received by the named receiver, not a message sent; confirmed by you), 10 handoffs were scored (9 due in the period, 1 with no due date): 2 received, 2 late, 3 open, 3 not measurable. All 3 open items and both late items are ones you marked critical to quality (CV29), all in your "clinical evidence" category. On time over measurable handoffs: 2 of 7, with the 3 not measurable listed below rather than counted.

| Work product | Category | CTQ | Status | Fact |
|---|---|---|---|---|
| Therapy model specification v2 | clinical evidence | yes | late | received 8 September, due 1 September |
| Clinical study report final | clinical evidence | yes | late | received 2 October, due 30 September |
| SRS and SDS trace to the therapy model | clinical evidence | yes | open | not received by 15 October |
| Impact assessment: journaling feature | clinical evidence | yes | open | not received by 15 October |
| Physician labeling: summary of clinical testing | clinical evidence | yes | open | not received by 15 October |

**Not measurable.** Reward rule (H3): received 21 September by Tom (QA), not by the named receiver Priya; under your rule receipt is not shown `[GAP]`. Deployment data dictionary (H8): no due date `[GAP]`; what is its due date? Design review 3 input pack (H9): receiver not named `[GAP]`; who receives it?

**The reSET recall.** The library holds two FDA recall rows dated 7 June 2021 (reSET and reSET-O, Class II): "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results." The library row states no cause beyond that; FDA's recall page may hold a root-cause category not read here `[GAP]`. Whether it bears on your H3 is yours to judge. What your own log shows is that H3's receipt is not recorded by its named receiver.

**Record:** "Handoff score, 1 September to 15 October 2026, draft. AI-assisted." Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made:** `python3 scripts/handoff_log.py score handoff_log_illustrative.csv --from 2026-09-01 --to 2026-10-15`; `regulatory-dh.search_safety_events {product_code: "PWE", limit: 10}`.

---

## B1 output (short mode)

**Answer.** Five handoffs are still owed as of 20 October 2026; the first in dependency order is the SRS and SDS trace, and design review 3 waits on three of them.

| Step | Work product | Owner owes | Blocked decision | Waits on | Look again on |
|---|---|---|---|---|---|
| 1 | SRS and SDS trace | Priya (software lead) | Design review 3 go or no-go | none | 27 October 2026 |
| 2 | Journaling impact assessment | owner not named | Design validation sign-off | none | [GAP] |
| 3 | Physician labeling summary | Dr Lena Kraus | Labeling freeze | none | 3 November 2026 |
| 4 | Deployment data dictionary | Priya (software lead) | Pilot site go-live plan | none | [GAP] |
| 5 | Design review 3 input pack | Priya (software lead) | Design review 3 go or no-go | 1, 2 | 27 October 2026 |

Design review 3 stays blocked until steps 1, 2 and 5 are received by their named receivers; holding the meeting does not unblock it. Who owes step 2, who receives step 5 (receiver not named `[GAP]`), and when to look again at steps 2 and 4 are yours to set.

**Record:** "Alignment repair list draft for owner not named. AI-assisted." Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made:** `python3 scripts/handoff_log.py repair handoff_log_illustrative.csv --as-of 2026-10-20`.
