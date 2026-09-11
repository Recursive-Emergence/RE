# X6: the direct Fourier route to the Union Lemma. Pre-registration

*Drafted 2026-09-11 on branch `x6-fourier-route`, on the author's go ("Draft and run X6, then final page, push after merge"), for the reviewer's ruling before any work. Documents plus proof sketches plus labelled numerics; `formal/` closed. g1, g5, g8 and g9 apply. The suspicion protocol applies to any positive result (X6c): two independent re-derivations before any label. This is the last attempt of the phase. The final-page update (X4–X6) follows, and then the loop pauses.*

## Target (the reviewer's)

**The Union Lemma for IP2 (tight form):** |Adv(IP2, q₁ ∪ … ∪ q_m)| ≤ poly(m)·2^{1.5n} for blocky q_j. The route is IP2's diagonal Fourier structure,

  Adv(IP2, U) = Σ_x Σ_{y∈U_x} (−1)^{x·y} = 2^n·Σ_x \hat{1_{U_x}}(x),  where \hat g(s) = 2^{−n}·Σ_y g(y)(−1)^{s·y}.

- **(a)** The single-blocky case in this form: recover 2^{1.5n} through Parseval.
- **(b)** The two-blocky case exactly: the cross term through the blocky intersection.
- **(c)** General m, by inclusion–exclusion or otherwise. Name the first step where the count exceeds poly(m).
- **(d) Kill:** block-Equality families with N = 2, 4, 8, and random large-weight slices, numerically, against (c)'s bound.

## Flags raised before any work (mine)

**Flag B (X6b as framed cannot occur at m = 2).** Lemma T (X5) already gives Adv(IP2, q ∪ q′) ≤ 3·2^{1.5n}: inclusion–exclusion over q, q′ and q ∩ q′, each blocky. So "the two-blocky case already needs 2^{Ω(·)}" is ruled out in advance.
- X6b is re-read as **a witness at m ≳ n/4** (Flag W of X5).
- The natural candidate is a *tensor family*, one blocky q_b per block of b bits. Its advantage is 2^n − ∏_blocks ⟨H_N, J − q_b⟩, so a witness needs |⟨H_N, J − q_b⟩| > N^{1.5}(1 + ε) per block. That in turn needs a blocky q_b with near-extremal advantage on H_N, close to the trace bound N^{1.5}.
- The run computes max |⟨H_N, q⟩| over blocky q **exhaustively for N = 4** and by search for N = 8. X5's numerics suggest single-slice advantages ≈ N^{1.05}–N^{1.2}, far below N^{1.5}.

**Flag F (a fragmentation bound, to be proved in the run).** Group rows by their *type* τ(x) = (t₁(x), …, t_m(x)), the index of the block of each q_j containing row x (or ⊥). Rows of one type share U_x =: U_τ. Parseval per type gives

  Adv(IP2, U) = 2^n·Σ_τ Σ_{x∈A_τ} \hat{1_{U_τ}}(x) ≤ 2^{n/2}·Σ_τ √(|A_τ|·|U_τ|).

Splitting U_τ ⊆ ∪_j B^{(j)}_{τ_j} should give **Adv ≤ m·√K·2^{1.5n}**, where K is the maximum number of row types inside a single block A^{(j)}_t.
- *Sketch:* √(Σ) ≤ Σ√, then Cauchy–Schwarz inside each block over its K types. To be proved or corrected in the run.
- **Consequence, if it holds:** the tight Union Lemma holds whenever the type fragmentation K ≤ poly(m).

**Flag S (the expected stall: fragmentation versus cancellation).** In the reviewer's HML family (2-bit block Equalities, m = n/2), the type τ(x) determines x, so every A_τ is a single row. The per-type bound is then trivial (≈ 2^{2n}), while the true advantage is 0 by cancellation across types. This is the same cancellation the operator-norm route discarded. **Expected outcome: X6a**, with the failing step named as "row-type fragmentation: the per-type Parseval bound cannot see cross-type cancellation."

## Outcomes (the reviewer's, with Flag B's re-reading)

| Code | Outcome |
|---|---|
| **X6a** | poly(m) at the two-blocky level (given, by Lemma T), and a named failing step at general m: the lemma under the Union Lemma. |
| **X6b** | Re-read per Flag B: a witness at m ≳ n/4 exceeds poly(m)·2^{1.5n}. The tight UL is false, which is X5c retroactively. |
| **X6c** | poly(m) goes through in general. Re-derived twice before any label; it would be the program's first new bound (linear alternation depth, up to re-absorption). |

**Priors.**
- Reviewer: X6a 55 / X6b 25 / X6c 20.
- Mine: **X6a 65 / X6b 15 / X6c 20.** Flag B removes X6b at small m, and a tensor witness needs near-extremal blocky advantage on H_N, which X5's numerics do not suggest.

## Ceiling

X6 proves nothing about P vs NP. At best it proves the Union Lemma in some regime, which moves one decision-list threshold. After X6, the final page is updated and the loop pauses.
