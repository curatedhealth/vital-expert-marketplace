# Worked example: routing a medical information request

Invented case for teaching. No real product or person.

## Request

"A doctor emailed asking whether our product can be used in patients with moderate
kidney impairment. Can you draft the reply? I've attached the label."

## Routing answer (as the person sees it)

You need a reply to a doctor's question about using the product in patients with
moderate kidney problems, drafted from the label you attached.

What I'd do first: confirm which country the doctor is in and that the question came
from them unprompted, because both change what the reply may say.
Then: take every dosing statement word for word from the label, and say nothing beyond
what it covers for kidney impairment.
And: if the label does not address moderate impairment, the reply says so plainly rather
than implying the product can be used.

After that it goes through your medical information procedure before it is sent.

Want me to start on the draft?

## Behind the answer (reference only)

Routed to `trusted-intake`, then `patient-safety` (Safe), then `claims-and-label`
(Rule-compliant). True applies throughout through TR-H1.

## Why this routing

- Safe comes first because a wrong dosing statement is the highest-harm failure here.
- Rule-compliant comes second because the risk of implying an unapproved use is real
  but is checked once the safety content is grounded.
- True runs in both through the hard rules (TR-H1): nothing is stated that is not in
  the label.
- No verdict is given on whether the reply can be sent (TR-H3, TR-H5).
