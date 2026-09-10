# A1: the bottom pair. Pre-registration

*Drafted 2026-09-10 on branch `a1-bottom-pair` (on top of the M-program final page), on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. It is a document only; guards g1, g8, g9, g10 and g11 apply.*

## Target (the reviewer's shape)

M5 found no unconditional instance of Pudlák's CON^N⁺ in the pair form, but that search was general. A1 searches the **bottom of the ladder**, where lower bounds exist:
- **(i)** the lowest pair (S, T) with **T ⊢ Con_S verified from a source**;
- **(ii)** whether "S has no polynomial-size proofs of Con_T(n̄)" already follows from a known S lower bound;
- **(iii)** if so, a first verified rung of the finite Gödel theorem;
- **(iv)** if not, that statement as the smallest open instance.

## Flags raised before any run

**Flag T (theories versus proof systems).**
- Pudlák's CON family is stated for first-order *theories* S, T ∈ 𝒯, in which Con_T(n̄) is a first-order sentence.
- At the bottom of the ladder, S is a *propositional* proof system (resolution, depth-d Frege), and it can only address the propositional translation ||Con_T(n)|| (a tautology family), or a propositional consistency statement for a proof system T.
- **The run must fix the formulation from a source before counting anything:** Pudlák's or Krajíček's propositional versions, if stated. That includes whether the propositional analogue keeps the pair hypothesis "T proves Con_S", and in which theory that is proved.

**Flag R (reflection gives consistency).**
- If a theory proves the reflection principle, or soundness, of a proof system S ("every S-provable formula is true"), it proves S's consistency. Consistency is reflection applied to the false formula ⊥. This is elementary and proved in the report.
- So the soundness results recorded in M2 (Cook–Nguyen: each theory proves the soundness of its corresponding system; "TV⁰ ⊢ RFN_ePK") can supply the pair condition at the *theory* level.
- Whether that suffices for the *propositional* pair formulation (Flag T) is to be checked.

## What the run must deliver

1. **The lowest verified pair (S, T) with T ⊢ Con_S.** Candidates: S = resolution or depth-d Frege, T = Frege or EF (via VNC¹ or V¹ proving soundness, from M2).
2. **For that pair, is S ⊬_poly Con_T(n̄) already known?** Either stated directly (for example "consistency statements of Frege or EF are hard for resolution"), or implied by a known S lower bound through a reduction the run can state and check. Candidates: the PHP bounds, and the Prf / refutation formulas of Garlík and Davis–Robere. Every reduction is proved in the report or not claimed (g5).
3. **The outcome, with the exact statement.**

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **B1** | A bottom-rung instance is already known. Record it and climb (A2). |
| **B2** | It follows from a known lower bound through a reduction we can state. A small real result, to be checked with suspicion. |
| **B3** | It is open even at the bottom. The smallest open instance, stated for attack. |

**Priors.** Mine: B3 50 / B1 30 / B2 20. Flag T may make the formulation itself the first obstacle. The reviewer's: B3 40 / B1 35 / B2 25.

## Ceiling

A1 proves nothing about P ≠ NP. At best it shows the finite Gödel theorem has a first rung; at least it names the smallest open instance in a form that a proof-complexity lower bound could address.
