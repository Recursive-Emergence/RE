# Y3: the adaptive question. Pre-registration

*Drafted 2026-09-11 on branch `y3-adaptive`, on the author's go ("Draft Y3 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply: smallest case first; every bound beside the record and the literature; every flag's implication carried into the priors.*

## Ceiling (first)

This line's success is OWF from NP ⊄ BPP-type hardness, which is conditional. Y3 at best narrows the door of LP23's holy grail to a round count. It proves nothing about P vs NP.

## §0. Facts verified at drafting (SS22's text, read this session)

1. **The reviewer's (b) is answered by the text.** The NEXP-hardness at an O(log n) gap is under **non-adaptive** reductions.
   - SS22 l.15–16: "using results of Hirahara [28], it follows that every language in NEXP has a randomized polynomial-time **non-adaptive** reduction … to O(log(n))-approximating the Kolmogorov complexity".
   - The same at l.205–207 and l.219–221.
   - [28] = Hirahara, "Unexpected hardness results for Kolmogorov complexity under uniform reductions" (STOC'20; SS22's bibliography l.1580).
   - **Consistency fact (to be written as a proof in the run):** any barrier covering honest non-adaptive reductions at an O(log n) gap, with an AM ∩ coAM conclusion, would place NEXP ⊆ AM ∩ coAM (⊆ Σ₂^p ∩ Π₂^p). That is not known to be false, but it is a collapse no one expects. So barriers of SS22's kind can exist only at gap ω(log n), matching SS22's "sharp dichotomy" (l.199–207). **The O(log n) gap is open from both sides.**
2. **Adaptivity is already known to be powerful at large gaps.**
   - SS22 l.221–223: "When the randomized reduction is allowed to be adaptive, it follows from work of [6] that approximating Kolmogorov complexity, even for large multiplicative approximation gap |q|^{1−ϵ} for any ϵ > 0, is hard for PSPACE."
   - [6] = Allender–Buhrman–Koucký–van Melkebeek–Ronneburger, "Power from random strings", SIAM J. Comput. 35(6), 2006 (SS22's bibliography l.1504–1505).
   - **Flag U (a ceiling on Y3a, before any work):** the entropy/coding barrier cannot extend to *unbounded* adaptivity at gap ω(log n) unless PSPACE ⊆ AM ∩ coAM, which gives PH = PSPACE = Σ₂^p. **So any extension breaks somewhere between O(1) rounds and polynomially many.** Y3's job is to find where.
3. **How SS22's proof uses non-adaptivity** (l.315–392).
   - Fix M and x. Let π(q) be the probability over (ρ, a random index i) that q_i(ρ) = q. The context-sensitive oracle is J(q) = ⌈log 1/π(q)⌉.
   - (A) M^J agrees with M^K except with probability ε/2. This goes through a context-insensitive K′ that is β-close to K, and uses "the first x on which the simulation fails", which is where honesty and computability enter.
   - (B) M^J is simulated in AM ∩ coAM by approximate counting of π(q) [25, 20], with a perturbation J[γ] so that the protocol's answers are consistent.

## §1. Arm (a): extending the barrier to r-round adaptive reductions, with my flags

**Flag C (step (A) survives adaptivity; expected).**
- For an r-round adaptive M, define J round by round:
  - π₁ from the round-1 queries;
  - then π₂(q) = Pr_ρ[q is a round-2 query of M^J(x; ρ)], with round-1 answers given by J;
  - and so on.
- J remains a computable function of q for fixed (M, x). So the coding theorem still gives K(q) ≤ J(q) + K(M, x) + O(log|q|).
- The counting direction (Pr_π[K(q) < log 1/π(q) − β] ≤ 2^{−β}·poly) holds for any distribution.
- The "first failing x" trick gives K(x) = O(log|x|), as in SS22.
- **So, contrary to the reviewer's expected failure ("answers as advice injecting entropy"), I expect step (A) to survive.** The answers are determined by (x, ρ) through J itself, not supplied as advice. This is to be checked against SS22's actual proof of (A), which may use non-adaptivity in K′'s construction.

**Flag S (step (B) fails first, at secrecy; my expected first failing step).**
- Approximating π₂(q) needs both a **lower bound** (Goldwasser–Sipser; public coins; fine) and an **upper bound** (the coAM side, e.g. Aiello–Håstad/Fortnow-type protocols).
- The upper-bound protocols need the verifier to hold a **secret** sample ρ and to evaluate the round-2 queries q₂(ρ). That evaluation needs J on the round-1 queries q₁(ρ), whose values are approximate counts that only the prover can certify.
- Asking the prover for them **reveals q₁(ρ)**, which leaks information about the secret ρ. In the non-adaptive case the verifier computes all queries itself, and nothing leaks.
- **Expected: 2-round adaptivity fails at the coAM (upper-bound) half of step (B), by leakage of the secret sample through the round-1 queries.** The AM (lower-bound) half is expected to survive, giving a one-sided (AM-only) consequence at best, which does not collapse PH for NP.
- **If leakage can be avoided** (e.g. round-1 queries of high min-entropy that reveal little about ρ, or a Merlin-free estimate of J on round-1 queries), the extension goes through for O(1) rounds. That needs the composition of AM ∩ coAM approximate counting to nest r times, i.e. a lowness property of AM ∩ coAM *for itself* or for AM.
  - To be checked under g1. Arvind–Köbler show AM ∩ coAM is low for ZPP^NP (secondary; search summary only), which is **useless for NP** (SAT ∈ ZPP^NP trivially). Lowness for AM is what would be needed.

**Proposition H′ (conditional; ours; sketch; an analogue of Y2's Proposition H at the adaptive end).**
- Suppose [6]'s adaptive PSPACE reduction is correct for every oracle within a multiplicative gap |q|^{1−ϵ} of K.
- Suppose its queries have depth K^t(q) − K(q) ≤ |q|^{1−ϵ}/2 with high probability, for a fixed polynomial t.
- Then K^t answers the queries within the gap (K^t is computable in P^NP by binary search), so PSPACE ⊆ BPP^NP ⊆ Σ₃^p, and PH collapses to Σ₃^p = PSPACE.
- **So, unless PSPACE ⊆ BPP^NP, [6]'s adaptive queries are very deep: depth ≥ |q|^{1−ϵ}/2 on a noticeable fraction.** Hiding is depth at the adaptive end too, with a polynomial rather than logarithmic depth threshold.
- To verify: [6]'s exact robustness statement, and whether its reduction is honest.

## §2. Arm (b): the converse check

Fact 1 of §0 is to be written as a proof. [28]'s reduction is non-adaptive, so the O(log n) gap is open from both sides. The run adds the statement's exact hypotheses from [28]'s text (honesty, number of queries, advantage).

## §3. Arm (c): Proposition H's two checks

These need [28]'s construction:
- the tolerated error constant c in "O(log n)-approximating";
- the depth of its queries.

Proposition H′ adds the same two checks for [6]. If either reduction's queries are **provably** deep, **hiding is depth becomes a theorem at that end**, and a constraint on any NP-level reduction: it must query non-deep strings (LP23's promise) while doing what those reductions do only through deep ones.

## §4. Literature (g1), in order

1. SS22's proof of (A) and (B), where non-adaptivity is used: §§4–6 of the full text.
2. [6] ABKMR 2006: the adaptive PSPACE reduction; robustness, honesty and rounds.
3. [28] Hirahara STOC'20: the NEXP non-adaptive reduction; its constant and its queries.
4. Any statement on adaptive reductions to K-approximation or to R_K with an AM ∩ coAM or SZK conclusion for bounded rounds (Hirahara–Watanabe; Saks–Santhanam follow-ups; GK24's related work).
5. Huang–Ilango–Ren (STOC'23, "NP-hardness of approximating meta-complexity: a cryptographic approach"): which reduction class their NP-hardness uses, and how it evades SS22's Theorem 2.
6. The lowness of AM ∩ coAM for AM.

## Outcomes (the reviewer's, with (c) adjusted to §0's verified fact)

| Code | Outcome |
|---|---|
| **Y3a** | The barrier extends to O(1)-round (or bounded-query) adaptive reductions at gap ω(log n): a new theorem if not stated. The door narrows to super-constant rounds, non-explicit arguments or compact reductions. Re-derive twice. |
| **Y3b** | It fails at a named step, expected Flag S (coAM secrecy at round 2). That step is where an adaptive reduction would have to live. |
| **Y3c** | *(Adjusted: SS22's NEXP reduction is verified non-adaptive, so the reviewer's original Y3c cannot occur as stated.)* [6]'s adaptive PSPACE reduction, or [28]'s structure, yields an NP-level template for the top-threshold regime. |

**Priors.**
- Reviewer: Y3b 55 / Y3a 30 / Y3c 15.
- Mine: **Y3b 55 / Y3a 35 / Y3c 10.** Carrying the flags into the prior:
  - Flag C moves weight toward step (A) surviving, which raises Y3a a little.
  - Flag S keeps Y3b the most likely.
  - Flag U caps Y3a at bounded rounds.
  - §0's fact 1 removes the reviewer's version of Y3c.
