# W36: arity-3 split-payment collisions. Pre-registration (one bounded round; the black-box sub-line rests after it unless a user redirects)

*Drafted 2026-09-12 on branch `w36-arity3-collisions` (from `w35-arity3-density`). Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before any computation.**

## §0. Target (the reviewer's)

At a dense hint, each window `w` has heavy strings `H_w` (at most about `16D*` at average mass, union-bounded at heavy windows). Each needs a two-sided split with a parity-class (in general, a partition-class) choice at each of its two payers. A payer takes at most one split. **Question:** is there an assignment of splits, and give-ups for the losers, such that every heavy string keeps `Ω(|P|/poly(D*))` protected inputs where it is paid? The reviewer expects W32-A §11's random-choice `(m − 1)/m` loss to apply per payer. **Kill template:** two heavy strings per hint with incompatible classes at every payer.

## §1. Counting done before the prior

**(a) Survival is a product again, and the loss is a constant for fixed `D*`, not polynomial.** A heavy string `v` hosted at protected `u` needs **both** payers of **each** window through `u` where `v` is heavy to take `v`'s split. With a uniform random choice among `≤ 16D*` heavy strings per payer slot, a window contributes `≥ (16D*)^{−2}`, and `u` has at most 3 windows at arity 3 in a ring (`D*` in general). **Survival `≥ (16D*)^{−2D*}`**: a constant at fixed `D*`, exactly W32-A §12's shape. The target "`Ω(|P|/poly(D*))`" should read **`Ω(|P|·D*^{−O(D*)})`**.

**(b) CAPACITY IS SHARED between assignment exclusions and a split.** A split costs about `N` at a payer, and the normal strings' assignment exclusions cost `p·16D*N`. With capacity `1.275N`, **both fit only if `p·16D*N ≤ 0.275N`, i.e. `p ≤ 1/(58D*)`**: still polynomial, but the constant must be written with it.

**(c) Payer slot coordination within a window.** Both payers of a window must choose the **same** heavy string, or the split is half-paid and useless. **Choose per window, not per payer:** the window picks one heavy string `v` and both payers restrict. But a payer lies in up to 3 windows at arity 3 (`D*` in general), and each window through it that carries a protected input wants its slot. **Under `c = 1`** (each payer adjacent to one protected input), the windows through a payer with protected inputs all share **that** protected input, so they can choose consistently. With two windows through the same `(u, payer)` pair choosing different heavy strings, only one is paid. **A per-(protected input, payer) choice** is the right granularity, and it still gives a constant.

**(d) The kill template.** With two heavy strings per hint at every payer using incompatible classes, a per-`(u, payer)` coin gives each string about `1/4` per window (both payers agree on it with probability 1/2 each, if chosen independently), or `1/2` if the choice is shared across the window's two payers. **A constant fraction, not everything.** I expect the kill template to pass.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **36a** arity-3 theorem at fixed `D*` (proof-of-shape) | 35 | **45** |
| **36b** collision count fails on the kill template, residue named | 45 | **35** |
| **36c** nothing | 20 | **20** |

**Why 36a above the reviewer:** §1(a)-(d) find no obstruction beyond constants; the shared-capacity constraint (§1(b)) and the coordination granularity (§1(c)) are both settled by constant choices. **Why not higher:** heavy strings at positions 1 and 2 (cheap keys) and at position 0 (splits) at the **same** payer mix the two payment types, and I have not priced that interaction.

## §3. Flags

- **A36:** audit §1(a)-(c) with the reviewer before any computation.
- **B36:** kill template, combinatorial (no CSP), at `|P|` large: two incompatible heavy strings per hint at every payer, measuring per-string paid fractions under per-window choice.
- **C36:** one round; then the sub-line rests.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# W36 Findings

*Appended after the reviewer's A36 rulings (36a). Nothing above is revised.*

## §4. Ceiling

**Definition 9, deterministic, depth 1, `n′ = n`, fan-in `≤ 3`, arbitrary glue.** The constant is proof-of-shape, at astronomical `N`. **Arity `≥ 4` is open** (hitting sets over tuple keys). Everything else is as in W32.1's ceiling: nothing randomised, nothing beyond depth 1, **nothing across the weakest arrow** (W33 PATH).

## §5. Outcome against priors

| code | mine / reviewer | outcome |
|---|---|---|
| **36a** arity-3 theorem at fixed `D*` | 45 / 35 | **achieved -- Theorem W36.1** |
| 36b | 35 / 45 | -- |
| 36c | 20 / 20 | -- |

**Reviewer's correction recorded:** its target "`Ω(|P|/poly(D*))`" is `Ω(|P|·D*^{−O(D*)})`, the same slip as at W32-A §12.

## §6. Theorem W36.1

> **Theorem W36.1.** *Definition 9, deterministic, depth 1, `n′ = n`. Every template in which each C′-input reads at most three C-inputs, with arbitrary glue, satisfies* **`qw ≥ c₃(D*)·N` for `N ≥ N₀(D*)`**, *with `c₃(D*) = D*^{−O(D*)}`.* **Proof-of-shape.**

**Ledger: what each round supplies.**

| ingredient | source |
|---|---|
| exhaustion, forced chains, `M_res` | **density** (W34): dense hint `≥ 0.7`, density-maximising hub branch |
| bounded degree | pre-pinning inputs of degree `> D*` (W29, W32-A) |
| strong independence with `c = 1` | protected inputs every fifth input in a ring (marginal about `1/(kD*)²` in general) (W32-B, W36 §1(c)) |
| normal strings | string-to-input assignment with unary partner exclusions, `p ≤ 1/(58D*)` (W35) |
| heavy strings (`|B_v| ≈ 2N`) | split payment with per-`(u, payer)` coordination (W35 §3A, W36 §1(c)) |
| capacity (§7) | W34's `1.4N` values per input at the dense branch |
| survival of a heavy string | `≥ (16D*)^{−2D*}` per protected input (W36 §1(a)) |
| concentration | McDiarmid over order and coins, union over strings, as in W32-A §12 |

## §7. The capacity check (the reviewer's arithmetic, with one correction)

At a payer: a split costs `N`; cheap-key exclusions from its protected neighbour cost `≤ p·16D*N ≤ N/58`; fine mass costs `≤ N/8`. The total `N + N/58 + N/8 ≈ 1.142N < 1.275N`. **Correction:** the reviewer concluded that the split's kept class "keeps at least `0.73N`". **But the kept class can also contain the input's unary-forbidden values**, up to `0.6N` at the dense branch, since W34 guarantees only `1.4N` usable values overall. The worst case is therefore **`N − 0.6N − N/8 − N/58 ≈ 0.26N`**. That is **still above the `D*·s = N/8` needed for W28.1's extension**, so the conclusion stands: **a cheap exclusion cannot empty a split's class, and the interaction is benign**, at a smaller margin than stated. Cheap exclusions concentrating on the kept class beyond their expectation is ruled out by the union bound over payers, as in W32-A §12.

## §8. Kill template (measured, combinatorial)

Two incompatible heavy strings at every window; ring; protected `u` with payers `u − 2, u − 1, u + 1, u + 2`. Minimum over the two strings of the paid fraction: **per-payer coin** 0.058-0.064 at `|P| = 10⁴` (exactly `1/16`: all four payers must agree), the wrong granularity; **per-`u` coin** (valid under `c = 1`) **0.491-0.499 at `|P| = 10⁴`**. A constant fraction for each string. **Passes.**

## §9. The black-box sub-line rests

**Final ledger** (all deterministic, depth 1, stretch `n ↦ n+1` to `n ↦ n+2`, below the weakest arrow):
- **W26.1** (membership model, any fan-in): `(q + 1)·k ≥ 0.58√N`.
- **W28.1** (Definition 9, small rows): `qw ≥ N/(D + 1)`.
- **W29.2** (hub plus unary): `qw ≥ N/4 − h`.
- **W32.1** (fan-in 2, unconditional after W34): `qw ≥ c(D*)·N`.
- **W36.1** (fan-in 3): `qw ≥ c₃(D*)·N`.
- **Open:** arity `≥ 4` (tuple-key hitting sets); constants; randomisation; depth `> 1`; Korten's Problem 1 at polynomial fan-in.

**No W37 is opened.** The next move (the door, or rest) is the user's.
