# W34: forced chains. Pre-registration (one bounded round)

*Drafted 2026-09-12 on branch `w34-forced-chains` (from `w33-consolidation` at d315498). The reviewer decided (a) under the line's standing rule that stalled questions are decided with reasons, **subject to the user's override**; if either user redirects to the door, this round stops where it stands and is recorded. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before any computation.**

## §0. Target and ceiling

**Target:** discharge (H_casc) in W32.1, making it unconditional for fan-in 2 (still proof-of-shape). **Ceiling:** nothing crosses the weakest arrow (W33 PATH). Depth 1, Definition 9, deterministic.

**The reviewer's proposal:** a hybrid in which chain windows (almost unary in their first coordinate, by §13's tightness) go to W12.2's per-coordinate adversary and the rest to W32.1, with the chain inputs as a pre-pinned set chosen by W12.2.

## §1. Counting done before the prior -- and a different lever

**(a) Almost-unary windows are W29.2's, not W12.2's.** For `g(a, b) = y_{w,a}` except at one `b*`, the constraint for hint `y` is **"C(u) = a ⇒ C(u′) = b*" for each `a` with `y_{w,a} = y`**. Such `a` number `2N` summed over hints, so **1/2 per hint on average: unary-like.** Excluding those `a` at `u` makes the window a product constraint, counted exactly like W29.2's unary windows. **The chain arises only when exclusion is impossible**, i.e. when `z₁` has **no** allowed value outside the implication values. **So the object is not the window class; it is inputs all of whose allowed values force.**

**(b) The §13 tightness assumes ONE start value, and a start with a CHOICE diverges.** If `z₁` has `m` allowed values, each forcing a different chain, then following all `m` chains costs link budget for each divergent branch. **At a hint with `links(y)` near-full rows, the shortest chain from such a start has length at most `links(y)/m`.** Since `Σ_y links(y) ≤ 2N²`, the hints with `links(y) ≥ 10N` number at most `0.2N`. **At the remaining hints, a start with `m ≥ N/4` allowed values has a chain of length at most 40.** Raising the exhaustion threshold so that every input keeps `t = N/4` allowed values costs about `0.14N` hints (bad_ext at `2N − t`), which fits the W32 margin. **Starts** (inputs whose every allowed value forces) each consume `≥ m ≥ N/4` links, so **at most 40 per good hint**. Pre-pinning all their shortest chains then pins **`O(1)` inputs**, which W32.1's pre-pinning absorbs.

**(c) The loophole: CONVERGENCE.** Branches can merge if different start values force the **same** next value, `b*(a) = b₀`. Then the window has `g(a, b) = y` for all `a` and all `b ≠ b₀`, which forces `z₂ = b₀` **unconditionally** at `y`. Such a window has `|E_w(y)| ≈ 4N²`, which is possible at one hint per window, so `N` such `(y, w)` pairs in total. **A length-`N/2` unconditional chain at every hint would need `2N²` of them: impossible.** Unconditional forcing averages `≤ 1/4` link per hint. **Partial convergence** (`b*` taking `r` values over `m` starts) sits in between, trading heavy-window budget against branching. **This interpolation is the step that can fail, and the round's crux.**

**(d) Interaction.** Distinct shortest chains from different starts may force one input to two values, making the chosen start values jointly invalid. With `m ≥ N/4` choices per start and at most 40 starts, a counting choice should avoid collisions. **Unverified.**

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **34a** forced chains closed; W32.1 unconditional for fan-in 2 | 20 | **30** |
| **34b** chain part handled but the recombination fails at a named count | 55 | **45** |
| **34c** nothing | 25 | **25** |

**Why 34a above the reviewer:** §1(b)'s divergence count is a count over an already-measured object (the link budget, from §13's own tightness observation), which is the kind of mechanism that has survived cross-audit. **Why not higher:** the convergence interpolation (§1(c)) and collision avoidance (§1(d)) are unverified, and W32-A's recombinations failed in the middle twice.

## §3. Flags and kill tests

- **A34 -- audit §1(b)-(c) with the reviewer before building anything.**
- **B34 -- kill template (Q4):** the forced-chain template at N = 8 from §13's structure, (i) with a single start value (the tight case), (ii) with `m` divergent start values, (iii) with convergent start values. Exact CSP; measure the shortest forced chain and hosting under the hybrid adversary, and against a template-aware Q that reads `z₁`.
- **C34 -- stop-rule:** a count closing convergence goes to the reviewer before writing.
- **D34 -- one round.** Whatever lands at the end of (B34) is scored.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §4A. Amendment -- A34 rulings, the reviewer's density count, and a threshold that dissolves (Q1). DISCLOSURE: derived before these priors

**A34 rulings recorded.** (1) The hybrid is withdrawn (the reviewer's sixteenth miss): almost-unary windows are unary-like. (2) Divergence closes starts that have a choice. **Convergent starts survive every existing count**, including §11's super-heavy one: one convergent start per hint suffices, and the template affords about two per hint.

**The reviewer's density count, audited (Q3): HOLDS.** For every `C`, `|range(C′)| ≤ N`, so `Σ_y |F_y| = Σ_C (4N − |range(C′)|) ≥ 3N·(2N)^N`, where `F_y` is the set of circuits valid for `y`. A certifying hint (`F_y ⊆ {v ∉ range(C)}` for some `v`) has density `≤ (1 − 1/2N)^N < e^{−1/2} ≈ 0.6065` for every `N` (checked: 0.5967 at N = 8, increasing to the limit). Conditioning on hub values `a_H` has maximum branch density `≥` the average.

**Mine: raise the density threshold above `e^{−1/2}`, and (Q1) disappears.** Let `δ = 0.7`. Then `Σ_y d_y ≥ 3N` and `Σ_y d_y ≤ #{d_y ≥ δ} + 4Nδ`, so **at least `(3 − 4δ)N = 0.2N` hints have `d_y ≥ 0.7`**. These are **automatically non-certifying** (`0.7 > 0.6065`). Choose `a_H` to maximise conditional density, so the branch density is `≥ 0.7`. At that branch:
- **No exhaustion.** An input with `k` values appearing in valid completions forces density `≤ k/2N`, so **`k ≥ 1.4N`** at every input.
- **No forced chains.** `L` jointly forced inputs give density `≤ (2N)^{1−L}`.
- **`M_res` bounded by density**, the step the reviewer could not get at `δ = 1/8`. If unary residual windows forbid `v` at `M` inputs, then `F ⊆ {C(u) ≠ v at those inputs}`, whose density is `(1 − 1/2N)^M ≤ e^{−M/2N}`. So `e^{−M/2N} ≥ 0.7` and **`M_res ≤ 2N·ln(1/0.7) ≈ 0.713N`**. Hence `|U_v| ≥ N − h − 0.713N ≥ 0.187N` at `h ≤ N/10`.

**So at a dense branch, (H_casc) is vacuous, W32's `M_res` count is replaced by a density bound, and the lightest-value choice is no longer needed.** The remaining W32 counts that range over hints (super-heavy windows, §11) must share the `0.2N` dense hints: their bad set is tunable to `≤ 0.1N` (larger `M`), leaving `≥ 0.1N` usable hints. **Capacity at payers improves** to `≥ 1.4N` minus fine mass.

**What this does NOT yet verify.** (i) That W32's give-up and protected-set machinery needs nothing further from the lightest-value choice. (ii) That the super-heavy hint count and the density-dense hint set intersect as claimed: both are counts over hints, so a union bound suffices, but the constants must be written out. (iii) Q's pins: W28's hosting count is per hint and branch, so it should be unaffected. **Stop-rule C34 applies: this goes to the reviewer before writing.**

**DISCLOSURE.** The `δ = 0.7` observation was derived while auditing the reviewer's message, **before** these re-registered priors, so the priors are contaminated by it.

| code (re-registered, the reviewer's target) | reviewer | **mine (contaminated)** |
|---|---|---|
| 34a density count plus branch selection closes forced chains; W32.1 unconditional for fan-in 2 | 25 | **55** |
| 34b density count recorded; selection fails at a named count | 50 | **35** |
| 34c nothing | 25 | **10** |
