# X3: four paths toward the missing measure. Pre-registration

*Drafted 2026-09-10 on branch `x3-measure-paths`, on the author's go ("Draft and run X3, push after merge"), for the reviewer's ruling before any work. g1, g5, g8 and g9 apply.*

*The author's decision on Path B's formal statement: **"No, keep formal/ closed."** Path B's statement is written here in precise markdown with explicit quantifiers, not in Lean. `formal/` stays untouched, and the no-sorry record stands.*

## The specification (the reviewer's, from X1–X2)

We want a measure μ on two-party functions such that:
1. μ is small on short decision lists of exact thresholds, including CM's F_n. This already excludes spectral and rectangle measures.
2. μ(IP2) is large.
3. μ is roughly additive under decision-list composition.

## Paths and kill tests (the reviewer's, verbatim in content)

- **A: Equality-oracle communication.**
  - Chattopadhyay–Lovett–Vinyals 2019, "Equality alone does not simulate randomness", and Pitassi–Shirley–Shraibman 2023: exact statements, the measure each uses, and the function it is proved for.
  - Does the measure survive weighted exact-threshold queries a(x) = b(y)? Does it give anything for IP2?
  - *Kill:* the measure is Equality-specific or already spectral.
- **D: the fold-exponent hierarchy.** Find the best known sign-rank lower bound inside THR∘THR.
  - *Kill:* if some THR∘THR function has sign-rank 2^{Ω(n)}, L1 dies.
  - Otherwise, state "the sign-rank exponent of THR∘THR is bounded away from 1", with the known exponent.
- **B: L0 restated.** "No short decision list of weighted diagonals (a(x) = b(y) gates) computes a bent function", with IP2 as the instance.
  - Give a first invariant that is neither spectral nor rectangle-based, and test it on CM's F_n first.
- **C: the algorithmic route.** Impagliazzo–Paturi–Schneider 2013, Alman–Chan–Williams 2016, Chen–Santhanam–Srinivasan 2016: the lower bounds, the SAT algorithms behind them, the wire frontier, and whether the gap is one of technique or of scale. No attempt.
- **Filter F (a reading).** By Book's transfer, the general fold hierarchy needs non-relativizing arguments. A fixed-class statement is not subject to that.

## Flags raised before any work (mine)

**Flag L (the author's decision).** B's statement goes in this document only.
- Fully quantified: ∀ polynomials p, ∃ n₀, ∀ n ≥ n₀, and every list ((a_i, b_i, o_i))_{i≤ℓ} with ℓ ≤ p(n), where a_i, b_i : {0,1}ⁿ → ℤ and o_i ∈ {0,1}, has some x, y with L(x, y) ≠ IP2(x, y).
- L(x, y) := o_j for the least j with a_j(x) = b_j(y), and a default output otherwise.

This is exactly "IP2 has no poly-length DL-ETHR". A weighted exact threshold Σw_i x_i + Σv_i y_i = t is a(x) = b(y) with a(x) = Σw_i x_i and b(y) = t − Σv_i y_i. Conversely, a general a(x) = b(y) with *arbitrary* functions a and b is **strictly more general** than an exact threshold.
- The report must say which of the two B means. Arbitrary a and b give "decision lists of Equality oracles on arbitrary encodings", which is a *different, stronger* model. Its lower bounds imply L0, not the other way round.

**Flag B (B's first candidate dies on a single Equality, before F_n).** "Distinct row patterns" is killed already by EQ itself: the identity matrix has 2^n distinct rows. Any candidate must be small on one Equality first. Measures that are small on EQ:
- randomized communication (O(1) public-coin), which is log-scale, and X2 showed it caps at linear;
- sign-rank (constant for EQ, if verified), which fails on F_n;
- approximate rank (small for EQ, if verified), whose status on F_n and IP2 is to be checked.

The report tests B's candidates against EQ, then F_n, then IP2, in that order.

**Flag S (the specification has a scale conflict).** Clue (3), additivity over the list, combined with clue (2) needs μ(IP2) ≥ ℓ · max μ(query) for superpolynomial ℓ.
- A **log-scale** measure (communication cost) is at most n + 1 on IP2, which has the trivial protocol. So additivity can certify at most ℓ ≈ n/μ(EQ): linear. That is X2's cap again.
- So μ must be an **exponential-scale** measure that is polynomial on EQ-type gates, additive over lists, and small on F_n, where sign-rank is not. The report states this as the sharpened spec. If no known measure has that shape, it says so (g8).

**Flag A (Equality oracles bear on L0 only through polylog cost).** IP2 has a trivial n-bit protocol, so an Equality-oracle lower bound helps only if **poly-length DL-ETHR ⊆ P^EQ at polylog cost**. CM's PMA protocol uses binary search with **OR∘EQ** queries (MA), not bare EQ.
- Whether short DL-ETHR has polylog-cost P^EQ protocols is the containment the report must settle from a statement.
- If it has none, Path A's lower bounds (for P^EQ) do not reach L0, and A dies at containment, not at the measure.

**Flag D.** Sherstov–Wu's exp(Ω(n^{1−ε})) is for AC⁰, and whether those circuits are in poly-size THR∘THR is not stated (X1). Even if they were, n^{1−ε} is o(n), so they would not kill L1. The kill needs a 2^{Ω(n)} exponent.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X3a** | A candidate μ survives its kill test on at least one path; the next attempt is on it. |
| **X3b** | All four paths die at their kill tests. The spec is recorded as the open object with four named failures. B's statement stands *in this document*, per the author's decision. |
| **X3c** | D kills L1 outright. Record it and reroute. |

**Priors.**
- Reviewer: X3b 45 / X3a 35 / X3c 20.
- Mine: **X3b 55 / X3a 25 / X3c 20.** X3b is raised by Flags B, S and A: B's first candidate is dead on EQ, the spec has a scale conflict, and A may fail at containment.

## Ceiling

X3 proves nothing. At best it names a surviving candidate measure. At worst it records the sharpened spec with four failures.
