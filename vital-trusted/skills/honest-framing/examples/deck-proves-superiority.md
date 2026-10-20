# Worked example: a sales-training deck that says a trial "proves" superiority

Invented case for teaching. "Velostra", "Corvane", "KELNA-1" and "Example Pharma" are
fictional; no real product, trial, company or person.

## Request

"Tighten these five slides for the sales-force training next month, then they go to the
agency to build the doctor-facing version. Keep the punch."

## Context card (from intake, short form)

Reader: sales force now, doctors later (agency build). Use: promotional. Stakes: leaving
the company. Market: not stated. Next process: promotional review.

## Material supplied (abstract and disclosures of the KELNA-1 paper)

> KELNA-1 was a randomized, open-label, active-controlled phase 3 trial in 640 adults
> with moderate condition Z (320 per arm). Primary endpoint: proportion with at least
> one flare by week 24: 22% with Velostra versus 28% with Corvane (relative risk 0.79,
> 95% CI 0.64 to 0.97; p = 0.03). Secondary endpoint: at least 75% improvement at
> week 16: 88% versus 84% (difference 4 percentage points, 95% CI −1 to 9; not
> statistically significant). Injection-site reactions: 3% versus 1%. Limitations named
> by the authors: open-label design; 24-week follow-up.
> Funding: Example Pharma, the maker of Velostra. Example Pharma designed the study and
> analyzed the data. Three of eight authors are Example Pharma employees.

## Draft slides

1. "KELNA-1 proves Velostra is superior to Corvane."
2. "Velostra cuts flares by 21%, a dramatic improvement."
3. "Independent head-to-head data."
4. Chart: bar chart of 75% improvement at week 16, y-axis from 80% to 90%, Velostra 88%,
   Corvane 84%, no n, no title.
5. "Injection-site reactions: only 3%."

## Repaired slides

1. "In KELNA-1, an open-label trial of 640 adults, fewer patients had a flare by week 24
   with Velostra than with Corvane."
2. "Flares by week 24: 22% with Velostra, 28% with Corvane: 6 percentage points fewer, a
   relative reduction of about 21% (relative risk 0.79, 95% CI 0.64 to 0.97). Follow-up
   was 24 weeks."
3. "KELNA-1 was funded and analyzed by Example Pharma, the maker of Velostra."
4. Chart: see the chart description below.
5. "Injection-site reactions: 3% with Velostra, 1% with Corvane."

## Framing note (as the person sees it)

What I changed and why (draft, not yet reviewed)

Based on: KELNA-1 abstract and disclosures (supplied)

Changed
1. "proves Velostra is superior" → the result of the one trial, with its design. One
   open-label trial cannot prove superiority; it shows fewer flares in this trial.
   Whether a superiority claim can be made at all is a question for your promotional
   review.
2. "cuts flares by 21%, a dramatic improvement" → both rates, the 6-point difference,
   the relative figure and its range. 21% on its own reads larger than 6 in 100;
   "dramatic" is gone, the numbers carry it.
3. "Independent head-to-head data" → who funded and analyzed the trial. The paper names
   Example Pharma as funder and analyst, and three authors are its employees, so
   "independent" would mislead.
4. Slide 5: "only 3%" → both arms. "Only" makes the reaction rate look unimportant, and
   the Corvane figure (1%) shows it was higher with Velostra.
5. Added the follow-up (24 weeks) and the open-label design, the two limitations the
   authors name, on the slides that use the result.

Charts
1. Slide 4, bar chart of 75% improvement at week 16. What the reader sees now: the
   Velostra bar looks twice as tall as the Corvane bar. What the data are: 88% versus
   84%, a 4-point difference that was not statistically significant, on a secondary
   endpoint. Measured: because the axis starts at 80%, the gap looks about 21 times its
   real size. Plainer version: with the axis from 0% to 100% the bars are nearly the
   same height. To change: start the axis at 0%; print 88% and 84% on the bars; add n
   = 320 per arm; title it as a secondary endpoint and say the difference was not
   statistically significant; add the source. Or drop the chart; that choice is yours.

Who stands behind the evidence
1. KELNA-1: funded, designed and analyzed by Example Pharma; three of eight authors are
   employees. Now stated on slide 3, where the result is used.

Questions for you
1. Which market is the doctor-facing version for? It changes which rules your review
   will apply.

Next step: this goes through your promotional review process before the sales force or
the agency uses it.

I compared the draft with what you gave me; nothing here was checked with a tool.

## Behind the note (reference only, not shown to the person)

Patterns UC1, UC2, NF1, NF7, CH1, IN1, IN5, UC7, UC8 in `references/patterns.md`.
Rules: R5 and R7 (UK, if the market is the UK), R1 to R4 as good practice since the
market is not stated and the audience is doctors, not consumers; R9 for what a
disclosure contains. The superiority claim itself goes to `claims-and-label`; the
relative-only figure on slide 2 is also counted by `grounded-statements`.

Scripts used:

```
python scripts/chart_scale.py --axis-min 80 --axis-max 90 --value 84 --value 88
python ../grounded-statements/scripts/risk_metrics.py --treat-rate 0.22 --ctrl-rate 0.28
python ../grounded-statements/scripts/risk_metrics.py --treat-rate 0.03 --ctrl-rate 0.01
```

Derived: drawn bar ratio 2.0 against an actual ratio of 1.048, so the difference looks 21
times its real size, and fills 40% of the plotted range. Flares: risk difference −6.0
percentage points, crude relative risk 0.786; the paper's 0.79 is reported as given.
Injection-site reactions: +2.0 percentage points, relative risk 3.0.

Check lines returned to `trusted-check`:

```
Unbiased · uncertainty: 2 statements more certain than the data allow, 0 statements less certain than the data allow, 2 results missing an interval, sample size, follow-up or limitation the material gives (not tool-checked)
  - slide 1: "proves superiority" from one open-label trial
  - slide 2: "dramatic"; follow-up and design not stated
Unbiased · framing: 3 figures or charts framed to look larger or smaller than they are (not tool-checked)
  - slide 4: axis starts at 80%, so a 4-point, non-significant gap looks like a doubling
  - slide 5: "only 3%" with no comparator, while the benefit is given as a relative figure
Unbiased · interests: 2 interests in the material, 2 not disclosed where the result is used, 1 source labeled independent or neutral without support in the material (not tool-checked)
  - slide 3 calls the trial independent; the paper names the maker as funder and analyst
```
