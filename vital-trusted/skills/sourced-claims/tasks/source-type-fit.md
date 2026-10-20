# Task TR-5.2.2 Right type of source for the use

Design-time guidance: which kind of source can carry which claim, for which reader. It
does not grade a specific source (peer review status checked, funding, retraction,
study quality); that is `source-assessment` with VERIFY.

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | Name each source's type, name each claim's kind, match them against the reader's bar |
| Skill | TR-5.2.2 |
| Knowledge | `references/rules.md` (R2, R5, R7, R8, R9, R10), `references/patterns.md` (T1–T7) |
| Tool | None. Companion slot: VERIFY `qualify_source` and `check_currency` through `source-assessment` |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/source-note.md` |
| Input | The draft, the supplied sources, the audience and use from intake |
| Governance | TR-H1, TR-H3, TR-H7, TR-H8, TR-H11 |

## What each kind of source can and cannot carry

Good practice, built on the rules in `references/rules.md`. Where a rule is marked
`[CHECK]` there, the row is practice, not a requirement.

| Source type | Can carry | Cannot carry on its own | Watch for |
|---|---|---|---|
| Approved label or product information (SmPC, prescribing information, patient leaflet) | What the product is approved for, dose, contraindications, warnings, side effects as listed, for the market it is approved in | Claims beyond the approved use; another market's approved use | Market and version: name which country's label and its date |
| Peer-reviewed publication of a study | That study's design, population and results, as reported | A general truth from one study; a comparison the study did not make | Primary or secondary endpoint; subgroup; the authors' own limitations |
| Systematic review or meta-analysis | The pooled picture across the studies it included | Results of a study it did not include | Date of the search; which studies were in |
| Preprint | That a result has been posted for comment | A settled finding; anything for a payer, doctor or patient as if reviewed | Must be labeled a preprint in the citation (R10) |
| Conference abstract or poster | That a result was presented, with the limited detail an abstract gives | Full methods; final results; a primary reference where a full article exists (R10) | Interim data; later publication may differ |
| Regulator or HTA document (assessment report, guidance, decision) | What that body decided, required or recommended, on that date, for that market | Another market's position; the body's view on a question it did not address | Draft versus final; superseded versions; title and date |
| Clinical guideline from a professional society | What the guideline recommends, at the grade it gives, as of its date | That the recommendation is universal or current without a date | Edition, year, region |
| Company data on file | Internal data the company holds and can provide on request | A claim a payer or doctor cannot see the basis for unless it will be provided; anything inconsistent with the label or the registration studies (R8) | Name the data on file specifically; confirm it can be shared on request through the company's process |
| Market research or survey (own or third-party) | What the surveyed group said or did, with sample size and date | What "physicians" or "patients" in general think; efficacy | Sample, method, sponsor, date |
| Sales or prescription data (third-party or internal) | Volumes, share, trends for the stated period and market | Why the numbers moved | Data provider, period, definition of the market |
| Press release (any company) | That the company announced something, on that date | Efficacy, safety or comparative claims as fact | Written by an interested party; look for the underlying publication or regulatory record |
| News article or trade press | That something was reported, on that date | Study results, regulatory decisions or competitor facts as fact | Find the primary record the article reports on |
| Blog, social post, opinion piece | That a person expressed a view | Any factual claim in material leaving the company | Author, date, interest |
| Internal document (strategy, brief, meeting notes) | What the team planned, decided or recorded | External facts unless it cites a primary source you also have | Doc-to-doc citation: the internal document is not the evidence |
| Personal communication | What a named person told the company, with their permission | A fact a reviewer cannot check (R4, R10) | Written permission; exact wording |

## Match to the reader

| Reader and use | Bar for factual claims |
|---|---|
| Internal brainstorm, team notes | Any named source, with its type visible; weak sources marked as weak |
| Leadership update, business review, competitor summary | Primary record where one exists; secondary sources (news, press releases) named as such and not used for efficacy or safety |
| Doctor or other health professional | Label for the approved use; peer-reviewed publications; any other source the company can provide on request through its process (R1, R5) |
| Payer, formulary or HTA body | Sources the payer can examine: published studies, regulator or HTA documents, economic analyses with method and limitations stated; data on file only where it will be provided (R9) |
| Patient or public | The approved label and patient information first; everything else through the company's review |

## Guard (while drafting)

1. **Label each supplied source's type** in the source list.
2. **Before using a source for a claim, check the table:** can this type carry this kind
   of claim for this reader? If not, keep the claim at the level the source supports
   ("the company announced…") or mark a gap for a stronger source.
3. **Prefer the primary record.** When a news story reports a trial, the trial
   publication or registry entry is the source to ask for; the story is a pointer.
4. **Say the type in the citation** when it is not obvious: "(press release, 3 March
   2026)", "(preprint)", "(conference abstract)", "(data on file)".

## Repair (existing draft)

1. **List each claim with the source it rests on** and that source's type.
2. **Flag mismatches:** a claim carried by a source type that cannot carry it for this
   reader. Name the mismatch in plain words ("this efficacy figure comes from a news
   story; the trial publication would be needed").
3. **Fix:** step the claim down to what the source supports, or keep it with a gap for the
   stronger source. Do not swap in a better source from memory.

## Check line

See `assets/check-line.md`.

## Boundaries

- This task names the type of source and whether that type fits. It does not judge
  whether a particular study is well done, peer reviewed, retracted or superseded; that
  is `source-assessment`. Say "not graded with a tool" when VERIFY has not run.
- Whether data on file may be used in a given market, and how it is provided on request,
  is for the company's promotional or medical review process (TR-H11).
