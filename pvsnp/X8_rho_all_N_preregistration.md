# X8: ρ(N) < 1 for all N ≥ 8, or a witness. Pre-registration

*Drafted 2026-09-11 on branch `x8-rho-all-n`, on the author's decision **"Draft X8 only"**: pre-register, obtain the reviewer's ruling, and stop. **No run until the author gives a separate go.** `formal/` closed. g5 for every bound used.*

## Target (the reviewer's, verbatim in content)

- **The quantity.** ρ(N) = (N + E⁻(N))/N^{1.5}, where E⁻(N) = max over blocky q of −⟨H_N, q⟩. Known:
  - ρ(4) = 1 and ρ(8) = 0.928 (exact);
  - ρ(16) ∈ [0.953, 0.969] (proved < 1);
  - ρ(32) ∈ [0.845, 1.061].
- **(a) Analytic upper bound.**
  - Sharpen the per-rectangle bound φ(a, b) using the proved all-(−1)-rectangle fact (area ≤ N/2), plus any refinement of Lindsey that the extremal 5×5 structure suggests.
  - Run the 2-D knapsack at N = 32, 64, 128 and report the upper bound on ρ(N).
  - The target is a theorem: ρ(N) < 1 for all N ≥ 8.
- **(b) Structured search at N = 32** over 5×5-type and Lindsey-near-saturating blocks, for a lower bound, so that a witness ρ(32) > 1 is found if one exists.
- **(d) Calibration.** Any new φ bound must reproduce, as knapsack upper bounds, ≤ 5, ≤ 16 and ≤ 46 at N = 4, 8, 16. It must be consistent with the exact E⁻ = 4 and 13 and with E⁻(16) ≥ 45.

## Flags raised before any work (mine)

**Flag D (the deficit accounting: why "for all N" needs a factor-2 improvement).**
- ρ(N) < 1 ⟺ E⁻(N) < N^{1.5} − N. A knapsack bound must therefore show a total *deficit* Σ_i (√(N·a_i·b_i) − φ(a_i, b_i)) ≥ N over every feasible family, below Lindsey's N^{1.5}.
- The knapsack's worst case for Lindsey-type bounds is about √N blocks of about √N × √N. For those:
  - the refinement used in X7, √(ab(N − b)) = √(Nab)·√(1 − b/N), gives a deficit of about b√(ab)/(2√N) = √N/2 per block;
  - that is **≈ N/2 in total, a factor 2 short**.
  - This matches X7's analytic ρ bounds, 1.078, 1.061 and 1.053 at N = 16, 32, 64, which exceed 1 by about N^{−1/2}/2.
- **So "closes for all N" needs a per-block bound with a two-sided deficit**, roughly √(Nab)·(1 − (a + b)/(2N)), or a structural gain of the same size.
- **Two candidates, to be derived:**
  - (i) a two-sided spectral refinement, projecting out *both* the all-ones row and column directions;
  - (ii) a combinatorial gain from the N/2 −1-rectangle fact. A block of area > N/2 must contain +1 entries; the run must show how many.
- If neither yields the full N, the analytic route stalls at a named step: "a per-block deficit ≥ (a + b)√(ab)/(2√N) for Sylvester rectangles".

**Flag K (the relaxation's own slack).** The exact-φ knapsack is tight at N = 16 (46 vs ≥ 45) but loose at N = 8 (16 vs 13). Even an exact φ may not certify ρ < 1 at every N: the cardinality relaxation drops disjointness. If the analytic φ reaches the exact φ at N ≤ 16 and the knapsack still exceeds N^{1.5} − N at some larger N, the report says the *relaxation*, not φ, is the obstacle.

**Flag S (the search design).** X7's decoupled local search at N = 32 (≥ 121, ρ ≥ 0.845) is likely weak, since N = 16's search reached its bound only after repeated restarts. (b) seeds from the N = 16 extremal shape: three 5×5 blocks at 75% of Lindsey, not monochromatic.
- Scaled analogues at N = 32 (blocks of ≈ √32 ≈ 5–6) and tensor combinations (q₁₆ ⊗ blocky₂) are the seed families.
- Affine-subspace rectangles are *not* near-saturating: a coset pair has |sum| = |A||B|·2^{−rank}, far from √(N|A||B|). They are recorded as a non-candidate.
- A witness needs E⁻(32) > 32^{1.5} − 32 ≈ 149.0.

## Outcomes (the reviewer's)

| Outcome | Meaning |
|---|---|
| **closes** | ρ(N) < 1 proved for all N ≥ 8: tensor unions never break the tight Union Lemma (a small theorem). |
| **witness** | ρ(N) > 1 at some N: the tight Union Lemma fails via tensor unions (X5c retroactively). |
| **undecided** | Both routes stall, each at a named step. |

**Priors.**
- Reviewer: closes 40 / witness 25 / undecided 35.
- Mine: **closes 15 / witness 15 / undecided 70.** Flag D: the known refinement is a factor 2 short of what "for all N" needs, and one run is unlikely to find the missing factor.

## Ceiling

X8 proves nothing about P vs NP. At best it closes one form of the Union Lemma (tensor unions) for all N.

## Ruling (the reviewer's): accepted as a draft; no run until the author's separate go

**Priors moved:** undecided 70 / closes 15 / witness 15. Flags K and S adopted.

**The reviewer's concrete candidate for Flag D (i), with a prediction; to be verified in the run.**

*Two-sided Lindsey.* Write 1_A = (a/N)𝟙 + u and 1_B = (b/N)𝟙 + v, with u, v ⊥ 𝟙. Sylvester H has H𝟙 = N·e₀ and 𝟙ᵀH𝟙 = N, so
  1_Aᵀ H 1_B = ab/N + b·(1_A(0) − a/N) + a·(1_B(0) − b/N) + uᵀHv,
and |uᵀHv| ≤ √N·‖u‖‖v‖ = √(ab(N−a)(N−b)/N).
- A mental check of the expansion, done at acceptance and not yet a computation, agrees.
- The leading term's deficit below √(abN) is ≈ √(ab)(a + b)/(2√N), the two-sided deficit Flag D asks for.
- The boundary terms are paid by at most one block each, since row 0 and column 0 each lie in at most one block.

*The reviewer's prediction:* at the worst case (√N blocks of √N × √N), the bound gives N^{1.5} − N + O(√N). That is **borderline, short by a lower-order O(√N)**.
- The named second source of deficit is **the equality analysis**. uᵀHv = √N‖u‖‖v‖ requires Hv ∝ u (centered Cauchy–Schwarz tightness), and the −1-rectangle fact (area ≤ N/2) should force a quantifiable loss.

*Calibration first:* the two-sided knapsack must give knapsack values ≤ 5, 16 and 46 at N = 4, 8, 16. If it reproduces 46 at N = 16, the remaining gap is the relaxation (Flag K).

*If the prediction holds,* X8's outcome is **"undecided at a named O(√N) term"**, which names what a proof of ρ(N) < 1 for all N needs.
