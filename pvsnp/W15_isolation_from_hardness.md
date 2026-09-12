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
