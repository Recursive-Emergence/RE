# W32-B: residual arity k. Pre-registration

*Drafted 2026-09-12 on branch `w32-correlated-assignment`, on the reviewer's W32-B specification, after W32-A §10. Documents only; `formal/` closed; LOCAL commit only.*

**Committed cold: before any computation.**

## §0. Target and ceiling

**Definition 9, deterministic, depth 1; after pre-pinning, residual windows of arity up to `k`**, with `k = poly(n) = polylog N` at the line's scale. **Reviewer's framing question, to answer before any mechanism:** is the protected set still an independent set (at most one protected input per window, a **strong** independent set), with the remaining `k − 1` inputs of each window absorbing the `(k − 1)`-dimensional slices induced by the protected input's values? **Target:** `|P| ≥ N/poly(k, D*)` and a polynomial loss, **if slice cost at a good hint is controlled by a count over hints.**

**Ceiling as for W28-W32-A.**

## §1. Warnings carried in from W32-A, stated as hypotheses from the start

1. **Cascade → induced slices (H_casc_k).** Pinning an input of an arity-`k` window turns the window into an arity-`(k − 1)` window with a fixed slice. Near-full induced slices exhaust partners.
2. **Multiplicity → slice counts.** Coarse structure counts slices per value, not windows.
3. **Window mass → slice cost (H_mass_k), and it is WORSE at arity `k`.** Summed over hints, a window's mass is `(2N)^k`, so the **average mass per `(y, w)` is `(2N)^{k−1}/2`**, while a payer's capacity is one input's domain, `2N`. **Mass is the wrong unit.** The payer cost must be the **projection** of the protected input's coarse slices onto the payer's coordinate, which is at most `2N` per payer coordinate but has no count over hints forcing it below capacity. **W32-A §10's failure (average `N` against capacity `1.5N`) predicts that at arity `k` the projection cost is at capacity in general, and that only overlap structure (as in the star template) makes it payable.**

## §2. Counting done before the prior

**(a) Strong independence costs `k·D*`.** Each protected input excludes the other `≤ k − 1` inputs of each of its `≤ D*` windows. A greedy strong independent set has size `≥ N/(1 + (k − 1)D*)`: polynomial, fine.

**(b) The payer's burden is split across `k − 1` coordinates.** A window with one protected input `u` can distribute the payment of `u`'s coarse slices across its other `k − 1` inputs: a slice is killed by excluding **any one** coordinate's value set that covers it. **That is a hypergraph vertex cover in `k − 1` dimensions, and it may be much cheaper than any single coordinate's projection**, which is the one place arity could help. Whether a count bounds the cheapest cover is the round's crux.

**(c) The line's record on recombinations:** mechanisms stated as counts over already-measured objects survived (multiplicative recombination, protected set). Rules and gloss-level claims did not. **(b) is a count over a new object (slice covers)**, not yet measured.

## §3. Priors

| code | reviewer | **mine** |
|---|---|---|
| **32B-a** arity-`k` theorem with polynomial loss under stated slice hypotheses | 25 | **12** |
| **32B-b** framing answered; the slice-cover cost is located as the gap, with a kill template | 50 | **55** |
| **32B-c** nothing | 25 | **33** |

**Why 32B-a low:** W32-A needed two hypotheses at arity 2, and §1.3 says the mass problem worsens with arity. **Why 32B-b highest:** the framing question has a definite answer (strong independence plus split payment), and a kill template (spread projections at every hint, no overlap) is easy to state.

## §4. Flags and kill tests

- **A32B -- framing first:** confirm strong independence is necessary (a window with two protected inputs has no payer for their joint slice), and state the split-payment cover.
- **B32B -- kill template:** arity-3 windows whose coarse slices have **spread** projections on every coordinate at every hint. Compute the cheapest cover exactly at N = 8.
- **C32B -- positive control:** an arity-3 star (coincident slices), where the protected set should give `N/poly`.
- **D32B -- stop-rule:** a count bounding the cheapest slice cover goes to the reviewer before writing.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
