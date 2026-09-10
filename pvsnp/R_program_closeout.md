# The R-program: close-out

*2026-09-10. R1 (outcome R1b) and R2 (outcome S1) were each accepted by the reviewer; both are merged. The program closes here unless it is reopened (§5). Everything below is proved here or verified in the R1 and R2 documents.*

## 1. The shrink

> **P ≠ NP ⇐ NP ⊄ BPP ⇐ OWF (PPT-secure) ⟺ K^t is mildly hard-on-average**

There are three arrows, all verified and all **uniform**:
- **A0.** Arora–Barak, Exercise 10.1; the proof, including the BPP form, is in the R2 pre-registration.
- **P ⊆ BPP.**
- **A4.** Liu–Pass 2020, Theorem 1.1.

MCSP is off the mainline. Its verified route to hardness needs OWF secure against SIZE(poly) (Santhanam ITCS'20, Theorem 22; Hirahara–Santhanam, Proposition 12), while Liu–Pass's OWF are PPT-secure (R1, finding F2).

## 2. The smallest attackable statement

*For some polynomial t(n) ≥ (1+ε)n, every PPT algorithm fails to compute K^t exactly on at least a 1/p(n) fraction of uniform n-bit strings.*

## 3. The density barrier

**Proposition.** Let t be a polynomial, S_k = {x ∈ {0,1}^n : K^t(x) ≤ k}, and k(n) ≤ n − ω(log n).
- **(a)** Pr_{x∼U_n}[x ∈ S_k] ≤ 2^{k+1−n}, which is negligible.
- **(b)** Let A and A′ be algorithms that agree on every x ∉ S_k. Then their probabilities of computing K^t correctly on U_n differ by at most 2^{k+1−n}. Hence any error set E ⊆ S_k, however it is exhibited, is compatible with A being a successful heuristic in the mild-hardness sense. In particular, (b) holds even if A errs on *all* of S_k.

*Proof.* (a) There are at most 2^{k+1} descriptions of length ≤ k. (b) The two correctness events differ only on S_k, so (a) bounds the difference. Since 2^{k+1−n} = n^{−ω(1)} < 1/p(n) for every polynomial p and all large n, errors confined to S_k never decide mild hardness. ∎

**Reading.** An argument whose contradiction comes from specific strings of low K^t — exhibiting them, sampling them, or conditioning on them — can refute at most a heuristic's correctness on S_k, and so it cannot refute mild average-case hardness. This informal reading is the proposition's content; "any argument" is not itself a formal claim. The shape is folklore: exhibiting an instance never proves average-case hardness. It is stated here for K^t, with RE's own candidates as its instances.

**Worked instances.** These are the three closed candidates.
1. **Self-generated sampler** ("run a random short program"). It fails test t1: constant mass on 0^n.
2. **Low-K^t conditioning (S_a).** It fails test t2 through padding, but **only for t ≥ C·n²**, because the padding program must count to n on a single tape. **At linear t the status is open**, and it is marked open, not refuted. Either way, by (b) it cannot bear on mild hardness.
3. **The Chaitin/Gödel diagonal.** It fails three ways:
   - *time:* the scan is exponential;
   - *coins:* randomness is not a description;
   - *density:* its output x_A lies in S_k, so by (b) it shows at most an error that a heuristic is allowed. It bears only on **worst-case** K^t computation.

**Separate from the mainline.** Removing the coin obstruction amounts to derandomization. Its verified characterization is Liu–Pass CCC'22, Theorem 1 (prBPP = prP iff worst-case hardness of GapMcKtP). **prBPP = prP does not give P ≠ NP, and the chain does not pass through it.**

## 4. What RE contributed

- It **selected** the endpoint in §2, the upper-layer object that meta-complexity already studies.
- It **closed its own native candidates** with proofs: the self-generated sampler, low-complexity conditioning, and the diagonal.
- **The lesson of §3.** If RE's recursion is to contribute, it must act on the **measure over typical strings**, not on any constructed object. In the reviewer's words, the fixed point is not a special string; it is that every efficient recognizer errs on random ones.

## 5. What would reopen the program

A candidate that acts at the level of the uniform measure on incompressible strings, which is to say, a new argument toward the existence of OWF.

**No verified partial route exists.** The nearest result, Hirahara's worst-to-average reduction (FOCS 2018, Theorem 1 and Corollary 2), lands at DistNP ⊄ AvgP. That is below OWF in the known ordering, and it uses the errorless model.

## 6. Calibration, verbatim from the R1 and R2 documents

From R1:

> Priors: mine R1b 65, the reviewer's R1b 60. The outcome matched, but my predicted *location* was partly wrong (finding F1).

> 1. **F1: the A3 prediction was partly wrong.** I pre-registered a PRF-vs-uniform distribution mismatch at A3. Instead, zero-error average-case hardness over the **uniform** distribution is exactly what natural properties give (Step 1). The variant changes are the threshold and non-uniformity.

From R2:

> ## Calibration
>
> - **The reviewer:** Flag 2's "immediate" was scored as the reviewer's sixth wrong outcome prior, and F3 of R1 as the sixth premise miss (per the ruling). Both are recorded here and not in the RE appendix, since the R-program stays outside the RE record.
> - **Me:** Flag 1 was overclaimed (see S_a above).
