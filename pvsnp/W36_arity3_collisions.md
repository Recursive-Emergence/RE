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
