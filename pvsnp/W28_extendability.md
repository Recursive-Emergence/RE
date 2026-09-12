# W28: local extendability. Pre-registration

*Drafted 2026-09-12 on branch `w28-extendability` (from `w27-dnf-extension` at 064811f), on the reviewer's W28 specification as restated after my audit of its radius definition. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed before re-reading Wilson's Theorem 12 or any W7-W14 proof for this round, and before the game search.**

## §0. Target and ceiling

**Korten's Definition 9 model (width-`w` DNF queries), deterministic, depth 1, `n′ = n`, glue fan-in `k`.** Fix a hint `y`. A partial assignment `P` is **CLEAN** if no window fully pinned by `P` has `g = y`. **Adversary (the reviewer's):** answer YES and pin a term iff `P` plus the term is clean; otherwise answer NO. At the end, host Q's output at a free input where the result is clean. **The adversary wins if CLEAN ⟹ EXTENDABLE (to some `C` with `y ∉ range(C′)`) and a hosting input exists.**

**Ceiling.** A structural statement about deterministic black-box depth-1 templates in Definition 9. It is not Korten's Problem 1 (depth `d`); nothing randomised; nothing about P vs NP.

## §1. The lemma as the reviewer stated it, and my audit before any run

**Hypotheses.** (H_t) **forbidden sets are small**: for every window and every setting of `k − 1` of its positions, at most `t` values of the last position give `g = y`. (H_D) **every input lies in at most `D` windows.**

**(i) Random glue satisfies (H_t), (H_D).** Forbidden-set size is `Bin(2N, 1/4N)`, mean `1/2`; a union over `N·(2N)^{k−1}` (window, setting) pairs gives `t = O(k log N / log log N)`; random reads give `D = O(k + log N)`. *Accepted as stated, to be checked numerically.*

**(ii) Clean ⟹ extendable when `D·t < 2N`.** *Re-derived, and it holds.* Fill free inputs one at a time. When `u` is filled, only windows whose **other** positions are all already set constrain it, each forbidding `≤ t` values by (H_t). Windows with another unset position constrain nothing yet, and will constrain their own last position later. So at most `D·t < 2N` values are excluded at every step, and non-cleanness is never created. **Soundness of NO:** a term whose addition is not clean contains a violated full window, so it is false on every completion extending `P`. Non-cleanness is monotone, so NO answers stay sound as `P` grows.

**(iii) THE REVIEWER'S CONCLUSION `qw < N/2` IS WRONG; the correct threshold is `qw < N/(D + 1)`.** Q picks its output `v` after seeing the pins. A free input `u` rejects `v` only if some window through `u` has all its other positions pinned (**almost-full**) and its forbidden set at `u` contains `v`. Q can aim `v` at those sets, so the reviewer's "all but `Dt` strings are hostable at each `u`" does not bound what Q chooses. **Correct count:** every almost-full window touches a pin, so there are at most `|P|·D ≤ qwD` of them, and at most `qwD` free inputs carry one. **If `N − qw > qwD`, some free `u` carries no almost-full window.** Then `P + (u := v)` is clean for **every** `v`, hence extendable by (ii), and Q fails.

> **Lemma W28.1 (candidate, corrected).** *In Definition 9, fix a depth-1 template and a hint `y`. If every forbidden set has size `≤ t`, every input lies in `≤ D` windows, and `D·t < 2N`, then every deterministic back-mapping correct on `y` has* **`qw ≥ N/(D + 1)`**.

**Consequences, if it holds.** (a) Random-like joint glue with `D = O(k + log N)` needs `qw = Ω(N/(k + log N))`, **F1's shape** from W26, now in Definition 9. (b) **Any template with small `q·w` must, AT EVERY HINT, have either a high-degree input (`D ≥ N/(qw) − 1`) or large forbidden sets (`t ≥ 2N/D`).** That is exactly the hubs (W24) and the projection-like coarse glue (W10, W12) the line has studied, and it names what a reduction needs. (c) Consistency: hub has `D = N` (excluded); the control template has `D = 1`, `t ≤ 1`, giving `qw ≥ N/2` against W8.1's `N − 1` (weaker, as it should be); one-input-per-coordinate glue (W12.2) has forbidden sets of size about `N` when an input controls one coordinate (excluded; W12.2 covers it differently); W25.3's hypergraph template has `D = N` (excluded).

**The step I trust least:** (H_t) must hold for **every** setting of the other `k − 1` positions, including settings the adversary's own pins create. It is a worst case over settings, which is what the union bound delivers for random glue. For structured glue it is the hypothesis a template breaks.

## §2. Priors

| code | reviewer | **mine** |
|---|---|---|
| **28a** locality lemma and theorem for random-like glue in Definition 9 | 40 | **50** |
| **28b** lemma needs a stronger hypothesis; gap named | 40 | **35** |
| **28c** nothing | 20 | **15** |

**Why 28a above the reviewer:** I re-derived (ii) and (iii) myself, and (iii)'s correction **weakens** the conclusion to a form I can check line by line. **Why not higher:** it is an impossibility claim on my record of eleven wrong ones plus W26.1's one right one, and (H_t)'s worst-case-over-settings clause is where a hidden dependency would sit.

## §3. Flags and kill tests

- **A28 -- the corrected threshold on every line:** `N/(D + 1)`, never `N/2`.
- **B28 -- measure `t` and `D` on every instance** before using any search result, and state whether `D·t < 2N` holds.
- **C28 -- game search (the reviewer's kill test, also my construction proposal):** at n = 3, random fan-in 2 and 3 glue. **Weight is limited:** at N = 8 the lemma allows only `qw < 8/(D + 1)`, i.e. about 1-2, so a failure to find a total Q is nearly vacuous there. A total Q **with `qw` below the bound on an instance meeting `D·t < 2N`** refutes the lemma.
- **D28 -- positive control:** W25.3's hypergraph template (`D = N`), where a total Q exists.
- **E28 -- stop-rule:** any refutation, or any proof of (H_t) for random glue, goes to the reviewer before writing.
- **F28 -- the W14 cross-check:** name which of W14's four choices the locality hypothesis makes unnecessary, and confirm W14's dangerous strings are non-local by (H_t) or (H_D) failing.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
