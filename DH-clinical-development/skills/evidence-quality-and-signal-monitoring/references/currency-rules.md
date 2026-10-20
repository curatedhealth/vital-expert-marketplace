# Currency and update rules

Interpretive reference. ES rows are in `EVIDENCE_SYNTHESIS_METHODS.md`, read 19 October 2026. Rules describe the review, not the person's schedule.

## 1. How old may the search be?

| Body | Rule | Rows |
|---|---|---|
| Cochrane (MECIR C37, mandatory) | Rerun or update searches for all relevant sources within 12 months before publication of the review or update, and screen the results; "preferably six months". | ES-52 |
| EU JCA, medicines and devices | Search cut-off at most 3 months before submission of the dossier; applies to any data or information informing relative effectiveness and safety, including covariate searches. | ES-152, ES-156, ES-168 |
| IQWiG General Methods 8.0 | For drug assessments the search update was replaced by an up-to-dateness check of ongoing studies (research "Changes and conflicts"). The operational detail of that check was not quoted in the rows `[GAP]`. | ES-137 |
| NICE PMG48 (HealthTech) | Existing systematic reviews may be used or updated if in line with the scope, with a judgment on which parts need redoing. | ES-133 |
| NICE PMG36 | No search-currency rule quoted in the rows read `[GAP]`. | |
| Rapid reviews | No currency rule quoted `[GAP]`. | |

Consequence for a published review used in an EU JCA dossier: its own last search date is fixed in the past, while the dossier's information retrieval must have a cut-off at most 3 months before submission (ES-168). A published review can inform the dossier's own search (seed studies, strategy ideas) but its search date does not meet the cut-off on its own. Whether and how to use it is the call of the owner the person names (in their words; if none, "owner not named" and ask).

## 2. How fast reviews age (context, not a rule)

In one study of 100 reviews cited in the Cochrane Handbook, the median time to need an update was 5.5 years; 23% were out of date within two years, 15% within one year, and 7% at publication (ES-102). Out-of-date reviews risk misleading decision makers (ES-101). These figures describe that sample, not any particular review.

## 3. Deciding whether to update (Cochrane chapter IV)

Order of questions (ES-103):

1. Is the review question still relevant to decision makers?
2. Was the review done well enough to be worth updating? (A2, AMSTAR 2)
3. Are there new studies, newly available information, or newly recommended methods?

Living systematic reviews suit high-importance questions with frequent new evidence that could change findings (ES-104). For an update, PRISMA 2020 asks for the number of studies in the previous version and the new search and selection results (ES-21); retraction notices and errata are checked for already-included studies too, and MEDLINE and Embase re-searched for latest versions (ES-119, ES-120).

## 4. Change signals the library can show, and what each means

| Signal | Library call | What it means | What it does not mean |
|---|---|---|---|
| Retracted | `literature.check_retraction(doi)` or `verify.check_currency(doi)` | Crossref holds a retraction for the DOI (with notice and date from `check_retraction`) | Not a check of PubMed, Retraction Watch or the journal page (ES-123) |
| Corrected | same | An erratum or correction exists; read it (ES-121) | That conclusions changed |
| Expression of concern | `check_retraction` status `expression_of_concern` | Editors are investigating (ES-125, [WF]) | That the paper is wrong |
| "current: true" | `verify.check_currency` | Not retracted, corrected, superseded or withdrawn in Crossref | That the review's search is up to date |
| Newer citing papers | `literature.find_related(direction="cited_by")` | Candidate new studies or reviews published after the review | That they meet the review's criteria; each needs screening (ES-103) |
| Newer studies by search | `literature.search_literature` with `filters.date_from` = day after the last search | Candidate new studies | A complete search; the library lacks CENTRAL and Embase |

Comments on included papers should not be discarded unread, since they may warn of a future retraction (ES-122); expressions of concern before 2018 need a phrase search in MEDLINE (ES-124).

## 5. Superseded methods and guidance (examples from the research files)

Signals that the methods, not the studies, have changed:

- PRISMA 2009 is superseded by PRISMA 2020 (ES-02).
- ROBINS-I V2 is a draft (November 2025 release); the 2016 tool remains the published one (ES-80, research "Changes and conflicts").
- The 2021 rapid-review guidance was refined by a 2024 update ([WF], ES-116).
- FDA's 2017 device RWE guidance is superseded by the final guidance of 18 December 2025 (CV88).
- CONSORT 2010 and SPIRIT 2013 are superseded by the 2025 statements; the AI extensions still sit on the old parents (CV110 [PAPER] doi 10.1136/bmj-2024-081123, CV115 [PAPER] doi 10.1136/bmj-2024-081477, CV118 [PAPER] doi 10.1136/bmj.m3164, CV122 [PAPER] doi 10.1136/bmj.m3210, research "Changes and conflicts").
- ICH E6(R3) Annex 2 reached Step 4 on 3 June 2026 and takes effect in the EU on 15 January 2027 (CV2).
- IQWiG version 8.0 (19 December 2025) renumbered information retrieval from chapter 8 to 9 (ES-137, research "Changes and conflicts").
- NICE PMG36 was last updated 13 October 2026 (ES-126).
