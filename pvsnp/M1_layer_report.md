# M1: the metamathematical layer, mapped. Report

*Run 2026-09-10 on branch `m1-layer`, against the pre-registration (accepted, with the reviewer's addition of the per-system Π₁ layer). g1, g8 and g9 apply. "Verified" means checked against the source text or its official abstract. "Secondary" means verified in a survey's restatement, with the primary text not reached. Derivations of mine are marked.*

## Outcome: **L2**

The map is complete in shape. Three items rest only on verified restatements, and one is **not found**:
- Ben-David–Halevi: secondary, via Aaronson's P =? NP survey.
- Kurtz–O'Donnell–Royer: secondary, via Aaronson's independence survey.
- Razborov 1995, the S¹₂ half: secondary.
- Krajíček's generator conjecture: **not found** (g8).

No item refutes a premise of M2, so there is no L3. G3 ("every hardness sentence is Π₂") is **refuted at the per-system level**, with the two precision points in §2. Priors: mine L2 35; the reviewer's L2 40.

## 1. The layer, on one page

**Objects:**
- **Proof system** (Cook–Reckhow, JSL 1979, Definition 1.3, verified): a polynomial-time computable f from strings onto L. It is *polynomially bounded* iff there is a polynomial p such that every y ∈ L has an x with f(x) = y and |x| ≤ p(|y|).
- **Theories.** Bounded arithmetic, with S¹₂ ⊆ T¹₂ ⊆ S²₂ ⊆ T²₂ ⊆ … (Aaronson, *Is P vs NP formally independent?*, l.545–548, secondary).
- **Hardness tautologies:**
  - Circuit_n := "SAT_n requires circuits of size n^{log n}" (Aaronson, independence survey §4.1, verified);
  - generator tautologies τ_b(g) := "G_n(x) ≠ b" for b outside the range of G (Alekhnovich–Ben-Sasson–Razborov–Wigderson, abstract, verified; Razborov, Annals 2015, abstract, verified).
  - The tautologies "truth table f has no small circuit" are true exactly on MCSP's No-instances, R2's object, now as tautologies.

**Verified theorems, each with its logical form (g9):**

| # | Statement | Form | Status |
|---|---|---|---|
| T1 | **Cook–Reckhow.** "NP is closed under complementation if and only if TAUT has a polynomially bounded proof system" (Proposition 1.4, l.140–146) | NP ≠ coNP is **Π₂** once the inner quantifier over proofs is bounded (my classification) | verified |
| T2 | **P ≠ NP is Π₂:** ∀M ∈ T, p ∈ P ∃x (M(x) ≠ 3SAT(x) ∨ M(x) runs for > p(\|x\|) steps) | Π₂ | verified (Aaronson P =? NP survey, l.744–747) |
| T3 | **Gödel's move is only for Π₁:** "If a Π₁-sentence … is independent of ZF, then it's true … this line of reasoning doesn't apply to Π₂-sentences like P ≠ NP" | meta | verified (same survey, footnote 25) |
| T4 | **Ben-David–Halevi.** If P ≠ NP is unprovable in PA + Π₁ (PA plus all true Π₁ sentences), then NP-complete problems are solvable in time n^{f⁻¹(n)} for any f in the Wainer hierarchy, "for infinitely many input lengths n", including n^{α(n)} with α the inverse Ackermann function. By McCreight–Meyer it cannot give n^{β(n)} for *every* unbounded β. | hypothesis about Π₂ provability; conclusion Σ-type, holding infinitely often | **secondary** (Aaronson survey l.1388–1422; Technion TR 714 not reached) |
| T5 | **Razborov 1995.** "If strong pseudorandom generators exist then the statement 'α encodes a circuit of size n^{log* n} for SATISFIABILITY' is not refutable in S²₂(α)." For S¹₂, a weaker assumption suffices. | unprovability of a lower bound in bounded arithmetic | S²₂ **verified** (Izvestiya, official abstract); S¹₂ **secondary** (Aaronson §4.1, l.555–559) |
| T6 | **Pich–Santhanam (FOCS 2019).** Unconditionally, propositional proof systems "cannot efficiently show that truth tables of random Boolean functions lack polynomial size non-uniform proofs of hardness"; assuming Rudich's conjecture, the same holds for random k-CNFs of linear density. Read as a natural-proofs analogue in proof complexity. | per-system hardness of meta-level tautologies | verified (abstract) |
| T7 | **Per-system hardness of generator tautologies.** ABRW: generators hard for Resolution, Polynomial Calculus and PCR "under certain circumstances". Razborov (Annals 2015): a generator with m ≥ 2^{n^{Ω(1)}} hard for Res(ε log n), and "Res(log log N) does not possess efficient proofs of NP ⊄ P/poly". | per-system, Π₁ at a fixed bound (§2) | verified (abstracts) |
| T8 | **Kurtz–O'Donnell–Royer** (and Hartmanis): a computable oracle O such that P^O vs NP^O is independent of ZF *no matter which Turing machine specifies O* | a relativized independence result | **secondary** (Aaronson independence survey, l.353–362) |

**Not found (g8):** a verified statement of *Krajíček's conjecture* that some generator is hard for every proof system, or for Frege. ABRW's text refers to his notions (s-iterability) with unresolved references. The search is recorded; the conjecture stays **UNVERIFIED**.

**The fixed point, circled (T4):** if P ≠ NP is *true* but *unprovable in PA + Π₁*, then NP is "almost" polynomial, infinitely often. Unprovability has computational content in the direction of easiness. It works because P ≠ NP, although Π₂, "can be extremely well approximated by Π₁-sentences" (the restatement of Ben-David–Halevi).

## 2. The per-system Π₁ layer, stated precisely (the reviewer's addition; my derivations)

**Claim 1 (Π₁ at a fixed bound).** Fix a Cook–Reckhow proof system P (a polynomial-time f), a family τ_n, an explicit time-constructible bound s(n), and n₀. Then

  H_{P,s} := ∀n ≥ n₀ ∀π with |π| ≤ s(n): f(π) ≠ τ_n

is **Π₁**. The quantifier over π is bounded by a computable bound and the matrix is decidable, so H_{P,s} is a single unbounded universal over a decidable predicate. ∎

**Precision (a).** "P has no *polynomial-size* proofs of τ_n" quantifies over every exponent c: ∀c ∀n ≥ n₀(c) … or ∀c ∃^∞n …. That is **Π₂ or higher, not Π₁**. The Gödel move is available only at a *fixed explicit* superpolynomial bound, such as s(n) = n^{log n}, which already rules out polynomial boundedness on τ.

**Claim 2 (the Gödel move, with its exact hypothesis).** If T is **Σ₁-complete** (it proves every true Σ₁ sentence, as PA and even Robinson's Q do) and T ⊬ ¬H_{P,s}, then H_{P,s} is true.
- *Proof.* ¬H_{P,s} is Σ₁. If it were true, T would prove it. ∎
- **Precision (b).** The ruling said "Σ₁-sound". The move needs Σ₁-*completeness*; Σ₁-soundness is the converse property.

**Claim 3 (the union).** Quantifying over all proof systems, "no P is polynomially bounded" is **NP ≠ coNP** (T1), which is Π₂ and implies P ≠ NP. So:
- the Π₁ objects live per proof system and per explicit bound;
- the Π₂ residue is their union.

This is the structure the ruling predicted, with (a) and (b) attached.

## 3. What this hands to M2 (for its own go)

- **G3 at the per-system level is refuted.** Π₁ hardness sentences H_{P,s} exist, and the Gödel move applies to them under Σ₁-completeness.
- **What remains is assembly.** How do Π₁ layers assemble toward the Π₂ union? Ben-David–Halevi is the one verified theorem that relates unprovability of the union to computation.
- **Arm (i)** of M2's target, unprovability of ¬H from the hardness H itself, has its nearest verified instances in T5, T6 and T7. Each one requires an assumption (strong PRGs, Rudich's conjecture) or is limited to weak systems.

## Calibration

- **The reviewer:**
  - *Kurtz–O'Donnell–Royer*, named from memory, exists. Its content is a representation-independent *oracle* independence result, not a relative or strengthening of Ben-David–Halevi, which is where it was placed. That is a premise miss, the **eighth**.
  - "Σ₁-sound" should be Σ₁-complete (precision b). That is a note.
  - The per-system Π₁ layer was right, with precision (a).
- **Me:** the pre-registered L2 risk (access to 1990s papers) materialized as expected.

## Sources

- Cook–Reckhow 1979: <https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf> (text)
- Aaronson, *P =? NP*: <https://www.scottaaronson.com/papers/pnp.pdf> (text)
- Aaronson, *Is P versus NP formally independent?*: <https://www.scottaaronson.com/papers/indep.pdf> (text)
- Razborov 1995, Izvestiya: <https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=im&paperid=9&option_lang=eng> (abstract)
- Pich–Santhanam, FOCS 2019: <https://conferences.computer.org/focs/2019/pdfs/FOCS2019-7pBwCpNH4Mz2L4MJWVl6Xp/56iA2dcOxsIRH4mhUMnHsF/7fFuY7OZO3pjLa3VT5aN86.pdf> (text)
- Alekhnovich–Ben-Sasson–Razborov–Wigderson: <https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/RAZBOROV/GENERATOR/FINAL/abrw00.pdf> (text)
- Razborov, Annals 2015: <https://annals.math.princeton.edu/2015/181-2/p01> (abstract)
- Ben-David–Halevi, Technion TR 714: not reached (secondary only)
- Kurtz–O'Donnell–Royer, IPL 1987: not reached (403/404; secondary only)
