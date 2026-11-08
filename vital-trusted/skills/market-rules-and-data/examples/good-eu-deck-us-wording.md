# Worked example: a US deck reused for doctors in Germany

Invented case for teaching. "Zelorastat" and "Fictional Pharma" are fictional; the
slides and labels are made up.

## Request

"We're reusing the US launch deck for a dermatology meeting in Germany next month. Can
you tidy up the closing slide so it works for German doctors? Here's the slide and our
EU SmPC section 4.1."

> (Slide, supplied) **Zelorastat: FDA-approved for adults with moderate to severe
> plaque psoriasis.** Important Safety Information: see Boxed Warning. Please see full
> Prescribing Information. To report SUSPECTED ADVERSE REACTIONS, contact Fictional
> Pharma at 1-800-555-0100 or FDA at 1-800-FDA-1088 or www.fda.gov/medwatch.
> WAC $6,200 per 4-week supply. US-ZEL-0912 09/26.
>
> (SmPC 4.1, supplied) Zelorastat is indicated for the treatment of moderate to severe
> plaque psoriasis in adults who are candidates for systemic therapy.

## What the skill recognizes

- Market: Germany, stated. Reader: dermatologists. Use: a company meeting about the
  product, so treated as promotional; the review process decides.
- US signals: FDA approval, "Boxed Warning", "Important Safety Information", "full
  Prescribing Information", MedWatch and a US phone number, a US list price, a US job
  code and date.
- The supplied SmPC indication is narrower than the slide's ("who are candidates for
  systemic therapy"). The fix uses the supplied SmPC wording word for word and flags the
  difference for the label check (`claims-and-label`) rather than judging it.
- The EU elements usually expected: essential information compatible with the SmPC
  with its date, and the supply classification (M1, M5); German national code
  elements were not read.

## Fixed slide (as the person sees it)

> **Zelorastat** [GAP: not supplied — authorization status for Germany, as your label
> states it — the German or EU product information]
> Indicated for the treatment of moderate to severe plaque psoriasis in adults who are
> candidates for systemic therapy (SmPC section 4.1, as supplied).
> [Essential information compatible with the SmPC, with its date — from your label owner]
> [Supply classification — from the SmPC]
> [Side-effect reporting statement for Germany, if your review process expects one]
> [Price and reimbursement information, only if your review process asks for it]
> [Job code — from your approval system] [Date of preparation — set at approval]

## Note (as the person sees it)

> Market and statements (draft, not yet reviewed)
>
> Written for: Germany, dermatologists, a company meeting, from the slide and SmPC
> section 4.1 you supplied.
>
> Changed for the market
> 1. "FDA-approved" → a placeholder for the German status. US approval tells a German
>    doctor nothing about use in Germany.
> 2. "Important Safety Information", "Boxed Warning", "full Prescribing Information" →
>    a placeholder for the essential information from the SmPC. These are US label
>    headings; German doctors look for the SmPC.
> 3. The US reporting line and phone numbers removed; a placeholder for the German one.
> 4. The US list price removed. Whether price or reimbursement belongs on the slide is
>    for your review process.
> 5. The US job code and date removed. The German version gets its own at approval.
>
> One more thing for your label check: the SmPC indication says "who are candidates
> for systemic therapy"; the slide did not. I've used the SmPC wording.
>
> Statements usually expected for promotional material for doctors in the EU
> - Essential information compatible with the SmPC, with its date ... placeholder left
> - Supply classification ............................................ placeholder left
> - Side-effect reporting statement ... not confirmed for Germany: ask your review process
> - Audience statement ...................................... not on the slide (usual practice)
> - Job code ........................................ placeholder left: from your approval system
>
> Not filled in by me: job code, dates, links and SmPC text beyond section 4.1.
>
> Next step: this goes through your promotional review process for Germany before the
> meeting. The list above is what is usually expected in the EU; German rules and the
> German industry code may add more, and that process holds the full list.

## Check line (to trusted-check only)

```
Rule-compliant · market: Germany, 5 statements that may not be allowed there (not tool-checked)
  - FDA approval, US label headings and US reporting route on a slide for Germany
  - US list price and US job code carried over
Rule-compliant · required statements: 4 missing for this kind of material, as the person's market and process define them (not tool-checked)
  - essential information, supply classification, job code and date left as placeholders
```

## Behind the reply (reference only, not shown to the person)

Patterns avoided: J1, J2, J5, S2, S3, S7. Rules: M1, M5 (EU and EFPIA, confirmed), M14
(US, used only to recognize the US elements), M19 `[CHECK]` for the reporting statement
outside the UK; German national code `[CHECK]`. The narrower SmPC indication goes to
`claims-and-label`.
