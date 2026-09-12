# W10: closing the residual for all projection templates. Pre-registration

*Drafted 2026-09-12 on branch `w10-projection-closed`, on the reviewer's W10 specification, after its W9 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the write-up. §2 contains a full disclosure of work already done, so that the priors are honest rather than merely early.**

## Ceiling (first)

Unchanged since W7. **Nothing here touches P vs NP or Avoid ∉ FP^NP.** By Flag H7 everything is about **deterministic** back-mappings; guess-and-test at this stretch is in FZPP^{NP^C} at depth 0. A full 10a would say: **no projection template beats Lemma 6 by one bit, black-box, deterministically.** Korten's Problem 1 — arbitrary polynomial-time glue — would remain open, and the NC⁰ part of this round is explicitly a **map, not a proof**.

## §1. Refuted premises checked

Not reused: "the generator's outputs are deep" (Y9); "prefix descent must resolve a deficit of 1" (W5); "the n term is the stubborn summand" (W6); value-query results do not transfer (W7); "pick a hint with a local certificate" (W8); **"non-injective q_i is the obstruction" (W9, mine — Flag P9 was backwards; it is the easy case)**; **"the forced set is small" as an unquantified step (W9, mine — corrected)**; **"each singleton clause forbids one value" (the reviewer's W10 justification — false when |B_x| = 1, see §2)**.

**Standing practice lines:** stay in Definition 9's DNF model; count removability, not only origin; never reconstruct a dropped superscript inside a quotation; **quantify every "small"/"large" claim** (W9's lesson, which I had to learn on my own text after charging it to the reviewer).

## §2. Disclosure: what I already derived before writing these priors

**Pre-registration is worthless if it hides prior work, so this is on the record before the attack.** While reading the ruling I worked out the following, and my 10a prior reflects it:

**(a) The reviewer's justification for full-value forcing is wrong as stated.** It argues that each non-vacuous singleton clause at u "forbids one pattern", so ≤ N/2 clauses forbid ≤ N/2 of the 2^{n+1} values. **A clause with index set B_x forbids 2^{n+1−|B_x|} values — half the space when |B_x| = 1** — so the sum can exceed the whole space and existence does not follow from that count.

**(b) A one-line replacement that does work — Lemma W9.4 (all-ones), already committed to the W9 page.** Let A = {i : y_i = 1}, B = {i : y_i = 0}. For non-vacuous x, b(x)(A) and b(x)(B) are **disjoint** (a shared position would carry two y-values at colliding coordinates, making K_x vacuous). The forbidden pattern is 1 on b(x)(A) and 0 on b(x)(B). So if **B ≠ ∅**, the value **c(u) = 1^{n+1}** satisfies every non-vacuous singleton clause at every u; symmetrically 0^{n+1} if y = 1^{n+2}.

**(c) Consequence I expect to carry the round.** Full-value forcing with the constant value 1^{n+1} makes **(1) automatic** (one value per input) and needs no counting. Combined with max-cut for vacuity and the sum-of-expectations hitting set, the three cases of W9 stop needing different hints for different reasons — which is exactly what the residual was.

**(d) What I have NOT done:** the |S_x| ≥ 2 part under a **general** y. W9's §2 used y = 0^{n+2} to make forced values uniform; under a max-cut y the designated coordinate's value ¬y_{i(x)} varies. Lemma W9.4 suggests the repair (force the full value 1^{n+1}, which satisfies a clause as soon as *some* coordinate of the clause has y_i = 0), **but I have not checked it for non-singleton clauses, where the clause's coordinates read bits at several different inputs.** That is the real open step and it is where I expect 10a to be won or lost.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **10a** one unified lemma for all projection templates, qw ≥ N/poly | 55 | **60** |
| **10b** a mixed template where every valid hint certifies a string out of range(C) | 10 | **5** |
| **10c** residual remains; obstruction named | 35 | **35** |

**Why I am above the reviewer on 10a:** §2(b) is proved and committed, and it removes the one structural reason the three cases needed different hints. **Why not higher:** §2(d) is untouched, and multi-input clauses are where the all-ones trick could simply fail to apply — a clause spanning several inputs is satisfied by forcing 1s only if some coordinate of it has y_i = 0 **and** that coordinate's bit is one I am actually forcing.

**Why I am below the reviewer on 10b:** the trap (all q_i = identity, y = 0) shows that a template *can* certify a string out of range — but only for a **bad choice of hint**, and the adversary picks the hint. For 10b one would need **every** valid hint to certify, which the max-cut hint already defeats in the singleton case. So 5, not 0 — and if a candidate appears, kill test (iii) applies: totality by hand.

## §4. Flags

- **Flag Q10 — the multi-input clause is the whole difficulty.** For |S_x| ≥ 2 the clause's coordinates read bits at different inputs, so "force 1^{n+1} at the inputs of H" satisfies K_x only if some coordinate i with y_i = 0 reads a bit at an input **in H**. Registered as the step to prove.
- **Flag R10 — condition (2) must be re-verified after switching to full-value forcing.** Full values are far more restrictive than single bits: forcing c(u) = 1^{n+1} on all of H pins those inputs entirely. The §4 trap of W9 is the warning. **No string is excluded so long as U_free ≠ ∅**, since any y′ can be placed at a free input — but this must be *stated*, not assumed.
- **Flag S10 — the NC⁰ scoping is a map, not a proof, and must be labelled so in the deliverable.** With C′(x)_i = g_i(x, O(1) oracle bits), a coordinate is satisfied by forcing an O(1)-bit **pattern** rather than one literal. I expect hitting sets over pattern-sets and placement to survive, and **patterns spanning several inputs (e.g. g_i = XOR of bits at two inputs) to need a new idea**, because forcing then constrains a *relation* between inputs rather than a value at one.

## §5. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only; no value queries.
- **(ii)** Determinism in every statement (Flag H7).
- **(iii)** Any 10b candidate checked for **totality over all y** by hand at the smallest n.
- **(iv)** Every "small"/"large" quantified — the W9 lesson, applied to my own text first.
- **(v)** Consistency: every bound at most Wilson's qw ≥ N, reducing to it when nothing is forced.
- **(vi)** Numbers with their comparison bound beside them; sampled results labelled sampled; exact results labelled exact.
- **(vii)** If the unified lemma does not close, name the step and deliver the obstruction — do not present §2(c) as if it were §2(d).
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*

---

# Findings (written after the attack; priors above are unrevised)

*Model: Korten Definition 9 / Wilson Theorem 12, DNF queries, **deterministic** back-mappings. Computations in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **10a** one unified lemma for all projection templates | **60** / 55 | **achieved, with an explicit hypothesis (β ≤ 1 − δ) that subsumes every case of W9** |
| **10b** a mixed template where every valid hint certifies a string out of range | 5 / 10 | no; none found, and the search in §6 looked for one |
| **10c** residual remains | 35 / 35 | **the residual is now a single named class (§5), much smaller than W9's** |

**Correction to my own working note.** In the course of the attack I announced a threshold **α < 1/3**. That came from bounding |R| ≤ N and applying the sampling probability to all N inputs. Doing it properly — sampling only outside the forced set, and using |R| ≤ (1 − α)N — gives the threshold **β < 1**, a far weaker hypothesis. **The corrected computation is §3; the 1/3 figure was mine and was slack, not wrong-signed.**

## 1. Lemma W10.1 — the all-ones reduction

Write Z = {i : y_i = 0} and **S_x^Z = {q_i(x) : i ∈ Z}**.

**Lemma W10.1.** *Assume Z ≠ ∅ and force the full value c(u) = 1^{n+1} at every u ∈ H. Then:*
1. *condition (1) holds automatically — one value per input, so no bit is forced twice;*
2. *for every non-vacuous x, K_x is satisfied by F₀ **iff** S_x^Z ∩ H ≠ ∅;*
3. *no string is excluded from range(C), provided U_free ≠ ∅.*

*Proof.* (1) is immediate. (2): coordinate i yields a mismatch iff bit(q_i(x), b_i(x)) ≠ y_i. If q_i(x) ∈ H the bit is 1, so this holds exactly when y_i = 0, i.e. i ∈ Z; if q_i(x) ∉ H the bit is unforced and guarantees nothing. So F₀ satisfies K_x iff some i ∈ Z has q_i(x) ∈ H. (3): any v ∈ {0,1}^{n+1} may be placed at a free input, so no value is excluded from the range across the family. ∎

*(If y = 1^{n+2} so that Z = ∅, apply the symmetric device c(u) = 0^{n+1} with Z' = [n+2].)*

**This is the whole content of the round:** every case W9 handled separately becomes one question — **does H hit the restricted call-sets S_x^Z?** Per-coordinate forcing, the max-cut/y = 0 conflict, and the injectivity hypothesis all disappear.

## 2. Why the hint must carry at least two zeros

**If |Z| = 1**, say Z = {i₀}, then S_x^Z = {q_{i₀}(x)} is a **singleton for every x**, so every non-vacuous x forces its input and H ⊇ q_{i₀}({non-vacuous x}). If q_{i₀} is a bijection and few x are vacuous, H is everything and U_free is empty. **So a hint with exactly one zero is useless**, and the adversary needs |Z| ≥ 2 — while vacuity needs *both* values present among colliding coordinates. That tension is the only one left, and §5 is what remains of it.

## 3. The budget, computed correctly

Let V be the vacuous inputs, **A = {x ∉ V : |S_x^Z| = 1}** the singleton-type inputs with forced set **H₀ = {u_x : x ∈ A}**, and **R = {x ∉ V : |S_x^Z| ≥ 2}**. Put β = |H₀|/N, α = |A|/N (so β ≤ α), and r = |R|/N; A and R are disjoint, so **r ≤ 1 − α ≤ 1 − β**.

Include each u ∉ H₀ in H independently with probability p. Then
- E[|H|] ≤ βN + p(1 − β)N,
- E[#missed] ≤ rN(1 − p)², since every x ∈ R has |S_x^Z| ≥ 2.

At **p = 1/2**, using r ≤ 1 − β,
  **E[ |H| + #missed ] ≤ βN + (1−β)N/2 + (1−β)N/4 = N(β + 3)/4.**

So some H attains |H| + #missed ≤ N(β+3)/4; adding one element of S_x^Z per missed x gives a hitting set of that size. Hence

  **|U_free| ≥ N(1 − β)/4.**

**Theorem W10.2 (unified).** *Let a projection template admit a hint y with Z ≠ ∅ whose singleton-forced fraction satisfies β ≤ 1 − δ. Then every correct deterministic back-mapping in Definition 9's model has* **qw ≥ δN/4.**

*Proof.* Lemma W10.1 gives conditions (1) and (3) and reduces satisfaction to hitting; the display above gives |U_free| ≥ δN/4; apply Lemma W9.0. ∎

## 4. Every case of W9 is now a corollary

- **W9.2a / W9.2b** (spread call-sets): take y = 0^{n+2}, so Z = [n+2] and S_x^Z = S_x. If every |S_x| ≥ 2 then A = ∅, β = 0, and **qw ≥ N/4** — exactly the corrected W9.2b, now without a separate argument.
- **W9.2c** (substantially non-injective calls): H₀ ⊆ image(q_i), so β ≤ |image(q_i)|/N ≤ 1 − 1/poly, giving **qw ≥ N/poly**. The quantitative hypothesis I insisted on in W9 is exactly what makes β bounded away from 1.
- **W9.3** (singleton call-sets, the trap family): with y = 0 every x is singleton-type and β = 1 — **the theorem correctly refuses to apply, which is the trap**. With a max-cut hint at least half the inputs are vacuous, so β ≤ 1/2 and **qw ≥ N/8** by Theorem W10.2 (the direct argument of W9.3 still gives the sharper N/2; the unified bound is deliberately conservative).

## 5. The residual, now a single class

> **Templates for which *every* hint y with |Z| ≥ 2 has β = 1 − o(1)** — that is, the singleton-type non-vacuous clauses force essentially every input, for every choice of hint.

**I could not exhibit such a template, and the search in §6 did not find one.** Both mechanisms that push β up — concentrating a template's calls on one input, and shrinking Z — are defeated by moving the hint: concentration is answered by vacuity (max-cut), and a small Z is answered by choosing a hint with more zeros. **What is missing is a proof that some hint always achieves β ≤ 1 − δ**, and that is the open step. It is strictly smaller than W9's residual, which required reconciling two different hints for two different case families; here there is one device and one quantity to bound.

## 6. Measurements (exhaustive over hints, sampled over templates)

For each template, **all 2^{n+2} hints were tried** and the best retained; hitting sets are **greedy**, hence upper bounds on |H| — the safe direction, since a smaller optimal H only increases U_free.

| family | n=3 (N=8) | n=4 (N=16) |
|---|---|---|
| spread bijective calls | β-count 0, free **0.75N** | β-count 0, free **0.75N** |
| all-identity (the trap) | β-count 0, free **1.00N** | β-count 0–1, free **0.94–1.00N** |
| concentrated (n+1 calls at one input, 1 elsewhere) | β-count 0, free **0.75–0.88N** | β-count 0, free **0.81–0.88N** |
| mixed half identity / half spread | β-count 0–1, free **0.75N** | β-count 1–2, free **0.81–0.88N** |

**Worst singleton fraction observed: 0.12, against a hypothesis needing only β ≤ 1 − δ.** The concentrated family was built specifically to stress the |Z| = 1 mechanism of §2 and did not stress it. **Sampled over templates (four families, two seeds, n ∈ {3,4}), so this supports the hypothesis of Theorem W10.2 being satisfiable; it does not prove it.**

## 7. NC⁰ glue — a map, not a proof (Flag S10, as registered)

With C′(x)_i = g_i(x, O(1) oracle bits), each coordinate reads a constant-size set of positions and is satisfied by forcing an O(1)-bit **pattern** rather than a single literal.

**Survives unchanged:** Lemma W9.0 — it needs only a fixed F₀ satisfying all clauses plus conditions (1) and (2), and never inspects the glue. **Full-value forcing** still makes (1) automatic. **Placement** is unchanged.

**Survives with work:** the hitting-set step becomes hitting over **pattern-sets** — for each x, the family of position-sets that a coordinate could be killed on — with the same sum-of-expectations budget, provided each coordinate's pattern-set lies inside one input.

**Needs a new idea:** coordinates whose pattern spans **several inputs**, e.g. g_i = XOR of one bit of C(u) and one bit of C(v). Then forcing constrains a **relation between inputs** rather than a value at one, so full-value forcing no longer decouples: two coordinates can demand incompatible relations, and condition (1) — which full values made free — can fail *across* inputs. **The all-ones trick specifically dies here**, since it relies on a coordinate being a bare projection, so that forcing a 1 falsifies y_i exactly when y_i = 0.

## 8. Kill tests

- **(i)** Definition 9 / Theorem 12 model throughout; no value queries.
- **(ii)** Determinism is in the statement of Theorem W10.2 and inherited by every corollary.
- **(iii)** No 10b candidate arose; §6 searched over all hints for all four families and found none.
- **(iv)** Every "small"/"large" quantified: β, α, r are defined as fractions and the bound is N(1−β)/4.
- **(v)** Consistency: N(1−β)/4 ≤ N always, and β = 1 (the trap at y = 0) correctly yields nothing.
- **(vi)** Exact vs sampled labelled in §6; greedy noted as an upper bound in the safe direction.
- **(vii)** The step that does not close is §5, stated as the open step and not dressed as a theorem.
- **Prior corrected in the same breath as the finding:** the α < 1/3 threshold, §0.

## Ceiling

Unchanged. **W10 proves nothing about P vs NP.** It reduces every projection template to one hitting-set quantity, closes all of W9's cases as corollaries of a single lemma, and leaves one hypothesis unproved. By Flag H7 none of it survives randomisation, and Korten's Problem 1 — arbitrary polynomial-time glue — is untouched; §7 says precisely which steps would transfer to NC⁰ and which would not.
