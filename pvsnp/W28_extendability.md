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

---

# W28 Findings

*Appended after the reviewer audited the corrected count and accepted Lemma W28.1. Nothing above is revised.*

## §4. Ceiling

**Definition 9 model (width-`w` DNF queries), deterministic, depth 1, `n′ = n`.** A structural theorem about black-box depth-1 templates. **Not Korten's Problem 1** (depth `d`), nothing randomised, nothing about P vs NP. **(H_t) is a worst-case-over-settings hypothesis**, including settings the adversary's own pins create. Relaxing it to an average case is the first thing a structured template would exploit, and that is where W14's coupling lives.

## §5. Outcome against priors

| code | mine / reviewer (reviewer later) | outcome |
|---|---|---|
| **28a** locality lemma and theorem | 50 / 40 (45) | **achieved -- Theorem W28.1, with the threshold corrected to `N/(D+1)`** |
| 28b stronger hypothesis needed | 35 / 40 | -- |
| 28c nothing | 15 / 20 | -- |

The reviewer's proposed conclusion (`qw < N/2`) was wrong. The correction is in §1(iii), made **before** priors and accepted by the reviewer (its eighth miss, recorded in its words).

## §6. Theorem W28.1 -- the hub-or-coarse dichotomy (headline)

> **Theorem W28.1.** *In Korten's Definition 9 model, let a depth-1 template from stretch `n ↦ n+1` to `n ↦ n+2` have maximum input degree `D` (windows per input). For a hint `y`, let `t_y` be the largest forbidden set: over every window, every position, and every setting of the window's other positions, the number of values at that position giving `g = y`. If `D·t_y < 2N`, then `y` is valid and every deterministic back-mapping correct on `y` has* **`qw ≥ N/(D + 1)`**. *Hence a total depth-1 back-mapping with `qw < N/(D+1)` must have* **`t_y ≥ 2N/D` at EVERY hint `y`**: *its glue is coarse everywhere, or else `D ≥ N/(qw) − 1` (a hub).*

*Proof.* **Adversary:** answer YES and pin a term iff it is consistent with the pins `P` and `P` plus the term is **clean** (no fully pinned window has `g = y`); otherwise answer NO.
**(NO is sound.)** A consistent but non-clean extension contains a violated full window, so it is false on every `C` with `y ∉ range(C′)` extending `P`. An inconsistent term is false on every extension. Non-cleanness is monotone, so later pins keep earlier NO answers sound.
**(Clean ⟹ extendable, `D·t_y < 2N`.)** Fill the free inputs in any order. When `u` is filled, only windows whose other positions are all set constrain it, each excluding `≤ t_y` values. So at most `D·t_y < 2N` values are excluded and a value remains. Cleanness is preserved throughout. With `P = ∅`, `y` is valid.
**(Hosting.)** After `q` queries, `|P| ≤ qw`. A window is **almost-full** if all its positions but one are pinned. Each contains a pin, so there are `≤ qwD` of them, and `≤ qwD` free inputs lie in one. If `N − qw > qwD`, some free `u` lies in none. Then `P + (u := v)` is clean for Q's output `v`, whatever it is, hence extendable: `C` has `y ∉ range(C′)`, `v ∈ range(C)`, and every answer is honest. ∎

**Corollary (random-like joint glue).** For random glue of fan-in `k`, `t = O(k log N / log log N)` and `D = O(k + log N)` with high probability, so **`qw = Ω(N/(k + log N))`**. That is F1's shape from W26, **now in Definition 9, at the line's scale**. *(The high-probability bounds are the standard Chernoff-plus-union estimates, checked numerically in §7, not written out in full here.)*

**Consistency table.** Each known template is excluded by the right parameter:

| template | D | t | lemma applies? | known result |
|---|---|---|---|---|
| control `(C(x), x&1)` | 1 | ≤ 1 | yes: `qw ≥ N/2` | W8.1: `N − 1` (stronger, bespoke) |
| hub | N | -- | no (D) | W24: validity-first beats it by pre-pinning |
| one-input-per-coordinate (W12.2) | small | ≈ N | no (t) | W12.2: `N/9`, by products |
| W25.3 hypergraph (fan-in N) | N | -- | no (D) | total at 5 queries |

## §7. Numerics and the executable check

**Flag B28, exact `t` and `D` for random glue** (hint `y = 0`; tables uniform):

| k | N | t | D | `D·t < 2N`? | N/(D+1) |
|---|---|---|---|---|---|
| 2 | 8 | 3 | 5 | yes (15 < 16) | 1.3 |
| 2 | 16 | 4 | 5 | yes | 2.7 |
| 2 | 32 | 4 | 5 | yes | 5.3 |
| 2 | 64 | 4 | 5 | yes | 10.7 |
| 2 | 128 | 6 | 7 | yes | 16.0 |
| 2 | 256 | 6 | 11 | yes | 21.3 |
| 3 | 8 | 4 | 4 | **no** (16) | 1.6 |
| 3 | 16 | 6 | 8 | **no** (48 > 32) | 1.8 |
| 3 | 32 | 7 | 6 | yes | 4.6 |

**The hypothesis holds for fan-in 2 at every size tried and for fan-in 3 from N = 32.** `t` and `D` grow slowly, as predicted. *Not reached: N up to 1024, which the reviewer asked for; exact `t` at fan-in 3 is cubic in `2N` per window.*

**Executable check of the proof.** The adversary was run against an aggressive Q: it places terms next to existing pins, to manufacture almost-full windows, and outputs the string most often forbidden by them. The final `C` was **built** by step (ii)'s greedy fill and verified: `y ∉ range(C′)`, output in range, every YES term satisfied, every NO query false. Random fan-in-2 glue, `qw` below `N/12`:

| N | w | q | qw | result over 30 seeds |
|---|---|---|---|---|
| 64 | 1 | 5 | 5 | adversary wins 30/30 |
| 64 | 2 | 2 | 4 | 30/30 |
| 128 | 2 | 5 | 10 | 30/30 |
| 256 | 3 | 7 | 21 | 30/30 |

**The reviewer's game search at n = 3 was not run.** At N = 8 the bound is `qw < 1.3`, and fan-in 3 fails the hypothesis there, so the search is vacuous by Flag C28's own weighting. The executable check replaces it at sizes where the bound has content. **Recorded as a substitution, not hidden.**

## §8. W14 cross-check (Flag F28)

W14's four choices were: (1) a valid non-certifying hint, (2) a sparse free set, (3) forced values chosen after the hint, (4) hosts for the dangerous strings. **Under locality, (2) and (3) are unnecessary**: any clean pin set extends, there are no forced values, and the free set is everything unpinned. **(1) and (4) survive with explicit counts**: (1) through `t_y` (any `y` with `D·t_y < 2N` is valid and non-certifying), and (4) through the free input carrying no almost-full window (exists while `qw(D+1) < N`). **This matches the reviewer's advance prediction.** W14's dangerous strings are non-local objects: they exist only where (H_t) or (H_D) fails.

## §9. Errors and misses

**Reviewer's:** the min-over-sets radius (seventh miss); the `qw < N/2` threshold (eighth). **Mine:** none new in the proof; one substitution (§7, the vacuous game search replaced by an executable check), and the N up to 1024 numerics not reached.
**Practice line: A DEFINITION QUANTIFIED OVER EVERYTHING IS USUALLY TOO STRONG FOR AN ADVERSARY THAT ONLY NEEDS WHAT IT CHOOSES** (radius over all sets vs clean sets), **AND A CONCLUSION QUANTIFIED OVER THE ADVERSARY'S CHOICES MUST ALSO SURVIVE THE OPPONENT'S** (hosting vs Q's aimed output).

## §10. Next: W29 candidate, degree reduction by pre-pinning (the reviewer's, registered here, not run)

If a template has `h` high-degree inputs, pin them **first**, to values chosen against `y`, and apply W28.1 to the residual template. This would extend §6 to **"either MANY high-degree inputs, or coarse glue"** and fold W24's validity-first in as the `h = 1` case. **The step that can fail:** pinning a hub may enlarge the forbidden sets of the windows through it, so (H_t) breaks, which is W14's coupling again. Positive control: hub (`h = 1`, residual `D = 1`). First test: two-hub.
