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
