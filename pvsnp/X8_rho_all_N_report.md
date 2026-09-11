# X8: ρ(N) < 1 for all N ≥ 8, or a witness. Report

*Run 2026-09-11 on branch `x8-rho-all-n`, on the author's go ("ya", after "X8 runs only if you give a separate go"). Against the pre-registration (1a46102) and its accepted amendment (09a4839): the reviewer's two-sided Lindsey candidate and prediction; priors undecided 70 / closes 15 / witness 15. A computation plus elementary bounds; scripts `x8_knap.py`, `x8_knap2.py`, `x8_knap3.py` and `x8_n32*.py` are in the job's scratch directory. `formal/` closed.*

## 0. Outcome

**Undecided for all N, as predicted, at the named O(√N) term. N = 32 and N = 64 are decided.**
- **ρ(32) ≤ 0.961 < 1, proved** by a knapsack using exact φ for small blocks.
- **ρ(64) ≤ 1, proved** by the analytic knapsack (the bound equals the target exactly).
- **ρ(128) ≤ 1.0027** (open).
- **For general N**, the two-sided analytic bound exceeds the target by a lower-order term that grows like √N: **the reviewer's prediction, confirmed.**
- **No witness** (ρ > 1) exists at any N where the question is now decided. The pre-registered search at N = 32 is moot, since ρ(32) < 1 is proved.
- **The ρ table now reads:**
  - N = 4: 1 (exact);
  - N = 8: 0.928 (exact);
  - N = 16: ≤ 0.969;
  - N = 32: ≤ 0.961;
  - N = 64: ≤ 1;
  - N = 128: ≤ 1.0027 (open).
- **Tensor unions with block size b ≤ 6 are therefore proved harmless** to the tight Union Lemma (b ≤ 5 strictly).

## 1. The two-sided Lindsey bound (the reviewer's candidate; verified)

**Expansion.** Write 1_A = (a/N)𝟙 + u and 1_B = (b/N)𝟙 + v, with u, v ⊥ 𝟙. Sylvester H has H𝟙 = N·e₀, 𝟙ᵀH = N·e₀ᵀ, and 𝟙ᵀH𝟙 = N. So
  1_Aᵀ H 1_B = ab/N + a·v₀ + b·u₀ + uᵀHv,  with u₀ = 1_A(0) − a/N and v₀ = 1_B(0) − b/N.

**Per-block bound on −Σ_{A×B} H (ours, from the expansion).**
- **Case 0 ∉ A and 0 ∉ B** (u₀ = −a/N, v₀ = −b/N): −Σ = ab/N − uᵀHv.
- **Case 0 ∈ A:** subtract b. **Case 0 ∈ B:** subtract a. Membership only lowers the bound.
- |uᵀHv| ≤ ‖H‖·‖u‖‖v‖ = √N·√(a(N−a)/N)·√(b(N−b)/N).
- **So** −Σ_{A×B} H ≤ **ab/N + √(ab(N−a)(N−b)/N)**.

**Two further exact refinements (ours, elementary).**
- **Parity:** Σ_{A×B} H ≡ ab (mod 2), so φ(a, b) can be lowered to the parity of ab.
- **Not all −1:** if ab > N/2, the block is not all −1, by the X7 theorem (area ≤ N/2). So −Σ ≤ ab − 2.

**The per-rectangle bound.** φ(a, b) := min(one-sided Lindsey, two-sided, ab, and ab − 2 if ab > N/2), adjusted to the parity of ab.

## 2. The knapsack results (E⁻(N) ≤ max Σ_i φ(a_i, b_i) with Σa_i, Σb_i ≤ N; target N^{1.5} − N)

| N | one-sided (X7) | two-sided alone | combined analytic | exact small blocks | target | ρ bound |
|---|---|---|---|---|---|---|
| 4 | 5 | 6 | 5 | (exact-φ: 5; truth 4) | 4.0 | exact: ρ = 1 |
| 8 | 16 | 16 | 16 | (exact-φ: 16; truth 13) | 14.6 | exact: ρ = 0.928 |
| 16 | 53 | 52 | 48 | **46** (exact φ, X7) | 48.0 | ≤ 0.969 |
| 32 | 160 | 152 | 150 | **142** (exact φ for sides ≤ 6) | 149.0 | **≤ 0.961** |
| 64 | 475 | 456 | **448** | — | 448.0 | **≤ 1.000** |
| 128 | 1375 | 1328 | 1324 | — | 1320.2 | ≤ 1.0027 |

- **Calibration** (pre-registered): every bound is ≥ the true value at N = 4, 8, 16 (4, 13, 45–46), so all are valid.
  - The combined analytic bound gives 5, 16 and 48. It matches the exact-φ knapsack at N = 4 and 8, and is 2 weaker at N = 16.
- **The reviewer's prediction, confirmed:** the two-sided bound's excess over the target is +3.0, +8.0 and +7.8 at N = 32, 64, 128, with √N = 5.7, 8, 11.3. That is O(√N): borderline, short by a lower-order term.

**N = 32, in detail.**
- The analytic knapsack optimum is six blocks with shapes (5,5), (5,5), (5,6), (5,6), (6,5), (6,5), value 150.
- Exact φ at these shapes is far below the analytic value: **φ(5,5) = 17** against analytic 23, and **φ(5,6) = 20**, **φ(6,6) = 22**. These come from enumerating all C(32,5) and C(32,6) row sets, each taking the b best columns.
- With exact φ for all block sides ≤ 6, the knapsack optimum moves to (7,8), (7,8), (8,7), (10,9), with value **142 < 149.02**. **So ρ(32) ≤ (32 + 142)/32^{1.5} = 0.9612.** ∎
- *Validity:* each φ entry is the minimum of valid upper bounds, and the knapsack relaxes disjointness to cardinality, so the value bounds E⁻(32) from above.

**N = 64.** The combined analytic knapsack gives exactly 448 = N^{1.5} − N, so ρ(64) ≤ 1. Exact φ at the relevant block sides (≈ 8) is out of reach (C(64,8) ≈ 4.4·10⁹).

## 3. What stands, and the named term

- **For all N, undecided.** The two-sided analytic bound leaves a lower-order excess of ≈ Σ_blocks ab/N ≈ √N at the worst case.
- **What a proof for all N needs**, the equality analysis the reviewer named: a *uniform* per-block deficit, below the two-sided bound, of total Ω(√N) over any feasible family.
- **The data locate it:** at N = 32, the exact φ(5,5) = 17 against the analytic 23 is a 26% gap on the knapsack's optimal block shape. That is far more than the needed deficit. So small near-√N×√N blocks cannot approach Cauchy–Schwarz equality in Sylvester H.
- **Proving that uniformly** (a bound like φ(a, b) ≤ two-sided bound − c·√(ab)/√N·… for a, b ≈ √N) is the missing lemma. It is **not proved here.**
- **The trend, with no extrapolation** (Flag D): 1, 0.928, ≤ 0.969, ≤ 0.961, ≤ 1.000, ≤ 1.0027. Every decided N has ρ ≤ 1.

## 4. Priors against outcome

| | closes | witness | undecided |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 40 → 15 | 25 → 15 | 35 → 70 |
| mine | 15 | 15 | 70 |
| **outcome** | | | **undecided for all N; decided (ρ ≤ 1) for N ≤ 64** |

No misses on pre-registered claims. The reviewer's two-sided prediction is confirmed quantitatively. The exact-small-block knapsack (not pre-registered as such; it extends X7's exact-φ method) is what decided N = 32.

## Formal record

Untouched (the author's decision).
