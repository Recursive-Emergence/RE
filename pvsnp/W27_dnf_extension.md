# W27: extending Theorem W26.1 toward Definition 9. Pre-registration

*Drafted 2026-09-12 on branch `w27-dnf-extension` (from `w26-query-fanin` at 99029ab), on the reviewer's W27 specification. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before re-reading W12.2, W8.1's proof, or Theorem 12's adversary for this round, and before any computation.**

## §0. Target and ceiling

W26.1 (membership model): `(q+1)·k ≥ 0.58√N`. It rests on W25.2's all-yes collapse: a transcript that is a function of `y` alone, and **one distribution over `C` shared by all hints** (step 2's `Σ_y Pr[y ∈ range(C′)] ≤ N`). **Definition 9** queries are width-`w` DNFs over `{α_x}`. Already at `w = 1`, a query `OR_x [α_x = v_x]` may name different values at different inputs, and then a "no" is not a win.

**Questions (the reviewer's):** (Q1) does the first moment survive with the query tree in place of `V(y)`? (Q2) where does `w` enter? (Q3) target form `q·w·k ≥ Ω̃(√N)`, which would make W26.1 the single-value `w = 1` case.

**Ceiling.** Even 27a is a statement about deterministic black-box depth-1 back-mappings. It would be the first bound in Korten's Definition 9 model for general joint glue, but it is **not** Korten's Problem 1 (depth `d` vs `log_α β`), and by Flag H7 nothing randomised. Nothing about P vs NP.

## §1. Governing lines

W26's two lines bind first: **the obstruction may be the model's, not the problem's** (so W14's selection problem may **return** exactly as far as this model reintroduces histories), and **price a mechanism against the probability of each case, not its worst case**. Standing: price every resource a statement quantifies over; framing audit precedes pricing; averages vs maxima; eleven wrong impossibility claims on my record, and W26.1 was an impossibility claim that held **only after a full audit**.

## §2. Counting done before the prior

**(a) THE REVIEWER'S KILL TEST DOES NOT BITE, I think, and the one that does is different.** "Does `range(C)` hit `T`", with `|T| ≈ N`, is answered yes with probability `→ 1` under the injective distribution: **it carries almost no information, so it cannot break a first-moment count.** The dangerous queries are the **balanced** ones. The natural width-1 example is a **matching query** `OR_{x ∈ A} [α_x = v_x]`, with `|A| = N` and the `v_x` distinct, answered yes with probability about `1 − e^{−1/2}`. **Proposed replacement kill test: a Q made of `q` random matching queries**, checked against whatever Q1's bound predicts.

**(b) WHY THE MEMBERSHIP PROOF DOES NOT LIFT DIRECTLY: pins come back.** Wilson's adversary answers true by fixing `≤ w` inputs per query, so after `q` queries it holds a positional partial assignment `P` of size `≤ qw`. **`P` depends on the queries, which depend on `y`.** Two ways to run W26.1's first moment, both of which I expect to fail:
- **Condition `C` on `P(y)`.** Step 2 then uses a different distribution for each hint, and `Σ_y Pr_{D_y}[y ∈ range(C′)]` is no longer `≤ N`: each `D_y` can put its own `y` in range. **The per-window budget is gone.** This is W14's selection problem, re-entering exactly where positions are pinned.
- **Keep `C` unconditioned, and charge `Pr[C extends P(y)]`.** A window that reads a pinned input gains a factor `≈ 2N` per pinned value it sees, against a probability `≈ k/N` of seeing it. `Σ_j C(qw, j)(k/N)^j (2N)^j = (1 + 2k)^{qw}`, which **explodes**. Priced against probability, the gain does NOT pay for itself -- the opposite of W26 step 4, because a positional pin is worth `log 2N` bits where a membership fact was worth 1.

**(c) What could rescue width 1 (Q1 at `w = 1`).** For `OR_x [α_x = v_x]`, the adversary chooses **which** `x` realises the yes. If it can choose `x` outside every window that matters, and the pins stay invisible to most windows, the explosion in (b) is avoided. But every input lies in `k` windows **on average** (and up to `N` at a hub), so "outside every window" is a selection over `y`-dependent choices, which is the selection problem again. **I do not see the rescue; I see where it would have to live.**

**(d) An information count that does survive, and is weak.** A `q`-query tree has `≤ 2^q` leaves. Without any hint, correctness forces the `2^q` leaf outputs not all to lie in one range, so `2^q > N`, i.e. `q > n`: **only `Ω(log N)`**, far below Wilson's `qw ≥ N`. **Counting leaves is not the mechanism.** The strength of Wilson's bound comes from the adversary's position choices, which is exactly the part (b) says the first moment cannot absorb.

## §3. Priors, fixed now

| code | reviewer | **mine** |
|---|---|---|
| **27a** a width-`w` version proved | 20 | **10** |
| **27b** survives width 1 with `x`-dependent values, not general `w`, gap named | 55 | **38** |
| **27c** nothing | 25 | **52** |

**Why 27c at 52.** §2(b): both natural lifts fail at the same point, **positional pins with `y`-dependent choices**. W26's own practice line predicts it: if the selection obstruction belonged to the DNF model, moving back toward that model should bring it back. §2(c): I see where a width-1 rescue would have to live, but no mechanism. **Why not higher:** W26.1 surprised both of us from the same position one round ago, and my record on impossibility-flavoured forecasts is poor in **both** directions. **Why 27a at 10:** a general-`w` proof would have to beat (b)'s `(1+2k)^{qw}` explosion, and I see nothing that does.

## §4. Flags

- **A27 -- framing first:** state precisely which Definition 9 queries keep a `y`-only transcript (single-value ORs), and which reintroduce `C`-dependence.
- **B27 -- one distribution or none:** any proposed count must say whether step 2 uses a single distribution for all hints. If it does not, the per-window budget must be re-proved, not assumed.
- **C27 -- the matching-query kill test** (§2(a)) replaces or accompanies the reviewer's large-set test; both run.
- **D27 -- averages vs maxima** for window incidences (`k` on average, up to `N`).
- **E27 -- stop-rule:** any argument that appears to beat §2(b)'s explosion is sent to the reviewer, with the step that does it, before writing.
- **F27 -- W12.2 re-read happens after this commit**, to ask what its adversary does with positional pins that a count cannot.

## §5. Kill tests

- (i) Large-set query: predicted uninformative under the injective distribution.
- (ii) Matching queries: `q` random matchings at small `N`, exact where feasible; compare with any Q1 bound.
- (iii) Every count states its distribution(s) (Flag B27).
- (iv) If the resolution is not the pre-registered one, say so in the same sentence.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §5A. Amendment -- Flag F27, the W12 re-read (after the priors commit 095e58d, before any computation)

**Read from `w12-one-input-glue`, §1 and §3.** W12.1 and W12.2 use two separate moves. **Move 1, a count that chooses ONE hint:** `Σ_y Σ_v #{x : G_x(v) = y} = N·2^{n+1}`, averaged over the valid hints, gives a `y` with `M(y) ≤ 2N/3`. **Move 2, Wilson's adversary for that `y`:** for one-input glue, "`y ∉ range(C′)`" is the **product** `F_y = ∏_u A_u`, so the adversary runs *"with no bookkeeping"*, and positional pins are harmless.

**§2(b)(i) is WITHDRAWN as stated.** A lower bound needs one bad hint. The count can fix `y` first and the adversary pins positions for that `y` only, so no cross-hint consistency is ever required. **My "shared distribution destroyed" obstacle came from insisting that count and adversary be one argument.** It is the same shape of error as my W25 lazy-hosting reading, one level up. §2(b)(ii) stands only for that single-argument route.

**The obstacle, restated:** for joint glue of fan-in `k ≥ 2`, **`F_y` is not a product.** Whether a "true" term is still completable becomes a global CSP question over overlapping windows. That is W13/W14's wall, returning as W26's practice line predicts.

**W27's question, restated for the reviewer's ruling:** can a W26.1-style count choose a hint `y` for which `F_y` contains a large **product subfamily** `∏_u B_u`, one closed under Wilson's true-answers? That is W10/W12's forced-value-plus-free-set architecture, with the hint chosen by precision counting.

**Priors are not revised.** Half of 27c's stated reasoning leaned on the withdrawn (b)(i); what remains is the non-product wall, where the line has failed four times.

## §5B. Amendment -- the reviewer's influence reformulation, audited before any run

*The reviewer's ruling crossed §5A. The two agree on what not to do (condition `C` per hint). The reviewer then proposes a single-argument lift under ONE unconditioned distribution, with a truthful transcript `τ(C, y)`, and charges positional information through a window's **influence**, the total variation between the law of `τ` given the window's view and its unconditioned law: (Q1′) influence `≤ c·qwk/N`; (Q2′) `Pr[F_y] ≥ 2^{−O(q)}`, with `F_y` = "Q's output lies in `R`"; (Q3′) a `j = 2` analogue.*

**Accepted: §2(b)(ii) charged the wrong quantity.** Under one unconditioned distribution nobody places pins, so `Pr[C extends P]` is not a term of the lift. **The kill-test ruling is also accepted:** the matching query is the balanced test, and the large-set query is the unbalanced control.

**(Q1′) IS FALSE AS STATED, by a one-line example.** Definition 9 permits the width-1 query *"is `C(u) ∈ T`?"* = `OR_{a ∈ T} [α_u = a]`, with `|T| = N`. It is **balanced** and reads **one position** (if the variables are bits, a single bit of `C(u)` is simpler still). **Q knows the template**, so on hint `y` it can query the inputs of the windows able to output `y`. For a window whose view contains `u`, that query's answer is **determined** by the view: influence `1/2`, not `k/2N`. `k(n+1)` such queries learn the whole view. **So influence is not `O(qwk/N)` for every Q and window.** The balanced matching query passes only because it is **untargeted**, so **the matching-query kill test cannot test (Q1′)**. The kill test that does is a **targeted Q**, which reads the positions of the windows that output its hint.

**What might survive: a ONE-SIDED bound.** Influence that **lowers** `Pr[F_y | view]` is harmless: learning view values tells Q strings that ARE in `R`, which it can avoid. Only influence that **raises** failure given the view hurts. Correctness ties raised failure to `y ∈ range(C′)`, so the harmful direction is exactly the template-exploitation question of W7-W14. **Unresolved; registered as the step to attack.**

**A SECOND GAP: uniformity across hints.** The lift's final step, `4N·Pr[F] ≤ N·E[max_y Pr[F_y | view]]`, needs every `Pr[F_y]` comparable. W26.1 got this by **padding `V(y)` to size exactly `s`**, making `Pr[V(y) ⊆ R] = p_s` for all `y`. A truthful-transcript Q can have `Pr[F_y]` far above `2^{−(q+1)}` on a few hints, and a window can pick exactly those hints. **The lift needs a padding analogue:** a sub-event `E_y ⊆ F_y` with equalised probability whose view-conditional gain stays bounded, for example `F_y ∩ {Z_y ⊆ R}` for fixed extra strings `Z_y`. **Its independence from `F_y` is not free, and it is not yet shown.**

**Priors are not revised.** The reviewer's case for 27a/27b rests on (Q1′). As stated, (Q1′) fails for targeted balanced width-1 queries; the one-sided version is open.
