# A3: finite second incompleteness, the self rung. Report

*Run 2026-09-10 on branch `a3-self-rung`, on the author's go ("Run A3, push after merge"), against the pre-registration (b933162) and its amendment at the reviewer's acceptance (f85c60e). A3 proves nothing; it verifies and maps. g1, g8, g9, g10, g11 and g12 applied. Every quotation is from a text read in this run, with its location.*

## 0. Outcome

**S2.**
- RFN^N_1 is a **∀S ∃T cross statement about first-order theories**, for Σ^b_1 reflection. It is not a self statement, and not about propositional proof systems.
- No self-rung-for-all-P statement appears in Pudlák's family.
- And none can hold as worded: the strong systems provably p-prove their own reflection (§2, rows 1–3). **S1 is refuted from a statement, not from the l.799 summary.** Under the amendment, this counts as the reviewer's ninth wrong outcome prior.

**Not S3.** Res(2)'s self rung is not found settled (g8) in Atserias–Bonet 2004, Pudlák 2020, Garlík 2020 or Cook–Nguyen. Garlík explicitly works around it (§3).

**The extension reading fails its pre-registered test, on the Frege row.** Frege has no extension, and it p-proves its own reflection (Buss, per Pudlák). §4 gives the reading the table does support. It is Pudlák's own remark, not ours.

## 1. (a) RFN^N_1, verbatim (Pudlák 2017, local text `inco.txt`)

- **The class 𝒯** (Definition 1, l.210–211): "the class of all consistent arithmetical theories that extend Buss's theory S¹₂ by a set of axioms that is decidable in polynomial time."
- **The sentences** (Definition 3, l.676–679): "The finite uniform Σ^b_1 principle is the sequence of sentences Σ^b_1RFN_T(n̄), n ∈ ℕ, defined by ∀e, u, x, z(|e|, |u|, |x|, |z| ≤ n̄ ∧ Pr_T(u, ⌈µ₁(ē, x̄, z̄)⌉) → µ₁(e, x, z))." Here µ₁ is a universal Σ^b_1 formula (l.668–672).
- **Conjecture RFN^N_1** (l.719–721): "For every S ∈ 𝒯, there exists T ∈ 𝒯 such that the lengths of S-proofs of Σ^b_1RFN_T(n̄) cannot be bounded by p(n) for any polynomial p."
  - Quantifier form (g9): ∀S ∃T, first-order theories, Σ^b_1 reflection restricted to proofs and parameters of length ≤ n. **The "1" is Σ^b_1**: a restriction on the reflected formulas.
- **CON^N ⇒ RFN^N_1** (l.722–726): "When α is 0 = 1, then Σ^b_1Rfn^α_T(n̄) is equivalent to Con_T(n̄) … by Lemma 3.9, there exists a polynomial q such that Σ^b_1RFN_T(q(n)) → Con_T(n̄) has an S¹₂-proof of length polynomial in |n|. Consequently, Conjecture CON^N implies Conjecture RFN^N_1." **Verified.**
- **RFN^N_1 ⇒ NP ≠ coNP**, by the contrapositive, Proposition 3.11 (l.731–733): "If NP=coNP, then there exists S ∈ 𝒯 such that for all T ∈ 𝒯, the lengths of S-proofs of Σ^b_1RFN_T(n̄) can be bounded by p(n) for some polynomial p."
  - **Verified as stated.** Pudlák's proof is marked "a sketch of a proof in more detail" (l.740). It pads true Σ^b_1RFN_T(n̄) instances in as axioms, with an NP-time acceptor, "regardless whether or not T is consistent".
- **The self statement in the same paper** is §3.3 (l.790–800; see also l.50–52, "a lower bound of the form n^ε for some ε > 0", where the extraction drops the superscript): Friedman's lower bound on T-proofs of Con_T(n̄). It is polynomial, and Pudlák offers it as another reading of "the finite Gödel theorem". This agrees with M5's record: the family "has no superpolynomial self-case conjecture".

**So the M5 chain CON^N ⇒ RFN^N_1 ⇒ NP ≠ coNP is cross-form throughout.** Its middle term is not the self rung. The reviewer's framing "A3 is the self rung, with RFN^N_1 as the frame" does not survive (a).

## 2. (b) The divide: which systems p-prove their own reflection principle

| # | System | Self-reflection | Quantifier form / measure | Source (read in this run) |
|---|---|---|---|---|
| 1 | Extensions of CF (CF, EF, ER, …) | **p-proves, provably** | poly-time constructible P-proofs of rfn_{P,m,n}, all m, n | Pudlák 2020 l.791–793: "all extensions of CF provably p-prove their reflection principles. This result is just an easy generalization of Cook's proof of this fact for Extended Resolution [7]" ([7] = Cook, STOC 1975). Also Corollary 3.2 (l.407–411): P p-proves {con_{P,m}} → {rfn_{P,m,n}}. |
| 2 | Frege | **p-proves** | "polynomial size proofs of the reflection principle for a Frege system in the Frege system" | Pudlák 2020 l.793–794, citing Buss [6], "Propositional consistency proofs", APAL 52 (1991). The route via VNC¹ is also cited there (l.794–795). Cook–Nguyen l.477 ("VNC¹ proves the soundness of Frege systems") and Exercise 10.64 ("Show that VNC¹ proves RFN_PK") point the same way; they are not used as the row's source (g10). |
| 3 | G_i (quantified propositional) | **p-proves** | "using polynomial length proofs" | Pudlák 2020 l.808–809, citing Krajíček–Pudlák [21] (1990). Cook–Nguyen §10B.3 gives the associated-theory form ("the RFN for each system G⋆_i or G_i is provable in the associated theory", l.23389). |
| 4 | Bounded-depth Frege F_d, d ≥ 1 | **open** | — | Pudlák 2020 Problem 1 (l.759): "Does F_d p-prove its reflection principle for d ≥ 1?" The cross statement F_{d+1} ⊢ rfn_{F_d} is "probably true" (l.740–745), with a proof idea only. |
| 5 | Res(k), k ≥ 2 | **open** (not found, g8) | — | Not in AB 2004, Pudlák 2020 or Cook–Nguyen. Garlík 2020 (l.94–96): "instead of the reflection principle for Res(k), which would correspond to the hypothesis of Pudlák's proposition above, we work with the reflection principle for resolution". The known results are cross: AB Theorem 5 (Res(2) refutes Res's reflection principle in size (nr + nm)^{O(1)}), and Pudlák l.753–754 (Res(k+1) provably p-proves rfn_Res(k)). |
| 6 | Cutting Planes | **does not p-prove** | "size ≥ 2^{n^ε} for some ε > 0" (n not defined in the statement) | Pudlák 2020 Theorem 3.11 (l.616), citing Pudlák [27] (2003). The primary [27] is not read here; the row carries "as stated by Pudlák 2020". |
| 7 | Resolution | **does not p-prove** | primary form: 2^{Ω(s^{1/4})} for n, r, m "of the order of a quasipolynomial 2^{(log s)^{O(1)}}" (Flags Q/T) | Atserias–Bonet 2004 Theorem 11 (p. 15, primary, read in A2). Pudlák's restatement as Theorem 3.12 (≥ 2^{n^ε}) is not inferred to match. Pudlák's Corollary 3.8 gives a second route, via Lemma 3.7 and feasible disjunction (claimed, not re-checked). |

**Also recorded, because it separates consistency from reflection at the bottom:** Resolution *does* p-prove its own consistency, and the local reflection for non-tautologies (Pudlák 2020 Proposition 3.9, from A1). The self rung at the bottom is therefore a *reflection* phenomenon, as A1 said.

**Where the divide sits (the finding).**
- **Known to prove their own reflection:** Frege, every extension of CF, and G_i.
- **Known not to:** Resolution and Cutting Planes.
- **Open, strictly between them:** Res(k) for k ≥ 2, and F_d for d ≥ 1.
- Finite second incompleteness in the self form therefore has content exactly on the weak side. Its frontier is Pudlák's Problem 1 together with the Res(k) row.

## 3. (c) The smallest open self rung, and its obstruction

**Res(2) ⊬_poly rfn_Res(2)** (open; g8, per row 5). Both routes known for Resolution fail at Res(2) at a named step, and both steps are now verified from text:
1. **The interpolation route (Atserias–Bonet Theorem 11).**
   - It uses *monotone feasible interpolation of Resolution*, applied to SAT ∧ REF with a clique/coloring reduction (p. 15: "Let C be the monotone circuit that interpolates these formulas given by the monotone feasible interpolation of Resolution").
   - For Res(k), AB p. 14: "We know, however, that Res(k) does not have monotone feasible interpolation (see [ABE02] and Corollary 1 in this paper)". **That step fails.**
2. **The disjunction route (Pudlák Corollary 3.8).**
   - It uses Resolution's *feasible disjunction property*.
   - For Res(k), Garlík 2020, Theorem 1 (l.81): "For every integer k ≥ 2, Res(k) does not have the weak feasible disjunction property." **That step fails.**
   - Garlík also restates a proposition of Pudlák [17] (l.69–78). A system with the weak FDP that is closed under restrictions, has poly-size proofs of its own reflection principle, and turns P-proofs of ¬SAT_¬F into P-proofs of F, would give every F either a short proof or a short refutation statement. Pudlák judges that conclusion unlikely, so FDP and self-reflection pull against each other.

**The obstruction, named as pre-registered (Flag O, now verified):** both known routes to a self-rung lower bound use a feasible-interpolation-type property that Resolution has and Res(2) provably lacks. A2's Lemma 3 does not help either: at a self rung there is no stronger system to project from. An attempt at Res(2) therefore needs a lower-bound method for the SAT ∧ REF_Res(2) pair that uses neither monotone interpolation nor feasible disjunction. That would be A4.

## 4. The interpretive line (labelled): the pre-registered test, and what survives

**The extension reading, as fixed in the amendment, FAILS.** The test was: "a system *without* extension that p-proves its own reflection" falsifies it. Frege has no extension, and it p-proves its own reflection principle (row 2: Buss, per Pudlák l.793–794). The reusability-threshold reading therefore does not mark the divide, as stated.

**What the table does support is Pudlák's own remark, not ours.** On why F_{d+1} ⊢ rfn_{F_d} is believed, Pudlák says (l.749–752): "the formulas expressing that a clause is satisfied by an assignment (general in the case of the reflection principle and specific in the case of the local reflection principle) have the appropriate depth, cf. the proof of Proposition 3.9." **Read as a divide (post hoc, suggested by the table, not pre-registered, so it is not confirmed by it):** P proves its own reflection when P's lines can express "a coded P-line is satisfied by an assignment". Checked row by row:
- **Resolution: the reading holds.** "Clause j is satisfied by z" is the 2-DNF ⋁_i (y_{0,i,j} ∧ z_i) ∨ (y_{1,i,j} ∧ ¬z_i). That is exactly AB's D_k (p. 11), and it lives in Res(2), not in Res. Res fails on its own reflection (row 7), and Res(2) succeeds on Res's (row 5, cross).
- **Res(k): the reading is consistent.** Evaluating a coded k-DNF needs (k+1)-terms, and Res(k+1) ⊢ rfn_Res(k) (row 5, cross). The self case is open, and the reading predicts it is hard.
- **Frege: the reading holds.** Formula evaluation is expressible by polynomial-size formulas: Buss's Boolean Sentence Value algorithms, with Cook–Nguyen §10C.2 stating that (Z ⊨₀ X) is Δ^B_1-definable in VNC¹ (l.24917–24918). Frege p-proves its own reflection (row 2).
- **CF / EF: the reading holds.** Circuits evaluate circuits (row 1).
- **F_d: the reading is consistent.** Depth-d evaluation needs more depth, the self case is open (row 4), and the reading predicts hardness.
- **CP: not checked.** Whether CP lines can express the satisfaction of a coded inequality is not examined here.

**Extension** is then one way to get self-evaluation (circuits), not the threshold itself: Frege gets self-evaluation from formula evaluation in NC¹. The reusability gloss is withdrawn for this divide. What the table supports is *self-evaluation*, i.e. the propositional form of a partial truth definition for the system's own lines. That is the Pudlák 1986 analogy the reviewer intended, minus the extension claim.

**(d) Typical-vs-named: no seventh instance.** The self/cross distinction is not typical-vs-named: both sides reflect over *all* proofs, and neither names a single object. By the table, the divide is about expressive power (self-evaluation). Under g12 there is no sourced pair formulation to count. The sixth instance (A1: consistency's named ⊥ vs reflection) stands unchanged.

## 5. Priors against outcome

| | S1 | S2 | S3 |
|---|---|---|---|
| mine (pre-reg) | 10 | 75 | 15 |
| reviewer (pre-reg → amended) | 60 → 15 | 25 → 65 | 15 → 20 |
| **outcome** | | **S2** | |

## 6. The path statement after A3 (as the amendment fixed it)

**The finite Gödel theorem, in its only form with content for all systems, is cross-form:**
- **CON^N**: ∀S ∃T, S-proofs of Con_T(n̄) are not polynomially bounded. M5 recorded this, from Pudlák 2017, as equivalent to "there exists no length-optimal proof system".
- **Its Σ^b_1-reflection weakening RFN^N_1**, which implies NP ≠ coNP (§1).
- The self form holds only below the self-evaluation divide (§2, §4), so it cannot be a route for all systems.

A4 (to be drafted, and only after this merges) would map what is known toward "no optimal proof system": Krajíček–Pudlák 1989, KMT, Beyersdorff–Köbler–Müller, and Messner. It would also test whether the self-reference reading ("an optimal system would be a universal layer") gives any leverage the literature lacks.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.
