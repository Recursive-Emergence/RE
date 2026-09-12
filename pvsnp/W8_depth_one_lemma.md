# W8: the depth-1 lemma with NC⁰ glue. Pre-registration

*Drafted 2026-09-12 on branch `w8-depth-one-lemma`, on the reviewer's W8 specification, after its W7 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the attack. The proof sketch in §4 is registered in advance precisely so that it can be broken; if it fails, the report says where.**

## Ceiling (first)

Unchanged from W7 and still the binding constraint. **This settles nothing about P vs NP, nothing about Avoid ∉ FP^NP, and — by Flag H7 — not even a randomised statement.** At stretch n ↦ n+1, at least half the codomain avoids range(C) and membership is one NP^C query, so guess-and-test sits in FZPP^{NP^C} at depth 0. **Every statement in W8 is about *deterministic* back-mappings**, and a full 8a would say only that one naive template family cannot beat Lemma 6 by one bit, black-box.

## §0. Refuted premises checked

Not reused: "(PL) is loose-access lowness" (Y6); "the Pessiland oracle does not bar the route" (Y7); "the generator's outputs are deep" (Y9); "prefix descent must resolve a deficit of 1" (W5); "(D1) is smaller than the door" (W4 prose); "the n term is the stubborn summand" (W6, refuted). **From W7, two of mine:** the value-query computations **do not transfer** to the NP^C model and are not evidence here; and Korten's [36] **is** Miles–Viola, retitled between TCC 2011 and J. Cryptology 2013 — I misidentified it mid-run before Viola's own listing settled it.

**Standing practice lines:** never reconstruct a dropped superscript inside a quotation; do the counting before the prior, including **removability**; and (new, from W7) **a lower bound proved in a weaker query model is not a lower bound** — stay in Theorem 12's DNF model throughout.

## §1. The model, fixed (decided in W7, restated so the proof has something to quantify over)

- **Oracle:** C : {0,1}ⁿ → {0,1}^{n+1}, arbitrary. Write N = 2ⁿ.
- **Construction:** C′ : {0,1}ⁿ → {0,1}^{n+2} is a fixed template of C-gates with NC⁰ glue, **depth 1** — no C-gate's input depends on another C-gate's output. **The NP^C oracle may not be used while building C′** (Lemma 6 does not, and allowing it destroys the depth accounting, since an NP^C query is not a C-gate).
- **Back-mapping:** A is **deterministic**, poly(n) time, with an NP^C oracle; given any y ∉ range(C′) it must output y′ ∉ range(C). Totality is over **every** such y — the adversary chooses which.
- **Query model (kill test (i)):** as in Korten §6.2 Theorem 12, each NP^C query is a **width-w DNF over the oracle's bits**, w = poly(n), and A makes q = poly(n) of them. Wilson's bound is qw ≥ N. **No value queries anywhere.**

## §2. The counting, done before the prior

Take C **injective** (the adversary's choice; it only makes Avoid harder). Then |range(C)| = N out of 2N.

**Single-call template** C′(x) = (C(x), h(x)), h : {0,1}ⁿ → {0,1} arbitrary (NC⁰ or not):
y = (z,b) ∉ range(C′) ⟺ **C⁻¹(z) ⊆ {x : h(x) ≠ b}**.
- If z ∉ range(C) the condition is vacuous: **both** (z,0) and (z,1) are non-range. That is 2N hints.
- If z ∈ range(C) with unique preimage x_z, exactly one b qualifies, namely b = 1 − h(x_z). That is N hints.
- **Total 3N = 3·2ⁿ**, matching the general count (|range(C′)| ≤ 2ⁿ out of 2^{n+2}).

**What each kind of hint is worth.**
- z ∉ range(C): A outputs **z** and is done — one NP^C query confirms it. **The reduction succeeds on 2N of the 3N hints trivially.**
- z ∈ range(C): A learns "every preimage of z has h ≠ b", i.e. (C injective) h(x_z) = 1−b. **A can even locate x_z**: prefix search with the NP^C queries "∃x with prefix p, C(x) = z" costs n queries. So A ends up knowing **one input–output pair of C**, and nothing else.

**So the adversary's move is forced and obvious: hand over a hint of the second kind.** The whole question for this family is whether knowing O(1) input–output pairs of C helps a deterministic P^{NP^C} machine find a non-range point — and Wilson says finding one unaided needs qw ≥ N.

## §3. Flags

- **Flag K8 — the hint is under the adversary's control, and for single-call templates it is nearly worthless.** Registered as the expected mechanism of 8a.
- **Flag L8 — the danger case for step 3, named in advance.** For k parallel calls with projection glue, "y ∉ range(C′)" may be forced only **globally** — each x excluded by a *different* coordinate — so no local certificate need exist. **If almost all non-range y lack a poly(n)-size certificate, that is the obstruction and the outcome is 8c**, not 8a. I expect this to be where the single-call proof stops generalising.
- **Flag M8 — the invariant/commitment conflict is the one real risk in §4.** Wilson's adversary answers a DNF FALSE only when *no* consistent extension satisfies any term. Adding the invariant "no x with h(x) = b maps to z" shrinks the family of admissible C, which can only make more terms unsatisfiable — so FALSE answers stay valid **relative to the restricted family**. The proof must say explicitly that correctness of A is required *for every C in that family*, so exhibiting one is enough. **If that quantifier slips, the proof is wrong.**

## §4. The proof sketch, registered in advance so it can be broken

**Claim (to be proved or withdrawn):** for every h and every deterministic poly-time A with NP^C oracle, there is an injective C and a hint y = (z,b) ∉ range(C′) on which A fails.

*Sketch.* Run Wilson's adversary, maintaining a partial injective ρ with |dom(ρ)| ≤ qw, plus the invariant **I**: no x with h(x) = b has C(x) = z. Commit at the start to one x₀ with h(x₀) ≠ b and ρ(x₀) = z, so z ∈ range(C) and the hint is valid. Answer each width-w DNF query by Wilson's rule, restricted to extensions satisfying **I**. At the end A outputs y′.
- If y′ = z: A is wrong, since z ∈ range(C) by construction.
- If y′ ≠ z: pick any x* ∉ dom(ρ) — one exists because qw < N — and set C(x*) = y′. This respects **I** (which constrains only the value z) and injectivity (y′ ∉ ρ's image, else A queried it). So y′ ∈ range(C) and A is wrong. ∎

**Degenerate case to handle explicitly:** if h is constant ≡ b then every (z, 1−b) is non-range vacuously, A gets nothing, and Wilson applies unchanged.

**Where I expect the write-up to be harder than the sketch:** making "y′ ∉ ρ's image, else A queried it" precise in the DNF model — a DNF answer commits *sets* of oracle bits, not single values — and confirming that the count qw < N survives the n extra prefix-search queries.

## §5. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **8a** impossible, full proof for at least the single-call family | 45 | **55** |
| **8b** a reduction exists, constructed and verified total | 15 | **10** |
| **8c** neither; obstruction named | 40 | **35** |

**I am above the reviewer on 8a, and the reason is that I did §2 and §4 before pricing rather than after.** The single-call family collapses to "does O(1) input–output pairs of C help", and Wilson already answers that. The W6 lesson was that I priced a term's *origin* without checking its *removability*; here the counting and the adversary move are both done in advance, so the prior is earned rather than guessed.

**Why I am nonetheless not higher than 55.** Flag M8 is a genuine risk, and the step-3 family (projection glue, the Miles–Viola form) is where I expect the argument to stop — **8a as the reviewer defines it only needs the single-call family, but a proof that visibly cannot generalise one inch is worth less than its code suggests**, and the report must say so rather than bank the outcome.

**Why I am below the reviewer on 8b.** A depth-1 "up" construction would have to make nearly all 3N non-range hints informative (W7's Flag J7), and Korten's bundle picture — n items, one round, one bundle — gives exactly n+1. I see no room, but "I see no room" is not evidence, which is why 8b is 10 and not 0.

## §6. Kill tests

- **(i) Theorem 12's DNF query model throughout.** No value queries. If I catch myself reasoning about "A asks for C(x)", the argument is void.
- **(ii) Determinism stated in every statement** (Flag H7).
- **(iii) Totality of any 8b candidate checked over ALL y by hand at the smallest n** — not sampled, not asserted.
- **(iv) Consistency with W1/W7:** without a hint Avoid ∉ FP^{NP^C} for random C (Wilson Thm 12); with a hard string the fold works at depth log(T/n) (RW26 Thm 3.1). Anything contradicting either is wrong.
- **(v) The quantifier in Flag M8 written out explicitly**, since that is where the proof would silently fail.
- **(vi) If the proof does not close, say exactly which step failed** and do not present the sketch as a result.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*

---

# Findings (written after the attack; priors above are unrevised)

*Sources: Korten, Bull. EATCS 145 (2025), §6.2 Definition 9 and Theorem 12 **including the proof's closing paragraph**, read this run; Miles–Viola (W7) for the projection form. Computation in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **8a** impossible, full proof for at least the single-call family | **55** / 45 | **achieved — Lemma W8.1 below, proved in Theorem 12's model** |
| **8b** a reduction exists | 10 / 15 | no |
| **8c** neither | 35 / 40 | — |

**Flags: K8 confirmed. M8 confirmed and handled explicitly (§2, step 4). L8 confirmed, and stronger than I registered — see §3.**

**A correction to the reviewer's plan, and it is the main structural finding (§3): step 1's "choose a y whose non-membership has a LOCAL certificate" is not available — not for projection glue, and not even for the single-call family. Local certificates essentially never exist. The single-call proof closes anyway, because what the adversary needs is not a local certificate but a *maintainable invariant*.**

## 1. Wilson's model and proof, quoted, since everything below reuses it

**Definition 9** (Korten §6.2) fixes the model: an assignment α defines f_α : [N] → [M]; a query algorithm Q *"may choose at each step a DNF D over the variables {α_i}, and receive its value"*, and *"the 'width complexity' of Q is the maximum width of a DNF it queries, and the 'query complexity' is the maximum number of queries it makes"*.

**Theorem 12's adversary, verbatim**: *"At each step we maintain a partial assignment ρ : [N] → [M], so that after t steps we have |domain(ρ)| ≤ tw. When a DNF D = ⋁_j τ_j is presented, we search for a term τ_j such that there exists a total assignment consistent with both τ_j and the current partial assignment ρ. If so, then since the width of τ_j is at most w, we may extend ρ to ρ′ by defining it on at most w additional inputs so that already τ_j(α) = 1 for all total assignments α extending ρ′; the adversary then answers 'true' for the DNF query D. If it cannot find such an extension the adversary answers 'false;' in this case we know that for any extension of ρ we will always falsify all terms in D."*

**And the closing step, verbatim**: *"Now, if qw < N then the adversary may continue this process q times and reach a termination point of Q, after which Q must output some candidate solution y. Since at this point |ρ| ≤ qw < N, there is some x ∈ [N] so that ρ(x) is undefined; the adversary then sets ρ(x) = y and completes ρ everywhere else to a total assignment α. At this point all the query responses supplied by the adversary are true of α, however y ∈ range(f_α), hence Q(α) has the wrong behavior."*

**Kill test (i) satisfied:** everything below is in this DNF model. No value queries appear.

## 2. Lemma W8.1 — the single-call family, proved

**Setting.** Fix n, N = 2ⁿ, and C : {0,1}ⁿ → {0,1}^{n+1} presented as an assignment α in Definition 9's sense. Fix any h : {0,1}ⁿ → {0,1} (**arbitrary** — NC⁰ is a special case, so the lemma is stronger than the target asks). Let the depth-1 construction be

  **C′(x) = (C(x), h(x)) ∈ {0,1}^{n+2}.**

Let Q be a **deterministic** algorithm that receives a hint y ∉ range(C′), makes q DNF queries of width ≤ w, and outputs y′ ∈ {0,1}^{n+1}.

**Lemma W8.1.** If **qw + 1 < N** then there are an assignment α and a valid hint y ∉ range(C′) such that Q's output satisfies y′ ∈ range(C). Hence any correct deterministic back-mapping for a single-call depth-1 template has **qw ≥ N − 1**.

*Proof.* Fix a bit b and a string z ∈ {0,1}^{n+1}, chosen as follows.

**Case 1 — h omits the value b** (i.e. h(x) ≠ b for all x). Then for **every** z, (z,b) ∉ range(C′) vacuously. Take y = (z,b) with z arbitrary, and let the invariant **I** be trivially true.

**Case 2 — h attains both values.** Fix any b, pick x₀ with h(x₀) ≠ b, take any z, and commit ρ(x₀) = z. Let **I** be: *for every x with h(x) = b, C(x) ≠ z.* Under **I**, no x has C′(x) = (z,b) — inputs with h(x) = b fail on the first coordinate, inputs with h(x) ≠ b fail on the second — so **y = (z,b) is a valid hint**, and z ∈ range(C) by the commitment.

Let **F** be the family of total assignments satisfying **I** and extending the commitment. Run Wilson's adversary **with every "exists a total assignment" replaced by "exists a total assignment in F"**. Its two answer rules remain sound relative to F: a "true" answer is forced by ρ, and a "false" answer holds for every completion **within F**, which is all that is needed because **Q is required to be correct for every C in F** — exhibiting one failing member suffices. *(This is Flag M8, and it is exactly where the quantifier must not slip.)*

After q queries, |domain(ρ)| ≤ qw + 1 < N, so some x* has ρ(x*) undefined. Q outputs y′.
- **If y′ = z.** In Case 2, z ∈ range(C) already by the commitment, so Q is wrong. In Case 1, set C(x*) = z; **I** is vacuous there, so this is permitted, and Q is wrong.
- **If y′ ≠ z.** Set C(x*) = y′ and complete ρ arbitrarily subject to **I**. This respects **I**, which forbids only the single value z on h⁻¹(b). All answers given remain true of the completed α, and y′ ∈ range(C), so Q is wrong. ∎

**Reading of the bound.** Wilson unaided gives qw ≥ N. With a single-call hint the bound is qw ≥ N − 1. **The hint from a single-call depth-1 template is worth at most one oracle position.** That is the quantitative content of 8a for this family, and it is the precise sense in which this template "hides nothing".

**Scope, stated plainly rather than banked.** Lemma W8.1 covers **one call plus arbitrary glue**. It is not a proof of Korten's Problem 1, not a proof for NC⁰ glue in general, and — by Flag H7 — not even a randomised statement: guess-and-test at this stretch is in FZPP^{NP^C} at depth 0. **The lemma says a naive template family cannot beat Lemma 6 by one bit, deterministically, black-box.**

## 3. Flag L8 confirmed, and the correction to step 1

The reviewer's step 1 asks for a hint whose non-membership has a **local certificate** — "a constraint on C at few positions". **That is not available, and the computation says so quantitatively.**

**The right formalisation.** A certificate for "y ∉ range(C′)" is a set S of oracle **bits** whose values already force C′(x) ≠ y for every x. For input x the coordinates currently witnessing a mismatch are W_x; S is a certificate iff S meets every W_x. **So the minimum certificate is a minimum hitting set**, and it is computable exactly at small n.

| n | N | hints measured | exact result | greedy upper bounds |
|---|---|---|---|---|
| 3 | 8 | 150 | 8 hints (5.3%) have minimum size 3; 49 (32.7%) size 4; **93 (62%) exceed 4** | 5–8 |
| 4 | 16 | 300 | **all 300 exceed 4** (exhaustive over every subset of size ≤ 4) | 6–13, clustering 9–10 |

**Sound content:** the "exceeds 4" figures are exact, from exhaustive search over all subsets of size ≤ 4. The greedy column is an **upper** bound on the minimum, not the minimum — the true value lies between 5 and the greedy figure, and I do not claim it is the greedy figure.

**And the same holds for the single-call family**, by hand: certifying (z,b) ∉ range(C′) requires C(x) ≠ z for **every** x with h(x) = b — about N/2 constraints. So even the family I just proved impossible has no local certificates.

**The correction, therefore:** locality is the wrong lever. What made Lemma W8.1 work is that the hint's constraint is a **single forbidden value on a set of inputs**, which the adversary can carry as an invariant at zero cost. Under **projection glue** the invariant instead reads *"for every x, at least one coordinate i has C(q_i(x))_{b_i(x)} ≠ y_i"* — a **covering/disjunctive** condition, in which one "true" answer can destroy the surviving witness for many inputs at once. **That, not locality, is the obstruction to extending Lemma W8.1**, and it is the precise form of Flag L8.

## 4. Kill tests

- **(i) DNF model throughout.** Satisfied; §1 quotes the model and §2 works inside it. No value queries. *(W7's value-query numbers are not cited here as evidence, per the standing practice line.)*
- **(ii) Determinism.** In the lemma statement, and Flag H7 restated in §2's scope paragraph.
- **(iii) Totality of an 8b candidate.** Not applicable — no 8b candidate was produced.
- **(iv) Consistency with W1/W7.** Lemma W8.1 **degrades** Wilson's bound from qw ≥ N to qw ≥ N − 1, so it neither contradicts nor strengthens him; and it says nothing about the fold with a hard string (RW26 Thm 3.1, depth log(T/n)), which is a different object.
- **(v) The Flag M8 quantifier** is written out in the proof, in the sentence beginning "Its two answer rules remain sound relative to F".
- **(vi)** The proof closed; where it does **not** extend is stated in §2's scope paragraph and §3.

## Ceiling

As pre-registered. **W8 proves nothing about P vs NP.** It closes one naive template family, deterministically and black-box, with a bound that degrades Wilson's by exactly one; and it replaces the reviewer's locality heuristic with the property that actually did the work. **Korten's Problem 1, and even its NC⁰-glue restriction, remain open.**
