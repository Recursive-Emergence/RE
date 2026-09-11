# Y1′: do known NP-hardness reductions land in the low-depth promise? Report

*Run 2026-09-11 on branch `y1-adversary`, on the author's go ("Run Y1′, push after merge"), against the pre-registration (b80209d) and the reviewer's ruling (30b6032): Y1′ replaces Y1, with the shape (a)–(d) per reduction and priors Y1′b 55/60, Y1′c 40/38, Y1′a 5/2 (reviewer/mine). Documents only; `formal/` closed.*

*Sources read as text this run:*
- *Liu–Pass CCC'22 (LP22, local `lp22b.txt`): §1.2, §2.3, §3.1–3.2;*
- *Hirahara FOCS'22 (Hir22, ECCC TR22-119): Theorem 1.2, the §2 overview, Definition 8.4, Theorem 8.5;*
- *Liu–Pass TR23-103 (LP23) and ePrint 2025/2184 (LP25), as cited in the pre-registration.*

*g5 applies to every depth bound. "Exact" means proved here from the cited statements.*

## 0. Outcome

**Y1′c (mixed), and the failure is not where either side predicted.** Both reviewed reductions leave the promise on the **NO side first, by threshold**, not on the YES side by depth. For LP22, depth *also* fails, on both sides.

| reduction | target problem | NO side vs "K^t ≥ \|x\| − 1" | depth (YES and NO outputs) | verdict |
|---|---|---|---|---|
| **LP22** (McK^tP[ζ], Theorem 1.2) | conditional K^t(x \| z), gap at the low end | **fails, proved:** every output has K^t(A \| z) ≤ λn + O(log n) = O(n log n), against \|A\| = n⁴. Padding cannot repair it (§2.2). | **fails on both sides, proved:** depth ≥ ℓ*(log r + 2·log t(nm) − 1) − O(λ), which is Ω((n/γ)·log n), against β·log K = O(β log n), with probability ≥ 1 − 2/n (§2.3) | outside Q^t_β and outside the NO set on every output |
| **Hir22** (MINKT\*, Theorems 1.2 and 8.5) | K^t of *partial* strings, factor-(log N)^α gap | **certified only** a (log N)^α factor above the YES threshold s ≥ n^{Ω(1)}. Nothing in the reduction makes NO outputs near-maximal (§3). | **not determined** by the texts read | problem-shape mismatch: LP23's promise is stated for total strings, and no partial-string analogue is stated |
| Ilango's reductions | — | not checked separately: LP22's construction *is* Ilango's set-cover-with-random-strings construction, with the oracle moved into z (LP22 l.273–305) | — | covered structurally by LP22 |

**The named obstruction: the random-NO requirement.**
- LP23's promise problem MK^tP[s] fixes **NO = {K^t ≥ |x| − 1}** for every threshold s (l.222–224; also Theorems 1.4 and 1.5). An OWF-complete problem must separate *structured* strings from *random* ones.
- Every NP-hardness reduction read separates **structured from less structured**: both YES and NO outputs have short descriptions built from the instance plus the reduction's keys.
- **No reduction read produces random NO instances.** That, not YES-side depth, is the first gap between the known NP-hardness results and LP23's door.
- LP22 adds a second gap: its hardness mechanism, "z is an obfuscation that a t-time program cannot scan", **is** computational depth. So LP22's outputs are deep by design.

**Priors.**
- Y1′c (mixed): reviewer 40, mine 38. **This is the outcome.**
- Y1′b (every reduction fails on the YES side by depth): reviewer 55, mine 60. **Wrong premise on both sides:** the failing side is NO (threshold), and the YES-side depth failure holds for LP22 only.
- Y1′a: 5 / 2. Not reached.

## 1. The smallest case and the kill tests (§(d) of the ruling)

**The identity on random strings lands in the promise (exact).** Let x be uniform on {0,1}^n.
- K^t(x) ≥ K(x) always.
- K(x) ≥ n − c with probability ≥ 1 − 2^{−c}.
- K^t(x) ≤ n + O(1) (the program that prints x, as in LP22 Fact 2.3).
- So depth(x) = K^t(x) − K(x) ≤ c + O(1). With c = β·log(n/2), x ∈ Q^t_β with probability ≥ 1 − O(n^{−β}).
- It is a NO instance of MK^tP[s] with probability ≥ 1/2 (K^t ≥ K ≥ n − 1).
- ✓ The promise is not empty on the NO side, as it must not be.

**A reduction whose YES outputs are all deep: LP22 is one** (§2.3), so the ruling's kill test fires there. Its NO outputs are deep as well.

## 2. LP22 (conditional K^t), per the ruling's (a)–(c)

**The construction (verified, §3.1, l.698–760).** From a γ-bounded set-cover instance (1^n, 1^ℓ, S = {S₁, …, S_r}):
- Take m = n³ and random A = A₁‖…‖A_n ∈ {0,1}^{n·m}.
- Gadgets W_i reveal A_j for j ∈ S_i and are 0^m elsewhere. Keys k_i are random in {0,1}^λ, with λ = 4·log r + 4·log t(nm).
- z has 2^λ blocks of length nm, with z_{k_i} = W_i and **every other block all-zero**.
- The instance is (A, z, 2λℓ).
- Prop 3.3 (verified): cover([n], S) ≤ ℓ ⇒ K^t(A | z) ≤ 2λℓ.
- Prop 3.4 (verified): with probability ≥ 1 − 2/n over the keys and A, K^t(A | z) ≤ 2λℓ ⇒ cover ≤ 4ℓ.
- **A, z and λ do not depend on ℓ.** Only the threshold does, so Prop 3.4 may be applied at any ℓ′ on the same (A, z).

Let ℓ* := cover([n], S). Assume S covers [n] (otherwise the reduction can reject outright), so ℓ* ≤ n, and ℓ* ≥ n/γ.

### 2.1 An unbounded (indeed polynomial-time) upper bound: K(A | z) ≤ ℓ*·⌈log r⌉ + O(log n) (exact)

The program is given n, m, λ (O(log n) bits) and the **ranks** ρ₁, …, ρ_{ℓ*} ∈ [r] of a minimum cover's gadgets among the nonzero blocks of z, sorted by position (ℓ*·⌈log r⌉ bits). It:
1. scans z;
2. lists its nonzero blocks in order (the W_i with S_i ≠ ∅, since empty S_i give zero gadgets that no minimum cover uses);
3. outputs the bitwise OR of the blocks with ranks ρ₁, …, ρ_{ℓ*}.

That OR is A, exactly as in Prop 3.3's proof. The running time is Õ(|z|) = poly(n, r). **So even K^{poly}(A | z) ≤ ℓ*·⌈log r⌉ + O(log n)**, and the bound survives LP23's remark that K may be replaced by K^{EXP} (l.244–246). ∎

### 2.2 The NO side: every output is compressible (exact; padding does not help)

- **Upper bound.** Apply Prop 3.3's program to a cover of size ℓ* ≤ n. It runs in time O(ℓ*·nm·polylog) ≤ t, so K^t(A | z) ≤ λ·ℓ* + O(log n) ≤ λn + O(log n) = 4n(log r + log t(nm)) + O(log n) = **O(n log n)**.
- **Comparison.** |A| = n⁴. So **no output is in the NO set {K^t(A | z) ≥ |A| − 1}**, YES or NO alike. LP22's "No" means K^t > 2λℓ, a *low-end* threshold.
- **Padding.** Let x′ = A‖R with any R. Then K^t(A‖R | z) ≤ K^t(A | z) + |R| + O(log n) ≤ |x′| − (n⁴ − O(n log n)), which is never ≥ |x′| − 1. ∎
- **Absorbing z into the instance** (an unconditional reading) is worse: z is all-zero outside r blocks, so K(z) ≤ r·(λ + n·m) + O(log n) ≪ |z|.

### 2.3 Depth: every output is deep (exact, with probability ≥ 1 − 2/n)

**Lower bound on K^t.** Apply Prop 3.4 at ℓ′ := ⌈ℓ*/4⌉ − 1, so that 4ℓ′ < ℓ*. On the event of probability ≥ 1 − 2/n, K^t(A | z) ≤ 2λℓ′ would give a cover of size ≤ 4ℓ′ < ℓ*, a contradiction. So
  K^t(A | z) > 2λℓ′ ≥ λℓ*/2 − 2λ.

**Depth, with §2.1:**
  K^t(A | z) − K(A | z) ≥ λℓ*/2 − 2λ − ℓ*·⌈log r⌉ − O(log n) ≥ ℓ*·(log r + 2·log t(nm) − 1) − O(λ + log n),
using λ/2 = 2·log r + 2·log t(nm).

**Numbers** (t ≥ n², so t(nm) ≥ n⁸; ℓ* ≥ n/γ): depth ≥ (n/γ)·(16·log n + log r − 1) − O(log n).

**The promise needs** depth ≤ β·log K(A | z) ≤ β·log(n·⌈log r⌉ + O(log n)) = O(β·log n). The ratio is Ω(n/(γβ)), so **every output, YES and NO, is outside the conditional analogue of Q^t_β for every β = o(n/log n).** ∎

**Re-derived a second way (the mechanism).** LP22's own intuition (l.313–330) is that a t-time program "can only access S_i if it 'knows' the random location", because |z| ≫ t. An unbounded program scans z instead of knowing locations. The cost of *locating* a gadget is λ bits under the time bound and ⌈log r⌉ bits (its rank) without it. The saving per cover set is at least λ/2 − ⌈log r⌉. **So the hardness is exactly computational depth**, and the obfuscation *is* the depth.

### 2.4 The ruling's (c): the modification that would be needed
- **NO side.** NO outputs would need K^t(x) ≥ |x| − 1. In LP22 the random mass A is always generated from z at cost O(n log n) (§2.2), in YES and NO alike. A fix would have to make the randomness **witness-compressible in YES and incompressible in NO**, i.e. an NP-hard problem whose NO instances are random. Padding cannot do it (§2.2).
- **Depth.** A fix would have to make locating a gadget as expensive for unbounded programs as for t-time ones. That removes the obfuscation on which Prop 3.4 rests. **Not consistent with LP22's proof as it stands.**

## 3. Hir22 (MINKT\*, partial strings), per (a)–(c)

**The problem (verified, Definition 8.4, l.1690).** MINKT\* = {(x, 1^t, 1^s) : x ∈ {0,1,∗}^n and some y consistent with x has K^t(y) ≤ s}.

**The reduction (verified, Theorem 8.5, l.1692–1700).** It outputs a partial function f : {0,1}^{log N} → {0,1,∗}, with N = n^{O(1)}, from an example distribution E with poly-time-enumerable support. It is NP-hard to approximate within a factor (log N)^α.
- YES has s ≥ n^{Ω(1)} (l.1253), with a program of size (1 + o(1))·θλ that holds the keys {f_i : α(i) = 1} (l.1294).
- The construction is sketched in the overview (l.586–600): x = (j, z, NW(Enc(f_{v₁}); z_{S₁}) ⊕ s₁, …), with the secret b shared by ϕ_j.

**(a)/(c) NO side.**
- NO is certified only as "no program of size s·n^ε (Theorem 1.2), or within a factor (log N)^α (Theorem 8.5), computes f": a polynomial or polylog factor above the YES threshold.
- *From the overview's construction (not re-derived from §8):* every output is computed by a program holding all n keys f_i and the instance Φ, so its complexity is bounded by nλ + |Φ| + O(log n) regardless of YES/NO.
- Whether that is below the number of defined points depends on |supp E|, which the overview does not state. **So the NO-side threshold failure is expected but not verified for Hir22.**

**(b)/(c) Depth.** Not determined from the texts read. The proof's compression arguments (NW as a one-time pad against a program that "does not know" f_i, l.26–31) bound *time-bounded* knowledge. Whether the unbounded K of a completion is much smaller (a depth gap) would need §7–8's exact encoding. **Recorded as missing.**

**Shape.** LP23's promise and characterization are stated for total strings (MK^tP), and neither LP23 nor LP25 states a partial-string analogue. So even a favourable depth analysis would land in a problem not known to characterize OWF.

## 4. What the door needs, stated exactly

By LP23's Theorem 1.1, the missing object is a randomized reduction R from SAT with outputs x = R(φ; ρ) such that:
1. YES: K^t(x) ≤ s;
2. NO: **K^t(x) ≥ |x| − 1** (random);
3. every output is non-deep: K^t(x) − K(x) ≤ β·log K(x).

**Flag D, generalized (exact).** K^{poly}(x) ≤ |φ| + |ρ| + O(log n). So condition 2 needs |ρ| ≥ |x| − |φ| − O(log n): the reduction must inject nearly |x| random bits that **stay incompressible on NO instances and become compressible via the witness on YES instances.**

**The two reductions read fail condition 2** (LP22 proved; Hir22 expected), and **LP22 fails condition 3 by construction.**

**Reading (not a theorem).** Condition 2 is compressibility versus density once more: NO instances must be dense (random), and reductions output compressible strings. This is its sixth appearance on the record, now at the *output* of NP-hardness reductions, after R2's density barrier, R5's S3/S4 tension, X-series naming, and LP23's depth promise (Y1). LP23 (l.386–392) says no barrier is known. This run does not find one either. It finds that **no existing reduction is shaped to satisfy condition 2**.

## 5. Misses and scoring

- **Joint wrong premise (both priors):** Y1′b placed the failure on the YES side (depth). The robust failure is on the NO side (threshold), and it is visible from LP23's l.222–224 definition beside LP22's Prop 3.3. The pre-registration's Flag D *did* point at the NO side ("NO outputs need K^t ≥ n − 1"), but only for deterministic reductions, and the priors did not follow it. The reviewer's ruling moved the risk to the YES side. **Scored as the reviewer rules.**
- **The practice line applied:** each bound was put beside LP23's definition (NO = n − 1) and beside the reduction's own Propositions before it was called a finding.

## Ceiling

Y1′ proves nothing about P vs NP or OWF. It locates the gap between existing NP-hardness reductions and LP23's OWF-complete promise problem: **random NO instances (condition 2), and non-deep outputs (condition 3, which LP22 violates by design).**

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as Y1′c on the report.** Merge b10f520; push on the author's standing go; then the final-page update.

**Scoring.** A joint wrong premise (the YES side): the reviewer's thirteenth. My Flag D pointed at the NO side for deterministic reductions, and neither prior followed it. This is recorded as **the practice failing in a new way: a flag's implication was not carried into the prior.**

**The finding, for the page's §3 and Y2's §0.** LP22's outputs are deep by design. Its hardness is "a t-time program must know the random location", and a hidden location is precisely K^t − K. So the mechanism by which the known reductions achieve NP-hardness (planted hidden structure) is the mechanism the low-depth promise Q^t_β excludes.
- If that is general, it is a barrier for the holy grail via planted-structure reductions, and proving it would be a real theorem.
- If it is not general, the escape is a reduction whose hardness does not come from hiding.

**Y2 ("hiding is depth: barrier or construction")** is named, for the author's go, as a pre-registration for ruling.
