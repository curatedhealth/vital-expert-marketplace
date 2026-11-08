Input:    the assumption list, the benchmarks and the documentation of the rate
Atom:     none (a scripted step)
Tool:     python3 scripts/assumptions.py input.json --pretty (fixture: evals/fixtures/good-assumptions-input.json)
Template: none
Output:   nine checks as ok / flag / gap with consequences; the statement; the [CHECK] message
Check:    exit 0; no validation claim; equal to the benchmark is not above. Rules: FV-PROB-ABOVE-BENCHMARK, FV-PEAK-ABOVE-ANALOG
Human:    the valuation reviewer reviews every flag and gap
