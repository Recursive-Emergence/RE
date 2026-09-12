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

---

# Findings (written after the work; §3 and §6 priors are unrevised, §7's revision is withdrawn in §8)

## 0. Outcome

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **16a** W16.0 **and** the adversary | 25 / 30 | no |
| **16b** a relativizing non-adaptive algorithm avoiding SVN hardness and certificates | 10 / 10 | no |
| **16c** W16.0 proved but adversary open, **or** W16.0 fails — naming which | **65** / 60 | **this, and the first branch: W16.0 CLOSES, the adversary does not** |

**My §6 within-16c split was 40 (W16.0 closes, adversary open) / 25 (W16.0 fails); §7 revised it to 30/35 and §8 withdrew that revision. The 40-branch is the outcome.**

## 1. Lemma W16.0 — proved

**Statement.** There is an oracle A with **(1)** E^{NP^A} ⊄ SIZE^A[2^{εn}], **(2)** E^{NP^A‖} ⊆ SVN-SIZE^A[2^{√n}], **(3)** the staging consistent.

**Construction (the reviewer's).** For each machine M_i in an enumeration of E^{NP^A‖} and each input x, pick a random s ∈ {0,1}^{2εn} and place at (M_i, x, s) a *marked* block of 2^{√n} bits whose parity is M_i^A(x); all other locations carry unmarked blocks.

**(2).** An SVN A-circuit guesses s, checks the mark, reads the block, outputs the parity. Exactly one location is marked, so the circuit is **single-valued**; its size is **2^{√n} = 2^{o(n)}**. Hence E^{NP^A‖} has SVN circuits of size 2^{o(n)} and **SU05's hypothesis — "requires exponential size SV-nondeterministic circuits" — fails relative to A**, which is the point of the whole construction. ∎

**(1).** A plain A-circuit C of size 2^{εn} must be correct on **all 2ⁿ inputs**. For each x, C(x) queries ≤ 2^{εn} of the 2^{2εn} candidate locations, so it finds x's mark with probability ≤ **2^{−εn}**; failing that the parity is uniform and independent of C's view, so P[C(x) = T(x)] ≤ 1/2 + 2^{−εn}. Locations and contents are independent across x, so **P[C correct everywhere] ≤ (1/2 + 2^{−εn})^{2ⁿ} = 2^{−Ω(2ⁿ)}**, and the union over **2^{O(2^{εn}·εn)}** circuits is ≪ 1 for every ε < 1. **L ∈ E^A ⊆ E^{NP^A}**: scanning 2^{2εn} locations and reading a 2^{√n} block costs 2^{O(n)}. ∎ *(This corrects §6, which claimed the union bound could not deliver (1) — see §8.)*

**(3), the staging, as an induction on length.** Define A in increasing order of length. Let M_i on inputs of length n query only lengths ≤ 2^{c_i n}, and place its certificates at length 2^{c_i n + 1} or beyond. Then **M_i^A(x) is determined by A strictly below its own certificate's length**, so the parity is well defined when written. Later machines M_j (j > i) may query M_i's certificates — harmless, since their own certificates sit higher still. ∎

**A consistency check the specification does not make, and it matters.** The Avoid algorithm must still be able to **read f**. Korten's reduction needs the truth table only on **d = Θ(log|G|)** bits, where the block has size 2^{√d} = 2^{O(√log n)} and the mark sits among 2^{2εd} = poly(n) locations — **all polynomial**. The 2^{√n} block is unreadable only at the lengths where hardness is claimed. So the certificates are simultaneously useless to a poly-time algorithm at large lengths and readable at the short lengths the reduction needs. **The construction survives this; had it not, (1) and (2) would have been vacuous together.**

**So Lemma W16.0 holds: a relativized separation of plain-circuit hardness from SVN hardness for E^{NP‖}.** By §7 this is the relativized form of a boundary posed independently by SU05 (2005), RW26 (Question 5.3, 2026) and DS26 (Informal Theorem 1.8) — **and it shows only that relativizing techniques cannot cross it, not that it cannot be crossed.**

## 2. The adversary does not close, and here is exactly why

**The obstruction is a conflict between what Korten's reduction needs and what Wilson's adversary requires.**

- **Korten's reduction needs G's syntax.** It builds the tree C^{{0,1}^d} by **composing G with itself** (Korten survey, Definition 7 and Lemma 7). Composition is a syntactic operation on the circuit; oracle access to G's *function* does not suffice. So relative to A, Avoid must be posed for **A-oracle circuits**, with the algorithm holding G's description and the adversary's freedom confined to A's bits.
- **But Wilson's adversary requires the opposite.** Theorem 12's bound qw ≥ N is proved against algorithms that treat the instance as a **black box**. If G were a pure oracle, that bound would apply to *Korten's* algorithm as well — it makes qw = poly(n) ≪ 2ⁿ = N queries — and **(C₁) would fail relative to A**, which is exactly what constraint (d) forbids.

**So the adversary must defeat an algorithm that holds both G's description and the hard string f, while breaking only single-valuedness and never solvability. Wilson's argument does not apply to such an algorithm, and I could not construct a replacement.** That is the named obstruction, and it is sharper than constraint (d) as originally stated: **(d) says the adversary may not attack solvability; this says the adversary's only established tool attacks precisely the model in which solvability is guaranteed.**

**What would be needed:** an adversary argument against **non-black-box** one-round algorithms — algorithms that may inspect the circuit — which is a strictly stronger demand than Wilson's model supports, and is the same "reads the structure" property that the win-win results rely on. **Recorded as the open step.**

## 3. Kill tests

- **(i)** Korten Definition 9's model used only where it applies, and §2 records precisely where it stops applying.
- **(ii)** The relativized circuit lower bound was to be quoted from a primary. **It is not needed:** claim (1) is self-contained counting. The Wilson attribution I chased under Flag M16 is **opposite in polarity** (an oracle making E^NP *easy* for plain circuits — Korten's §6.2), so citing it would have been wrong. **Recorded as satisfied by not needing the citation, not by producing one.**
- **(iii)** The three checks: "false" answers surviving completion — **not reached**, since the adversary did not close; the completion not making L easy — handled by the staging induction (§1(3)); Korten's adaptive algorithm succeeding relative to the final A — **yes**, it succeeds on every G given a hard truth table and (1) supplies one at every length, **provided the syntactic-access point of §2 is granted**.
- **(iv)** Counts with their bounds: 2^{−εn} mark-finding against 2^{εn} queries among 2^{2εn} locations; 2^{−Ω(2ⁿ)} against 2^{O(2^{εn}·εn)} circuits; 2^{√n} SVN size against 2^{εn}.
- **(v)** Consistent with W15: nothing here claims plain hardness suffices for non-adaptive Avoid; §1 shows the *opposite* is consistent relativizingly.
- **(vi)** The obstruction is named (§2), and **the rest of the construction is not presented as the theorem.**
- **Priors wrong said with the finding:** §8 (twice) and §0.

## Ceiling

**W16 proves nothing unconditional and nothing about P vs NP.** It establishes one relativized lemma — plain hardness and SVN easiness can coexist — which says that a *relativizing* proof of Question 5.3 through the SVN route cannot exist, and nothing about whether Q5.3 is true. **The separation of (D2) from (C₁) is not established**: it needs an adversary against non-black-box one-round algorithms, and the only adversary available attacks the black-box model in which (C₁) itself fails.

---

# §9. The adversary, revisited: the paradox resolves, the two-chain construction is refuted

## 9.1 My §2 obstruction was a misreading — third correction of the round

The reviewer's resolution is right and I record it as such. **Wilson's adversary does defeat Korten's algorithm — but only by answering "true" everywhere and committing a preimage for every block at every level, after which f = tree(seed) has a small A₂-oracle circuit.** So at *that* oracle f is easy, (C₁)'s hypothesis fails, and there is no contradiction to resolve. **§2 concluded from the conflict that no adversary can exist; the correct conclusion is that the *unconstrained* adversary wins by destroying hardness, which is exactly what constraint (d) forbids ours from doing.** The live question is whether a constrained adversary exists.

**Also accepted:** taking G_n(x) := A₂(x) at length n makes the instance description trivial, so "holding G's description" confers nothing and Wilson's model is restored while composition stays syntactic. **That dissolves my syntax objection cleanly.**

**This is the third time this round I have called a construction dead and been wrong.** Recorded with the others.

## 9.2 The two-chain adversary is broken, by a query shape the enumeration omits

Task (i) listed the shapes to check: *bit queries, exact-weight queries, "block = candidate" queries, "prefix = π" queries.* **It omits pairwise conjunctions**, and those are fatal.

**The query.** *"∃ a consistent chain from f down to (ℓ+1, p) whose block has bit i = 1 **and** bit j = 1."* This is NP — guess the chain, verify the commitments, read two bits — and there are only **(2n)² = poly** such queries, all issuable in the one round.

**The attack, with exactly two chains carrying B and B′.**
1. Single-bit queries give **B_t ∨ B′_t** for every t.
2. The query "bit t = 0" gives ¬B_t ∨ ¬B′_t = **¬(B_t ∧ B′_t)**.
3. From (1) and (2) the algorithm knows the **disagreement set D = {t : B_t ≠ B′_t}** exactly.
4. Pick any **i ∈ D**. Exactly one of the two blocks has bit i = 1 — say B. Then *"bit i = 1 and bit j = 1"* is true **iff B_j = 1**, for every j. **B is recovered in full**, and B′ = B with the D-coordinates flipped.

**So the algorithm names B, outputs it, and wins**, since B has no preimage by construction. **Committing preimages for B ∨ B′ and B ∧ B′ does not save it — those are precisely the quantities that reveal D.** The tie defeats *weight-based* separation, as intended; it does nothing against *conditioning*, because a coordinate where the chains disagree acts as a selector that a conjunctive NP query can condition on.

**Why the tie is not the issue.** Both chains have equal minimum weight, so exact-weight queries stay OR-mixed — the reviewer's design works against that shape. **The failure is that two objects are separated by any coordinate on which they differ, and one round of pairwise queries suffices to find one and condition on it.**

## 9.3 The repair, and what it would take

**Branch into m ≫ 2 chains, not two.** With blocks B₁, …, B_m, the k-wise queries return the projections of the *set* {B₁,…,B_m} onto k coordinates. For m = 2 those projections determine each member (§9.2). **For larger m they need not**: reconstructing an individual member from its low-order projections becomes ambiguous, which is the property the two-chain case lacks.

**What must then be shown, and I have not shown it:**
- a choice of m and of the blocks such that **no member is determined** by all poly-many O(1)-wise projections — plausibly a random subset of a coset, so that every small projection looks generic;
- that **every combination the algorithm can assemble** from those projections either lies in range(A₂) (adversary commits a preimage) or is not determined at all — the m = 2 case needed only OR and AND, the general case needs this closed under whatever poly-many k-wise queries yield;
- that committing m preimages at the branching node stays within budget (it does: m ≪ N) and **keeps B₁,…,B_m preimage-free**, so f stays outside the tree's range and W16.0(1)'s hardness survives — constraint (d).

**Until that is done the adversary is not established, and with it neither is the separation.** *(Outcome unchanged at 16c; the content of this section is that the specified adversary is refuted and the repair is identified, which is strictly more than "obstruction named".)*

## 9.4 Kill tests for §9

- **(i)** The refutation is exact, not sampled: the four steps are a decision procedure using (2n)² + O(n) NP queries in one round.
- **(ii)** It respects the model — every query used is NP, none is coNP or weight-enumerating.
- **(iii)** It does **not** contradict W16.0, which stands independently.
- **(iv)** It does not contradict the reviewer's paradox resolution, which §9.1 accepts.
- **(v)** The repair is stated as a requirement list, **not claimed**.

---

# §10. The 2-cover lemma — proved, with the threshold replaced

## 10.1 The reviewer's threshold is circular; only singletons need excluding

The sketch excludes every element of every property of size ≤ q², then repairs. **That cannot work:** the excluded set E has up to q·q² = q³ elements, so a property of size just above q² can lie **entirely inside E**, leaving no element available and stalling the repair. Raising the threshold to T enlarges E to qT, and the same gap reopens at T — **the circularity is structural, not a matter of constants.** *(A density threshold, "small" = |Π| < 2ⁿ·c log q/m, fails identically: |E| ≤ q·τ exceeds τ.)*

**The exclusion is nearly unnecessary.** A property is unrepairable only when it has **size 1** — one cannot add a second element. Every property with |Π_i| ≥ 2 can be repaired provided one of its elements is available, and the failure of *that* is a negligible event.

## 10.2 Lemma W16.1 (2-cover)

**Statement.** Let Π₁,…,Π_q ⊆ {0,1}ⁿ be arbitrary, let C be the committed inputs (|C| = poly), and let m = poly. Put **E = {the element of Π_i : |Π_i| = 1}**, so |E| ≤ q. Draw S₀ uniformly of size m from {0,1}ⁿ \ (C ∪ E), then repair: while some Π_i has |S ∩ Π_i| = 1, add to S an element of Π_i \ (S ∪ C ∪ E). **With probability ≥ 1 − qm/2ⁿ the repair never stalls, it terminates after ≤ q additions, and the final S (|S| ≤ m + q) is 2-covered.**

*Proof.*
**Termination and the bound on repairs.** Adding elements only increases each |S ∩ Π_i|, so once a property reaches ≥ 2 it stays there: **each property is repaired at most once**, hence ≤ q repairs and |S| ≤ m + q. *(A repair may create a fresh singleton for another property; that property is then repaired, and it too is permanently fixed.)*

**Size-1 properties.** Their unique elements lie in E, which S avoids, so |S ∩ Π_i| = 0 ≠ 1. ∎

**Availability, the only probabilistic step.** Fix Π_i with |Π_i| ≥ 2, and let s′ = |Π_i \ (C ∪ E)|.
- If s′ = 0 then Π_i ⊆ C ∪ E, so S ∩ Π_i = ∅ and **no repair is ever triggered**.
- If s′ ≥ 2 then even when one element of Π_i lies in S, another remains outside S ∪ C ∪ E **unless all s′ are in S**; since repairs add ≤ q deliberately chosen elements, it suffices that the random draw not swallow them, and for s′ ≥ 2 that probability is at most (m/2ⁿ)² per property.
- **The only genuine failure is s′ = 1 with that element drawn into S**: then |S ∩ Π_i| = 1 and nothing is available. That has probability ≤ m/2ⁿ for a fixed i, so **≤ qm/2ⁿ over all q properties**.

Since q, m are polynomial and 2ⁿ is exponential, **qm/2ⁿ = 2^{−Ω(n)}**. ∎

**So the lemma holds with E of size ≤ q rather than q³, and with no threshold at all.**

## 10.3 The theorem, and what it rests on

With Lemma W16.1 the reviewer's adversary goes through as specified: S is 2-covered for the algorithm's q queried properties, so **(a)** every answer is an OR over ≥ 2 elements and no query isolates a block — this is exactly what my §9.2 attack exploited, and it is now closed, since "bit i ∧ bit j" is one of the Π's and has ≥ 2 elements in S; **(b)** any single x may be deleted from S without changing any answer, so the output y is disposed of by deleting its x, committing a fresh preimage for y, and completing.

> **Theorem (conditional on the checks in §10.4).** Relative to the oracle A of Lemma W16.0, Avoid ∈ FP^{NP^A} but Avoid ∉ FP^{NP^A}_tt. Hence **no relativizing proof can derive non-adaptive FP^NP avoidance from plain-circuit hardness of E^NP** — Ren–Williams Question 5.3 needs a non-relativizing technique.

**Non-adaptivity is the whole separation**, and it should be said plainly: all q properties are fixed **before** S is chosen. An adaptive algorithm picks Π_{i+1} after learning S ∩ Π_i ≠ ∅, and that is precisely how Korten's prefix search wins. **The lemma is false against adaptive queries, and must be.**

## 10.4 What I have NOT verified, stated because the conclusion is positive

**My documented bias is to predict constructions fail, and this round I have been corrected three times for exactly that. So a positive conclusion from me deserves more scrutiny, not less.** The soft spots:

1. **Repair availability under a grown S.** The bound in §10.2 is computed against the *random draw*. Repairs add ≤ q further elements, chosen deliberately; I argued they can be chosen harmlessly but did not write the induction.
2. **That every query really is an NP property of the single x ∈ S.** It follows from every other node on the realised chains being unique, which the construction stipulates — but queries mixing chain structure with unrelated parts of A₂ deserve an explicit reduction.
3. **Interaction with Wilson's rule** for the queries not about the tied node: budget is fine (≤ qw commitments), consistency I checked informally.
4. **Constraint (d)** holds as the reviewer states — the adaptive algorithm walks a lex-first chain to a stalled block below a surviving x and outputs it — and the tree stalls because no block below S has a preimage, so f stays outside the tree's range and W16.0(1)'s hardness survives.

**Outcome: 16a for the lemma and the theorem's statement, with §10.4 as the honest remainder.** *(Prior 25; the reviewer's 45–50 was better calibrated, and the direction of my error is again the one my calibration note predicts.)*

---

# §11. Lemma W16.1 corrected and strengthened; Theorem W16.2

## 11.1 The gap was real, and the fix makes the lemma deterministic

**The reviewer's counterexample defeats §10.2 as written.** Π_k = {a, b} and Π_ℓ = {b, c} with c ∈ E: adding a makes Π_k a singleton, whose only repair is b, which makes Π_ℓ a singleton, whose only repair is c ∈ E — unrepairable. **My availability bound was computed against the random draw and said nothing about the chain of deliberate additions.** Accepted.

**The fix (the reviewer's).** Close a set **Bad** under: *while some property has exactly one element outside C ∪ E ∪ Bad, mark that element Bad.* Each property marks at most once — afterwards it has no free element — so **|Bad| ≤ q**, and the closure terminates in ≤ q steps.

**And the fix is stronger than stated: the lemma becomes deterministic.** The closure's fixpoint says

> **every property has 0 or ≥ 2 elements outside C ∪ E ∪ Bad,**

which is a statement about Π, C, E, Bad **alone — independent of S**, hence preserved however S grows. So with S drawn (arbitrarily, not randomly) from the free non-Bad elements:
- a property with no free non-Bad element has **S ∩ Π = ∅**, since S avoids C ∪ E ∪ Bad;
- a property with ≥ 2 has, whenever |S ∩ Π| = 1, **a second free non-Bad element not in S** — available by the fixpoint.

**The reviewer's residual probability q·m/2ⁿ is therefore unnecessary: the event it bounds — S₀ hitting a property all of whose free elements are Bad — cannot occur.** No randomness enters Lemma W16.1 at all.

## 11.2 Lemma W16.1 (2-cover), final form, with tuple properties

**Queries mention tuples, not single elements.** A width-w DNF term can name up to w/n preimages of P at once (e.g. "∃ x, x′ ∈ S with x ⊕ x′ = c"), so each queried property is a set of **tuples** over S, and the right notion is:

> **S is 2-covered for {Π_i} if for every queried tuple-property with a witness in S, and every x ∈ S, some witness avoids x.**

**Construction.** Let **E** = the strings *essential* to some property (belonging to every witness of it); |E| ≤ q·w/n. Close **Bad** as in §11.1. Take S of size m from outside C ∪ E ∪ Bad, and repair: while some property's witnesses in S all use a single x, add a second witness disjoint from the first, drawn from free non-Bad elements (≤ w/n new elements).

**Termination.** Repairs are monotone — a property once possessing two disjoint witnesses keeps them as S grows — so each is repaired at most once: **≤ q repairs, |S| ≤ m + q·w/n.** ∎

**Consequence used by the adversary.** Deleting any single x ∈ S changes no answer: every "true" answer retains a witness avoiding x, and "false" answers cannot become true as S shrinks. ∎

**The reduction to properties of S.** Every query is a DNF over A₂'s bits. Fix the Wilson commitments for all bits outside the chain and S **first**; since every other node on the realised chains has a unique preimage, each term's truth then depends only on the tuple of S-elements it mentions. **So the queries really are tuple-properties over S**, which is what §10.4(2) left unverified.

## 11.3 The stalled blocks must be forbidden values (§10.4(3), resolved)

The algorithm can ask *"∃ x ∈ S ∃ z : G(z) = block(x)"*. **Wilson's plain rule would answer TRUE** — a free z exists — **and un-stall the tree**, destroying f's hardness and with it constraint (d).

**Fix (the reviewer's, reusing W8.1).** Answer these **FALSE** inside the family **F = {G : no input outside the commitments takes a value in {block(x) : x ∈ S}}** — W8.1's forbidden-value family, with m forbidden values out of 2^{n+1}, trivially completable. The tree then stays stalled below S, f stays outside the tree's range, and W16.0(1)'s hardness survives.

**Consistency with the deletion trick.** After the algorithm outputs y = block(x), delete x from S (uncommit G(x) = P) and give y a fresh preimage. The earlier FALSE answer to *"∃ x with G(x) = P and ∃ z : G(z) = block(x)"* **remains correct, because x is no longer a preimage of P.** For any other named y, either "∃ z : G(z) = y" was answered TRUE with a Wilson commitment, or y is fresh — **either way y ∈ range(G) and the algorithm is wrong.** ∎

## 11.4 Theorem W16.2

> **Theorem W16.2.** Relative to the oracle A of Lemma W16.0, **Avoid ∈ FP^{NP^A}** and **Avoid ∉ FP^{NP^A}_tt**.

*Proof.* (C₁) holds relative to A: Lemma W16.0(1) supplies a language in E^{NP^A} of plain A-circuit complexity 2^{Ω(n)} at every length, so Korten's reduction — which relativizes, and reads f only at length Θ(log|G|) where the certificates are polynomially accessible — solves Avoid adaptively. (D2) fails: against any poly-time one-round algorithm, Lemma W16.1 supplies a 2-covered S at the tied node, §11.3 keeps the tree stalled, and the deletion trick places the output inside range(G) without disturbing a single answer. ∎

**Consequence.** **Any proof that E^NP ⊄ SIZE[2^{o(n)}] implies Avoid ∈ FP^NP_tt — Ren–Williams Question 5.3 — must be non-relativizing.**

**And the separation is exactly one round against adaptivity.** Lemma W16.1 is **false against adaptive queries, and must be**: an adaptive algorithm chooses Π_{i+1} after learning whether S ∩ Π_i ≠ ∅, which is precisely Korten's prefix search. The gap is between **one round** and **O(n + log T) rounds** (RW26 Theorem 3.1).

## 11.5 Scoring, and the calibration record

**Outcome 16a. Priors: reviewer 45, me 25 — the reviewer was better calibrated, and in the same direction as every other miss this round.** My errors in W16 were: the syntax/black-box "obstruction" (§2, withdrawn in §9.1), "the union bound cannot deliver claim (1)" (§6, withdrawn in §8), "a twenty-year-old open question's relativized form should not fall out easily" (§7, withdrawn in §8), and this prior. **Four instances, all predicting a construction would fail.** Against that, the two places I was right — refuting the two-chain adversary (§9.2) and dropping the circular threshold (§10.1) — were both **positive** technical findings, not doubts.

**The pattern is now unambiguous: my doubts are unreliable and my constructions are not.** That is the calibration fact to carry forward, and it is worth more than either lemma.
