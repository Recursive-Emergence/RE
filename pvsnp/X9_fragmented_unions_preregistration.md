# X9: the loose Union Lemma under exponential fragmentation. Pre-registration

*Drafted 2026-09-11 on branch `x9-fragmented`, on the author's go ("Draft and run X9, push after merge"), for the reviewer's ruling before any work. Documents plus computation; `formal/` closed. g5 for every bound. **The practice from X8 applies:** every table starts at the smallest case, and "compared against which bound" is written next to every number.*

## Target (the reviewer's)

**The loose Union Lemma (loose UL) for IP2:** |Adv(IP2, q₁ ∪ … ∪ q_m)| ≤ poly(m)·2^{1.75n}, with q_j blocky and m = poly(n).
- By the narrowing lemma (X8), it is open only when some block's row-type count K exceeds 2^{n/2}/poly(n).
- **(a) Witness search:** a union of poly(n) blocky matrices, exponentially fragmented and non-cancelling, with advantage > poly·2^{1.75n}.
- **(b) Structure:** does exponential K force cancellation, via Adv = 2^n·Σ_τ ⟨1_{A_τ}, \hat{1_{U_τ}}⟩? Test on block-Equality families (must give ≈ 0) and AND-rectangle families (must give 2^n − 3^n).

## Flags raised before any work (mine)

**Flag S (the scale a witness must reach, from the smallest case up).**
- Tensor unions have per-bit growth log₂(N + E⁻(N))/log₂N:
  - **N = 2: log₂3 = 1.585** (the AND family, 3^n);
  - N = 4: log₂8/2 = 1.5;
  - N = 8: log₂21/3 = 1.464;
  - decreasing, since (N + E⁻)/N^{1.75} ≤ 0.805 for N ≥ 8.
- **So the best tensor union reaches 2^{1.585n}, against the loose bound 2^{1.75n}.** A witness must be **non-tensor** and must beat the AND family by 2^{0.165n}.

**Flag C (the complement view; how a witness would have to look).** Adv(IP2, U) = 2^n − Adv(IP2, C), with C = ∩_j (J − q_j) an intersection of m *co-blocky* sets.
- For the AND family, C is disjointness {x ∧ y = 0}, where IP2 ≡ 0. So Adv(C) = |C| = 3^n.
- **A witness needs C (or U) of size ≫ 2^{1.75n} that is heavily biased under IP2**: a large, nearly monochromatic subset of IP2's matrix cut out by poly(n) non-equality constraints.
- The *whole* 0-set of IP2 would need exponentially many blocky sets to carve (Pitassi–Shirley–Shraibman-type nondeterministic Equality-oracle lower bounds; to be checked, not assumed). A witness has to sit strictly between disjointness (3^n) and the full 0-set (≈ 4^n/2).

**Flag F (the fragmentation of the known families, to be computed).** The AND family (m = n) has row types τ(x) = the support pattern of x, so K is large, about 2^{n−1} per block. **It is itself an exponentially fragmented, non-cancelling union**, with advantage 2^{1.585n} (loose-safe). The witness search starts from it, as the reviewer said, and asks which modifications raise the exponent above 1.75.

**Flag P (a proof route for (b) to try: the complement Fourier bound).** Bound |Adv(IP2, C)| for C an intersection of m co-blocky sets directly, e.g. by Fourier expansion of ∏_j (1 − 1_{q_j}) and IP2's diagonal structure. The first step where the count leaves poly(m)·2^{1.75n} gets named.

**Flag N (the numerics design).** At n ≤ 10:
- greedy and annealed unions over pools of AND-type rectangles, block-Equality sets, exact-threshold slices and random blocky sets;
- report max |Adv| **next to 2^{1.585n} (the AND family) and 2^{1.75n} (the loose bound)**, and the fragmentation K of the best union.

At n ≤ 10 the exponents are blurred by constants, so the numerics can *find* a witness but cannot confirm the absence of one.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X9a** | A witness: the loose UL is false, and the threshold question is reset. |
| **X9b** | A proved cancellation lemma for exponential K: the loose UL is proved and linear alternation depth follows. Re-derived twice. |
| **X9c** | Neither: the named stall inside (b). |

**Priors.**
- Reviewer: X9c 55 / X9a 25 / X9b 20.
- Mine: **X9c 65 / X9a 15 / X9b 20.** Flag S: the best known family sits 2^{0.165n} below the loose bound, and tensor families are proved capped. A witness needs a non-tensor, strongly biased structure that the literature's nondeterministic Equality-oracle lower bounds may exclude.

## Ceiling

X9 proves nothing about P vs NP. At best it settles the loose Union Lemma, which would move one decision-list threshold to linear alternation depth (up to re-absorption).
