# Y8: Hirahara–Nanashima as a second horn, and the oracle question. Pre-registration

*Drafted 2026-09-11 on branch `y8-hn-oracle`, on the author's go ("Draft Y8 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply, including the newest: **when a flag's force comes from applying a theorem inside an oracle world, check first whether that theorem relativizes.***

## Ceiling (first)

Unchanged and stated in the same breath as any result: success on either arm is **conditional** — it bears on `NP ⊄ ioBPP ⇒ OWF`, and `NP ⊄ ioBPP` is itself open and untouched by this branch.

## §0. Refuted premises checked (the practice)

Not reused: "hidden ρ" (Y3); "no off-sample rows", "(1+ζ) inflation" (Y4); "the grid is symmetric" (Y5); "(PL) is loose-access lowness" (Y6, mine); **"the Pessiland oracle bars the non-explicit route" (Y7, mine — it does not, because LP23's equivalence is not known to relativize)**.

## §1. Availability, checked at drafting (g1)

| source | status |
|---|---|
| **HN23**, "Learning in Pessiland via Inductive Inference" (ECCC TR23-100) | **fetched, readable**, 89 pp. Abstract, §2.2–2.3, §4.2 read at drafting. |
| **HN22**, "Finding Errorless Pessiland in Error-Prone Heuristica" (CCC 2022, LIPIcs 234:25) | **fetched, readable**. Abstract read at drafting. |
| LP23, GK24, SS22, HMX10, Wee, AW | already local and verified in Y1–Y7. |

## §2. Arm (a): Hirahara–Nanashima as a candidate second horn

**What their theorems actually say (read at drafting, to be re-checked in the run).**
- **Theorem 2.3** and **Theorem 2.4** are **equivalences with the non-existence of io-OWF**: "The following are equivalent: 1. There exists no infinitely-often one-way function. 2. [agnostic learning / ACD learning / … is solvable on average]".
- **Theorem 2.10 ([IL90])**, likewise: "no io-OWF ⟺ a randomized poly-time algorithm approximates Q^t".
- **§2.3:** they obtain "the first characterization of the existence of a one-way function … by the worst-case intractability of some promise problem", the promise problem being in **AM**.

**Flag H (my expected verdict for arm (a); to be proved or refuted in the run).** These are the **first horn restated**, not a second horn:
- A dichotomy needs "MK^tP|Q easy ⇒ *something* ⇒ OWF **or** NP easy". HN23 gives "¬OWF ⇒ learning objects exist". Composing them yields "¬OWF ⇒ learners", which is the same side of the disjunction, not the other one.
- To close, one needs **"learners ⇒ NP easy on average"**, and HN23 states plainly (§1, verified at drafting): *"The major open problem of ruling out Pessiland is equivalent to proving that there exists a heuristic algorithm that solves NP on average under the non-existence of a one-way function."*
- **So the missing step is exactly "rule out Pessiland", which is at least as hard as the goal.** Expected outcome for arm (a): **circular in the sense that matters** — the second horn's completion is the open problem the whole line is trying to avoid.

**Flag C7 applied to HN23 (ruling of Y7).** Their algorithms "run in exponential time in the computational depth of secret information" (§4.2, verified at drafting), so the case split is **not** polynomial-time decidable. **That satisfies Lemma C7's necessary condition** — which is why arm (a) is worth the reading even though Flag H expects it to fail: HN23 is the only candidate read so far that is *not* excluded by C7.

**Flag R8 (the new practice line, applied to HN23 before use).** HN23 §4.2, verbatim: *"Since all the proofs in this work are relativizing, improving the running time of our learning algorithms requires fundamentally new ideas."* **All their proofs relativize.** So any win-win built on HN23 is a relativizing argument, and by Y7's ingredient map it cannot supply the non-relativizing ingredient the door needs. **This is an independent reason to expect arm (a) to fail**, and it was not available before drafting.

## §3. Arm (b): the oracle question

**(b1) Does LP23's proof relativize?** Walk the code-reading step with the oracle's description included: LP23 bound the number of instances on which an attacker errs, then conclude those instances have small K. Relative to O, describing the attacker's *behaviour* requires describing O as well. **The question is whether the K-bound survives.** Expected: it does not, so LP23's equivalence is not known to relativize, confirming Y7.

**(b2) If not, attempt the barring oracle:** an O with **NP^O ⊄ ioBPP^O and MK^tP|Q^t_β ∈ ioBPP^O**.
- **Flag O (drafting finding, which cuts against a quick construction).** HN22's abstract (verified) says that in *their* relativized world, meta-complexity is **hard**: *"GapMINKT^O ∉ pr-SIZE^O[2^{o(n/ log n)}]"*, alongside DistNP^O ⊆ HeurP^O. That is the **opposite** of what the barring oracle needs on the meta-complexity side. So the most sophisticated relativized construction in this area produces hardness where I would need easiness.
- **Expected first failing step:** making MK^tP|Q easy relative to O while keeping NP hard requires the oracle to answer K^t-questions about *itself*, and the promise Q^t_β is defined by unbounded K relative to O. **The self-reference of the promise under relativization is the named step to test.**
- If the construction provably cannot exist because "MK^tP|Q ∈ ioBPP^O forces OWF-inversion relative to O by a relativizing argument", then the implication holds relative to every oracle, which would be **striking and must be treated with full suspicion**: it would mean the door is provable by relativizing means, contradicting the expectation that the holy grail is hard.

## §4. Kill tests

- **Non-circularity first** for any candidate second horn (ruling of Y7, carried forward).
- **Lemma C7** applied to each candidate's case split.
- **Flag R8:** any argument assembled must be checked for whether its ingredients relativize, *before* it is called a route.
- **Suspicion protocol at full strength** for the (b2) "cannot exist" branch.

## §5. Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y8a** | HN gives a non-circular second horn: the win-win stands with one named open hypothesis. |
| **Y8b** | HN circular or reduction-based **and** the barring oracle exists: the door needs a non-relativizing, non-algorithmic technique, stated. |
| **Y8c** | LP23 relativizes: Pessiland bars the door and Y7 is reversed. |

**Priors.**
- Reviewer: Y8b 45 / Y8c 30 / Y8a 25.
- Mine: **Y8b 40 / Y8c 25 / Y8a 15, with 20 on a fourth outcome the reviewer's list does not contain: "HN is circular *and* the barring oracle is not constructed here" — i.e. arm (a) fails and arm (b2) stalls at the self-reference step, leaving the door open and unbarred exactly as Y7 left it.** Flag O is the reason: the one relativized construction in this area gives meta-complexity *hardness*, not easiness.
- **The reviewer is asked to rule on whether that fourth outcome is admissible**, since on my reading it is the most likely single outcome and the reviewer's Y8b presumes the oracle gets built.
