# W12: single-block templates with arbitrary glue, and one-input patterns. Pre-registration

*Drafted 2026-09-12 on branch `w12-one-input-glue`, on the reviewer's W12 specification, after its W11 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the write-up. §2 discloses everything already derived, including a defect found in the reviewer's Lemma W12.1.**

## Ceiling (first)

Unchanged since W7. **Nothing here touches P vs NP or Avoid ∉ FP^NP**, and by Flag H7 every statement is about **deterministic** back-mappings. The strongest outcome would say: no depth-1 black-box reduction whose glue reads **one input per coordinate** increases stretch by one bit deterministically below a query-width threshold. **Korten's Problem 1 — arbitrary glue, any number of inputs per coordinate — stays open**, and item 3 is explicitly a map.

## §1. Refuted premises checked

Not reused: value-query results do not transfer (W7); "pick a hint with a local certificate" (W8); "non-injective q_i is the obstruction" (W9, mine, backwards); "each singleton clause forbids one value" (the reviewer's); "threshold α < 1/3" (W10, mine, slack); **"Z(x) uniform means W10.3 transfers" (W11, mine — the distribution was never the point; pigeonhole was)**; **"odd cycles break the coupled-coordinate device" (W11, mine — they cost one extra element)**.

**Standing practice lines:** Definition 9's DNF model only; quantify every "small"/"large"; **check the combinatorial step, not only the distribution feeding it** (the W11 lesson); report slack rather than adjusting a definition; register the sketch in advance.

## §2. Disclosure: what I derived before writing these priors

**(a) Lemma W12.1's structure is right and I verified the counting.** With C′(x) = G_x(C(u_x)), the constraint "y ∉ range(C′)" is **a product**: C(u) ∈ A_u for every u, where A_u is the complement of Φ_u(y) = ∪_{x : u_x = u} G_x^{−1}(y). Wilson's adversary runs inside a product with no bookkeeping. For placement, #{u : v ∈ Φ_u(y)} ≤ #{x : G_x(v) = y} since distinct u contribute distinct x. And Σ_y Σ_v #{x : G_x(v) = y} = N·2^{n+1}, because each pair (x, v) contributes to exactly one y.

**(b) Its validity step is WRONG as stated, and I have a repair.** The ruling says a hint "is invalid only if some G_x is constant ≡ y, which excludes ≤ N hints". **False:** Φ_u(y) can cover all of {0,1}^{n+1} with no G_x constant — two x's at the same u can have preimages covering complementary halves. **Repair:** u is blocked iff Σ_{x : u_x = u} |G_x^{−1}(y)| ≥ 2^{n+1}; averaging over y, E_y|G_x^{−1}(y)| = 2^{n+1}/2^{n+2} = 1/2, so E_y[Σ] = m_u/2 and by Markov P_y[u blocked] ≤ m_u/2^{n+2}. **Since Σ_u m_u = N**, we get **E_y[#blocked u] ≤ N/2^{n+2} = 1/4**, so at least 3/4 of all hints are valid — that is 3·2^n hints, numerically the same count the ruling used. **So qw ≥ N/3 survives on a different argument**; a fully self-contained variant averaging M(y) + N·1[invalid] over all hints gives the slightly weaker qw ≥ N/4.

**(c) The special cases check out, with weaker constants — as they should.** W8.1 is G_x(v) = (v, h(x)): then Φ_x(y) = {z} when h(x) = b and ∅ otherwise, so M(y) = |h^{−1}(b)| ≤ N/2 and W12.1 yields **qw ≥ N/2**, against the direct **qw ≥ N − 1** of Lemma W8.1. W8.2 is the masked version G_x(v) = (v ⊕ m(x), h(x)); W9.3 is the projection case G_x(v) = (v_{b₁(x)}, …). **A general lemma giving weaker constants than the bespoke ones is the expected relationship, and its failure to do so would be the alarm.**

**(d) What I have NOT done:** Theorem W12.2's two-regime expectation. That is where 12a is won or lost.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **12a** W12.1 **and** W12.2 proved | 50 | **50** |
| **12b** a counterexample template that is a total reduction | 5 | **5** |
| **12c** W12.1 proved, W12.2 gap named | 45 | **45** |

**Why I match the reviewer rather than sitting above it, despite having half of 12a already.** W12.1 is essentially done (§2a–b). But W11 taught me the specific lesson that applies here: I priced that round high because I had verified a *distribution* and not the combinatorial step it fed. **W12.2 is a single expectation carrying five failure terms — misses, Z(x) = ∅, G_x(1^{n+1}) = y at forced inputs, blocked free inputs, and Z = ∅ — plus the max_v term, and its claimed constant N/12 is exactly the crossover value of the two regimes.** A constant that is tight at the regime boundary has no slack to absorb an error in any one of those terms. Having half the outcome in hand does not justify pricing the fiddly half optimistically.

## §4. Flags

- **Flag W12 — the validity repair (§2b) must appear in the write-up**, or Lemma W12.1 is stated on a false premise even though its conclusion holds.
- **Flag X12 — the regime boundary is where the constant is decided.** At s = 1/4 both regimes give exactly N/12: regime one gives sN/3 = N/12, regime two gives N(1+s)/4 − 2sN/3 = 0.1458N. **So any slack lost in the failure terms shows up first at the crossover**, and that is the number to compute exactly rather than asymptotically.
- **Flag Y12 — item 3 is a map only.** I expect the V11 device to compose with the product family, because a coupled coordinate constrains pairs (u, σ(u)) with u free and σ(u) forced, which is still a condition per free input. **I expect two coupled coordinates with different σ to break the product structure**, since they impose a joint condition across two different partners of the same free input — which is no longer a product over u.

## §5. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only; no value queries.
- **(ii)** Determinism in every statement (Flag H7).
- **(iii)** Any 12b candidate checked for **totality over all hints** by hand at the smallest n.
- **(iv)** Constants computed exactly at the regime boundary (Flag X12), not absorbed into Ω(N).
- **(v)** Consistency: W8.1, W8.2, W9.3 must fall out of W12.1 with **weaker** constants; if any comes out stronger, something is wrong.
- **(vi)** Exact vs sampled labelled.
- **(vii)** **If a constant does not close, report the exact slack — do not adjust a definition to make it close.** (The reviewer's instruction, adopted verbatim.)
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*

---

# Findings (written after the attack; priors above are unrevised)

*Model: Korten Definition 9 / Wilson Theorem 12, DNF queries, **deterministic** back-mappings. Computations in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **12a** W12.1 **and** W12.2 proved | **50** / 50 | **achieved — and W12.2's constant improves from N/12 to N/9** |
| **12b** a counterexample that is a total reduction | 5 / 5 | none |
| **12c** W12.1 proved, W12.2 gap named | 45 / 45 | — |

**Two corrections to the reviewer, one to me.** Its Lemma W12.1 rests on a false validity step (§1, repaired). Its Theorem W12.2 constant is **not tight** — placing the regime boundary at the true crossing gives **N/9**, not N/12 (§3). And **my Flag Y12 prediction was wrong**: two coupled coordinates with different σ do *not* break the product structure (§4).

## 1. Lemma W12.1 — single-block templates, arbitrary glue

**Setting.** C′(x) = G_x(C(u_x)) with G_x : {0,1}^{n+1} → {0,1}^{n+2} and x ↦ u_x both arbitrary. For a hint y put **Φ_u(y) = ∪_{x : u_x = u} G_x^{−1}(y)** and **A_u = {0,1}^{n+1} \ Φ_u(y)**.

**The constraint is a product.** y ∉ range(C′) ⟺ G_x(C(u_x)) ≠ y for all x ⟺ **C(u) ∈ A_u for every u**. So the admissible family is **F = ∏_u A_u**, and Wilson's adversary runs inside it with no bookkeeping: a term is usable iff its bits are completable inside each touched A_u — a per-input test, because the family is a product — and "false" is sound for the same reason.

**Validity — the reviewer's step is false, and here is the repair (Flag W12).** The ruling asserts a hint is invalid "only if some G_x is constant ≡ y, which excludes ≤ N hints." **That is wrong:** Φ_u(y) can exhaust {0,1}^{n+1} with no G_x constant — two x's at the same u can have preimages covering complementary halves. **Repair.** u is blocked iff Σ_{x : u_x = u} |G_x^{−1}(y)| ≥ 2^{n+1}. Since Σ_y |G_x^{−1}(y)| = 2^{n+1} over the 2^{n+2} hints, E_y|G_x^{−1}(y)| = 1/2, so E_y[Σ_{x : u_x = u}] = m_u/2 and Markov gives P_y[u blocked] ≤ m_u/2^{n+2}. **Because Σ_u m_u = N**,
  **E_y[#blocked u] ≤ N/2^{n+2} = 1/4**, hence P_y[∃ blocked u] ≤ 1/4 and **at least 3·2^n hints are valid** — numerically the count the ruling used, on a correct argument.

**Placement counting.** Let M(y) = max_v #{u : v ∈ Φ_u(y)}. Distinct such u contribute distinct x, so M(y) ≤ max_v #{x : G_x(v) = y}. Each pair (x, v) contributes to exactly one hint, so Σ_y Σ_v #{x : G_x(v) = y} = N·2^{n+1}, and therefore Σ_y max_v ≤ N·2^{n+1}. Averaging over the ≥ 3·2^n valid hints gives a valid y with **M(y) ≤ 2N/3**, i.e. **every v is allowed at ≥ N/3 inputs**.

**Lemma W12.1.** *For every single-block template with arbitrary glue, any correct deterministic back-mapping has* **qw ≥ N/3**.
*Proof.* Fix the y above; F = ∏_u A_u is non-empty. Run Wilson's adversary inside F. After q queries |dom ρ| ≤ qw < N/3, so some input allowing Q's output v is free; set C(u) = v and complete inside F. Then y ∉ range(C′) still, every answer remains true, and v ∈ range(C). ∎

## 2. The special cases fall out, all weaker — kill test (v)

- **W8.1** is G_x(v) = (v, h(x)). For y = (z,b), G_x^{−1}(y) = {z} when h(x) = b and ∅ otherwise, so M(y) = |h^{−1}(b)| ≤ N/2 at the better b, and W12.1 gives **qw ≥ N/2** against the bespoke **N − 1**.
- **W8.2** is the masked G_x(v) = (v ⊕ m(x), h(x)); M(y) is the largest fibre of m inside h^{−1}(b) — exactly the "bad set" of Corollary W8.2.
- **W9.3** is the projection case G_x(v) = (v_{b₁(x)}, …); Φ_x(y) is a subcube, empty precisely when the clause is vacuous.

**All three come out weaker than their bespoke bounds, which is the expected relationship** — a general lemma beating a special-case one would have been the alarm.

## 3. Theorem W12.2 — and its constant is N/9, not N/12

**Setting.** C′(x)_i = g_i(x, C(q_i(x))), each coordinate reading **one** input, glue arbitrary. Fix the forced value c ≡ 1^{n+1} **before** drawing y; let s be the fraction of single-block x. For multi-block x, Z(x) = {i : g_i(x, 1^{n+1}) ≠ y_i} is a uniformly random subset, and x is satisfied throughout F iff S_x^{Z(x)} ∩ H ≠ ∅. Single-block x at a forced input needs G_x(1^{n+1}) ≠ y; at a free input it is carried by A_u as in §1.

**The two regimes, with placeable(v) computed exactly.**
- **Repair regime:** H takes one input per multi-block x from S_x^{Z(x)}, so |H| ≤ (1−s)N, U_free ≥ sN, and subtracting §1's 2/3 bound applied to the sN single-block x gives **placeable ≥ sN/3**.
- **Random-half regime:** H is a random half plus repairs (W10.2's sum trick), U_free ≥ N(1+s)/4, so **placeable ≥ N(1+s)/4 − 2sN/3 = N(3 − 5s)/12**.

**The reviewer splits the regimes at s = 1/4, and that is not where they cross.** Setting sN/3 = N(3−5s)/12 gives 4s = 3 − 5s, so **s = 1/3**, where both equal **N/9**. Taking the better regime pointwise, the binding value is the minimum of the upper envelope, attained at the crossing:

  **min_s max( s/3 , (3−5s)/12 ) = 1/9 at s = 1/3.**

**Theorem W12.2 (sharpened).** *For one-input patterns with arbitrary per-coordinate glue, any correct deterministic back-mapping has* **qw ≥ N/9 − O(1)**.

**The failure terms are O(1) and never bind.** Carrying all five explicitly — misses, Z(x) = ∅ and G_x(1^{n+1}) = y at 2^{−(n+2)} each, blocked free inputs at ≤ 1/4 by §1, and Z = ∅ — their total is **< 1 input** across the whole sweep (0.50 to 0.94 for n = 8…20). So the constant is decided entirely by the two main terms.

**Computed check of the reviewer's split** (arithmetic on the claimed bounds, n = 8…20): with the boundary pinned at s = 1/4, net/N dips to **0.08332–0.08333 at the crossover** and rises on both sides (0.1500 at s = 0.24, 0.0867 at s = 0.26, 0.2500 at s = 0 and s = 0.75). **N/12 = 0.08333** — so the ruling's constant is exactly what its own regime split yields, and the dip is an artefact of splitting at 1/4 rather than at 1/3. **Moving the boundary removes it.**

## 4. Item 3, the cross-input map — and my Flag Y12 was wrong

**Flag Y12 predicted** that one coupled coordinate composes with the product family but **two with different σ break it**, since they impose a joint condition across two different partners of the same free input.

**They do not.** With full-value forcing, "K_x guaranteed" is exactly **GF(2) infeasibility** of the match system, so this is decidable rather than sampleable. Exhaustively at n = 3 over all 256 subsets, all 16 forced values and all 32 hints:

| template | best U_free |
|---|---|
| two coupled, same σ (x⊕1, x⊕1) | **4 of 8** |
| two coupled, σ = x⊕1 and x⊕2 | **4 of 8** |
| two coupled, σ = x⊕1 and x+1 mod N | **4 of 8** |
| two coupled, σ = x⊕1 and x⊕3 | **4 of 8** |
| **control: one coupled coordinate** | **4 of 8** |

**Differing σ cost nothing, and two coordinates cost nothing over one.** This is the third prediction in the V11/Y12 family in which I expected cross-input coupling to be harder than it is. *(Exhaustive in configuration space; n = 3 with two coordinates only, so it supports composition rather than establishing it.)*

## 5. The residual

> **Coordinates reading three or more inputs**, and cross-input coupling at n > 3 — untested. Everything proved here assumes each coordinate reads **one** input (§3) or that the template is single-block (§1); §4's evidence for two-input coupling is exhaustive only at n = 3.

This is a narrower residual than W11's: that one was a *joint feasibility* condition the forced-bit device could not address, and §1 now dissolves it by making the constraint a product. What remains is a **scope** limit, not a structural obstruction.

## 6. Kill tests

- **(i)** Definition 9 / Theorem 12 model throughout; no value queries.
- **(ii)** Determinism in both theorem statements (Flag H7).
- **(iii)** No 12b candidate arose; §4 searched exhaustively over configurations.
- **(iv)** The constant is computed **at** the regime boundary, and the boundary itself is derived rather than assumed — which is what moved N/12 to N/9 (Flag X12 discharged).
- **(v)** W8.1, W8.2, W9.3 all fall out of W12.1 with **weaker** constants (§2).
- **(vi)** §3's table is arithmetic on the claimed bounds; §4 is exact GF(2) decision, sampled over templates. Both labelled.
- **(vii)** No definition was adjusted to make a constant close; the slack was reported and then removed by moving the boundary.
- **Prior wrong said with the finding:** §0 and §4.

## Ceiling

Unchanged. **W12 proves nothing about P vs NP.** It closes single-block templates with arbitrary glue at qw ≥ N/3, one-input patterns at qw ≥ N/9, and reports that cross-input coupling composes rather than breaks. By Flag H7 none of it survives randomisation, and **Korten's Problem 1 — glue reading arbitrarily many inputs — remains open.**
