# Worked example: a competitor claim from a press release (with VERIFY)

Invented case for teaching. "Orvelin", its maker and every figure are fictional. The
VERIFY values below are placeholders in angle brackets: no tool ran for this example,
and a real answer prints only what the tool returned (TR-H4).

## Request

"Brand manager. I'm writing the competitor summary for our leadership team. Orvelin
says it cuts relapses by 60%. Here's their press release link. Can I put that in as a
fact?" The person supplies an https link to the competitor's news page.

VERIFY is connected.

## Depth

Leadership material, internal: short card (TR-H12). The person's question is whether
the press release can carry "a fact".

## Steps and calls

1. `python scripts/identify_source_id.py "<link>"` returns URL only, with the note
   that the currency check will come back "not checked".
2. Qualify, passing the person's question:

   ```
   qualify_source({ "url": "<link as supplied>", "question": "Does Orvelin reduce relapses by 60%?" })
   ```

3. Currency, with the only identifier available:

   ```
   check_currency({ "url": "<link as supplied>" })
   ```

   Per the schema, a URL alone returns notices ["not checked"].
4. Read the page as supplied: dated 2 May 2026; issued by Orvelin's maker; says the
   phase 3 trial "reduced relapses by 60%"; gives no event rates, no number of patients
   and no publication; says full results "will be presented at an upcoming meeting".
5. No sentence is being tested against the page here. If the person later wants
   "Orvelin's maker reported a 60% relative reduction" checked against the page, that
   goes to `claim-assessment` with the quoted passage.

## What the person reads

**Orvelin press release, 2 May 2026:** a company announcement by Orvelin's maker, not
peer reviewed. It can carry: "Orvelin's maker announced on 2 May 2026 that its phase 3
trial reduced relapses by 60% (relative figure; no event rates or publication yet)." It
cannot carry "Orvelin cuts relapses by 60%" as a fact: the trial results are not
published, the figure is relative only, and the source is the competitor itself.
Worth watching for the full results at the meeting the release mentions.

Checked with VERIFY on 20 October 2026
<title, issuer and date as returned>
Source score <total as returned>: <each axis with a number, as returned>
Tier: <tier as returned> (how completely the source identifies itself, not how strong
the evidence is)
Retraction and updates: not checked (link only, no DOI)

The score describes the page: who published it, how recent it is, how well it matches
your question, how completely it identifies itself. It does not say whether the 60%
is right.

## If qualify_source had returned inadmissible

"VERIFY could not qualify this link: <reason as returned; for a failed fetch, the fetch
failed>. The title, publisher and date are not filled in. If you paste the page text or
send a PDF of it, I can work from that." The rest of the card is filled from what the
person supplied and marked "as supplied by you".

## Behind the answer (reference only)

- Patterns: S1 (press release as evidence), S8 (made by an interested party), S16
  ("not checked" is not "clear"), S15 (score is not a verdict on the 60%).
- Why short: an internal leadership summary. If the same claim went into sales-force
  material, the full card and the promotional review pointer would apply, and
  comparative claims would go to `claims-and-label`.
