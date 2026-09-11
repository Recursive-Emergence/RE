# X6: the direct Fourier route to the Union Lemma. Report

*Run 2026-09-11 on branch `x6-fourier-route`, on the author's go ("Draft and run X6, then final page, push after merge"), against the pre-registration (bf95adb), accepted by the reviewer with Flag B's re-reading of X6b, the precision on Flags F/S, and priors X6a 65 / X6c 20 / X6b 15. Documents plus proofs plus labelled numerics; `formal/` closed. g1, g5, g8 and g9 applied.*

## 0. Outcome

**X6a.** The Union Lemma for IP2 is a statement about **cancellation across row types** of a union of blocky matrices.
- **Every termwise bound is blind to it:** operator norm (X5, closed by the HML counterexample), Parseval, and per-type inner products bounded one at a time.
- **A proof must sum across types before bounding.** It names the *operation* a proof must perform, not a measure it must find.
- **Proved here (ours, elementary):**
  - the exact type identity (§1);
  - the fragmentation bound, Adv ≤ m·√K·2^{1.5n} (§3). So the tight Union Lemma holds whenever the type fragmentation K is poly(m).
- **Measured (exploratory numerics):**
  - tensor families *reach* the trace bound 2^{1.5n} with m = n/2 queries, and so gain exponentially over the best single blocky set in the same family;
  - they *do not exceed* the trace bound in any search (exhaustive at N = 4; local search at N = 8, 16).
- **No witness: X6b does not occur**, and **X6c does not occur.**

## 1. The exact identity (a), with the reviewer's precision

For U ⊆ {0,1}ⁿ × {0,1}ⁿ, write U_x for row x's column set, and \hat g(s) = 2^{−n}·Σ_y g(y)(−1)^{s·y}. Then
  Adv(IP2, U) = Σ_x Σ_{y∈U_x} (−1)^{x·y} = 2^n·Σ_x \hat{1_{U_x}}(x).
For a union of m blocky q_j, group rows by **type** τ(x) = (t₁(x), …, t_m(x)), where t_j(x) is the block of q_j containing row x, or ⊥. Rows of one type share U_x =: U_τ, so
  **Adv(IP2, U) = 2^n·Σ_τ ⟨1_{A_τ}, \hat{1_{U_τ}}⟩** (exact).
Each per-type term is an **inner product** and keeps within-type cancellation. **Checked numerically:** the exact type-sums equal the advantage in every case of §5.

- **Single blocky (m = 1).** Types are blocks A_t, and U_τ = B_t. Parseval gives |⟨1_{A_t}, \hat{1_{B_t}}⟩| ≤ √|A_t|·√(|B_t|/2^n). So Adv ≤ 2^{n/2}·Σ_t √(|A_t||B_t|) ≤ 2^{1.5n}, which is Lemma T recovered.
- **Two blocky (b).** \hat{1_{B∪B′}} = \hat{1_B} + \hat{1_{B′}} − \hat{1_{B∩B′}}. The third term's row grouping is the blocky intersection q ∩ q′, whose blocks are (A_t ∩ A′_{t′}) × (B_t ∩ B′_{t′}). So |Adv| ≤ 3·2^{1.5n}: poly at m = 2, as Flag B said.

## 2. General m (c): where the count leaves poly(m)

Inclusion–exclusion yields 2^m − 1 blocky terms, each ≤ 2^{1.5n}, a loss of 2^m. The type identity avoids inclusion–exclusion, but a termwise bound on it loses cross-type cancellation (§4).

## 3. The fragmentation bound (Flag F; ours, proved)

**Claim.** Adv(IP2, ∪_{j≤m} q_j) ≤ m·√K·2^{1.5n}, where K = max_{j,t} (number of types τ with τ_j = t).

**Proof.**
1. Parseval per type gives Adv ≤ 2^{n/2}·Σ_τ √(|A_τ|·|U_τ|).
2. Since U_τ = ∪_j B^{(j)}_{τ_j}, we have √|U_τ| ≤ Σ_j √|B^{(j)}_{τ_j}|. So Adv ≤ 2^{n/2}·Σ_j Σ_t √|B^{(j)}_t|·Σ_{τ: τ_j = t} √|A_τ|.
3. The types with τ_j = t partition A^{(j)}_t into at most K parts, so by Cauchy–Schwarz Σ √|A_τ| ≤ √(K·|A^{(j)}_t|).
4. Hence Adv ≤ 2^{n/2}·√K·Σ_j Σ_t √(|A^{(j)}_t||B^{(j)}_t|) ≤ 2^{n/2}·√K·m·2^n. ∎

**Consequence.** The tight Union Lemma holds for IP2 whenever K ≤ poly(m). This is the first *structural* sufficient condition in the program beyond m ≤ n/4 (Lemma T). The bound was checked numerically to dominate both the Parseval sum and |Adv| in every case of §5.

## 4. The stall (Flag S, as the ruling located it)

- The fragmentation bound is the **Parseval relaxation of the exact identity**.
- **Within-type** cancellation is kept by the inner product, and Parseval loses it by taking norms.
- **Cross-type** cancellation, between different τ, is what neither Parseval nor any per-type bound can see.
- **The reviewer's HML family is the extreme case.** For 2-bit block Equalities (m = n/2), τ(x) determines x, so every type is a single row. The per-type bound is then essentially trivial, while the true advantage is **0** by cross-type cancellation alone.
  - At n = 8: Parseval sum 54,185, K = 64, Adv = 0.
  - At n = 10: 915,747, K = 256, Adv = 0.
- This is the same cancellation the operator-norm route discarded in X5.

**The X6a statement:**
> the Union Lemma for IP2 is a statement about cancellation across row types of a union of blocky matrices; every termwise bound (operator, Parseval, per-type inner product bounded termwise) is blind to it; a proof must sum across types before bounding.

## 5. The kill search (d) (exploratory numerics, script `x6_run.py` and `x6_anneal.py` in the job's scratch directory)

**Block-Equality families** (blocks of b bits, m = n/b):

| n | b | m | Adv | K | types | Parseval sum | m·√K·2^{1.5n} | 2^{1.5n} |
|---|---|---|---|---|---|---|---|---|
| 8 | 1 | 8 | 0 | 128 | 256 | 65,408 | 370,728 | 4,096 |
| 8 | 2 | 4 | 0 | 64 | 256 | 54,185 | 131,072 | 4,096 |
| 8 | 4 | 2 | 0 | 16 | 256 | 22,806 | 32,768 | 4,096 |
| 9 | 3 | 3 | 0 | 64 | 512 | 150,608 | 278,046 | 11,585 |
| 10 | 2 | 5 | 0 | 256 | 1024 | 915,747 | 2,621,440 | 32,768 |

**Random exact-threshold slice unions** (weights up to 8, m = 2–5):
- |Adv|/2^{1.5n} ranges 0.004–0.045.
- The exact type-sums equal Adv, and the Parseval sums are 10²–10³ times larger.
- *Example:* n = 8, m = 3: Adv = 37, Parseval sum 25,791.

**Tensor families (Flag B)**, per-block factor max |⟨H_N, J − q⟩| over blocky q:
- **N = 4, exhaustive over all 2^16 matrices, blocky filter:**
  - max |⟨H₄, q⟩| = **6** (trace bound 8);
  - max |⟨H₄, J − q⟩| = **8 = N^{1.5} exactly**.
- **N = 8, random search (2·10⁵) plus annealing:** at most 21, against 22.63.
- **N = 16, annealing:** at most 61, against 64.
- *Consequence (ours):* a tensor union of m = n/2 blocky sets with N = 4 attains |Adv(IP2, U)| = |2^n − (±8)^{n/2}| = 2^{1.5n}·(1 ± 2^{−n/2}). That **saturates** the trace bound, but does not exceed poly(m)·2^{1.5n}. The best single tensor blocky set in the same family reaches only 6^{n/2} ≈ 2^{1.29n}.
- **So unions genuinely gain, by up to (8/6)^{n/2}, over a single blocky set, but only up to the trace bound.** Whether some N gives a per-block factor above N^{1.5}, which would be an X6b witness, is **open** (searched, not proved; the bound |⟨H_N, J − q⟩| ≤ N + N^{1.5} is all we have).

**Limits:** small n; searches, not proofs; N = 8 and 16 not exhaustive.

## 6. What stands after X4–X6 (for the final page)

- **The sharpened open statement** (X3): IP2 against poly-size ELDL of alternation depth ≳ n/log n.
- **The Union Lemma** (X4) would move the threshold to ≈ 0.36n, with re-absorption as the residual.
- **In it, the operation a proof must perform** (X6): sum across row types before bounding, because the operator route (X5, closed by the HML counterexample) and all termwise bounds discard cross-type cancellation.
- **Known partial regimes** (ours, elementary): m ≤ n/4 (Lemma T); any f with m ≤ ½log(1/d) (Lemma T′); K ≤ poly(m) (the fragmentation bound).
- **The tight constant is attained** by tensor unions at m = n/2 (N = 4, exhaustive).

## 7. Priors against outcome

| | X6a | X6b | X6c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 55 → 65 | 25 → 15 | 20 → 20 |
| mine | 65 | 15 | 20 |
| **outcome** | **X6a** | | |

No misses on pre-registered claims. The fragmentation bound was pre-registered as a sketch and is proved as sketched.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as X6a.** The following go in as proved or verified:
- the exact type identity;
- the fragmentation bound: the tight Union Lemma whenever K ≤ poly(m), the first structural sufficient condition beyond m ≤ n/4;
- the N = 4 exhaustive result: the per-block factor equals N^{1.5} exactly.

The reviewer proposes one more item before the pause, X7: the per-block extremal problem E⁻(N)/N^{1.5}. It decides whether tensor unions falsify the tight Union Lemma. It needs the author's go.
