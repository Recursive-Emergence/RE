# W35: arity 3 with density. Pre-registration (one bounded round)

*Drafted 2026-09-12 on branch `w35-arity3-density` (from `w34-forced-chains` at 9862169), on the reviewer's specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push. Subject to either user's redirect to the door.*

**Committed cold: before any computation.**

## §0. Target and ceiling

**Definition 9, deterministic, depth 1, residual arity 3.** W34's dense branch holds at **every** fan-in: every input keeps `≥ 1.4N` values, there are no forced chains, and `M_res ≤ 0.713N`. **So the arity-`k` residue is only the payment problem** (strong independence, and the slice cost at payer coordinates). **Target:** an arity-3 theorem with a constant for fixed `D*`, with the protected set limited to coarse single-coordinate structure (W32-B §6), the STAR3 and PROJ3 controls, and the question whether density also bounds the slice cost. **Ceiling:** as W34; at `k = polylog N` any such bound is vacuous (W32-B §4A).

## §1. Counting done before the prior

**(a) What density gives at arity 3, and what it does not.** Density bounds **single-coordinate** product sets: "`v` never appears at `u` in a valid completion" caps density at `(1 − 1/2N)`, and `M` such incidences give `e^{−M/2N}`. **Payment is a pairs question:** hosting `v` at protected `u` needs the payers `(u₂, u₃)` to avoid the slice `S_v = {(b, c) : g(v, b, c) = y}`. The adversary's pre-committed restrictions are sets `B ⊆ [2N]` at `u₂` and `C ⊆ [2N]` at `u₃` such that `B × C` misses `S_v`, for every `v` it wants hostable. **Density constrains the marginals of valid completions, not which product sets avoid a slice.**

**(b) A possible density bound on slice cost.** If for most `v` the slice `S_v` needs a cover of size `≥ κN` at the payers, then every valid completion with `C(u) = v` excludes... *no*: a valid completion only needs its own pair `(C(u₂), C(u₃)) ∉ S_v`, which is a density-`(1 − |S_v|/4N²)` event, **not** a product set. So density bounds `|S_v|` (large slices cap density through the `u`-marginal), **but not the cover size**. A slice of small mass can need a large cover: a matching needs a cover of size equal to its number of edges. **Expectation: density does not bound payment, and W35 lands 35b at the cover-versus-mass gap**, unless a count over hints bounds cover sizes the way W32-A §11 bounded give-up multiplicity.

**(c) PROJ3** (`(a << 1) | (b₀ ⊕ c₀)`) is the natural kill template for single-coordinate payment: its slice at `a = y >> 1` is `{b₀ ⊕ c₀ = y₀}`, half of all pairs, with a minimum cover of `2N` (all of one coordinate's values in two parity classes). **It is coarse at `u` but has no coarse single-coordinate row at either payer.** **Its density:** the slice caps the `u`-marginal of `y >> 1` at 1/2, so density is about `1 − 1/(4N)`, and it stays dense. **Density gives no help here, and payment by cover is impossible. The adversary must give up `y >> 1` at protected inputs**, which concentrates on `y >> 1` unless the count spreads it.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **35a** arity-3 theorem, constant for fixed `D*` | 20 | **15** |
| **35b** payment fails at a named count (cover vs mass) | 55 | **60** |
| **35c** nothing | 25 | **25** |

## §3. Flags and kill tests

- **A35 -- audit §1(b)-(c) with the reviewer first.**
- **B35 -- controls:** STAR3 and PROJ3 at N = 8, exact, with the protected set limited to coarse single-coordinate structure, give-ups otherwise.
- **C35 -- the give-up concentration on PROJ3:** does the count over hints (W32-A §11 form) spread the give-ups of `y >> 1`, or is `y >> 1` given up at every protected input at every hint?
- **D35 -- one round.**

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §3A. Correction to §1(c), mine, before any computation or ruling

**"Payment by cover is impossible on PROJ3" is WRONG.** Split payment does not need one payer to absorb a vertex cover. It needs restrictions `B` at `u₂` and `C` at `u₃` with `B × C` avoiding `S_v`. For `S = {b₀ ⊕ c₀ = y₀}`, take `B = {b₀ = 0}` and `C = {c₀ = 1 ⊕ y₀}`. Every pair in `B × C` has `b₀ ⊕ c₀ = 1 ⊕ y₀ ≠ y₀`. **Cost: `N` values at each payer**, which fits W34's capacity of `1.275N`. The minimum vertex cover of `2N` is the **total** across the two payers, not a single payer's load. **This is exactly the split payment of W32-B §1(b), which I then failed to apply to my own kill template.** What remains of §1(c): each payer loses a whole parity class, so **strings of that class are unhostable at the payers**, and with protected inputs at one third of the inputs, **hosting of those strings falls to the protected third plus unaffected payers**. That is the W30 two-sided cost, not a failure. **§1(b)'s "mass versus cover" point stands in general** (a matching slice needs a cover as large as itself). But PROJ3 is not its example, and **a kill template for (b) needs a slice with a large cover that no two-sided product split avoids cheaply.** The priors are not revised; the correction is recorded before the reviewer's audit.

## §3B. Second self-audit, before any computation: the "mass versus cover" worry (§1(b)) is moot, and the real object is per-pair coarse rows

**Payment is only needed where single-coordinate forbidden sets are large.** W28.1's extension works whenever every forbidden set at one coordinate, given the window's other coordinates, is small: `D·t < capacity`. A slice with a large vertex cover but small rows is **matching-like**: for each `b` at `u₂`, few `c` at `u₃`. **Its single-coordinate forbidden sets are small, so W28.1 extends through it and no payment is needed.** The random-slice kill test proposed in §3A would test nothing: random arity-3 glue has `t = O(1)` at `N = 8` and is W28.1's (consistent with W32-B §6's RAND3 reading).

**Where payment IS needed at arity 3:** a coarse row at one coordinate given the other two, e.g. `R_{v,b} = {c : g(v, b, c) = y}` with `|R_{v,b}| ≥ s`. Neutralising it: **exclude `b` at `u₂` (for the protected value `v`)**, or **restrict `R_{v,b}` at `u₃`**, or give up `v` at `u`. These are W31/W32-A's triples with the pair `(v, b)` in place of a value, so **the multiplicity of coarse `(v, b)` pairs replaces coarse-value multiplicity.** The protected set and the give-up counts lift if the super-heavy count bounds the number of coarse `(v, b)` pairs per window: at most `|E_w(y)|/s` per window, **as before**. **So the honest arity-3 statement is W32-A's machinery with (value) replaced by (value, partner value), and the constant loses a factor `2N`-free polynomial in `D*` per extra coordinate, if the super-heavy count is re-derived for `E_w(y) ⊆ [2N]³`.** Its average is `(2N)³/4N = 2N²` per `(y, w)`, not `N`, so **the threshold `M·s` must be re-scaled by `2N`, and that is the step to check.**

**Revised B35:** STAR3 and PROJ3 (with split payment) as controls, exact at N = 8; **no random-slice test.** Plus the re-derived super-heavy count for arity 3.
