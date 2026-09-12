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
