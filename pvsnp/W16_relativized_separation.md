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

---

## §6. AMENDMENT — revised outcome codes and priors (committed before the work)

**The reviewer accepted §2(a) and restated the round.** It verified independently that L(x) = ∃y A₁(x,y) over a random sparse A₁ is hard for SVN A-circuits as well as plain ones — *"on x ∉ L an SVN circuit needs a 0-path, and a 0-path that queries ≤ s positions cannot exclude a witness among the 2ⁿ − s unqueried ones, so flipping one keeps the path and breaks single-valuedness"* — so the original oracle made the separation **false**, and **Flag J16 did its job**. My §2(b), (c), (d) are adopted.

**The outcome codes have changed materially, so my priors are restated against the new ones.** The old codes asked for "the theorem with three checks"; the new ones put a prerequisite lemma first:

> **Lemma W16.0.** There is an oracle A with (1) E^{NP^A} ⊄ SIZE^A[2^{εn}], (2) E^{NP^A‖} ⊆ SVN-SIZE^A[2^{√n}], (3) staging consistent.

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **16a** W16.0 proved **and** the one-round adversary closed under (d) | 30 | **25** |
| **16b** a relativizing non-adaptive algorithm avoiding both SVN hardness and certificates | 10 | **10** |
| **16c** W16.0 proved but the adversary does not close, **or** W16.0 itself fails — naming which | 60 | **65** |

**Within 16c I split further, so the outcome is falsifiable rather than a catch-all: 40 that W16.0 closes and the adversary stays open; 25 that W16.0 itself does not close this round.**

**Why 16a stays low, and it is not the adversary.** Claim (2) is clean: exactly one marked location makes guess-and-verify **single-valued**, at size 2^{√n} = 2^{o(n)}, so SU05's hypothesis fails relative to A. **Claim (1) is the hard one.** The certificate at (M_i, x, s) encodes M_i^A(x) — the hard language's *own* bits — so plain-circuit hardness requires **every** plain A-circuit of size 2^{εn} to miss the mark. **A union bound cannot deliver that:** there are 2^{O(2^{εn}·εn)} circuits of that size against a mark hidden among only 2^{2εn} locations, so the per-circuit miss probability 1 − 2^{−εn} is worthless summed over them. It needs a **staged diagonalisation** in which the hard truth table and the certificate placements are chosen together, circuit by circuit, with each stage's reservations respected by later ones. **That is the step I expect to consume the round.**

**Flag M16 (new).** Before attempting the diagonalisation, **check whether Lemma W16.0 is already known.** A relativized separation of plain from nondeterministic/single-valued circuit hardness is the kind of statement Wilson's *Relativized circuit complexity* (FOCS 1985 — already the source of Theorem 12 in this line) may contain outright. **If it is known, saying so is worth more than reproving it**, and the round's content becomes the adversary.

**Flag N16 (new).** The certificates about G itself — "bits of its lexicographically first non-range string" — are **determined by G**, which the adversary is simultaneously building against the one-round algorithm. **The staging must therefore be checked for circularity**: G's certificates must lie beyond polynomial reach *and* be consistent with the adversary's later choices. If that circularity cannot be broken, it is a 16c obstruction distinct from claim (1)'s.

## §7. Flag M16 discharged, and a prior-art finding that reframes W16.0 (recorded before the diagonalisation)

**M16 resolved, negatively, and my guess was wrong.** Wilson is a single paper — *Relativized Circuit Complexity*, JCSS 31(2):169–181 (1985), preliminary version FOCS 1983:329–334 (dblp; this reconciles Korten's FOCS 1983 citation with the JCSS 1985 hit, which I had briefly taken for two different works). **But the polarity is wrong for us.** Korten attributes to it *"an oracle relative to which E^NP ∈ P/poly"* — an oracle making E^NP **easy** for plain circuits, which is how Theorem 12's black-box bound is obtained. **W16.0 needs the opposite: E^NP hard for plain circuits and easy for SVN ones.** Wilson is not the source, and **no relativized plain-versus-SVN separation appears in either search or anywhere in this line's corpus.**

**The finding that reframes the round. SU05's own open-problems section sits exactly on this boundary** (verbatim):

> *"One can ask how far this 'weakening' of hardness assumptions can go. For example we do not know whether the existence of relative error approximators, or conditional discrepancy set generators, imply the nondeterministic hardness assumption that we have used to construct them in this paper. **The standard argument that shows that 'pseudorandomness entails hardness' only gives hardness for deterministic circuits. Is it possible to construct these objects using a weaker hardness assumption?** Constructing them from hardness for deterministic circuits would have some interesting consequences, like placing approximate counting in ZPP^NP unconditionally."*

**So the plain-versus-SVN gap is not an artefact of the W16 construction. It is Shaltiel–Umans' own open question from 2005, it is the same gap Ren–Williams pose as Question 5.3 in 2026, and DS26's Informal Theorem 1.8 says black-box techniques cannot cross it.** Three independent sources, twenty years apart, locating the identical boundary.

**Consequence for this round, stated before attempting anything.** Lemma W16.0 asks for a *relativized* separation of exactly that boundary. That is not a lemma one expects to fall out of a staged diagonalisation written in a single round — **and if it did fall out easily, the right response would be suspicion, not celebration**, since it would be a twenty-year-old open question's relativized form settled in passing. **I am therefore lowering my own expectation further: within 16c, I now put the split at 30 (W16.0 closes, adversary open) / 35 (W16.0 does not close this round), against the 40/25 registered in §6.** *(Recorded as a revision with its reason, before the work, not after.)*

**What would still be worth having even so:** the *statement* of W16.0 as the precise relativized form of SU05's open question, with the certificate construction as a candidate and its diagonalisation obstacle named. That is a 16c deliverable of real value — it says what a barrier for Q5.3 would have to prove, and why the obvious oracle does not supply it.

## §8. Correction to §6, before the findings: the union bound DOES deliver claim (1)

**I registered in §6 that claim (1) could not be had by a union bound. That is wrong**, and the error is precise: I compared the circuit count against a **single input's** mark-finding probability.

**The correct accounting.** A plain A-circuit C of size 2^{εn} must be correct on **all 2ⁿ inputs**. Fix x. C(x) queries at most 2^{εn} of the 2^{2εn} candidate certificate locations, so

  **P[C(x) finds x's mark] ≤ 2^{εn}/2^{2εn} = 2^{−εn}.**

Failing that, the block's parity is uniform and independent of C's view, so **P[C(x) = T(x)] ≤ 1/2 + 2^{−εn}**. Certificate locations and contents are drawn independently for distinct x, and C is a fixed circuit, so these events are independent across inputs:

  **P[C correct on every x] ≤ (1/2 + 2^{−εn})^{2ⁿ} = 2^{−Ω(2ⁿ)}.**

Against the **2^{O(2^{εn}·εn)}** circuits of that size, the union bound gives 2^{O(2^{εn}·εn)}·2^{−Ω(2ⁿ)} ≪ 1 **for every ε < 1**. **Claim (1) holds, with no staged diagonalisation.** *(L ∈ E^A ⊆ E^{NP^A}: scanning 2^{2εn} locations and reading a 2^{√n} block is 2^{O(n)} time. The certificates for other inputs and machines encode other values and are independent, so they do not help.)*

**And my §7 pessimism was a second error, of inference rather than arithmetic.** I reasoned that because the plain-vs-SVN boundary is a twenty-year-old open question, its relativized form should not fall out easily. **That does not follow:** a relativized separation shows only that *relativizing techniques* cannot settle the question — it does not settle it. W16.0 being reachable is fully consistent with SU05's question standing open since 2005. **The reframing in §7 stands; the revised split I drew from it (30/35) does not, and I withdraw it.**

**Two self-corrections in one round, both in the same direction — the construction is better than I claimed.** Together with the four cross-input-coupling misses of W9–W13, **my errors are not randomly distributed: they cluster on predicting that a construction will fail.** That is a calibration fact about me, not about the constructions, and it belongs on the record next to the results.
