# Method: diagnose-value-leaks

## Purpose
Screen alleged value leaks before framing. Inventory who / what / period / how-known. Never invent magnitudes or peer comps.

## Rules
1. Categories closed set: delay, rework, unused_capacity, quality_escape, missed_adoption, other.
2. Evidence class M/V/H/O required per row. Dollarization requires M or V plus magnitude_source.
3. `attest_none` allowed when the owner attests no leaks — empty list otherwise refused.
4. Offline script `leak_screen.py` enforces schema; does not invent figures.

## Outputs
Leak worksheet + gaps. Next: `rebuild-baselines` or `frame-the-decision` / `size-value-at-stake`.

## Lane A absorb — step-level probes without invented $ (7 November 2026)

Probe variability, speed, and output quality at job steps; link leaks to **evidence requests**, not estimated savings (HBR job map “Uncovering Opportunities” — LA-HBR-JOBMAP / WR-017). Categories remain owner taxonomy; magnitudes stay sourced (existing `leak_screen.py`).

## C5 absorb — evidence-first leak screen (7 November 2026)

Lane A: LA-C5-002 (IPA disbenefit≠risk), LA-C5-005 (stakeholder effects), LA-C5-010 (LEI aliases — contextual only), LA-C5-012 (MAPS incentive warning). Keep closed codes: delay, rework, unused_capacity, quality_escape, missed_adoption, other.

### Allegation → evidence (WR-C5-009,010)
Inventory who / what / workflow / period / how-known. Distinguish observed current leak, anticipated change-disbenefit, and uncertain risk. Source raw evidence; no model-supplied dollars.

### Closed aliases (WR-C5-021,027)
Supported contextual aliases only: waiting→delay; correction/rework→rework. No new closed category without owner triage. Headroom ≠ automatic unused_capacity loss. Detected/repaired defect ≠ quality_escape. Mandatory inspection/control is not removable Lean "waste".

### Measurement traps (WR-C5-022,023)
MAPS examples/percentages/directions are not live rules. Meeting-count ≠ impact/sales/ROI. No MLR/regulatory-risk reduction claim without domain assessment.

### Facilitation
- Who experiences this alleged loss, over which period, and what record shows it?
- What negative effect or unwanted behavior could this metric conceal or encourage?

Offline fields: `references/proposed-record-contracts-c5-2026-11-07.yaml`. Catalogue: `references/lane-a-sources-c5-2026-11-07.md`.

## C5 deepen — measured figures and what is worth measuring (8 November 2026)

`leak_screen.py` content rules (exit 1 on any gap): a `magnitude` needs `magnitude_source`, `magnitude_unit` and a recognised `period` (2025-Q3, FY2025, 2026-H1, 2025-11 or an ISO range); a dollarized leak needs class M or V, a magnitude, a source and a currency unit; `who` is required because the leak names who bears the loss (V-C5-LEAK-02). IDs follow the known-answer suite: mandatory inspection is not removable waste (V-C5-LEAK-03); meeting or activity counts are not impact (V-C5-ATTR-05).

Internal method notes (cleared `owner_internal_pack_yes`; not for external redistribution):
- VP-ON-C5-003 (WR-C5-010): the leak record states "where or how the benefit or impact happens", that is, who experiences the loss and in which step.
- VP-ON-C5-004 (WR-C5-023): "Just because something can be measured does not mean that it should be measured." A countable activity is not a leak, and a count is not an impact.

## Deepening note (8 November 2026)

WR-012: the eight job-map steps find where leaks might sit; they are never gates, scores or funding units. `leak_screen.py` refuses `job_steps_as_gates`, a gates list that equals the step names, and gate wording tied to a step. Leak ids follow the suite: V-C5-LEAK-02 closed codes and who bears the loss, V-C5-LEAK-03 mandatory inspection is not removable waste, V-C5-LEAK-05 no invented magnitude, V-C5-ATTR-05 activity counts are not impact.
