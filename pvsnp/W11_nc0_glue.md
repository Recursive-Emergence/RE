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
