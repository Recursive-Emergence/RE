# R4: the door, pre-registration

*Drafted 2026-09-10 on branch `r4-door`, on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. It is a document with no Lean, and g1 applies throughout.*

## §1. The RE reading, stated once

The door R3-fold left has two halves:
- a reduction that is **adaptive**, to a function that is not size-verifiable;
- a reduction that is **non-black-box**.

Hirahara (FOCS 2018) passes through the second half by reading the heuristic's **source code**. This is the self-referential move at the right level. It does not exhibit a special string (ruled out by the density barrier). It treats the adversary, itself a short program inside the layer, as data the reduction reads.

*In RE's terms, non-black-box reductions are the mathematical form of "the layer's own methods are objects of the layer".* This is the reviewer's reading, stated here once; RE language is not used again.

## A flag raised before any run: the adaptive half is "unbarred", not "open"

If the smallest case is **not** size-verifiable, the consequence is only that the known adaptive barrier (Bogdanov–Brzuska; AGGM's Theorem 3 as re-proved) **does not apply**. That does not show that an adaptive reduction exists. For adaptive reductions to inverting general one-way functions, no barrier and no reduction is known. The ruling's wording, "the adaptive half of the door is open", is therefore restated as "**unbarred**".

## Part (1): size-verifiability of the smallest case

The smallest case, from R3-fold, is **f = F_{P,n,m}: d = 3, P non-linear, m = Θ(n)**.

**Definitions** (Bogdanov–Brzuska, ECCC TR14-108, verified in R3-fold):
- f is *size-verifiable* if N_f = {(y, s) : |f⁻¹(y)| = s} ∈ AM.
- f is *approximately size-verifiable* if the promise problem A_f is in AM, where A_f has YES instances (y, s, 1^a) with |f⁻¹(y)| ≤ s and NO instances with |f⁻¹(y)| > (1 + 1/a)·s.

**The run must determine:**
- **(a) Which notion BB14's adaptive theorem needs:** exact, approximate, or both.
- **(b) Lower bounds.** "|f⁻¹(y)| ≥ s" is in AM for every f, since f⁻¹(y) is an NP set and Goldwasser–Sipser applies. This is to be stated from a verified source: AGGM's Theorem 5 is the Goldwasser–Sipser statement they use, seen in R3-fold as a theorem heading.
- **(c) Upper bounds.** Is "|f⁻¹(y)| ≤ s" in AM for local f with m = Θ(n)?
  - For general f this is precisely where AGGM's general-case proof failed (per BB14).
  - For local f, f⁻¹(y) is the solution set of a planted CSP with Θ(n) arity-3 constraints, so the question is an AM upper bound on the number of CSP solutions.
  - **Expected: unknown in the literature, with no elementary argument available.** If so, it is recorded as unknown, not guessed.
- **(d) Preimage size itself.** Whether, for m ≥ c·n with a suitable c, a random local function is almost injective with high probability, so that preimage sets are polynomially bounded. Then AGGM's *polynomial-preimage-size* case, the part the erratum did not retract (per BB14), may apply. To be determined from Applebaum's survey or the random-CSP literature, or recorded as unknown.

## Part (2): the non-black-box half, mapped

**What Hirahara's reduction reads from the code.** Verified in R3-fold (l.400–404): the reduction describes x by "the description d and a source code of the algorithm accepting T". The run must state *why* the code helps:
- MINKT is a problem **about the lengths of descriptions**. A heuristic's code is itself a short description, so it can be spliced into a description of x.
- The reviewer's expectation is that this instance-shaped self-reference is what does the work. It is **to be checked against the paper's text**, not assumed.

**Why this evades BT06 / FF93.** Those barriers assume black-box access to the heuristic (verified: Hirahara l.283–286).

**Gap (i): the target problem must be NP-hard.** The run must verify what is known:
- Hirahara, FOCS 2022 (partial MCSP NP-hard under randomized reductions, to verify);
- any later NP-hardness result for meta-complexity problems: Ilango; Ilango–Loff–Oliveira (multi-output MCSP); and others the literature search finds.

**Gap (ii): the landing must be OWF inversion, not DistNP ⊄ AvgP.** The run must verify:
- Liu–Pass 2020 (uniform; verified in R1);
- Liu–Pass, CCC 2022, *On One-Way Functions from NP-Complete Problems* (to verify);
- Hirahara, STOC 2023, *Capturing One-Way Functions via NP-Hardness of Meta-Complexity* (to verify).

For each, the run states what it actually gives.

## Part (3): the sentence that would close the door

**Template:** *a non-black-box worst-to-average reduction from an NP-hard meta-complexity problem P\* to inverting [the smallest-case local function / a K^t-type problem], landing at OWF.*

Filled in:
- the smallest P\* that is known to be NP-hard;
- the closest known technique;
- what that technique lacks: NP-hardness of its source, or OWF as its landing.

## Outcomes

| Code | Outcome |
|---|---|
| **D1** | The door is already someone's stated programme (Hirahara's). Our contribution is the precise sentence plus whatever part (1) determines. Say so. |
| **D2** | Part (1) yields a new fact, such as the smallest case being provably not size-verifiable, so that the adaptive half is *unbarred* for local functions. That is a small real result. |
| **D3** | Both halves close for the smallest case. Record it and stop. |

**Priors.** Mine: D1 75 / D3 15 / D2 10. Part (1)(c) is most likely unknown, which leaves D1. D3 needs a barrier theorem for non-black-box reductions, which I don't expect to exist. The reviewer's: D1 60 / D2 25 / D3 15.

## Guards

- **g1:** no citation from memory; UNVERIFIED counts as none.
- **g5:** every elementary argument is proved in full or not claimed.
- **g8 (new):** "unknown" is an admissible, reportable answer. Not finding a result is reported as not found, with the search stated, and never as "no such result exists".
- **g7:** RE language appears in §1 only.

## Ceiling

Nothing in R4 proves P ≠ NP. At best it restates the frontier of Hirahara's programme, with one possibly new fact. That is where "make it smaller" ends: one sentence naming the reduction that would do it, and the smallest case to try it on.
