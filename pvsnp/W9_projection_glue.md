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

---

# Findings (written after the attack; priors above are unrevised)

*Model throughout: Korten Definition 9 / Wilson Theorem 12, DNF queries of width w, q of them, **deterministic** back-mapping. Computations in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors, and two misses of mine

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **9a** re-scoped: proved for every projection template whose case analysis closes | **50** / 45 | **achieved for the families in §2–§4; residual named in §5** |
| **9b** a projection template beating Lemma 6 | 5 / 10 | no — but the trap in §4 shows *why* one would have to look here |
| **9c** neither | 45 / 45 | — |

**Miss 1 — Flag P9 was backwards, and it was the flag I priced the round on.** I predicted that **non-injective** q_i is the obstruction, because one input's bits then sit in exponentially many clauses and LLL dies. It is the **easy** case: take H = image(q_i), which hits every S_x by definition. High multiplicity means **one forced bit satisfies exponentially many clauses at once**. My whole §2(e) reasoning had the sign wrong — I was counting the difficulty of *satisfying* the CNF when the adversary's task is to satisfy it *cheaply*.

**Miss 2 — my §6 "doubt" was a misparse, not a disagreement.** The reviewer wrote that the masked bound degrades *unless* m is constant. I read it as asserting constant m was the *bad* case and pre-registered a doubt against a position it never held. The refinement I attached (placement is also available outside h⁻¹(b)) is correct and is used in §6 below, but there was no disagreement to have.

**The device below is the reviewer's, not mine.** It replaces my LLL/CSP plan entirely, and it is what makes the round close.

## 1. The forced-bit device, and the lemma it yields

**Set-up.** S_x = {q_i(x) : i ∈ [n+2]} is the set of *call-inputs* of x. K_x is **vacuous** (true for every oracle) iff some i ≠ j have (q_i(x), b_i(x)) = (q_j(x), b_j(x)) with y_i ≠ y_j — one bit cannot equal two different values.

**The device.** The adversary picks y and, for each non-vacuous x, a designated coordinate i(x), and **forces the single oracle bit** (q_{i(x)}(x), b_{i(x)}(x)) := ¬y_{i(x)}. Let F₀ be the resulting partial assignment of oracle bits, and let

  **U_free = {u : no bit of C(u) is forced by F₀}.**

Two obligations:
**(1) Consistency** — no bit is forced to both values.
**(2) Freedom** — |U_free| is large.

**Lemma W9.0.** *Suppose F₀ satisfies (1) and |U_free| > qw. Then every deterministic Q in Definition 9's model making q queries of width w fails: there are an oracle C and a valid hint y ∉ range(C′) on which Q's output y′ lies in range(C).*

*Proof.* Let **F** be the set of total assignments extending F₀; it is non-empty by (1). Every member satisfies every K_x — vacuously, or via its designated forced literal — so **y ∉ range(C′) for every C ∈ F**, and y is a valid hint throughout. Run Wilson's adversary relative to **F**: maintain a partial ρ on inputs; on a DNF query, use a term iff some assignment in **F** is consistent with it and with ρ, extending ρ on ≤ w inputs; otherwise answer false, which is sound because every completion inside **F** falsifies every term. After q queries |dom ρ| ≤ qw < |U_free|, so some x* ∈ U_free \ dom ρ exists. Q outputs y′. Set C(x*) = y′ — permitted, since **no bit of C(x*) is forced** — and complete arbitrarily respecting F₀. Every clause keeps the witness it already had (vacuity, or a forced bit, which cannot sit at x*), so the result lies in **F**; all answers remain true; and y′ ∈ range(C). ∎

**Why this is stronger than my registered plan.** Nothing is *maintained*: the invariant is a fixed partial assignment chosen in advance, exactly as the single forbidden value was in Lemma W8.1. My §4 sketch's "extend along a stored satisfying assignment" was unnecessary machinery.

## 2. Case (a): when the call-inputs are spread

Throughout this case take **y = 0^{n+2}**, so every forced value is 1 and **(1) is automatic**.

**Lemma W9.2a (distinct call-inputs).** *If |S_x| ≥ n+1 for every x, then qw ≥ 0.4N for all large n.*

*Proof.* Put each u ∈ {0,1}ⁿ into H independently with probability 1/2. A fixed S_x is missed with probability ≤ 2^{−(n+1)}, so the expected number of missed sets is ≤ N·2^{−(n+1)} = 2ⁿ/2^{n+1} = 1/2, and P[some S_x missed] ≤ 1/2. By Chernoff P[|H| > 0.6N] ≤ exp(−2N(0.1)²) < 1/2 for large n. So some H hits every S_x with |H| ≤ 0.6N. Designate for each x a coordinate with q_{i(x)}(x) ∈ H; forced bits then lie only at inputs of H, so |U_free| ≥ 0.4N. Apply Lemma W9.0. ∎

**Lemma W9.2b (all call-sets of size ≥ 2).** *If every non-vacuous x has |S_x| ≥ 2, then qw ≥ N/5 for all large n.*

*Proof.* Random H of density 1/2 misses a given S_x with probability ≤ 1/4, so in expectation ≤ N/4 sets are missed; fix H attaining this with |H| ≤ 0.55N (Chernoff), then add one element per missed set, giving a hitting set of size ≤ 0.55N + 0.25N = 0.8N. Hence |U_free| ≥ 0.2N. ∎

**Lemma W9.2c (substantially non-injective calls) — and a correction to the reviewer's version.** *If some q_i has |image(q_i)| ≤ N − N/poly, then H = image(q_i) hits every S_x and qw ≥ N/poly.*

The reviewer stated this for q_i merely **non-injective**, concluding |U_free| ≥ N/2. **That does not follow:** non-injectivity alone gives only |image(q_i)| ≤ N − 1, hence |U_free| ≥ 1, which is far too weak for Lemma W9.0. The hypothesis must be quantitative. It is satisfied by the intended example q(x) = (x₁…x_{n/2}, 0…0), where |image| = 2^{n/2} = √N and |U_free| ≥ N − √N.

## 3. Case (b): singleton call-sets, closed by max-cut

Here every call of x reads the same input: S_x = {u_x}.

**Pigeonhole.** All n+2 coordinates read bits of the single (n+1)-bit string C(u_x), so some i ≠ j have b_i(x) = b_j(x). Fix one such colliding pair e_x = {i, j} for each x, and let **G** be the multigraph on vertex set [n+2] with edge e_x for each x. **K_x is vacuous iff y 2-colours some colliding pair of x bichromatically** — in particular if y cuts e_x.

**Lemma W9.3.** *If every |S_x| = 1 and x ↦ u_x is injective, then qw ≥ N/2.*

*Proof.* A uniformly random y ∈ {0,1}^{n+2} cuts each edge of G with probability 1/2, so some y cuts at least half of the N edges (max-cut ≥ m/2). Those x are vacuous and need no forced bit. For each remaining x force one bit of C(u_x). **Condition (1) is automatic here:** injectivity of x ↦ u_x means each input u carries forced bits from at most one x, which forces exactly one bit. So |U_free| ≥ N/2, and Lemma W9.0 applies. ∎

**If x ↦ u_x is *not* injective**, the forced set {u_x} has size < N and the situation falls into Lemma W9.2c's shape — few inputs carry forced bits, so U_free is large. **The two sub-cases are complementary**, which is what closes case (b).

**Measured (sampled, random b_i, all q_i = identity).** Max-cut guarantees ≥ N/2 vacuous; the best y did far better — 8/8, 8/8, 8/8 at N = 8; 16/16, 16/16, 15/16 at N = 16; 30/32, 31/32, 31/32 at N = 32 — with condition (1) holding in every instance and free inputs equal to the vacuous count. **These are samples over random b_i, not exhaustive, so they validate the mechanism; the proof rests on the ≥ N/2 max-cut bound, not on the observed near-totality.**

## 4. The trap, confirmed — why condition (2) is a real obligation

With all q_i = identity and **y = 0^{n+2}**, no clause is vacuous, so the device forces a 1-bit at **every** input; then no oracle in the family has 0^{n+1} in its range, and **Q wins by outputting 0^{n+1}**. My control reproduces this exactly: at N = 8 and N = 16, vacuous count 0 and forced inputs N of N.

**Reading.** This is not a defect of the device but the content of obligation (2): **a forced set that touches every input does not merely fail to help the adversary — it hands the reduction a correct answer.** It also shows the choice of y is not free: at this template the max-cut y of §3 is right and y = 0 is exactly wrong. The reviewer's rule — maximise vacuity first, hit the remainder, then verify (2) — is the correct order, and the trap is the proof that verification cannot be skipped.

## 5. The residual class, stated precisely (as ruled)

The case analysis closes when a **single** y discharges both jobs. It is not proved for:

> **Mixed templates** in which a constant fraction of inputs have |S_x| = 1 with x ↦ u_x injective, *and* a constant fraction have |S_x| ≥ 2, where the singleton part demands the **max-cut y** of Lemma W9.3 while §2 obtains condition (1) from **y = 0**. A single hint must serve both, and I have not shown the two choices can be reconciled.

**What a repair would need.** Under a general y the forced value ¬y_{i(x)} varies with the designated coordinate, so condition (1) can fail when two inputs designate the same bit via coordinates of opposite y-value. There is slack — for |S_x| ≥ 2 one may choose *which* element of S_x to hit, and often which coordinate — so I expect this is reconcilable, but **expecting is not proving, and it is the open step.**

## 6. The two corollaries owed from W8

**Corollary W8.2 (masked single-call).** For C′(x) = (C(x) ⊕ m(x), h(x)) the invariant is the input-dependent forbidden value **C(x) ≠ z ⊕ m(x) on h⁻¹(b)**. Placement needs a free x* with either x* ∉ h⁻¹(b) — where the invariant says nothing, so **any** such x* works — or x* ∈ h⁻¹(b) with y′ ≠ z ⊕ m(x*). The bad set is B = h⁻¹(b) ∩ m⁻¹(z ⊕ y′), giving **qw ≥ N − |B| − 1**. If m ≡ c is constant, B is either empty or all of h⁻¹(b); in the latter case the adversary instead takes the **vacuous** hint (z, ¬b) — the range of C′ misses every string with second coordinate ¬b — and Lemma W8.1's bound applies unaided. **So constant m is the benign case**, as the reviewer said.

**Corollary W8.3 (x-bit copying).** For C′(x) = (x₂…x_n, C(x)₁C(x)₂C(x)₃), a hint y = (w, c) is non-range iff both inputs x ∈ {0w, 1w} have C(x)₁₂₃ ≠ c. **The hint constrains C at exactly two inputs**, so F₀ forces bits at two inputs, |U_free| = N − 2, and **qw ≥ N − 2**: Wilson goes through with two committed positions.

## 7. Kill tests

- **(i)** Definition 9 / Theorem 12 model only; no value queries anywhere.
- **(ii)** Determinism is in every lemma statement (Flag H7).
- **(iii)** No 9b candidate arose, so totality checking is moot — but §4 records the one place a candidate would live, and it is a genuine win for Q, verified by control.
- **(iv)** Consistency: every bound here is **at most** Wilson's qw ≥ N and reduces to it when F₀ = ∅ (Lemma W9.1's vacuous case); nothing claims anything about the fold with a hard string.
- **(v)** Numbers reported with their comparison bound beside them, and sampled results are labelled sampled (§3).
- **(vi)** The step that does not close is named in §5 rather than papered over.
- **Priors wrong said with the finding:** §0, Misses 1 and 2.

## Ceiling

Unchanged. **W9 proves nothing about P vs NP.** It closes the projection-glue family for spread call-sets, substantially non-injective calls, and singleton calls, deterministically and black-box, leaving one mixed residual. Korten's Problem 1 — arbitrary glue — is untouched, and by Flag H7 none of this survives randomisation.
