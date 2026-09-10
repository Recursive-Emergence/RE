# R1: the reduction chain, report

*Run 2026-09-10 on branch `r1-chain`, against the pre-registration in `R1_chain_preregistration.md`, which the reviewer accepted. Every statement marked **verified** was checked against the paper's own text (PDFs converted locally with `pdftotext`, line-level). Anything else is marked **UNVERIFIED** and, by guard g1, does not count.*

## Outcome: **R1b**

The chain goes through on known results only after **two changes of variant**:

- the MCSP threshold becomes 2^{εn} (or poly(n), under exponentially hard OWF);
- the security of the one-way functions becomes **non-uniform**.

The second change is the weak link. The OWF ⟺ K^t equivalence (Liu–Pass) is stated for uniform PPT adversaries, and I found no verified route from uniformly secure OWF to MCSP hardness.

Priors: mine R1b 65, the reviewer's R1b 60. The outcome matched, but my predicted *location* was partly wrong (finding F1).

## Arrow by arrow

**A1. MCSP ∉ P ⇒ P ≠ NP.** *Unconditional, elementary.*
- MCSP-C is defined as: given (y, s) with y ∈ {0,1}^{2^n}, does fn(y) have C-circuits of size ≤ s? Parameterized variants fix s in advance (Hirahara–Santhanam CCC'17, Definition 5, verified).
- The input length is N = 2^n. Guessing a circuit of size ≤ s ≤ 2^n and evaluating it on all 2^n inputs takes time poly(N), so MCSP[s] ∈ NP for every polynomial-time computable s.
- No citation is needed.

**A2. Zero-error average-case hardness of MCSP[s] ⇒ MCSP[s] ∉ C.** *Unconditional, trivial.*
- The notion used is Hirahara–Santhanam Definition 11 (verified). "Solvable in C on average with success ε" means A(x) ∈ {L(x), '?'} for every x, and A(x) = L(x) with probability ≥ ε over x ∼ U.
- A worst-case algorithm is a zero-error average-case algorithm with success 1.
- Hirahara–Santhanam explain why the notion must be zero-error (§1, verified). For s = o(2^n/n), almost every truth table is a NO instance, so answering "NO" everywhere succeeds with high probability.

**A3. One-way functions ⇒ MCSP zero-error hard on average (uniform distribution).** *Unconditional, but only in the variants below.*

Step 1. **Average-case easiness is equivalent to natural properties.** For s(n) = 2^n / n^{ω(1)}, the following are equivalent for C ∈ {P, SIZE(poly)} (Hirahara–Santhanam Proposition 12, verified; Santhanam ITCS'20 Proposition 8, verified, citing it):
- C-natural properties useful against SIZE(s(cn)) exist, for all c;
- MCSP[s(cn)] is solvable in C on average with success 1/poly(N);
- the same, with success 1 − 1/poly(N).

This matters because it makes the average case the *uniform distribution on truth tables*.

Step 2(a). **Exponentially hard OWF ⇒ MCSP[poly(n)] zero-error hard on average** (non-uniform adversaries).
- Santhanam ITCS'20 §1.3 (verified): *"This can be re-interpreted [24] as saying that if exponentially-hard one-way functions exist, then MCSP[poly(n)] is zero-error hard on average."*
- The source is Razborov–Rudich. Its statement as restated in Hirahara–Santhanam Theorem 22 is verified: exponentially hard OWF ⇒ no SIZE(poly)-natural properties useful against SIZE(poly). Razborov–Rudich's own text was not reachable (HTTP 403 and a certificate error).
- The PRF step is GGM as restated in Hirahara–Santhanam Theorem 21 (verified). GGM's own text was not reachable (connection reset).

Step 2(b). **OWF secure against SIZE(poly) ⇒ MCSP[2^{εn}] zero-error hard on average against SIZE(poly(N)), for every ε > 0.**
- Santhanam ITCS'20 Theorem 22 lists these as items (1)/(2) ⇒ (8) ⇔ (7) (verified).
- The implication (2) ⇒ (8) is proved by "applying the constructions of [22] and [20]" (HILL and GGM) to auxiliary-input OWF. **As written, that proof does not invoke Conjecture 19**, although Theorem 22 as a whole is stated under it. This is my reading of the proof text; it is not a separately stated unconditional theorem.
- (7) ⇔ (8) is Hirahara–Santhanam, via Step 1.

Step 2(c). **The uniform route: PPT-secure OWF ⇒ MCSP ∉ BPP.** Attributed to Kabanets–Cai, STOC 2000 (a search summary reads "MCSP ∈ BPP implies that any one-way function can be inverted"). **UNVERIFIED:** the ECCC PDF (TR99-045) uses Type 3 fonts, so no text could be extracted. Excluded by g1.

Two variant changes follow:
- **Threshold:** 2^{εn}, or poly(n) only under exponentially hard OWF.
- **Adversary:** non-uniform, on both the OWF side and the MCSP side.

**A4. OWF ⟺ K^t mildly hard on average.** *Unconditional, uniform.*
- Liu–Pass 2020 (arXiv:2009.11514), Theorem 1.1 (verified): OWF exist iff K^poly is mildly hard-on-average. It is strengthened in the text to every polynomial t(n) ≥ (1+ε)n.
- "Mildly HoA" (verified, §1): there is a polynomial p such that every PPT algorithm **fails to compute K^t exactly** on at least a 1/p(n) fraction of uniform n-bit strings, for all sufficiently large n.
- Theorem 1.2 (verified) extends this to (d log n)-approximation.
- OWF are defined against **PPT** adversaries (Definition 2.1, verified), and the text makes no non-uniform remark.

**A5. The junction: not a link.**
- A4 gives OWF secure against **uniform** PPT adversaries. A3's verified route needs OWF secure against **SIZE(poly)**. No implication from the first to the second was found, and none is known in general. So "K^t mildly HoA ⇒ MCSP zero-error average-hard" is **not closed on verified links**.
- MCSP and K^t can't be swapped at the bottom either. Santhanam's equivalence between OWF and MCSP[2^{εn}] zero-error hardness holds only **under his Universality Conjecture** (Conjecture 19, verified). Liu–Pass describe it the same way, as "under a new (and somewhat complicated) conjecture" (verified, §1).
- K^t therefore describes the bottom of the chain but is not a link in it, as pre-registered.

## The derandomization obstruction at the bottom

**The Chaitin diagonal fails in the time-bounded, randomized setting.** This is my argument, not a citation. Search for the first string a recognizer of "K^t(x) ≥ n − c" accepts, and output it:
- the search is exponential, so it bounds no polynomial K^t;
- with a randomized recognizer, the output is not one fixed string.

**pK^t is the measure built to tolerate randomness.**
- Goldberg–Kabanets–Lu–Oliveira CCC'22, Definition 17 (verified): pK^t_δ(x | y) is the least k such that, with probability ≥ δ over w ∼ {0,1}^t, some k-bit M outputs x from (w, y) within t steps.
- Under standard derandomization assumptions, K^{poly(t)}, pK^{poly(t)} and rK^{poly(t)} agree up to an additive O(log t) (their §1, verified).

**A correction to the ruling.** The derandomization characterization verified here is **not** about probabilistic K^t.
- Liu–Pass CCC'22, Theorem 1 (verified): prBPP = prP iff, for every BPTIME(n^c) algorithm M and every sufficiently long z, there is some x on which M fails to decide GapMcKtP[O(log n), n − 1]. This concerns **conditional Levin Kt**, is **worst-case** over x, and is the **promise** version.
- Chen–Tell (STOC 2021) is compared there as having "a gap between the sufficient and necessary assumptions" (verified, from Liu–Pass's own comparison).
- A characterization of OWF via boundary hardness of pK^t appears in search results (ITCS 2026). It is UNVERIFIED and not used.

## Findings

1. **F1: the A3 prediction was partly wrong.** I pre-registered a PRF-vs-uniform distribution mismatch at A3. Instead, zero-error average-case hardness over the **uniform** distribution is exactly what natural properties give (Step 1). The variant changes are the threshold and non-uniformity.
2. **F2: the weak link is uniform vs non-uniform security.**
   - Liu–Pass's OWF are secure against uniform adversaries, and the verified MCSP route needs non-uniform security.
   - Closing it needs one of three things: a verified uniform version of A3 (Kabanets–Cai, pending a readable source); a non-uniform version of Liu–Pass; or a uniform-to-non-uniform transfer, which is not known in general.
3. **F3: the reviewer's pK^t characterization claim does not match the verified source.** The verified derandomization characterization is for conditional Levin Kt, worst-case, promise problems.

## Verification ledger

| Claim | Source | Where checked | Status |
|---|---|---|---|
| OWF ⟺ K^t mildly HoA; t ≥ (1+ε)n | Liu–Pass 2020, Theorem 1.1 | arXiv PDF, text l.107–120 | verified |
| mildly HoA = exact computation, PPT, uniform, 1/p | Liu–Pass 2020, §1 | l.94–100 | verified |
| approximation version | Liu–Pass 2020, Theorem 1.2 | l.133 | verified |
| OWF defined against PPT | Liu–Pass 2020, Definition 2.1 | l.397 | verified |
| Santhanam's OWF⟺MCSP equivalence is conditional | Liu–Pass 2020, §1 | l.184–188 | verified |
| MCSP-C definition | Hirahara–Santhanam 2017, Definition 5 | DROPS PDF | verified |
| zero-error average-case notion | Hirahara–Santhanam 2017, Definitions 11 and 13 | l.323–330 | verified |
| natural properties ⟺ average-case easiness | Hirahara–Santhanam 2017, Proposition 12 | l.335–361 | verified |
| exponentially hard OWF ⇒ PRFG vs SIZE(poly) (GGM) | Hirahara–Santhanam 2017, Theorem 21 | l.476 | verified (secondary) |
| exponentially hard OWF ⇒ no SIZE(poly)-natural properties (Razborov–Rudich) | Hirahara–Santhanam 2017, Theorem 22 | l.484 | verified (secondary) |
| exponentially hard OWF ⇒ MCSP[poly] zero-error hard | Santhanam 2020, §1.3 | l.469–472 | verified |
| Theorem 22 items; the (2)⇒(8) proof | Santhanam 2020, Theorem 22 | l.1012–1051 | verified; the reading that it needs no conjecture is mine |
| Universality Conjecture | Santhanam 2020, Conjecture 19 | l.999 | verified |
| OWF ⟺ PRG | HILL 1999, Theorem 7 | PostScript → text, l.1148 | verified |
| prBPP = prP ⟺ GapMcKtP hardness | Liu–Pass CCC'22, Theorem 1 | l.142–148 | verified |
| Chen–Tell has a sufficient/necessary gap | Liu–Pass CCC'22, comparison | l.184–186 | verified (secondary) |
| pK^t definition | Goldberg–Kabanets–Lu–Oliveira 2022, Definition 17 | DROPS PDF | verified |
| K = pK = rK under derandomization assumptions | Goldberg–Kabanets–Lu–Oliveira 2022, §1 | l.278–280 | verified |
| MCSP ∈ BPP ⇒ OWF invertible | Kabanets–Cai 2000 | ECCC TR99-045 (Type 3 fonts) | **UNVERIFIED** |
| Razborov–Rudich original | JCSS 1997 / STOC 1994 | HTTP 403, certificate error | **UNVERIFIED** (restatement used) |
| GGM original | JACM 1986 | connection reset | **UNVERIFIED** (restatement used) |
| OWF ⟺ boundary pK^t hardness | ITCS 2026 (search result only) | not fetched | **UNVERIFIED**, unused |

## Sources

- Liu, Pass. On One-way Functions and Kolmogorov Complexity. <https://arxiv.org/abs/2009.11514>
- Hirahara, Santhanam. On the Average-Case Complexity of MCSP and Its Variants. CCC 2017. <https://drops.dagstuhl.de/storage/00lipics/lipics-vol079-ccc2017/LIPIcs.CCC.2017.7/LIPIcs.CCC.2017.7.pdf>
- Santhanam. Pseudorandomness and the Minimum Circuit Size Problem. ITCS 2020. <https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.68/LIPIcs.ITCS.2020.68.pdf>
- Liu, Pass. Characterizing Derandomization Through Hardness of Levin-Kolmogorov Complexity. CCC 2022. <https://drops.dagstuhl.de/storage/00lipics/lipics-vol234-ccc2022/LIPIcs.CCC.2022.35/LIPIcs.CCC.2022.35.pdf>
- Goldberg, Kabanets, Lu, Oliveira. Probabilistic Kolmogorov Complexity with Applications to Average-Case Complexity. CCC 2022. <https://drops.dagstuhl.de/storage/00lipics/lipics-vol234-ccc2022/LIPIcs.CCC.2022.16/LIPIcs.CCC.2022.16.pdf>
- Håstad, Impagliazzo, Levin, Luby. A Pseudorandom Generator from any One-way Function. <https://cseweb.ucsd.edu/~russell/sicomp.ps>
- Kabanets, Cai. Circuit Minimization Problem. ECCC TR99-045. <https://eccc.weizmann.ac.il/report/1999/045/> (text not extractable)
