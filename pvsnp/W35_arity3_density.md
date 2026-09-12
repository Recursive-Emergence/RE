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

---

# W35 Findings (one bounded round)

*Appended after the reviewer's ruling (35b). Nothing above is revised.*

## §4. Ceiling

Definition 9, deterministic, depth 1, residual arity 3, at W34's dense branch (every input `≥ 1.4N` values, `M_res ≤ 0.713N`, no forced chains). **No theorem this round.** Nothing crosses the weakest arrow.

## §5. Outcome against priors

| code | mine (cold) / reviewer (cold) | reviewer revised after §3B | outcome |
|---|---|---|---|
| 35a arity-3 theorem, constant for fixed `D*` | 15 / 20 | 30 | -- |
| **35b** payment fails at a named count | 60 / 55 | 45 | **the outcome: residue = capacity collisions among heavy strings' split payments** |
| 35c nothing | 25 / 25 | 25 | -- |

**Not the pre-registered count.** §1(b)'s "mass versus cover" was moot (§3B), and my later "window mass `2N²` against capacity `N`" priced the wrong object. The reviewer corrected it: a protected input need not host every string.

## §6. The mechanism: string-to-input assignment (the reviewer's), audited

For each protected `u` (strongly independent), choose a **hosted set `V_u`** with probability `p` per string. For `v ∈ V_u`, the coarse rows are keyed by a **single partner value**: `R_{v,b} = {c : g(v, b, c) = y}`, `|R_{v,b}| ≥ s`. **Excluding `b` at `u₂` neutralises the whole row at `u₃`**, and symmetrically. The payer's load per window is `|∪_{v ∈ V_u} B_v| ≤ p·Σ_v |B_v| ≤ p·|E_w(y)|/s`, about `p·16D*N` at average mass. With `p = Θ(1/D*)` this is within capacity, and **every string is hosted at about `p|P|` protected inputs, with no product over windows.** A payer serving `c` protected inputs scales `p` by `1/c`. **Arity 2 does not benefit**: there the key is `v` itself, so exclusion is a give-up. **Arity `≥ 4`**: keys are `(k − 2)`-tuples, and unary exclusion is a **hitting-set problem over tuple keys** (the next gap, not W35's).

## §7. PROJ3 defeats assignment alone (exact, analytic)

Every input `u` is position 0 of its own window `(u, u + 1, u + 2)` with glue `(a << 1) | (b₀ ⊕ c₀)`. For `v = y >> 1` and **every** `b`, the row at `u + 2` is `{c₀ = b₀ ⊕ y₀}`, of size `N`. So **`B_v` is the whole domain of `u + 1`**, and hosting `y >> 1` at any protected input would cost its payer everything. **`y >> 1` is in no `V_u`, at every hint.** This is **consistent with the reviewer's (hint, string) count** (`Σ_y |B_v| = 4N` per `(w, v)`): the count bounds how often a **given** string is heavy, while hosting at a hint needs the **maximum** over strings, and some string is heavy at every window at every hint. *(Sum versus max; the reviewer's seventeenth miss, in its words.)*

**The hybrid (the fix).** Strings with normal `B_v` use assignment. Strings with `|B_v| ≈ 2N` use **§3A's split payment**: restrict one parity class at `u₃` and exclude the matching class at `u₂`, costing about `N` at each of two payers, within `1.275N`.

## §8. Named residue

**Capacity collisions among heavy strings' split payments at a shared payer.** At these constants a payer holds one split, so two heavy strings needing incompatible parity classes at one payer cannot both be paid, and the loser is given up at that protected input. **Multiplicity is bounded:** heavy strings (`|B_v| ≥ L`, `L = N`) per `(hint, window)` number at most `|E_w(y)|/(s·L)`, about `16D*` at average mass, union-bounded at heavy windows. **So the residue is a bounded-multiplicity assignment problem, not an unbounded one.** **A string this scheme cannot pay is not thereby unhostable in truth** (rows of size `N` leave half of the partner's domain), so the gap is again in the construction.

## §9. Data

Exact CSP at N = 9 (arity-3 ring, protected inputs 0/3/6, `S = 3`, hosted-set probability `p = 0.5` and `0.25`, 9 hints): STAR3 mostly 0 hosts; PROJ3 mostly invalid or 0; the mixed template is invalid at most hints and gives 3-5 hosts elsewhere. **Uninformative, recorded as such.** The mechanism needs `p·|P| ≫ 1`, while `|P| = 3` leaves some of 18 strings in no hosted set by chance, and payer overload invalidates hints. That regime is out of exact reach at arity 3. **The PROJ3 failure rests on §7's analysis, not on these numbers.**

## §10. Practice line

**A COUNT THAT BOUNDS HOW OFTEN EACH STRING IS BAD DOES NOT BOUND WHETHER SOME STRING IS BAD NOW.** Per-string budgets over hints and per-hint maxima over strings are different quantifiers. This is the third sum-versus-max failure of the line.
