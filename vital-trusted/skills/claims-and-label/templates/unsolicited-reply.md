# Output format: reply to an unsolicited question

For a medical science liaison, medical information or medical affairs reply to a
doctor's own question (`tasks/promotional-boundary.md`). The reply is a draft for the
medical information procedure. Everything factual comes from the material supplied
(TR-H1). No clinical recommendation (TR-H6).

## First, if any input mentions a safety event (TR-H14)

If the doctor's question or any other input mentions a possible side effect, pregnancy
or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
medication error, lack of effect or product quality problem, put the safety flag from
`../../patient-safety/templates/safety-flag.md` ("Before the draft: something to pass to your
safety reporting procedure"), with the doctor's exact words quoted. It is unconditional:
no "may need", no judgment of whether the event is related or reportable. If the question
mentions none of these, there is no flag. A use the doctor asks about for a specific
patient that has not happened yet is not a flag: it is the medical information question
this reply answers. A use that already happened is a report and gets the flag. The flag
comes before the reply and before any question.

## The reply

```
Subject: Your question about <topic, in neutral words; no brand slogan>

Dear Dr <name as given>,

Thank you for your question of <date as given> about <the question, restated in one
sentence>.

<If the use is outside the label supplied:> This use is not included in the approved
<market> product information (revision <date>). The approved use is
<indication, in the label's words>.
<If the market or revision date was not given, keep the sentence and put the gap inside
the draft:> This use is not included in the approved [GAP: not supplied; market;
which country this reply is for] product information (revision [GAP: not supplied;
revision date; from the label you are working from]). The information below is provided in response to your
question and is not a recommendation to use <product> in this way.

What the available data show
<Study as supplied: design, number of patients, population, what was measured, result
as reported, with its uncertainty.>
<Limitations as reported or evident from the design, e.g. small, open-label, no
comparator, post hoc.>
<If no data were supplied:> [GAP: not supplied; data on <use>; supply the
publication or medical information response document]

References
<Only references supplied by the person.>

<Offer of further contact only in the form the company's procedure allows.>

<Sender as given>
```

## Note to the person (not part of the reply)

```
This reply answers only the question asked and makes no recommendation on dose or use.
<If the use is outside the label supplied:> "Not included" is per the label you supplied
(<market>, revision <date>). I did not check that it is the current approved version;
your regulatory team holds that.
<If the market or revision date is missing:> The market and the label's revision date
were not given; they are left open in the draft for you to fill.
<One line per thing kept out, e.g. "I left out the efficacy data in the approved
indication; the doctor did not ask for it.">
Next step: this goes through your medical information procedure before it is sent.
```

## What the reply never contains

- Brand taglines, promotional adjectives, exclamation marks, calls to prescribe.
- Data, uses or products the doctor did not ask about.
- A dose, patient selection or treatment recommendation for the use asked about.
- A statement that the use is safe or effective in TRUSTED's own voice.
