# Rendered example: deck repair with framing note and chart card (sourced draft)

Invented teaching case ("Velostra", "KELNA-1", "Example Pharma" fictional). Full bundle
after `honest-framing` repair.

## Repaired slide headlines (excerpt)

1. In KELNA-1 (open-label, 640 adults), fewer patients had a flare by week 24 with Velostra
   than with Corvane (22% vs 28%; relative risk 0.79, 95% CI 0.64 to 0.97).
2. Flares: 6 percentage points fewer on Velostra; relative reduction about 21%. Follow-up 24
   weeks.
3. KELNA-1 was funded and analyzed by Example Pharma, maker of Velostra.

## Framing note (`templates/framing-note.md`, excerpt)

What I changed and why (draft, not yet reviewed)

Based on: KELNA-1 abstract and author disclosures (supplied)

Changed
1. "proves superiority" → one trial result with open-label design named.
2. "dramatic" and relative-only "21% cut" → absolute rates plus relative risk with interval.
3. "Independent head-to-head" → sponsor funding line from the abstract.
4. "only 3%" → 3% vs 1% for injection-site reactions, both arms.

Left as gaps
None from the abstract for the primary endpoint.

Next step: promotional review before agency build for doctors.

## Chart description (`templates/chart-description.md`)

Slide 4 (75% improvement at week 16): A bar chart that starts the vertical axis at 80%
makes a 4-point gap between 88% and 84% look much larger than it is. A plain reading:
88% on Velostra vs 84% on Corvane (difference 4 points, 95% CI −1 to 9; not statistically
significant in the paper). Show the axis from 0%, both n values (320 per arm), and the
secondary-endpoint label. Do not use this chart to imply superiority on the 75% endpoint.

## Source card (shared `../../templates/source-card.md`)

- **Source:** KELNA-1 trial report (supplied abstract)
- **Role:** Primary efficacy and safety data; sponsor-run study
- **Sponsor:** Example Pharma (design, analysis; 3/8 authors employees)
- **Action:** Disclosure line on slide 3; not described as "independent"

## Finding 2 (shared finding-card)

- **Draft:** "Velostra cuts flares by 21%, a dramatic improvement."
- **Issue:** Relative change without absolute rates; certainty beyond open-label trial.
- **Action:** Rewrote with 22% vs 28% and RR 0.79 (95% CI 0.64 to 0.97).

## Disclosure line (`templates/disclosure-line.md`)

KELNA-1 was funded by Example Pharma, which also designed the study and analyzed the data.

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / honest-framing: not tool-checked (offline tools) · uncertainty: 2 overclaims fixed; charts: 1 axis issue; interests: 1 disclosure added
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Unbiased · uncertainty at its real size: 2 certainty or hedging issues fixed (not tool-checked)
Unbiased · numbers and charts: 1 chart needs axis/full-period fix (not tool-checked)
Unbiased · interests: 1 independence word replaced with sponsor disclosure (not tool-checked)
```
