# The M-program: final state

*2026-09-10. This page is written to be read on its own. Every cited statement was checked against a source's text or official abstract; "secondary" means verified in another paper's text. Details and line numbers are in `pvsnp/M1`–`M5`. Nothing here proves anything about P vs NP.*

## 1. The reading, in one sentence (interpretive)

A proof of P ≠ NP is itself a certificate, so the question can be asked one layer up, about the lengths of proofs in formal theories and proof systems. There, "P vs NP is an instance of itself" can be stated as theorems and conjectures, not only as a slogan.

## 2. The named target

**Pudlák's CON^N⁺** (*Incompleteness in the finite domain*, BSL 2017, verbatim): *"for every S, T ∈ 𝒯, if T proves Con_S, then S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n."* Here Con_T(n̄) says "there is no T-proof of a contradiction shorter than n".

**Its relatives and consequences:**
- **CON^N** ("for every S there is a T such that S-proofs of Con_T(n̄) are not polynomially bounded") ⟺ there is no length-optimal proof system. CON^N ⇒ RFN^N_1 ⇒ **NP ≠ coNP** (Pudlák, verified).
- **CON** ⟺ there is no p-optimal proof system.
- CON^N ⇒ **NE ≠ coNE**, and CON ⇒ **E ≠ NE**. These come from Krajíček–Pudlák 1989's "NE = coNE ⇒ optimal" and "E = NE ⇒ p-optimal" (secondary).

Pudlák: *"If Conjecture CON^N were proven true, we would certainly advocate calling it the finite Gödel theorem."*

## 3. Why the naive Gödel lever fails: two theorems

1. **On hardness sentences, Gödel's move is a restatement (M3, proved here).** For a Π₁ lower-bound sentence H at a fixed bound, and any Σ₁-sound theory T containing Robinson's Q, "T does not prove ¬H" holds **if and only if** H is true. Establishing unprovability is the same problem as proving the lower bound. Gödel's leverage comes from the diagonal fixed point, and hardness sentences have none.
2. **The diagonal builds strong but cheap extensions** (Hrubeš, unpublished; Pudlák 2017, Theorem 3.4, verified). For a sequential, finitely axiomatized S ⊆ T, a Rosser-style fixpoint φ exists that is true and unprovable in T, yet S has *polynomial-length* proofs of Con_{S+φ}(n̄). So strength alone gives no hardness. The conjecture needs **T ⊢ Con_S**, and Con_S is the Π₁-reflection principle for S (Pudlák, verified): reflection over *all* S-proofs, not a single named sentence that T lacks.

**What the lever does give** (Krajíček, *Diagonalization in proof complexity*, 2004, from the official page). Diagonalization over implicit proofs proves, **unconditionally**, that at least one of three conjectures holds:
- a function computable in **[class UNVERIFIED]** has circuit complexity 2^{Ω(n)};
- **[class UNVERIFIED]** ≠ co-**[same class]**;
- **there is no p-optimal propositional proof system**, which is Pudlák's CON.

The two class names are missing from the source's own metadata, and no full text was reached.

## 4. The smallest instance

> **Extended Frege (EF) has no polynomial-size proofs of Con_{iEF}(n)**

iEF is Krajíček's implicit Extended Frege, whose proofs are exponentially long EF-proofs described by small circuits.
- **It is conditional.** It is a CON^N⁺ instance only if iEF's corresponding theory proves EF's consistency, and no source reached states that (a correction recorded in M5).
- **What a proof would need.** On the lower-bound side, finitistic derivability conditions (Pudlák 1986). The upper-bound side of Pudlák's theory uses a partial truth definition in sequential, finitely axiomatized theories.
- **Unknown (not found stated):** whether a partial truth definition applies to implicit proofs, and which derivability conditions survive for iEF.

## 5. An observation (a reading, not a theorem)

In every layer examined, the obstruction concerns *typical* objects and never *named* ones:
1. **Instances (R2):** compressible strings are exponentially rare, so average-case arguments cannot use them.
2. **Adversaries (R4/R5):** the fact that makes an errorless heuristic a usable test, few Yes instances, is the same fact that lets a two-sided heuristic hide its errors.
3. **Tautologies (M2/M3):** a system can prove its own lower bounds on *named* families (Davis–Robere: depth-d Frege), but no system efficiently proves hardness of *random* truth tables (Pich–Santhanam).
4. **Self-reference (M4):** a diagonal sentence is as large as what it excludes, in its own measure.
5. **Consistency (M5):** the *named* fixpoint extension is cheap (Hrubeš), while reflection over *all* proofs is what the conjecture needs.

## 6. What was proved here

**Nothing about P vs NP.** Proved in these documents:
- the M3 equivalence (§3.1);
- the M4 bound: a self-referential sentence improves on the trivial proof-length bound by at most a polynomial, *in any Cook–Reckhow system, implicit ones included*. Compression changes the measure, not the ratio.

Everything else is verified **location**: where the problem sits, which theorems bound it, and which conjecture it reduces to.

## 7. Calibration, both sides (verbatim from the reports)

**M1:**

> - **The reviewer:**
>   - *Kurtz–O'Donnell–Royer*, named from memory, exists. Its content is a representation-independent *oracle* independence result, not a relative or strengthening of Ben-David–Halevi, which is where it was placed. That is a premise miss, the **eighth**.
>   - "Σ₁-sound" should be Σ₁-complete (precision b). That is a note.
>   - The per-system Π₁ layer was right, with precision (a).
> - **Me:** the pre-registered L2 risk (access to 1990s papers) materialized as expected.

**M2:**

> - **The reviewer:**
>   - the fixed-point framing of KP'89 did not survive at the primaries (A3, pre-registered as Flag O);
>   - the stall was expected at Frege, but the verified source places it lower;
>   - the "one layer up" prediction fails, and in a direction neither side listed.
>
>   These are outcomes, not premise misses. Its note on Flag P was exactly right.
> - **Me:** Flags P and O were right. My A2 prior (50) missed the within-system case. Davis–Robere was not anticipated by either side.

**M3:**

> - **The reviewer:** its three-object precision located the failure exactly. Its T1 expectation did not occur; T3 did, through Flag G. That is an outcome, not a premise miss.
> - **Me:** Flag G was right. My T1 prior (55) was also wrong.

**M4:**

> - **The reviewer:**
>   - its catch (b) was right, and sharpened here;
>   - its sharpened (c) led directly to CON^N⁺;
>   - its D1-through-(iii) expectation held, restatement included.
>
>   No premise misses.
> - **Me:** Flags S and F held, and D1 held.

**M5:**

> - **The reviewer:**
>   - its Flag-I addition (place the single-system results against Pudlák's self case) was right, and there is no superpolynomial self case;
>   - its Flag-N warning prevented deriving CON^N ⇒ NE ≠ coNE before the text was read, and the implication is now verified secondarily;
>   - its G2 prior (30) did not occur.
>
>   No premise misses.
> - **Me:**
>   - Flags I, N and D held;
>   - M4's smallest instance carried an unverified pair condition. That is corrected here as a **miss of mine**: g10 was not applied to the instance in M4.
