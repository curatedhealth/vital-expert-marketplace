# Chart description (honesty sheet)

| Field | Value |
|---|---|
| Model owner | |
| Chart kind | bar / line / waterfall / tornado / quadrant / other |
| Title (must be non-causal) | |
| Axis min | 0 unless justified below |
| Axis min justified? | Y/N — reason: |
| Relative effect shown? | Y/N |
| Absolute effect shown? | Y/N (required if relative) |
| Withhold chart? | Y/N — reason: |
| Linked exhibit template | options-matrix / sensitivity-tornado / value-waterfall / portfolio-placement / delivery-dependency |

## Series
| Name | Value | Source id | Class |
|---|---|---|---|
| | | | |

## Render rule
Use the linked exhibit template’s mermaid/ASCII block. Values come only from this series table. Prefer withhold over cropped axes or causal titles.

Script: `python3 scripts/chart_scale.py exhibit.json --json`
