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
