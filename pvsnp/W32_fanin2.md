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
