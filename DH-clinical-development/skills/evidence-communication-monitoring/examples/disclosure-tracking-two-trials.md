# Worked example: A1 disclosure tracking, short mode (public registry records, 19 October 2026)

**Request (test):** "Check registration and results status for NCT05067569 and NCT05561790. Results will go to an ICMJE journal. Treat first consent as the registry start date. Neither is a US applicable clinical trial and neither runs under the EU CTR. Registry owner: Maria Holm."

The regime answers and the first-consent assumption are test inputs written for this example, not facts about these trials.

**Calls and inputs:** `literature.find_trial {nct_id: "NCT05067569"}` (status COMPLETED, phase NA, sponsor Woolcock Institute of Medical Research; no dates returned). Dates from the public ClinicalTrials.gov records (`examples/live/ctgov_registry_snapshot.json`). Script: `python3 scripts/disclosure_clock.py examples/live/trials_registry_records_with_test_answers.csv --as-of 2026-10-19` (output: `examples/live/disclosure_clock_run_2026-10-19.md`).

---

**Answer.** As of 19 October 2026, on the test answers: no results clock applies to either trial (not US applicable clinical trials, not under the EU CTR, as stated by the person). One ICMJE registration test is missed: NCT05561790 was first submitted to the registry 22 days after the date given as first consent, and ICMJE journals may not consider such a trial (CV132). NCT05067569 was submitted before its first-consent date.

| Trial | Clock | Rule | Basis date (source field) | Due or test | Status |
|---|---|---|---|---|---|
| NCT05067569 | ICMJE registration | CV132 | First consent 1 October 2022 (registry start date, as instructed); registration submitted 8 September 2021 (first submitted) | At or before first consent | Met |
| NCT05561790 | ICMJE registration | CV132 | First consent 6 September 2022 (registry start date, as instructed); registration submitted 28 September 2022 (first submitted) | At or before first consent | Missed by 22 days |
| Both | US results | CV145 | Person: not an applicable clinical trial | None | No US clock |
| Both | EU results | CV152 | Person: not under the EU CTR | None | No EU clock |

**Not computed.**
- WHO joint statement: signatory status not given `[GAP]` (CV140).
- Neither registry record shows a results posting date; whether results were posted elsewhere, or a paper published, was not given `[GAP]`. `find_trial` listed no linked publication for NCT05067569; that is a limit of the library, not proof there is none.
- The registry start date was used as first consent on instruction; if the first participant consented on a different date, the ICMJE test changes.

**What the person decides.** Whether the ICMJE result matters for the planned journal (the journal decides on consideration); the regime answers. Registry actions stop for Maria Holm.

**Record.** AI-assisted draft. Clears it: Maria Holm (registry owner, as named; fictional test name). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (without the calls list and the source column): checked by script (whitespace tokens), 290 words.
