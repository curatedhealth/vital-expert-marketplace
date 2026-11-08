"""Structural claim-vs-passage checks (offline). Ported from mcps/verify/claim_structure.py.

Label results not tool-checked. Never treats a match as world-truth.
"""

from __future__ import annotations

import re
from typing import Optional

_PCT = re.compile(r"(\d+(?:\.\d+)?)\s*%")
_POINTS = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:percentage\s+)?points?\b|(\d+(?:\.\d+)?)\s*[- ]point\b",
    re.I,
)
_WEEK = re.compile(r"\bweek\s*(\d+)\b", re.I)
_MONTH = re.compile(r"\b(?:month|months)\s*(\d+)\b|\b(\d+)\s*months?\b", re.I)
_HALF = re.compile(r"\b(?:about|around|roughly|nearly|almost)\s+half\b|\bhalf\b", re.I)
_REL_PCT_GAIN = re.compile(
    r"\b(?:an?\s+)?(\d+(?:\.\d+)?)\s*%\s+(?:gain|increase|rise|improvement|reduction|decrease)\b",
    re.I,
)
_ABS_POINT = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:percentage\s+)?points?\b|"
    r"(\d+(?:\.\d+)?)\s*[- ]point\s+(?:gain|increase|difference|improvement)",
    re.I,
)
_NEG_PASSAGE = re.compile(
    r"\b(?:no\s+significant\s+difference|did\s+not\s+(?:improve|reduce|increase|differ)|"
    r"not\s+significant|failed\s+to\s+(?:improve|show)|was\s+not\s+(?:improved|superior))\b",
    re.I,
)
_POS_CLAIM = re.compile(
    r"\b(?:improved|improves|reduced|reduces|increased|increases|superior|benefit(?:ed|s)?)\b",
    re.I,
)
_MAY = re.compile(r"\b(?:may|might|could|possibly|potentially)\s+(\w+)", re.I)
_DOSING = re.compile(
    r"\b(?:once|twice)\s+a\s+(?:day|week|month|year)\b|\b(?:daily|weekly|monthly|yearly)\b|"
    r"\bevery\s+\d+\s+(?:hours?|days?|weeks?|months?)\b",
    re.I,
)
_COMPARATORS = (
    (re.compile(r"\bplacebo\b", re.I), "placebo"),
    (re.compile(r"\bstandard\s+care\b|\busual\s+care\b|\bactive\s+control\b", re.I), "active"),
)
_SUBGROUP = re.compile(
    r"\b(?:in\s+(?:the\s+)?(?:subgroup|sub-group|women|men|elderly|patients\s+with)|"
    r"among\s+\w+|restricted\s+to)\b",
    re.I,
)
_OVERALL = re.compile(r"\b(?:overall|in\s+all\s+patients|the\s+whole\s+population|across\s+all)\b", re.I)

# Number words / fractions → percent value (general English, not product-specific).
_NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
_N_IN_M = re.compile(
    r"\b(" + "|".join(_NUMBER_WORDS) + r")\s+in\s+(" + "|".join(_NUMBER_WORDS) + r")\b",
    re.I,
)
_FRACTION = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")

# Unit / schedule families — mismatch → contradicted.
_MASS_UNIT = re.compile(r"\b(\d+(?:\.\d+)?)\s*(mg|g|µg|ug|mcg|kg)\b", re.I)
_PER_PERIOD = re.compile(r"\bper\s+(day|week|month|year)\b|\b(?:once|twice)\s+(?:daily|weekly|monthly)\b", re.I)

# Association in passage vs causal claim language.
_ASSOC = re.compile(
    r"\b(?:associat(?:ed|ion)|correlat(?:ed|ion)|link(?:ed)?\s+with|observ(?:ed|ational))\b",
    re.I,
)
_CAUSE = re.compile(
    r"\b(?:caus(?:ed|es|ing)|responsible\s+for|led\s+to|resulting\s+in|because\s+of)\b",
    re.I,
)

# Arm / group cue near a percent (windowed).
_ARM_NEAR = re.compile(
    r"(\d+(?:\.\d+)?)\s*%[^.]{0,40}?\b(on\s+\w+|with\s+\w+|placebo|control|standard\s+care)\b|"
    r"\b(on\s+\w+|with\s+\w+|placebo|control|standard\s+care)\b[^.]{0,40}?(\d+(?:\.\d+)?)\s*%",
    re.I,
)


def _claim_percents_including_words(claim: str) -> set[str]:
    """Percents written as digits or as N-in-M / fraction forms."""
    out = set(_PCT.findall(claim))
    for match in _N_IN_M.finditer(claim):
        num = _NUMBER_WORDS[match.group(1).lower()]
        den = _NUMBER_WORDS[match.group(2).lower()]
        if den:
            out.add(str(int(round(100.0 * num / den))))
    for match in _FRACTION.finditer(claim):
        num, den = int(match.group(1)), int(match.group(2))
        if den:
            out.add(str(int(round(100.0 * num / den))))
    return out


def _passage_arm_percents(passage: str) -> dict[str, set[str]]:
    """Map coarse arm token → percents mentioned near it."""
    arms: dict[str, set[str]] = {}
    for match in _ARM_NEAR.finditer(passage):
        if match.group(1) and match.group(2):
            pct, arm = match.group(1), match.group(2).lower()
        else:
            arm, pct = (match.group(3) or "").lower(), match.group(4)
        if not pct or not arm:
            continue
        # Normalize "on fictimab" → last token
        token = arm.split()[-1]
        arms.setdefault(token, set()).add(pct)
    return arms


def _mass_pairs(text: str) -> set[tuple[float, str]]:
    pairs = set()
    for match in _MASS_UNIT.finditer(text):
        try:
            pairs.add((float(match.group(1)), match.group(2).lower().replace("µg", "ug").replace("mcg", "ug")))
        except ValueError:
            continue
    return pairs


def structural_verdict(claim: str, passage: str) -> Optional[tuple[str, str]]:
    """Return (verdict, reasoning) or None if overlap scoring should continue.

    Verdict strings match ClaimVerdict values: supported, partially_supported,
    not_supported, contradicted.
    """
    claim = claim or ""
    passage = passage or ""
    if not claim.strip() or not passage.strip():
        return None

    # H5 / negation: passage denies effect, claim asserts improvement.
    if _NEG_PASSAGE.search(passage) and _POS_CLAIM.search(claim):
        return ("contradicted", "passage denies an effect the claim asserts")

    def _stem(word: str) -> str:
        w = word.lower()
        for suf in ("ing", "ies", "ied", "ed", "es", "s"):
            if w.endswith(suf) and len(w) > len(suf) + 2:
                return w[: -len(suf)]
        return w

    # H7 / modality: passage hedges, claim states certainty (verb stems may differ).
    may_pass = list(_MAY.finditer(passage))
    if may_pass and not _MAY.search(claim):
        for match in may_pass:
            stem = _stem(match.group(1))
            if stem and re.search(rf"\b{re.escape(stem)}\w*\b", claim, re.I):
                return ("partially_supported", "passage hedges (may/might/could); claim states it as fact")

    # Association vs cause.
    if _ASSOC.search(passage) and _CAUSE.search(claim) and not _CAUSE.search(passage):
        return ("partially_supported", "passage reports association; claim states causation")

    # Dosing schedule asserted in the claim but absent from the passage.
    if _DOSING.search(claim) and not _DOSING.search(passage):
        return ("not_supported", "claim states a dosing schedule the passage does not")

    # Unit / per-period change (mg↔g, per day↔per week).
    claim_mass = _mass_pairs(claim)
    passage_mass = _mass_pairs(passage)
    if claim_mass and passage_mass:
        # Same numeric magnitude with a different unit family → contradicted.
        for c_val, c_unit in claim_mass:
            for p_val, p_unit in passage_mass:
                if c_val == p_val and c_unit != p_unit:
                    return ("contradicted", "claim unit does not match the passage unit")
                # 1000× scale mg↔g with same digit written
                if {c_unit, p_unit} <= {"mg", "g"} and c_val == p_val:
                    return ("contradicted", "claim unit does not match the passage unit")
    claim_per = {m.group(1).lower() for m in re.finditer(r"\bper\s+(day|week|month|year)\b", claim, re.I)}
    passage_per = {m.group(1).lower() for m in re.finditer(r"\bper\s+(day|week|month|year)\b", passage, re.I)}
    if claim_per and passage_per and claim_per.isdisjoint(passage_per):
        return ("contradicted", "claim dosing period does not match the passage")

    # H4 / time point mismatch.
    claim_weeks = set(_WEEK.findall(claim))
    passage_weeks = set(_WEEK.findall(passage))
    if claim_weeks and passage_weeks and claim_weeks.isdisjoint(passage_weeks):
        return ("contradicted", "claim time point does not match the passage")

    # H6 / comparator mismatch.
    claim_comps = {name for rx, name in _COMPARATORS if rx.search(claim)}
    passage_comps = {name for rx, name in _COMPARATORS if rx.search(passage)}
    if claim_comps and passage_comps and claim_comps.isdisjoint(passage_comps):
        return ("contradicted", "claim comparator does not match the passage")

    # H2 / relative % vs absolute points (explicit "points" wording).
    if _REL_PCT_GAIN.search(claim) and _ABS_POINT.search(passage) and not _REL_PCT_GAIN.search(passage):
        return ("contradicted", "claim states a relative percent change; passage states absolute points")
    if _REL_PCT_GAIN.search(claim) and re.search(r"\b(?:point|points)\b", passage, re.I):
        abs_nums = {m for m in re.findall(r"(\d+(?:\.\d+)?)\s*[- ]point", passage, re.I)}
        rel = _REL_PCT_GAIN.search(claim)
        if rel and abs_nums and rel.group(1) in abs_nums:
            return ("contradicted", "relative percent wording for an absolute point difference")

    # Relative % gain when passage only states two arm percents whose difference equals N.
    rel = _REL_PCT_GAIN.search(claim)
    passage_pct_vals = [float(p) for p in _PCT.findall(passage)]
    if rel and len(passage_pct_vals) >= 2 and not _REL_PCT_GAIN.search(passage):
        try:
            n = float(rel.group(1))
            diffs = {abs(a - b) for a in passage_pct_vals for b in passage_pct_vals if a != b}
            if any(abs(d - n) < 0.05 for d in diffs):
                return (
                    "contradicted",
                    "claim states a relative percent gain; passage states absolute arm percents",
                )
        except ValueError:
            pass

    # H1 / rounding that changes meaning: vague half vs a specific percent in passage.
    claim_pcts = _claim_percents_including_words(claim)
    passage_pcts = set(_PCT.findall(passage))
    if _HALF.search(claim) and passage_pcts:
        try:
            vals = [float(p) for p in passage_pcts]
            nearest = min(vals, key=lambda v: abs(v - 50.0))
            if abs(nearest - 50.0) > 8:
                return ("contradicted", "vague half does not match the passage percent")
            return ("partially_supported", "vague half approximates but does not state the passage percent")
        except ValueError:
            return ("partially_supported", "vague half versus a numeric percent")

    # Arm-aware percent check: a figure that appears in the passage for the same arm is fine;
    # a figure absent from the passage (and not explained as number-words of a passage figure) conflicts.
    if claim_pcts and passage_pcts:
        missing = claim_pcts - passage_pcts
        if missing:
            # Allow number-word / fraction forms that equal a passage percent (already folded into claim_pcts).
            # Only contradict when the claim percent is truly absent.
            return ("contradicted", "claim percent is not the percent stated in the passage")
        # If claim attributes a passage percent to the wrong arm, contradict.
        claim_arms = _passage_arm_percents(claim)
        passage_arms = _passage_arm_percents(passage)
        if claim_arms and passage_arms:
            for arm, pcts in claim_arms.items():
                # Find if this percent belongs to a different arm in the passage.
                for pct in pcts:
                    for p_arm, p_pcts in passage_arms.items():
                        if pct in p_pcts and arm != p_arm and pct not in passage_arms.get(arm, set()):
                            return ("contradicted", "claim attributes a passage percent to the wrong arm")

    # H3 / subgroup as overall: passage scoped to a subgroup, claim states overall.
    if _SUBGROUP.search(passage) and _OVERALL.search(claim) and not _SUBGROUP.search(claim):
        return ("partially_supported", "passage is subgroup-scoped; claim states overall")
    if _SUBGROUP.search(passage) and not _SUBGROUP.search(claim) and not _OVERALL.search(claim):
        if claim_pcts and passage_pcts and claim_pcts <= passage_pcts:
            return ("partially_supported", "passage result is for a subgroup; claim omits that scope")

    # Number-word paraphrase of a passage percent with matching arm cues → supported structurally.
    if claim_pcts and passage_pcts and claim_pcts <= passage_pcts and _N_IN_M.search(claim):
        return ("supported", "number-word form matches a passage percent")

    return None
