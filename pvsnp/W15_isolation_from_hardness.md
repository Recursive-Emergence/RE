# W15: uniqueness, isolation, and the non-adaptive door. Pre-registration

*Drafted 2026-09-12 on branch `w15-isolation-from-hardness`, on the reviewer's W15 specification, after its W14 ruling closed the black-box sub-line. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the work. §2 discloses what I already derived, including a counting problem in Q3 that arises before Q3's stated question does.**

## Ceiling (first)

The target is **(D2)**: Ren–Williams **Question 5.3** — the weakest circuit lower bound implying Avoid ∈ FP^NP_tt. **Even the best outcome (15a) would be conditional**: a theorem of the form "E^NP ⊄ SIZE[2^{o(n)}] ⇒ Avoid ∈ FP^NP_tt", which answers an open question in the literature but proves nothing unconditional and nothing about P vs NP. W5 established that (D1)-type statements are **at least as strong as the door**, not weaker; the same caution applies here. **The realistic outcome is a reduction of (D2) to a precisely stated compressibility question, which is 15b.**

## §1. Refuted premises checked

Not reused: "α < 1/3" (W10, mine); "Z(x) uniform means W10.3 transfers" (W11, mine); "odd cycles break the coupled device" (W11, mine); "differing σ break the product structure" (W12, mine); "uncapped forced inputs are the obstruction" (W13, mine). **Four of those are one bias — predicting cross-input coupling is harder than it is — and Flag Z13 stays standing.**

**Carried from the closed sub-line, as principles rather than results:** *invariant maintainability, not locality, is the lever*; *high multiplicity helps whoever gets to choose*; *and a bound proved in a weaker query model is not a bound.* **The last one applies directly here:** this round is about a real algorithm in FP^NP_tt, not a black-box adversary, so **none of W7–W14's bounds transfer to it** and I will not cite them as evidence.

## §2. Disclosure: what I derived before pricing

**(a) Q1's lemma looks clean, and it trades a parameter that RW26 track.** With unique preimages the lex-smallest search disappears — that is exactly W6's *search-to-decision* term, the n rounds per stage. The chain-existence question ("is there a consistent chain of preimages from f down to block (ℓ,j), and is bit i of it 1?") is a **single NP query**, and uniqueness makes the answers across all (ℓ, j, i) mutually consistent, so **one parallel round** suffices. **But the witness is the entire subtree of preimages above the block — O(T) bits, against RW26 Theorem 3.1's witness length n.** For FP^NP_tt only non-adaptivity matters, so this is harmless for the target; **RW26's class is parameterised by rounds AND length, so the trade must be stated, not elided.** Query count ≈ Σ_ℓ 2^{ℓ−1}·2n = O(T).

**(b) Q3 has a counting problem BEFORE its stated question.** Isolation over {0,1}ⁿ needs weights of **O(n log n)** bits per node (n weights of O(log n) bits). The Jeřábek–Korten tree has **≈ T/n** nodes. So the weights consume **≈ T log n bits — strictly more than |f| = T.** Deriving all weights from f's bits therefore **overruns the budget by a log factor**, and reusing weights across nodes correlates the isolation failures, which is precisely what the win-win cannot tolerate. **So "does an isolation failure compress f?" is not yet well posed; the budget question comes first.** I register this now because it is the kind of step I have previously priced without checking.

**(c) What I have not done:** Q2's verbatim pinning of the derandomisation predicate, and the Korten–Santhanam oracle-access pattern.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **15a** Q1 proved **and** Q3 gives plain-circuit compressibility (answers Q5.3) | 10 | **8** |
| **15b** Q1 proved; Q3's failure witness needs NP-oracle circuits, reducing (D2) to a precise compressibility statement | 60 | **52** |
| **15c** other | 30 | **40** |

**Why I am below the reviewer on 15b and above on 15c.** §2(b) says Q3 may not reach its own question: if the weight budget cannot be made to fit, the outcome is neither "compresses by a plain circuit" nor "needs an NP-oracle circuit" but **"the construction does not get off the ground as posed"**, which is 15c. That is a real possibility and I am pricing it rather than assuming the question is well formed.

**Why I am at 8 on 15a.** It would answer an open question of Ren–Williams. The isolation predicate is *prima facie* coNP-ish (§2c to confirm), and plain-circuit hardness is not known to fool such tests — that is exactly why Q5.3 is open. A route round it via f's own bits is worth testing, not believing.

## §4. Flags

- **Flag F15 — the witness-length trade in Q1 must appear in the lemma statement** (§2a), since RW26's class tracks rounds and length separately.
- **Flag G15 — the weight budget (§2b) is checked before any compression claim.** If it does not fit, say so and report 15c rather than adjusting the construction to make it fit. *(The W14 instruction, adopted: report slack, do not redefine.)*
- **Flag H15 — "isolation fails ⇒ compression" must name WHICH circuit class does the compressing.** If the reconstruction needs to test preimage membership, it needs NP queries, and the route is the SVN one in disguise — that is 15b, and it must be demonstrated, not asserted.
- **Flag Z13 (standing).**

## §5. Kill tests

- **(i)** Primaries verbatim: RW26 §3 and §5, SU05 §3, Korten survey §4, Korten–Santhanam abstract and algorithm section. Every theorem number checked against source text.
- **(ii)** No bound from the closed sub-line (W7–W14) is cited as evidence here — different model, and it does not transfer.
- **(iii)** The ECCC keyword page checked before writing "open" anywhere.
- **(iv)** Every count with its comparison bound: weight bits against |f| = T; query count and witness length against RW26 Thm 3.1's n.
- **(v)** Exact vs sampled labelled; no computation is presented as proof of an asymptotic claim.
- **(vi)** If Q3 does not reach its question, say so plainly (Flag G15).
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings (written after the work; priors above are unrevised)

*Primaries read verbatim this run: RW26 §3 (Theorem 3.1 and the stage recursion) and §5 (Questions 5.2, 5.3 and the closing question); SU05 §3.3 (Theorem 3.12 and the Valiant–Vazirani/PRG prose); Korten survey §5.2 (Definition 7, Lemma 7, Theorem 7, Corollary 6); Korten–Santhanam ECCC TR25-104 (abstract, Hypotheses SH/WH, Theorems 12–16, Corollary 1), extracted locally; ECCC range-avoidance keyword page; ECCC TR25-191 abstract via fetch.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **15a** Q1 **and** plain-circuit compressibility | 8 / 10 | no |
| **15b** Q1 proved; (D2) reduced to a precise compressibility statement | **52** / 60 | **this is the outcome, with the test's class sharpened** |
| **15c** other | 40 / 30 | no — **my reason for pricing this high was wrong (§1)** |

## 1. My §2(b) budget objection is dissolved — by a mechanism I had not considered

I pre-registered that Q3 could not get off the ground: fresh isolation weights at each of the ≈ T/n nodes cost O(n log n) bits each, totalling ≈ T log n against |f| = T. **That is correct for per-node weights and wrong as a general obstruction.**

**Lemma W15.0 (weights fit; the reviewer's construction, verified here).** Share one weight assignment across all blocks *at a level*, drawing a fresh assignment per level. Conditioned on the levels above — which fix this level's blocks — a fresh assignment isolates every one of the ≤ T/n blocks except with probability ≤ (T/n)·(n/W) = T/W, by a union bound **which needs no independence across blocks**. Taking W = T·k·n gives failure ≤ 1/(kn) per level and ≤ 1/n over all k = ⌈log(T/n)⌉ levels. **Budget: k levels × n weights × log W ≈ n·(log T)² bits**, which at T = 2^{Θ(n)} is ≈ n³ — against |f| = T = 2^{Θ(n)}. **It fits with exponential room.** ∎

**Recorded as a miss**: I priced 15c at 40 against the reviewer's 30 *specifically* on this objection, and the objection does not survive. *(I also, mid-round, retracted the objection for the wrong reason — confusing the survey's d-parameterised tree with RW26's — and then reinstated it. The correct disposal is Lemma W15.0, neither of my two positions.)*

## 2. Q1 — the uniqueness lemma, with the parameter trade in the statement

**RW26's adaptivity, verbatim** (§3): *"for every Φj, let xj ∈ {0,1}^n denote its lexicographically smallest satisfying assignment. The simplest way to compute xj would cost **n parallel rounds per stage**: one round for each variable value."* Theorem 3.1's parameters are **#rounds = O(n + log(T/n))**, **length = n**.

**Lemma W15.1.** *Suppose every block arising in the Jeřábek–Korten tree on (G, f) has a **unique** preimage under G (by injectivity on the relevant blocks, or by promise). Then the reduction runs in **one round** of parallel NP queries.*

*Proof.* For each stage i, block j and bit t, ask the single NP query **"is there a consistent chain of preimages from f down to block (i,j), and is bit t of that block 1?"** — the witness being the ancestry of (i,j): the preimages at each level between the root and (i,j). Under uniqueness that chain is unique, so the answers across all (i,j,t) describe **one** assignment and are mutually consistent; the blocks reconstruct correctly. In parallel, ask for each (i,j) whether a consistent chain down to (i,j) exists at all; the first level at which some block answers NO yields that block as the AVOID solution, exactly as in the sequential algorithm. Query count: Σ_i 2^{i−1}·2n = **O(T)**. ∎

**The trade (Flag F15, in the statement).** The witness is the whole ancestry subtree, **O(T) bits**, against Theorem 3.1's **n**. For FP^NP_tt this is harmless — only non-adaptivity matters, and T is the input length — **but RW26's class is parameterised by rounds *and* witness length, so the lemma buys one round at the cost of the length parameter and must be quoted that way.**

**What breaks without uniqueness**, and it is RW26's own failure mode: distinct queries may be answered along **different** chains, so the assembled bits need not form a preimage of anything — the single-valuedness failure. Uniqueness is exactly what makes the parallel answers refer to one object.

## 3. Q2 — the predicate the derandomisation must fool, and why plain hardness is not known to suffice

**SU05 §3.3, verbatim:** *"there is a polynomial time algorithm that makes non-adaptive NP queries to test whether the outcome of applying the Valiant-Vazirani reduction to a satisfiable circuit C (for a specific choice of random bits) succeeds in producing a circuit that has a unique satisfying assignment. Using a PRG for non-adaptive SAT-oracle circuits, it is then possible to deterministically produce a list of candidate circuits from C, one of which is guaranteed to have a unique satisfying assignment."*

**So the test is "these random bits isolate", it is decided by non-adaptive NP queries, and the PRG must therefore fool non-adaptive SAT-oracle circuits.** By Klivans–van Melkebeek that needs hardness against those circuits; SU05 Corollary 3.3 supplies it from SV-nondeterministic hardness, giving **Theorem 3.12**: *"If E^{NP‖} requires exponential size SV-nondeterministic circuits, then there is a procedure that, given a circuit C, outputs a satisfying assignment for C if one exists, and runs in polynomial time with non-adaptive NP-oracle access."* **Plain-circuit hardness of E^NP is not known to fool SAT-oracle circuits — that is precisely the gap in Question 5.3.**

**Korten–Santhanam (TR25-104) does not bear on this, and the round's question about it is a category error.** Their hypothesis is *"there is an ϵ > 0 for which TIME[T(n)] ⊄ TIME^NP[T(n)^ϵ]/2^{ϵn}"*, and NP enters **only inside the hypothesis** — the algorithms are **polynomial time with no oracle at all** (Theorem 13: *"Polynomial time construction of…"*; Corollary 1: *"a polynomial-time algorithm which solves Range Avoidance on uniform circuits of size n^d"*). **There is no oracle-access pattern to classify as adaptive or not.** Moreover their target is **uniform** Avoid, which their Corollary 1 explicitly separates from the general problem: general Avoid is infeasible under NP ≠ coNP plus sub-exponentially secure iO (their Theorem 16, citing ILW23). **So it is not a route to (D2).**

**ECCC check (kill test (iii)), done before writing "open":** the 2025–26 range-avoidance entries are TR25-030, TR25-034, TR25-104, TR25-121, TR25-191, TR25-210, TR25-220, TR26-118. The only one I had not seen is **TR25-191** (Ren–Wang–Zhong), which proves Avoid is hard **for nondeterministic algorithms** from demi-bits generators; on the fetched abstract it states no barrier for FP^NP, FP^NP_tt or non-adaptive NP-oracle algorithms and no sufficient circuit lower bound. **Question 5.3 stands open.** *(Fetched abstract, not my own reading of the body — labelled as such.)*

## 4. Q3 — the crux, and the class of the failure test

**Tie-by-tie compression is dead, but not for the reviewer's reason.** The ruling argues a tie costs 2n bits to name and saves ≈ log W, "a net loss". **That arithmetic does not hold at the parameters Lemma W15.0 needs:** log W ≈ log T + 2n, so naming a tie explicitly *gains* ≈ log T bits. **The idea fails for a structural reason instead:** the compressing circuit must **locate** the tying pair, and locating a minimum-weight preimage requires NP queries — so the object doing the compressing is an **NP-oracle circuit**, which is Flag H15's criterion and routes straight back to SVN hardness. **The correct shape is the reviewer's PRG contrapositive**, not tie counting: f is the hard function of a Nisan–Wigderson generator whose outputs are the weight assignments, and a failure to isolate yields a distinguisher **in the class that decides the failure test**.

**So everything turns on the class of T(w) = "at every node, the min-weight preimage is unique", and here the reviewer's expectation can be sharpened.** Written directly, uniqueness of a minimum over an exponentially large preimage set is ∃x ∈ S_z ∀x′ ∈ S_z (x′ ≠ x → w(x′) > w(x)) — **Σ₂-type**, as the ruling says. **But a strictly stronger and cheaper predicate suffices:**

> **T′(w) := "for every block, all preimages have pairwise distinct weights."**

T′ trivially implies unique minima, and it is **Π₁ (coNP)** — a universal statement over pairs, with no alternation. Its cost: for x ≠ x′, w(x) − w(x′) is a non-zero linear form, so P[w(x) = w(x′)] ≤ 1/W; union over ≤ |S_z|² ≤ 2^{2n} pairs and ≤ T/n blocks per level and k levels gives failure ≤ k·(T/n)·2^{2n}/W, so **W = T·2^{2n}·poly** suffices, costing log W ≈ log T + 2n bits per weight and **≈ n³ bits overall** — still far inside |f| by Lemma W15.0's accounting.

**Therefore (b): the hardness this route needs is hardness against co-nondeterministic circuits** — a PRG fooling Π₁ tests — **which is the SV-nondeterministic / non-adaptive-SAT-oracle family of KM02, MV05 and SU05 Theorem 3.12, rediscovered.** Plain-circuit hardness of E^NP does not fool coNP circuits, and that is the whole of the gap.

**15b in precise form:** *(D2) from plain-circuit hardness requires an isolation test for the Jeřábek–Korten tree lying in a class that plain-hard strings can fool. The natural test is coNP-type — sharper than Σ₂, and still strictly above plain.*

## 5. The two gaps are different, and this is worth recording

**(C₁)'s gap is reconstruction; (D2)'s gap is adaptivity.** RW26's closing question is about the former, verbatim: *"Let Π be an encoded computational history, then either Π is 'hard enough' to solve AVOID, or Π is 'easy' so that one can 'reconstruct' Π efficiently. Is there a suitable definition of 'hardness' so that any 'hard enough' Π can be used to solve AVOID in FP^NP_tt, while Π being 'easy' implies an efficient MA algorithm for reconstructing Π?"* **Inside (D2) there is no win-win and no reconstruction: f is handed over by the hypothesis, and the only thing hardness must buy is the isolation.** Conflating the two would make (D2) look harder than it is.

## 6. Kill tests

- **(i)** Primaries verbatim with theorem numbers; every quote checked against source text this run.
- **(ii)** No bound from the closed black-box sub-line (W7–W14) is cited as evidence — different model, does not transfer.
- **(iii)** ECCC keyword page checked before writing "open"; TR25-191 identified and labelled as a fetched abstract.
- **(iv)** Counts with their comparison bounds: n³ weight bits against |f| = T = 2^{Θ(n)}; O(T) queries and O(T) witness length against Theorem 3.1's n.
- **(v)** No computation is presented as proof of an asymptotic claim; §4's union bounds are written out.
- **(vi)** Flag G15 honoured in the hard direction: the budget question was resolved **against** my pre-registered objection, and I record that rather than defending it.
- **Priors wrong said with the finding:** §0 and §1.

## Ceiling

**W15 proves nothing unconditional and nothing about P vs NP.** It supplies one lemma (uniqueness collapses the Jeřábek–Korten adaptivity to a single round, at a witness-length cost), and it locates Question 5.3's obstruction exactly: **the isolation test is coNP-type, and plain-circuit hardness is not known to fool coNP circuits.** Whether a weaker test exists whose failure probability is still 1/poly is the open question this leaves.
