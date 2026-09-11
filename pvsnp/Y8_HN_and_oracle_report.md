# Y8: Hirahara–Nanashima as a second horn, and the oracle question. Report

*Run 2026-09-11 on branch `y8-hn-oracle`, on the author's go ("Run Y8, push after merge"), against the pre-registration (b2b4432) and the reviewer's ruling (b4503cc).*
- *Priors, both sides: Y8b 40 / Y8c 25 / Y8d 20 / Y8a 15.*
- *Documents only; `formal/` closed.*

**⚠ This report reverses Y7's headline finding, which the reviewer accepted and which is on the page. §2 is written under the suspicion protocol at full strength, and §4 says exactly what would falsify it.**

**Sources read as text this run (all local, all previously fetched):** HN23 (ECCC TR23-100) §2 theorem inventory, Theorems 2.11, 7.1, 7.2, §4.2; HN22 (CCC'22) abstract and §1.1, §1.3; LP23 l.325–335 and l.460–485; Wee (TCC'06) §1.1; plus the Y1–Y7 verified record.

## 0. Outcome

**Y8c: LP23's direction relativizes, so the Pessiland oracle bars the non-explicit door, and Y7's "first door with no known barrier" is withdrawn.** Arm (a) is settled as Lemma D, as the reviewer ruled it should be recorded whichever outcome landed.

1. **Arm (a), closed (§1).** Every HN23 theorem inventoried is an equivalence with "there exists no infinitely-often one-way function", including the AM promise problem of Theorem 2.11. **Lemma D stands: no dichotomy whose second horn is an HN-family learning or compression object shortcuts the door.**
2. **Arm (b1), the reversal (§2).** LP23's code-reading step survives relativization: the failure-set indexing argument goes through with descriptions that may query the oracle, giving K^O in place of K. With the promise relativized consistently, LP23's equivalence holds relative to every oracle. **Therefore, relative to the Impagliazzo–Rudich / Wee oracle, NP is hard and MK^tP|Q is easy, so the implication `NP ⊄ ioBPP ⇒ MK^tP|Q ∉ ioBPP` is false there, and every proof of it — reduction or not — must be non-relativizing.**
3. **Arm (b2) is moot (§3):** the barring oracle is not something to construct; it already exists, and it is the standard Pessiland oracle. Flag O's tension dissolves: HN22's world was the wrong world to look at.
4. **The page must be amended** (§5): the non-explicit door is **not** barrier-free. It evades the *reduction* barriers (GK24, SS22) but not relativization.

## 1. Arm (a): Lemma D, settled (the reviewer's ruling, recorded)

**The inventory (verified this run).** In HN23, every one of Theorems 2.1, 2.3, 2.4, 2.8, 2.9, 2.10, **2.11**, **7.1**, **7.2**, 9.7, 10.6, 10.8 has the form *"The following are equivalent: 1. There exists no infinitely-often one-way function. 2. …"*.

**Theorem 2.11 verbatim**, the one candidate that might have had a different shape:

> "There exists a constant c such that the following are equivalent. 1. There exists no infinitely-often one-way function. 2. The following promise problem Π = (Π_Yes, Π_No) ∈ pr-AM is in pr-BPP. Π_Yes = {(x, 1^s, 1^t) : K(x) ≤ s and cd^t(x) ≤ log t}, Π_No = {(x, 1^s, 1^t) : K(x) > s + c log t and cd^t(x) ≤ log t}."

**So Lemma D holds as stated at pre-registration.** The second horn of any HN-based win-win is ¬io-OWF restated; completing it needs "learners ⇒ NP easy on average", which HN23 §1 says is *equivalent to ruling out Pessiland*. **Y8a is closed.**

## 2. Arm (b1): the relativization walk, and the reversal

**LP23's step, verbatim (l.464–479):**

> "assume for contradiction that some uniform polynomial-time attacker A manages to solve Π on average with probability 1 − 1/n^{c′} … there are at most 3 × 2^n/n^{c′} instances on which A fails with probability ≥ 1/3 over its randomness. But then all those instances must have Kolmogorov complexity bounded by log(2^n/n^{c′}) + O(log n) (to index the instance among the list of elements on which A fails with probability ≥ 1/3, plus the additional O(log n) to describe n as well as to provide the constant-size description of A). … Note that the above argument is non-black box: we rely on the fact that we have a short description of the attacker A."

**The walk (ours).** Fix an oracle O and relativize every ingredient: the attacker is A^O, time-bounded complexity is K^{t,O} (oracle-aided universal machine), unbounded complexity is K^O, and the promise is Q^{t,O}_β = {x : K^{t,O}(x) − K^O(x) ≤ β·log K^O(x)}.
- The failure set F = {x : A^O errs on x with probability ≥ 1/3} is determined by A's code **and** O.
- A decoder **with oracle access to O** can enumerate F (simulate A^O on each candidate, estimating its error probability) and select the i-th element.
- So every x ∈ F has **K^O(x) ≤ log|F| + |A| + O(log n)**, exactly LP23's bound with K replaced by K^O.
- Hence "worst-case hardness of Π|KR^O ⇒ mild average-case hardness relative to O" goes through verbatim.

**Why the rest of LP23 comes along.** Their own account (l.325–335, verified): *"While our constructions are black-box, our analysis is non-black box"*. Black-box constructions relativize. The non-black-box **analysis** is the counting step just walked, and it relativizes because the decoder may query O. **"Non-black-box" is not "non-relativizing"** — that conflation is what Y7 got wrong.

**The consequence.** Relative to the Impagliazzo–Rudich oracle (Wee, Theorem 3, verified in Y7): *"There exists an oracle relative to which there exists a strongly hard-on-average language in NP ∩ coNP, but no one-way functions."*
- NP^O ⊄ ioBPP^O: a strongly hard-on-average language is not decided at any large length, so it is not in ioBPP^O.
- No OWF relative to O, so by the relativized LP23 equivalence, **MK^tP[s]^O|Q^{t,O}_β ∈ ioBPP^O**.
- **So the implication is false relative to O**, and any proof of it must be non-relativizing — **whether or not it exhibits a reduction**. That is exactly Flag R7 as I first pre-registered it in Y7, and I withdrew it there for a reason that does not hold.

**Re-derivation, second route.** Independently of the counting step: LP23's Theorem 1.1 is proved from LP20/LP21a's cryptographic machinery (PRG/PRF/EP-PRF constructions and reductions), all of which are black-box and therefore relativize, composed with the counting step above. A composition of relativizing steps relativizes. Same conclusion.

## 3. Arm (b2): moot, and Flag O dissolved

The barring oracle does not need to be constructed: **it is the Pessiland oracle**. Flag O (HN22's world makes meta-complexity hard while DistNP is easy) is now beside the point — that world was constructed for the errorless/error-prone question, not for this one. The pre-registered "self-reference of the promise under relativization" worry also dissolves: the promise relativizes by defining K^O and K^{t,O} with the oracle-aided universal machine, which is the standard convention and is what makes §2's walk go through.

## 4. Suspicion protocol: what would falsify §2

Stated, because this reverses an accepted finding:
1. **The universal machine convention.** If one insists that K^t be defined by a *fixed, oracle-free* universal machine even in a relativized world, then K^{t,O} is not the right object, the promise does not relativize, and §2 collapses. **Check:** this is not the standard convention, and it would make "MK^tP relative to O" meaningless; but the convention should be confirmed against a source that states relativized meta-complexity explicitly. **Not done this run.**
2. **The quantifier match.** LP23's equivalence is "OWF secure against PPT ⟺ Π ∉ ioBPP". IR/Wee's world has *no* one-way functions, which is stronger than "no io-OWF", so the direction used is available. If IR/Wee's statement were only about a restricted class of OWF, §2 would need the matching class. **Wee's wording is unrestricted ("but no one-way functions").**
3. **A hidden non-relativizing ingredient in LP20/LP21a.** I inferred that their constructions relativize from LP23's "our constructions are black-box". If some step of LP20/LP21a is non-relativizing in a way that statement does not cover, §2 weakens. **Not verified against LP20/LP21a's own text this run.**

**Because of items 1 and 3, §2 is stated as: LP23's equivalence relativizes, on my walk of the argument, with two source-level checks outstanding.** It is not offered as a fully verified theorem.

## 5. What the page must say now (correcting Y7)

- **Withdraw:** "the non-explicit route … is NOT known to be relativization-barred" and "the first door in the program with no known barrier against it".
- **Replace with:** the non-explicit route evades the **reduction** barriers (GK24, SS22) by construction, **but is relativization-barred**: relative to the Pessiland oracle, NP is hard and MK^tP|Q is easy, so any proof — reduction or not — must be non-relativizing. The barring oracle is not hypothetical; it is Impagliazzo–Rudich's.
- **Keep:** Lemma C7, Lemma D, the ingredient map, and the ceiling. The map's conclusion is now sharper: the door needs a technique that is non-relativizing **and** non-reduction-producing, and Y7's map found none.

## 6. Priors against outcome, and misses

| | Y8c | Y8b | Y8d | Y8a |
|---|---|---|---|---|
| reviewer → ruling | 30 → 25 | 45 → 40 | — → 20 | 25 → 15 |
| mine | 25 | 40 | 20 | 15 |
| **outcome** | **✓** | | | closed by Lemma D |

- **My miss, and it is the serious one of this program.** In Y7 I withdrew Flag R7 by arguing that LP23's equivalence "is not known to relativize" because it "reads the attacker's code". **That conflated non-black-box with non-relativizing.** The code-reading step relativizes, because the decoder may query the oracle. I then carried the wrong conclusion into the page as "the first door with no known barrier", and the reviewer accepted it.
- **The reviewer's miss:** accepting that reasoning in Y7 (its nineteenth was for calling the Pessiland test decisive; this is the mirror image — accepting the reversal without checking the conflation).
- **Practice line proposed:** *"non-black-box" and "non-relativizing" are different properties; when a proof is called non-black-box, ask separately whether it relativizes.*

## Ceiling

Unchanged. Y8 proves nothing about P vs NP. It removes an opening this program briefly thought it had found: **there is no barrier-free door on this branch.** Both arms end where the circuit side ended — on statements whose proofs would need techniques nobody has.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as Y8c on the report.** Merge e16b9e7; push on the author's standing go; then the page amendment and §10 item 20.

**Scoring, as proposed.** Mine is the serious one: the conflation of "non-black-box" with "non-relativizing", withdrawing a correct flag, and putting the wrong headline on the page. The reviewer's is its **twentieth accepted-without-checking**: accepting that withdrawal in Y7.

**Practice line adopted verbatim:** *"non-black-box" and "non-relativizing" are different properties; when a proof is called non-black-box, ask separately whether it relativizes.*

**The reviewer's condition on the amendment:** the two outstanding checks go in the same commit as the amendment, or the amendment carries them as explicit caveats. **They are discharged in that commit** (page §7):
- **(1)** the relativized-K^t convention is standard and sourced — ABKMR l.126–128 ("…relativizes with respect to any oracle A can be viewed in terms of a Kolmogorov measure which we denote…"), and HN22's Theorem 4 states relativized meta-complexity directly;
- **(2)** LP20's steps carry nothing non-relativizing beyond "constructions are black-box": their outline is counting over programs plus Yao amplification, with the converse through PRG/EP-PRG facts, and unlike ABKMR (which flags "our proofs do not relativize" when it applies) LP20 carries no such caveat.

**So Y8c stands as stated, not as a caveated claim.** **Y9 (the O(log n)-gap regime)** is named, on the author's go.
