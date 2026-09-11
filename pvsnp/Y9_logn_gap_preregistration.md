# Y9: the O(log n)-gap regime. Pre-registration

*Drafted 2026-09-11 on branch `y9-logn-gap`, on the author's go ("Draft Y9 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply, including the two newest: **when a flag's force comes from applying a theorem inside an oracle world, check first whether that theorem relativizes**, and **"non-black-box" and "non-relativizing" are different properties.***

## Ceiling (first)

Unchanged. Even the favourable outcome (Y9a) would be an **explicit reduction at the top threshold**, hence a conditional route to OWF from NP ⊄ ioBPP — and `NP ⊄ ioBPP` is itself open and untouched by this branch. Y9 proves nothing about P vs NP.

## §0. Refuted premises checked (the practice)

Not reused: "hidden ρ" (Y3); "no off-sample rows", "(1+ζ) inflation" (Y4); "the grid is symmetric" (Y5); "(PL) is loose-access lowness" (Y6, mine); **"the Pessiland oracle does not bar the route" (Y7, mine — reversed by Y8: it does)**.

## §1. Why this regime, and what is verified about it already

**The regime.** Gap O(log n) between the YES and NO complexity thresholds, at the top threshold s = n − 2.
- **Barriers are silent there.** GK24/SS22-style arguments need a gap of ω(log n) (Y3, Y4, verified). Observation O needs s ≤ n − 2 − β·log n (Y2, proved).
- **Reductions are known to be powerful there, for unbounded K.** SS22's Theorem 3, second part (verified in Y3): every L ∈ NEXP has a randomized polynomial-time non-adaptive, polynomially honest reduction to O(log n)-approximating **K**.
- **Y2's compact-reduction escape lands in the same regime** (|x| ≈ K(φ) + s gives gap O(log n)), and Y2 found no compact reduction known.

**So this is the one place where the barriers are silent *and* strong reductions exist — but for K, not for K^t under LP23's depth promise.** Y9 asks whether the technique crosses that gap.

## §2. The step that uses unbounded K (located at drafting; verbatim)

**Hirahara STOC'20, l.146–150:**

> "The set R_K of Kolmogorov-random strings is a distinguisher for a hitting set generator. Indeed, **for any computable hitting set generator** G = {G_n}, the Kolmogorov complexity of G_n(z) is small: **K(G_n(z)) ≤ s(n) + O(log n)** for any z ∈ {0,1}^{s(n)}; thus G_n(z) ∉ R_K."

**SS22, l.253–255:**

> "[28] shows that for every language L ∈ NEXP, L randomized polynomial-time non-adaptively reduces to avoiding the range of an **EXP^NP-computable** hitting set generator with seed length n − O(log n)."

**The step, named (this is what the run must test).** The reduction's power comes from R_K being a distinguisher, and that rests on the bound K(G_n(z)) ≤ s(n) + O(log n), which holds **for any computable generator, with no time bound on the decoder**. The generator actually used is **EXP^NP-computable**. So its outputs are strings with **small K and (presumably) large K^t**: exactly **deep** strings.

## §3. Flags (mine, before any work)

**Flag Z9 (my expected outcome: the step does not survive a time bound — hiding is depth, a fifth instance).**
- Replace K by K^t with t polynomial. The decoder must now *run* the generator, and an EXP^NP-computable generator cannot be run in polynomial time.
- So the bound becomes K^t(G_n(z)) ≤ s(n) + O(log n) only for t exceeding the generator's running time — exponential — and for polynomial t nothing follows.
- **Either** one keeps the EXP^NP generator, and its outputs are deep (small K, large K^t), so they violate LP23's promise Q^t_β and the reduction's outputs fall outside the promise problem;
- **or** one insists on a polynomial-time generator, and then the NO-side "random" guarantee weakens, because the reduction's power in [28] came precisely from the generator being that strong.
- **Expected: Y9c**, with the depth conjecture gaining its fifth instance, and Y9b's naming satisfied by the two horns above.

**Flag R9 (mandatory, from Y8).** If anything *does* adapt, it must be checked for relativization **before** it is called a route: Y8 established that any proof of `NP ⊄ ioBPP ⇒ MK^tP|Q ∉ ioBPP` is non-relativizing, and SS22/[28]'s machinery is a relativizing hitting-set-generator argument as far as read. **An adaptation that relativized would contradict Y8c**, so either it is non-relativizing (and the run must say where), or the adaptation is wrong.
- This flag makes Y9a *self-checking*: the more natural the adaptation looks, the more likely it is mistaken.

**Flag T9 (the promise's role, to be checked).** LP23's problem at the top threshold has NO instances with K^t ≥ n − 1 **and** the depth promise. The [28] reduction's NO instances are "not in the range of the generator", i.e. K-random. **Whether K-random strings satisfy the depth promise is immediate (depth 0 for K^t ≈ K ≈ n), but whether the YES side can be made to fit while keeping the gap at O(log n) is the question.** The run states this explicitly rather than assuming it.

## §4. Kill tests

- **Silent on Y8:** nothing in Y9 may resurrect the non-explicit door; Y9 is about an **explicit** reduction.
- **The depth conjecture's ledger:** if Flag Z9 holds, record it as the fifth instance beside LP22, Proposition H, Proposition H′ and HIR23 — and say plainly that it is an instance, not a proof of the conjecture.
- **Smallest case first:** state the obstruction at the smallest parameters where it appears, not only asymptotically.

## §5. Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y9a** | The technique adapts: an NP-level reduction at the top threshold, the holy grail's explicit form. Re-derive twice, full suspicion, **and Flag R9 first** — it must be non-relativizing or it is wrong. |
| **Y9b** | The unbounded-K step is named and depth or NO-side randomness fails: the regime closes with the reason. |
| **Y9c** | SS22/[28]'s technique already produces deep outputs: the depth conjecture gains its fifth instance. |

**Priors.**
- Reviewer: Y9b 50 / Y9c 35 / Y9a 15.
- Mine: **Y9c 45 / Y9b 40 / Y9a 15.** Flag Z9 carried into the prior: the verbatim bound is stated for *any computable* generator, and the one in use is EXP^NP-computable, so "the outputs are deep" is not a guess about the technique — it is visible in the quoted step. I put Y9c above Y9b because the fifth-instance reading is the more informative way to record the same fact.

## Ruling (the reviewer's, recorded at acceptance as a draft)

**Accepted as a draft.** No run until the author's separate go. **Priors** moved to mine: Y9c 45 / Y9b 40 / Y9a 15 — the reviewer agrees that "the outputs are deep" is visible in the quoted step rather than guessed. **Flags Z9, R9 and T9 adopted.** R9 is the discipline: the relativization check comes first on anything that adapts, and **an adaptation that relativizes is thereby wrong.**

**Ruling (1): Flag Z9 must become a proved statement about the specific generator, not a reading.**
- One half is [28]'s own line: K(G_n(z)) ≤ s(n) + O(log n).
- **The half to prove is the other one: that K^t(G_n(z)) is large for polynomial t.** That is what makes the outputs deep and places them outside Q^t_β.
- **If K^t(G_n(z)) can be small for some z, the fifth instance is not established, and the report says so.**

**Ruling (2): the drop-to-polynomial-time-generator arm must be stated precisely.**
- State exactly what NO-side guarantee [28] needs from the generator's strength (EXP^NP-computability), and what a polynomial-time generator loses.
- **If the loss is "the hitting-set property against the relevant class", name the class.** That is the precise reason the regime closes for K^t, and it is more useful than "weakens".

**Kill tests** as drafted; **smallest case first.**
