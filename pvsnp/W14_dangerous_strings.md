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

---

# Findings (written after the attack; priors above are unrevised)

*Model: Korten Definition 9 / Wilson Theorem 12, deterministic back-mappings. Computations in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **14a** proved | 45 / 40 | **not proved** |
| **14b** a rigidly-excluding template | 10 / 10 | **ruled out on every template tested, exactly** |
| **14c** neither; obstruction named | 45 / **50** | **this is the outcome** |

**Per the agreed stopping rule, this closes the black-box sub-line W7–W14.** §5 states the recommendation plainly.

## 1. Both repairs from §2 stand and are carried

**(b) The k-factor.** The ruling's Fact (3) — U_free drawn among inputs carrying ≤ 1 rigid x, "at least half of all inputs" — is **false for k ≥ 2**: rigid (x,u) pairs number up to kN, so #{u : ≥ 2 rigid x} ≤ kN/2 ≥ N/2. **Repaired:** at least 3N/4 of inputs carry ≤ 4k rigid x's, and W12.1's averaging must absorb 4k rigid contributions per input. **The constants degrade by a factor of k, carried here rather than hidden (Flag C14).**

**(c) The sparsity requirement.** Disjoint forced neighbourhoods costs poly(n) overlapping pairs only when **δ ≥ 1/2**; with neighbourhoods of size ≤ 2k² and |U_free| = N^{1−δ} the expectation is ≈ 4k⁴N^{1−2δ}. **Harmless for the target** (qw ≤ √N, and √N ≫ poly(n)) **but it belongs in the statement (Flag D14).**

## 2. 14b is ruled out — exactly, and with a validated harness

A template is a total reduction iff every valid hint excludes some string: E(y) = {v : no admissible C has v ∈ range(C)}, where admissible means no x produces y. Membership is a small CSP — pin C(u) = v, ask whether the rest completes — so this is **decided by backtracking, not sampled**.

**Positive control first, because the first sweep came back suspiciously uniform.** For C′(x) = (C(x), 0), hint (z,0) is admissible exactly when z ∉ range(C), so z must appear in E((z,0)):

| control | valid hints | E empty | E **nonempty** |
|---|---|---|---|
| C′(x) = (C(x), 0), n = 3 | 32 | 16 | **16**, with E = {z} for hint (z,0) |
| C′(x) = (C(x), 0), n = 4 | 64 | 32 | **32**, same shape |

**The harness discriminates.** So the sweep below is a real property of the templates, not a bug:

| template | valid hints | E empty | E nonempty |
|---|---|---|---|
| successor (C(x), C(x+1)₁) | 32 | **32** | 0 |
| hub (C(x), C(0)₁) | 32 | **32** | 0 |
| double projection, q₁ q₂ bijections (2 seeds) | 32 each | **32** each | 0 |
| random arbitrary glue (3 seeds) | 32 each | **32** each | 0 |

**No template tested rigidly excludes a string on every valid hint.** Note that even the control is *not* a total reduction: it certifies on half its hints and the adversary simply takes the other half — which is the mechanism in miniature.

## 3. Why 14a did not close, and what the evidence does and does not say

**The hosting idea has the slack it appeared to have.** ≤ k ≈ poly(n) dangerous strings against ≈ N = 2ⁿ candidate forced hosts, each hosting costing ≤ 2k constraints, and §2 shows rigid exclusion — the only thing that could block hosting outright — never occurred in any template tested. **I nonetheless could not prove the CSP satisfiable in general**, and I am not presenting the absence of a blocker as a proof that none exists.

**The query-budget evidence is inconclusive, stated plainly.** With a value-query back-mapping (weaker than DNF, so these do not transfer upward anyway):

| n | N | result | reading |
|---|---|---|---|
| 2 | 4 | worst-case q = 4 for succ, hub **and** const0 | **degenerate** — 4 = N is the trivial maximum, and the max over hints is dominated by non-certifying hints even for a template that certifies on half of them |
| 3 | 8 | sampled instance fails at q = 2, so true q ≥ 3 | a sound lower bound, but **two points, one degenerate, establish no trend** |

**I am not claiming a scaling law from this.** That is the W6 error — reading a pattern into two data points, one degenerate — and a larger sample pushing the bound to 4 would still not establish Ω(N). *(Discrimination check: const0 shows exactly 16 hints won at q = 0, matching its 16 certifying hints; succ, hub and rand show none. The harness works.)*

## 4. The named obstruction (the 14c deliverable)

**The argument now requires four choices that interact, and no single averaging handles them:**

1. the **hint** y, which must be valid and non-certifying;
2. the **free set** U_free, sparse with δ ≥ 1/2 (§1c) and drawn among inputs carrying ≤ 4k rigid x's (§1b);
3. the **forced values**, chosen *after* y — the freedom W13 identified as the one no round had exploited;
4. the **hosts** for the ≤ k dangerous strings, each imposing ≤ 2k constraints back on (3).

**Choice (3) is constrained by both (2) and (4), and (4)'s constraints are on the same variables (3) sets.** W13 proved that averaging over hints alone cannot deliver (1); nothing in W14 supplies a selection that delivers (1)–(4) jointly. **That coupling is the obstruction, and it is not a template family — it is the absence of a selection principle.**

## 5. Recommendation: close the sub-line

**Per the stopping rule agreed in advance, and independently my own judgement:** W7–W14 should close. Its theorems are **Lemma W8.1** (single-call, qw ≥ N − 1), **Theorem W10.3** (projection glue, qw ≥ N/8 − o(N)), **Lemma W12.1** (single-block arbitrary glue, qw ≥ N/3) and **Theorem W12.2** (one-input patterns, qw ≥ N/9). Depth-1 in full generality is reduced to the dangerous-string residue and left open.

**The marginal return has been falling visibly:** W8–W12 each closed a family; W13 showed the method cannot reach the general case; W14 removed the only concrete way it could have failed (rigid exclusion) without supplying the missing selection. **Another round of the same shape would most likely produce another 14c.**

## 6. Kill tests

- **(i)** Definition 9 model for all claims; the value-query budget results are labelled as **not transferable upward** and are not used as evidence for any bound.
- **(ii)** Determinism throughout (Flag H7).
- **(iii)** All four named templates tested — successor, hub, double projection with bijective q₁/q₂, random arbitrary glue — with the dangerous set computed **exactly**.
- **(iv)** The k-factor (§1b) and δ ≥ 1/2 (§1c) both carried into the statements.
- **(v)** Nothing here appears to finish by averaging alone, which W13 proved impossible.
- **(vi)** Exact vs sampled labelled, with the soundness direction named in each case; the positive control is reported before the sweep it validates.
- **(vii)** The obstruction is named (§4), and **the recommendation to close is stated rather than a W15 proposed** (§5).
- **Prior:** 14c was tied for my highest at 45; the reviewer's 50 was marginally better calibrated.

## Ceiling

**W14 proves nothing.** It rules out one shape of counterexample, repairs two steps of the surrounding argument, and reports that the selection principle the line needs does not exist yet. By Flag H7 none of the sub-line survives randomisation, and **Korten's Problem 1 is untouched.**
