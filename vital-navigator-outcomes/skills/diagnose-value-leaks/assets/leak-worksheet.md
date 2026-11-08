# Value leak worksheet

Use for live facilitation. Leave cells blank rather than invent. Categories are closed: delay · rework · unused_capacity · quality_escape · missed_adoption · other. No new codes. Waiting→delay and correction/rework→rework only when evidence fits.

| Field | Value |
|---|---|
| Owner (named) | |
| Attest none (Y/N) | |
| Period under review | |
| Teaching-as-live? (must be N) | N |

## Leak rows

| Id | Category | Who / workflow | Period | How known (source id / date) | Observed vs forecast vs risk | Class (M/V/H/O) | Magnitude | Magnitude source | Dollarized? |
|---|---|---|---|---|---|---|---|---|---|
| L1 | | | | | | | | | N |
| L2 | | | | | | | | | N |

## Facilitation probes (human)
- Who experiences this alleged loss, in what period, and what record shows it?
- What unwanted behavior or negative effect could this metric conceal?

## Refusals (do not fill)
Invented $, live teaching figures, mandatory inspection as removable waste, meeting-count as impact/ROI, headroom as automatic unused-capacity loss, new closed codes.

Classes: M measured · V document · H design · O owner-stated.  
Dollarized requires class M or V plus magnitude_source.  
Script: `python3 scripts/leak_screen.py screen.json --json`
