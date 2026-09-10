# R3-fold: pre-registration

*Drafted 2026-09-10 on branch `r3-fold`, on the author's go, for the reviewer's ruling before any work. It is a document with no Lean. It reopens the program closed in `R_program_closeout.md`, on the reviewer's user's objection: the density barrier covers arguments built from specific compressible strings, not measure-level candidates. The reviewer records its "program closed" ruling as its seventh premise miss.*

## The candidate, as proposed

A **fold** Π : Ψ → Φ is cheap to compute and erases information (ΔH). Checking a fold's output at each layer is local, and unfolding needs a search over the erased entropy. Composing folds accumulates that entropy. The proposed conjecture: for a natural class of explicit folds, such as iterated local compression maps with a fixed short description, the description does not allow the erased entropy to be recovered faster than 2^{Ω(ΔH)}.

## Findings made while drafting, before any run (flags, not rulings)

**Flag A: the conjecture as stated is false.**
- *Counterexample.* The projection p(x, y) = x (|x| = |y| = n) is a 1-local compression map with a constant-size description, and it erases n bits. It is trivially invertible on every input: given x, output (x, 0^n).
- So "no inversion faster than 2^{Ω(ΔH)}" fails for a member of the proposed class. ∎
- More generally, **ΔH is neither sufficient nor necessary for one-wayness.** Projections erase a lot and are easy to invert. One-way *permutations*, if they exist, erase nothing (ΔH = 0) and are hard.
- Erasure increases the number of preimages, and all an inverter must do is find *one* preimage. So the thermodynamic parameter is not the cryptographic one.

**Flag B: the target is wrong.**
- The erased bits of a compressing map cannot be recovered at all: that is information-theoretic, not computational.
- One-wayness asks for *some* preimage of f(x), on average over x.
- The conjecture must be restated with that target. Once it is, ΔH drops out of the hardness bound.

**Flag C: a correction to the ruling's citation.** According to its abstract (verbatim check against the paper is deferred to the run), Impagliazzo–Rudich (STOC 1989) is a **black-box separation**:
- it gives strong evidence that "one-way permutations ⇒ secret key agreement" cannot be proved by standard techniques;
- relative to a randomly chosen permutation oracle, that permutation is strongly one-way in a provable, information-theoretic way;
- if P = NP, no key agreement is secure in that setting.

It is not a query lower bound for inverting a random function. The ruling's point stands, that oracle hardness doesn't transfer because of relativization, but it rests on a different theorem. The random oracle's own one-wayness is the simple part.

**Flag D: the barriers apply to proof strategies, not to conjectures.**
- Relativization (Baker–Gill–Solovay) and natural proofs (Razborov–Rudich) constrain *how* a lower bound can be proved, not whether a candidate one-way function is one-way.
- So tests (a) and (b) in part (2) can only be applied to a *named proof strategy* for the conjecture.
- Without a strategy they are vacuous. The pre-registration therefore requires one.

## The repaired candidate, and its expected identity

With Flags A and B applied, the natural "explicit fold with a short description" becomes a **local function that preserves length**:
- f_{G,P}(x)_i = P(x restricted to the neighbourhood N_G(i));
- P is a fixed d-ary predicate and G is a bipartite expander of right-degree d, with n → n.

That is **Goldreich's candidate one-way function** (ECCC TR00-090 / ePrint 2000/063, to verify). Its hardness for random or expander graphs and suitable predicates is the subject of **Applebaum's survey**, *Cryptographic Hardness of Random Local Functions* (Computational Complexity 25(3), 2016; ECCC TR15-027), also to verify. Inverting it is a planted constraint-satisfaction problem.

**Expected outcome: F1.** The repaired fold is a known candidate under another name. Two questions remain:
- **Composition.** Does *iterating* folds add a reduction that single local functions lack? For example, does the composition of two d-local maps inherit one-wayness from either, or amplify it?
- **The first non-trivial case.** What is the smallest locality, predicate and output length at which the known attacks stop? This is "make it smaller" applied to the base fold, and it is read off the survey, not invented.

## Part (1): the map of what is already a theorem

Each item is to be verified under g1 in the run.

| Item | Claimed statement | Source to check |
|---|---|---|
| Amplification | weak OWF ⇒ strong OWF | Yao 1982; Goldreich, *Foundations of Cryptography* vol. 1, Theorem 2.3.2 |
| Composition | PRF ⇒ PRP in 3 Feistel rounds; strong PRP in 4 | Luby–Rackoff 1988 |
| Black-box arrow | a random permutation oracle is one-way; key agreement is black-box-separated from it | Impagliazzo–Rudich 1989 (Flag C) |
| Local candidates | Goldreich's function; attacks and positive results | Goldreich 2000; Applebaum 2016 survey |

One point is circled as unproved: **the base fold**, an explicit map with a short description that is weakly hard to invert on average. Everything above it composes; nothing below it is known.

## Part (2): the precise conjecture and its tests

- **Conjecture.** State it in the survey's language: family, predicate class, locality, output length, and the adversary's time and success probability.
- **Tests, applied to a named proof strategy (Flag D).**
  - **(a) Relativization.** Does the strategy use only oracle access to f? If so, it relativizes and proves nothing white-box.
  - **(b) Naturalness.** Would it yield a constructive, large property that distinguishes f's outputs, or its truth tables, from random? If so, it is a natural proof, and Razborov–Rudich applies to the lower bound it would imply.
- The strategy must name the white-box feature it uses. **If no strategy is proposed, the run records "no strategy; tests vacuous" and stops at F1 or F3.**

## Part (3): the ceiling

Proving the conjecture for any class implies OWF, and hence P ≠ NP (A0). No verified partial route exists. Hirahara's worst-to-average result lands below OWF and is errorless (R2). The deliverable is the conjecture stated precisely enough that its first non-trivial case can be identified, plus the list of what "first non-trivial case" means: the smallest locality d, the smallest predicate, output length n, and the adversary class.

## Outcomes

| Code | Outcome |
|---|---|
| **F1** | The repaired conjecture is a known one (expected: Goldreich / random local functions). Say whether folding (composition) adds a reduction. |
| **F2** | It is new and survives both tests for a named strategy. R4 attacks its smallest case. |
| **F3** | It fails a test, or is false as stated. Record which, and the white-box feature it lacks. The *unrepaired* ΔH form is already F3 by Flag A. |

**Priors (mine), for the repaired form:** F1 75 / F3 20 / F2 5. **Reviewer's (for the proposal):** F1 50 / F3 35 / F2 15.

## Guards

- **g1:** no citation from memory; UNVERIFIED counts as none. Every row of the part (1) table is checked against the paper text.
- **g5:** every counterexample or test verdict comes with a proof.
- **g6:** the barrier tests apply only to named strategies (Flag D).
- **g7:** RE language is confined to the fold's description and one sentence on contribution.

## Calibration

The reviewer's seventh premise miss ("program closed", treating the density barrier as covering measure-level candidates) is recorded here, at its request.

## Sources found while drafting (search results; the abstract-level facts are to be verified in the run)

- Impagliazzo–Rudich, STOC 1989: <https://dl.acm.org/doi/10.1145/73007.73012>
- Goldreich, *Candidate One-Way Functions Based on Expander Graphs*: <https://eprint.iacr.org/2000/063>, <https://eccc.weizmann.ac.il//eccc-reports/2000/TR00-090/index.html>
- Applebaum, *Cryptographic Hardness of Random Local Functions (Survey)*: <https://eprint.iacr.org/2015/165>, <https://link.springer.com/article/10.1007/s00037-015-0121-8>
