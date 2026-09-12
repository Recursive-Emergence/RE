# W26: the query-versus-fan-in tradeoff. Pre-registration

*Drafted 2026-09-12 on branch `w26-query-fanin` (from `w25-read-count` at ff2f888), on the reviewer's W26 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE any run and before re-reading any primary for this round -- including Korten's Definition 9 and the W8.1 / W12.2 statements, which this page quotes only from W14's committed summary line.**

## §0. Target and ceiling

**Membership-query model, deterministic, depth 1, stretch `n ↦ n+1` to `n ↦ n+2`, `n′ = n`.** Glue fan-in `k`. By W25.2, totality is static set certification: `y ↦ V(y)`, `|V(y)| ≤ q + 1`, and every `C` with `V(y) ⊆ range(C)` has `y ∈ range(C′)`.

**Known endpoints.** `k = N`: `q ≤ 5` for all `N ≥ 16` (W25.3). `k = 1`: `q = Ω(N)` -- **if** the DNF-model theorems transfer (§2(a)).

**Candidate forms (the reviewer's):** (F1) `q·k = Ω(N)`; (F2) `q²·k = Ω(N)`; (F3) `q = Ω(log N / log(N/k))`.

**Ceiling.** Nothing about P vs NP; nothing randomised (Flag H7); the black-box question itself lives at `k = poly(n) = polylog N`, so **only the small-`k` end of any tradeoff bears on the line** -- a tradeoff that is loose at large `k` but tight at `k = polylog N` answers what the line needs.

## §1. Governing lines

W25's practice line binds first: **price every resource a statement quantifies over before counting under it** -- here `k`, `q`, and the size of each window's view. Also standing: framing audit precedes mechanism pricing; a verified premise does not license its consequence; calibration asymmetry indexed to source; eleven wrong impossibility claims on my record, and W25.3 was a *positive* construction that held.

## §2. Disclosure and counting done before the prior

**(a) THE ENDPOINT TRANSFER, unverified.** W8.1 (single-call, `qw ≥ N − 1`) and W12.2 (one-input patterns, arbitrary per-coordinate glue, `qw ≥ N/9`) are proved in Korten's Definition 9 / Wilson Theorem 12 DNF model. **A membership query "`v ∈ range(C)`?" is the DNF `OR_x [C(x) = v]`, whose terms have width 1** -- so if Definition 9's `w` is term width, membership is a special case, `w = 1`, and the DNF lower bounds transfer DOWN: `q = Ω(N)` at `k = 1` in the membership model. **I have not re-read Definition 9 for what `w` measures.** The reviewer's "W8.1's model might be stronger than membership" is the other horn; this audit decides it, and it runs first.

**(b) IF (a) HOLDS, F2 AND F3 ARE ALREADY DEAD AS TIGHT FORMS.** At `k = 1`, F2 gives `q = Ω(√N)` and F3 gives `Ω(1)`, both below the known `Ω(N)`. They survive only as (true but loose) lower bounds. **Only F1 matches both endpoints -- but it is not the only form that does**: `q·k² = Θ(N)` and threshold shapes (`q = Θ̃(N)` for all `k ≤ N^{1−ε}`, collapsing near `k = N`) also match. So "F1 is the truth" competes with more than F2 and F3.

**(c) A PLACEMENT ARGUMENT I SEE, stated as a sketch and not priced as proof.** The windows form a hypergraph on inputs (`N` windows of size `k`). An input co-occurs with at most `Σ_{windows containing u} k` others -- `k²` **on average**, not per input (W25's lesson: hubs). If the adversary can place the `q + 1` elements of `V(y)` on inputs pairwise sharing no window -- greedily possible for `q + 1 ≲ N/k²` on a regular window system -- then **every window sees at most one element of `V(y)`**, and the reviewer's precision argument has to handle views of size one. This suggests `q·k² = Ω(N)` for **regular** window systems and says nothing for hub-heavy ones, where the independent placement fails. **So I expect the fan-in's *distribution* (max co-occurrence), not just `k`, to enter the true statement.**

**(d) The reviewer's precision derivation, checked in advance for W25-type premise errors.** "A window must see at least two elements of `V(y)` before it may output `y`" is derived "on average" over hints from the output budget `N`; an average bound on `j` gives coverage only for most hints, and the pair-sharing probability `C(q+1, 2)·k/N` assumes **random** placement, whereas the adversary places adversarially (which helps the lower bound) and the template chooses windows (which can concentrate co-occurrence, which hurts it). Registered as two places to check, not as errors.

**(e) Construction side, what I see.** Block-local windows see `C(B_j)`, a `k`-subset of `2N` strings; certifying `V(y) ⊆ range(C)` is global. A hypergraph trick per block (W25.3 locally) certifies `V(y) ⊄ C(B_j)`, not `V(y) ⊄ range(C)`. **I have no construction below `q = Θ(N)` for any `k = o(N)`**, which is weak evidence for a threshold shape and against F1 being tight at intermediate `k`.

## §3. Priors, fixed now

Forms, read as "the tight tradeoff is `Θ̃` of this, over all `k`":

| form | reviewer | **mine** |
|---|---|---|
| F1 `q·k = Θ̃(N)` | 45 | **35** |
| F2 `q²·k` | 30 | **5** -- dead at `k = 1` if §2(a) holds |
| F3 | 15 | **2** -- same |
| other (`q·k²`, threshold, distribution-dependent) | 10 | **58** |

Outcomes:

| code | reviewer | **mine** |
|---|---|---|
| **26a** a proved tradeoff in one form | 15 | **12** |
| **26b** located between two forms, gap named | 60 | **58** |
| **26c** nothing | 25 | **30** |

**Why "other" at 58.** §2(b) removes F2/F3 as tight forms before any run if the transfer holds (I put the transfer at ~85); §2(c) and §2(e) both point at shapes not on the reviewer's list. **Why 26c above the reviewer:** §2(e) -- I see no construction below `Θ(N)`, and without one the tradeoff cannot be *located*, only bounded from one side.

## §4. Flags

- **A26 -- transfer audit FIRST** (§2(a)): read Korten Definition 9 / Theorem 12 for what `w` measures, and W8.1 / W12.2 from their committed pages.
- **B26 -- membership model on every line**; W25.2's all-yes collapse used explicitly wherever totality is checked.
- **C26 -- averages vs maxima**: every co-occurrence or reader count is stated as average or maximum, never unlabelled (W25's two premise errors).
- **D26 -- construction side before lower-bound pricing**: search block templates at n = 3 with a **graded** score, positive control first (K_{4,4}-style at `k = N` must score 0).
- **E26 -- stop-rule**: any construction with `q·k = o(N)` at intermediate `k` -> stop and send before writing.
- **F26 -- re-derive, never recall.**

## §5. Kill tests

- (i) A26 discharged in writing before pricing F2/F3.
- (ii) Positive control scores 0 at `k = N` before any bounded-`k` search is read.
- (iii) Search scores graded, never 0/1 (W25 §10's flat-score miss).
- (iv) The placement sketch (§2(c)) checked on a hub-heavy window system, where it should fail.
- (v) If the resolution is not the pre-registered one, say so in the same sentence.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §5A. Amendment -- Flag A26 discharged (after the priors commit da60556, before any run)

**Read from the committed pages** (W8 §2 quotes Definition 9 and Theorem 12's adversary verbatim; W12's statements via W14's summary line):
- Definition 9: *"may choose at each step a DNF D over the variables {α_i}, and receive its value"*; *"the 'width complexity' of Q is the maximum width of a DNF it queries"*. Theorem 12's adversary extends `ρ : [N] → [M]` *"on at most w additional inputs"* per true term.
- **So width counts inputs**, and a membership query `OR_x [α_x = v]` has width 1: **the membership model is Definition 9 at `w = 1`, and the DNF lower bounds transfer DOWN.** *One wording gap, recorded:* W8's model line says *"width-w DNF over the oracle's bits"*. If the variables are bits, `[α_x = v]` has width `n + 1`, and the transferred bound loses a `log N` factor. **Either way `q = Ω̃(N)` at `k = 1`**, so the reviewer's other horn ("W8.1's model is stronger than membership") does not hold.
- **The `k = 1` endpoint is W12.2, not W8.1.** W8.1 is only the template `(C(x), h(x))`. W12.2 (one input per coordinate, arbitrary per-coordinate glue, `qw ≥ N/9`) covers general fan-in-1 glue -- **and more: coordinates may read DIFFERENT inputs, so W12.2 already reaches total fan-in `n + 2 = log N + 2` under the per-coordinate one-input restriction.** So for that structured class, `q = Ω̃(N)` holds at `k = Θ(log N)`, which is inside the line's `k = poly(n)` range.

**Consequences, exactly as §2(b) registered.** F2 and F3 are **dead as tight forms** (they sit below `Ω(N)` at `k = 1`) and survive only as loose lower bounds. **The live question at the line's scale:** does `q = Ω̃(N)` survive when a window of `k = polylog N` inputs is read by **joint** glue, not per-coordinate projections? W12.2 is the per-coordinate case; W25.3 shows joint glue at `k = N` collapses `q` to `O(1)`. **Where between `k = log N` (joint) and `k = N` the collapse starts is the tradeoff.**

---

# W26 Findings

*Appended after the reviewer audited every step of the proof and accepted it. Nothing above is revised.*

## §6. Ceiling -- FIRST

**Membership-query model only, deterministic, depth 1, `n′ = n` (stretch `n ↦ n+1` to `n ↦ n+2`).** A membership query is *"is `v ∈ range(C)`?"* = `OR_x [α_x = v]` with **one** value `v` at every `x`.

**Correction to §5A, the reviewer's.** §5A said "the membership model **is** Definition 9 at `w = 1`". **Too strong.** A width-1 DNF may name a **different value at each input**, `OR_x [α_x = v_x]`. A "no" to such a query excludes no single string, so it is not a win for Q, and W25.2's all-yes collapse fails for it. Correctly: **the membership model is the single-value subclass of width-1 DNFs.** Definition 9 lower bounds transfer **down** to it (§5A's conclusion about the `k = 1` endpoint stands). **W26.1 does not transfer up, not even to width 1.** It says nothing about NP^C queries, hence nothing about `FP^NP`, and nothing about Korten's Problem 1 as posed. Nothing randomised (Flag H7).

## §7. Outcome against priors

| code | mine / reviewer | outcome |
|---|---|---|
| **26a** a proved tradeoff | 12 / 15 | **achieved -- Theorem W26.1, in a form on nobody's list** |
| 26b located between forms | 58 / 60 | -- |
| 26c nothing | 30 / 25 | -- |

Forms: F1 35 / 45 (reviewer later 30), F2 5 / 30, F3 2 / 15, **other 58 / 10 (reviewer later 63)**. **The proved form, `q·k = Ω(√N)` ("F4"), falls under "other".** The mechanism is not the one I pre-registered: I registered a placement argument (§2(c)) and no lower-bound mechanism, and the proof came from pricing the reviewer's precision idea exactly. **The placement sketch was a detour.** The reviewer's position-pair count (`≤ N·C(k,2)` co-located pairs for ANY window system) shows hubs cannot raise co-location, and the proof never needs co-location at all.

## §8. Theorem W26.1

> **Theorem W26.1.** *In the membership-query model, let `C′` be a depth-1 template from stretch `n ↦ n+1` to `n ↦ n+2` (`N = 2ⁿ`) whose every C′-input applies ARBITRARY glue to at most `k` values of `C`. If a deterministic back-mapping with `q` membership queries is correct on every hint, then*
>
>   **`(q + 1) · k ≥ 0.58 · √N`.**

*Proof.* Let `s = q + 1`.

**(1) Static sets.** By W25.2, a total Q has, for each hint `y`, a set `V(y)` of `≤ s` strings (its queries plus its output under all-yes) such that **every `C` with `V(y) ⊆ range(C)` has `y ∈ range(C′)`.** This holds for **any** total Q, not only an optimal one: if some `C` had `V(y) ⊆ range(C)` and `y ∉ range(C′)`, all-yes would be truthful for that `C` and Q's output would lie in the range. **Pad `V(y)` to size exactly `s`**; the implication survives. **The implication holds for all `4N` hints**, vacuously for a never-valid one.

**(2) Distribution and coverage.** Let `C` be a uniformly random injection onto a uniformly random `N`-subset `R` of the `2N` strings, and `p_s = Pr[fixed s-set ⊆ R] = Π_{i<s} (N−i)/(2N−i)`. Summing the implication over hints, and using that each window outputs exactly one hint per view:
  `4N · p_s ≤ Σ_y Pr[y ∈ range(C′), V(y) ⊆ R] ≤ Σ_{x′} E_view[ Pr[V(g_{x′}(view)) ⊆ R | view] ]`.

**(3) Precision, exact.** Let `S` be the set of values in the view and `j = |V(y) ∩ S|`. Given the view, `R \ S` is a uniform `(N−k)`-subset of the `2N − k` unseen strings, so the other `s − j` elements all lie in `R` with probability `Π (N−k−i)/(2N−k−i) ≤ 2^{−(s−j)}`. Hence each window contributes `≤ 2^{−s} · E[max_y 2^{j_y}]`.

**(4) A window seldom sees two elements.** Pointwise, `max_y 2^{j_y} ≤ 2 + Σ_{y : j_y ≥ 2} 2^{j_y}`. `S` is a uniform `k`-subset of `[2N]` (repeated inputs only shrink it), so `Pr[j_y ≥ j] ≤ C(s,j)(k/2N)^j`. By Abel summation, `E[2^{j_y} 1(j_y ≥ 2)] ≤ Σ_{j≥2} C(s,j)(k/N)^j = (1 + k/N)^s − 1 − sk/N ≤ (sk/N)²` for `sk ≤ N` (from `e^t ≤ 1 + t + t²` on `[0,1]`). Over `4N` hints: `E[max_y 2^{j_y}] ≤ 2 + 4s²k²/N`.

**(5) Combine.** `2^{−s}/p_s = Π (2N−i)/(2N−2i) ≤ exp(s²/2N)` for `s ≤ N/2`. So
  **`4N ≤ (2N + 4s²k²) · e^{s²/2N}`.**
Split at `s² = 0.34N`. If `s² ≤ 0.34N`, then `4s²k² ≥ 4N·e^{−0.17} − 2N`, so `sk ≥ 0.586√N`. Otherwise `sk ≥ s > 0.583√N`. If `sk > N` the claim is trivial. ∎

*(The audited version used 3N valid hints and a split at `N/5`, giving 0.42. The 4N strengthening is the reviewer's.)*

**Audit record.** The reviewer audited every step, including my three self-attacks: repeated inputs (harmless), the valid-hint step (sound, and superseded by the vacuous case), and padding under adaptivity (preserved, for any total Q). **Monte Carlo check of step 4**, the only inexact step (3000 views each; random and clustered `V`; `N` up to 1024, `k` up to 16): the bound held in all 12 cells. The random-hypergraph templates sat at `E[max] ≈ 2.4`, **below what totality needs**, consistent with the theorem. **At `s = 1`, step 4's true value is 2 (`j ≤ 1`), which recovers W25.1 exactly for every `k`.**

## §9. What it says

- **At the line's scale, `k = poly(n) = polylog N`:** `q ≥ √N / polylog N = 2^{n/2 − O(log n)}`. **In the membership model, no polynomial-query deterministic depth-1 back-mapping exists for any poly-fan-in joint glue.** It is the first theorem of the black-box line for **general joint glue**, and it comes from a count, not an adversary.
- **Relation to W12.2:** W12.2 (per-coordinate one-input glue, reaching total fan-in `log N + 2`) gives `q ≥ N/9` in its class. W26.1 is weaker there (`√N`) but covers the whole joint class.
- **Relation to W25.3:** at `k = N`, `q = O(1)` is achievable, and W26.1 permits `q = O(1)` only once `k ≳ √N`. **Consistent.**
- **Relation to W13/W14:** W14 ended on "no selection principle" for four interacting choices. **That obstruction belonged to the DNF model.** In the membership model the transcript is a function of `y` alone (W25.2), so there is nothing to select.

## §10. Tightness -- W26's open residue

**Tight at neither endpoint; the `√N` comes from the count, not the problem.** At `k = 1` the truth is `Θ(N)` (W12.2 transfers down). At `k ≈ √N` the theorem allows `s = O(1)`, but W25.3's hypergraph construction does not localise: a `√N`-window contains a fixed 6-set with probability about `(1/(2√N))^6`. **So the truth there is probably higher.** **Residue: at `k = polylog N`, is the membership-model truth of order `N` or `√N`?** In particular, does per-coordinate structure (W12.2) buy the missing `√N`? Any localised `O(1)`-query construction needs `k ≳ √N`. **By the reviewer's ordering, this is pursued only if W27's DNF extension stalls at its first step.**

## §11. Errors and misses

**Reviewer's (its words: fifth miss in W24-W26):** priced the precision mechanism at 45 on its endpoints without computing its middle. Its re-derivation bounded `2^j ≤ 2^{q+1}` uniformly, which cancelled the `q`-dependence and gave only `q ≥ log(N/k²)`. **Mine:** §5A's "membership **is** Definition 9 at `w = 1`" (corrected in §6); a placement sketch (§2(c)) priced as the likely shape, which was a detour; and the pre-registered construction search was never run, because the proof arrived first (**recorded, not hidden**). The W25 n = 3 rows were never obtained: the constant-PP run timed out, and I killed the count run by an over-broad process match that also killed a page append (caught before commit, nothing lost).

**Practice line (the reviewer's wording): THE OBSTRUCTION WAS THE MODEL'S, NOT THE PROBLEM'S.** W13/W14 found no selection principle because their model needs one; the membership model has none to find. **A companion line, mine: PRICE A MECHANISM AGAINST THE PROBABILITY OF EACH CASE, NOT AGAINST ITS WORST CASE.** The `2^j` gain was affordable because seeing `j` elements costs `(k/2N)^j`.

## §12. Closing

**W26 proves nothing about P vs NP**, nothing about `FP^NP`, nothing about the DNF model, and nothing randomised. It proves Theorem W26.1: **in the membership model, depth-1 black-box stretch increase with poly fan-in needs `2^{n/2 − O(log n)}` queries.** **Next, W27** (`pvsnp/W27_dnf_extension.md`): extend toward Definition 9, where a query may name different values at different inputs and the transcript depends on `C`. The §10 residue waits behind it.
