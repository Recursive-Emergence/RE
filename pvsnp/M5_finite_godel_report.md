# M5: the finite Gödel theorem. Report

*Run 2026-09-10 on branch `m5-finite-godel`, against the pre-registration (accepted; the reviewer's additions to Flags I and N are applied). g1, g8, g9, g10 and g11 apply. "Verified" means checked against the source text or official abstract. "Secondary" means verified in another paper's text, with the primary not reached.*

## Outcome: **G1**

- **G1 holds.** CON^N⁺ is Pudlák's stated conjecture, with its obstacles named in his own text. The programme's smallest form is his conjecture, and the path is his.
- **G2 does not occur.** No unconditional instance *in the pair form* was found at the bottom of the ladder. The single-system results fit neither CON^N⁺ nor any superpolynomial self-case in Pudlák's family (§(b)).
- **G3 does not occur.** Krajíček's diagonalization paper does not close the lever. It proves an **unconditional disjunction**, and one of its three disjuncts is exactly Pudlák's CON (§(c)).

Priors: mine G1 50; the reviewer's G1 45. Flag I held; Flag N is resolved in §(a).

## (a) Pudlák 2017, mapped (paper text, verified; forms per g9)

**The finite consistency statements themselves.**
- **Theorem 3.1:** "(1) For every theory T ∈ 𝒯, there exists ε > 0 such that the length of the shortest T-proof of Con_T(n̄) is at least n^ε. (2) If, moreover, T is sequential and finitely axiomatized, then there are T-proofs of Con_T(n̄) lengths of polynomial in n."
- Each Con_T(n̄) is Π₁ with a bound, of length O(log n).

**The conjectures:**

| Conjecture | Statement | Stated relations |
|---|---|---|
| **CON^N** | "For every S ∈ 𝒯, there exists T ∈ 𝒯 such that the lengths of S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n." | ⟺ "There exists no length-optimal proof system" ([27] = Krajíček–Pudlák 1989) |
| **CON^N⁺** | "for every S, T ∈ 𝒯, if T proves Con_S, then S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n." | a strengthening of CON^N |
| **RFN^N_1** | the finite Σ^b_1-reflection version | CON^N ⇒ RFN^N_1, and "Conjecture RFN^N_1 implies NP ≠ coNP" |
| **CON** | "There exists no p-optimal proof system." | ⟺ its uniform version: "S-proofs of Con_T(n̄) cannot be constructed in polynomial time in n" |

Pudlák on the name: "If Conjecture CON^N were proven true, we would certainly advocate calling it the finite Gödel theorem." He also notes that Friedman's n^ε lower bound "can also be viewed as the finite Gödel theorem".

**Flag N, resolved.** The Krajíček–Pudlák implications, *secondary*: verified in the text of arXiv:2408.07408; the primary, JSL 1989, was not reached. Verbatim:

> Sufficient conditions. Krajíček and Pudlák [KP89] were the first to study sufficient condi- tions for the existence of optimal proof systems outside NP. They prove that NE = coNE implies the existence of optimal proof systems for TAUT, and E = NE implies the existence of p-optimal proof systems for TAUT. Köbler, Messner, and Torán [KMT03] improve this result to NEE = coNEE for optimal and EE = NEE for p-optimal proof systems for TAUT. Köbler and Messner [KM98] and Messner [Mes00] show that the existence of (p-)optimal

**Consequences:**
- CON^N (no length-optimal proof system; Pudlák's "optimal" in [27] is the length version, per his l.1285–1287) ⇒ **NE ≠ coNE**, and by the extension quoted, NEE ≠ coNEE.
- CON (no p-optimal proof system) ⇒ **E ≠ NE**.
- CON^N ⇒ RFN^N_1 ⇒ **NP ≠ coNP** (Pudlák).

Every instance of the family therefore has a separation of exponential-time classes as its price.

## (b) What is known toward CON^N⁺

**Flag I, applied, with the reviewer's addition.**
- *Self versus pair, in Pudlák's own words.* The self case is settled polynomially by Theorem 3.1, and Pudlák writes that "the fact that T does not prove its own consistency is not important", placing the conjecture on *pairs* ("if T is sufficiently stronger than a theory S, then S-proofs of Con_T(n̄) cannot be polynomially bounded").
- **His family has no superpolynomial self-case conjecture.** So Garlík (resolution on its own refutation statements) and Davis–Robere (depth-d Frege on its own Prf formulas) fit neither CON^N⁺ nor a self-case conjecture of his. They are self-directed lower bounds for structured families, and they sit where M2 placed them.
- **Why the pair condition must be "T proves Con_S" (verified; Hrubeš, unpublished, Pudlák Theorem 3.4).** For sequential, finitely axiomatized S ⊆ T, there is a true Π₁ sentence φ, built by the fixpoint theorem as a Rosser-style sentence with T ⊬ φ, S ⊬ ¬φ and N ⊨ φ, such that "the lengths of S-proofs of Con_{S+φ}(n̄) can be bounded by a polynomial in n". **The diagonal lever can manufacture a strong extension whose finitistic consistency is cheap.** Strength alone does not give hardness.
- **Known partial results:**
  - Pudlák [31]: "S₂ does not prove bounded consistency of the apparently weaker theory S¹₂". A theory-level, uniform statement, not a proof-length one.
  - Köbler–Messner–Torán, via Pudlák: a p-optimal proof system would give UP a complete set.
  - Pudlák's open-problem list: "Apparently the only separation that is known is a separation of Conjectures CON and DisjNP", relativized.
- **An unconditional pair-form instance: not found** (g8).

## (c) Krajíček, *Diagonalization in proof complexity* (Fundamenta Mathematicae 182, 2004)

**Verified from EUDML's raw page, where the class names are missing from the site's own metadata.**
- "We study diagonalization in the context of implicit proofs of [10]. We prove that at least one of the following three conjectures is true:
  - There is a function f: {0,1}* → {0,1} computable in __ that has circuit complexity 2^{Ω(n)}.
  - __ ≠ co__.
  - There is no p-optimal propositional proof system."
- It continues: "if a minor variant of a recent conjecture of Razborov [17, Conjecture 2] is true (stating conditional lower bounds for the Extended Frege proof system EF) then actually unconditional lower bounds would follow for EF."
- **The two blank class names are UNVERIFIED.** They are dropped in EUDML's HTML and BibTeX, and no full text was reached. A tool's fill-in of "NP ≠ co-NP" was **rejected**, because it did not come from the source.

**What this means for the lever.** Diagonalization over implicit proofs yields an **unconditional theorem**: one of three conjectures holds, and the third ("no p-optimal propositional proof system") **is** Pudlák's CON (verified). So at the top of the ladder the diagonal lever does not fail. It yields a *disjunction* in which the finite-Gödel conjecture is one arm. That is G1-consistent, and it is the most the lever is verified to give.

## (d) The smallest instance: what a proof would need

- **The instance (from M4):** "EF has no polynomial-size proofs of Con_{iEF}(n)".
- **Correction to M4 (g10).** This counts as a **CON^N⁺ instance only if iEF's corresponding theory proves the consistency of EF's**. No source reached states that. M4's statement is therefore conditional on that pair condition and is recorded here as such.
- **What the lower-bound side can use:** finitistic derivability conditions (Pudlák 1986; the n^ε bound needs only T ⊇ Q).
- **What the upper-bound side uses:** a partial truth definition in *sequential, finitely axiomatized* theories (Theorem 3.1(2); Pudlák 1986 §5).
- **Whether a partial truth definition applies to implicit proofs, and which derivability conditions survive for iEF: not found stated** (g8). By g10 it is not inferred.

## (e) The cost

- Any proof of CON^N would give **NE ≠ coNE** (and NEE ≠ coNEE); any proof of CON would give **E ≠ NE** (Flag N, secondary); and CON^N gives **NP ≠ coNP** through RFN^N_1.
- The EF/iEF instance, if its pair condition holds, would give a **superpolynomial EF lower bound for an explicit family** (M2's frontier) as an immediate consequence.
- No instance is cheap.

## Calibration

- **The reviewer:**
  - its Flag-I addition (place the single-system results against Pudlák's self case) was right, and there is no superpolynomial self case;
  - its Flag-N warning prevented deriving CON^N ⇒ NE ≠ coNE before the text was read, and the implication is now verified secondarily;
  - its G2 prior (30) did not occur.

  No premise misses.
- **Me:**
  - Flags I, N and D held;
  - M4's smallest instance carried an unverified pair condition. That is corrected here as a **miss of mine**: g10 was not applied to the instance in M4.

## Sources (checked this run)

- Pudlák, *Incompleteness in the finite domain*, BSL 2017: <https://users.math.cas.cz/~pudlak/inco.pdf> (text: Theorems 3.1 and 3.4, conjectures, l.436, 798–806, 1285–1296, 1523–1534, 1640–1650, 1875–1892)
- Krajíček, *Diagonalization in proof complexity*, Fund. Math. 182 (2004): <https://eudml.org/doc/286451> (raw page; class names missing)
- arXiv:2408.07408, *Optimal Proof Systems for Complex Sets are Hard to Find* (text, l.83–88): the restatement of Krajíček–Pudlák 1989 and Köbler–Messner–Torán
