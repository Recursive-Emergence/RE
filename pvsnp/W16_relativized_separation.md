# W16: a relativized separation of (D2) from (C₁). Pre-registration

*Drafted 2026-09-12 on branch `w16-relativized-separation`, on the reviewer's W16 specification, after its W15 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the work. §2 discloses a requirement the specification does not state and which, on my reading, is where the theorem is won or lost.**

## Ceiling (first), stated carefully because this is a barrier claim

A full 16a would say: **any proof of Ren–Williams Question 5.3 must be non-relativizing.** It would **not** show Q5.3 is false, would say nothing about P vs NP, and would not by itself be evidence that Q5.3 is hard — barriers constrain techniques, not truth. **And the Y7/Y8 lesson governs this round:** I once concluded "must be non-relativizing" from "the proof reads the code", conflating non-black-box with non-relativizing, put it on the page, and had to withdraw it. **The discipline that catches this is to ask first what *does* relativize** — which is §2(a), and it changes the round.

## §1. Refuted premises checked

Not reused: "odd cycles break the coupled device" (W11, mine); "differing σ break the product structure" (W12, mine); "uncapped forced inputs are the obstruction" (W13, mine); **"the isolation weight budget does not fit" (W15, mine — dissolved by per-level sharing, Lemma W15.0)**; and **"non-black-box implies non-relativizing" (Y7, mine — the error this round is most exposed to)**.

**Flag Z13 stands.** **New standing item: nothing from the closed black-box sub-line (W7–W14) transfers here** — that was a model with no hard string; this round's whole point is that the algorithm *has* one.

## §2. Disclosure: what I derived before pricing

**(a) THE REQUIREMENT THE PLAN OMITS, and it is decisive.** SU05's route **relativizes**: the PRG construction and the downward collapse (Cor 3.3) are black-box, so **relative to every oracle A, SVN hardness of E^{NP^A‖} implies Avoid ∈ FP^{NP^A}_tt** by Theorem 3.12. Hence the target oracle must give E^{NP^A} **plain-circuit hardness while denying it SVN hardness**. A random A₁ of the kind the plan proposes will, on any reasonable accounting, be hard against **both** plain and single-valued nondeterministic A-circuits — random functions are hard against everything — **so the plan's A₁ defeats its own conclusion.** **16a therefore requires an oracle separating plain-circuit hardness from SVN hardness for E^NP**, which is a substantial problem in itself and is precisely the gap DS26's black-box barrier (recorded in W5) says is hard to close.

**(b) How one round succeeds *with* isolation — stated so that what must fail is unambiguous.** Issue, in a single round, the queries "is there a preimage of weight exactly t?" for all t, **and** "is there a preimage of weight exactly t with bit i set?" for all (t, i). Read W₀ off the first family, then read the bits off the (W₀, i) answers. **One round, and uniqueness at weight W₀ is exactly what makes those answers consistent.** The weight range must be poly-size for this enumeration to be affordable, which is why nW = poly and why collisions are abundant.

**(c) A sharpening of the plan's pigeonhole.** The plan says the adversary arranges ties "under every weighting the algorithm derives". A pair tying under **all** weightings of a poly-size list need not exist. It does not have to: consistency is needed at **every node**, so it suffices to break weighting j at **its own node v_j** — different nodes for different weightings, which the adversary controls since it is building G. **This makes the plan's step work, and it should be stated that way.**

**(d) A constraint on the adversary that the plan does not draw.** Wilson's adversary defeats **adaptive** algorithms too (qw ≥ N regardless of rounds), so relative to his oracle (C₁) itself fails. Here (C₁) must **hold**: given a hard f, Korten's reduction succeeds on **every** G. **So the adversary may not make Avoid unsolvable — only non-adaptively unsolvable — and the single-valuedness failure is the only lever it is permitted.** Any step that looks like "the algorithm cannot find a solution" is disqualified on its face.

**(e) Not done:** the relativized circuit lower bound from a primary, and the three checks.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **16a** theorem proved with the three checks | 55 | **25** |
| **16b** a relativizing non-adaptive algorithm given a hard string (barrier fails; Q5.3 relativized is TRUE) | 10 | **15** |
| **16c** obstruction named | 35 | **60** |

**I am far below the reviewer on 16a, and §2(a) is the entire reason.** The specification's A₁ is a random oracle, and a random oracle plausibly supplies SVN hardness as well as plain hardness — at which point SU05 Theorem 3.12 relativized puts Avoid in FP^{NP^A}_tt and the separation collapses. **To get 16a one must first separate plain from SVN circuit hardness relative to an oracle**, which the plan neither does nor mentions. That is not a check on the construction; **it is a prerequisite the construction has not met**, and on the evidence of DS26 it is where the difficulty of this whole question has been sitting all along.

**Why I am slightly above on 16b.** If a random oracle does give SVN hardness, then relative to it the non-adaptive algorithm exists, which is 16b's shape for that oracle — though 16b as stated asks for the relativized Q5.3 to be true in general, which is stronger. 15, not higher.

## §4. Flags

- **Flag J16 — before any claim that a proof "must be non-relativizing", state what DOES relativize.** SU05's route does. This is the Y7 error's exact shape and the flag exists to catch it.
- **Flag K16 — the oracle must separate plain hardness from SVN hardness**, and the report must say explicitly whether the construction achieves that or assumes it. **If it assumes it, the outcome is 16c and the assumption is the obstruction.**
- **Flag L16 — the adversary is forbidden from making Avoid unsolvable** (§2d). Any argument whose effect is "no solution is findable" has proved the wrong theorem.
- **Flag Z13 (standing).**

## §5. Kill tests

- **(i)** Korten Definition 9's DNF model for the query bounds; determinism stated.
- **(ii)** The relativized circuit lower bound quoted **verbatim from a primary I fetch**, not from memory.
- **(iii)** The three checks the ruling names — "false" answers surviving completion; the completion not making L easy (state the length separation); Korten's adaptive algorithm genuinely succeeding relative to the final A — each answered explicitly or recorded as not done.
- **(iv)** Every count with its comparison bound; the quantitative form (one round vs O(n + log T) rounds) stated, and the r-round question answered by counting or declared open.
- **(v)** Consistency with W15: the isolation test is coNP-type (T′) and SU05's is P^{NP‖}; **any claim here that plain hardness suffices would contradict W15 and is therefore wrong.**
- **(vi)** If the plain-vs-SVN separation is not achieved, **report 16c with that as the named obstruction** — do not present the rest of the construction as if it were the theorem.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
