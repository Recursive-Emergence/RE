# W14: disposing of the dangerous strings. Pre-registration

*Drafted 2026-09-12 on branch `w14-dangerous-strings`, on the reviewer's W14 specification, after its W13 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the attack. §2 discloses two defects found in the reviewer's step, one of which is wrong by a factor of k.**

## Ceiling (first), and the stopping rule

Unchanged. **Nothing here settles Korten's Problem 1**, even in the black-box model: this is depth 1, one bit of stretch, deterministic back-mappings only (Flag H7 — guess-and-test sits in FZPP^{NP^C} at depth 0). **The reviewer proposes a stopping rule: if W14 lands on 14c, the black-box sub-line W7–W14 closes** with W8.1, W10.3, W12.1, W12.2 as its theorems and the target returning to the door. **I accept that as a sensible endpoint and will say so in the report either way — the sub-line has been running for eight rounds and its marginal return is now visibly falling.** That judgement is mine to offer and my user's to make.

## §1. Refuted premises checked

Not reused: "each singleton clause forbids one value" (the reviewer's); "α < 1/3" (W10, mine); "Z(x) uniform means W10.3 transfers" (W11, mine); **"odd cycles break the coupled device" (W11, mine)**; **"differing σ break the product structure" (W12, mine)**; **"uncapped forced inputs are the obstruction" (W13, mine — backwards; high multiplicity at a forced input is an adversary asset)**.

**Flag Z13 is now a line principle and stays standing: high multiplicity helps whoever gets to choose.** I have been wrong about cross-input coupling four times. **Any prediction this round that coupling is fatal must be tested before it is believed.**

## §2. Disclosure: two defects in the reviewer's step

**(a) Fact (1) is correct.** For fixed w, Σ_{v,y} 1[G_x(w,v) = y] = 2^{n+1} since each v yields exactly one y; the expectation over w preserves it. So Σ_{v,y} r_{x,u}(v,y) = 2^{n+1}, the same mass a rigid k = 1 x carries.

**(b) Fact (3) is WRONG for k ≥ 2.** The ruling says U_free may be drawn among inputs carrying **≤ 1 rigid x**, "which is at least half of all inputs since the rigid x's contribute total multiplicity ≤ N". **Each x reads k inputs, so the number of rigid (x,u) pairs is bounded by kN, not N**; hence #{u : ≥ 2 rigid x at u} ≤ kN/2, which is **≥ N/2 for every k ≥ 2** and makes the conclusion vacuous. **Repair:** by Markov, at least 3N/4 of inputs carry **≤ 4k** rigid x's. **Consequence to track:** W12.1's averaging must then absorb 4k rigid contributions per input instead of one, so the constants degrade by a factor of k — which must be carried explicitly, not hidden.

**(c) Fact (2) needs a constraint it does not state.** Disjointness of forced neighbourhoods is asserted "after removing the poly(n) many overlapping pairs". With neighbourhoods of size ≤ 2k² and |U_free| = N^{1−δ}, the expected number of overlapping pairs is ≈ 4k⁴·N^{1−2δ}, which is poly(n) only when **δ ≥ 1/2**. **This is harmless for the target** — it gives qw ≤ √N, and √N ≫ poly(n), so it still beats any real FP^NP reduction — **but the sparsity requirement belongs in the statement.**

**(d) The mass bound checks out.** Σ_{v,y} Σ_{x at u} r_{x,u} ≤ mult(u)·2^{n+1} ≤ 2k·2^{n+1}; summing over U_free and dividing by the ≈ 2^{n+2} hints gives average Σ_v Σ_u p_{u,v} ≤ k|U_free|. A dangerous v contributes ≈ |U_free|, so **at most ≈ k dangerous strings per hint** — the reduction stands, modulo (b) and (c).

**(e) What I have not done:** the hosting CSP itself.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **14a** proved — no dangerous string survives, or all are hosted | 40 | **45** |
| **14b** a string rigidly excluded at every input for every valid hint (a total reduction) | 10 | **10** |
| **14c** neither; the exact CSP obstruction | 50 | **45** |

**Why I am slightly above on 14a.** The hosting idea has enormous slack: **≤ k ≈ poly(n) dangerous strings against ≈ N = 2ⁿ candidate forced hosts**, each hosting imposing only ≤ 2k constraints on other forced values. And W13's search is direct evidence — **805 templates, none with a string excluded everywhere.** **Why not higher:** the chain now has two repaired steps (§2b, §2c), and repairs are where constants die; §2b in particular costs a factor of k in exactly the averaging that W12.1 supplies.

**Why I match on 14b.** For 14b, *every* valid hint must rigidly exclude something. Templates that exclude on *some* hint are easy — C′(x) = (C(x), 0) excludes z on hint (z,0) — but the adversary then takes the vacuous hint (z,1). W13 found no template resisting across 805 tries. So 10, not lower: "none found" over random templates is weak evidence against a *designed* one.

## §4. Flags

- **Flag C14 — the k-factor from §2b must be carried to the end.** If the final constant is stated without it, the proof is wrong. **Track it explicitly through the averaging.**
- **Flag D14 — the sparsity requirement δ ≥ 1/2 (§2c) must appear in the theorem statement**, not in a remark.
- **Flag E14 — the 14a/14b dichotomy is clean and I expect it to be the round's shape:** either every dangerous v can be hosted at some forced input, or some v is *rigidly* excluded at every input — and the latter is exactly a total reduction. **If I reach 14a, the report must state that the dichotomy, not the hosting construction, is the content.**
- **Flag Z13 (standing)** — test before believing any "coupling is fatal" claim.

## §5. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only; no value queries.
- **(ii)** Determinism in every statement; ceiling restated with any 14a.
- **(iii)** Tested on all four templates the ruling names: successor; hub; double projection C′(x) = (C(q₁(x)), C(q₂(x))₁) with q₁, q₂ bijections; and a random arbitrary-glue template at n = 3, **computing the dangerous set exactly**.
- **(iv)** Every constant with its comparison bound; the k-factor of §2b tracked (Flag C14); δ ≥ 1/2 stated (Flag D14).
- **(v)** Consistency: W12.1 must remain the k = 1 case; W13's counting limit must not be contradicted — **any argument that appears to finish by averaging alone is wrong**, since W13 proved averaging cannot.
- **(vi)** Exact vs sampled labelled, with the soundness direction named.
- **(vii)** If the CSP does not close, name the exact obstruction; and **if the outcome is 14c, say plainly that the sub-line should close** rather than proposing a W15.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*
