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
