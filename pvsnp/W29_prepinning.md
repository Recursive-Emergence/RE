# W29: degree reduction by pre-pinning. Pre-registration

*Drafted 2026-09-12 on branch `w29-prepinning` (from `w28-extendability` at 54cdc5b), on the reviewer's W29 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed before any computation, and before re-reading W24's validity-first data.**

## §0. Target and ceiling

**Definition 9 model, deterministic, depth 1.** The adversary pre-pins a set `H` of `h` inputs to clean values `a_H` and applies W28.1's adversary to the **residual** template (`H` fixed), whose parameters are `D_res` (maximum degree outside `H`) and `t_res` (forbidden sets with `H` fixed, worst case over the remaining positions). **Reviewer's Lemma W29.1:** if `D_res·t_res < 2(N − h)`, then `qw ≥ (N − h)/(D_res + 1)`. **Reviewer's charge:** pre-pins are not added to `qw`; the free pool is `N − h − qw`, and almost-full residual windows number `≤ qw·D_res`.

**Ceiling as for W28.** Not Korten's Problem 1; nothing randomised; nothing about P vs NP.

## §1. Audit of the specification, before priors

**THE HOSTING COUNT IN W29.1 IS WRONG AS STATED.** "Almost-full residual windows are created only by Q's pins" is false. **A window whose only non-`H` position is one input `u` is almost-full at time zero**: pre-pinning makes it a **unary residual window**. Examples: every hub window `(x, hub)`, and every parity-hub window. Its forbidden set at `u` is **fixed before Q moves**, and Q can aim its output at it. W28's count `≤ qwD` held because with `h = 0` every almost-full window contains a Q pin. **With `h > 0` it does not.**

**Corrected accounting.** Let `M_res(a_H) = max_v #{u ∉ H : some unary residual window at u forbids v}`. Q's output `v` is rejected at a free `u` only if an almost-full window through `u` forbids it: either a unary residual window (at most `M_res` inputs, for the worst `v`) or a window completed by Q's pins (at most `qw·D_res`). So the adversary wins if

  **`N − h − qw − qw·D_res > M_res`**, i.e. **`qw < (N − h − M_res)/(D_res + 1)`**,

together with `D_res·t_res < 2(N − h)` for extendability (step (ii) runs unchanged on the residual). **`M_res` is W14's dangerous string made quantitative:** a string forbidden at many inputs by windows that pre-pinning has made unary.

> **Lemma W29.1 (corrected candidate).** *If clean pre-pins `a_H` give `D_res·t_res < 2(N − h)`, then every back-mapping correct on `y` has* **`qw ≥ (N − h − M_res(a_H))/(D_res + 1)`**.

**Consequences for the reviewer's controls, predicted now.**
- **(1) Hub, `h = 1`.** With the hub's low bit `≠ y`'s, every window's forbidden set at `x` is empty: `t_res = 0`, `M_res = 0`, `D_res = 1`, so `qw ≥ (N − 1)/2`. **Killing matters here after all**: with the other value, every window forbids `y >> 1`, so `M_res = N − 1` and the bound is vacuous. Choosing the kill value **is** validity-first.
- **(2) Two-hub, `h = 2`.** XOR `≠ y`'s bit kills every window: `M_res = 0`, `qw ≥ (N − 2)/2`.
- **(3) Parity-hub.** When `y`'s two bits differ, any hub value leaves half the windows live, each forbidding `y >> 1` at its `x`: `M_res = N/2`, `t_res = 1`, `D_res = 1`. **So `qw ≥ (N/2 − 1)/2 ≈ N/4`, NOT the reviewer's predicted `≈ (N − 1)/2`.** Killing is unnecessary for a nonvacuous bound, as the reviewer claimed, but it costs a factor 2.
- **(4) Many medium-degree inputs:** pre-pin all inputs of degree `> D*`. Then `h ≤ kN/D*`, and the bound `(N − h − M_res)/(D* + 1)` is at best about `√(N/k)` **when `M_res` is small**. **A tool for few-hub templates, not a replacement for W28.1**, as the reviewer says.

**The kill test, restated with `M_res`:** a template where **every** clean `a_H` makes `M_res ≈ N − h` (fixing the hubs forces a dangerous string at almost every residual input), or makes `t_res ≥ 2(N − h)/D_res`. **Note:** a string forbidden at every input for every hub value is blocked unconditionally, so its hint certifies at `q = 0`, and W25.1 bounds such hints by `2N`. **So the coupling template must make the dangerous string depend on `a_H`, with no `a_H` free of one.**

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **29a** W29.1 proved, controls landing, parity-hub included | 45 | **35** |
| **29b** W29.1 holds, but a coupling template shows the residual hypothesis failing for a natural class, gap named | 40 | **50** |
| **29c** nothing | 15 | **15** |

**Why 29a below the reviewer:** the specified hosting count was wrong, and the corrected lemma carries `M_res`, which is exactly the quantity a coupling template attacks. The parity-hub prediction also changes (`N/4`, not `N/2`). **Why 29b up:** the residue now has a precise name (`a_H`-dependent dangerous strings), and building one at n = 3 or 4 looks feasible.

## §3. Flags and kill tests

- **A29 -- `M_res` on every line.** No hosting count without it.
- **B29 -- controls in order** (hub, two-hub, parity-hub), each with `h, D_res, t_res, M_res` computed exactly, for the best and the worst `a_H`.
- **C29 -- executable check:** W28's aggressive-Q harness extended with pre-pins, on parity-hub at N = 64 and 256, with `qw` just below the corrected bound **and** just above the reviewer's uncorrected one. **If the adversary loses above `N/4` but below `N/2`, the correction is confirmed in code.**
- **D29 -- coupling search** at n = 3 and 4: templates with one or two hubs where `min over clean a_H of M_res` is large at every hint not certified at `q = 0`.
- **E29 -- stop-rule:** a coupling template found, or `M_res` shown irrelevant, goes to the reviewer before writing.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
