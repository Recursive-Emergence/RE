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

## §3A. Amendment -- my own correction was loose; the lemma sharpened (before any computation)

*The reviewer's ruling accepted §1 in full, including the `N/4` prediction for parity-hub. It crossed this self-audit, which withdraws that prediction.*

**§1's `qw·D_res` term over-counts.** It counts windows that Q's pins make almost-full. A **unary** residual window is almost-full already; its forbidden set is fixed and **Q's pins cannot add rejections through it**. Q-created almost-full windows come only from residual windows of **arity ≥ 2**. Sharpened:

> **Lemma W29.1 (sharpened candidate).** *If clean pre-pins `a_H` give `D_res·t_res < 2(N − h)`, then every back-mapping correct on `y` has* **`qw ≥ (N − h − M_res(a_H))/(D′_res + 1)`**, *where* `D′_res` = max over `u ∉ H` of the number of residual windows of arity `≥ 2` through `u`.

**Both corrections are needed:** `M_res` (missing from the specification; the hub with its non-kill value breaks the uncorrected proof step) and `D′` (my over-count). **Parity-hub prediction REVISED:** every residual window is unary, so `D′_res = 0`, and the adversary chooses the hub value leaving the smaller live half (`N/2 − 1` inputs), so `M_res = N/2 − 1` and **`qw ≥ N/2`**. **The reviewer's original `≈ (N − 1)/2` was right; my `N/4` came from my over-count, not the phenomenon.** Matching exploiter: one query for the hub bit, pins on the `N/2` dead inputs, then output `y >> 1`, so `qw = N/2 + 1`. Hub and two-hub predictions unchanged (`M_res = 0` at the kill value; `(N − 1)`, `(N − 2)` with `D′ = 0`, strictly above the §1 figures).

**Recorded sentence (the reviewer's request): `M_res` is W14's dangerous string made quantitative, and the adversary's choice of `a_H` is the forced-bit invariant on the read structure, minimising `M_res`.**

---

# W29 Findings

*Appended after the reviewer audited every step of Theorem W29.2 and scored the round. Nothing above is revised.*

## §4. Ceiling

**Korten's Definition 9 model (width-`w` DNF queries), deterministic, depth 1, `n′ = n`.** W29.2's class: **every window reads at most one input outside a fixed set `H` of `h` inputs.** Not Korten's Problem 1; nothing randomised; nothing about P vs NP.

## §5. Outcome against priors

| code | mine / reviewer (reviewer later) | outcome |
|---|---|---|
| **29a** W29.1 proved, controls landing | 35 / 45 (40) | **achieved -- W29.1 with both corrections, controls exact, C29 tight to within one, and Theorem W29.2 answering the kill test** |
| 29b coupling template shows the residual hypothesis fails | 50 / 40 (45) | -- **in the unary-residual class, no coupling template can exist (§8)** |
| 29c nothing | 15 / 15 | -- |

**The resolution is not the pre-registered one in the direction I leaned.** I put 29b at 50 because `M_res` looked attackable by a coupling template. The count over hints (Move 1) shows such a template cannot exist whenever the residual is unary.

## §6. Lemma W29.1 (as it stands)

*Pre-pin `H` to clean `a_H`. Extension holds if `D_res·t_res < 2(N − h)`. Hosting holds if* **`qw < (N − h − M_res)/(D′_res + 1)`**, *with `M_res = max_v #{u ∉ H : some unary residual window at u forbids v}` and `D′_res` = max over free inputs of the residual windows of arity `≥ 2` through them.*

**Why `M_res` is there (the hub example).** Pre-pin the hub to its **non-kill** value. It is clean, `t_res = 1`, `D_res = 1`, yet every unary residual window forbids `y >> 1`, and a zero-query Q outputting `y >> 1` cannot be hosted by that adversary. This breaks the **proof** of the uncorrected count, though not necessarily its conclusion. **`M_res` is W14's dangerous string made quantitative**, and the adversary's choice of `a_H` is the forced-bit invariant on the read structure, minimising `M_res`. **Why `D′`:** a unary residual window is already almost-full and its forbidden set is fixed, so Q's pins make new almost-full windows only through arity `≥ 2`. *Corrections:* `M_res` was missing from the reviewer's specification (its ninth miss: "killing is not required" was wrong); `D′` corrects my own over-count, and my `N/4` parity-hub prediction is withdrawn.

## §7. Controls and C29

**Exact residual parameters** (N = 8 and 16, hints 0-3, best and worst `a_H`):

| template | best `a_H`: t, D, D′, M -> bound | worst `a_H`: M -> bound |
|---|---|---|
| hub | 0, 1, 0, 0 -> **N − 1** | N − 1 -> 0 |
| two-hub | 0, 1, 0, 0 -> **N − 2** | N − 2 -> 0 |
| parity-hub | 1, 1, 0, N/2 − 1 -> **N/2** | N/2 -> N/2 − 1 |

Every prediction of §1 and §3A landed on every hint.

**C29 (executable).** (a) Hub, non-kill `a_H`, zero-query Q outputting `y >> 1`: **the adversary cannot host at N = 64 and 256**; with the kill value it can. This is the positive control for the `M_res` term. (b) Parity-hub, best `a_H`, the exploiter (hub-bit query, then pins on the dead half, then output `y >> 1`): **Q first wins at `qw = 33` (N = 64) and `qw = 129` (N = 256), against the bound `qw < N/2`.** **The hosting count is tight to within one on this template**, a data point that the count is exact on unary residuals.

## §8. Theorem W29.2 -- hub-plus-unary templates

> **Theorem W29.2.** *In Definition 9, let `H` be a set of `h` inputs such that every window reads at most one input outside `H`. Then every deterministic back-mapping correct on all valid hints has* **`qw ≥ N/4 − h`**, *for any glue values and any width.*

*Proof.* Fix **any** `a_H`. Each of the `N` windows is either H-internal (arity 0, outputs one hint) or unary at one free input `u`. For a unary window `w`, let `F_w(y) = {v : g_w(v) = y}`.
- **bad_clean:** `a_H` is non-clean for `y` iff an H-internal window outputs `y`, so at most (#H-internal windows) hints.
- **bad_ext:** at `u`, the value set is exhausted for `y` only if `Σ_{w ∈ W_u} |F_w(y)| ≥ 2N`. Summed over `y` this is `|W_u|·2N`, so at most `|W_u|` hints at `u`, and at most (#unary windows) overall. **Each window lies in exactly one bullet, so bad_clean + bad_ext `≤ N`.**
- **bad_M:** `c(y, v) = #{u : v ∈ ∪_{w ∈ W_u} F_w(y)}`. `Σ_y Σ_v c(y, v) ≤ Σ_u |W_u|·2N ≤ 2N²`, and `M_res(y) ≤ Σ_v c(y, v)`, so at most `8N/3` hints have `M_res ≥ 3N/4`.

So **at least `4N − N − 8N/3 = N/3` hints** are clean, extendable, and have `M_res < 3N/4`. For such a `y`, run the adversary with `a_H` as initial pins. A term is clean iff its free pins are non-forbidden and its H-pins agree with `a_H`; otherwise it is false on every completion, so **NO is sound**. Extension is per input (unary windows do not interact). **Hosting:** Q's output is forbidden at `< 3N/4` inputs and `≥ N − h − qw` are free, so a host exists when `qw < N/4 − h`. Complete the rest; `y` is valid (clean, and extendable at `P = ∅`). ∎

**Audited by the reviewer, every step, plus a fifth point it checked: `a_H` is ARBITRARY**, so no optimisation over hub values is needed, and that removes the kill-value requirement entirely.

**What it says.** (a) **In this class the coupling template of D29 cannot exist**: the count over hints always finds a clean, extendable hint with a small dangerous set. **Move 1, the count over hints, here does the work W14 assigned to choices (1) and (4) jointly. It is the selection principle W14 said did not exist, for this class.** (b) At `h = poly(n)`: `qw = Ω(N)` for every hub-plus-unary template. (c) `h = 0` is W12.1's single-block class (W12.1: `N/3`; W29.2: `N/4`, consistent and weaker). The control, hub, two-hub and parity-hub all have `h ≤ 2`. **It is the line's second theorem for a general class, after W28.1.**

## §9. Residue -- W30

**Residual windows of arity `≥ 2` after pinning the hubs.** There `bad_clean` and `bad_M` should count as here, and hosting should follow W28's almost-full count with `D′`. **The crux is extension:** for arity `≥ 2`, a free input's forbidden set depends on the other positions' current values. A count over hints controls the **average** over settings, while the adversary faces the settings Q's pins create, **the worst case**.

## §10. Practice lines

- **A PROOF STEP CAN FAIL WHILE THE CONCLUSION HOLDS; KEEP THE TWO APART** (the hub with its non-kill value).
- **CHECK YOUR OWN CORRECTION WITH THE SAME AUDIT YOU GAVE THE ORIGINAL** (§3A withdrew half of §1).
