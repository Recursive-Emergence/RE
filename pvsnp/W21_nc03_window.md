# W21: (S2), the NC^0_3-Avoid stretch window. Pre-registration

*Drafted 2026-09-12 on branch `w21-nc03-window`, on the reviewer's W21 specification, after W20 closed at `13cb4b7` and the program page was narrowed at `908c3e3`. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. Ceiling, first -- and this round's ceiling is different in kind

**(S2) is OFF the door.** Every round from W15 to W20 was about (C_1) or its neighbours. This one is not, and the page must not drift into door-talk because the habit of twenty rounds pulls that way.

**What (S2) actually buys**, as the reviewer states it: rigidity and linear-circuit lower bounds in Valiant's sense -- GGNS23 Thm 1, `FP^NP` for NC^0_3-Avoid at stretch `m = n + O(n^{2/3})` gives an explicit rigid matrix, hence a linear map with no `o(n log log n)`-size linear NC^1 circuit. **That is a real payoff and it is not (C_1).** Nothing proved here moves the door.

**Flag E21 exists to enforce that**: if a finding is stated in terms of (C_1), it is either wrong or off-target.

## §1. Refuted premises checked, and the two lines that now govern

Not reused: the four W16 errors, the three W17 errors, Lemma W17.1, the three W18 errors. **Ten consecutive wrong impossibility claims**, with positive contributions holding.

**Two practice lines earned in W20 govern this round specifically:**

1. **The framing audit precedes the mechanism's pricing.** A mechanism can die by losing its framing without ever being refuted. Twice I inflated the "other" bucket on a named mechanism (W17: 38 against 27; W20: 38 against 32) and both times the mechanism was invalidated by its framing collapsing rather than by being wrong.
2. **Name the scarce resource before ruling on a component.** The same component gave opposite verdicts in W17 and W20 depending on whether the scarce resource was fooling or enumeration.

**Both bear directly here.** A "window" between a hardness end and an algorithmic end is a *framing*, and it is only a gap if both ends are statements about the **same object** at the **same parameters**. In W20 the reviewer's route conflated the GGM range with the Reed-Muller encoding of the witness, and I nearly priced a gap between two different things. **Flag F21 is that audit, and it runs first.**

## §2. Disclosure

**(a) Contamination, declared.** Earlier this session, while verifying the "two doors are one" attribution, I read the reviewer's **W3 page**, which contains (S2)'s window and several of this round's citations -- including the bracket `(n + n^{2/3}, n^{1.4})`, GGNS23, KPI25 (TR25-030), HLZ26, RSW22, and Korten's survey. I did not read it *for* this round, but I have read it, and the window I am about to "pin" is one I have already seen asserted. **That is exactly the position in which a mapping round can confirm a number rather than check it**, and Flag C21 is the guard.

**(b) What I believe before reading, stated so it can be scored.** I expect the hardness end to be limited by the **rigidity target** rather than by the perfect-encoding step -- i.e. that `n^{2/3}` is where *Valiant's application* sits rather than where the AIK06 degree-2 to NC^0_3 encoding gives out. That is a guess about which of two constraints binds, and it is the reviewer's question (ii). I have no view yet on question (i).

**(c) What I do NOT have a mechanism for.** Nothing. Unlike W20 I am opening with no candidate idea of my own, and per §1 line 1 that is a reason to keep the "other" bucket **low**, not high: absence of a named, framing-audited mechanism is absence of evidence for 21c.

**(d) Not done -- no primary read for this round.** Not yet consulted: GGNS23 (Thms 1 and 2, §3 and the `n^{12/17-ε}` remark); KPI25 TR25-030 §5 and its barrier section; HLZ26 §1.1.3; RSW22 §5.2; Kuntewar-Sarma TR25-034; Huang-Li-Zhong ITCS 2026 on local algorithms; the ECCC 2025-2026 sweep.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **21a** an `FP^NP` algorithm for NC^0_3-Avoid at stretch strictly below `Õ(n^{1.4})`, **or** an extension of the hardness reduction to stretch strictly above `n + O(n^{2/3})` | 8 | **10** |
| **21b** both ends pinned to named quantities with the exact gap -- rigidity parameters `(r, s)` reachable as a function of stretch on one side, the verbatim 3-probe static cell-probe bound behind `Õ(n^{1.4})` on the other | 60 | **60** |
| **21c** other | 32 | **30** |

**Why 21a is 10, slightly above the reviewer's 8.** It is a **construction** question, and the standing asymmetry says my constructions are the reliable half of my output while my doubts are not -- so pricing it near the floor would be importing a doubt I have no grounds for. But only slightly above: this is an **active area with specialists**, not a model I built myself, and the W-line's own theorems were produced inside a black-box model of my own construction. Producing a new result in an area where Korten, Pitassi, Impagliazzo and others are actively working is a materially lower base rate than producing one in a setting I defined.

**Why 21b matches the reviewer exactly at 60.** I have no reason to differ, and inventing a difference to look independent would be noise. **This is the "do the work properly" outcome and the primaries exist**, so it should carry most of the mass.

**Why 21c is 30, below the reviewer's 32, and the reasoning is the point.** I have **no named mechanism** (§2(c)). By the W20 line, a mechanism is what earns mass in this bucket, and only after its framing is audited. What keeps 21c as high as 30 rather than lower is a base-rate consideration rather than an idea of mine: **this is an active area with 2025-2026 results** (KPI25, HLZ26, Kuntewar-Sarma, Huang-Li-Zhong), so there is a real chance the window as stated on the W3 page is **stale** -- which would be 21c by default and is the single most likely way this round surprises.

## §4. Flags

- **Flag F21 -- the framing audit, and it runs FIRST.** Before any "gap" is computed: are the two ends statements about the **same problem** at the **same parameters**? Same `Avoid` variant, same stretch convention (`m` as output length vs `m - n` as stretch), same circuit class (NC^0_3 vs 3-local vs degree-2), same algorithm class (`FP^NP` vs `FP` vs `FP^NP` list). **W20's near-miss was exactly this failure**, and a window is a subtraction that silently assumes commensurability.
- **Flag E21 -- (S2) is off the door.** Payoff is rigidity/Valiant. Any finding phrased in terms of (C_1) is off-target.
- **Flag C21 -- verbatim with numbers, against the contamination of §2(a).** The window `(n + n^{2/3}, Õ(n^{1.4}))` is a number I have already seen asserted on the reviewer's page. **It gets re-derived from the primaries, not confirmed from memory.** When a cited label will not resolve, search for what the statement *says*, not what it is *called* (the W19 method line).
- **Flag D21 -- stop-rule.** If 21a appears to close -- a genuine new algorithm or a genuine extension of the reduction -- **stop, send exact parameters, write nothing further** until the reviewer has checked it. A new result in an active area gets a second pair of eyes before it gets prose.
- **Flag G21 -- do not inflate 21c on an unaudited mechanism.** If one occurs to me mid-round, its framing is audited before it is allowed to move anything.

## §5. Kill tests

- **(i)** Both ends quoted verbatim with their theorem numbers: GGNS23 Thm 1 and Thm 2; KPI25's 3-probe cell-probe statement; HLZ26's `2^{n^{1-ε/2+o(1)}}`-time algorithm at `n^{1+ε}`.
- **(ii)** Flag F21 discharged explicitly and **in writing** before the gap is named -- with the answer stated even if it is "yes, commensurable".
- **(iii)** The reviewer's three questions answered separately: (i) is the algorithmic end limited by the **cell-probe bound itself** or by the **correspondence's loss**; (ii) is the hardness end limited by the **perfect-encoding step** (AIK06 degree-2 to NC^0_3) or by the **rigidity target**; (iii) what single statement would move either end by a polynomial factor.
- **(iv)** ECCC 2025-2026 swept before writing "open" or "best known".
- **(v)** Whether the known 3-probe bound is **tight** is answered, not assumed -- the reviewer flagged it and it is the difference between "the algorithm is at the barrier" and "the algorithm is at the current bound".
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Nothing from the door rounds (W15-W20) is cited as evidence here; different object, and Flag E21 forbids the drift.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 21b, with the gap pinned -- but the substantive content is Flag F21's correction, so it goes in the same sentence per kill test (vi): the bracket `(n + n^{2/3}, Õ(n^{1.4}))` is not a window between two commensurable ends, and treating it as one misstates what closing it would buy.** Flag D21 never armed.

## §6. F21 first, as promised: the sign, and who carries the error

**The exponent is a MINUS, and it is KPI25's own theorem, not only its abstract.** Verbatim:

> **Theorem 3.** "Let `t = O(1)` be a fixed odd number. There is a polynomial time algorithm which outputs a list of strings in `{0,1}^m`, such that for any `NC^0_t` generator `G : {0,1}^n → {0,1}^m` with **`m ≥ Õ(n^{t/2 − (t−2)/(2(t+2))})`** one of the strings in the list must be a range-avoidance solution for `G`. In particular, there is a polynomial time NP-oracle algorithm for range avoidance on instances of the above form."

So `ε_t = (t−2)/(2(t+2))`; at `t = 3` that is `1/10`, giving `1.5 − 0.1 = 1.4`. **The endpoint is `Õ(n^{1.4})`, derived here rather than recognised** -- which was the entire point of §2(a)'s declaration.

**Li-Zhong (TR25-049) carry the error.** Verbatim: "Most recently, this was improved to `Õ(n^{k/2})` for even `k` by [KPI25], which also improved the stretch to `(Õ(n^{k/2+(k−2)/(2k+4)}))` with an FP^NP algorithm for odd `k`." Since `2k+4 = 2(k+2)`, the second term is **identical** and only the **sign** differs; their `k=3` value is `1.6`.

**Attribution: a VERSION SPLIT, not an error on either side.** I first recorded this as a mistake in the reviewer's spec, because TR25-049's title page reads **Xin Li and Yan Zhong, April 13 2025** -- two authors -- and the only Huang in its bibliography is `[CHLR23]`, a different paper. The reviewer corrected me back: the **ITCS 2026 version (Dagstuhl LIPIcs 362:79)** lists **"Shengtang Huang, Xin Li, and Yan Zhong"**, with a footnote recording work done while visiting Johns Hopkins. **Cite as `Li-Zhong, ECCC TR25-049 (Apr 2025) / Huang-Li-Zhong, ITCS 2026`.** W3's attribution stands as correct -- it cites the ITCS version.

**A correction I owe the reviewer.** Its spec gave Li-Zhong's algorithm as `2^{n^{1−ε/2+o(1)}}`. **Theorem 1.9** reads `2^{n^{1−ε/(k−1)+o(1)}}` -- with `k−1`, not `2`. Its number is the `k=3` instance and so correct for NC^0_3, but stated as though general. Flag C21 cuts both ways.

## §7. Flag F21 fired: the bracket is mis-shaped, not stale

**My 21c hypothesis was that the window had gone stale. It has not.** What is wrong is structural: **a window is a subtraction, and a subtraction presumes commensurable ends.** Both ends are layered.

### (7.1) The hardness end is a CURVE, not a point

> **GGNS23 Theorem 3.2.** "For every constant `1/2 ≤ δ ≤ 1`, an FP (resp. FP^NP) algorithm for degree-2-Avoid with stretch `m = 2n^{2/(1+δ)}` will provide an FP (resp. FP^NP) algorithm for finding an `(n^δ/10, n^{δ−1/2}/10)`-rigid matrix. **Furthermore, for every `1/2 ≤ δ ≤ 1`, an FP (resp. FP^NP) algorithm for NC^0_3-Avoid with stretch `m = n + O(n^{2/(2+δ)})` will provide** an FP (resp. FP^NP) algorithm for finding an `(n^δ/10, n^{δ−1/2}/10)`-rigid matrix."

So `n + n^{2/3}` is merely the `δ = 1` endpoint. Checks:

- `δ = 1` gives stretch exponent `2/3` and rigidity `(n/10, n^{1/2}/10)` -- Valiant's application, matching **GGNS23 Theorem 1** and **Valiant Theorem 2.3** ("an `(εn, n^δ)`-rigid matrix ... requires linear NC^1 circuits of size `Ω(n log log(n))`").
- Solving `2/(2+δ) = 12/17` gives **`δ = 5/6`**, which reproduces GGNS23's own remark exactly: "even an FP^NP algorithm for NC^0_3-Avoid with stretch `m = n + n^{12/17−ε}` for any constant `ε > 0` would already improve on these known constructions of rigid matrices" -- the benchmark being `[AC19, BHPT20]`'s `(2^{ε log n/log log n}, Ω(n))`-rigid matrices in polynomial time with an NP oracle.

**So the hardness side is a continuum of (stretch, payoff) pairs.** `n^{2/3}` and `n^{12/17}` are two points on one curve, not two different facts.

### (7.2) The algorithmic end is four statements, not one

| regime | threshold | source |
|---|---|---|
| FP | `m ≥ n^{k−1}/log n`, i.e. `n²/log n` at `k=3` | GGNS23 Thm 2 |
| **FP^NP** | **`m ≥ Õ(n^{1.4})`** | KPI25 Thm 3 |
| FP^NP, **conditional** | `m ≥ n^{1+γ}`, any `γ > 0` | RSW22 Conj 3.8 via Thm 3.12 |
| subexponential `2^{n^{1−ε/(k−1)+o(1)}}` | `m ≥ n^{1+ε}` | Li-Zhong Thm 1.9 |
| FP, **restricted families** | **`m = n + 1`** (monotone; symmetric) | Kuntewar-Sarma TR25-034 |

The last row matters: **restricted NC^0_3 families are already solved at minimal stretch**, inside the hardness end's own regime.

### (7.3) Why this is not a window

The payoff lives at `m = n + n^{≤0.706}`; the unconditional algorithms live at `m ≥ n^{1.4}`. **Moving the algorithmic end from `n^{1.4}` to `n^{1.2}` to `n^{1.01}` buys nothing for rigidity** -- the reduction does not fire until the stretch is *additive*. In additive-stretch exponent the gap is roughly `(0.71, 1.4)`, a factor of two, and nothing converges until an algorithm actually crosses into `n + n^{o(1)}...n + n^{2/3}`.

**Li-Zhong say as much themselves:** "most interesting explicit construction problems only reduce to `C`-Avoid with very small stretch. For example, in the case of NC^0-Avoid, to show a better circuit lower bound, one needs `m = n + n^{o(1)}`; while finding rigid matrices enough for Valiant's application needs `m = n + n^{2/3}` [GGNS23]."

### (7.4) A commensurability trap I nearly walked into

**Li-Zhong Theorem 1.2** gives a *stronger* payoff at small stretch: "For any constant `δ ∈ (0,1)` and any integer `i`, `NC^i-Avoid[n, n + n^δ] ∈ FP^NP ⟹ E^NP ⊄ i.o.-NC^{i+1}-SIZE[o(2^n/n)]`." It is tempting to fold this into the hardness end and declare the payoff far stronger than rigidity. **Their footnote 6 forbids it:** *"In the case of `i = 0`, the results apply to NC^0_4-Avoid."* **That route is NC^0_4, not NC^0_3** -- a different object from (S2), and folding it in would have been exactly the error F21 exists to catch.

## §8. The reviewer's questions

**(i) The algorithmic end is limited by the cell-probe bound itself -- and the improvement is barriered.**

> **KPI25 Theorem 5(2).** "If there is a universal constant `ε > 0` and an explicit data structure problem `F : [N] × [M] → {0,1}` with `M = poly(N)` requiring space `S ≥ N^ε` for nonadaptive data structures making `O(1)` bit probes, then there is a polynomial time NP oracle algorithm for NC^0 range avoidance with polynomial stretch."

They add that this conclusion "was directly posed in [RSW22] as an important direction in unconditional range avoidance algorithms". But:

> **KPI25 Theorem 6(2).** "Assume existence of polynomial stretch NC^0 PRGs. Then for every `ε > 0` there is `t ∈ N` so that no natural proof can establish a lower bound `S ≥ N^ε` for data structures making `t` nonadaptive bit probes solving a problem `F : [N] × [poly(N)] → {0,1}`."

**A Razborov-Rudich barrier sits on precisely the improvement Theorem 5(2) would consume.** So: the bound, not the correspondence's loss.

**(v), which bears on (i): the bound is tight.** "By known constructions [Sie89, Sie04] ... the lower bound in Theorem 1 is tight up to `log N` factors and the factors depending only on `w` provided `t` is not too large", and "the tightness of Theorem 1 holds **even in this restricted setting of nonadaptive bit probe data structures**". *(Honest caveat they state themselves: they do not know whether Theorem 2's small-bias bound can be made natural, so "it is unclear at the moment whether or not the 'natural properties barrier' ... has already been broken by the new results in this paper.")*

**(ii) The hardness end is limited by the rigidity target, not the perfect-encoding step.** **This was my §2(b) disclosure, made before reading, and it is confirmed.** GGNS23 **Lemma 2.7** is a generic degree-`d` to `NC^0_{d+1}` reduction -- "there is a polynomial time reduction from degree-`d`-Avoid to `NC^0_{d+1}`-Avoid" -- independent of `δ`, and Theorem 3.2 runs cleanly across the whole `δ ∈ [1/2, 1]` range. What binds is **which `(r,s)` you need**: `δ = 1` for Valiant, `δ = 5/6` merely to beat the known NP-oracle constructions.

**(iii) One statement per end.**

- **Algorithmic:** an **FP^NP derandomisation of hypergraph cut sparsifiers.** RSW22 **Theorem 3.12** makes Conjecture 3.8 follow from FP^NP-computable CSP sparsifiers, and PZ21's construction "only uses the hypergraph cut sparsifiers in [BST19] as a black box, and thus is computable in randomised polynomial time". **This is concrete and, unlike the cell-probe route, not barriered** -- which makes it the better target of the two.
- **Hardness:** nothing about Avoid at all. It would have to be an improvement to **Valiant's implication itself** -- weaker rigidity sufficing for super-linear linear-NC^1 lower bounds.

## §9. Scoring

| code | mine | reviewer | outcome |
|---|---|---|---|
| **21a** | 10 | 8 | **Did not fire.** No new algorithm and no extension of the reduction; Flag D21 never armed. |
| **21b** | 60 | 60 | **The outcome.** Both ends pinned to named quantities: hardness as GGNS23 Thm 3.2's `δ`-curve with `(n^δ/10, n^{δ−1/2}/10)`; algorithmic as KPI25 Thm 3's `t/2 − (t−2)/(2(t+2))`, with the 3-probe bound's tightness answered. |
| **21c** | 30 | 32 | **Partial, and my stated reason was wrong.** I priced it on the window being **stale**. It is not stale -- it is **mis-shaped**. The category was right for a reason I did not name. |

## §10. Calibration

**§2(b) was right, and it is worth recording that it was a *positive* prediction.** I predicted before reading that the hardness end is limited by the rigidity target rather than the encoding. Confirmed by Lemma 2.7 and Theorem 3.2's `δ`-range. **The standing asymmetry holds: my constructions and positive structural predictions land; my doubts do not.**

**My 21c reasoning failed in a new way, and it is not the W20 failure mode.** In W17 and W20 I overpriced the "other" bucket on a **named mechanism** that later lost its framing. Here I had **no mechanism** (§2(c)) and priced on a **base rate** -- "active area, the number may be stale." The number was not stale. But the bucket was still partly right, because the *shape* was wrong. **So a base-rate justification can be right about the bucket and wrong about the reason**, which is a weaker form of the W20 lesson rather than a repeat of it: the framing audit does not just decide whether a mechanism survives, it can be *the finding itself*.

**Flag F21 earned its place.** It was written as a guard against pricing a gap between two different objects, and it produced the round's main content, twice: the `δ`-curve, and Li-Zhong Theorem 1.2's footnote-6 restriction to NC^0_4.

**Impossibility-claim record unchanged at ten.** This round produced no impossibility claim of mine.

> **New practice line, earned twice now: when two careful readers disagree about an author list or a theorem number, suspect a VERSION SPLIT before suspecting an error.** W19: I found the reviewer's "SU05 Theorem 3.16" at Theorem 4.10 and recorded it as a mis-citation; it was the CCC'05 conference numbering against the journal's. W21: I found its "Huang-Li-Zhong" listed as Li-Zhong and recorded it as a mis-attribution; it was the ITCS 2026 version against the ECCC revision. **Both times the disagreement was real, both times "someone transcribed it wrong" was the wrong diagnosis, and both times the fix is a dual citation rather than a correction.** The general form: a bibliographic disagreement between two readers who have each checked a source is evidence about *editions*, not about care.

## §11. What this leaves open

1. **The gap itself**, correctly stated: no unconditional algorithm is known at any *additive* stretch `m = n + n^{o(1)} … n + n^{2/3}` for general NC^0_3, while restricted families (monotone, symmetric) are solved at `m = n+1`.
2. **RSW22's Conjecture 3.8 -- and this is the round's deliverable, stated exactly, because it is the one unbarriered statement found.**

   > **Conjecture 3.8** (verbatim). "For every constant `c ≥ 1` and `γ > 0`, let `C` be the class of functions with `n` input bits and `n^{1+γ}` output bits where each output bit depends on at most `c` input bits. Then there is an FP^NP algorithm for `C`-Avoid."
   >
   > **Theorem 3.12** (verbatim). "Suppose that for every constant `k ≥ 1`, there is an **FP^NP algorithm** that given any `k`-uniform directed hypergraph `G` and any predicate `P : {0,1}^k → {0,1}`, outputs a `P`-sparsifier of `G` with error `ε = 0.5` using `Õ(n)` hyperedges. Then for every constants `γ > 0` and `c ≥ 2`, there is an FP^NP algorithm for `C`-Avoid, where `C` is the family of `NC^0_c` circuits with stretch `n^{1+γ}`."

   **Precisely what must be derandomised**, from Definition 3.9: a `k`-CSP is a `k`-uniform **directed** hypergraph `G = (V,E)` plus a predicate `P : {0,1}^k → {0,1}`, with `value_{G,P}(α) := (1/|E|) Σ_{(v_1..v_k) ∈ E} P(v_1,...,v_k)`; a sub-hypergraph `G' = (V, E' ⊆ E)` is a **`P`-sparsifier with error `ε`** if `|value_{G',P}(α) − value_{G,P}(α)| ≤ ε` **for every assignment** `α : V → {0,1}`. So the object is: **for each constant `k` and each predicate `P`, an NP-oracle algorithm outputting `Õ(n)` hyperedges preserving the satisfied fraction to within additive `0.5`, uniformly over all assignments.**

   **Why it is live rather than hopeless.** RSW22's Remark 3.10 notes their definition is **weaker** than PZ21's ("using a weaker definition of sparsifiers makes it potentially easier to construct them"), and the known construction is randomised: **Theorem 3.11 ([PZ21])** gives "a randomised polynomial-time algorithm ... outputs a `P`-sparsifier of `G` with error `ε` using `O(n ε^{−2} log(1/ε))` hyperedges", built on `[BST19]` hypergraph cut sparsifiers **as a black box**. Deterministic **spectral** sparsifiers for graphs are known (Batson-Spielman-Srivastava); **whether the hypergraph/CSP case admits a deterministic or FP^NP construction is the open question**, and it is an algorithmic question with no natural-proofs barrier attached -- unlike the cell-probe route of §8(i).

   **This is the reviewer's proposed W22 target, and it survives my framing audit**: the object is fully specified, the sufficient condition is a theorem rather than a hope, and the gap is a derandomisation rather than a lower bound.
3. **Whether Theorem 2's small-bias cell-probe bound is natural** -- KPI25 explicitly do not know, and it decides whether their own work has already crossed the barrier of Theorem 6.
4. **(S2) remains off the door** (Flag E21). Nothing here touches (C_1).
