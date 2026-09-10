# A1: the bottom pair. Report

*Run 2026-09-10 on branch `a1-bottom-pair`, against the pre-registration (accepted, with guard g12: an instance counts only under a propositional pair formulation taken from a source). g1, g5, g8, g9, g10, g11 and g12 apply. Most statements are verified from the text of Pudlák, *Reflection principles, propositional proof systems, and theories* (arXiv:2007.14835); line numbers refer to that text. Derivations and formulations of mine are marked.*

## Outcome: **B3**, with a precisely stated B2 candidate

- **At the top of the ladder the propositional pair form exists in the source (g12 met).**
- **At the bottom, the *consistency* form degenerates.** Resolution proves its own consistency cheaply. The object that works there is *reflection*, and its self case is a known exponential lower bound.
- **The lowest verified pair condition** is Res(k+1) p-proving the reflection principle for Res(k), for k ≥ 2.
- **The pair-form lower bound for that pair is not found** (g8), so the outcome is B3, *open at the lower bound*. The formulation itself is sourced.
- A B2 route exists with two unverified steps (§4).

Priors: mine B3 50; the reviewer's B3 45.

## 1. The propositional pair form: what the sources state (g12)

- **The propositional objects (verified, l.387–391).** con_{P,m} := ¬prf_{P,m,n₀}(x⃗, ⌈⊥⌉), the local reflection principle applied to ⊥, which "expresses the consistency of the proof system". rfn_{P,m,n} is the reflection principle.
- **At the top: the pair form for theory-induced systems (verified, Corollary 4.11).**
  - For T = S¹₂ + A (A a true ∀Σ^b_0 sentence) and S = T + Con_T, these are equivalent: "1. T-proofs of Con_S(n̄) can be constructed in time polynomial in n. 2. The weak system of S polynomially simulates the strong system of S."
  - The proof uses S¹₂ ⊢ Con_S(n̄) ≡ Taut(con_{Q_S,n}), which is the **propositional translation** of the first-order pair statement.
  - So **g12 is met at the top**: the uniform CON-type pair statement is equivalent to a proof-system simulation statement, and Pudlák connects "a conjecture about proof complexity of finite consistency statements" with it (introduction, l.126–130).
- **Consistency gives reflection only in strong systems (verified).** Corollary 3.2: "Let P be an extension of CF. Then P-proofs of the propositions rfn_{P,m,n} … can be constructed in polynomial time from P-proofs of propositions con_{P,m}." Here CF is Circuit Frege (Jeřábek). Below CF the two principles can separate.

## 2. At the bottom, the consistency form degenerates

**Proposition 3.9 (verified):** "There exists a polynomial p such that for every nontautology φ, and m ≥ n, ¬prf_{Res,m,n}(x⃗, ⌈φ⌉) has a Resolution proof of length at most p(m)."

⊥ is a non-tautology, so **con_{Res,m} has polynomial-length Resolution proofs**. *(Immediate from the verified statement; the instantiation is mine.)* Resolution proves its own finitistic consistency cheaply, so a consistency-based finite Gödel theorem has no content at this rung.

**Flag R, proved.** Reflection gives consistency: instantiate rfn_P at φ = ⊥, as Pudlák does at l.387–391. A theory or system proving the reflection of S therefore proves con_S. At the bottom the implication does *not* reverse (§1), and reflection is the stronger, harder principle.

## 3. With reflection, the bottom rung has a known self case and a verified pair condition

- **The self case, known (verified):**
  - *Theorem 3.12* (Atserias–Bonet): "Res-proofs of the reflection principle of Res have size ≥ 2^{n^ε} for some ε > 0."
  - *Theorem 3.11*: the same for Cutting Planes.
  - *Corollary 3.8*: "There is no subexponential upper bound on the proofs of the Res-local reflection principle for tautologies in Res."
- **The lowest verified pair condition (verified, l.753–754):** "3. For every k ≥ 2, Res(k + 1) provably p-proves the reflection principle for Res(k), Atserias and Bonet [1]."
- **Stated as "probably true", not verified (l.740–745):** "F_{d+1} provably p-proves the reflection principle for F_d" (Beckmann et al., proof idea only). This would put the pair condition at (Res = F₀, F₁).
- **Open, per Pudlák, Problem 1:** "Does F_d p-prove its reflection principle for d ≥ 1?"

**The reflection pair form (my formulation, the most conservative the sources support):**

> *If T provably p-proves rfn_S, then S has no polynomial-size proofs of rfn_T.*

**The smallest open instance under it (verified pair condition; the lower bound not found, g8):**

> **Res(2) has no polynomial-size proofs of the reflection principle for Res(3).**

It is not implied by Theorem 3.12, because Res(2) is stronger than Res and lower bounds do not transfer upward.

## 4. A B2 candidate: two unverified steps

**The pair (Res, CF).**
- **Step 1.** Theorem 2.3 (verified): "If S¹₂ proves a ∀Σ^b_0 sentence A, then CF provably p-proves [[A]]_n." So *if* S¹₂ proves the soundness of Resolution as a ∀Σ^b_0 statement for bounded proofs, CF provably p-proves rfn_{Res}, which is the pair condition. **UNVERIFIED:** no reached source states that S¹₂ proves Resolution's soundness (g10).
- **Step 2, the restriction lemma (mine, unproved).** Resolution p-proves prf_{Res}(x, φ) → prf_{CF}(t(x), φ) for a syntactic translation t of resolution proofs into CF-proofs. Then a Resolution proof of rfn_{CF} would yield one of rfn_{Res}, contradicting Theorem 3.12.
- **Result, if both steps hold.** Res ⊬_poly rfn_{CF}, the first rung of the reflection form of the finite Gödel theorem, derived from a known lower bound.
- **Not claimed.** Both steps are unverified (g5). Step 2 depends on the encoding. This is the B2 candidate the ruling asked to be checked with suspicion, stated so that each step can be checked separately.

## 5. What this says about the ladder

At the bottom, the finite Gödel theorem changes form:
- **consistency is cheap** (Proposition 3.9);
- **reflection is hard**, with a known self case (Theorem 3.12), a verified pair condition one rung up (Atserias–Bonet), and an open pair instance (§3).

The first rung is a lower bound for Res(2) on Res(3)'s reflection principle, or, through §4, possibly for resolution on Circuit Frege's. It is a concrete tautology family for a weak system, within reach of the known techniques (feasible interpolation, as in the proofs of Theorems 3.11–3.12).

## Calibration

- **The reviewer:**
  - its g12 guard was exactly the right first check, because the formulation differs by rung;
  - its memory claim that "consistency statements of stronger systems are a standard hard family for resolution" is **contradicted for consistency and confirmed for reflection**. It was flagged as memory and counted for nothing, so this is a note, not a miss.
- **Me:** Flag T was right and decisive, Flag R held, and my B3 prior held.

## Sources

- Pudlák, *Reflection principles, propositional proof systems, and theories*: <https://arxiv.org/abs/2007.14835> (text: l.118–136, 168–189, 270–280, 380–412, 486–568, 610–665, 740–760, 818–850, 1026–1070)
- Atserias–Bonet, Information and Computation 189 (2004): statements as quoted by Pudlák (Theorem 3.12; l.753–754). The primary abstract page was blocked.
