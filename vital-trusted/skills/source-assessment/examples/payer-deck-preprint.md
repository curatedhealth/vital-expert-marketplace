# Worked example: a preprint in a payer deck (without VERIFY)

Invented case for teaching. "Tavexa", "Kestrel-RW" and every figure are fictional. No
real product, study, server or person.

## Request

"Market access lead here. Slide 6 of our payer deck says 'Tavexa cuts hospital
admissions by 35% (Lee et al., 2026)'. Is that source good enough to put in front of
the regional payer next month? Here's the PDF."

## What was supplied

A PDF. Its first page shows: "Kestrel-RW: hospital admissions with Tavexa versus
standard care in routine practice. Lee J, Haas M, et al. Posted 3 June 2026. This
article is a preprint and has not been certified by peer review." Funding section:
"Funded by the manufacturer of Tavexa. JL and MH are employees of the manufacturer."
Methods: retrospective cohort from claims data in two countries, 4,200 adults with
condition X; admissions within 12 months 13.0% with Tavexa versus 20.0% with standard
care; adjusted hazard ratio 0.65 (95% CI 0.55 to 0.77). No DOI on the PDF. The payer
is in a third country.

VERIFY is not connected in this assistant.

## Depth

Payer material leaves the company: full card, both tasks, pointer to the review process
(TR-H12, TR-H11).

## What the person reads

I can't tell you whether it is good enough; your medical and promotional review decides
that. Here is what it can and cannot carry for a payer, so you can decide how to use it.

**Source:** Kestrel-RW, Lee J, Haas M and colleagues, posted 3 June 2026
**Identifier:** none on the PDF

**What it is:** a preprint of an observational study (a look back at insurance claims
data).
**Peer review:** not peer reviewed. The PDF says so on its first page.
**Who made it:** funded by Tavexa's manufacturer; two authors are employees, as the
paper discloses.
**Fits your question:** partly. It is about hospital admissions with Tavexa compared
with standard care in adults with condition X, which matches. The data come from two
other countries, not the payer's, and from routine practice, not a trial.

**How strong:** one observational study. It shows that Tavexa use was linked with fewer
admissions; it cannot show on its own that Tavexa caused the difference, because the
patients were not randomly assigned.
**Up to date:** posted 3 June 2026. Whether a peer-reviewed version has since been
published, or the preprint revised: not checked.

**What it can carry for a payer:** "In a manufacturer-funded observational study of
4,200 adults, posted as a preprint and not yet peer reviewed, 13.0% of patients on
Tavexa and 20.0% on standard care were admitted within 12 months (adjusted hazard ratio
0.65)."
**What it cannot carry:** "Tavexa cuts hospital admissions by 35%." That reads as a
proven effect, gives only the relative figure, and drops that the data are unreviewed,
observational, sponsor-funded and from other countries. A payer will ask about all
four.

**To use it:** check whether a journal version exists and cite that if so; give both
admission rates; label it as a preprint; and expect the payer to ask for local data.
**Next step:** the deck goes through your medical and promotional review process before
it is used.

Not tool-checked. With VERIFY connected, the document could be qualified and its
update status checked; without a DOI, the update check would come back "not checked".

## Behind the answer (reference only, not shown to the person)

- Patterns: S2 (preprint as published), S6 (association as cause), S8 (interests),
  S12 (another market's data), S5 (one study). Relative-only figure: hand the wording to
  `grounded-statements` (N1); the person's 35% is the relative reading of the adjusted
  hazard ratio, which is reported as given, not recomputed.
- Rules: R3 (ICMJE on preprints: label as preprint; cite the published version when it
  exists), R1 (GRADE: observational evidence starts lower; one study is not the body of
  evidence), R7 (disclosure of sponsor and interests).
- Script: `python scripts/identify_source_id.py "Kestrel-RW Lee 2026"` returned no
  identifier, so the card says "none on the PDF" and the currency line says "not
  checked".
- Gap the reviewer would see in the TRUSTED summary:
  `[GAP: out of date or unclear date — whether a peer-reviewed version exists — check the preprint page or ask the authors]`.

## Check line returned to trusted-check

```
True · sources: 1 looked at, 1 not peer reviewed or status not confirmed, 1 made or paid for by an interested party, 1 do not fit the question or reader (not tool-checked)
True · strength and currency: 1 single studies carrying a general claim, 0 retracted or corrected, 1 may be replaced or undated, 1 currency not checked (not tool-checked)
```
