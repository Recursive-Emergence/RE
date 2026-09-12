# W30: residual arity at least 2. Pre-registration

*Drafted 2026-09-12 on branch `w30-residual-arity` (from `w29-prepinning` at c81d84d), on the reviewer's W30 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before any computation and before re-reading W10.3 or W14.**

## §0. Target and ceiling

**Definition 9, deterministic, depth 1.** Pre-pin `h` hubs; the residual has windows of arity up to `r ≥ 2`. W29.2 handled `r ≤ 1` by counting; W28.1 handled `h = 0` under the worst-case hypothesis `D·t < 2N`. **Question:** which parts of W29.2's count survive arity 2, and does extension need the worst-case hypothesis? Reviewer's questions: (Q1) a counting version of extension for arity 2; (Q2) otherwise, whether (H_t) is the only route; (Q3) a hub plus pair windows `(x, x′)` as the first test.

**Ceiling as for W28-W29.**

## §1. Counting done before the prior

**(a) bad_clean and bad_M count as in W29.2**, provided `c(y, v)` is defined with a stated convention. I fix it now: **`c(y, v)` counts inputs where `v` is forbidden by a window that is unary in the residual.** Arity-`≥ 2` windows are charged through the almost-full term `D′`, as W29.1 does. So hosting gives `qw < (N/4 − h)/(D′ + 1)` **only if extension holds.**

**(b) (Q1), counting extension, FAILS for arity 2, and I have a one-line template.** Take a window at `(u, u′)` with glue `g(a, b) = (a << 1) | b₀`. For **every** hint `y`, the row at `a = y >> 1` forbids **half** of the values at `u′` (those with `b₀ = y₀`). A count over hints cannot avoid it, because it is present at every `y`. **Count over rows:** `Σ_y Σ_a |row_a(y)| = 4N²`, so the number of hints with some row of size `≥ s` is at most `4N²/s`, which is vacuous unless `s > N`, and rows have size `≤ 2N`. **So the count over hints does not control worst-case rows at arity 2.** With two such windows `(u₁, u′)` and `(u₂, u′)` whose rows forbid **complementary** halves at `u′`, the clean pins `u₁ := y >> 1`, `u₂ := y >> 1` **kill `u′`** without violating any window. **That is split-reader, in residual form: clean does not imply extendable.** This glue is projection-like, so W10.3 covers the pure template (`qw ≥ N/8`). **Counting extension fails, and a different theorem covers the example.**

**(c) So the adversary's invariant must be EXTENDABLE, not clean.** Pin a term only if the result is **globally** extendable (a CSP check). NO stays sound. The difficulty moves entirely to **hosting**: the pins Q forces shrink neighbouring domains by up to a row's size, propagating through arity-2 windows. **That propagation is W14's coupling.** Where rows are small (`t` worst case), W28.1's almost-full count controls it; where rows are coarse, only a template-specific argument (W10.3's) does.

**(d) (Q3) prediction.** Hub plus pair windows with **random** joint glue: after pinning the hub, the residual is random arity 2 with `t_res = O(log N)` and `D_res = O(1)` w.h.p., so **W28.1 applies to the residual under (H_t)**, giving `qw = Ω(N)`. That combination is a worst-case-hypothesis theorem, which is **30b's shape, not 30a's.**

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **30a** combined theorem with COUNTING extension | 30 | **12** |
| **30b** extension needs (H_t), gap named | 50 | **68** |
| **30c** nothing | 20 | **20** |

**Why 30a at 12:** §1(b)'s template defeats any count over hints at arity 2, at every hint. **What could still rescue 30a:** a count over hints **and** rows jointly, using that coarse rows force projection-like structure, which could then be handed to a W10.3-type argument. That is a dichotomy, not a count, and I price it low.

## §3. Flags and kill tests

- **A30 -- the §1(b) template run first:** confirm clean-but-non-extendable pins at small N, and confirm that W10.3's class contains it.
- **B30 -- the convention for `c(y, v)` on every line** (unary windows only).
- **C30 -- (Q3):** hub plus random pair windows. Measure `t_res`, `D_res`, `D′`, `M_res` exactly at N = 8 and 16, and run W28's executable adversary with the **extendable** invariant.
- **D30 -- dichotomy probe:** for arity-2 glue, is "some row of size `≥ s` at every hint" equivalent to projection-like structure? Registered as a question only.
- **E30 -- stop-rule:** a counting extension argument that survives §1(b) goes to the reviewer before writing.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
