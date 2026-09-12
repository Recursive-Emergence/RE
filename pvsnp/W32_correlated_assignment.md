# W32: the correlated side assignment. Pre-registration

*Drafted 2026-09-12 on branch `w32-correlated-assignment` (from `w31-side-assignment`), on the reviewer's W32 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before any computation.**

## §0. Target and ceiling

W31.1's independent coin loses `β^{D_out}(1−β)^{D_in}`, exponential in degree. **Target:** a correlated assignment (per-string b-matching, LP rounding, or a deterministic greedy over strings) that gives every string `v` at least `N/poly(D)` hosting inputs, while keeping collisions (C1) under control. **Kill test (the reviewer's):** a middle-band template (incidences about `D` at every input) where no assignment beats `N·2^{−Θ(D)}`. **Ceiling as for W28-W31.**

## §1. Counting done before the prior

**(a) The cost structure is asymmetric.** RESTRICT on a triple blocks `|R| ≥ s` strings at `u′`; EXCLUDE blocks **one** string at `u`. In total mass, excluding everything is cheapest (at most `D_out` strings blocked per input). **The only reason to restrict is concentration:** a string that is the excluded value at many inputs. So the natural correlated assignment is **exclude by default, and restrict only to break concentration of excluded values**, restricting at a spread subset of a concentrated string's inputs.

**(b) Concentration exists on BOTH sides, so this is a two-sided max problem.** Restricting rows that contain `v` at many inputs concentrates on `v` from the row side, which is exactly how RESTR lost on projections. So a string `v` must be spread in two families at once: the inputs where `v` is an excluded value, and the inputs where `v` lies in a restricted row. **Per-string sums are easy to bound; the maxima are the problem**, and three of this line's misses were exactly that confusion. An LP relaxation handles the sums; **rounding must control a maximum over `2N` strings**, a finite form of W23's rounding wall. Randomised rounding brings back concentration bounds with union bounds over strings, which is where independence gave `2^{−D}`.

**(c) Why polynomial might still hold.** In the independent coin, a string's `inc` incidences at one input must **all** come out favourably, which is the `2^{−inc}` loss. A correlated assignment can **coordinate the incidences of one string at one input** (choose all of `v`'s incidences at `u` together), at the price of hurting other strings sharing those edges. Each edge is shared by one value string and `|R|` row strings, so coordination for `v` at `u` costs the row strings of `v`'s out-edges. Whether the costs spread depends on how rows overlap across inputs, a design-level quantity the template controls.

**(d) Kill-test feasibility.** An exact optimum over assignments is `2^{#coarse triples}`, which is infeasible beyond about 25 triples. At N = 8 a middle-band template has well over that. **The search is local search / ILP-free heuristic: evidence only.** A heuristic failing to beat `N·2^{−D}` is not a proof of exponentiality (W27's practice line). A heuristic beating it refutes exponentiality for that template.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **32a** polynomial-in-`D` assignment theorem | 20 | **22** |
| **32b** optimum on a middle-band template is exponential; gap named | 55 | **43** |
| **32c** nothing | 25 | **35** |

**Why 32b below the reviewer:** §1(d). Proving the optimum exponential needs a lower bound over **all** assignments, a discrepancy-type statement, and at testable sizes search can only show it heuristically. That makes a clean 32b less likely than a heuristic non-answer, hence 32c higher. **Why 32a about matched:** §1(c) is a real mechanism, but §1(b)'s two-sided max is the wall the line keeps meeting.

## §3. Flags and kill tests

- **A32 -- build the middle-band template first** and report its incidence profile (median and max `inc` per `(u, v)`), confirming it actually sits in the band.
- **B32 -- three assignments on it:** W31's biased coin; the §1(a) rule (exclude by default, restrict a spread half of each concentrated string's inputs); local search maximising `min_v |hostable(v)|`. All checked with exact CSP.
- **C32 -- report against `N·2^{−median inc}`** and against `N/D`.
- **D32 -- if local search beats the coin by a factor growing with `D`, stop and send before writing.**

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §4A. Re-aim (after the priors commit 1196f48, before any computation)

**The object registered above cannot be built.** An arity-2 residual has `N` windows, so `Σ_u deg(u) ≤ 2N`: degree `≈ D` at every input is impossible, and the kill-test template does not exist. **The §2 priors were set against that object and are superseded, not revised.** The middle band is residual **arity** (W32-B, later). **W32-A**, the fan-in-2 theorem, is re-registered in `pvsnp/W32_fanin2.md`.
