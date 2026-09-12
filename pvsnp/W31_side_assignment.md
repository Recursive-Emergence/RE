# W31: the side assignment for coarse rows. Pre-registration

*Drafted 2026-09-12 on branch `w31-side-assignment` (from `w30-residual-arity` at 6765871), on the reviewer's amended W31 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before any computation.**

## §0. Target and ceiling

**Definition 9, deterministic, depth 1, arity-2 residual after pre-pinning.** For a hint `y`, each coarse triple `(w, a at u, R at u′)` with `|R| ≥ s` takes one side. **EXCLUDE** adds `a` to `Excl(u)`. **RESTRICT** adds `R` to `Excl(u′)` and consumes capacity at `u′`: the union of restricted rows plus the fine forbidden mass must leave a value. **Hosting** needs, for every string `v`, `|{u : v ∉ Excl(u)}| > qw(D′ + 1) + pins`. **Candidate assignment (the reviewer's):** a fixed random edge order; for each edge, flip a coin to RESTRICT if the capacity at `u′` allows it, otherwise EXCLUDE.

**Ceiling as for W28-W30.**

## §1. Counting done before the prior

**(a) Hosting probability is per incidence, and forced exclusions only help the row side.** A string `v` is unhostable at `u` only through `v`'s own incidences at `u`: an out-edge with value `v` that is excluded, or an in-row containing `v` that is restricted. A capacity-forced EXCLUDE lands on the **value** side, so it removes one restriction at `u′` and cannot hurt hosting there. **So `Pr[v hostable at u] ≥ 2^{−inc_v(u)}` with `inc_v(u) ≤ D + D_in`**, and `E|hostable(v)| ≥ N·2^{−(D + D_in)}`. On projections (`D = D_in = 1`) that is `N/4` for the worst string, consistent with HALF's win.

**(b) The loss is EXPONENTIAL in degree, and that matters for the line.** For bounded `D` it is a constant. For random-like residuals `D ≈ log N`, so `2^{−2D} = N^{−Θ(1)}`, weaker than W28.1 itself. **So the coin assignment can give 31a only for bounded degree.** Whether a smarter assignment (a b-matching, or a biased rule) makes the loss polynomial in `D` is the natural strengthening and **is not priced as reachable here.**

**(c) Concentration across `u` (Q2).** The events "`v` hostable at `u`" depend on each other only through shared edges, and each input shares edges with at most `O(D + D_in)` others. So a bounded-dependence Chernoff bound (or Janson) gives `|hostable(v)| ≥ N·2^{−(D + D_in)}/2` except with probability `exp(−Ω(N·2^{−(D + D_in)}/(D + D_in)))`. **A union over the `2N` strings closes when `N·2^{−(D + D_in)} ≫ (D + D_in) log N`.** At testable sizes (N ≤ 64, `D + D_in` about 3-4) this is marginal, so exact counts must be reported rather than assumed.

**(d) Capacity must reserve the fine rows.** W28's almost-full count needs fine forbidden mass `< 2N` after restrictions, so capacity at `u′` is `2N − D·s − |∪ restricted rows|`. **The threshold `s` then sets `D_in`**: lower `s` means more coarse edges but more room. I fix `s = N/D` for the tests, not by optimisation.

**(e) The mixed control.** A projection chain `(x, x+1)`, plus two extra windows `(u₁, z)`, `(u₂, z)` whose rows at a shared `z` are complementary halves. **Prediction:** the coin alone fails at `z` about half the time (both rows restricted); the capacity check forces one exclusion; hosting stays `Ω(N)`.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **31a** assignment theorem, `qw = Ω(N/f(D, D_in))`, bounded degree | 25 | **40** |
| **31b** works on controls, fails on a named mixed template | 55 | **45** |
| **31c** nothing | 20 | **15** |

**Why 31a above the reviewer:** §1(a) is a clean per-incidence bound, and forced exclusions only help. The dependence is bounded, so (c) is standard. **Why not higher:** (b) confines it to bounded degree, and §1(d)'s interaction between capacity and the fine rows under Q's pins is unverified.

## §3. Flags and kill tests

- **A31 -- controls first:** projection (the coin alone), killing chain (the capacity check alone), then the mixed template (§1(e)). Exact CSP checks against SMART-Q0 and against a pinning Q.
- **B31 -- report `min_v |hostable(v)|` exactly**, over random seeds, against `N·2^{−(D + D_in)}`.
- **C31 -- the capacity/fine-row interaction (§1(d)):** after Q pins, check extension exactly, not by the count.
- **D31 -- stop-rule:** any template where every assignment fails hosting for some `v` goes to the reviewer before writing.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# W31 Findings

*Appended after the reviewer ruled on the data and on the proof decomposition. Nothing above is revised; §1(a) is corrected in §7.*

## §4. Ceiling

**Korten's Definition 9 model, deterministic, depth 1, `n′ = n`.** The theorem is **existential**: it gives one good hint and one good side assignment, which is all a lower bound needs, since the adversary is unbounded. **Derandomising the choice is neither required nor claimed.** Not Korten's Problem 1; nothing randomised; nothing about P vs NP.

## §5. Outcome against priors

| code | mine / reviewer | outcome |
|---|---|---|
| **31a** assignment theorem for bounded degree | 40 / 25 | **achieved -- Theorem W31.1, with the exponential loss in the statement** |
| 31b fails on a named mixed template | 45 / 55 | -- (the mixed control passed) |
| 31c nothing | 15 / 20 | -- |

**Not the pre-registered mechanism in one respect:** §1(a)'s per-incidence bound was wrong as stated (§7). The proof uses the reviewer's decomposition, **coin then deterministic repair**, with a **biased** coin that I introduced to handle the killing chain's capacity collisions. The biased coin was W32's proposed device; it enters here.

## §6. Theorem W31.1

**Setting.** After pre-pinning, the residual has arity `≤ 2`, maximum degree `D`, and a threshold `s` with `D·s < 2N`. A **coarse triple** `e = (window, value a at u, row R_e at u′)` has `|R_e| ≥ s`; triples are taken in **both orientations** of every window. Rows below `s` are **fine**. `D_out` = max coarse triples with value side at one input; `D_in` = max with row side at one input. **Capacity** at `u′`: a set `S` of coarse rows into `u′` **fits** if `|[2N] \ ∪_{e ∈ S} R_e| > D·s`.

> **Theorem W31.1.** *Fix a hint `y` and a bias `β ∈ (0, 1)`. Let `p_cap` bound, for every `u′`, the probability that the rows into `u′` selected independently with probability `β` do not fit. If*
>   *(C1) `D_in · p_cap ≤ β^{D_out}(1−β)^{D_in} / 8`, and*
>   *(C2) `N · (β^{D_out}(1−β)^{D_in})² / (32 · D_out) > ln(4N)`,*
> *then `y` is valid and every deterministic back-mapping correct on `y` has*
>   **`qw ≥ (N·β^{D_out}(1−β)^{D_in}/4 − M_res) / (D′ + 1)`.**
> *For `D, D_in, D_out = O(1)` and a constant `β` satisfying (C1), this is `qw = Ω(N) − O(M_res)`.* **The loss `β^{D_out}(1−β)^{D_in}` is exponential in degree.**

*Proof.* **Step A (independent coins).** Each coarse triple is RESTRICTED with probability `β`, otherwise EXCLUDED, independently. Let `H_A(v)` be the set of inputs `u` where every coarse out-triple at `u` with value `v` is restricted and every coarse in-row at `u` containing `v` is excluded. Then `E|H_A(v)| ≥ N·μ` with `μ = β^{D_out}(1−β)^{D_in}`. Changing one triple's coin changes `|H_A(v)|` by at most 2 (its `u` and its `u′`), and there are at most `N·D_out` coins. **McDiarmid:** `Pr[|H_A(v)| < Nμ/2] ≤ exp(−2(Nμ/2)²/(4·N·D_out)) = exp(−Nμ²/(8D_out))`. A union over the `2N` strings is `< 1/4` under (C2) (which has slack).
**Step B (deterministic repair).** At every `u′` where the restricted rows do not fit, convert **all** its restricted in-triples to exclusions. Afterwards every input's remaining domain exceeds `D·s`. Each conversion removes hosting of **one** string at **one** value-side input, and there are at most `D_in` of them per over-capacity input. `E[#over-capacity] ≤ N·p_cap`, so by Markov `#over ≤ 4N·p_cap` with probability `≥ 3/4`. The total hosting lost **by any single string** is then `≤ D_in · 4N p_cap ≤ Nμ/2` by (C1). Conversions only enlarge row-side domains, so they never hurt hosting elsewhere.
**Joint.** With probability `> 1/2`, every `v` has `≥ Nμ/2 − Nμ/4 = Nμ/4` hosting inputs after repair. **Fix such an assignment.**
**Adversary.** Exclusions `X` and restrictions are its promises. Its invariant is W28's: pins are consistent, avoid `X` and restricted values, and create no violated full window among **fine** rows. **NO is sound** (terms against the promises are false on the final `C`, which honours them). **Extension:** every domain exceeds `D·s` and fine rows exclude `< s` each, so W28.1's greedy fill works; with `P = ∅`, `y` is valid. **Hosting:** W29.1's count with `D′` and `M_res`. ∎

*(The union-bound constants are loose on purpose; the statement's shape, not its constants, is the claim.)*

**Controls for (C1).** Projections: coarse in-rows per input `D_in = 1`, and a single row always fits, so `p_cap = 0`. The killing chain: two complementary halves into one input, so `p_cap = β²`, and (C1) needs `2β² ≤ β(1−β)²/8`, i.e. **`β ≈ 0.055` suffices, and `β = 1/2` does NOT.** **A fair coin provably fails the proof's condition on the killing chain; a biased coin passes it.**

## §7. Data, and the correction to §1(a)

**Exact CSP, all hints × 3 seeds, fair coin with an exact global capacity check.** `min_v |hostable(v)|`, best / distribution:
- projections, N = 8: best 4 = N/2 (a single zero among 96 pairs); N = 16: best 8 = N/2 (a single zero among 192)
- killing chain, N = 8: best 7 (bimodal 0-1 / 6-7, tracking its odd-hint `M_res` artefact)
- mixed, N = 8: best 4; N = 16: best 8 = N/2

**The zeros are why the theorem is existential, not for-all-assignments.**

**Capacity overrides of the coin** (the reviewer asked for the number behind "behaves like projections once forced"): mixed N = 8: 0 overrides at 67 pairs, 1 at 29; mixed N = 16: 0 at 147, 1 at 45; projections: 0 at every pair; killing chain: 1 at 25/96. **Never more than one**, and one override in about a quarter of runs is the predicted rate (both complementary rows drawn as restrict, 1/4).

**Incidence profile, `Pr[hostable | inc]`:** projections N = 16: 1.000, 0.499, 0.249 for inc = 0, 1, 2; mixed N = 16: 1.000, 0.513, 0.248, **0.083** for inc = 0-3 (`2^{−3} = 0.125`); killing chain inc = 1: 0.597. **The loss tracks `2^{−inc}` with no favourable correlation**, so the observation a polynomial-in-`D` bound would need is absent here.

**CORRECTION to §1(a), mine.** "Capacity-forced exclusions only help" holds on the **row** side only. On the **value** side they push an out-triple's exclusion probability above 1/2 whenever capacity binds: mixed inc = 3 sits at 0.083 < 0.125. **The pre-registered bound `2^{−inc}` was false as stated.** The theorem's `p_cap` term and Step B's repair accounting are what the correction requires.

**Not tested: the middle band** (rows between `2N/D` and `cN`, many per input). It needs templates with growing degree that random glue does not produce at N ≤ 16. **C31** (extension under Q's pins) was uninformative at these sizes; recorded as such, not as passed.

## §8. Coverage -- the headline for the program page

**W28.1 covers small rows at any degree. W31.1 covers coarse rows at bounded degree. W29.2 covers hub-plus-unary templates. The uncovered case is coarse rows at growing degree -- the middle band at `D ≈ log N` -- where W31.1's loss is `N^{−Θ(1)}`.** A polynomial-in-`D` side assignment is W32's candidate.

## §9. Errors and misses

**Mine:** §1(a)'s "forced exclusions only help" (true on one side only; caught by the incidence data). **Reviewer's:** none new this round; its greedy-cascade warning about the proof is what produced the coin-then-repair decomposition.
**Practice line: A GREEDY STEP THAT IS CORRECT IN CODE CAN BE UNPROVABLE -- SPLIT IT INTO INDEPENDENT RANDOMNESS PLUS A DETERMINISTIC REPAIR WHOSE DAMAGE YOU COUNT.**
