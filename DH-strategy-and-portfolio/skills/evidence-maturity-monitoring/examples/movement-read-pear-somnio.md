# Worked example: A2 evidence movement read (real earlier run, illustrative later run)

**Request (illustrative investor):** "Attached are our evidence maturity runs for K191716 and somnio from 19 October 2026 and 1 December 2026. What moved, and is it real? Owner: Lena Park, investment director."

Data: the earlier run is real, saved live on 19 October 2026 (`examples/live/evidence_maturity_K191716_somnio_2026-10-19.json`, read 20 October 2026). The later run is ILLUSTRATIVE, written by the builder to exercise the script (`examples/sample-data/evidence_maturity_later_ILLUSTRATIVE.json`); it states nothing about Pear Therapeutics or mementor. Diff: `python3 scripts/maturity_diff.py examples/live/evidence_maturity_K191716_somnio_2026-10-19.json examples/sample-data/evidence_maturity_later_ILLUSTRATIVE.json` (output in `examples/sample-data/diff_K191716_somnio_ILLUSTRATIVE.md`).

---

**Answer.** K191716 (resolves to Pear Therapeutics, Inc.) moved from 67 to 78 on an input change: one product-linked study now has results posted in the library (0 to 1). The record is not yet read, so it is not yet new evidence. somnio (mementor DE GmbH) moved from 33 to 40 with no change in evidence inputs: the rubric and the assessable maximum changed, so the two scores are not a trend.

**Differences**

| Company | 19 October to 1 December 2026 | Change | Class | Record behind it |
|---|---|---|---|---|
| K191716 | 67 (60 of 90) to 78 (70 of 90) | Clinical evidence 20 to 30; results posted 0 to 1 | INPUT | Record not yet read |
| somnio | 33 (30 of 90) to 40 (40 of 100) | Maximum 90 to 100; reimbursement added as a component; rubric v2 | METHOD | None: the convention changed |

**What would confirm the K191716 change.** The registry entry with results posted for a product-linked study. US results are due no later than 1 year after primary completion (CV145), later for certified unapproved products (CV146). The library's change log can date the event, but it began on 12 October 2026 and filters on event dates, so an older posting may have no entry.

**somnio.** The earlier saved output is trimmed: it lacks the rubric version and the excluded list, so those were not compared. Save full responses at each run.

**Flags and status.** Carried forward from the 19 October 2026 somnio run, classed RESOLUTION until you validate it: "2 filing names normalize to this company and are combined; the combination is a proposal until a person validates it". Neither run shows company status. Pear, as read on 20 October 2026 (SEC rows [WF]): chapter 11 (Pear 8-K, 7 April 2023, SP-156); last filing Form 25-NSE, 2 May 2023, not dissolution (SP-155, DL-144); Somryst (K191716) is now listed with FDA by Nox Medical (SP-167). mementor DE GmbH: [GAP]: not read; open the German insolvency notices and register extract (DL-165, DL-168).

**Perimeter.** The later run lists more clinicaltrials records (128 to 140) and drops three "not loaded" lines; these are coverage changes, not evidence.

**Measures.** None set in this request `[GAP]`; B1 needs your measures to mark a trigger. The framework level stays as you confirmed it; no new level is proposed from an unread record.

**Gaps and stops.** A grade for the new results goes to `dh-clinical-development` literature-and-real-world-evidence-review. No value effect is stated.

Full version on request.

**Calls made:** none in this run. Earlier run: `diligence-dh.get_evidence_maturity {company: "K191716"}` and `{company: "somnio"}`, saved 19 October 2026. Script: `scripts/maturity_diff.py` as above. Research rows read 20 October 2026.

**Record.** Evidence movement read draft for Lena Park. AI-assisted. Clears it: Lena Park, investment director. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (between the rules, without the calls list and the tables' source column), counted with `python3 scripts/maturity_diff.py --count` on 20 October 2026 after the status revision: 433 (including tables and the record line), under 450.
