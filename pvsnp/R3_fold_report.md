# R3-fold: report

*Run 2026-09-10 on branch `r3-fold`, against the pre-registration (accepted, with the strategy named by the ruling). Every citation was checked against the paper's text (PDFs or PostScript converted locally, line-level) unless it is marked otherwise. It is a document with no Lean.*

## Outcome: **F1** for the conjecture, **F3 on test (c)** for the named strategy

- **The conjecture.** Repaired by Flags A and B, it is a known conjecture: Applebaum's Conjecture 1.2 / 3.9 on random local one-way functions (Goldreich's candidate family).
- **What folding adds.** Nothing new structurally. An iterated fold is itself a local function, of higher locality and with a structured graph.
- **The named strategy fails test (c).** That strategy is a worst-case-to-average-case reduction from an NP-hard problem to inverting the iterated fold. The barrier results below rule it out unless the reduction is adaptive (to a function that is not size-verifiable) or non-black-box. **That is the door, stated precisely in §4.**
- **Priors.** Mine were F1 75 / F3 20; the reviewer's were F1 55 / F3 35. Both expected outcomes occurred, on different parts.

## 1. The thermodynamic reading, closed (Flag A, with the reviewer's lesson)

Erasure is not the cryptographic arrow.
- The projection p(x, y) = x erases n bits and is trivially invertible (pre-registration, Flag A). One-way permutations erase nothing.
- **The parameter that matters is entanglement of the *retained* bits.** Each output depends on several inputs spread through an expander. Goldreich's candidate has that; a projection does not. (This lesson is the reviewer's, recorded here as ruled.)

## 2. Part (1): the map of what is already a theorem

| Item | Verified statement | Source, where checked |
|---|---|---|
| Amplification | Yao: if weak one-way functions exist, so do strong ones | Arora–Barak (draft) text l.10025–10030 (proof deferred to Ch. 17); Liu–Pass 2020, Theorem 2.3 |
| Composition | Luby–Rackoff: a pseudorandom permutation from a pseudorandom function by composing **four** Feistel permutations (**three** for weakened security) | Naor–Reingold, ePrint 1996/011, abstract (a restatement: **secondary**; the original was not fetched) |
| Black-box arrow | With probability 1 over random oracles, the oracle's function is one-way: every oracle PPTM inverts with expectation ≤ poly(n)/2^n | Impagliazzo–Rudich, Theorem 4.1 (PostScript → text) |
| Black-box separation | P = NP ⇒ Eve breaks any secret-agreement protocol with the same probability that Alice and Bob agree | Impagliazzo–Rudich, Theorem 3.3 |
| Local candidates | Conjecture 1.2: for d ≥ 3, a random d-local function with a properly chosen predicate P and output length m is likely one-way. Conjecture 3.9: for every c > 1 there are d and P with F_{P,n,n^c} hard to invert | Applebaum, *Cryptographic Hardness of Random Local Functions* (survey), l.92–95, 520–521 |
| Goldreich's original | expander graph and d-ary predicate, n → n | Goldreich, ECCC TR00-090. **UNVERIFIED:** Type 3 fonts, no text extracted. The family is used only as the survey states it. |

**Circled, and unproved:** the base fold, an explicit local map that is weakly hard to invert on average. Amplification and composition act above it; nothing verified reaches below it.

## 3. Part (2): the conjecture, the first non-trivial case, and composition

**The precise conjecture** is Applebaum's Conjecture 1.2, quoted above, or its polynomial-stretch form, Conjecture 3.9.

**The first non-trivial case, read off the survey** (all verified):
- **Locality.** d = 2 is invertible: "if d = 2 the inversion problem can be reduced to a 2-CNF problem, and can therefore be solved efficiently for any value of m" (l.364–365). So d ≥ 3.
- **Predicate.** Linear (XOR) predicates are trivially invertible (l.365–366). Theorem 3.4: a predicate of F₂-degree c is efficiently invertible at m = Ω(n^c log n) (l.291). So P must be non-linear, and m must stay below n^{deg P}·log n.
- **Output length.** "For linear output lengths m = O(n), the complexity of the best known attacks is 2^{Ω(n)}" (l.522–523).
- **Pseudorandomness side.** Theorem 4.8, a dichotomy at m = n^{1+ε}: degenerate predicates (unbalanced, 1- or 2-correlated, or affine) give noticeable bias; non-degenerate ones give negligible bias (l.860–870).
- **So the smallest case is d = 3, a non-linear predicate, and m = Θ(n).** There the known attacks are exponential. This is "make it smaller" applied to the base fold.

**Composition (question i).**
- *Structure (elementary).* If f is d-local and g is d′-local, then each output bit of f∘g depends on at most d·d′ inputs. So k iterated folds form a d^k-local function whose dependency graph is a composed, structured graph. Iterating adds locality; it adds no new kind of function.
- *What the survey says.* The only composition statement found by search (l.672–674) concerns pseudorandom generators: "a d-local PRG with linear stretch m = (1 + c)n bits can be composed with itself a constant number of times to yield a PRG with an arbitrary linear stretch c′ at the expense of increasing the locality to a larger constant d′".
- No statement was found that iteration *increases* one-wayness. The survey's own framing is that composition trades locality for stretch. On one-wayness under composition the verified record is **silent**, not negative.

## 4. The barrier tests, applied to the named strategy

**The strategy (the reviewer's):** a worst-case-to-average-case reduction via iterated folding. Inverting the composed local function on average over uniform inputs should yield a solver for an NP-hard worst-case problem, with composition supplying amplification and the local structure supplying the reduction.

**(a) Relativization: PASS in principle.** The reduction is meant to use the fold's explicit local structure, not only oracle access to it. A proof that used only oracle access would be Impagliazzo–Rudich territory: relative to a random oracle, the function is one-way with probability 1 (Theorem 4.1).

**(b) Naturalness: PASS.** A reduction is not a large, constructive property of truth tables, so Razborov–Rudich does not apply to the reduction itself.

**(c) Worst-to-average barriers: the naive strategy FAILS.** The verified results:
- **Bogdanov–Trevisan (SICOMP 2006), Theorem 18:** for L NP-hard, V′ an NP relation, and D′ a samplable ensemble, a *non-adaptive* δ worst-to-average reduction from L to (V′, D′) gives L ∈ NP/poly. Their Theorem 7 remark: for NP-complete L this gives coNP ⊆ AM_poly = NP/poly and Σ₃ = Π₃. Inverting a fold on uniform inputs is such a (V′, D′).
- **Akavia–Goldreich–Goldwasser–Moshkovitz (STOC 2006), Theorem 4:** unless coNP ⊆ AM, there is no non-adaptive reduction from deciding an NP-complete language to inverting a polynomial-time computable function. Bogdanov–Brzuska state this is not affected by the gap in the erratum.
- **Adaptive reductions.** AGGM Theorem 3 claimed: unless coNP ⊆ AM, there is no reduction (even adaptive) from an NP-complete language to inverting a *size-verifiable* function. Per Bogdanov–Brzuska (ECCC TR14-108), the proof of the general size-verifiable case "was found to be erroneous and has been retracted [AGGM10]". **Bogdanov–Brzuska give a proof of the claim:** adaptive reductions to inverting size-verifiable OWFs imply NP ⊆ coAM.
- **Feigenbaum–Fortnow (SICOMP 1993), Corollary 3.3:** if any NP-complete set is non-adaptively poly-random-self-reducible, then the polynomial-time hierarchy collapses at the third level.

**The door, stated precisely.** For the strategy to reach P ≠ NP without a collapse, the reduction from an NP-hard problem to inverting the (iterated) local function must be **adaptive, to a function that is not size-verifiable**, or **non-black-box**. Local functions are not known to be size-verifiable in general; that is an observation, not a cited result.

**The one known non-black-box instance** is Hirahara (FOCS 2018), verified.
- He says his technique is "essentially non-black-box". If Theorem 1 came from a non-adaptive black-box reduction, the Bogdanov–Trevisan techniques would give Gap_{σ,τ}MINKT ∈ coNP/poly (l.283–286).
- The non-black-box step is the one that "need[s] a source code of the errorless heuristic algorithm in order to have a short description for x" (l.403–404).
- Its worst-case problem is **GapMINKT, not known to be NP-hard**. Its conclusion lands at DistNP ⊄ AvgP, below OWF (R2).
- So the door has been passed once, for a meta-complexity problem and toward a weaker conclusion. It has never been passed for an NP-hard problem toward OWF.

## 5. The ceiling (part 3), unchanged

Proving the conjecture for any class implies OWF, and hence P ≠ NP (A0). No verified partial route exists. The deliverable is the conjecture in the survey's precise form, its smallest case (d = 3, a non-linear predicate, m = Θ(n)), and the door in §4.

## Calibration

- **The reviewer.** Its strategy and test (c) were stated accurately. The Bogdanov–Trevisan hypothesis "unless NP ⊆ coNP/poly" is equivalent, by complementation, to the verified coNP ⊆ NP/poly. The AGGM citation needs the erratum note added in §4. That is a note, not a miss: the adaptive theorem was retracted and later re-proved.
- **Me.** The pre-registration's F1 expectation held for the conjecture. The strategy result (F3) was the reviewer's addition.

## Sources (checked this run)

- Applebaum, survey: <https://eprint.iacr.org/2015/165> (ECCC TR15-027 text used)
- Bogdanov–Trevisan, SICOMP 2006: <https://lucatrevisan.github.io/pubs/redux-sicomp.pdf>
- Akavia–Goldreich–Goldwasser–Moshkovitz, STOC 2006: <http://www.cs.toronto.edu/tss/files/papers/AGGM.pdf>
- Bogdanov–Brzuska, ECCC TR14-108: <https://eccc.weizmann.ac.il/report/2014/108/>
- Feigenbaum–Fortnow, SICOMP 1993: <https://lance.fortnow.com/papers/files/rsr.pdf>
- Impagliazzo–Rudich, STOC 1989: <https://cseweb.ucsd.edu/~russell/secret.ps>
- Naor–Reingold (Luby–Rackoff restated): <https://eprint.iacr.org/1996/011>
- Hirahara, ECCC TR18-138: <https://eccc.weizmann.ac.il/report/2018/138/>
- Goldreich, ECCC TR00-090: <https://eccc.weizmann.ac.il/report/2000/090/> (text not extractable; UNVERIFIED)
