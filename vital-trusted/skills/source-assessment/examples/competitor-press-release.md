# Worked example: a competitor claim from a press release (by hand)

Invented case for teaching. "Orvelin", its maker and every figure are fictional. No tool
ran for this example, and none is needed: the card is built from the page the person
supplied.

## Request

"Brand manager. I'm writing the competitor summary for our leadership team. Orvelin
says it cuts relapses by 60%. Here's their press release link. Can I put that in as a
fact?" The person supplies an https link to the competitor's news page and pastes the
text of the page.

## Depth

Leadership material, internal: short card (TR-H12). The person's question is whether
the press release can carry "a fact".

## Steps

1. `python scripts/identify_source_id.py "<link>"` returns a link only, with the note that
   there is no DOI or PMID to look up in a retraction database.
2. Read the page as supplied: dated 2 May 2026; issued by Orvelin's maker; says the
   phase 3 trial "reduced relapses by 60%"; gives no event rates, no number of patients
   and no publication; says full results "will be presented at an upcoming meeting".
3. Name the kind (a company press release), peer review (not peer reviewed, because it
   is a press release), funders and interests (made by the competitor itself) and fit (it states a relative
   figure for the question asked and nothing else).
4. No sentence is being tested against the page here. If the person later wants
   "Orvelin's maker reported a 60% relative reduction" checked against the page, that
   goes to `claim-assessment` with the quoted passage.

## What the person reads

**Orvelin press release, 2 May 2026:** a company announcement by Orvelin's maker, not
peer reviewed. It can carry: "Orvelin's maker announced on 2 May 2026 that its phase 3
trial reduced relapses by 60% (relative figure; no event rates or publication yet)." It
cannot carry "Orvelin cuts relapses by 60%" as a fact: the trial results are not
published, the figure is relative only, and the source is the competitor itself.
Worth watching for the full results at the meeting the release mentions.

Currency: not checked. The check you can do: look at the company's news page for a
newer or corrected release, and at the meeting program for the abstract.

Not tool-checked: I read what you supplied. No tier or score is given.

This check flags issues. It is not medical, legal, regulatory or ethics review.

## If the person gave only a link and no text

"I can't open links, so the title, publisher and date are not filled in. If you paste the
page text or attach a PDF of it, I can work from that." The rest of the card is filled
only from what the person supplied and marked "as supplied by you".

## Behind the answer (reference only)

- Patterns: S1 (press release as evidence), S8 (made by an interested party), S16
  ("not checked" is not "clear"), S15 (no score or tier is invented).
- Why short: an internal leadership summary. If the same claim went into sales-force
  material, the full card and the promotional review pointer would apply, and
  comparative claims would go to `claims-and-label`.
