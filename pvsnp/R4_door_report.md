# R4: the door, report

*Run 2026-09-10 on branch `r4-door`, against the pre-registration (accepted; the reviewer's additions are incorporated: (1d) pre-registered both ways, and part (3) names the reduction type). g1 applies throughout: "verified" means checked against the paper's text, or its official abstract where stated. The report is in part / expected / observed form.*

## Outcome: **D1**

The door is already a stated research programme. Liu–Pass (CCC 2022) write it as a crisp characterization (verified, l.248–252):

> *"There exists (concrete) polynomials t, ζ such that 'Basing OWFs on NP ⊄ BPP' is equivalent to the existence of a worst-case to (mild) average-case reduction for McK^tP[ζ]."*

Hirahara's line of work (FOCS 2018, STOC 2023) is the non-black-box side of the same programme.

This report contributes three things:
- the door sentence, with its reduction types stated exactly (§3);
- an elementary fact settling part (1d) for random graphs;
- an honest "unknown" for part (1c).

Priors: mine D1 75; the reviewer's D1 65.

## Part (1): size-verifiability of the smallest case (d = 3, P non-linear, m = Θ(n))

**(a) Which notion the barrier needs.**
- *Expected:* exact or approximate.
- *Observed (verified):* Bogdanov–Brzuska, Theorem 1 and Corollary 2. If f is efficiently computable and **approximately** size-verifiable, there is no efficient reduction from an NP-hard L to inverting f *with respect to deterministic inversion oracles*, unless NP ⊆ coAM. Approximate size-verifiability suffices for the barrier.
- AGGM's own statement of the adaptive case (verified, §1.1, l.90–101): it covers f such that "|f⁻¹(y)| is efficiently computable given y", and "more generally … efficiently verifiable via an AM protocol", for example regular functions with an efficiently recognizable range. It "holds for any reduction, including adaptive ones".

**(b) Lower bounds.**
- *Expected:* always in AM.
- *Observed (verified):* AGGM Theorem 5 (Goldwasser–Sipser): for every NP set S there is an AM protocol for which an honest prover with s = |S| is accepted, and every prover is rejected if s > (1 + ρ)|S|. The preimage set f⁻¹(y) is an NP set.

**(c) Upper bounds in AM for local f.**
- *Expected:* unknown.
- *Observed:* **unknown (g8).**
- *Search, stated:* queries on AM upper-bound protocols for preimage or CSP-solution counts, and on the size-verifiability of Goldreich's function. They found no result establishing or refuting approximate size-verifiability for random local functions.
- The nearest results do not reach it:
  - **Abbe–Edwards** (arXiv:1504.08316, abstract verified): for random planted CSPs and Goldreich's model, (1/n)·log Z → φ_k(α) in probability. That is concentration of the **logarithm**, precision 2^{o(n)}, not the (1 + 1/a) multiplicative precision that approximate size-verifiability needs.
  - **Cook–Etesami–Miller–Trevisan** (ECCC TR12-175, abstract verified): they "bound the expected size of this preimage" for random right-degree-d graphs with typical random predicates, or predicates of the form x₁⊕…⊕x_{d−h}⊕Q(…). That is an expectation, not per-y verification.
- **Consequence:** the adaptive half is **unbarred** for the smallest case, as far as the verified record goes. That is not a proof that it is open.

**(d) Preimage size, both ways as pre-registered.**
- *Expected:* not almost injective, because the graph is sparse.
- *Observed (proved here, for random graphs):*

*Claim.* Let G be a random d-uniform hypergraph with m = c·n hyperedges on n inputs, with d and c constants, and let f = f_{G,P}. Let I be the number of inputs that lie in no hyperedge. Then with probability 1 − 2^{−Ω(n)} over G, I ≥ (1/2)·n·e^{−cd}, and every preimage set satisfies |f⁻¹(f(x))| ≥ 2^I = 2^{Ω(n)}.

*Proof.*
- **Expectation.** A fixed input avoids one hyperedge with probability 1 − d/n, so it avoids all of them with probability (1 − d/n)^{cn} → e^{−cd}. Hence E[I] = (1 − o(1))·n·e^{−cd}.
- **Concentration.** I is a function of the m independent hyperedges, and changing one hyperedge changes I by at most d. By McDiarmid's inequality, Pr[I < E[I] − λ] ≤ exp(−2λ² / (m·d²)). With λ = n·e^{−cd}/3 this is exp(−Ω(n)).
- **Preimages.** Flipping an isolated input never changes the output, so every x has at least 2^I preimages under f. ∎

**Therefore** the smallest random-graph case is **not almost injective**, and AGGM's polynomial-preimage route does **not** bar the adaptive half. (Large preimages do not by themselves rule out size-verifiability: regular functions are size-verifiable.) For Goldreich's *expander* family, whose graph may be built with no isolated inputs, (1d) is **not settled here**.

## Part (2): the non-black-box half, mapped

**What Hirahara's reduction reads, and why.**
- *Expected (the reviewer's):* MINKT is a problem about programs, so the heuristic's code is instance-shaped.
- *Observed (verified, Hirahara 2018, l.380–404):* the argument has four steps.
  1. Few strings are compressible, so MINKT[r] has few Yes instances. An errorless heuristic must therefore reject a large fraction of random strings.
  2. That gives a dense test T ∈ P, which is a statistical test for any hitting-set generator, in particular for the Nisan–Wigderson generator applied to Enc(x).
  3. The NW reconstruction then gives a short description d of x *relative to T*.
  4. x is described by d together with "a source code of the algorithm accepting T". This is "the crucial part in which our proof is non-black-box".
- **So the reviewer's expectation holds, and one ingredient is added.** The lever is the **density fact** from R2's barrier (few compressible strings), and the code is spliced into a *description*, which is exactly what MINKT measures. The same fact that blocks exhibiting special strings is what makes the heuristic usable as a dense test.

**Why it evades BT06 / FF93.** Those barriers concern black-box reductions. Hirahara argues directly that a non-adaptive black-box version would give Gap_{σ,τ}MINKT ∈ coNP/poly (l.283–286; verified in R3-fold).

**Gap (i): NP-hardness of the source.** The verified results, with reduction types:

| Problem | NP-hard under | Source |
|---|---|---|
| McK^tP[ζ], for t ≥ n² and some polynomial ζ | **randomized polynomial-time reductions** (NP-complete) | Liu–Pass CCC'22, Theorem 1.2 |
| learning programs / partial MCSP | **randomized polynomial-time many-one reductions** | Hirahara FOCS'22, ECCC TR22-119 abstract |
| Multi-MCSP | **many-one randomized polynomial-time reductions** | Ilango–Loff–Oliveira CCC'20, Theorem 4 |
| Partial-MCSP | "even under **deterministic** reductions" (a "substantially simpler proof") | Ilango–Loff–Oliveira CCC'20, text l.227 |

The problem Hirahara's 2018 reduction starts from, GapMINKT, is **not** among them.

**Gap (ii): the landing at OWF.**
- **Liu–Pass 2020, Theorem 1.1:** OWF ⟺ K^t is mildly hard-on-average over the uniform distribution (verified in R1).
- **Liu–Pass CCC'22, Theorem 1.1:** for every t ≥ 1.1n and every ζ, mild average-case hardness of McK^tP[ζ] ⟺ OWF (verified).
- **Hirahara STOC'23** (ECCC TR23-037, abstract verified): OWF exist iff "it is NP-hard to approximate the distributional Kolmogorov complexity under randomized polynomial-time reductions **and** NP is hard in the worst case". Under the *Meta-Complexity Padding Conjecture*, the worst-case hardness of an approximate MCSP characterizes OWF.
- **The landing gap, stated exactly.** Hirahara 2018 lands at DistNP ⊄ AvgP, in the errorless model. Both of the equivalences above land at OWF, but they need a worst-to-*mild*-average reduction (Liu–Pass) or a randomized NP-hardness of distributional K^t (Hirahara 2023) that no one has produced.

## Part (3): the sentence that would close the door

> **A worst-case to mild-average-case reduction under the uniform distribution for McK^tP[ζ] — with t(n) ≥ n² and the ζ of Liu–Pass CCC'22 Theorem 1.2, a problem NP-complete under *randomized* polynomial-time reductions — would, by that paper's Theorems 1.1 and 1.2, base one-way functions on NP ⊄ BPP. Such a reduction must be adaptive or non-black-box.**

**Why "adaptive or non-black-box".** McK^tP[ζ] is in NP. A non-adaptive black-box δ worst-to-average reduction from it to its own average case would, by Bogdanov–Trevisan Theorem 7 (verified), put it in AM_poly. For a problem that is NP-hard even only under randomized reductions, that is the kind of collapse the literature treats as implausible, and Hirahara makes the same argument for GapMINKT (l.283–286). *This last step is a standard inference, not a separately cited theorem.*

**The smallest instance:** t(n) = n², with ζ as in Theorem 1.2.

**The closest known technique:** Hirahara's 2018 non-black-box reduction, which splices code into a description through the density-derived test. It lacks:
1. a source problem that is NP-hard. It starts from GapMINKT, unconditional, not the conditional McK^tP;
2. the right error model. It uses errorless heuristics, while mild hardness allows two-sided 1/p error;
3. the right landing. It reaches DistNP ⊄ AvgP, not OWF.

## Calibration

- **The reviewer:**
  - The expectation about *what the code is used for* was confirmed, with the density ingredient added.
  - "AGGM's poly-preimage case" is BB14's description of the part AGGM10 did not retract. AGGM's own adaptive hypothesis is computable or AM-verifiable preimage size (§1.1, l.90–101). This is a note, not a miss.
  - D3 through (1d) did not occur.
- **Me:** (1c) unknown and (1d) proved for random graphs matched the pre-registration. D1 held.

## Sources checked in R4 (beyond earlier ledgers)

- Liu–Pass, *On One-Way Functions from NP-Complete Problems*, CCC 2022: <https://drops.dagstuhl.de/storage/00lipics/lipics-vol234-ccc2022/LIPIcs.CCC.2022.36/LIPIcs.CCC.2022.36.pdf> (text l.238–252)
- Hirahara, *NP-Hardness of Learning Programs and Partial MCSP*, FOCS 2022: <https://eccc.weizmann.ac.il/report/2022/119/> (abstract)
- Hirahara, *Capturing One-Way Functions via NP-Hardness of Meta-Complexity*, STOC 2023: <https://eccc.weizmann.ac.il/report/2023/037/> (abstract)
- Ilango–Loff–Oliveira, CCC 2020: <https://drops.dagstuhl.de/storage/00lipics/lipics-vol169-ccc2020/LIPIcs.CCC.2020.22/LIPIcs.CCC.2020.22.pdf> (text l.227–236)
- Abbe–Edwards, arXiv:1504.08316: <https://arxiv.org/abs/1504.08316> (abstract)
- Cook–Etesami–Miller–Trevisan, ECCC TR12-175: <https://eccc.weizmann.ac.il/report/2012/175/> (abstract)
- Bogdanov–Brzuska, ECCC TR14-108 (text, Theorem 1 and Corollary 2); AGGM (text §1.1, Theorem 5); Hirahara 2018 (text l.380–404). All re-read locally.
