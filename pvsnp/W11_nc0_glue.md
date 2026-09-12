# W11: verifying W10.3, and NC⁰ glue. Pre-registration

*Drafted 2026-09-12 on branch `w11-nc0-glue`, on the reviewer's W11 specification, after its W10 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the write-up. §2 discloses everything I had already derived, so the priors are honest rather than merely early.**

## Ceiling (first)

Unchanged since W7. **Nothing here touches P vs NP or Avoid ∉ FP^NP.** By Flag H7 every statement is about **deterministic** back-mappings. Even the strongest outcome — projection glue closed and one NC⁰ subclass proved — says only that a restricted family of depth-1 black-box constructions cannot increase stretch by one bit below a query-width threshold. **Korten's Problem 1, with arbitrary polynomial-time glue, stays open.**

## §1. Refuted premises checked

Not reused: "the n term is the stubborn summand" (W6); value-query results do not transfer (W7); "pick a hint with a local certificate" (W8); "non-injective q_i is the obstruction" (W9, mine, backwards); "the forced set is small", unquantified (W9, mine); "each singleton clause forbids one value" (the reviewer's, false when |B_x| = 1); "threshold α < 1/3" (W10, mine — slack; the truth is β < 1).

**Standing practice lines:** Definition 9's DNF model only; quantify every "small"/"large"; count removability, not only origin; never reconstruct a dropped superscript inside a quotation; **register the sketch in advance so the write-up can refute it**.

## §2. Disclosure: what I verified before writing these priors

**(a) I checked Theorem W10.3's argument in full and it holds.** The maximisation is the step worth recording: subject to Σ_b s_b = n+2 with at least two blocks, Σ_b 2^{s_b} is maximised by convexity at sizes (n+1, 1), giving Σ_b 2^{−(n+2−s_b)} = 2^{−(n+2)}(2^{n+1} + 2) = **1/2 + 2^{−(n+1)}** — so the reviewer's constant is correct **and tight**. The combined expectation E[|A| + N·1[Z = ∅]] ≤ (1/2 + 2^{−n})N < N forces the chosen y to satisfy Z ≠ ∅, since otherwise the left side is already N. I also checked the two attacks the ruling names: multi-block x need no separate vacuity handling (case (b) bounds membership in A without using vacuity, and vacuity only helps), and β counts **distinct** forced inputs so β ≤ α. **My W10 measurements corroborate the bottleneck:** the "concentrated" family is exactly the extremal partition (n+1, 1), and it measured 0.75–0.88N free against the N/8 guarantee.

**(b) A correction to the ruling's NC⁰ worry, registered now.** The ruling says coordinates with constant g_i(x, ·) "never mismatch under forcing and must be handled by vacuity … or by choosing a different forced value". **I believe that is backwards.** A constant coordinate takes a fixed value independent of the oracle, so over a random hint it mismatches y_i with probability 1/2, and **when it does, K_x is satisfied unconditionally — no forcing, no membership in H required.** Constant coordinates are therefore *free wins*, strictly better than forced ones. To be confirmed or withdrawn in the run.

**(c) The one-input NC⁰ sketch, and its cost.** With C′(x)_i = g_i(x, bits of C(q_i(x))) reading O(1) bits of one input, put a_i(x) := g_i evaluated at the forced value v, and **Z(x) := {i : a_i(x) ≠ y_i}**. Lemma W10.1 generalises: K_x is satisfied by F₀ iff some i ∈ Z(x) has q_i(x) ∈ H (or some constant coordinate mismatches, by (b)). **Over a uniformly random hint, i ∈ Z(x) with probability 1/2 independently across i, so Z(x) is a uniformly random subset — exactly the distribution W10.3 uses.** The one structural change: "Z = ∅" was a single global event (y = 1^{n+2}); now **Z(x) = ∅ is a per-x event** of probability 2^{−(n+2)}, so E[#{x : Z(x) = ∅}] = N·2^{−(n+2)} = 1/4. Folding that into the expectation gives β ≤ 3/4 + o(1) and hence **qw ≥ N/16 − o(N)**, a worse constant than W10.3's N/8 but the same shape.

**(d) What I have NOT done:** the multi-input case beyond checking the reviewer's worked example (which I verified: forcing bit 1 to ¬z₁ on the half-cube {u : u₁ = 0} satisfies every clause, since an x with x₁ = 1 has its partner forced and the XOR becomes z₁ ⊕ ¬z₁ = 1 ≠ 0, while an x with x₁ = 0 is itself forced so C(x) ≠ z). **Whether that device generalises is untouched, and it is where 11a is won or lost.**

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **11a** W10.3 verified **and** the one-input NC⁰ subclass proved | 45 | **60** |
| **11b** a counterexample NC⁰ template that is a total reduction | 10 | **5** |
| **11c** W10.3 verified, NC⁰ residual named | 45 | **35** |

**Why I am well above the reviewer on 11a:** §2(a) is checked and §2(c) is sketched with its constant, and the two halves of 11a are exactly those. **Why not higher:** §2(c) is a sketch, not a write-up; the per-x Z(x) = ∅ event has to be folded in without breaking the "some y works" selection, and that is precisely the kind of step where I have been wrong before.

**Why I am below the reviewer on 11b:** the multi-input example the ruling supplies is *not* a reduction — the adversary wins it with a half-cube — so the one concrete multi-input template on the table falls to the device. A counterexample would have to defeat **every** hint and every forcing pattern.

## §4. Flags

- **Flag T11 — constant-glue coordinates are free wins, not obstacles** (§2(b)). To be confirmed; if I am wrong, the one-input case needs the different-forced-value repair the ruling suggests.
- **Flag U11 — the per-x emptiness event is the only structural change in the one-input case**, and it costs a constant (N/8 → N/16). If it costs more than a constant, say so rather than hiding it in o(1).
- **Flag V11 — the multi-input device is "force on a half, let the relation work at free inputs".** Its generalisation needs the coupling structure to admit a **transversal** — a forced set meeting every coupled pair — with values chosen so that every cross-input relation at a free input is satisfied when the free input takes the dangerous value. **I expect it to fail when the coupling graph has odd cycles, or when two multi-input coordinates demand incompatible forced values at a shared input.** That is the predicted residual.

## §5. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only; no value queries.
- **(ii)** Determinism in every statement (Flag H7).
- **(iii)** Any 11b candidate checked for **totality over all hints** by hand at the smallest n.
- **(iv)** Every constant tracked explicitly — N/8, N/16 — not absorbed into Ω(N).
- **(v)** Consistency: every bound at most Wilson's qw ≥ N; β = 1 must still yield nothing.
- **(vi)** Exact vs sampled labelled; greedy noted as an upper bound where used.
- **(vii)** If the one-input case does not close, name the step; do not present §2(c) as if it were a proof.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*

---

# Findings (written after the attack; priors above are unrevised)

*Model: Korten Definition 9 / Wilson Theorem 12, DNF queries, **deterministic** back-mappings. Computations in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors — my 11a prior was wrong, and here is why

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **11a** W10.3 verified **and** one-input NC⁰ proved | **60** / 45 | **half achieved: W10.3 verified (§1); the NC⁰ half does NOT close** |
| **11b** an NC⁰ counterexample that is a total reduction | 5 / 10 | none found; §4's exhaustive search looked for one |
| **11c** W10.3 verified, NC⁰ residual named | 35 / **45** | **this is the outcome** |

**My miss, and it is a clean one.** I priced 11a at 60 on the strength of §2(c): "Z(x) is again a uniformly random subset, so W10.3's distribution is unchanged." **That is true and irrelevant to the hard case.** W10.3's case (a) does not rest on the distribution of Z — it rests on **pigeonhole**: for a projection template, a single-block x has n+2 coordinates reading the n+1 bits of one input, so two coordinates read the *same oracle bit*, and a random hint separates them with probability 1/2. **For general NC⁰ glue there is no pigeonhole** — two coordinates collide only if they compute the *same function* of the bits they read, and there are far more functions than bits. So n+2 coordinates can be pairwise distinct and non-constant, P[x ∈ A] rises from ≤ 1/2 to ≈ 1, and the argument gives nothing. **I checked the distribution and failed to check the combinatorial step that the distribution feeds.** The reviewer's prior (45/45) was better calibrated than mine.

## 1. Theorem W10.3, verified and stated

**Theorem W10.3.** *Every projection template (any q_i, b_i) admits a hint y with Z ≠ ∅ and β ≤ 1/2 + 2^{−n}. Hence every correct deterministic back-mapping has* **qw ≥ N/8 − o(N)**.

*Proof.* Draw y uniformly from {0,1}^{n+2}; let π_x partition the coordinates by the input they call.
**(a) π_x a single block.** All n+2 coordinates read bits of one (n+1)-bit value, so by pigeonhole some i ≠ j read the **same** oracle bit; that pair is bichromatic with probability 1/2, making K_x vacuous. Only non-vacuous x can lie in A, so P[x ∈ A] ≤ 1/2.
**(b) π_x with ≥ 2 blocks.** x ∈ A requires |S_x^Z| = 1, i.e. Z inside a single block, and P[Z ⊆ block of size s] = 2^{−(n+2−s)}. Hence P[x ∈ A] ≤ Σ_b 2^{−(n+2−s_b)} = 2^{−(n+2)} Σ_b 2^{s_b}. **Subject to Σ_b s_b = n+2 with at least two blocks, Σ_b 2^{s_b} is maximised by convexity at sizes (n+1, 1)**, giving 2^{−(n+2)}(2^{n+1} + 2) = **1/2 + 2^{−(n+1)}** — so the constant is correct and **tight**.
Therefore E[|A|] ≤ (1/2 + 2^{−(n+1)})N, and P[Z = ∅] = 2^{−(n+2)}. So
  E[ |A| + N·1[Z = ∅] ] ≤ (1/2 + 2^{−(n+1)} + 2^{−(n+2)})N < N,
and some y attains the mean. **That y must have Z ≠ ∅**, since otherwise the left side is already N. For it, β ≤ α ≤ 1/2 + 2^{−n}. Apply Theorem W10.2 with δ = 1 − β ≥ 1/2 − 2^{−n}. ∎

**Both attacks the ruling names check out.** Multi-block x need no separate vacuity treatment — case (b) bounds membership in A without invoking it, and vacuity only helps. And β counts **distinct** forced inputs, so β ≤ α throughout.

**Corroboration from W10's measurements.** The family I called "concentrated" — n+1 calls at one input, one elsewhere — **is exactly the extremal partition (n+1, 1)**, so it is where the bound is tight; it measured 0.75–0.88N free against the N/8 guarantee, i.e. the theorem is conservative by roughly a factor of six on the worst family it admits.

**So projection glue is closed:** no depth-1 black-box reduction with projection glue increases stretch by one bit deterministically with query-width below N/8 − o(N).

## 2. Flag T11 confirmed — constant-glue coordinates are free wins

**Lemma W11.1.** *If g_i(x, ·) is constant, its coordinate takes a fixed value independent of the oracle. Over a uniformly random hint it differs from y_i with probability 1/2, and when it does, **K_x holds for every oracle** — no forcing, no membership in H.*

So constant coordinates are **strictly better** than forced ones, and the ruling's suggestion that they "must be handled by vacuity … or by choosing a different forced value" inverts their role. *(They do contribute nothing when they happen to agree with y_i, which is the only sense in which they are inert.)*

## 3. Why the one-input NC⁰ case does not close

Write C′(x)_i = g_i(x, bits of C(q_i(x))), each g_i reading O(1) bits of a **single** input. Lemma W10.1 generalises cleanly: with a_i(x) := g_i evaluated at the forced value and **Z(x) := {i : a_i(x) ≠ y_i}**, F₀ satisfies K_x iff some i ∈ Z(x) has q_i(x) ∈ H, or some constant coordinate mismatches (§2). And Z(x) is uniformly random, as I claimed at pre-registration.

**The break is elsewhere.** For a **single-block** x — all coordinates reading the same input u_x — the projection proof used pigeonhole to force a collision. Under NC⁰ glue the n+2 coordinates may compute n+2 **pairwise distinct non-constant functions**, so no two ever collide, no hint makes K_x vacuous, and x ∈ A whenever Z(x) ≠ ∅ — probability 1 − 2^{−(n+2)}. If x ↦ u_x is injective across such x, **H must contain every input and U_free is empty.**

**What such a template actually is.** A single-block x with all-non-constant glue means C′(x) = G_x(C(x)) for a map G_x : {0,1}^{n+1} → {0,1}^{n+2}. Then y ∉ range(C′) iff C(x) ∉ G_x^{−1}(y) for every x — **an input-dependent forbidden set**, which is the shape of **Corollary W8.2's masked template**, not of W10's hitting-set analysis. Two sub-cases, both real:
- **If y ∉ image(G_x) for every x**, the hint is vacuous and Wilson applies unaided (qw ≥ N). Such a y exists when the G_x are all equal, since |image(G)| ≤ 2^{n+1} < 2^{n+2}.
- **If the G_x vary with x**, their images can cover {0,1}^{n+2} jointly, and then every hint is constraining. The adversary must pick c(u) outside ∪_{x : u_x = u} G_x^{−1}(y), which exists **iff** that union is not everything — and a union that *is* everything means y ∈ range(C′) for every oracle, i.e. **that y was never a valid hint**. So validity and smallness of β become a **joint** condition on the hint.

**That joint condition is the open step.** I can bound the pieces in expectation — E[|G_x^{−1}(y)|] = 1/2 over a random hint, so E[Σ_{x : u_x = u} |G_x^{−1}(y)|] = m_u/2 ≤ N/2 < 2^{n+1} — but I could not turn that into a single hint that is simultaneously valid and has β bounded away from 1. **I am not presenting the expectation as if it were the selection argument.**

## 4. Multi-input glue: the device generalises further than I predicted

**Flag V11 predicted failure from odd cycles. That was wrong.** For a single coupled coordinate C(x)₁ ⊕ C(σ(x))₁ with hint bit c:
- **c = 0** reduces the requirement to "every x ∉ S has σ(x) ∈ S" — a domination condition costing ⌈L/2⌉ per cycle of σ, so **odd cycles cost one extra element, not failure**; |S| ≤ 2N/3 and U_free ≥ N/3.
- **c = 1** breaks for permutations (the two roles force |S_A| + |S_B| ≥ N), but that is exactly when σ has fixed points, and a fixed point makes the coordinate **constant 0**, which by §2 is a free win at c = 1.

**So the real tension is fixed points versus non-fixed points, resolved by the hint bit**, and taking the better of c = 0 and c = 1 leaves U_free large in every mixed case.

**Two coupled coordinates, searched exhaustively.** With full-value forcing, "K_x is guaranteed" is exactly **infeasibility of a GF(2) system** — projections give one-variable equations, XORs two-variable ones — so it is decided by elimination, not estimated. At n = 3 I searched **all 256 subsets S, all 16 forced values, and all 32 hints**:

| seed | best U_free | witness |
|---|---|---|
| 1 | **6 of 8 (0.75)** | \|S\| = 2, v = 0 |
| 2 | **5 of 8 (0.62)** | \|S\| = 3, v = 0 |
| 3 | **5 of 8 (0.62)** | \|S\| = 3, v = 0 |
| 4 | **5 of 8 (0.62)** | \|S\| = 3, v = 0 |

**Exhaustive in the configuration space, sampled over templates** (four seeds, two XOR coordinates, n = 3 only). Every template left a constant fraction free with a tiny forced set, and every witness used the constant value v = 0. **No 11b candidate appeared.** The reviewer's worked example is confirmed by hand: forcing bit 1 to ¬z₁ on {u : u₁ = 0} leaves U_free = N/2, since an x with x₁ = 1 has its partner forced and the XOR becomes z₁ ⊕ ¬z₁ = 1 ≠ 0, while an x with x₁ = 0 is itself forced.

## 5. The residual, named

> **Single-block NC⁰ templates with pairwise-distinct non-constant glue** — C′(x) = G_x(C(x)) with the G_x varying across x so that their images jointly cover {0,1}^{n+2}. Here pigeonhole is unavailable, every hint is constraining, and what is needed is a hint that is **simultaneously valid and has β bounded away from 1**.

**This is a different obstruction from every previous round's.** W9's residual was two hints wanted for two case families; W10's was one quantity to bound. This one is a **joint feasibility** condition, and it is the first residual in the W-line that the forced-bit device does not even address — the right comparison is Corollary W8.2's masked analysis, which handles it only when the forbidden values are spread.

## 6. Kill tests

- **(i)** Definition 9 / Theorem 12 model throughout; no value queries.
- **(ii)** Determinism in every statement (Flag H7).
- **(iii)** No 11b candidate arose; §4 searched exhaustively over configurations for four templates.
- **(iv)** Constants tracked explicitly: N/8 − o(N) in §1, N/3 and N/2 in §4. **§3's N/16 from my pre-registration is withdrawn — it was computed for a case the argument does not cover.**
- **(v)** Consistency: N/8 ≤ N; β = 1 still yields nothing; §1 reduces to Wilson when nothing is forced.
- **(vi)** Exact vs sampled labelled in §4; the GF(2) decision is exact, the template choice is sampled.
- **(vii)** §3 names the step that fails and does not present the expectation bound as a selection argument.
- **Prior wrong said with the finding:** §0.

## Ceiling

Unchanged. **W11 proves nothing about P vs NP.** It closes projection glue at qw ≥ N/8 − o(N), confirms that constant-glue coordinates are free, shows the multi-input device survives two coupled coordinates under exhaustive search, and identifies precisely where NC⁰ glue defeats the method: **pigeonhole, not probability, was doing the work in W10.3**. By Flag H7 none of this survives randomisation, and Korten's Problem 1 remains open.
