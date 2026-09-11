# X5: the Union Lemma. Report

*Run 2026-09-11 on branch `x5-union-lemma`, on the author's go ("Draft and run X5, push after merge"), against the pre-registration (962f8b5), accepted by the reviewer with Flags G, T, W and N and priors X5b 60 / X5c 25 / X5a 15. Documents plus proof sketches, plus a small numerical exploration labelled as such; `formal/` closed. g1, g5, g8 and g9 applied. Strongest suspicion protocol: no positive claim beyond the elementary lemmas in §2, each proved below.*

## 0. Outcome

**X5b.**
- **The γ₂ route dies**, as expected: the γ₂ of a union of m blocky matrices is exponential in m.
- **No witness to a counterexample** was found, analytically or in a small-n greedy search.
- **The direct IP2 route stalls at one named step,** the **Hadamard masking lemma** (§4):
  > for blocky q₁…q_m and C = ∏_l (1 − q_l), ‖H ∘ C‖_op ≤ poly(m)·2^{n/2}.
  - It implies the tight Union Lemma for IP2, and so the loose one.
  - The only general tool (γ₂ as a Schur multiplier) gives 2^m·2^{n/2}.
  - Numerically, at n ≤ 10, the norm stays ≤ 1.48·2^{n/2} (exploratory; §5).
- **Quantitative gains, stated as exactly what they are** (the ruling):
  - **Lemma T**, for IP2: the Union Lemma holds for m ≤ n/4 unconditionally.
  - **Lemma T′**, general: it holds for any f when m ≤ ½·log₂(1/d) − O(1).
  - **Lemma S:** Lemma 44's single-blocky bound sharpens from √d to O(d).
  - **Each gives only a constant factor in the alternation threshold, which stays Θ(n/log n).** Nothing here moves it to linear depth.

## 1. Sources read in this run

- **Pitassi–Shirley–Shraibman**, ITCS 2023 (primary, author PDF), §2 "The γ2 norm and variants":
  - "γ2(A) = min_{XY^⊤=A} r(X)r(Y)";
  - "By an application of norm duality and Grothendieck's Inequality, for any real matrix A we have γ2(A) ≤ ν(A) ≤ µ(A) ≤ 4K_G γ2(A)";
  - "The µ-norm of a matrix is the minimum of Σ_i |α_i| over {α_i}, {R_i} where Σ_i α_i R_i equals the matrix" (R_i rectangles).
- **Podolskii–Prior** (carried from X4): Lemma 44 and Theorem 45.
- **Used but not re-read (standard):** γ₂ is submultiplicative under the Schur (entrywise) product; γ₂ is multiplicative under tensor product; the Hadamard matrix has ‖H‖ = 2^{n/2}; ⟨A, B⟩ ≤ ‖A‖_op·‖B‖_tr.

## 2. The elementary lemmas (ours; g5; proofs)

**Blocky facts.** A blocky M = Σ_t 1_{A_t}1_{B_t}^⊤ has row-disjoint A_t and column-disjoint B_t.
- (i) **γ₂(M) ≤ 1.** Take X_x = e_{t(x)} (or 0) and Y_y = e_{t(y)} (or 0); then XY^⊤ = M with rows of norm ≤ 1.
- (ii) **‖M‖_tr ≤ 2^n.** ‖M‖_tr = Σ_t √(|A_t||B_t|) ≤ √(Σ|A_t|·Σ|B_t|) by Cauchy–Schwarz.
- (iii) **Intersections of blocky matrices are blocky:** {a(x) = b(y)} ∩ {a′(x) = b′(y)} = {(a, a′)(x) = (b, b′)(y)}.

**Lemma S (sharper single-query bound, any f).** Adv(f, M) ≤ 4K_G·γ₂(M)·4^n·Disc_U(f). In particular Adv(f, blocky) ≤ 4K_G·4^n·d.
- *Proof.* By PSS, M = Σ α_i R_i with Σ|α_i| = µ(M) ≤ 4K_G·γ₂(M).
- So Adv(f, M) = Σ α_i Adv(f, R_i) ≤ µ(M)·max_R |Adv(f, R)|, and max_R |Adv(f, R)| = 4^n·Disc_U(f) (PP25's identity "Adv(R, f) = 2^{2n} Disc_U(R, f)"). ∎
- *Compare:* Lemma 44 gives 2^{2n+1}√d. Since d ≤ √d, Lemma S is stronger.

**Lemma T (IP2, the ruling's (i)).** For a single blocky M, Adv(IP2, M) = ⟨H, M⟩ ≤ ‖H‖·‖M‖_tr ≤ 2^{n/2}·2^n = 2^{1.5n}. For m ≤ n/4 blocky matrices, inclusion–exclusion over the blocky intersections (iii) gives
  |Adv(IP2, ∪_{j≤m} q_j)| ≤ (2^m − 1)·2^{1.5n} ≤ 2^{1.75n}.
**So the tight-normalization Union Lemma holds for IP2 for all m ≤ n/4, unconditionally.** ∎

**Lemma T′ (any f).** 1_U = J − ∏_j (J − q_j), a Schur product, with γ₂(J − q_j) ≤ 2. So γ₂(1_U) ≤ 1 + 2^m, and by Lemma S, Adv(f, U) ≤ 4K_G(1 + 2^m)·4^n·d. This is ≤ the loose A = 2^{2n+1}√d whenever 2^m ≲ 1/(2K_G√d), i.e. **m ≤ ½·log₂(1/d) − O(1).** ∎

## 3. (a) The γ₂ route, and why it dies (Flag G, re-checked)

- **Exponential.** Take m disjoint blocks of b = n/m bits, N = 2^b. The complement of OR_m∘EQ_block is ⊗_i (J_N − I_N).
  - γ₂ is multiplicative under ⊗, and γ₂(J_N − I_N) ≥ ‖J_N − I_N‖_tr/N = (2N − 2)/N. So **γ₂ ≈ (2 − 2/N)^m, exponential in m.**
  - Lemma S's route to the Union Lemma therefore caps at m = O(log(1/d)), which is Lemma T′.
- **Harmless against IP2.** Adv(IP2, ⊗(J − I)) = ∏_i Adv(IP_N, J − I). Adv(IP_N, J) = N (only the x = 0 row sums to N), and Adv(IP_N, I) = Σ_x (−1)^{|x|} = 0. So each factor is N and the product is 2^n. Hence Adv(IP2, OR_m∘EQ) = Adv(IP2, J) − 2^n = 2^n − 2^n = **0**.
- **Numerically confirmed:** 0 for m = 2 and m = 4 at n = 8, and m = 2 at n = 10 (§5).

**Verdict (a):** the γ₂ route to the Union Lemma dies at m ≈ ½log(1/d). The family that kills it is not a witness against the lemma. So the lemma, if true, is f-specific (discrepancy is not enough), as the reviewer anticipated.

## 4. (c) The direct IP2 route, and its named stall

**The reduction (ours, elementary).** Disjointify: 1_U = Σ_j q_j ∘ C_j with C_j = ∏_{l<j} (J − q_l). Then
  Adv(IP2, U) = Σ_j ⟨H ∘ C_j, q_j⟩ ≤ Σ_j ‖H ∘ C_j‖_op·‖q_j‖_tr ≤ m·max_j ‖H ∘ C_j‖_op·2^n.

**Hence the Hadamard masking lemma (HML)**
  ‖H ∘ C‖_op ≤ poly(m)·2^{n/2} for C = ∏_{l≤m} (J − q_l), q_l blocky,
**implies the tight Union Lemma for IP2**: Adv ≤ poly(m)·2^{1.5n}. That implies the loose one, which implies linear alternation depth (≈ 0.36n) via X4's recursion, with re-absorption as the residual (d).

**Where it stalls.** The one general tool is the Schur-multiplier bound ‖H ∘ C‖_op ≤ γ₂(C)·‖H‖. That gives 2^m·2^{n/2}, and γ₂(C) is genuinely exponential (§3). On §3's family the true value is much smaller:
- H_N ∘ (J − I) = H_N − D with D = diag((−1)^{|x|}), and the product structure gives ‖H∘C‖ ≤ ∏(√N + 1).
- For single-bit blocks (N = 2), H₂ ∘ (J − I) is a permutation matrix, so ‖H∘C‖ = 1.

So the stall is precise: **no tool is known here that bounds ‖H∘C‖ better than γ₂(C)·‖H‖ for complements of unions of blocky matrices** (g8: not found in the sources read).

**Why HML is not automatic.** Masks can inflate Hadamard norms. For example, H ∘ 1_{H>0} has norm ≈ 2^n/2, so HML must use the blocky structure of the q_l. A large ‖H∘C‖ would need C correlated with H's sign pattern. By the reduction that would mean a union of few blocky matrices with large IP2-advantage, which is the Union Lemma itself. **The two statements stand or fall together**, and neither is proved.

## 5. (b) The kill search (exploratory numerics; not evidence about asymptotics)

The script is in the job's scratch directory. Pools of random exact-threshold slices {w·x + v·y = t} with weights in [−3, 3], and greedy unions maximizing |Adv(IP2, U)|:

| n | single slice max | greedy union, m = 12 | greedy, m = 24 | 2^{1.5n} | loose A = 2^{1.75n+1} |
|---|---|---|---|---|---|
| 8 | 800 | 1930 | 2055 | 4096 | 32768 |
| 10 | 1408 | 4800 | — | 32768 | 370728 |

- **The greedy union advantage grows sublinearly in m** and stays **≤ 0.5·2^{1.5n}**. No witness.
- **The masked norm** ‖H ∘ (1 − 1_U)‖ over random unions (m ≤ 16 at n = 8, 60 trials; m ≤ 12 at n = 10, 12 trials) stays **≤ 1.48·2^{n/2}**, consistent with HML.
- Trace norms of slices are ≤ 2^n, and single-slice advantages are ≤ 2^{1.5n}, both as Lemma T predicts.
- **Limits:** small n; random and greedy families, not adversarial; weights ≤ 3. Large-weight slices (the priority family of Flag W) are only partly covered, since weights up to 3 at n ≤ 10 give moderate resolution. Theorem 50-style block families were **not run** (g8: not searched).

## 6. The batching arithmetic (the ruling's (ii)), with Lemma S

- **PP25's recursion.** Covered b-entries ≤ 2^{2n+k}·A_*·∏ s_j, with A_* the single-query advantage bound. Balance gives ∏ s_j ≳ 4^n/(2^k A_*).
- **Batching** a layer into groups of ≤ β queries, each group's union charged once, replaces s_j by ⌈s_j/β⌉ and A_* by 2^β·A_* (Lemma T′/T).
- **For IP2 with A_* = 2^{1.5n}** (Lemma T) and β = n/4: (4s/n)^k ≳ 2^{n/4}/2^k.
  - With s = n^c: k·((c − 1)·log n + O(1)) ≳ n/4, so k* ≈ n/(4(c − 1)·log n).
  - Unbatched with Lemma 44's A: k* ≈ n/(4c·log n). **The ratio is c/(c − 1): a constant factor.**
- **With Lemma S unbatched** (A_* = 4K_G·4^n·d, d = 2^{−n/2}): s^k ≳ 2^{n/2}/2^k, so k* ≈ n/(2c·log n). **A factor of 2 over PP25: a constant.**
- **The ruling's statement is confirmed:** factor ≈ n per layer from batching, a constant factor in the alternation threshold, and **the threshold stays Θ(n/log n), i.e. superpolynomial exactly for k = o(n/log n)**. Nothing larger came out of the arithmetic, so no re-derivation beyond this check was needed.

## 7. (d) Re-absorption

Unchanged from X4 (07c0953). Even the full Union Lemma yields only k ≲ 0.36n, because later layers can overlap all earlier opposite-value coverage.

## 8. Priors against outcome

| | X5a | X5b | X5c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 15 → 15 | 55 → 60 | 30 → 25 |
| mine | 15 | 60 | 25 |
| **outcome** | | **X5b** | |

No misses on either side in this round's pre-registered claims. Flags G, T, W and N all held. Flag W's priority family was only partly searched, and that is recorded in §5.

## Formal record

Untouched (the author's decision).
