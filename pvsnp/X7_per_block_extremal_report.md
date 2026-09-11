# X7: the per-block extremal problem. Report

*Run 2026-09-11 on branch `x7-per-block-extremal`, on the author's go ("Run X7, then final page, push after merge"), against the pre-registration (4c35b76), accepted by the reviewer with Flags F, D and L, priors X7b 50 / X7a 30 / X7c 20, and the N = 32 addition. A computation: exact results are labelled exact, searches are labelled searches. Scripts `x7_exact.py`, `x7_milp.py`, `x7_ls.py` and `x7_knap.py` are in the job's scratch directory. `formal/` closed.*

## 0. Outcome

**X7b, restricted to N ≤ 16 (proved for those N), with N = 32 undecided.**
- The per-block tensor factor ρ(N) = (N + E⁻(N))/N^{1.5} is:
  - **ρ(4) = 1 exactly;**
  - **ρ(8) = 0.928 exactly;**
  - **ρ(16) ∈ [0.953, 0.969], proved < 1.**
- **So tensor unions with block size b ≤ 4 are harmless** to the tight Union Lemma. Their advantage is at most 2^{1.5n}·(1 + o(1)), reached with equality in the base only at N = 4.
- **At N = 32:** ρ(32) ∈ [0.845, 1.061] (search below, analytic bound above). Not decided.
- **A small proved fact:** the maximum all-(−1) rectangle of the Sylvester Hadamard H_N has area exactly N/2 (proof in §3, exhaustive check for N ≤ 16). The all-(+1) maximum is N.
- **X7a does not occur** in any computed case. **X7c** (an exact E(N) formula) is not reached: exact values at N = 4 and 8 only.

## 1. Exact values at N = 4 and 8

**The decoupling reduction (the reviewer's; proof).** A blocky q is a family of disjoint row sets A_i matched to disjoint column sets B_i, and −⟨H, q⟩ = Σ_i Σ_{x∈A_i} −(H1_{B_i})(x). For a fixed column family {B_i}, each row x joins at most one block, and the best choice is its best block or none. So
  E⁻(N) = max_{{B_i}} Σ_x max(0, max_i −(H1_{B_i})(x)),
and E likewise with the sign flipped. ∎ The number of nonempty column families is Bell(N+1) − 1: **51 at N = 4 and 21,146 at N = 8** (enumerated).

| N | E(N) | E/N^{1.5} | E⁻(N) | E⁻/N^{1.5} | ρ(N) | method |
|---|---|---|---|---|---|---|
| 4 | 6 | 0.750 | 4 | 0.500 | **1.000** | exhaustive (2^16 matrices, and families) |
| 8 | 16 | 0.707 | 13 | 0.575 | **0.928** | exhaustive families; MILP optimal (HiGHS status 7, gap 0) |

These agree with the reviewer's independent enumeration (E(8) = 16, E⁻(8) = 13).

**Extremal structure (Flag L).**
- N = 4, E⁻: blocks {1,2}→rows {3} and {3}→rows {1,2}. Both are monochromatic −1 rectangles of area 2 = N/2. Σ√(|A||B|) = 2.83.
- N = 8, E⁻: blocks {1,2,4}×{3,5,7} (sum 5, *not* monochromatic, Lindsey 8.49), {3,5}×{1,6} and {6,7}×{2,4}. The last two are monochromatic −1 rectangles of area 4 = N/2. Σ√(|A||B|) = 7.00 < 8.
- N = 8, E: {0,1,2,4}×{0,1,2,4} (sum 10, Lindsey 11.31), {3,5,6}×{7} and {7}×{3,5,6}.

## 2. N = 16 (proved ρ < 1) and N = 32 (undecided)

- **Lower bound, E⁻(16) ≥ 45.** Found three times independently: X6's annealing (61 − 16), the decoupled local search, and the MILP incumbent.
  - Structure: three 5×5 blocks, each with −sum 15 against Lindsey's 20 (75%), none monochromatic, Σ√(|A||B|) = 15 < 16.
- **MILP:** after 1800 s it has not closed: incumbent 45, dual bound 88, ρ ∈ [0.953, 1.625]. **Inconclusive as a solver run.**
- **Upper bound, E⁻(16) ≤ 46 (proved by computation).**
  - Let φ(a, b) := max over rectangles with |A| = a and |B| = b of −⟨H, A×B⟩. It is computed **exactly** by enumerating all 2^16 row sets A; for each, the best B of size b takes the b largest entries of −1_A^⊤H.
  - Since a blocky q is disjoint rectangles with Σ|A_i| ≤ N and Σ|B_i| ≤ N, we get **E⁻(N) ≤ max Σ_i φ(a_i, b_i) subject to Σa_i ≤ N, Σb_i ≤ N** (a 2-D knapsack, with disjointness relaxed to cardinality).
  - Calibration: it gives 5 at N = 4 (exact 4) and 16 at N = 8 (exact 13), both valid upper bounds.
  - **At N = 16 it gives 46 < N^{1.5} − N = 48.** Hence E⁻(16) ∈ {45, 46}, and **ρ(16) ∈ [0.9531, 0.9688] < 1.** ∎
- **N = 32 (the reviewer's addition).**
  - Search lower bound E⁻(32) ≥ 121, so ρ ≥ 0.845 (decoupled local search, 20 × 4·10⁴ steps; labelled a search).
  - The exact-φ knapsack is infeasible (2^32 row sets).
  - The analytic knapsack, with φ′(a, b) = ⌊min(√(Nab), √(ab(N−a)), √(ab(N−b)), ab)⌋, gives E⁻(32) ≤ 160 and ρ ≤ 1.061.
    - The refinement excludes the all-ones row and column: Σ_{x≠0}(H1_B(x))² = N|B| − |B|².
    - It gives ρ ≤ 1.078 at N = 16 and 1.053 at N = 64, so it is too weak to decide.
  - **Undecided: ρ(32) ∈ [0.845, 1.061].**

## 3. Monochromatic rectangles (a small proved fact)

**Claim.** An all-(−1) rectangle A × B of the Sylvester H_N has |A||B| ≤ N/2. An all-(+1) rectangle has |A||B| ≤ N.

**Proof (ours, elementary).**
1. Fix a₀ ∈ A and let V = span{a − a₀ : a ∈ A}, so A ⊆ a₀ + V and |A| ≤ |V|.
2. For y ∈ B and a ∈ A we have a·y = 1 = a₀·y, so (a − a₀)·y = 0. Hence B ⊆ {y ∈ V^⊥ : a₀·y = 1}.
3. That set is empty or a coset of a hyperplane of V^⊥ (if a₀·y were constant on V^⊥, it would be 0, since 0 ∈ V^⊥). So |B| ≤ |V^⊥|/2 = N/(2|V|), and the product is ≤ N/2.
4. For +1: B ⊆ {y ∈ V^⊥ : a₀·y = 0}, which has size ≤ |V^⊥|, so the product is ≤ N (also Lindsey). ∎

**Exhaustive check:** max −1 area = 2, 4, 8 and max +1 area = 4, 8, 16 at N = 4, 8, 16.

**Consequence (Flag L).** Blocks that saturate Lindsey with the −1 sign and have area ≥ N cannot be monochromatic. None of the extremal families at N = 8 or 16 uses near-saturating blocks: 0.59 and 0.71 of Lindsey at N = 8, and 0.75 at N = 16.

## 4. What this decides

- **Tensor unions** (one blocky set per block of b bits, m = n/b) have |Adv(IP2, U)| ≈ ρ(N)^{n/b}·2^{1.5n}. For b ≤ 4, ρ ≤ 1 (proved), so they give no witness against the tight Union Lemma. At b = 2 they saturate it exactly (X6).
- **The tight Union Lemma's status:** open, and now open only against *non-tensor* unions **or** tensor unions with blocks of ≥ 5 bits. The first undecided case is ρ(32) ∈ [0.845, 1.061].
- **The trend (Flag D):** 1.000, 0.928, [0.953, 0.969], then ≥ 0.845 by a weaker search. It is non-monotone, and **no extrapolation is made**.

## 5. Priors against outcome

| | X7a | X7b | X7c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 40 → 30 | 45 → 50 | 15 → 20 |
| mine | 30 | 50 | 20 |
| **outcome** | | **X7b (N ≤ 16, proved); N = 32 open** | |

**Miss (mine, a method miss):** I expected the MILP to close N = 16. It did not (gap 45 vs 88). The exact-φ knapsack relaxation, not pre-registered, is what decided N = 16. That is recorded here as a change of method during the run.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as X7b, restricted to N ≤ 16.**
- The knapsack relaxation is recorded as the method that closed N = 16. The MILP timeout is recorded as a method miss, not a result.
- The −1-rectangle theorem (area ≤ N/2) goes in as proved: ours, elementary.
- X8 (an analytic knapsack aimed at ρ(N) < 1 for all N ≥ 8, or a ρ(32) > 1 witness) is named for after the pause, on the author's go only.
- The reviewer's X8 priors, on record: bound closes for all N 40 / ρ(32) > 1 witness 25 / undecided 35.
