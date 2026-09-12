# W26: the query-versus-fan-in tradeoff. Pre-registration

*Drafted 2026-09-12 on branch `w26-query-fanin` (from `w25-read-count` at ff2f888), on the reviewer's W26 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE any run and before re-reading any primary for this round -- including Korten's Definition 9 and the W8.1 / W12.2 statements, which this page quotes only from W14's committed summary line.**

## §0. Target and ceiling

**Membership-query model, deterministic, depth 1, stretch `n ↦ n+1` to `n ↦ n+2`, `n′ = n`.** Glue fan-in `k`. By W25.2, totality is static set certification: `y ↦ V(y)`, `|V(y)| ≤ q + 1`, and every `C` with `V(y) ⊆ range(C)` has `y ∈ range(C′)`.

**Known endpoints.** `k = N`: `q ≤ 5` for all `N ≥ 16` (W25.3). `k = 1`: `q = Ω(N)` -- **if** the DNF-model theorems transfer (§2(a)).

**Candidate forms (the reviewer's):** (F1) `q·k = Ω(N)`; (F2) `q²·k = Ω(N)`; (F3) `q = Ω(log N / log(N/k))`.

**Ceiling.** Nothing about P vs NP; nothing randomised (Flag H7); the black-box question itself lives at `k = poly(n) = polylog N`, so **only the small-`k` end of any tradeoff bears on the line** -- a tradeoff that is loose at large `k` but tight at `k = polylog N` answers what the line needs.

## §1. Governing lines

W25's practice line binds first: **price every resource a statement quantifies over before counting under it** -- here `k`, `q`, and the size of each window's view. Also standing: framing audit precedes mechanism pricing; a verified premise does not license its consequence; calibration asymmetry indexed to source; eleven wrong impossibility claims on my record, and W25.3 was a *positive* construction that held.

## §2. Disclosure and counting done before the prior

**(a) THE ENDPOINT TRANSFER, unverified.** W8.1 (single-call, `qw ≥ N − 1`) and W12.2 (one-input patterns, arbitrary per-coordinate glue, `qw ≥ N/9`) are proved in Korten's Definition 9 / Wilson Theorem 12 DNF model. **A membership query "`v ∈ range(C)`?" is the DNF `OR_x [C(x) = v]`, whose terms have width 1** -- so if Definition 9's `w` is term width, membership is a special case, `w = 1`, and the DNF lower bounds transfer DOWN: `q = Ω(N)` at `k = 1` in the membership model. **I have not re-read Definition 9 for what `w` measures.** The reviewer's "W8.1's model might be stronger than membership" is the other horn; this audit decides it, and it runs first.

**(b) IF (a) HOLDS, F2 AND F3 ARE ALREADY DEAD AS TIGHT FORMS.** At `k = 1`, F2 gives `q = Ω(√N)` and F3 gives `Ω(1)`, both below the known `Ω(N)`. They survive only as (true but loose) lower bounds. **Only F1 matches both endpoints -- but it is not the only form that does**: `q·k² = Θ(N)` and threshold shapes (`q = Θ̃(N)` for all `k ≤ N^{1−ε}`, collapsing near `k = N`) also match. So "F1 is the truth" competes with more than F2 and F3.

**(c) A PLACEMENT ARGUMENT I SEE, stated as a sketch and not priced as proof.** The windows form a hypergraph on inputs (`N` windows of size `k`). An input co-occurs with at most `Σ_{windows containing u} k` others -- `k²` **on average**, not per input (W25's lesson: hubs). If the adversary can place the `q + 1` elements of `V(y)` on inputs pairwise sharing no window -- greedily possible for `q + 1 ≲ N/k²` on a regular window system -- then **every window sees at most one element of `V(y)`**, and the reviewer's precision argument has to handle views of size one. This suggests `q·k² = Ω(N)` for **regular** window systems and says nothing for hub-heavy ones, where the independent placement fails. **So I expect the fan-in's *distribution* (max co-occurrence), not just `k`, to enter the true statement.**

**(d) The reviewer's precision derivation, checked in advance for W25-type premise errors.** "A window must see at least two elements of `V(y)` before it may output `y`" is derived "on average" over hints from the output budget `N`; an average bound on `j` gives coverage only for most hints, and the pair-sharing probability `C(q+1, 2)·k/N` assumes **random** placement, whereas the adversary places adversarially (which helps the lower bound) and the template chooses windows (which can concentrate co-occurrence, which hurts it). Registered as two places to check, not as errors.

**(e) Construction side, what I see.** Block-local windows see `C(B_j)`, a `k`-subset of `2N` strings; certifying `V(y) ⊆ range(C)` is global. A hypergraph trick per block (W25.3 locally) certifies `V(y) ⊄ C(B_j)`, not `V(y) ⊄ range(C)`. **I have no construction below `q = Θ(N)` for any `k = o(N)`**, which is weak evidence for a threshold shape and against F1 being tight at intermediate `k`.

## §3. Priors, fixed now

Forms, read as "the tight tradeoff is `Θ̃` of this, over all `k`":

| form | reviewer | **mine** |
|---|---|---|
| F1 `q·k = Θ̃(N)` | 45 | **35** |
| F2 `q²·k` | 30 | **5** -- dead at `k = 1` if §2(a) holds |
| F3 | 15 | **2** -- same |
| other (`q·k²`, threshold, distribution-dependent) | 10 | **58** |

Outcomes:

| code | reviewer | **mine** |
|---|---|---|
| **26a** a proved tradeoff in one form | 15 | **12** |
| **26b** located between two forms, gap named | 60 | **58** |
| **26c** nothing | 25 | **30** |

**Why "other" at 58.** §2(b) removes F2/F3 as tight forms before any run if the transfer holds (I put the transfer at ~85); §2(c) and §2(e) both point at shapes not on the reviewer's list. **Why 26c above the reviewer:** §2(e) -- I see no construction below `Θ(N)`, and without one the tradeoff cannot be *located*, only bounded from one side.

## §4. Flags

- **A26 -- transfer audit FIRST** (§2(a)): read Korten Definition 9 / Theorem 12 for what `w` measures, and W8.1 / W12.2 from their committed pages.
- **B26 -- membership model on every line**; W25.2's all-yes collapse used explicitly wherever totality is checked.
- **C26 -- averages vs maxima**: every co-occurrence or reader count is stated as average or maximum, never unlabelled (W25's two premise errors).
- **D26 -- construction side before lower-bound pricing**: search block templates at n = 3 with a **graded** score, positive control first (K_{4,4}-style at `k = N` must score 0).
- **E26 -- stop-rule**: any construction with `q·k = o(N)` at intermediate `k` -> stop and send before writing.
- **F26 -- re-derive, never recall.**

## §5. Kill tests

- (i) A26 discharged in writing before pricing F2/F3.
- (ii) Positive control scores 0 at `k = N` before any bounded-`k` search is read.
- (iii) Search scores graded, never 0/1 (W25 §10's flat-score miss).
- (iv) The placement sketch (§2(c)) checked on a hub-heavy window system, where it should fail.
- (v) If the resolution is not the pre-registered one, say so in the same sentence.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
