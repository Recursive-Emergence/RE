# X10: the bias-to-monochromatic bridge. Pre-registration

*Drafted 2026-09-11 on branch `x10-bias-bridge`, on the author's go ("ya", after X10 was named in the final page), for the reviewer's ruling before any work. Documents plus proof sketches; `formal/` closed. The X8 practice applies: smallest case first, and the compared bound beside every number.*

## Flag Z first: a correction to X9 (my miss; X9 was accepted with it)

**X9's claim "polynomially many constraints cannot make C monochromatic" is false.** The AND family, with m = n, makes C = disjointness, which is entirely +1 (IP2 ≡ 0 there) and has 3^n entries.

**The error.** Pitassi–Shirley–Shraibman's Theorem 29 bounds C1B(A), the number of blocky matrices needed to *cover the ones of A*, where every covering matrix lies *inside* A. X9 applied it to a union U that merely *contains* a sign class. The AND rectangles contain entries of both signs, so they are not a 1-cover.

**The correct statements (ours; proof sketches, re-checked in the run).**
- **(Z1, exact).** If C equals an *entire* sign class of IP2, then U = J − C equals the other class exactly. U's blocky pieces then lie inside that class, forming a valid 1-cover, and PSS applies: m ≥ Ω(2^{n/2}). This is what X9's §3 actually proves.
- **(Z2, robust; new).** Suppose U covers ≥ (1 − ε) of the −1 class and contains ≤ ε·2^{2n−1} of the +1 entries, with ε ≤ 1/(8m). Then m ≥ Ω(√N) = Ω(2^{n/2}).
  - Each entry lies in ≤ m of U's rectangles, one per blocky matrix, so the rectangles hold ≤ m·ε·2^{2n−1} +1 entries in total.
  - *Impure* rectangles (≥ 1/4 of their entries +1) therefore hold ≤ 3mε·2^{2n−1} of the −1 entries, so the *pure* ones cover ≥ 2^{2n−2}.
  - By Lindsey, a pure rectangle (≤ 1/4 of its entries +1) has area ≤ 4N.
  - PSS's counting (each row and column lies in ≤ m rectangles) then gives m·2N ≥ Σ 2√|R_i| ≥ 2^{2n−2}/√N, so m ≥ √N/8.
  - The +1-class version is symmetric.
- **The final page's §3(iv) sentence** "so polynomially many constraints cannot make C monochromatic" is corrected to "cannot make C (or ε-close to, with ε ≤ 1/(8m)) an *entire* sign class". The correction goes in the X10 report and in the next page update.

## Target (the reviewer's) and its two readings

**The bridge.** If a conjunction C of m co-blocky constraints has |Adv(IP2, C)| ≥ A, then some sub-cube (restricting coordinates of x and y together, so IP2 restricts to IP2 on n′ bits up to a constant) has the restricted C "ε-close to monochromatic with density ≥ δ". Then PSS forces m ≥ Ω(2^{n′/2}·δ).

- **Reading R1: C is ε-monochromatic on the sub-cube with density δ.** **Refuted by the pre-registered kill test (the AND family), before any work.**
  - C = disjointness is monochromatic on the whole cube (n′ = n) with density δ = (3/4)^n, and m = n.
  - R1's conclusion would give m ≥ Ω(2^{n/2}·(3/4)^n) = Ω((3/(2√2))^n) = Ω(1.0607^n), which is false for m = n.
  - This is Flag Z again: monochromatic is not the same as covering a sign class.
- **Reading R2: C is ε-close to an *entire* sign class of IP2_{n′} on the sub-cube, with ε ≤ 1/(8m).** Z2 then gives m ≥ Ω(2^{n′/2}).
  - The bridge's content becomes a **density increment from bias α := A/4^n to near-complete class coverage (density ≈ 1/2, error ≤ 1/(8m)) on a sub-cube of dimension n′**.
  - The loose UL corresponds to α ≈ poly·2^{−n/4}. For it to follow, the increment must reach n′ ≥ 2·log₂m + ω(log n).

## Flags raised before any work (mine)

- **Flag K (the kill tests, fixed as the reviewer set them).** The AND family (α = (3/4)^n, m = n) must give n′ ≤ 2·log₂n + O(1) under R2. The block-Equality family (bias 0) must give nothing. Under R1 the AND family already kills the bridge (above).
- **Flag D (the size of the increment R2 needs).** Going from α ≈ 2^{−n/4} to near-complete coverage with error 1/(8m) is an increment of about 2^{n/4} in relative density. Standard density-increment steps, restricting one coordinate pair at a time, gain a constant factor per step when they work at all. So a gain of 2^{n/4} would cost Θ(n) restricted coordinates, leaving n′ = n − Θ(n). Whether the constant keeps n′ ≥ 2·log₂m + ω(log n) is exactly the question.
- **Flag C (whether any increment step exists).** For IP2, restricting x_i = σ and y_i = τ maps IP2 to ±IP2 on n − 1 bits, and C to a co-blocky conjunction. The *advantage* of C splits over the four (σ, τ) branches, so the best branch has relative bias at least the average: no gain in relative density is automatic. An increment needs a branch where the density-weighted bias grows by a constant factor, and the AND family shows the gain can be as small as 1 per step (disjointness restricts to disjointness). The expected first failing step is **"no branch gains"**: a conjunction whose bias is spread evenly over restrictions, as the AND family's is.

## Outcomes (the reviewer's, with the readings)

| Outcome | Meaning |
|---|---|
| **fails at a named step** | R1 refuted by AND (known now); R2's increment fails at a named step, expected to be "no branch gains", or an increment too weak (n′ = O(log m)). |
| **nontrivial but below the threshold** | R2's increment yields some n′ = ω(log m) but < 2·log₂m + ω(log n) at bias 2^{1.75n}. |
| **loose UL proved** | R2's increment reaches the threshold. Re-derive twice. |

**Priors.**
- Reviewer: 60 / 25 / 15.
- Mine: **80 / 15 / 5.** R1 is already refuted, and R2 needs a density increment of 2^{n/4} with error 1/m. Flag C: the AND family's bias does not concentrate under restriction.

## Ceiling

X10 proves nothing about P vs NP. The Flag Z correction stands regardless of outcome.
