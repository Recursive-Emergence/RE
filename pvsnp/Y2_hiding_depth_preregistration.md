# Y2: hiding is depth: barrier or construction. Pre-registration

*Drafted 2026-09-11 on branch `y2-hiding`, on the author's go ("Draft Y2 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices on record apply:*
- *smallest case first;*
- *every new bound beside the record's lemmas and the literature;*
- ***(new, from Y1′) every flag's implication carried into the priors.***

## Ceiling (first)

- **Y2a** would be a barrier: a result about the route, not about P ≠ NP or OWF.
- **Y2b** would be the shape of a conditional route to OWF.

Both decide whether this door is open at all.

## §0. The finding this starts from (Y1′, the reviewer's statement)

LP22's outputs are deep by design. Its hardness is "a t-time program must know the random location", and a hidden location is precisely K^t − K. So the mechanism by which the known reductions achieve NP-hardness (planted hidden structure) is the mechanism the low-depth promise Q^t_β excludes.
- If that is general, it is a barrier for the holy grail via planted-structure reductions. LP23 (TR23-103, l.386–392) say no barrier is known.
- If it is not general, the escape is a reduction whose hardness does not come from hiding. Y1′'s conditions (1)–(3) say what it must do.

## §1. Arm (a): the barrier (the reviewer's candidate), with my flag raised before any work

**The reviewer's candidate.** Let R be a randomized poly-time many-one reduction from an NP-complete L to MK^tP[s], with NO outputs K^t ≥ |x| − 1 and YES outputs K^t ≤ s ≪ |x|. Then R's outputs are deep on one side.

**Flag E (mine; an expected route, to be written as a proof in the run, not assumed).** The promise converts K^t into K, and the K of a samplable distribution's outputs is its entropy. Sketch:
1. **NO side, where the promise is used.** Take a NO instance φ and an output x of R(φ; ·) inside the promise. Then K^t(x) ≥ |x| − 1 and depth ≤ β·log K, so **K(x) ≥ |x| − 1 − β·log|x|**.
   - D_φ, the output distribution, is computable from φ. By the coding theorem, K(x) ≤ K(φ) + log(1/D_φ(x)) + O(log n).
   - So log(1/D_φ(x)) ≥ |x| − |φ| − O(β log n) on a (1 − ε) fraction of the mass, and **H(D_φ) ≥ (1 − ε)·(|x| − |φ| − O(log n))**.
2. **YES side, where no depth is needed.** K(x) ≤ K^t(x) ≤ s on a (1 − ε) fraction of the mass, and at most 2^{s+1} strings have K ≤ s. So **H(D_φ) ≤ s + 2 + ε|x|**.
3. **The gap.** If (1 − 2ε)·|x| > (1 − ε)·|φ| + s + O(log n) (length expansion), then φ ↦ (the circuit R(φ; ·), a threshold k computable from |φ|, |x| and s) is a Karp reduction from L to (the complement of) Entropy Approximation, **with no hiding and no time bound in sight**.
4. **The collapse.** Entropy Approximation is NISZK-complete (Goldreich–Sahai–Vadhan; to be verified under g1), and NISZK ⊆ SZK ⊆ AM ∩ coAM, with SZK closed under complement. So L ∈ SZK and **NP ⊆ coAM, hence PH = Σ₂^p** (Boppana–Håstad–Zachos; to be verified).

**What Flag E implies, carried into the priors (the new practice).**
- If the sketch survives, arm (a) holds **for length-expanding randomized many-one reductions** (|x| ≥ C·(|φ| + s), with C depending on the error ε).
- It does so *without* the hiding mechanism. **"Hiding is depth" is then the explanation of how planted reductions evade the barrier:** depth on the NO side keeps the output entropy the same on YES and NO. It is not the barrier itself.
- The escapes left open would be:
  - adaptive (Turing) reductions: Bogdanov–Trevisan-type arguments are non-adaptive, and Flag E's argument is per query;
  - reductions that do not expand length (|x| < C·(|φ| + s));
  - non-black-box reductions.

  This matches LP23's "perhaps with a non-black box reduction" (l.391).
- **The suspicion protocol at full strength:** LP23 say no barrier is known, so either Flag E is known in another form, or it has a gap. Candidate gaps to check first:
  - (i) the promise's error handling: outputs outside the promise on an ε fraction;
  - (ii) whether EA's completeness uses the same entropy notion (Shannon) and the same gap form;
  - (iii) whether the coding-theorem step needs D_φ computable exactly or only samplable;
  - (iv) whether length expansion is really forced for natural reductions from SAT, since padding φ changes |φ| but not K(φ).

**Kill tests for the barrier (the reviewer's).**
- **The identity on random strings** (no reduction, no hiding; it lands in Q). It is not a reduction from an NP-complete problem, so it must be consistent with any statement. Check that Flag E says nothing about it.
- **LP22** (hiding, deep): its NO outputs are *not* K-random (K(A | z) = O(n log n), Y1′ §2.1), so step 1 does not apply. Consistent.
- **Any known reduction landing in Q^t_β would refute the barrier.** Y1′ found none.

## §2. Arm (b): the construction shape (the reviewer's), with my flag

**The reviewer's shape.** YES outputs are compressible for a non-hidden reason, e.g. YES outputs lie in the range of a fast generator on witness-derived seeds (K^t ≤ |w| + O(1)), and NO outputs are uniform. The depth on YES is then small if witnesses are incompressible.

**Flag W (mine; before any work).**
- A reduction never holds the witness, whether it is many-one, Turing, adaptive or not. So "outputs = G(witness)" can only mean that the reduction samples x so that *if* a witness exists, x has a short description through it.
- By Flag E's step 2, that makes the YES distribution low-entropy while the NO distribution is high-entropy. **So arm (b), as shaped, is exactly the case Flag E rules out for length-expanding many-one reductions.**
- Arm (b) survives only through the escapes in §1: adaptivity, no length expansion, or non-black-box use.
- **To check: which notion of NP-hardness LP23's holy grail requires.** By their definitions (l.90–110: OWF-hard means "if Π is decided by efficient attackers then all poly-time functions can be inverted"), BPP-Turing reductions, and even non-explicit ones, suffice. So the holy grail does *not* need many-one reductions. The escape "adaptive Turing" is live by definition, to be verified in the text.
- **To check: LP25's boundary promise.** YES: K^t < n − 1 but K^poly > n − log n; NO: K^poly ≥ n − 1. Both sides are near-random in K, so Flag E's entropy gap **does not arise** (both entropies are ≈ n). The expectation is that the boundary promise is immune to Flag E. Whether that was LP25's design reason is to be read in their motivation (l.196–240 and around).

## §3. Arm (c): the literature (g1)

In this order:
1. whether Flag E is stated anywhere: an entropy/SZK barrier for NP-hardness of Gap-K or K-random-string problems under randomized many-one reductions. Candidates to search:
   - Allender et al. on reductions to R_K;
   - Hirahara STOC'20 (hardness of K under uniform reductions);
   - Hirahara–Watanabe;
   - Saks–Santhanam;
   - LP23/LP25's own remarks;
2. Goldreich–Sahai–Vadhan's EA completeness statement (exact gap form);
3. Boppana–Håstad–Zachos (NP ⊆ coAM ⇒ PH collapse), secondary if not read;
4. LP23's definition of OWF-hardness (the reduction notion);
5. LP25's reason for the boundary promise;
6. Hirahara's discussion of planted structure in the NP-hardness of meta-complexity.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y2a** | The barrier is proved for many-one reductions (here: length-expanding randomized many-one, via Flag E). A new theorem if not found stated; the holy grail then needs a non-many-one notion. Re-derive twice, with the suspicion protocol at full strength. |
| **Y2b** | A construction shape exists under some notion (adaptive, non-expanding, or boundary promise), with its requirements met on paper. |
| **Y2c** | Neither closes: the first failing step of (a) is named. |

**Priors.**
- Reviewer: Y2c 50 / Y2a 30 / Y2b 20.
- Mine, carrying Flag E and Flag W into the prior: **Y2a 45 / Y2c 40 / Y2b 15.**
  - Y2a is high because the sketch is short and uses only standard facts.
  - Y2c is substantial because a short barrier that LP23 missed is suspicious: gap (iv), or a known statement making this "known" rather than new, would each move the outcome.
  - If Flag E is found stated, the outcome is Y2a-as-known, recorded with the citation, and it is not a new theorem.
