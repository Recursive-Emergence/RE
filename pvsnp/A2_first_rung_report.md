# A2: the first rung, (Res, CF). Report

*Run 2026-09-10 on branch `a2-first-rung`, against the pre-registration at 408f852 and the reviewer's acceptance (Flags P, E, Q adopted as guards; reviewer's priors C3 40 / C1 35 / C2 25). g1, g5, g8, g9, g10, g11, g12 applied. Every step of ours below is a proof; every outside fact is quoted from a text read in this run, with its location.*

## 0. Outcome in one paragraph

**Proposed outcome: C2.** Res ⊬_poly rfn_CF is proved here, elementarily, and **without Theorem 3.12**. The pre-registered route, the translation lemma (b) plus the composition (c) through Atserias–Bonet, was not needed and was not run.

The proof is a *reflection ⇒ simulation* lemma for Res(k), done by restriction and literal substitution. Its content is this: if Res(k) had short refutations of the negated reflection principle of a system T, then Res(k) would have short refutations of every CNF that T refutes shortly. Instantiated with the pigeonhole principle (Haken; Buss), it gives the target.

Instantiated with the Res(k)/Res(k+1) hierarchy, it also gives **Res(2) ⊬_poly rfn_Res(3)**. That is the "smallest open instance" of A1, and it is therefore **not open**: it follows from a known separation plus this lemma. This is a correction to A1 (§6).

The method is classical: Cook–Nguyen attribute "the idea of using the Reflection Principle for p-simulation" to Cook [28]. The two instances were not found stated in the sources checked (g8: not found, which is not a novelty claim). The reviewer may prefer to rule this C1-adjacent. §7 gives the program-level readout, which matters more than the rung.

## 1. Sources read in this run (g1)

- **Atserias–Bonet, *On the automatizability of resolution and related propositional proof systems*, Inf. & Comp. 189(2) (2004).** The primary was reached this time (cs.upc.edu/~atserias/papers/autom/infocomp.pdf). Its math is in Type 3 fonts, so pages 5, 6, 8, 9, 10, 11, 14 and 15 were read as rendered images. Used:
  - the definitions of SAT^n_r and REF^n_{r,m} (pp. 5–6, 10–11);
  - Res(k) and its rules (p. 9);
  - "projection-closed" (p. 8);
  - Theorem 5 (p. 11);
  - Theorem 11 (p. 15).
- **Pudlák, arXiv:2007.14835.** Used:
  - l.160–185 (CF, "the same rules as a Frege system");
  - l.330–362 (rfn_{P,m,n} and the ∀Σ^b_0 form of Rfn_P);
  - l.566–570 and Theorem 3.12 (l.650–665);
  - Corollary 3.8 (l.536–560);
  - l.600–608;
  - the pair list (l.740–760);
  - Theorem 2.3.
- **Cook–Nguyen, *Logical Foundations of Proof Complexity*.** Used:
  - l.9844–9860: Haken and Buss;
  - §10B.5 and Notes l.26957: "The idea of using the Reflection Principle for p-simulation is from [28]", where [28] is "Stephen Cook, Feasibly constructive proofs and the propositional calculus".
- **Ben-Sasson–Nordström, arXiv:1008.1789, l.110–122**, stating the result of Segerlind–Buss–Impagliazzo [SBI04] and Segerlind [Seg05]. **Secondary.** Both primary hosts failed from here: the UCSD page fails TLS verification, which was not bypassed, and eScholarship returned a CloudFront 403. Every use below carries the tag *"[SBI04, Seg05] as stated by Ben-Sasson–Nordström"*.

## 2. The encoding: Flag E, discharged by quantifying over encodings

**Atserias–Bonet's SAT, verbatim in content (p. 10).**
- The CNF formula has variables v_1..v_n and clauses j = 1..r.
- x_{0,i,j} means "v_i appears in clause j", and x_{1,i,j} means "¬v_i appears in clause j".
- z_i means "v_i is true". z_{0,i,j} means "clause j is satisfied by the literal v_i", and z_{1,i,j} means "clause j is satisfied by the literal ¬v_i".
- SAT^n_r(x, z) consists of:
  - (1) z_{0,1,j} ∨ z_{1,1,j} ∨ … ∨ z_{0,n,j} ∨ z_{1,n,j}
  - (2) ¬z_{0,i,j} ∨ z_i
  - (3) ¬z_{e,i,j} ∨ x_{e,i,j}
  - (4) ¬z_{1,i,j} ∨ ¬z_i

The reflection principle of a refutation system f is the contradiction SAT^n_r(x, z) ∧ REF^n_{r,m}(x, y) (pp. 5–6). For Resolution, REF is clauses (5)–(18) on p. 11.

**What we assume of a REF for an arbitrary system T.** We work with the *negated* reflection principle in Atserias–Bonet's shape:

  ¬rfn^T_{n,r,m} := SAT^n_r(x, z) ∧ REF^T_{n,r,m}(x, y, u),

where REF^T is any CNF with three properties:
- **(i) separation:** its variables are the x_{e,i,j}, proof variables y and auxiliary variables u only. It shares only x with SAT.
- **(ii) completeness:** for every CNF F with n variables and r clauses and every T-refutation of F of size ≤ m, some assignment to (y, u) satisfies REF^T(⌈F⌉, y, u). Here ⌈F⌉ is F's x-code.
- **(iii) size:** its size is poly(n, r, m).

Soundness of the encoding is *not* used. If the encoding is unsound, the formula may be satisfiable, and "no short refutation" is then trivially true.

Every result below holds **for every REF^T with (i)–(iii)**. So no encoding match has to be asserted (Flag E): the only fixed encoding is Atserias–Bonet's SAT, read from the primary. Atserias–Bonet's own REF for Resolution satisfies (i) and (iii) by inspection of (5)–(18).

On (ii) for their REF, which asks for exactly m clauses with the last one empty: a refutation with fewer clauses is padded by repeating a resolution step, which (8)–(18) accept. This is a remark; nothing below depends on their REF.

## 3. The lemmas (ours; g5)

**Res(k) as defined by Atserias–Bonet (p. 9).** Lines are k-disjunctions, i.e. disjunctions of terms with at most k literals. There are three rules:
- Weakening: A ⊢ A ∨ B.
- ∧-Introduction: A ∨ l₁, B ∨ (l₂ ∧ … ∧ l_s) ⊢ A ∨ B ∨ (l₁ ∧ … ∧ l_s).
- Cut: A ∨ (l₁ ∧ … ∧ l_s), B ∨ ¬l₁ ∨ … ∨ ¬l_s ⊢ A ∨ B.

Here s ≤ k, and axioms x ∨ ¬x are allowed. Res(1) is Resolution: "Res(1) is equivalent to Resolution since the axioms and the weakening rule are easy to eliminate in this case" (p. 9).

**Lemma 1 (literal substitution).** Let σ map each variable to a literal or to a constant 0/1. For a k-disjunction A, define σ(A) as follows:
- apply σ to every literal;
- delete from each term the literals that became 1;
- delete every term that contains a 0 or a complementary pair (such a term is false);
- if some term became empty, that term is true, and σ(A) := **1**.

So σ(A) is **1** or a k-disjunction; it may be the empty disjunction, and it may contain complementary 1-terms, which are kept. If Π is a Res(k) refutation of a CNF Γ with |Π| = S, then there is a Res(k) refutation of

  σ(Γ) \ {**1**} ∪ {axioms}

of size ≤ 2S + |Γ|.

*Proof.* Induction along Π: every line A with σ(A) ≠ **1** gets σ(A) derived from the images of its premises in at most 2 steps. Premises whose image is **1** are never needed. Initial clauses map to clauses of σ(Γ) or to **1**. An axiom x ∨ ¬x maps to σ(x) ∨ ¬σ(x), which is an axiom, or to **1**. The empty line maps to itself.

- **Weakening A ⊢ A ∨ B.** σ(A ∨ B) = σ(A) ∨ σ(B). If σ(A) = **1**, the conclusion is **1**. Otherwise weaken.
- **Cut.** Let t = σ(l₁ ∧ … ∧ l_s).
  - If σ(A) = **1** or σ(B) = **1**, the conclusion is **1**.
  - If t is deleted (it has a 0 or a complementary pair), the first premise's image is σ(A); weaken it to σ(A) ∨ σ(B).
  - If t became empty (all lᵢ true), every ¬lᵢ is 0, so the second premise's image is σ(B); weaken it.
  - Otherwise t is a consistent term T′ ≠ ∅, after removing duplicates and the true literals. The images are σ(A) ∨ T′ and σ(B) ∨ ⋁_{m∈T′} ¬m (false ¬lᵢ are dropped, duplicates merge). Then Cut gives σ(A) ∨ σ(B).
- **∧-Introduction.** Let T₂ = σ(l₂ ∧ … ∧ l_s), and assume σ(A), σ(B) ≠ **1**.
  - If σ(l₁) = 0, the first premise's image is σ(A); weaken. The conclusion's term is deleted, so the conclusion is σ(A) ∨ σ(B).
  - If T₂ is deleted, the conclusion's term is deleted as well. The second premise's image is σ(B); weaken.
  - If σ(l₁) = ¬m with m ∈ T₂, write T₂ = m ∧ T₃. The conclusion is σ(A) ∨ σ(B), because its term is contradictory.
    - Weaken σ(A) ∨ ¬m to σ(A) ∨ ¬m ∨ ⋁_{q∈T₃} ¬q.
    - Cut it against σ(B) ∨ (m ∧ T₃), which gives σ(A) ∨ σ(B).
    - That is two steps.
  - If σ(l₁) = 1, the conclusion's term is T₂, and the second premise's image σ(B) ∨ T₂ is weakened to σ(A) ∨ σ(B) ∨ T₂.
  - If T₂ is empty, i.e. all of l₂..l_s are true, the conclusion's term is σ(l₁) = m. Weaken σ(A) ∨ m.
  - If σ(l₁) = m ∈ T₂, the conclusion's term is T₂; weaken σ(B) ∨ T₂.
  - Otherwise apply ∧-Introduction to σ(A) ∨ m and σ(B) ∨ T₂. The term m ∧ T₂ has at most s ≤ k literals.

Every conclusion is derived in at most 2 new lines per line of Π. ∎

**Lemma 1′ (Res).** For k = 1, the resulting Res(1) refutation uses weakening and axioms x ∨ ¬x. Both are eliminated without increasing size, by the usual subsumption induction:
- replace every line C by a clause C* ⊆ C derived by resolution alone;
- a resolution step whose pivot is missing from one premise's C* keeps that C*;
- a premise that is an axiom x ∨ ¬x makes the step's conclusion subsumed by the other premise.

So Resolution proper gets a refutation of size ≤ 2S + |Γ|.

**Lemma 2 (the SAT projection).** Let F be a CNF with clauses C_1..C_r over v_1..v_n. Define σ_F by:
- x_{e,i,j} ↦ the bit of ⌈F⌉;
- z_{0,i,j} ↦ z_i if v_i ∈ C_j, and 0 otherwise;
- z_{1,i,j} ↦ ¬z_i if ¬v_i ∈ C_j, and 0 otherwise;
- z_i ↦ z_i.

Then σ_F(SAT^n_r(x, z)) consists of the clauses C_j(z), the axioms z_i ∨ ¬z_i, and **1**.

*Proof, clause family by clause family:*
- **(1)** becomes ⋁_{v_i∈C_j} z_i ∨ ⋁_{¬v_i∈C_j} ¬z_i = C_j(z).
- **(2)** becomes ¬z_i ∨ z_i, an axiom, or ¬0 ∨ z_i = **1**.
- **(3)** becomes **1**: if the literal is present then x_{e,i,j} ↦ 1, and otherwise z_{e,i,j} ↦ 0.
- **(4)** becomes z_i ∨ ¬z_i or **1**. ∎

Flag P asked whether the substitution is a projection. **On the route taken it is one**, written out: σ assigns constants to x, y, u, and assigns σ_F's literals to the z_{e,i,j}. No formula is substituted anywhere.

**Lemma 3 (reflection ⇒ simulation for Res(k)).** Let k ≥ 1 and let T be any refutation system with REF^T satisfying (i)–(iii). Suppose Res(k) refutes ¬rfn^T_{n,r,m} in size S. Then every CNF F with n variables and r clauses that has a T-refutation of size ≤ m has a Res(k) refutation of size ≤ 2S + |¬rfn^T_{n,r,m}|. For k = 1 this is a Resolution refutation, by Lemma 1′.

*Proof.* Let (b, c) satisfy REF^T(⌈F⌉, y, u); it exists by (ii). Let σ := σ_F ∪ {y ↦ b, u ↦ c}, which is well defined by (i).
- Every clause of REF^T has all its variables among x, y, u, all of which are assigned, and it is satisfied, so it maps to **1**.
- By Lemma 2, SAT maps to F(z) plus axioms plus **1**.
- Lemma 1 turns the given refutation into a Res(k) refutation of F(z) of the stated size. ∎

## 4. The target: Res ⊬_poly rfn_CF

**Outside facts, quoted.**
- **Haken** (Cook–Nguyen l.9844–9846): "an exponential lower bound on the length of any Resolution refutation of ¬PHP^{n+1}_n".
- **Buss** (Cook–Nguyen l.9853): "polynomial size Frege proofs of PHP^{n+1}_n".
- **CF** (Pudlák l.168–170): "use circuits instead of formulas and the same rules as a Frege system with an additional rule". A Frege proof is therefore a CF proof, after coding formulas as straight-line programs, and that coding is polynomial.

**Theorem A (ours).** For every REF^CF with (i)–(iii), where a "CF-refutation of F" is a CF proof of ¬⋀F: there is no polynomial p such that Res refutes every ¬rfn^CF_{n,r,m} in size p(N), where N := |¬rfn^CF_{n,r,m}|.

*Proof.*
1. Take F_n := ¬PHP^{n+1}_n. It has n(n+1) variables and r = (n+1) + n·C(n+1, 2) = O(n³) clauses.
2. By Buss and the CF fact, F_n has a CF-refutation of size m_n = poly(n). The rewriting between ¬⋀F_n and Buss's PHP^{n+1}_n is a polynomial Frege step.
3. So N_n = poly(n) by (iii).
4. Suppose Res refuted ¬rfn^CF at size p(N_n). By Lemma 3, F_n would have a Resolution refutation of size ≤ 2p(N_n) + N_n = poly(n).
5. That contradicts Haken. ∎

**Flag Q, the measure.** The size parameter is N, the length of the reflection formula. In N the bound is exponential in n, where N = poly(n); "exponential" is Cook–Nguyen's word, and g9 means the exponent was not read. Hence it is superpolynomial in N. That is all "⊬_poly" needs, and the bound is also infinitely often, along N_n. It is stronger in form than what Theorem 3.12's primary gives (§5), even though it concerns the stronger system's reflection.

**(a) the pair condition, S¹₂ ⊢ Rfn_Res (our proof sketch; not found stated, g8).** Let x be a Res refutation of the CNF ¬y, and let a satisfy all clauses of ¬y. By induction on k ≤ (number of clauses of x), a satisfies every clause C_j, j ≤ k:
- the induction formula is sharply bounded in the codes, so length induction in S¹₂ covers it;
- for the step, a resolvent of C_i ∋ v and C_j ∋ ¬v gets a true literal from whichever premise's pivot is false under a;
- the last clause is empty and cannot be satisfied, which is a contradiction.

So S¹₂ ⊢ Rfn_Res. Rfn_P is ∀Σ^b_0 (Pudlák l.341–343), so by Theorem 2.3 (l.275: "If S¹₂ proves a ∀Σ^b_0 sentence A, then CF provably p-proves [[A]]_n"), **CF provably p-proves [[Rfn_Res]]_n**. The pair (S, T) = (Res, CF) thus has both halves:
- T provably p-proves rfn_S, in Pudlák's translation;
- S ⊬_poly rfn_T, in Atserias–Bonet's shape for every admissible REF.

These are two formulas about two different systems, so no encoding match between them is required.

## 5. Flags E and Q on Theorem 3.12, recorded though no longer used

Pudlák's Theorem 3.12 reads "Res-proofs of the reflection principle of Res have size ≥ 2^{n^ε}" and does not define n there. The primary Theorem 11 (p. 15) reads: "Let s be a parameter. For a choice of n, r, and m of the order of a quasipolynomial 2^{(log s)^{O(1)}}, every Resolution refutation of SAT^n_r(x,z) ∧ REF^n_{r,m}(x,y) requires size at least 2^{Ω(s^{1/4})}."

In the formula size N = poly(n, r, m) we have log N = (log s)^{O(1)}. So the primary bound is 2^{2^{Ω((log N)^δ)}} for some δ > 0: superpolynomial and subexponential in N, and only along the chosen parameter triples (g9).

If Pudlák's n is the graph size s, the two statements agree. If it is the formula size, the restatement is stronger than the primary. I do not infer which (g10). Pudlák's own Corollary 3.8 route, via Lemma 3.7 (Atserias–Müller, Garlík), claims an exponential global bound for rfn_Res by another road. That was not checked.

## 6. A1's "smallest open instance" is closed

**Outside fact, secondary** (Ben-Sasson–Nordström l.113–122, stating [SBI04, Seg05]): "there exists a constant ε > 0 such that for every integer k > 0 there exists a family of formulas {F_n} of arbitrarily large size n such that F_n has a R(k+1)-refutation of polynomial length n^{O(1)} but all R(k)-refutations of F_n require exponential length 2^{n^ε}."

**Theorem B (ours, modulo the secondary tag).** For every k ≥ 1 and every REF^{Res(k+1)} with (i)–(iii), Res(k) ⊬_poly ¬rfn^{Res(k+1)}. In particular, **Res(2) ⊬_poly rfn_Res(3)**.

*Proof.* This is Lemma 3 with T = Res(k+1) and the family F_n above. We have N = poly(n), and any Res(k) refutation has size ≥ 2^{n^ε}/2 − N = 2^{N^{Ω(1)}}. ∎

For k ≥ 2, the pair condition of A1's reflection pair form is the verified "Res(k+1) provably p-proves the reflection principle for Res(k)" (Pudlák l.753–754). So **every rung (Res(k), Res(k+1)), k ≥ 2, satisfies both halves of that form.** The rung (Res, Res(2)) has the lower bound (k = 1). Its pair condition is only the *p-provability* of Atserias–Bonet's Theorem 5 (p. 11: Res(2) refutations of size (nr + nm)^{O(1)}); "provably" is not verified there.

**My miss in A1.** A1 said the instance was "within reach of the known techniques (feasible interpolation, as in the proofs of Theorems 3.11–3.12)". The actual route is simpler, and it was available from sources A1 had already read: Cook–Nguyen's Haken/Buss paragraph and §10B.5.

## 7. Readout for the program (the part that matters)

**Lemma 3 empties the reflection pair form wherever the upper system is strictly stronger.** On any rung (S, T) where
- S is closed under literal substitution, and
- some CNF family has short T-refutations and only long S-refutations,

"S ⊬_poly rfn_T" is a consequence of that separation and says nothing more. That covers the Res(k) and PHP rungs here. It also covers systems extending CF, through substitution (Pudlák Lemma 2.1) and the Cook–Nguyen §10B.5 argument; that last point is a pointer, not re-proved here.

The reflection form has content of its own only where T is p-simulated by S. Two such places are known:
- the **self** rungs: Atserias–Bonet's Res ⊬ rfn_Res, and Pudlák's Theorem 3.11 for CP. These are exactly the ones that needed interpolation.
- the **top**: for strong S, "S ⊬_poly rfn_T" already follows from any superpolynomial separation of S from T. That is a separation problem, not a Gödel phenomenon.

This refines A1's readout without adding an instance. Reflection of a stronger system is defeated by **typical** hard tautologies: any separating family is restricted into it. **Consistency** is about the **named** ⊥, which no restriction reaches. I count this under A1's sixth typical-vs-named instance, not as a seventh (g12: no new sourced pair formulation).

**What remains of the finite Gödel theorem after A1 and A2:**
- **Bottom:** it is about reflection. The strictly-stronger rungs are now settled by separations (Theorems A and B). The open reflection questions are the self rungs above Resolution:
  - Res(k) vs rfn_Res(k), k ≥ 2 (not found stated, g8);
  - Pudlák's Problem 1 for F_d.
- **Top:** only the consistency form (CON^N⁺) carries content beyond separations. It stays where the M-program left it.

**Proposed next (for the reviewer's ruling): A3 at a self rung.** Does Res(2) p-prove rfn_Res(2)? Atserias–Bonet's Theorem 5 gives Res(2) short refutations of the reflection principle of *Resolution*, and Theorem 3.12 denies Resolution its own reflection. That makes Res(2)'s own self-reflection the first self rung above the one known case. The alternative is to close the bottom and return to the top's consistency form.

## 8. Priors against outcome

| | C1 | C2 | C3 |
|---|---|---|---|
| mine (pre-reg) | 35 | 30 | 35 |
| reviewer (accepted) | 35 | 25 | 40 |
| proposed | | **C2** | |

Both of us put the most weight on C3, and on Flag P specifically. The projection question did not bite, because the route that needs a projection of *proofs* (the translation t) was not needed. The only substitution is σ = constants ∪ σ_F. Flag E was dissolved by proving the result for every admissible encoding, not by matching one.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.
