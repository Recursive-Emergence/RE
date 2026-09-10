# A2: the first rung, (Res, CF). Pre-registration

*Drafted 2026-09-10 on branch `a2-first-rung`, on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. **This is an attempt: g5 applies in full, and every step of ours is a written proof with size bounds, not a citation.** g1, g8, g9, g10, g11 and g12 also apply.*

## Target

**Res ⊬_poly rfn_CF**: Resolution has no polynomial-size proofs of Circuit Frege's reflection principle. It is to be derived from Atserias–Bonet (Theorem 3.12 as quoted in Pudlák, arXiv:2007.14835: "Res-proofs of the reflection principle of Res have size ≥ 2^{n^ε}") together with:
- **(a) the pair condition, at the theory level:** S¹₂ ⊢ Sound(Res). Find it in the literature: Cook–Nguyen (V⁰ proves the soundness of bounded-depth PK; the exact containment of resolution in depth-1 PK; the exact relation of V⁰ to S¹₂). Otherwise state the missing link.
- **(b) the translation lemma (ours, to prove):** Res p-proves prf_Res(x⃗, φ) → prf_CF(t(x⃗), φ) for a syntactic translation t.
- **(c) the composition:** a short Res-proof of rfn_CF gives a short Res-proof of rfn_Res, which contradicts Theorem 3.12, with the size arithmetic stated explicitly.
- **(d) novelty:** whether the (Res, CF) instance, or a general statement such as "Res does not p-prove rfn of any system that p-simulates it", is already stated (Pudlák 2020; Atserias–Bonet).

## A structural point (mine), fixed before the run

The **lower bound** Res ⊬_poly rfn_CF needs only **(b) + (c) + Theorem 3.12**. The **pair condition (a)** is needed only to count the result as an instance of the *reflection pair form* of the finite Gödel theorem: T provably p-proves rfn_S, and S ⊬_poly rfn_T. The report keeps the two apart. If (a) fails but (b) and (c) hold, the lower bound stands, and only the pair interpretation is open.

## Flags raised before any attempt

**Flag P (projection): the likeliest place for (b) and (c) to fail.**
- Resolution is closed under *restrictions and renamings*, substituting variables with variables or constants, but not under substituting formulas.
- Step (c) instantiates rfn_CF(π, φ, y) at π := t(x⃗). Inside Resolution this is available only if **t is a projection**: every bit of the CF-proof code t(x⃗) is a bit of x⃗ or a constant.
- So the lemma must be proved *for a projection t*, and that constrains the encodings:
  - CF lines are circuits and Res lines are clauses;
  - one resolution step becomes a *fixed template* of CF lines;
  - clause widths up to n need padded, position-indexed encodings.
- **If no projection t exists for the encodings in the literature, (c) fails as stated. That is C3, with the encoding as the obstacle.**

**Flag E (encoding): Theorem 3.12 is about a specific formula.** Its lower bound is for Atserias–Bonet's encoding of rfn_Res. What (c) produces is rfn_Res *in the encoding induced by t and by CF's encoding*. The run must show that the two coincide, or that one is converted to the other in polynomial-size Resolution. Otherwise Theorem 3.12 does not apply. The primary is not reached (M-program: the Information and Computation page was blocked), and Pudlák's paper notes that "the encoding of Resolution proofs in the two cited papers are different" for Lemma 3.7. **This may make C3 the honest outcome.**

**Flag Q (measure).** State what n is in "2^{n^ε}": the size of the formula φ, the proof-size parameter m, or the length of the reflection formula. Also state what "polynomial" in Res ⊬_poly rfn_CF is measured against. The composition must keep these consistent.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **C1** | Already stated in the literature. The first rung is known, and A3 climbs to (Res(2), Res(3)). |
| **C2** | Proved here: elementary, novelty-checked, and labelled ours. |
| **C3** | (a), (b) or (c) fails. The smallest open instance stands as A1 stated it, and the failing lemma is the obstacle. |

**Priors.** Mine: C3 35 / C1 35 / C2 30. C3 is raised by Flags P and E. The reviewer's: C1 40 / C2 40 / C3 20.

## Ceiling

A2 is one rung. The reflection form of the finite Gödel theorem would need every rung, and the stall is where the pair conditions are only "probably true" (F_{d+1} proving the reflection of F_d) and at Pudlák's Problem 1. Nothing here touches NP ≠ coNP.
