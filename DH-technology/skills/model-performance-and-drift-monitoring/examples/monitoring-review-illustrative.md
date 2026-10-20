# Worked run: model register, drift read and review (ILLUSTRATIVE, with one saved library read)

ILLUSTRATIVE. The person's files in `sample-data/` are invented (a register of four model versions with a pass rule written 1 June 2026, a quarterly prediction log for DET-1 with thresholds written 15 December 2025, a sleep-program decision log and rule table). No real patient, site or model. Script outputs are saved beside the inputs (`records_output.txt`, `drift_output.txt`, `adaptation_output.txt`). The public-records step uses saved live library output for a real product (`examples/live/`, called 19 October 2026); the connector was not connected when this example was written.

Request: "Read date 20 October 2026. Check our model register against our rule, read DET-1 for Q3 against Q1 and the sleep engine's September log, then help us assign the misses."

---

## A1 answer (short mode)

**Answer.** Against your rule of 1 June 2026, two of four versions pass and two fail; one of the failures, NOSHOW-3 1.4.0, is in production and fails all seven elements. DET-1 2.1.0 passes the record rule but its drift watch fired on 31 August 2026 with no action recorded, so it stays open.

**Records (`drift_check.py records`).**

| Model | Version | In production | Against your rule |
|---|---|---|---|
| DET-1 | 2.1.0 | yes | pass; W3 watch fired 31 August 2026, no action recorded |
| DET-1 | 2.0.3 | no | fail: approver, metric named before the run (named 20 September 2024, run 12 September 2024), test set independence ("none") |
| NOSHOW-3 | 1.4.0 | yes | fail: intended use ("clinical decision support", no decision named), decision, test set, metric, run id, approver, watch |
| SLEEP-ENG | 0.9.2 | yes | pass; W4 watch fired 14 September 2026, rolled back 15 September 2026 |

A production model with no run id is a fail under the old task DH-01.04.2.2.1; test independence is what the FDA draft guidance of January 2025 asks manufacturers to describe (draft, DA-39 to DA-41).

**Open fired watches.** DET-1 2.1.0: signal monthly O/E and AUROC; your threshold O/E outside 0.8 to 1.25; action specified "stop the decision and review"; watch owner on your register Dr. Amara Okafor. Not closed.

**Calls made.** None (connector not connected). `drift_check.py records`, 20 October 2026. Full version on request.

**Record.** Record check draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## A2 answer (short mode)

**Answer.** Between Q1 and Q3 2026, DET-1's event rate rose from 0.213 to 0.283 while O/E (1.02 to 1.05) and AUROC (0.736 to 0.795) stayed inside your thresholds; lactate crossed two of your limits (standardized mean difference 0.43 against 0.2; missing share 0.140 against 0.1), and 75 Q3 outcomes are still pending. The sleep engine delivered "double prompt", outside its allowed options, 9 times on 14 and 15 September 2026.

**Performance by period (`drift_check.py drift`; thresholds written 15 December 2025).**

| Period | Outcomes known | Event rate | O/E | AUROC | Slope | Flags |
|---|---|---|---|---|---|---|
| 2026-Q1 | 520 | 0.213 | 1.02 | 0.736 | 0.83 | none |
| 2026-Q2 | 520 | 0.190 | 1.11 | 0.763 | 0.92 | none |
| 2026-Q3 | 445 of 520 | 0.283 | 1.05 | 0.795 | 1.15 | none |

Recalibration fits calibration drift with event-rate shift and stable discrimination (Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-92); whether that pattern applies is your reading. The cause of the lactate change is not in the log; acquisition devices are a common cause of input drift (Sahiner et al. 2023, DOI 10.1259/bjr.20220878, DA-88).

**Engine (`drift_check.py adaptation`).** Missing tailoring data in 176 decisions; 41 delivered other than your rule ("no prompt"). Engagement by week: 0.672 (week 36) to 0.406 (week 39); week 40 holds 17 decisions. Per-option rates are descriptive: the rule chose the option (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM90).

**Calls made.** None. `drift_check.py drift` and `adaptation`, 20 October 2026. Full version on request.

**Record.** Monitoring read draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

## A2 public-records step on a named product (saved live library output)

Request: "We deploy Aidoc's BriefCase-Triage. Any recalls or reports?"

- `regulatory-dh.search_devices {query: "Aidoc", jurisdiction: "all", limit: 10}` (library, retrieved 19 October 2026): stored manufacturer "Aidoc Medical , Ltd."; for example K261317, BriefCase-Triage, 510(k) Substantially Equivalent, 14 May 2026, product code QAS.
- `regulatory-dh.search_safety_events {manufacturer: "Aidoc", limit: 10}` (19 October 2026): no recall records returned. MAUDE counts by product code: QAS 0, QFM 0, QIH 10 (2 in 2024, 5 in 2025, 3 in 2026); counts are reports, not confirmed events, and carry no manufacturer, so they are not attributed to Aidoc. No result is evidence of safety; a recall filed under another entity name would not match. Since date: not given; asked.

---

## B1 answer (short mode)

**Answer.** Four misses by your rules and thresholds; one has an owner the register names, none has an action you chose, and none has a recheck date. The sleep engine's off-rule decisions are listed as facts but not marked failed: no pass rule for personalization rules was given. The open DET-1 watch most limits the review.

**Misses.**

| Miss | Fact | Owner | Action | Recheck |
|---|---|---|---|---|
| DET-1 2.1.0 watch fired 31 August 2026 | no action recorded | Dr. Amara Okafor (watch owner on your register) | not given (the watch specifies "stop the decision and review") | not given |
| DET-1 lactate | SMD 0.43, missing 0.140 against your limits | owner not named | not given | not given |
| NOSHOW-3 1.4.0 | fails all seven elements; in production | owner not named | not given; whether it may keep influencing a decision is yours (old task DH-01.04.3.2.3) | not given |
| DET-1 2.0.3 | fails three elements; not in production | owner not named | not given | not given |

SLEEP-ENG DP1: 9 decisions outside allowed options and 41 missing-data decisions off-rule; pass rule not given `[GAP]` (old task DH-01.06.1.2.2: write the rule, with the element that blocks release, before scoring). Whether the lactate limits count as the DET-1 watch firing is your call: the watch is defined on O/E and AUROC, the limits on inputs. A retrain on an authorized device routes to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control; reportability to `dh-regulatory-and-quality` audit-capa-and-complaints.

**Calls made.** None. Full version on request.

**Record.** Performance review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
