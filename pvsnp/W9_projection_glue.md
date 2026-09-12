# W9: the projection-glue family, and maintainability of the covering invariant. Pre-registration

*Drafted 2026-09-12 on branch `w9-projection-glue`, on the reviewer's W9 specification, after its W8 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the attack. The sketch in §4 is registered in advance so it can be broken; if it fails, the report says where.**

## Ceiling (first)

Unchanged, and it has not moved since W7. **Nothing here bears on P vs NP or on Avoid ∉ FP^NP.** By Flag H7 every statement is about **deterministic** back-mappings — guess-and-test at this stretch is in FZPP^{NP^C} at depth 0. A full 9a would say: one further template family cannot beat Lemma 6 by one bit, black-box, deterministically. **Korten's Problem 1 stays open either way.**

## §0. Refuted premises checked

Not reused: "the generator's outputs are deep" (Y9); "prefix descent must resolve a deficit of 1" (W5); "the n term is the stubborn summand" (W6); the value-query computations **do not transfer** (W7); **"pick a hint with a local certificate" (W8 — the reviewer's plan, refuted: local certificates essentially never exist, for projection glue *or* single-call; the working lever is invariant-maintainability)**.

**Standing practice lines:** never reconstruct a dropped superscript inside a quotation; count **removability**, not only origin; a lower bound in a weaker query model is not a lower bound — **stay in Korten Definition 9 / Wilson Theorem 12's DNF model**; and register the sketch in advance so the write-up can refute it.

## §1. The object

C : {0,1}ⁿ → {0,1}^{n+1}, N = 2ⁿ, oracle bits indexed by (u, j) with u ∈ {0,1}ⁿ, j ∈ [n+1]. The template is

  **C′(x) = (C(q₁(x))_{b₁(x)}, …, C(q_{n+2}(x))_{b_{n+2}(x)})**, q_i and b_i NC⁰ (I will prove for **arbitrary** q_i, b_i where I can).

This is exactly the form Miles–Viola Theorem 1.4 rules out on the PRG side. Fix a hint y ∈ {0,1}^{n+2}. The covering invariant, as a CNF over oracle bits: for each input x one clause

  **K_x  =  ⋁_{i=1}^{n+2} [ bit(q_i(x), b_i(x)) ≠ y_i ]**,   and   **Φ_y = ⋀_x K_x**,

so "y ∉ range(C′)" ⟺ the oracle assignment satisfies Φ_y. Clause width n+2; N clauses.

## §2. The counting, done before the prior

**(a) Multiplicity — the number the reviewer asked for.** A bit (u, j) occurs in K_x exactly when some i has q_i(x) = u and b_i(x) = j. **If every q_i is a bijection**, then for each i there is exactly one x with q_i(x) = u, so

  **each oracle bit occurs in at most n+2 clauses.**

Hence the LLL dependency degree is **d ≤ (n+2)·(n+2) = (n+2)²** (each of a clause's ≤ n+2 variables is shared with ≤ n+2 clauses).

**(b) Violation probability.** Under a uniform random oracle, K_x fails only if all n+2 coordinates match y, which forces the bits at the **distinct** pairs (q_i(x), b_i(x)). Writing P_x for the set of distinct pairs, **Pr[K_x fails] = 2^{−|P_x|}**, and |P_x| = n+2 when the pairs are distinct.

**(c) LLL check.** With p = 2^{−(n+2)} and d ≤ (n+2)², the condition e·p·(d+1) ≤ 1 reads e·((n+2)²+1)/2^{n+2} ≤ 1, **true for all small n upward**. So for bijective q_i the CNF is satisfiable with room to spare, and the slack is exponential.

**(d) Collisions are the adversary's friend, not its problem.** If two coordinates i ≠ j have (q_i(x), b_i(x)) = (q_j(x), b_j(x)) but y_i ≠ y_j, then K_x is **automatically true** — one bit cannot equal two different values — and that input is unconstrained. So collisions only shrink the constraint set.

**(e) Where it must break.** For **non-injective** q_i — the reviewer's q(x) = (x₁…x_{n/2}, 0…0) — a single u has 2^{n/2} preimages, so a bit of C(u) sits in **exponentially many** clauses. Then d is exponential, LLL dies, and one fixed input can destroy the surviving witness for exponentially many x at once. **This is the predicted 9c.**

## §3. Flags

- **Flag N9 (registered prediction about where the difficulty is NOT).** Maintainability is close to free, because the adversary can simply **extend along a satisfying assignment**: keep the invariant "the ρ-restricted Φ_y is satisfiable", and when a term forces some bits, complete the newly fixed inputs using the values of a satisfying assignment consistent with those forced bits. The restricted formula is then still satisfied by that same assignment. **I predict the real content is not maintainability but the FINAL PLACEMENT of y′.**
- **Flag O9 (the placement obligation, stated now).** Setting C(x*) = y′ must keep Φ_y satisfiable. With bijective q_i this touches ≤ n+2 clauses, but the adversary must find a **free** x* for which it is harmless. I expect this to cost at most a poly factor, giving **qw ≥ N/poly**, not qw ≥ N − 1 as in W8.1.
- **Flag P9 (the obstruction, predicted).** The exact quantity that decides 9a vs 9c is the **multiplicity** max_{(u,j)} #{x : (u,j) occurs in K_x}. Bijective ⇒ ≤ n+2 ⇒ LLL applies. Non-injective ⇒ up to 2^{n/2} ⇒ LLL fails and so does the "one true answer destroys many witnesses" defence. **If I reach 9c, this multiplicity bound is the deliverable.**

## §4. The sketch, registered in advance

**Claim (to be proved or withdrawn).** For all bijective q_i and arbitrary b_i, any correct deterministic back-mapping in Definition 9's model has qw ≥ N/poly(n).

*Sketch.* Fix y for which Φ_y is satisfiable (§2c). Adversary maintains partial ρ on inputs plus the invariant **S**: the ρ-restricted Φ_y is satisfiable, witnessed by a stored assignment σ. Answer a width-w DNF by Wilson's rule with "consistent" read as "consistent with ρ **and** extendable inside Φ_y"; when using a term, fix its ≤ w bits and complete each newly fixed input from σ, re-choosing σ if the term forced bits σ disagreed with (possible iff the term is Φ_y-compatible; otherwise the term is unusable). "False" is sound relative to the family of Φ_y-satisfying assignments, and Q must be correct for every member of it. At the end Q outputs y′; pick a free x* whose ≤ n+2 touched clauses survive setting C(x*) = y′, and complete. Then y′ ∈ range(C) and Q is wrong. ∎

**Where I expect trouble:** (i) proving a free, placement-safe x* always exists — this is Flag O9 and is the reason I say N/poly rather than N − 1; (ii) the case |P_x| < n+2 for many x, which raises p above 2^{−(n+2)}; (iii) b_i colliding in ways that make some clauses trivial and others rigid.

## §5. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **9a** maintainability proved for all q_i bijective, giving qw ≥ N/poly | 45 | **50** |
| **9b** a projection template beating Lemma 6 is found | 10 | **5** |
| **9c** neither; obstruction named | 45 | **45** |

**Why I am slightly above on 9a:** §2's multiplicity count is the whole ballgame and it came out at **n+2**, which leaves LLL an exponential margin; combined with Flag N9's observation that maintainability is nearly free, the bijective case looks reachable. **Why not higher:** Flag O9 is unresolved and is exactly the kind of "find a good free element" step that has broken my arguments before.

**Why I am below the reviewer on 9b:** projections are the side Miles–Viola prove **impossible** for PRGs (their Theorem 1.4, strengthened by Applebaum to AC⁰). A projection template beating Lemma 6 would sit on the settled-impossible side of the PRG mirror. That is suggestive, not binding — the two problems differ exactly as W7 established (no pseudorandomness in Avoid) — so 5, not 0.

## §6. Owed from W8, to be worked and not adopted

The reviewer's ruling asks me to record two corollaries of Lemma W8.1. **I will derive both myself rather than transcribe them**, because one of its stated conclusions looks off to me in advance:

1. **Masked single-call**, C′(x) = (C(x) ⊕ m(x), h(x)). The invariant becomes the **input-dependent** forbidden value C(x) ≠ z ⊕ m(x) on h⁻¹(b). The reviewer says the bound degrades to qw ≥ 2^{−O(1)}·N *"unless m is constant"*. **My pre-registered doubt: I think constant m is the benign case** (it reduces to W8.1 with z shifted), and the cost is instead governed by the density of the bad set {x : m(x) = z ⊕ y′} ∩ h⁻¹(b) — with placement also available **outside** h⁻¹(b), where the invariant does not apply at all. I will do the arithmetic and report whichever of us is right.
2. **x-bit-copying projections**, e.g. C′(x) = (x₂…x_n, C(x)₁C(x)₂C(x)₃), where the hint constrains C at few inputs and Wilson goes through with those committed.

## §7. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only. No value queries anywhere.
- **(ii)** Determinism in every statement (Flag H7).
- **(iii)** Any 9b candidate checked for **totality over all y** by hand at the smallest n.
- **(iv)** Consistency with Wilson (qw ≥ N unaided) and with the fold at depth log(T/n).
- **(v)** Every number reported with the bound it is compared against beside it; exact results distinguished from upper bounds (the W8 hitting-set lesson).
- **(vi)** If the proof does not close, name the step. Do not present a sketch as a result.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*
