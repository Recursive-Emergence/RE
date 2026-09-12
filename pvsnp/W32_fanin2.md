# W32-A: all fan-in-2 depth-1 glue. Pre-registration

*Drafted 2026-09-12 on branch `w32-correlated-assignment`, on the reviewer's re-aimed specification. Supersedes the object of `W32_correlated_assignment.md` §0-§2 (see its §4A). Documents only; `formal/` closed; LOCAL commit only.*

**Committed before any computation.**

## §0. Target (the reviewer's)

**Every template whose windows read at most two inputs** (Definition 9, deterministic, depth 1). Plan: pre-pin the `h ≤ 2N/D*` inputs of degree `> D*`; the windows through them become unary or arity 0 and are counted over hints as in W29.2 with **arbitrary** `a_H`; run W31.1's biased coin on the arity-2 residual windows. The two effects combine **multiplicatively**, `hosting ≥ (N − h − M_res)·μ/4`, because the coin is independent of `a_H`. Near-full rows are handled by collision-based must-exclude with a coin over the choice. Claim: `qw = Ω(N)` with an absurd constant.

## §1. Audit before priors

**(Q1) THE INDEPENDENCE CLAIM HOLDS.** The unary forbiddances are fixed by `a_H` and `y` before the coin, so `E|{u ∈ U_v : v coin-hostable at u}| = |U_v|·μ`, and McDiarmid applies unchanged. **But two things must be carried:**
- **W31.1's repair loss is absolute, not relative.** It is bounded against `N` (`≤ Nμ/4` under the corrected (C1), W31 §11), while the coin's margin is now `|U_v|μ/2`. With `|U_v| ≥ N/8`, (C1) must tighten to **`D_in·p_cap ≤ μ/128`**.
- **§11's erratum applies here:** the W31 constant was off by a factor of 2.

**THE RECOMBINATION FAILS AT EXTENSION CAPACITY, which the specification does not track.** The unary residual windows (from pre-pinning) and the arity-2 rows act on the **same inputs' domains**. At a good hint W29.2 guarantees only that the unary forbidden mass at `u` is `< 2N`; it can be `2N − 1`, leaving one value. Then **no** coarse row can be restricted at `u` and fine rows fail W28.1's `D·s` count, so everything must be excluded, and exclusion concentrates (the W30 lesson). **A capacity-aware count over hints must bound unary forbidden mass below a fraction `θ·2N` at every input.** Rebalanced: `#{y : mass ≥ θ·2N at some u} ≤ (#unary windows)/θ`; with bad_clean this totals `≤ N/θ`. bad_M at threshold `m` is `≤ 2N²/m`. **With `θ = m/N = 0.9`: `1.11N + 2.22N = 3.33N < 4N`, leaving `≈ 0.67N` good hints**, so the count survives. But then:
- `|U_v| ≥ N − h − 0.9N` forces **`h < N/10`**, i.e. `D* > 20`;
- the remaining capacity is only `0.2N` values, so fine rows need `D*·s < 0.2N`, i.e. **`s < N/100`**, and **almost every row is coarse**. A coarse row of size above `0.2N` **cannot be restricted at all**, so it must be excluded, and exclusion's concentration returns.

**So the recombination's crux is not only (Q2) near-full rows but capacity after unary forbiddances.** The theorem needs either (i) a count showing that exclusions forced by exhausted capacity spread across strings, or (ii) a hypothesis bounding unary forbidden mass per input. **My expectation: (i) is the sum-versus-max question once more.** A template where pinned hubs forbid most values at the partners of near-full rows that all carry one value string is the natural kill template, extending the reviewer's.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **32a** fan-in-2 theorem, any glue, `Ω(N)`, constant stated | 35 | **20** |
| **32b** theorem under a near-full-row or capacity hypothesis, kill template as gap | 45 | **45** |
| **32c** nothing | 20 | **35** |

**Why 32a below the reviewer:** §1's capacity finding. The plan's pieces are proved, but the recombination has to pass through a max (exclusions forced by exhausted capacity) that none of the pieces controls. **Why 32c up:** the line's recombinations have failed in the middle repeatedly, and this one already shows a middle it did not price.

## §3. Flags

- **A32 -- capacity after unary forbiddances first:** state and check the rebalanced count (§1) exactly.
- **B32 -- the kill template:** pinned hubs that exhaust capacity at partners of near-full rows carrying one value string. Build it at N = 16 and compute exact hosting under the best heuristic assignment.
- **C32 -- controls:** projections, killing chain, and random fan-in 2 (`h ≈ 0`).
- **D32 -- constant honestly** (proof-of-shape), once a statement survives.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §1A. Amendment -- my capacity objection over-counted: few inputs are exhausted at a good hint (before any computation)

**§1 required unary forbidden mass below `θ·2N` at EVERY input. That was the wrong quantifier, and a max error in the pessimistic direction.** Count pairs instead: `Σ_y Σ_z (unary mass at z for y) = 2N·(#unary windows) ≤ 2N²`, so `#{(y, z) : mass ≥ θ·2N} ≤ N/θ`. By Markov, the hints at which more than `K` inputs are exhausted number at most `N/(θK)`. **Rebalanced good hints:** `4N − N (clean/ext) − 8N/3 (M_res ≥ 3N/4) − N/(θK) > 0` whenever `θK > 3`, e.g. **`θ = 1/2, K = 7`**. So at a good hint **at most 7 inputs have less than half their domain**, not all of them.

**Consequences.** (a) The low-capacity inputs are `O(1)` per hint. Treat them as **additionally pre-pinned** (value chosen among their allowed values); that adds at most `7·D*` unary windows elsewhere, a bounded second round of the same count. (b) Every other input keeps capacity `≥ N`, so fine rows need only `D*·s < N/2`, and restriction is available for rows that fit. (c) **The kill template in capacity form cannot exist:** no template exhausts many inputs at a constant fraction of hints, by the pair count. **What remains of the crux is (Q2), near-full rows colliding at one `u′`.** Collision-based must-exclude with a coin over the maximal non-colliding choice costs each incidence a factor about `1/D_in` instead of `1/2`, so the constant is about `D*^{−O(D*)}` for `D* ≈ 20`, still `Ω(N)`.

**Priors are not revised** (committed at c97502b). **§1's reason for pricing 32a low is half withdrawn**: the capacity obstacle dissolves by a pair count. The near-full-row collision cost is the half that stands.

## §3A. B32 data -- the near-full collision template does not kill

**Template (N = 16).** Value inputs 0-7 and row inputs 8-15. Row input `8 + j` receives two windows, from `u = j` and `u = j + 1 (mod 8)`, with **complementary half rows** (`(a << 1) | b₀` and `(a << 1) | (b₀ ⊕ 1)`). Every value input therefore has two out-edges carrying the **same** string `y >> 1`, and every row input has a colliding pair. **Rule:** at each row input restrict exactly one of its two rows and exclude the other, chosen either **ALTERNATING** (by `j` parity) or by a **COIN**. Exact CSP, all 64 hints:

| rule | `min_v |hostable(v)|` |
|---|---|
| ALTERNATING | **8 = N/2 at every hint** |
| COIN (two seeds per hint) | 0:1, 2:4, 3:4, 4:22, 5:20, 6:26, 7:24, 8:27 |

**The collision template does not force exponential or concentrated loss.** A structured choice (restrict the row from the even-indexed neighbour) keeps every string hostable at half the inputs, and a coin reaches `N/2` often. In a ring of `m` value inputs, `m/2` can have both their out-edges restricted, which is the analysis behind the ALTERNATING row. **Evidence that (Q2) costs a constant per collision, consistent with §1A.**

---

# W32-A Findings

*Appended after the reviewer's rulings on the cascade, on coarse-triple multiplicity, and on the protected-set mechanism. Nothing above is revised.*

## §4. Ceiling

**Korten's Definition 9 model only; deterministic only; fan-in `≤ 2` only; depth 1, `n′ = n`.** The constant is proof-of-shape. **Not touched:** Korten's Problem 1 at polynomial fan-in, randomised reductions, and the arity-`k` middle band (W32-B). **The theorem below is CONDITIONAL on a cascade hypothesis**, and the gap is in the argument, not known to be in the truth.

## §5. Outcome against priors

| code | c97502b mine / reviewer | reviewer final | outcome |
|---|---|---|---|
| 32a unconditional fan-in-2 theorem | 20 / 35 | 10 | -- |
| **32b** theorem under a hypothesis, gap named | 45 / 45 | 75 | **the outcome: W32.1 under (H_casc); the multiplicity gap closed by the protected set** |
| 32c nothing | 35 / 20 | 15 | -- |

## §6. Two gaps found in the recombination, and what happened to each

**(a) The cascade -- OPEN; named gap.** Pinning a half-exhausted input `z` to a value turns every arity-2 window `(z, u)` into a fixed row at `u`. That row can be near-full and exhaust a healthy partner, starting another round, with up to `D*` times more damage per round. The reviewer's audit bounded the effect on `c(y, v)` (a count per string) but not on **mass** at partners (its twelfth miss, in its words). **Fitting induced rows** are ordinary coarse rows handled by the collision coin at multiplicity `≤ K`. **Near-full induced rows are not.** A count over `(y, z, a)` cannot localise the bad incidences (about `8N·D*` per window over all hints) to the at most `2N` exhausted pairs, since a template may align them. Choosing the **lightest** value per hub leaves total exhaustion mass `≤ 4N` at a good hint (at most 4 exhausted inputs), but not pinning them only moves the near-full induced row to the other direction. **Not exhibited:** a template exploiting this. **Q does not know `a_H`**, so it cannot cheaply locate the exhausted input.

**(b) Coarse-triple multiplicity -- CLOSED by the protected set (the reviewer's mechanism, audited here).** W31.1's `D_in` counts coarse **triples**, one per value with a large row, so a single window contributes up to `|E_w(y)|/s` of them. **W31 §8's gloss "bounded degree" is wrong and is corrected to "bounded coarse-triple multiplicity"** (a shared miss: I wrote the gloss, the reviewer approved it). **The per-window vertex cover is the product-family formulation restated, not a repair.** The repair is to make hosting a per-input event:

**Protected set.** Choose an independent set `P` in the coarse-edge graph. For `u ∈ P`, every coarse triple incident to `u` is **paid by the partner**: a triple with value side `u` is RESTRICTED at the partner, and one with row side `u` is EXCLUDED at the partner's value side. **Then every string is hostable at every `u ∈ P ∩ U_v`, deterministically, with no per-triple loss.**

**(Q1) audit -- the payer's mass: HOLDS.** For one protected neighbour across window `w`, the partner loses `Σ_{coarse values b at u} |column_b| + #{coarse values a at partner with row into u}` `≤ |E_w(y)| + |E_w(y)|/s`. **The multiplicity of triples never enters; only the window's mass does.** Two caveats the proof must carry: (i) **heavy windows.** `Σ_y Σ_w |E_w(y)| = 4N³`, so the pairs `(y, w)` with `|E_w(y)| ≥ λN` number at most `4N²/λ`, i.e. about `N/λ` per hint on average. Their endpoints are removed from `P` and from the payers by a Markov step over hints. (ii) **Unprotected pairs** are resolved by exclusion. That costs an unprotected input at most `Σ_w |E_w(y)|/s ≤ λD*²` values, small at `s = N/(2D*)`. **Payer capacity** `c ≈ (2N − D*·s − λD*²)/(λN(1 + 1/s))`, a constant for constant `λ`. **A random-order greedy independent set** in which each outside vertex has at most `c` protected neighbours has marginal `≥ c/(D* + c)` at every input. McDiarmid applies to the order (one swap moves `≤ D* + 1` inputs). So **`|P ∩ U_v| = Ω(|U_v|/D*)` for all `v`**: polynomial in `D*`.

**Separation test, the STAR template (exact CSP, N = 16).** Ring windows `(x, x+1)` with glue `8·α(a) + β(b)` (classes of size 4), so every `E_w(y)` is a `4 × 4` complete bipartite set, and every row and column is coarse. **Protected set (alternating): min over `v` of hosts = 8 = N/2 at every hint tested (13 hints). Fair coin with exact capacity check: 0 at every hint and seed (26 runs).** The two mechanisms separate cleanly: the coin's per-triple loss (`2^{−inc}`, with `inc ≈ 10` here) is real, and the protected set removes it.

## §7. Theorem W32.1 (conditional)

> **Theorem W32.1.** *Definition 9, deterministic, depth 1, `n′ = n`. Let every C′-input read at most two C-inputs, with arbitrary glue. Pre-pin the inputs of degree `> D*` (`h ≤ 2N/D*`) to the lightest values. Assume* **(H_casc)**: *at some good hint, every exhausted input (fewer than `t` allowed values) has an allowed value whose induced rows all fit their partners' capacity. Then every back-mapping correct on all valid hints has* **`qw = Ω(N/D*²)`**, *with constants of proof-of-shape size (`D* = 20`, `λ = 8`, `K = 8`, `t = 6`, `M_res < 7N/8`).*

*Proof structure* (every count audited in §6 and in the reviewer's rulings): **good hints** (clean/ext at `2N − t`; `M_res < 7N/8`; at most `K` exhausted inputs; heavy windows at most `N/λ`), leaving `≥ 0.4N` hints; **(H_casc)** resolves the exhausted inputs; the **protected set** gives `|P ∩ U_v| = Ω(|U_v|/D*)` with `|U_v| ≥ N − h − M_res ≥ N/40`; **extension** at payers and unprotected inputs by W28.1's count with capacity `≥ D*·s`; **hosting** under Q's pins by W28/W29's almost-full count, dividing by `D′ + 1 ≤ D* + 1`. *The explicit constant is left at its shape, with the heavy-window Markov step flagged as the one count audited only in outline.*

**(H_casc) on the controls, analytic check.** Hub, two-hub and parity-hub (lightest/kill value), the killing chain, B32's ring, the star template, projections and random fan-in 2: in every case each unary window, original or induced by the hub pin, forbids **at most one value** per input at each hint. So unary mass is at most the degree (`≤ 3`), no input is exhausted, and (H_casc) holds vacuously.

**Consistency.** W10.3 (projection glue, `N/8`) and W12.2 (one-input glue, `N/9`) are `h = 0` special cases with far better constants; W29.2 is the unary case. W32.1 is weaker than each of them on its own class and covers all fan-in-2 glue under (H_casc).

## §8. Named gap, and the W32-B warning

**Gap:** templates where every good hint has an exhausted input all of whose allowed values induce a near-full row. The localisation count fails (bad `(window, a, y)` incidences, about `8N·D*` per window, cannot be charged to the at most `2N` exhausted pairs), and no such template has been exhibited. **Warning carried to W32-B:** the cascade will reappear at arity `k` as induced `(k − 1)`-slices, and multiplicity as slice counts. W32-B must state its hypotheses on both from the start.

## §9. Errors and misses

**Mine:** W31.1's (C1) arithmetic (erratum W31 §11); §1's capacity objection (a max error, withdrawn in §1A); the "bounded degree" gloss (shared). **Reviewer's:** the cascade audit (twelfth miss); the gloss approval (shared). **Practice line: AUDIT THE QUANTITY THE ARGUMENT NEEDS, NOT THE TERM YOU DEFINED FOR IT** (mass at partners vs `c(y, v)`; triples vs windows).

## §10. The heavy-window step, written out at the reviewer's request -- IT FAILS; W32.1 needs a second hypothesis

**The count.** `Σ_y Σ_w |E_w(y)| = N·(2N)² = 4N³`, since each pair `(a, b)` of a window maps to exactly one hint. There are `4N` hints and `N` windows, **so the AVERAGE mass per `(y, w)` is exactly `N`.** Markov gives `#{(y, w) : |E_w(y)| ≥ λN} ≤ 4N²/λ`, so a fraction `1/λ` of all `(y, w)` pairs, **and nothing better**.

**The capacity it must meet.** A payer serving one protected neighbour across `w` loses `|∪_{coarse b at u} column_b| + #{coarse a with row into u}`, and the union can be as large as `|E_w(y)|`. Its capacity is `2N − D*·s`, about `1.5N` at `s = N/(2D*)`. **So a window is unpayable once `|E_w(y)| > 1.5N` or so, i.e. `λ ≈ 1.5`, and Markov then permits up to `2/3` of all `(y, w)` pairs to be heavy.** A hint count can only make heavy windows rare at `λ ≫ 1`. **The two requirements do not meet:** payers need `λ < 2`, and rarity needs `λ` large. §6(b)'s caveat (i) ("removed by a Markov step over hints") is **wrong**. The §7 proof structure's line "heavy windows at most `N/λ`" does not deliver a usable `λ`.

**Why the star template passed.** Its coarse columns coincide (every column is the same `α`-class), so the union removed is 4, not 16. Coarse structure with **overlapping** projections is cheap to pay. Coarse structure with **spread** projections is not, and nothing in the counts forces overlap.

**A structure that is unpayable in both directions but trivial.** Take `E_w(y) = ({a₁} × all) ∪ (all × {b₁})`, of mass about `4N`. This occurs at `N` of the `4N` hints per window, and a template can stagger windows so a constant fraction are of this type at every hint. Protecting `u` forces the partner to restrict the column of `b₁` (all values): dead. Protecting `u′` is symmetric. **Yet the window is just two unary forbiddances** (`C(u′) ≠ a₁`, `C(u) ≠ b₁`). **The payer model is wasteful here**: the right move lets the protected input lose the few values whose columns are huge, **at the cost of hosting those strings at `u`**. Whether those losses concentrate on one string across inputs is the sum-versus-max question again. Its extreme case (`E = all × {y >> 1}` everywhere) is certified at `q = 0`, so W25.1 caps it at `2N` hints, which suggests a count may close it. **Not done.**

**Status of W32.1, corrected.** W32.1 holds under **(H_casc)** and **(H_mass)**. **(H_mass):** at some good hint, every window incident to the protected set has coarse payer cost below its payer's capacity. **The controls satisfy (H_mass)**: the star template by coincident columns, and the rest because coarse mass is `≤ N` with overlapping projections, or zero. **Gap (b) is therefore NOT fully closed.** Multiplicity is removed, but **window mass** replaces it as a hypothesis. The named repair is "protected inputs may lose huge-column values", with a W25.1-type count for their concentration. **Scoring unchanged (32b), with two named gaps: the cascade, and window mass.** *The reviewer's instruction to write out this step is what caught it.*

## §11. Pre-registration: discharging (H_mass) by give-ups -- audit before measuring

**The reviewer's rule.** Protected `u`, payer `u′`, `s = N/(8D*)`. **Tier 1:** the payer restricts coarse columns of `u`'s values up to its capacity (about `1.75N`). **Tier 2:** if the union still exceeds that, `u` **gives up** values (each costs one string one host at `u`), choosing by **load balancing** (least-loaded strings first). The reviewer claims (γ): give-up load per string is `O(D*)` per hint, an **additive** loss.

**Audit of (γ): the additive claim is WRONG, but a multiplicative version closes.** Load balancing cannot spread give-ups beyond the candidates a window offers. Suppose at a hint every protected input's heavy window has coarse columns for the **same two strings** `{v₁, v₂}`, each of size `0.9N` with spread supports (union `1.8N > 1.75N`). Then every window gives up one of the two, and **balanced, each string is given up at `|P|/2` inputs**: load `Θ(N/D*²)`, not `O(D*)`. **Does the per-string budget (β) forbid it?** A string with a column of size `0.9N` at all `N` windows uses `0.9N²` of its `2N²` budget, so it can do this at about 2 hints; two strings per hint then cover only about half the hints. **It is not forbidden at a constant fraction of hints.** But the loss is **multiplicative and bounded**: a window with `m` coarse candidates gives up at most `m − 1`, balanced to a fraction `≤ (m − 1)/m` per string. **So hosts(v) ≥ |P ∩ U_v|/m_max − (|P| − |P ∩ U_v|)**, which needs `U_v` large (it is `≥ (1 − ε)|P|` only if `M_res` is small, a point to carry) **and `m_max` bounded.**

**Bounding `m` by a count over hints.** `m ≤ |E_w(y)|/s`. Call `(y, w)` **super-heavy** if `|E_w(y)| ≥ M·s`. Their number is `≤ 4N³/(M·s) = 32D*N²/M`. Hints with more than `J` super-heavy windows number `≤ 32D*N²/(MJ)`. Taking `J = N/(100D*²)` (the excluded endpoints `2J` are small against `|P| ≈ N/D*²`) and `M ≥ 32000·D*³` leaves at most `0.1N` bad hints. **So `m_max ≤ M = poly(D*)` at a good hint, and the loss is `1/poly(D*)`, still polynomial.**

**(δ) audit: HOLDS under `c = 1`.** Each payer serves one protected input, so give-ups at different protected inputs never compete for the same payer slot. Two windows at the same `u` forcing the same `v` out cost `v` one host, `u`.

**Carried point:** the bound `hosts(v) ≥ |P ∩ U_v|/m − …` needs `|P ∩ U_v| ≥ (1 − ε)|P|`. With `M_res < 7N/8`, `U_v` can miss most of `P`. **The multiplicative give-up loss and the `M_res` loss compound**, and the combination must be `hosts(v) ≥ |P ∩ U_v ∩ NotGivenUp(v)|`, with `P` random and independent of `a_H`, so the two losses multiply in expectation. **To be checked in writing.**

**Priors on (H_mass) closing:** reviewer 35; **mine 45**. Up, because the multiplicative version has a clean count behind `m`. Down from higher, because the compounding with `U_v` and the random-`P` independence under a give-up rule that **depends on loads** (and so on `P`) are unverified. **The load-dependent rule breaks the independence of `P` from the give-up pattern that the McDiarmid step needs; a load-OBLIVIOUS rule (give up uniformly at random among candidates) may be required.**

**Measure first (reviewer's instruction):** at N = 16, a rotating two-string heavy template, measure per-string give-up fractions under (i) load-balanced and (ii) uniform-random give-ups, against `(m − 1)/m`.
