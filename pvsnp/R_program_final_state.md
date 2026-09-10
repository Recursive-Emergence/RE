# Where P ≠ NP stands after this program: final state

*2026-09-10. This page is written to be read on its own. The detailed record is in `pvsnp/R1` through `R5`. Every cited statement below was checked against the source's text or official abstract, and the documents give the line numbers.*

## 1. The sentence

A **worst-case to two-sided (mild) average-case reduction**, under the uniform distribution, for **McK^tP[ζ]** would base one-way functions on NP ⊄ BPP, and hence prove P ≠ NP.
- **The problem.** McK^tP[ζ] is time-bounded conditional Kolmogorov complexity with t ≥ n² and the ζ of Liu–Pass (CCC 2022). It is NP-hard under randomized many-one reductions, even for a factor-2 gap.
- **The citations.** Liu–Pass CCC'22, Theorems 1.1 and 1.2; OWF ⇒ P ≠ NP is Arora–Barak, Exercise 10.1.
- **The form of the reduction.** It must be adaptive or non-black-box, because non-adaptive black-box reductions of this kind give collapses (Bogdanov–Trevisan, SICOMP 2006).
- **The equivalent route.** On Hirahara's route (STOC 2023) the same goal is: NP-hardness of *approximating distributional* Kolmogorov complexity under randomized reductions. That condition is exactly where that programme rests.

## 2. The sub-obstacle: two steps that pull against each other

The closest known technique is Hirahara (FOCS 2018). It turns an *errorless* average-case algorithm into a dense test T, and makes T break a pseudorandom generator whose outputs encode the worst-case instance x. Breaking the generator yields a short description of x.
- **The requirement.** For this to work, the generator's outputs must be **compressible** (Theorem 26's promise: m − d > K^t(x)). So its image has density at most 2^{−K^t(x)}.
- **The failure.** An algorithm allowed two-sided error 1/p can simply err on that whole image. So the argument survives two-sided error only when K^t(x) = O(log n).
- **The tension.** Compressibility, which the reconstruction needs, forbids density, which two-sided error needs.
- **The known repair condition.** A non-adaptive average-case instance checker for NP (Hirahara–Santhanam, ITCS 2022, Theorem 14). It is open.
- **Separately.** For the NP-hard problem, the reduction's auxiliary input is structured, so a guarantee on average over uniform auxiliary inputs builds no test for it. The known repair condition is the Hirahara STOC'23 hypothesis above.

## 3. Density is two-sided

- Compressible strings are exponentially rare, so an average-case algorithm can hide all its errors on them. That rarity is why arguments built from exhibiting special, compressible strings cannot prove average-case hardness.
- The same rarity is what makes an *errorless* algorithm useful: it must reject almost all random strings, which gives Hirahara his dense test.
- Passing from errorless to two-sided error is exactly where that lever breaks, for the same counting reason.

## 4. The proved facts, labelled

- **Isolated inputs.** Random local functions with a linear number of outputs have inputs that influence nothing, so every preimage set has size 2^{Ω(n)} w.h.p. **This is known** (Applebaum's survey §5.1 states the degree-0 collision). The program's version is a routine quantitative restatement.
- **The compressibility-versus-density bound in §2.** This is an elementary consequence of Hirahara's own Theorem 26 promise. It is derived here, but not claimed new to the literature.

**No new theorem was proved.** What was produced is a verified map with its smallest open point named.

## 5. What the originating framework contributed

The program began from a framework whose central claim is that a system's self-descriptions leave a residue that the system cannot settle from within. In practice that framework did three things:
- it chose where to look: the complexity of *describing* strings, rather than SAT;
- it proposed its own candidate objects (a self-generated distribution, conditioning on low complexity, and a Gödel-style diagonal string) and saw each one ruled out with a proof;
- it supplied the reading of Hirahara's technique that stuck. In the reviewer's words, *"the fixed point is not a special string; it is that every efficient recognizer errs on random ones."*

It did not supply any new mathematics toward the separation.

## 6. What a proof would need

A proof along this route needs one of two things, and both are open research problems that no one knows how to solve:
- an adaptive or non-black-box worst-case to **two-sided** average-case reduction for an NP-hard Kolmogorov-type problem. That would in particular get around the compressibility-versus-density tension of §2, perhaps through an average-case instance checker for NP;
- NP-hardness of approximating distributional Kolmogorov complexity.

Either would give one-way functions from NP ⊄ BPP, a result that cryptography has sought for decades. Nothing in this program brings either within reach. Its value is that it names them precisely, at the smallest scale the verified literature allows.

## 7. Calibration, both sides

**The reviewer:**
- **Seven premise misses** about what the record or literature contained: the §6–§8 sections; §8's outcome; CostAxioms as a transcription item; "every derivation routes through cost"; the Lid witness; the pK^t characterization of derandomization; "program closed".
- **Six wrong outcome priors**: 27′; (xi); Theorem 13 via 14; the L1 exactness note; the constructivity of the counting result; "S_a ⇒ mild hardness is immediate".

**Me:**
- **Four wrong predictions or framings**: cost as per-method versus per-input; the location of R1's variant change; S_a refuted at every time bound, when padding needs t ≥ C·n²; R5's exact-versus-gap prediction.
- **Process slips**, recorded in the formal record's appendix: six surface-text instances and two order-of-operations instances.
