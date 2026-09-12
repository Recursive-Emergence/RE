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

---

# W34 Findings

*Appended after the reviewer audited §4A step by step and ruled 34a. Nothing above is revised.*

## §5. Ceiling

**Definition 9, deterministic, depth 1, `n′ = n`, fan-in `≤ 2`.** The constant is proof-of-shape, at astronomical `N`. **Nothing here crosses the weakest arrow (W33 PATH):** no statement about `FP^NP`, nothing randomised, nothing beyond depth 1. **Distribution note:** the density count is over **uniform functions** `C : [N] → [2N]`, not injections. W26.1's injective distribution is a different object, and the two must not be conflated.

## §6. Outcome against priors

| code (re-registered target) | pre-contamination mine (§2, 34a/b/c) / reviewer | contaminated mine (§4A) | outcome |
|---|---|---|---|
| **34a** forced chains closed; W32.1 unconditional for fan-in 2 | 30 / 20, re-registered 25 | 55 | **ACHIEVED** |
| 34b | 45 / 55, re-registered 50 | 35 | -- |
| 34c | 25 / 25 | 10 | -- |

**Scored against the pre-contamination priors and the reviewer's**, as §4A disclosed. **The mechanism is neither of the pre-registered ones:** §1(b)'s divergence count closes starts with a choice but not convergent starts. The closing object is **a count over (hint, circuit) pairs**.

## §7. The density count and its consequences

**(1) Double count (the reviewer's, audited).** `|range(C′)| ≤ N` for every `C`, so `Σ_y |F_y| = Σ_C (4N − |range(C′)|) ≥ 3N·(2N)^N`. Normalised: **`Σ_y d_y ≥ 3N`**.
**(2) The threshold (mine, the decisive move).** At `δ = 0.7`, `#{d_y ≥ 0.7} ≥ (3 − 4δ)N = 0.2N`. A certifying hint (`F_y ⊆ {v ∉ range(C)}`) has density `≤ (1 − 1/2N)^N < e^{−1/2} ≈ 0.6065`, so **every hint with `d_y ≥ 0.7` is non-certifying.** No branch selection is needed.
**(3) Branch.** Choose `a_H` maximising conditional density; the branch has density `≥ 0.7`.
**Five consequences at that branch:**
- (a) **No exhaustion.** Every input has `≥ 1.4N` values appearing in some valid completion.
- (b) **No forced chains.** `L` jointly forced inputs cap density at `(2N)^{−L}`, so **(H_casc) is vacuous.**
- (c) **`M_res ≤ 2N·ln(1/0.7) ≈ 0.713N`**, since unary forbiddance of `v` at `M` inputs caps density at `e^{−M/2N}`. So `|U_v| ≥ 0.187N` at `h ≤ N/10`. *(At the reviewer's original `δ = 1/8` this bound is `2N ln 8 > N`, which is why the threshold had to sit above `e^{−1/2}`.)*
- (d) **Validity:** positive density, so the branch is clean.
- (e) **Payer domains:** unary-forbidden mass at any input is `≤ 0.6N`.

## §8. Ledger -- what density replaces and what it does not

| W32 component | status after W34 |
|---|---|
| bad_ext (inputs with `< t` values) | **gone** (`k ≥ 1.4N`) |
| exhaustion pair count, second-round pinning | **gone** |
| bad_M and W29.2's count over hints for `M_res` | **replaced** by `e^{−M/2N} ≥ 0.7` |
| lightest-value hub rule | **replaced** by density-maximising `a_H` |
| bad_clean | **automatic** (positive branch density) |
| (H_casc) | **vacuous** |
| pre-pinning of degree `> D*` | still needed (for `D_res`) |
| super-heavy count (§11 of W32-A) | still needed; a per-hint union bound (§9) |
| protected set, payer capacity `c = 1` | unchanged in form; capacity improves (§10) |
| random give-ups, (H_mass) discharge | unchanged |
| W28's hosting count under Q's pins | unchanged (per hint and branch) |

## §9. Constants

Dense hints `≥ 0.2N`. Super-heavy exclusion: hints with more than `J = N/(100D*²)` super-heavy windows number `≤ 32D*N²/(M·J) = 3200·D*³·N/M`. **At `M = 64000·D*³` (the reviewer's choice) that is `≤ 0.05N`, leaving `≥ 0.15N` hints that are dense and have at most `J` super-heavy windows.** *(`M = 32000·D*³` would leave `0.1N`; the larger value is used for slack.)* The rest of W32.1's chain is as in W32-A §12.

## §10. Tier-1 threshold, corrected (the reviewer's caution)

Payer capacity is the domain after unary-forbidden mass (`≤ 0.6N`), fine mass (`≤ N/8`) and absorbed rows. So **capacity `≥ 1.4N − N/8 = 1.275N`**, and the tier-1 rule restricts only rows of size **at most `1.275N − 1`**, not W32-A's `1.75N`. Larger rows go to give-ups. §11's give-up counts are unchanged in form; `m ≤ |E_w(y)|/s` still holds.

## §11. Consistency checks (exact enumeration, N = 4, all 4096 circuits, 16 hints)

| template | `Σ_y d_y` (≥ 12) | hints with `d ≥ 0.7` (≥ 0.8) | at dense hints: min values per input (claim ≥ 5.6) / max inputs missing one string (claim ≤ 2.85) |
|---|---|---|---|
| almost-unary ring, 2 seeds | 12.37, 12.47 | 11, 13 | 8 / 0 |
| random fan-in-2 ring, 2 seeds | 12.33, 12.32 | 15, 15 | 8 / 0 |
| projection ring | 12.35 | 16 | 8 / 0 |
| **explicit full forced chain** (every window outputs hint 0 unless its pair equals a fixed `c`) | 14.94 | 15 | **hint 0: density 0.000244 = 1/4096, all 4 inputs single-valued** |

**The forced-chain hint sits far below 0.7, as the count requires, and the other 15 hints are dense.** At N = 4 the claims are easily met (sizes are too small to be tight). These are consistency checks, not tests of the asymptotic constants.

## §12. Theorem W32.1, unconditional

> **Theorem W32.1 (unconditional).** *Definition 9, deterministic, depth 1, `n′ = n`. Every template in which each C′-input reads at most two C-inputs, with arbitrary glue, satisfies* **`qw ≥ c(D*)·N` for `N ≥ N₀(D*)`**, *with `c(D*) = D*^{−O(D*)}` and `N₀ = D*^{O(D*)} log N` (`D* = 20`).*

*Proof:* a dense branch (§7), whose consequences are recorded in the ledger (§8), then W32-A §12's protected set, random give-ups and McDiarmid, with §9's constants and §10's tier-1 threshold. **Proof-of-shape.**

## §13. Practice line (shared)

**COUNT OVER THE PRODUCT SPACE.** W26.1 counted circuits at a fixed hint; W29.2 counted hints at a fixed structure. **The object that closed the fan-in-2 case was the count over (hint, circuit) pairs, which neither of us wrote down for nine rounds.** The decisive refinement was placing the density threshold above the certifying density.
