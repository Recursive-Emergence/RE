# Y4: the lowness lemma at two rounds. Pre-registration

*Drafted 2026-09-11 on branch `y4-lowness`, on the author's go ("Draft Y4 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply:*
- *smallest case first;*
- *every bound beside the record and the literature;*
- *every flag's implication carried into the priors;*
- ***(new, from Y3's miss) every expected failing step checked against the source's actual protocol before it is pre-registered.***

## Ceiling (first)

- **Y4a** would be a barrier: bounded-round adaptive honest reductions at gap ω(log n) put the language in AM ∩ coAM. That is a result about the route, and the door would narrow to unbounded adaptivity, which ABKMR shows is powerful and Proposition H′ shows must be deep.
- **Y4b** records the exact lemma missing.

Neither says anything about P vs NP.

## §0. The target (the reviewer's), stated against SS22's verified structure

**Setting (SS22, verified in Y3).** M is a randomized reduction with query map f(ρ, i) = q_i(ρ). The context-sensitive oracle is J[γ](q) = ϕ((1 + γ)·s(q)), where s(q) = |f^{−1}(q)|. The protocol:
- Step 1: Lemma 21, entropy estimation of π_f, given a circuit C_f.
- Step 2: public ρ₁, …, ρ_t and the matrix χ = f(ρ_i, j).
- Step 3: Merlin's counts B.
- Step 4: the entropy consistency σ(B) ≈ h, within ±3.
- Step 5: Lemma 22, a lower bound: no count is overclaimed beyond (1 + ζ).
- Steps 6–7: the output, with a random perturbation λ̂/D.
- Corollary 26 gives coAM by flipping the failure output.

**The target lemma.** Let M ask k₁ round-1 queries (a function of ρ), then k₂ round-2 queries (a function of ρ and the round-1 answers). Give an AM ∩ coAM protocol for the language M decides with the canonical oracle J[γ₁] ∘ J[γ₂] (per-round perturbations). Round 1's counts are certified as in SS22, and round 2's query map uses the certified round-1 answers.

## §1. A premise correction to the reviewer's expected failing step (before any work)

The reviewer's (c) expects: "Merlin's certified count for q₁(ρ) reveals information about ρ that the coAM side's soundness needs hidden". **That repeats my Flag S premise, which Y3 found false.** In SS22, ρ₁, …, ρ_t are public coins (Step 2), and the coAM protocol is the same public-coin protocol with the failure output flipped (Corollary 26). Nothing about ρ is hidden, so leakage cannot be the failure. The ruling is asked to replace (c) with the flag below.

## §2. My flags (raised before any work; checked against SS22's Steps 1–7 and Lemmas 21–22)

**Flag I (inflation by steering: my expected first failing step).**
- Lemma 22 (soundness) rejects if some claimed count s_i ≤ |f^{−1}(q_i)|/(1 + ζ). It protects against **over**claiming only.
- **Under**claiming is controlled only **on average**, by Step 4's entropy check (±3 bits on σ(B), an average over t rows).
- In round 2, Merlin chooses round-1 answers within the oracle's tolerance, each one an underclaim that shifts a J-value by a few bits. That **steers** a row's round-2 queries toward a query q of his choice.
- To inflate the round-2 count of q by the factor (1 + ζ) that Lemma 22 tolerates, he needs to steer only a ζ·π₂(q) fraction of rows. **For light q, that fraction is far below what Step 4's average check can see.**
- **Expected: Lemma 22's soundness fails for round-2 queries, because round-2 preimage membership "(ρ, i) ∈ S₂(q)" depends on round-1 answers that are certified only up to average underclaim.**
- The exact statement, to be proved or refuted: *there is a Merlin strategy passing Steps 1–5 for both rounds that inflates s₂(q) by the factor (1 + ζ) for some q with π₂(q) ≤ 2^{−J}, using round-1 underclaims on ≤ ζ·2^{−J} of rows.*

**Flag F (the fixed-oracle requirement, the deeper form of Flag I).**
- SS22's step (A) needs M correct for **context-insensitive** oracles K′ within β of K (hypothesis H5, robustness).
- Merlin's per-row choices within the tolerance make the oracle **row-dependent**: the same query q may receive different answers on different ρ.
- In the non-adaptive case, Props 15–16 force Merlin's answers to be canonical for good γ, *if* his counts are within (1 ± τ) of the truth. Underclaims break that on a small fraction of rows, and each such row contributes only its own output error, which SS22 absorbs in the ε/16 margins.
- **Adaptive:** a row-dependent round-1 oracle changes the round-2 query *distribution*. That is what Lemmas 21 and 22 certify for round 2, so the error is no longer per-row. **Expected: the error is absorbed at round 1 and not at round 2.**

**Does SS22's per-round γ-perturbation already bound steering? (The reviewer's question, answered before any work from the verified statements.)**
- Proposition 16 gives ϕ((1 + γ)s) = ϕ((1 + γ)t) whenever t ∈ [s/(1 + τ), s(1 + τ)] and γ avoids a bad set of measure O(τ) around µ(s).
- So the perturbation neutralizes **small** deviations: any claimed count within a (1 ± τ) factor yields the canonical answer, for a random γ.
- It does **not** neutralize an underclaim by a factor ≥ 2 (a shift of one or more bits in ϕ). That is outside Proposition 16's window, and is limited only by Step 4's average entropy check.
- Steering needs only such shifts on a small fraction of rows. **So the perturbation bounds steering by small deviations, but not steering by bit-shifts on a sparse set of rows.** Flag I lives in exactly that gap.
- Coherent inflation across rounds (the reviewer's alternative form) is the same move iterated. It is to be analysed after the 2-round case.

**Flag L (the lemma that would repair it).** Round-1 answers must be canonical on all but a ≪ ζ·min_q π₂(q) fraction of rows: **exact on almost all inputs**, not merely correct on average.
- Approximate counting (Goldwasser–Sipser; entropy estimation) certifies counts up to (1 + ζ) and averages; it gives no "canonical on all but 2^{−J}" guarantee.
- **So the repair needs a certified *canonical* approximate count**: a protocol in which Merlin cannot choose among valid approximations. This is to be checked against the literature on unique or canonical approximate counting (e.g. "pseudo-deterministic" or "canonical" AM protocols).
- The reviewer's (b)/Y4c route (a known lowness result) would have to supply exactly this. Low(AM) = AM ∩ coAM (verified in Y3) supplies it only when the oracle is a *language*, and a canonical count *would* be one (the language {(q, j) : J[γ](q) = j}). **So Y4c reduces to: is the canonical perturbed count J[γ] (for a fixed good γ) decidable in AM ∩ coAM?**
  - SS22 get consistency only "for a random γ, with high probability" (Props 15–16, the perturbation over λ̂). A fixed γ may be bad for some q, so the language {J[γ](q) = j} is in AM ∩ coAM *on the good q only*: a promise problem, not a language.
  - Whether Low(AM) extends to **promise** problems in AM ∩ coAM is the precise version of Y4c. As far as I know it does not in general, and that is to be checked.

**Kill test (the reviewer's).** The lemma must be silent on ABKMR (PSPACE via unbounded adaptivity). Two checks:
- that the error of any induction over rounds grows at least linearly in r, so it closes only for r ≪ 1/(per-round error);
- that ABKMR's (and [IW98]'s) round count exceeds that. The [IW98] round count is to be read, since Y3 noted it is not stated in the text read.

## §3. Literature (g1), in order

1. SS22 §5: the exact use of Step 4's tolerance, and Theorem 25's error accounting. Where does the per-row error enter?
2. Lemma 21's source [24] and Lemma 22's source [25] in SS22's bibliography: whether either is stated for oracle circuits or for promise-certified gates.
3. Lowness of promise AM ∩ coAM for AM, and any "canonical" or "pseudo-deterministic" approximate counting in AM.
4. [IW98]'s uniform reconstruction: the number of adaptive rounds (the kill test).

## Outcomes (the reviewer's, with (c) corrected per §1)

| Code | Outcome |
|---|---|
| **Y4a** | The 2-round lemma closes, and by induction O(1) rounds do. The theorem: bounded-round adaptive honest reductions at gap ω(log n) put L in AM ∩ coAM. Re-derive twice, and pass the kill test. |
| **Y4b** | Fails at a named step. Expected Flag I/F: inflation by steering in round-2 lower bounds. The missing statement is a canonical certified count (Flag L), recorded as open. |
| **Y4c** | The 2-round case reduces to a known lowness result: Low(AM) for the canonical-count *language*, or its promise extension if one is stated. Cite and climb. |

**Priors.**
- Reviewer: Y4b 55 / Y4a 30 / Y4c 15.
- Mine: **Y4b 60 / Y4a 25 / Y4c 15.** Carrying the flags in:
  - Flag I names a concrete attack on round-2 soundness, which lowers Y4a.
  - Flag L shows that Y4c needs a *promise* lowness, which I do not expect to find stated.
  - Y4a stays at 25 because the error could be absorbable by taking ζ polynomially small (Lemma 22 costs poly(1/ζ)) together with a sharper entropy tolerance. §3's item 1 decides it.

## Scoring note (the reviewer's, recorded before the ruling)

- The reviewer's expected failing step (c), "hidden ρ", is **withdrawn**. It is scored as the **reviewer's fifteenth premise miss**: the same failure mode as before, a settled finding (Y3: SS22's Corollary 26 is public-coin, and ρ is public in Step 2) not carried into the next pre-registration.
- **Practice line added:** every new pre-registration is checked against the previous report's refuted premises before it is sent.
- The candidate failing step is steering/inflation (Flags I and F), with the perturbation question answered in §2.
- The reviewer's priors are unchanged until the draft is ruled: Y4b 55 / Y4a 30 / Y4c 15.
