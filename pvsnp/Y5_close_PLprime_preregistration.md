# Y5: close (PL′). Pre-registration

*Drafted 2026-09-11 on branch `y5-close`, on the author's go ("Draft Y5 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply:*
- *smallest case first;*
- *every bound beside the record and the literature;*
- *every flag's implication carried into the priors;*
- *every expected failing step checked against the source's actual protocol;*
- *every new pre-registration checked against the previous report's refuted premises;*
- *when a printed inequality and the cited protocol disagree, the protocol wins, and the disagreement is logged.*

## Ceiling (first)

- **Y5a** would be a new barrier: bounded-round adaptive honest reductions with O(β/log n) bits of adaptivity, at gap ω(log n), put L in AM ∩ coAM. That is a result about the route, not about P vs NP or OWF.
- Y5b and Y5c narrow (PL′) to one named step.

## §0. Refuted premises checked (the new practice)

**Refuted in Y3 and Y4, and not reused here:**
- "hidden ρ / secret sample": SS22 is public-coin (Corollary 26);
- "rows outside the sample don't exist": Goldwasser–Sipser (GS) has Merlin exhibit rows of his choosing;
- "inflation by (1+ζ)": the true bound is A/δ (Lemma B);
- SS22's printed Lemma 22 direction: the GS reading holds (overclaims blocked per entry).

**Availability, checked at drafting.** Goldreich–Vadhan (SS22's [24], the source of Lemma 21):
- the Weizmann copy (wisdom.weizmann.ac.il/~oded/COL/entropy.pdf) reset the connection twice in Y4;
- the only other copy found is the Springer chapter (Studies in Complexity and Cryptography, LNCS 6650, 2011), which is paywalled;
- no ECCC copy was found in the drafting search.

Arm (ii)'s literature step therefore tries, in order: the Weizmann copy again, Goldreich's book *Computational Complexity: A Conceptual Perspective* (if an entropy-estimation protocol is stated there), and lecture-note or survey descriptions. Anything other than the paper itself is labelled secondary.

## §1. Arm (ii): monotonicity of the relativized Lemmas 21–22, with my flag

**What (PL′)(ii) requires.** When round-2 membership f₂(x) = y is certified with Merlin-supplied round-1 answers, steering (round-1 underclaims on Merlin-chosen rows) can only make certified quantities move in the direction that the protocol's soundness already tolerates. Concretely:
- **(ii-a) Lemma 22 (GS) direction:** steering can only **inflate** proven lower bounds on counts. That is Lemma B's regime, bounded by A/δ.
- **(ii-b) Lemma 21 (entropy estimation):** steering shifts the certified entropy by at most log(1 + A/δ) + O(1), **in a known direction**, so that Step 4's consistency check stays sound up to that margin.

**Flag N (non-monotone entropy estimation; my expected failing step for arm (ii)).**
- A two-sided entropy estimate within ±1 needs both an upper bound on H (points have large preimages) and a lower bound on H (the distribution is spread).
- In the standard constructions I know of, both sides go through GS lower bounds, on different sets:
  - **H ≤ h** via proving |f^{−1}(f(x))| large for verifier-random x. Steering inflates these, making H look **smaller**.
  - **H ≥ h** via proving an **image**-type set large (many y with f^{−1}(y) ≠ ∅, or many pairs with distinct images). Steering can **also** inflate that, by exhibiting x with steered f₂(x) = y for y outside the canonical image, making H look **larger**.
- **If both sides use GS on steerable membership, steering moves the entropy estimate in both directions, and (ii-b) fails: there is no monotonicity.**
- Merlin can then shift h to match any σ(B) within ±log(1 + A/δ) in either direction. That re-opens deflation of round-2 counts, which Y4 §6.4 assumed was average-limited.
- **This is to be checked against Goldreich–Vadhan's actual protocol** (the practice line from Y3). If their H ≥ h side uses verifier sampling without exhibited elements, Flag N fails, and (ii) may hold.

## §2. Arm (iii): robustness against coin-adaptive in-window oracles, with my flag

**The reviewer's route 1: H5 plus a union bound over Merlin's commitments.**

**Flag U′ (the union bound fails by counting; to be written as a proof in the run).**
- Merlin's round-2 commitment covers the t·k₂ entries of the sampled rows, each an in-window value among ≤ log(1 + A/δ) + O(1) shifts. So there are C ≥ t·k₂·log log(A/δ) bits of choice: **C grows linearly in t**.
- For a fixed in-window oracle O, H5 gives Pr_ρ[M^O correct] ≥ 1/2 + ε. So the fraction of the t sampled rows on which M^O errs exceeds 1/2 − ε/2 with probability ≤ exp(−Ω(ε²t)).
- A union bound over 2^C oracles needs ε²t ≫ C ≥ t·k₂. **That fails for every t** once k₂ ≥ 1/ε². The failure is structural, not quantitative: the richness of the class grows with the sample.
- **Expected: route 1 fails at "the commitment size is linear in the sample size".**

**The reviewer's route 2: an SS22-Theorem-18-style conversion.**
- **How SS22 avoids coin-adaptivity (Y3/Y4, verified structure):** the perturbation λ̂/D is drawn in Step 6, **after** Merlin commits. By Proposition 16, every claim within (1 ± τ) collapses to the canonical J[λ̂], which does not depend on the sample. So SS22's effective oracle is **fixed**, and H5 applies.
- **Flag P (the perturbation cannot absorb steering):** steering-induced deviations are **bit-shifts**, outside Proposition 16's (1 ± τ) window (Y4 §2). They survive the perturbation, so the effective round-2 oracle stays sample-dependent. A Theorem-18-style K′, agreeing with the effective oracle on the sampled queries, would be defined **after** the sample, whereas H5 speaks of oracles fixed **before** M's coins.
- **Expected: route 2 fails at "the post-commitment perturbation collapses only sub-bit deviations; steering deviations are bit-sized".**

**What (iii) would need instead.** Either:
- **(iii-a) strong robustness:** M is correct with probability ≥ 1/2 + ε against in-window oracles chosen **after** seeing M's coins (an adaptive adversary). That is a hypothesis on the reduction, stronger than H5, and to be compared with the robustness notions in SS22, AHT23 and GK24; or
- **(iii-b)** a coarser perturbation: a random shift of the answer grid at scale log(1 + A/δ) rather than 1 bit. It would collapse steering shifts to a canonical value, at the cost of adding log(1 + A/δ) to the tolerance needed.
  - **This looks feasible and is my candidate repair.** It trades the error window for canonicity, exactly as SS22's γ does at scale 1.
  - To be checked: does Proposition 16's argument scale (the bad-γ measure O(τ) becomes O(τ·log(A/δ))?), and does the extra window fit inside (PL′)(i)'s margin?

## §3. Arm (i): the parameter condition (stated only)

β ≥ β_SS22 + log(1 + 16k₂A/ε), with A = (r + log k)^{k₁}. If (iii-b) is used, add log(1 + A/δ) for the coarse grid. **Both terms are O(k₁·log n) for k₁ round-1 queries**, so the scope stays "few bits of adaptivity".

## §4. Kill test (the reviewer's)

The closure must be silent on IW98's n stages:
- reach compounds over rounds (A_R ≥ (r + log k)^{Σ k_j});
- the coarse grid of (iii-b) widens with the reach;
- so the margin needed exceeds any ω(log n) tolerance after ω(1) rounds of Θ(1) queries each.

To be checked: (iii-b)'s grid does not somehow reset per round.

## §5. Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y5a** | (PL′) closes, e.g. via (iii-b) together with a monotone (ii). The theorem: bounded-round barrier for reductions with O(β/log n) bits of adaptivity. Re-derive twice; kill test. |
| **Y5b** | (ii) or (iii) fails at a named step (expected Flag N for (ii); Flag U′ and Flag P for routes 1–2 of (iii)). (PL′) reduces to that step. |
| **Y5c** | Goldreich–Vadhan unreachable again: (ii) stays open, and the page says so. |

**Priors.**
- Reviewer: Y5b 45 / Y5a 35 / Y5c 20.
- Mine: **Y5b 50 / Y5c 30 / Y5a 20.** Carrying the flags in:
  - Flag N makes (ii) likely to fail if the source is read.
  - The source was unreachable twice, which raises Y5c.
  - (iii-b) is a live repair for (iii), but Y5a needs both (ii) and (iii).

## Ruling (the reviewer's, recorded at acceptance as a draft)

**Accepted as a draft.** No run until the author's separate go.

**Priors** moved to mine: Y5b 50 / Y5c 30 / Y5a 20. Flags N, U′ and P are adopted as expectations to verify.

**Ruling (1): (iii-b) gets the attempt's effort.** It must show three things:
- **(α)** Proposition 16's collapse scales to the coarse grid. State the scaled proposition and prove it (g5).
- **(β)** The grid is drawn once per round, **after** Merlin's commitment for that round, and does not reset the reach. The cost compounds with rounds, and the argument dies at ω(1) rounds (the kill test).
- **(γ)** With the grid, Flag N's steerable side of the two-sided estimate is collapsed too; otherwise (ii) still fails independently.

If all three hold, (PL′) reduces to (i) alone, a parameter condition, and Y5a is a bounded-round barrier for reductions with O(β/log n) bits of adaptivity. Re-derive twice.

**Ruling (2), Flag N.** Check Goldreich–Vadhan's protocol for **which** side uses verifier-random x.
- If the H ≥ h side is verifier-sampled (Arthur picks x, Merlin bounds the preimage), steering cannot exhibit off-image points there, and Flag N fails on that side. Then only the H ≤ h side is steerable, and (iii-b)'s collapse may cover it.
- If both sides are prover-exhibited, record the exact deflation route, and say whether the grid also collapses deflation (it should be symmetric; say so, or show why not).

**Sources for Goldreich–Vadhan, in order:** Weizmann again; then Goldreich's textbook chapter on entropy approximation / NISZK; then notes, labelled secondary. If all fail, (ii) stays open as Y5c, and the report says which sources were tried.
