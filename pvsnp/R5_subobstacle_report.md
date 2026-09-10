# R5: the first sub-obstacle inside the door, report

*Run 2026-09-10 on branch `r5-subobstacle`, against the pre-registration (accepted, with the reviewer's addition to (A)). g1 applies: "verified" means checked against the paper's text. Derivations of my own are marked as such. The report is in part / expected / observed form.*

## Outcome: **E1**

Both first failures are identified, and **no verified repair exists for either**. Priors: mine E1 70; the reviewer's E1 70.

## The argument, as steps (re-checked against Theorem 26 and Corollary 27, l.800–840)

| Step | Claim | Hypothesis used |
|---|---|---|
| S1 | Few strings are compressible | counting |
| S2 | An errorless heuristic for (MINKT[r], D_u) answers "No" on a δ-dense set T | errorlessness, and D_u |
| S3 | T ⊆ R_r[t₁], the r-random strings, so T rejects every output of NW^{Enc(x)}_{m,d} | errorlessness, and Theorem 26's promise **K^t(x) + d + O(log(nmd/δ)) < r(m)** |
| S4 | T distinguishes NW from uniform with advantage ≥ δ, so the reconstruction outputs a certificate of length ≈ exp(ℓ²/d)·m + d + O(log) | NW security proof, list decoding |
| S5 | With m ≈ K^t(x) + d and d = ℓ·√(K^t(x)), the certificate has length K^t(x) + O(ℓ√(K^t(x))) + ℓ², giving the gap σ; the heuristic's code is spliced in | non-black-box use of the code |

## (A) Two-sided error: the tension between S3 and S4

*Expected:* S3 fails first (80). *Observed:* yes. As the reviewer asked, it is stated as a tension between two steps, and it is sharper than one about seed length.

**Proof** (mine, from the verified promise of Theorem 26):
- S3 needs T to reject the image of NW. With an errorless heuristic this is automatic, because the image is compressible and T contains only random strings.
- Theorem 26's promise requires exactly that compressibility: K^t(x) + d + O(log) < r(m) ≤ m, so m − d > K^t(x).
- The image has at most 2^d points in {0,1}^m, so its density is at most 2^{d−m} < 2^{−K^t(x)}.
- A heuristic with two-sided error 1/p may answer "No" on the whole image once 2^{−K^t(x)} ≤ 1/p. Then T no longer distinguishes.
- **So the argument survives two-sided error only for instances with K^t(x) ≤ log p + O(1) = O(log n).** ∎

**The reviewer's proposed repair (a dense generator image) is excluded by the same counting.** Any set that the errorless guarantee forces T to reject must be compressible, and a set of compressible strings has negligible density. The tension is between *compressibility* (needed for S3's guarantee and for S4's short certificate) and *density* (needed for S3 under two-sided error). Seed length is only one expression of it. Hirahara names a related tension himself (verified, l.423–426): short seeds are needed for exhaustive search, long seeds for short descriptions.

**Repairs checked:**
- **Liu–Pass CCC'22, footnote 2** (verified, l.160–163) states the gap directly: *"we need a worst-case to 2-sided error average-case reduction. Hirahara's elegant work [25] makes partial progress on this question by presenting a worst-case (approximate) to errorless average-case reduction; errorless average-case hardness does not suffice"*.
- **Hirahara–Santhanam, ITCS 2022, Theorem 14** (verified): for every NP-complete L, the following are equivalent:
  - for every D ∈ PSamp/poly, a non-adaptive AvgBPP/poly *instance checker* for (L, D) exists;
  - for every such D, an errorless-to-error-prone non-adaptive reduction exists.

  They call instance checkers for NP-complete problems "a long-standing open question". Unconditionally they obtain the equivalence only for P against NC¹ and for UP ∩ coUP against P (abstract, verified).
- **So a repair for (A) needs a non-adaptive average-case instance checker for NP**, at least on the non-adaptive route. Theorem 14 speaks to non-adaptive reductions only; a non-black-box route is not excluded by it.

## (B) An NP-hard source: first failure at S2, the auxiliary input

*Expected:* the conclusion at S5, because of an exact threshold against an additive gap (confidence 55). *Observed:* **that prediction was wrong.**

**Why it was wrong** (verified, Liu–Pass Propositions 3.3 and 3.4):
- A set cover of size ℓ gives K^t(A | z) ≤ λℓ + O(log n); the proof of Proposition 3.3 says it "can be represented using λℓ + O(log n) ≤ 2λℓ bits".
- Conversely, K^t(A | z) ≤ 2λℓ forces cover ≤ 4ℓ.
- So McK^tP[ζ] is NP-hard under many-one randomized reductions (Theorem 3.1) **already for a factor-≈2 gap**. Hirahara's additive O(ℓ√s) approximation would resolve such a gap.

**The actual first failure (my inference from verified facts):**
- The reduction's auxiliary input z is *structured*: gadget blocks W_i placed at key positions, and "otherwise, let z_p = 0^{n×m}" (verified, §3.1 and Figure 3).
- Mild average-case hardness in Liu–Pass is over the *uniform* distribution on instances (Theorem 1.1).
- A heuristic that is good on average over uniform z gives no dense test T for the reduction's z. So the dense-test construction fails at **S2**, for the instances that NP-hardness produces.

**The repair object:** Hirahara STOC'23 (ECCC TR23-037, abstract verified) works with *distributional* Kolmogorov complexity, where the auxiliary input comes from a distribution. Its characterization takes "NP-hard to approximate the distributional Kolmogorov complexity under randomized polynomial-time reductions" as a *condition* equivalent (together with worst-case hardness of NP) to OWF. **That condition is where Hirahara's programme currently rests.** No verified result supplies it.

## Novelty check on R4's isolated-input fact: **known**

Applebaum's survey §5.1 (verified, l.1203–1217): a random local function at m = (1−ε)n "is likely to have some input i of degree 0, … with no influence at all. Hence, we can find a collision with a target string x simply by flipping the values of x_i". The e^{−cd} count appears at l.464. R4's version (m = c·n, 2^{Ω(n)} preimages w.h.p., by McDiarmid) is a routine quantitative restatement. **It is labelled known, not new.** (The Cook–Etesami–Miller–Trevisan text was also searched; it has no such statement.)

## Calibration

- **Me:** (A) was right. (B)'s predicted location was wrong: the hardness already has a constant-factor gap.
- **The reviewer:** the dense-image repair it proposed is excluded by counting, which refines the tension; that is a note, not a miss. The novelty check it asked for found the fact already known, which was its instinct.

## Sources checked in R5

- Hirahara 2018: Theorem 26 and Corollary 27 (l.800–840), l.416–430.
- Liu–Pass CCC'22: footnote 2 (l.160–163), Theorems 3.1–3.2, Propositions 3.3–3.4, §3.1 and Figure 3.
- Hirahara–Santhanam ITCS'22: abstract and Theorem 14. <https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.84/LIPIcs.ITCS.2022.84.pdf>
- Applebaum's survey: §5.1 (l.1203–1217) and l.464.
