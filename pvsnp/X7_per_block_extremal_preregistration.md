# X7: the per-block extremal problem. Pre-registration

*Drafted 2026-09-11 on branch `x7-per-block-extremal`, on the author's go ("Run X7, then final page, push after merge"), for the reviewer's ruling before any work. This is a computation. Exact values are labelled exact, and searches are labelled searches. `formal/` closed. g5 and g9 apply.*

## Definitions (the reviewer's)

- E(N) := max over blocky q ⊆ [N]×[N] of ⟨H_N, q⟩, and E⁻(N) := max over blocky q of −⟨H_N, q⟩, for the Sylvester Hadamard H_N.
- A tensor union of n/b blocks (N = 2^b) has |Adv(IP2, U)| ≈ (N + E⁻(N))^{n/b}. So the **per-block factor is ρ(N) := (N + E⁻(N))/N^{1.5}**.
  - The tight Union Lemma fails via tensor unions **iff ρ(N) > 1 for some N**.
  - That happens in particular if E⁻(N)/N^{1.5} → 1, since then ρ = E⁻/N^{1.5} + N^{−1/2}.
- Known so far:
  - ρ(4) = 1 exactly (X6, exhaustive): E⁻(4) = 4, E(4) = 6.
  - ρ(8) ≥ 21/22.63 = 0.928.
  - ρ(16) ≥ 61/64 = 0.953 (searches).
  - The reviewer's independent exact values at N = 8: E(8) = 16 and E⁻(8) = 13, so ρ(8) = 21/22.63 exactly.

## Method

- **The decoupling reduction (the reviewer's; to be proved in the report).** For a fixed family of disjoint nonempty column sets {B_i}, rows decouple, since each row joins at most one block:
  E⁻(N) = max_{{B_i}} Σ_x max(0, max_i −(H 1_{B_i})(x)), and likewise E with the sign flipped.
  - The number of families is Bell(N+1) − 1: 51 at N = 4 and 21,146 at N = 8.
- **N = 4 and 8: exact**, by enumerating all families. Report the extremal families and the rows they take.
- **N = 16:** Bell(17) ≈ 8·10^10 families, too many naively. In order:
  - (i) an exact MILP via scipy's HiGHS, if it closes within a time limit;
  - (ii) else a column-family local search under the decoupled objective, labelled as a search.
  - Orbit enumeration under AGL(4,2) is not attempted unless (i) fails and time permits.
- **(b) Monochromatic rectangles:** the maximum area of an all-(−1) and of an all-(+1) rectangle of H_N, exhaustive over row subsets for N ≤ 16.

## Flags raised before any work (mine)

**Flag F (the sign to watch).** The tensor factor uses N + E⁻, not E. The +1 side gives |N − E| = E − N, which is smaller. The report tracks ρ(N), not E/N^{1.5}.

**Flag D (the trend is not yet a trend).** ρ = 1.000, 0.928 and ≥ 0.953 at N = 4, 8, 16 is non-monotone, so no extrapolation. A witness needs ρ(N) > 1 at a *single* N, and tensor powers then give exponential growth at constant b. The report states ρ(16) as exact or as a lower bound, and does not conclude beyond it.

**Flag L (the Lindsey-tightness structure).** ρ → 1 would need blocks nearly saturating Lindsey with the −1 sign: |Σ_{A×B} H| ≈ √(N|A||B|) and Σ_i √(|A_i||B_i|) ≈ N. The report checks how close the extremal N = 8 and N = 16 families come to both, and compares with the maximum −1 rectangle area. That area is expected to be N/2, and it would forbid monochromatic √N×√N blocks, but not non-monochromatic Lindsey-saturating ones.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X7a** | E⁻/N^{1.5} → 1 (a constructive family), or ρ(N) > 1 found at some N. The tight Union Lemma is false via tensor unions: X5c retroactively. |
| **X7b** | E⁻ ≤ (1 − c)N^{1.5}, proved or strongly indicated; tensor families are harmless. |
| **X7c** | The exact E(N) is determined with its structure. |

**Priors.**
- Reviewer: X7a 40 / X7b 45 / X7c 15.
- Mine: **X7a 30 / X7b 50 / X7c 20.** Flag D: the trend is not monotone, and ρ(8) < 1.

## After X7

The final-page update covers X4–X7, and then the loop pauses.
