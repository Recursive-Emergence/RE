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

## §3A. Amendment -- A30 and C30 data (before findings)

**A30, residual split-reader, exhaustive.** N = 8. Window `(0, 2)` has glue `(a << 1) | b₀`; window `(1, 2)` has glue `(a << 1) | (b₀ ⊕ 1)`; the other inputs have odd unary glue. **For every hint tested, the pins `{0 := y >> 1, 1 := y >> 1}` are clean and non-extendable**: input 2 is dead, and no window is violated. That is 31 of the 32 hints. Hint 1 was excluded only by the checker's crude fill of inputs 3-7 with the value 0, which equals `y >> 1` there; this is an artefact of the check, not of the template. **Clean ⟹ extendable fails at arity 2, as §1(b) predicted.**

**C30, hub plus random pair windows** (window `x` reads `(x, p(x), hub)`, random glue). Pinning the hub makes every residual window arity 2, so `M_res = 0` and `D′ = D_res`. Exact residual parameters, best hub value, three hints:

| N | D_res = D′ | t_res | D·t vs 2(N − 1) | bound `qw <` |
|---|---|---|---|---|
| 16 | 3 | 3 | 9 < 30 | 3.8 |
| 32 | 5 | 3-4 | 15-20 < 62 | 5.2 |

**The residual meets W28.1's hypothesis at every hub value tested**, whereas the un-pinned template has hub degree `N − 1` and W28.1 is vacuous. **So the combination closes for this template under (H_t), as §1(d) predicted: 30b's shape.** The bounds are small at these sizes only because the maximum random degree `D` is 3-5.

---

# W30 Findings

*Appended after the reviewer accepted the side-choice corrections and approved this record. Nothing above is revised.*

## §4. Ceiling

**Korten's Definition 9 model, deterministic, depth 1, `n′ = n`.** Residual arity `≥ 2` after pre-pinning hubs. Not Korten's Problem 1; nothing randomised; nothing about P vs NP.

## §5. Outcome against priors

| code | mine / reviewer (reviewer later) | outcome |
|---|---|---|
| **30a** | 12 / 30 (25) | **achieved for a CLASS: residuals with `D_res·t_res < 2(N − h)`, a checkable hypothesis** (scored by the reviewer's rule that a checkable class hypothesis makes a class theorem) |
| 30b | 68 / 50 (55) | the coarse regime's content, recorded as a reduction in §7, not as a theorem |
| 30c | 20 / 20 | -- |

**The resolution is not the pre-registered one in scoring:** I registered the `(H_t)` combination as 30b's shape. The reviewer's rule (checkable class hypothesis = class theorem) moves it to 30a. The coarse regime stayed open, as I registered.

## §6. Theorem W30.1 (combination) and the negative result

> **Theorem W30.1.** *Pre-pin hubs `H` to clean `a_H`. If the residual has `D_res·t_res < 2(N − h)`, every deterministic back-mapping correct on `y` has* **`qw ≥ (N − h − M_res)/(D′_res + 1)`**. *Proof: W29.1's hosting count, with extension from W28.1 on the residual.*

**Evidence (C30):** hub plus random pair windows, residual `D = 3, t = 3` at N = 16 and `D = 5, t ≤ 4` at N = 32, meeting the hypothesis at every hub value tested. The un-pinned template is vacuous for W28.1.

**Negative result: counting extension is impossible at arity 2.** The glue `(a << 1) | b₀` has a row forbidding half the partner's values at **every** hint; a count over rows is vacuous below `s = N`. **A30:** two such windows with complementary rows kill input 2 under clean pins at every hint tested (N = 8; hint 1 lost to a checker fill artefact, recorded). **So the adversary's invariant must be extendability, and the coarse regime needs a device.**

## §7. The coarse regime reduces to a per-hint side choice with TWO hosting costs

A coarse triple (window `w`, value `a` at `u`, row `R` at `u′`, with `|R| ≥ s`) is neutralised in one of two ways:
- **EXCLUDE** `(u, a)`: string `a` becomes unhostable at `u`.
- **RESTRICT** `R` at `u′`: every string in `R` becomes unhostable at `u′`, **and** `|R|` values of extension capacity are spent there.

**Tested evidence** (exact CSP satisfiability, all hints). Q0 outputs `y >> 1` with no queries. **SMART-Q0** outputs the string excluded at the most inputs under the adversary's rule. QKILL pins the coarse values, then outputs `y >> 1`.

| template | rule | Q0 | SMART-Q0 | QKILL |
|---|---|---|---|---|
| projection N = 8 / 32 | EXCL | Q wins at every hint, 0 pins | Q wins at every hint | Q wins, 0 pins |
| projection | RESTR | adversary wins at half the hints | **Q wins at every hint** | at the good half Q needs `N` pins |
| projection | **HALF** (restrict if `u′` even, else exclude) | -- | **adversary wins at every hint** | -- |
| projection | NONE (extendability only) | adversary wins at every hint | adversary wins at every hint | Q needs `N/2` or `N` pins |
| killing chain N = 8 | EXCL | adversary wins at 16/32 | 16/32 | 16/32 |
| killing chain | RESTR | every hint invalid (kills input 2) | invalid | invalid |
| killing chain | HALF | -- | every hint invalid (both rows restricted into input 2) | -- |
| killing chain | NONE | adversary wins at 32/32 | 32/32 | Q wins at 16/32, 1 pin |

**Readings.**
- **No fixed rule of the three works for both templates.** Projections need a **balanced** choice. The killing chain needs exclusion, and HALF fails there only because a conflict-blind parity restricts both rows into input 2. **The choice must be conflict-aware on extension and spread on hosting.**
- **NONE** (the extendability invariant alone) already prices the killing chain at `Ω(N)` against the natural exploiter. The side devices exist for hosting under an **adversarial choice of output**, which SMART-Q0 embodies.
- The killing chain's losing hints under EXCL are **`M_res` strings of that template's own unary windows**: W29's term, not a failure of the side choice.

## §8. Errors and misses

**Mine:** "projection: restrict". I misremembered W10's device (it is the balanced, random-half regime, W12 §3) and priced it without checking; the smart zero-query Q refuted it. The `N^{1/k}` exponent and §5D's "shrink" belong to W27, not here. **Reviewer's (its tenth miss):** the self-exclusion count bounded the sum over strings rather than the maximum, so exclusion concentrated on `y >> 1` on its own positive control. Also its W31 draft omitted restriction's hosting cost, corrected before registration.
**Practice line: EVERY DEVICE THAT REMOVES VALUES FOR EXTENSION ALSO REMOVES STRINGS FOR HOSTING -- TEST IT AGAINST THE Q THAT OUTPUTS THE MOST-REMOVED STRING.**

## §9. Next: W31, the side assignment

Per hint: coarse triples are edges, each taking one side. RESTRICT consumes extension capacity at `u′` and adds `R` to `Excl(u′)`; EXCLUDE adds `a` to `Excl(u)`. Hosting needs, for every `v`, `|{u : v ∉ Excl(u)}| > qw(D′ + 1) + pins`. Candidate (the reviewer's): greedy with a capacity check and random tie-breaking.
