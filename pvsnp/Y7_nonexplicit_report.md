# Y7: the non-explicit door. Report

*Run 2026-09-11 on branch `y7-nonexplicit`, on the author's go ("Run Y7, push after merge"), against the pre-registration (ee03dff) and the reviewer's ruling (3bdc650).*
- *Priors, both sides: Y7b 55 / Y7a 25 / Y7c 20.*
- *Ruling (1): the Pessiland kill test is decisive; then map the non-relativizing ingredients.*
- *Ruling (2): Flag C7 as a lemma, with the usability question.*
- *Ruling (3): non-circularity first; the map from statements, not vocabulary.*

*Documents only; `formal/` closed.*

**Sources read as text this run:**
- **Wee, "Finding Pessiland" (TCC'06)**, abstract, §1.1 Theorems 1–2, and Theorem 3 (restating Impagliazzo–Rudich);
- **Aaronson–Wigderson, "Algebrization" (ECCC TR08-005)**, abstract and §8.4;
- **SS22 footnote 6** and **HIR23 l.668–673**, both on Ko's relativization barrier;
- **LP23 l.86–99 and l.325–335** (verified in Y6 and re-read here).
- *Impagliazzo's five-worlds survey was fetched but its two-column extraction is too corrupted to quote; it is used only as background and nothing rests on it.*

## 0. Outcome

**Y7b, with a correction to my own Flag R7.**

1. **The Pessiland oracle exists and is standard (verified).** Wee's Theorem 3: *"There exists an oracle relative to which there exists a strongly hard-on-average language in NP ∩ coNP, but no one-way functions."* His Theorem 1 adds a relativized Pessiland containing *"a language that lies within NP but outside BPTime(2^{o(n)})"*.
2. **But it does not bar the implication, and my pre-registered Flag R7 overstated.** To conclude "MK^tP|Q^t_β ∈ ioBPP relative to O" from "no OWF relative to O" one needs **LP23's direction to relativize**, and LP23's own account (l.325–335) is that their analysis *"make[s] use of the code of the attacker"*. So the oracle gives a world with NP ⊄ ioBPP and no OWF, **not** a world with NP ⊄ ioBPP and the promise problem easy. **The barring statement I pre-registered does not follow.** (§1)
3. **What is verified instead:** any **NP-hardness** proof for meta-complexity problems must be non-relativizing (Ko, in two independent sources), and the technique that overcame it in this area is the **PCP theorem**, which produces reductions. (§2)
4. **The ingredient map (ruling 1) has no entry of the needed shape** — non-relativizing *and* not reduction-producing — so **Y7b stands in the reviewer's wording**: the non-explicit door is open only to a non-relativizing, non-algorithmic technique, and none is known. (§3)
5. **Flag C7 as a lemma (ruling 2): proved, and the usability question answered — LP23's formulation does tolerate a non-constructive horn.** (§4)

## 1. The Pessiland kill test, and the correction to Flag R7

**Verified (Wee, §1.1).**
- **Theorem 1:** *"There exists an oracle relative to which there exists a strongly hard-on-average language in NP ∩ coNP, but no one-way functions. Furthermore, there is a 2-round public-coin argument system with poly-logarithmic communication complexity for a language that lies within NP but outside BPTime(2^{o(n)})."*
- **Theorem 3 (Impagliazzo–Rudich):** the first sentence of Theorem 1, attributed.
- Wee's own use of such an oracle is the standard one: *"a proof of this statement must use a non-relativizing argument"*, for the statement "if there exists a non-trivial 2-round argument system, then there exists one-way functions".

**What this gives us, exactly.** Relative to that oracle O:
- NP^O ⊄ ioBPP^O (a strongly hard-on-average language is not decided by any efficient algorithm at any large length; Wee's Theorem 1 even gives worst-case hardness beyond 2^{o(n)});
- no one-way functions exist relative to O.

**What Flag R7 claimed, and why it fails.** I pre-registered: "if Pessiland is consistent with relativization, then every proof of `NP ⊄ ioBPP ⇒ MK^tP|Q ∉ ioBPP` is non-relativizing". The step from "no OWF relative to O" to "MK^tP|Q^t_β ∈ ioBPP relative to O" uses LP23's Theorem 1.1 **relativized**. LP23 l.325–335 (verified):

> "the proof of our main theorems rely on non-black box techniques. In particular … we make use of the code of the attacker in analyzing the security of the OWFs."

An argument that describes an attacker by its code does not obviously survive relativization: relative to O, an attacker's behaviour is not determined by a short string, since the oracle must be described too, and LP23's counting step is exactly a short-description argument. **So the relativized form of the equivalence is not available, and the oracle does not place the promise problem in ioBPP^O.**

**Honest status:** what would bar the implication is an oracle with **NP ⊄ ioBPP and MK^tP|Q ∈ ioBPP**. No such oracle is exhibited in anything read. **That is the named gap**, and it is the correct replacement for Flag R7.

## 2. What the relativization barrier does cover here (verified, two sources)

- **SS22, footnote 6:** *"A result of Ko [39] states there is no relativizing NP-hardness proof for K^poly, but this seems to say little about the unrelativized case."*
- **HIR23, l.668–673:** *"There are mainly two barriers to showing NP-hardness of meta-complexity problems: relativisation [Ko91] and oracle independence [HW16]. Ko [Ko91] showed that any NP-hardness result for MINLT … must be non-relativising. This relativisation barrier was overcome by [Hir22a] using non-relativising techniques such as the PCP theorem."*

**Scope.** Both statements are about **NP-hardness proofs**, i.e. about exhibiting reductions. The non-explicit door is precisely the attempt to prove the implication **without** a reduction, so these statements do not close it by themselves — they constrain the reduction-producing route, which Y2–Y6 already closed by other means.

**The one-line summary of the barrier situation:**
- reduction-producing routes: barred by GK24/SS22 (explicit, entropy/SZK) and constrained by Ko (relativization);
- the non-explicit route: **not** covered by either, and **not** barred by the Pessiland oracle for the reason in §1.

## 3. The ingredient map (ruling 1)

The question the ruling converts to: **which non-relativizing ingredients exist that do not produce a reduction?**

| ingredient | non-relativizing? | produces a reduction? | verdict |
|---|---|---|---|
| **Arithmetization** | yes, but **algebrizes**. Aaronson–Wigderson's abstract: *"all known non-relativizing results based on arithmetization—both inclusions such as IP = PSPACE and MIP = NEXP, and separations such as MA_EXP ⊄ P/poly—do indeed algebrize"*, and *"almost all of the major open problems … require non-algebrizing techniques"* | typically yes (protocols, simulations) | **fails twice:** algebrizes, and is algorithmic |
| **PCP / code-reading, non-black-box** | yes — HIR23: Ko's barrier *"was overcome by [Hir22a] using non-relativising techniques such as the PCP theorem"*; LP23 read the attacker's code | **yes, by construction** — this is exactly Flag C7 | **fails:** the barriers reapply to the reduction it yields |
| **Shannon-style counting over short programs** | not by itself: counting arguments relativize (the count is taken relative to the same oracle) | no algorithm produced | **fails at the other end:** it yields typical-side statements, and gives **no implication from NP-hardness** — counting says a random string is incompressible, never that *if* SAT is hard *then* a particular problem is hard |
| **Cryptographic assumptions** (HIR23's route) | evades oracle-independence *by assumption*, not by technique | yes | **fails:** and it assumes what the holy grail wants to conclude |

**So the map contains no ingredient that is simultaneously non-relativizing and non-reduction-producing**, which is the reviewer's Y7b wording: *the non-explicit door is open only to a non-relativizing, non-algorithmic technique, and none is known.*

## 4. Flag C7 as a lemma, and the usability question (ruling 2)

**Lemma C7 (ours).** Let the argument be a dichotomy: "either MK^tP[s]|Q^t_β is average-case hard (hence OWF), or structure S exists and S yields OWF by another route." If the case split is decidable in polynomial time, then the two horns compose into an explicit reduction, and GK24/SS22 reapply.

*Proof.* Given an instance and a poly-time decision of which horn holds, the argument names, for each input, which of the two efficient constructions to run. That is a poly-time computable map from the hypothesis to an OWF-breaking or problem-deciding procedure, i.e. an explicit reduction of the kind GK24 Theorem 5 and SS22 Theorem 3 quantify over. ∎

**Consequence.** Any admissible win-win needs a case split **not decidable in polynomial time**.

**The usability question, answered from LP23's own formulation (verified, l.86–99).** OWF-hardness reads:

> "if Π can be decided (in the worst-case) for infinitely many input lengths by 'efficient attackers', then **all poly-time functions can be inverted** with probability 1/2 by 'efficient attackers'."

This is a statement about the **existence** of inverters, and OWF-completeness is stated as "Π ∉ ioBPP **iff** OWFs exist". Neither formulation asks anyone to **identify** which function is one-way or to exhibit the inverter. **So a non-constructive second horn is tolerated**: an OWF that exists but cannot be identified still falsifies "OWFs do not exist", which is all the equivalence needs. **The undecidable case split is compatible with LP23's notion**, and Lemma C7's constraint is therefore not fatal to the shape — it only excludes efficient case splits.

## 5. Non-circularity (ruling 3)

Every candidate second horn must yield OWF by a theorem **other than** LP23's equivalence. Checked against the statements (not vocabulary):
- **LP20/LP23/LP25's characterizations:** all are the first horn restated. **Circular.**
- **Hirahara STOC'23:** its conclusion is conditioned on NP-hardness of approximating distributional K^t, i.e. on a reduction existing. **Not usable in a non-explicit argument**, and it reintroduces exactly the object the door avoids.
- **HIR23:** OWF-hardness under cryptographic assumptions (witness encryption, injective OWF). **Assumes OWF-type objects**, so it cannot serve as the second horn of an argument whose conclusion is OWF.
- **Hirahara–Nanashima ("Learning in Pessiland"):** the natural shape is "either meta-complexity is hard, or a learning algorithm exists". Read only secondhand in this program, so **recorded as unexamined**; it is the one candidate not excluded here, and the report names it as the only place a non-circular second horn might be found.

## 6. Priors against outcome, and misses

| | Y7b | Y7a | Y7c |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 45 → 55 | 35 → 25 | 20 → 20 |
| mine | 55 | 25 | 20 |
| **outcome** | **✓** (the ingredient map has no entry of the needed shape) | | |

- **My miss:** Flag R7 as pre-registered was **wrong**. The Pessiland oracle does not bar the implication, because the step through LP23's equivalence needs that equivalence to relativize, and LP23's proof reads the attacker's code. I carried the flag into my prior (I raised Y7b from 45 to 55 **on the strength of a claim that does not hold**), which makes the prior right for the wrong reason. Scoring is the reviewer's.
- **The practice line this suggests:** when a flag's force comes from applying a theorem inside an oracle world, check first whether that theorem relativizes.
- **Correct in the pre-registration:** the structural point about LP23's notion (an implication, not a reduction), Flag C7, and the non-circularity test.

## Ceiling

Y7 proves nothing about P vs NP or OWF. It closes the last of Y2's three escapes **as a map, not as a barrier**: the non-explicit door is not barred by anything read, and no known technique fits through it. The one unexamined candidate is Hirahara–Nanashima's Pessiland-learning line.

## Formal record

Untouched (the author's decision).
