# Benchmark tables

bio-2011-2020.json holds the figures transcribed from the BIO/Informa/QLS report (B1). Each stratum records
n per transition, probability of success per transition, durations where reported, the figure name and the PDF page.

- Use ONE stratum per estimate. The source has no combined cells (for example rare disease within oncology); combine by adjustment, with a reason.
- Rare-disease and chronic-disease strata are non-oncology only (Fig 8b). Biomarker strata are all indications (Fig 11).
- Strata with no durations (rare, chronic, biomarker, modality) fall back to all-indications durations in timeline_range.py and say so.
- Gene therapy has n of 2 on the last transition: treat as a flag, not a benchmark.
- Re-check any figure against the PDF before release; the transcription was checked once on 6 Nov 2026 by the test `test_benchmark_table_matches_report_figures` for two rows only.
- The BIO report is an industry report, not peer-reviewed. Wong 2019 (peer-reviewed) uses different data and definitions (13.8% against 7.9%): report either, never mix them. Wong notes biomarker and orphan results outside oncology rest on small samples (VP-B-064, VP-B-066).
- review-timing.json holds US context (FDA PDUFA report FY 2025: goals, first-cycle percentages) and EU context (EMA annual report 2025: averages in days) as separate blocks. They are different statistics and are never combined or compared.
