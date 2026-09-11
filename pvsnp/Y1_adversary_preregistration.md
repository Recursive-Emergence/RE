# Y1: self-reference at the adversary. Pre-registration

*Drafted 2026-09-11 on branch `y1-adversary`, on the author's go ("Draft Y1 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices on record apply: smallest case first; every new bound beside the record's own lemmas (R4, R5) **and beside the literature** before it is called new.*

## Ceiling (first)

Success gives one-way functions from NP ⊄ BPP, which is conditional. It does not give P ≠ NP unconditionally, and no unconditional route is known; the record shows why (Book's transfer; naming costs what it names).

## §0. The literature check (g1), done at drafting, as the reviewer asked

**The field has moved past errorless.** Two-sided error has been converted into a **promise on the instances**. Every statement below was read in the source's text this session unless it is marked secondary.

| source | verified statement | where |
|---|---|---|
| **Liu–Pass, ECCC TR23-103 (TCC'24)** | **Theorem 1.1.** For polynomial t(n) ≥ 2n, constant β, δ > 0, and n^δ ≤ s(n) < n − 1, the following are equivalent: OWF exist ⇔ MK^tP[s]\|Q^t_β ∉ ioBPP. Here Q^t_β = {x : K^t(x) − K(x) ≤ β·log K(x)} (small computational depth), and MK^tP[s] is the promise problem YES: K^t ≤ s, NO: K^t ≥ n − 1. | l.221–283 |
| same | **The key idea is the reviewer's mechanism.** If A fails on ≤ 3·2^n/n^{c′} instances, then "all those instances must have Kolmogorov complexity bounded by log(2^n/n^{c′}) + O(log n) (to index the instance among the list of elements on which A fails …, plus … the constant-size description of A) … the above argument is non-black box: we rely on the fact that we have a short description of the attacker A." For randomized A, the error set is taken as {x : A fails with probability ≥ 1/3}. | l.464–479 |
| same | "Solving [the holy grail] is equivalent to showing that our promise problem is NP complete (perhaps with a non-black box reduction). As far as we know, there are no barriers to this." | l.386–392 |
| **Liu–Pass, IACR ePrint 2025/2184** | Boundary hardness of MINK^poly characterizes OWF: for randomized K^t, and for plain K^t under E ⊄ ioSIZE[2^{o(n)}]. This builds on Liu–Pass CRYPTO'25. **Theorem 1.3:** under E ∉ ioSIZE[2^{εn}], MINK^poly ∉ BPP ⇔ MINK^poly ∉ AvgBPP (*errorless*). | abstract; l.196–240 |
| same | **Why errorless is easier, in their words:** "instances on which an errorless reduction fails are sparse and **explicitly identifiable** (since the heuristic needs to output ⊥). Thus, we can again use the language compression algorithm of [GS85] to compress them," which bounds their *K^t*. | l.364–370 |
| **Hirahara, ECCC TR23-037 (STOC'23)** | OWF exist ⇔ it is NP-hard to approximate distributional Kolmogorov complexity under randomized polynomial-time reductions *and* NP is hard in the worst case. The errorless/error-prone gap is closed *conditionally* by combining Nanashima's techniques with Hir18's non-black-box reductions. | abstract |
| Hirahara–Nanashima, "Learning in Pessiland via inductive inference" (FOCS'23) | A worst-case characterization of *infinitely-often* OWF, conditioned on a depth variant. **Secondary** (LP23 l.416–445); not read. | — |
| Liu–Pass CCC'22, footnote 2 | Errorless average-case hardness does not suffice. Already on record in R5. | R5 |

**What this does to the reviewer's (a)–(d):**
- **(a)–(b) are known.**
  - E_A is nameable, and its elements have *K* ≤ log|E_A| + |A| + O(log n). That is LP23's key idea.
  - The crux the reviewer named, that naming does not give deciding, is **exactly the gap between K and K^t**, i.e. computational depth.
  - LP25 l.364–370 states the deciding half: errorless failures are *identifiable*, so language compression bounds their K^t. Two-sided failures are not identifiable, so only their K is bounded.
  - The literature's answer is to **condition on low depth** (Q^t_β), where a K bound implies a K^t bound.
- **So the "fifth appearance of the tension" is already in the literature, with a name: computational depth.** The obstruction did not vanish. It moved into the promise, and the open step in every version is **NP-hardness of the promise-restricted problem**.

## §1. Y1 as posed, re-stated against §0, with the flags (mine, raised before any work)

**Flag S (the sign: which error hurts, and whether naming touches it).**
- In R5's steps (Hir18, re-checked there), S3 needs T = {A says "No", i.e. K^t ≥ r} to reject the NW image. The image consists of **YES instances** (K^t ≤ K^t(x) + d + O(log) < r).
- **The hurting error is A answering "No" on YES instances.**
- The double use of A's code bounds the K of the error strings. That excludes **NO-side** errors under the depth promise: a NO instance with K^t ≥ n − 1 and small K is deep.
- It does nothing on the **YES side**: a YES instance already has K ≤ K^t < r, so naming it via A costs no more than it already costs. Its depth can be 0, so the promise does not exclude it.
- **Expectation: the double use removes the harmless side and leaves R5's hurting side untouched.** Y1b at (c), with the named reason: "the hurting error sits where a short description is already free."
- To be checked: whether LP23's route avoids YES-side errors by a different mechanism, via LP20's OWF construction rather than Hir18's reconstruction. If it does, that mechanism, not the double use, is what defeats two-sided error, and the report says so.

**Flag K (the kill test, fixed now).**
- **The constant heuristic A ≡ "No"** on MINKT[r] under the uniform distribution. It has two-sided error ≤ 2^{r−n+1} and code length O(1), and E_A is exactly the YES set.
- Any reduction that "uses A's code twice" gets no information from this A. So it would be a worst-case algorithm on its own.
- Hence a two-sided-error reduction can exist only when the error bound 1/p is below the YES density, consistent with R5's "survives only for K^t(x) ≤ log p + O(1)".
- The reviewer's kill test (d), random answers on a 1/p fraction, is subsumed: for deterministic A, E_A is a fixed set named by A's code; for randomized A, LP23 uses the threshold set {Pr fail ≥ 1/3}, named the same way.

**Flag M (the model question (d); expected not to change the statement).** For randomized A, the error set is {x : Pr_r[A(x; r) wrong] ≥ 1/3}. It is nameable from A's code at the same cost (LP23 l.466–474), and deciding it still needs the truth. **Y1c is expected only if the Flag S check turns up a YES-side mechanism that depends on the model.**

## §2. The proposed retarget, Y1′: the frontier step (the reviewer rules whether Y1′ replaces Y1)

**Target.** Do the known NP-hardness reductions for MK^tP variants output instances inside LP23's promise Q^t_β, or inside LP25's boundary promise? Separately for YES outputs and for NO outputs. By LP23 l.386–392, a reduction landing inside the promise is the whole remaining step to OWF from NP ⊄ BPP. **The expectation is that none does, and the run names where each leaves the promise.**

**Flag D (depth of deterministic outputs; an elementary observation, to be written as a proof).**
- A deterministic reduction R, running in time below t, has K^t(R(φ)) ≤ |φ| + O(log n), so every output lies within |φ| + O(log n) of 0 in K^t.
- **NO outputs** need K^t ≥ n − 1, so they require |φ| ≥ n − O(log n): no length blow-up.
- Randomized reductions escape only if their NO outputs carry about n bits of randomness **and** remain non-deep, i.e. K(x) ≥ K^t(x) − β·log K(x).
- This is a condition on the reduction's randomness budget, to be checked per reduction. It is not a kill.

**Reductions to check** (texts to be fetched and read under g1; none is assumed):
- Liu–Pass CCC'22 (McK^tP[ζ], NP-hard under randomized many-one reductions; on record in R5);
- Hirahara FOCS'22 (NP-hardness of learning programs and partial MCSP);
- Ilango's MCSP-type reductions, if a stated K^t variant exists.

For each: the output distribution, its randomness budget, and the depth of YES and NO outputs, as far as the text determines it.

## Outcomes

**Y1 as posed (the reviewer's codes):**

| Code | Outcome |
|---|---|
| **Y1a** | The double use survives two-sided error in Hir18's reduction. Re-derive twice. |
| **Y1b** | It fails at a named step. Expected at (c) by Flag S: the hurting error is YES-side, where naming is free. |
| **Y1c** | The model changes the statement. |

**Y1′ (proposed):**

| Code | Outcome |
|---|---|
| **Y1′a** | A known reduction lands inside Q^t_β, or inside the boundary promise, on both sides. This would be OWF from NP ⊄ BPP; re-derive twice and assume an error first. |
| **Y1′b** | Each reduction leaves the promise at a named side, with the reason. |
| **Y1′c** | The texts do not determine the outputs' depth; record exactly what is missing. |

**Priors.**
- Reviewer (Y1 as posed): Y1b 70 / Y1c 20 / Y1a 10.
- Mine (Y1 as posed): **Y1b 80 / Y1c 15 / Y1a 5.** Its (a)–(b) are LP23's key idea, and Flag S expects the idea to miss R5's hurting side.
- Mine (Y1′): **Y1′b 60 / Y1′c 38 / Y1′a 2.** Y1′a would be the holy grail and would already be known if it were within reach of existing reductions.

## Scoring note (before any work)

The reviewer's mechanism was proposed as new. It is LP23's published key idea (l.464–479), and the reviewer's own g1 instruction ("if the field has already moved past errorless, Y1 starts from the current frontier") caught it before any work. This is recorded as a **premise note, not a miss**: the check ran first, as instructed.

## Ceiling (restated)

Y1 and Y1′ prove nothing about P vs NP. At best, Y1′ locates exactly where known NP-hardness reductions leave the promise that the OWF characterizations need.
