# M3: the turnaround at the object that survives. Report

*Run 2026-09-10 on branch `m3-turnaround`, against the pre-registration (accepted, with the reviewer's precision: three distinct objects). g1, g8, g9, g10 and g11 apply. "Verified" means checked against the source text or official abstract. Derivations of mine are marked and proved.*

## Outcome: **T3, at the theory step, before explicitness**

The turnaround fails at the first step that needs a claim about a *theory's* provability, the third object, and it fails in a specific way:
- the verified theorems of that kind point the **wrong way** for Gödel's move;
- the direction the move needs is **equivalent to the lower bound itself**, so it gives no leverage unless the sentence has a diagonal fixed point, and hardness sentences have none.

Explicitness is a *second* obstruction, met only if the first is passed. Explicit forms of the unprovability exist only conditionally.

Priors: mine T3 35; the reviewer's T3 35, after moving to mine. Both of us favoured T1. T3 occurred through Flag G.

## The three objects (the reviewer's precision, used as labels)

| Label | Object | Truth status / form |
|---|---|---|
| **O1** | a tautology τ, e.g. tt(f_n, s), "f_n has no circuit of size s" | true by definition when it is a tautology |
| **O2** | a length sentence H_{P,s}(τ), "P has no proof of τ of size ≤ s" | Π₁ at a fixed explicit bound s (M1, Claim 1) |
| **O3** | a theory T's provability of H or of ¬H | where Gödel's move acts, given Σ₁-completeness (M1, Claim 2) |

## (i) Pich–Santhanam (FOCS 2019) stated exactly (verified, paper text)

- **Rudich's conjecture, as they define it:** "For any proof system R verifiable in polynomial size, most Boolean functions on n bits do not have short (i.e., poly(2ⁿ)) size R-proofs of hardness." Here "most" means a 1 − 1/N^{ω(1)} fraction of functions on n = log N bits, with truth tables of length N.
- **Theorem 1 (unconditional):** "Rudich's Conjecture does not admit feasible propositional proofs." That is, "there is a propositional proof system R with polynomial advice such that no propositional proof system S can prove lower bounds on the size of R-proofs for most circuit lower bound tautologies". Their footnote extends it to systems S that take polynomial advice.
- **What "feasible proofs" means here:** S must efficiently prove lb_R(tt(f_n, n^d), m^d) for a 1 − o(1) fraction of truth tables (their definition, l.570–580).
- **Which objects it concerns:** the unprovable formulas are **O1** tautologies whose *content* is an **O2** statement about R. The theorem is an **O2** statement about S. **It says nothing about O3.**

## (ii) The turnaround, attempted step by step (g9, g11)

| Step | Object | Claim | Status |
|---|---|---|---|
| S1 | O1 | Fix τ_n = tt(f_n, s) for a family f_n | fine; true when f_n is hard |
| S2 | O2 | H := H_{P,s}(τ), "P has no s-size proof of τ", is Π₁ | M1 Claim 1; *length* (g11) |
| S3 | O2 | Pich–Santhanam: for *most* f, no S proves lb_R(tt(f)) efficiently | verified; *length*, about random f |
| **S4** | **O3** | Gödel's move needs **T ⊬ ¬H** for a Σ₁-complete T | **no source**: first failing step |

**Why S4 fails, with the verified theorems of kind O3:**
- **Razborov 1995:** if strong PRGs exist, S²₂(α) cannot *refute* "α encodes a circuit of size n^{log* n} for SAT". That is, **T ⊬ H** (the lower bound). Wrong direction.
- **Pich–Santhanam (STOC 2021), verified from the text,** unconditional and for *any* nondeterministic polynomial-time M: T₀APC¹ (containing PV₁) cannot prove "for every n > n₀ and every co-nondeterministic circuit D of size ≤ 2^{n^δ}, there are 2ⁿ/n inputs xᵢ with D(xᵢ) ≠ M(xᵢ)". Again **T ⊬ H**. Wrong direction.
- **Krajíček–Oliveira (arXiv:1605.00263), abstract as quoted:** "for every integer k ≥ 1 there is a language L ∈ P such that it is consistent with Cook's theory PV that L ∉ Size(n^k)", so PV cannot prove "L ∈ Size(n^k)". This is the **right direction** (T ⊬ ¬H), but the upper bound is **Π₂** (∀n ∃C), where the Gödel move is unavailable (M1, T3).

**Claim (mine, proved): at a fixed bound, the right direction is equivalent to the lower bound.** Let H be Π₁ (a lower bound at a fixed explicit bound), and let T contain Robinson's Q and be Σ₁-sound. Then **T ⊬ ¬H ⟺ H**.
- *Proof.* ¬H is Σ₁. If H is false, ¬H is a true Σ₁ sentence, and Q (hence T) proves it; this is Σ₁-completeness of Q, a standard fact stated here without citation. If H is true, ¬H is a false Σ₁ sentence, and a Σ₁-sound T does not prove it. ∎
- **Consequence.** Establishing S4 for an H at a fixed bound is *the same problem* as proving H. Gödel's leverage in the incompleteness theorem comes from the diagonal fixed point: G ↔ ¬Prov_T(⌜G⌝), so unprovability is derived from consistency without first knowing truth. Hardness sentences H carry no such fixed point, so the move becomes a restatement, not a lever. **S4 is the first failing step, and the failure is at O3.** That is outcome T3.

## (iii) Derandomization: explicit families with Pich–Santhanam-type unprovability (g8)

- **Conditional, explicit.** Pich–Santhanam Theorem 9, which restates Krajíček–Pudlák (verified): for P, Q simulating EF, "P does not admit p-size proofs of lb_Q(φ_n, n^{log n}) for any sequence of propositional formulas φ_n … unless every sequence of tautologies with p-size Q-proofs admits n^{O(log n)}-size P-proofs". It holds for *every* explicit φ_n, but its condition is a proof-system separation of the same kind, so it is circular at the smallest scale. For P = Q it says nothing, consistent with Davis–Robere.
- **Conditional, explicit-generated.** Pich–Santhanam Theorem 3 (verified), assuming Rudich's conjecture and that E lacks sub-exponential nondeterministic circuits: either EF does not efficiently prove tt(f_n, s) for *any* sequence {f_n} with s = n^{ω(1)}, or there are polynomial-time-generated sets S_N whose members are mostly tautologies requiring EF-proofs of size N^{ω(1)}, "and yet no propositional proof system S can prove in size N^c that for most φ ∈ S_N, φ requires EF proofs of size at least N^c".
- **Unconditional and explicit: not found.** Searches recorded: Pich's later work, Krajíček's generator papers, and "explicit / derandomized" queries. Related conditional result: arXiv:2405.02232 (abstract verified), linking Implicit EF proving a derandomization assumption to #P ⊄ FP/poly.

## (iv) The smallest form at this layer, two sentences

1. **A derandomized Pich–Santhanam.** An explicit, polynomial-time-generated family φ_n and a proof system R such that no proof system S has polynomial-size proofs of lb_R(φ_n, ·), **unconditionally**. Known only under a separation of the same kind (Theorem 9) or under Rudich plus circuit hypotheses (Theorem 3).
2. **The lever the Gödelian reading actually needs.** A lower-bound sentence with a **diagonal fixed point**, one whose unprovability in T follows from T's consistency the way G's does. None is known. Without one, "T ⊬ ¬H" for a Π₁ H is equivalent to H (the Claim above), and the move is not a lever.

## The observation, checked against this layer

Pich–Santhanam (random truth tables: the unprovability holds) against Davis–Robere (named PHP families: a system proves its own lower bounds). This is consistent with "the obstruction concerns the typical, not the named", the third instance of the observation recorded in M3's pre-registration. Gödel's move needs a *name* (an explicit f makes H Π₁), which matches the reviewer's expectation. But the step that fails first is the theory step, not the name.

## Calibration

- **The reviewer:** its three-object precision located the failure exactly. Its T1 expectation did not occur; T3 did, through Flag G. That is an outcome, not a premise miss.
- **Me:** Flag G was right. My T1 prior (55) was also wrong.

## Sources (checked this run)

- Pich–Santhanam, FOCS 2019: text (Theorems 1, 3, 7, 9; definitions at l.185–200 and 570–590)
- Pich–Santhanam, STOC 2021: <https://users.ox.ac.uk/~coml0742/papers/stoc-final.pdf> (text: abstract and Theorem 1)
- Krajíček–Oliveira: <https://arxiv.org/abs/1605.00263> (abstract as quoted)
- Razborov 1995: official abstract (M1)
- arXiv:2405.02232 (abstract)
