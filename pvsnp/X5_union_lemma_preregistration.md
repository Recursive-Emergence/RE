# X5: the Union Lemma. Pre-registration

*Drafted 2026-09-11 on branch `x5-union-lemma`, on the author's go ("Draft and run X5, push after merge"), for the reviewer's ruling before any work. Documents plus proof sketches; `formal/` closed. g1, g5, g8 and g9 apply. **The strongest suspicion protocol:** a positive result (X5a) is re-verified from scratch by a second derivation before any label, and until then it stays unlabelled.*

## The statement (from X4 §4)

**Union Lemma (UL).** For f: {0,1}ⁿ×{0,1}ⁿ → {0,1} with Disc_U(f) ≤ d, and blocky matrices q₁, …, q_m,
  |Adv(f, q₁ ∪ … ∪ q_m)| ≤ poly(m)·2^{2n}√d.
If UL holds, Podolskii–Prior's recursion moves from o(n/log n) to alternation depth ≈ 0.36n (X4, 07c0953). Re-absorption remains the obstruction beyond that.

## Targets (the reviewer's, verbatim in content)

- **(a) The γ₂ route first.** A single blocky matrix has γ₂ ≤ 1. A Linial–Shraibman-type bound gives advantage ≤ γ₂(M)·(disc-type quantity), with the exact inequality and constants from a source. So UL follows if γ₂(1_{∪q}) ≤ poly(m). Check the EQ-oracle literature (Hambardzumyan–Hatami–Hatami; PSS; CLV) for the γ₂ of an OR of m blocky matrices. The reviewer expects it to be exponential.
- **(b) The kill test for UL itself.** Look for a union of m blocky matrices whose advantage against IP2 exceeds poly(m)·2^{2n}·2^{−n/4}. Try families from PP25 Theorem 50 and unions of generalized diagonals.
- **(c)** If (a) is exponential and (b) finds no witness, attempt a direct IP2-specific bound (Fourier/spectral) and name where it stalls.
- **(d)** Re-absorption stays the obstruction after UL, as in 07c0953.

## Flags raised before any work (mine; computations are sketches to be re-checked in the run)

**Flag G (the γ₂ route dies, and its witness is harmless against IP2).**
- Take m disjoint blocks of N = 2^{n/m} bits. The complement of OR_m∘EQ_block is ⊗_i (J_N − I_N).
- γ₂ is multiplicative under tensor products, and γ₂(J_N − I_N) ≥ ‖J_N − I_N‖_tr / N = (2N − 2)/N = 2 − 2/N. So γ₂ ≈ (2 − 2/N)^m, exponential in m, which confirms the reviewer's expectation.
- But **its advantage against IP2 is tiny.** Both IP2's sign pattern and this matrix tensorize, so Adv(IP2, ⊗(J − I)) = ∏_i Adv(IP_N, J − I) = ∏_i (N − 0) = 2^n. Hence Adv(IP2, OR_m∘EQ) = Adv(IP2, all) − 2^n = 0.
- So γ₂ dies as a *route*, while this family is no *witness* against UL. UL, if true, must be IP2-specific or discrepancy-specific, as the reviewer anticipated.

**Flag T (IP2 has spectral slack: UL holds for m ≤ n/4 already).**
- For IP2's Hadamard matrix H (‖H‖ = 2^{n/2}): Adv(IP2, M) = ⟨H, M⟩ ≤ 2^{n/2}·‖M‖_tr.
- A blocky matrix has ‖M‖_tr = Σ_t √(|A_t||B_t|) ≤ 2^n by Cauchy–Schwarz, since the blocks are row- and column-disjoint. So **a single blocky matrix has IP2-advantage ≤ 2^{1.5n}**. Lemma 44's general bound, with d = 2^{−n/2}, gives only A ≈ 2^{1.75n+1}.
- Intersections of blocky matrices are blocky, so inclusion–exclusion gives Adv(IP2, ∪_{j≤m} q_j) ≤ 2^m·2^{1.5n} ≤ 2^{1.75n} **for m ≤ n/4**. That is UL for IP2 up to m = n/4, for free.
- **Consequence to check in the run:** a layer can be split into same-output batches of ≤ n/4 queries. Each batch is charged the fixed opposite-value coverage once. That replaces PP25's per-layer factor s_i by ≈ 4s_i/n: a factor-n improvement per alternation, not a threshold change.

**Flag W (where a witness must live).** By Flag T, any counterexample to UL against IP2 needs **m ≳ n/4** blocky matrices with coherent advantage: at least 2^{n/4}/poly(m) worth of inclusion–exclusion mass. Search families with m ≥ n/4:
- unions of large-weight exact-threshold slices;
- Theorem 50's INT⁽ᵏ⁾-style block structures;
- unions of "orthogonal" rectangles {x_T = 0} × {y_{T^c} = 0}, where IP2 ≡ 0. Each has size 2^n, so unions are small.

**Flag N (the normalization).** UL as stated uses Lemma 44's A = 2^{2n+1}√d, which is loose for IP2 by 2^{n/4}. The report states both the *loose* UL, which is what the recursion needs, and the *tight* IP2 version, Adv ≤ poly(m)·2^{1.5n}. The loose one may hold even if the tight one fails.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X5a** | UL proved (γ₂ of unions polynomial, or a direct bound); the threshold moves to linear depth. Re-verified by a second derivation before any label. |
| **X5b** | γ₂ exponential, no witness, and the direct route stalls at a named step. UL is open, IP2-specific, and stated. |
| **X5c** | A witness kills UL. The multiplicative loss is necessary at the union step, and the measure must change. |

**Priors.**
- Reviewer: X5b 55 / X5c 30 / X5a 15.
- Mine: **X5b 60 / X5c 25 / X5a 15.** Flag T makes small-m witnesses impossible, which lowers X5c slightly.

## Ceiling

X5 proves nothing about P vs NP. At best UL is proved, and it moves one decision-list threshold from o(n/log n) to linear alternation depth, after re-verification.
