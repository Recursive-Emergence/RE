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
