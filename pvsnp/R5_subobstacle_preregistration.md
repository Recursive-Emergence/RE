# R5: the first sub-obstacle inside the door, pre-registration

*Drafted 2026-09-10 on branch `r5-subobstacle`, on the author's go (draft, run, close out, push), for the reviewer's ruling before any work. It is a document only; guards g1, g5, g7 and g8 apply.*

## Target

Take Hirahara (FOCS 2018), the technique closest to the door sentence of R4. Write its argument as numbered steps, each with the hypothesis it uses. Then, **separately for two changes**, find the first step whose hypothesis is no longer available:
- **(A) Two-sided error.** The heuristic may err on a 1/p fraction, as in Liu–Pass mild hardness, instead of being errorless.
- **(B) An NP-hard source.** The problem is McK^tP[ζ] at t = n² (Liu–Pass CCC'22, Theorem 1.2), instead of GapMINKT.

For each first failure, the run determines whether a **verified** result repairs it.

## The argument, as steps

This draft is read off the verified text of Hirahara 2018, l.380–404 and Theorem 1 (l.217). **The run must re-check each step and hypothesis against the full proof, not only the overview.**

| Step | Claim | Hypothesis used |
|---|---|---|
| **S1** | MINKT[r] has few Yes instances under D_u: at most 2^r strings have K^t < r | counting (the density fact); r ≤ n − c√(n log n) makes the fraction small |
| **S2** | An errorless heuristic A for (MINKT[r], D_u) outputs "No" on a dense set of random strings | A is **errorless** (never wrong, may answer "?") plus the success bound Avg_{1/6m} |
| **S3** | T := {x : A answers "No"} is a dense set in P that contains **no** string of K^t < r, so T is a statistical test that every hitting-set generator with short seeds fails, in particular NW_{Enc(x)} | **errorlessness**, which makes T ⊆ {K^t ≥ r}; generator outputs have small K^t |
| **S4** | NW reconstruction plus list decoding turns the test T into a short description of x relative to T | the NW security proof (Nisan–Wigderson) and list-decodable codes (Theorem 22 in the paper) |
| **S5** | Splicing in A's source code gives a program of size ≤ σ(\|x\|, K^t(x)) producing x within τ steps. The result is a worst-case *search* algorithm for the gap problem Gap_{σ,τ}MINKT, with additive gap O((log n)√s + (log n)²) | **non-black-box** use of A's code; the conclusion is an **approximation** |

## Expected first failures (priors attached)

**(A) Two-sided error: S3 fails first. Confidence 80.**
- With a 1/p error budget, A may answer "No" on compressible strings, including the entire image of NW_{Enc(x)}. That image has density 2^{−Ω(n)}, well inside the error budget.
- So T is no longer guaranteed to reject generator outputs, and the argument loses its distinguisher.
- This is exactly **Flag 2 of R2, the density barrier**: errors can concentrate on the negligible compressible set. It is the observation that density cuts both ways, which the reviewer wants as the central finding. The fact that makes errorless heuristics usable, few Yes instances, is the same fact that lets two-sided heuristics hide their errors.
- *Repair candidates to check:* results passing from two-sided-error to errorless average-case easiness for NP, or for meta-complexity problems in particular (a search to be recorded under g8); Hirahara STOC'23's distributional-K framework; and any two-sided-error discussion in Liu–Pass CCC'22.

**(B) An NP-hard source: the conclusion fails first, at S5, unless an earlier step does. Confidence 55.**
- Hirahara's output is an **additive-gap approximation** of K^t. The NP-completeness of McK^tP[ζ] (Liu–Pass CCC'22, Theorem 1.2) may be for the **exact** threshold problem.
- If it is exact only, an approximation algorithm does not contradict it, and the gap version's NP-hardness is not known. Hirahara STOC'23 takes NP-hardness of *approximating* distributional K^t as a *hypothesis* of its OWF characterization. That is to be verified.
- **Alternative first failure, at S1 or S2:** a mismatch of distribution or of problem shape. Hirahara uses D_u (x, 1^t); Liu–Pass use the uniform distribution on (x, z, k) with the conditional K^t(x | z). Does the argument carry over to conditional complexity with an auxiliary z? To be checked.

## Also run: is (1d) new?

R4's isolated-input fact says that random-graph local functions at m = c·n have 2^{Ω(n)} preimages. Before calling it new to the record, the run checks whether Applebaum's survey or Cook–Etesami–Miller–Trevisan (full text) already state it, or an equivalent. It is labelled "new" only if neither does, and otherwise cited.

## Outcomes

| Code | Outcome |
|---|---|
| **E1** | The first failing step is identified for both changes, and no verified repair exists. The program ends with the exact sub-obstacle named. |
| **E2** | A verified repair exists for one change but not the other. Record which, and shrink the sentence accordingly. |
| **E3** | Both are repaired in the literature. Re-verify with suspicion; that would itself be the finding. |

**Priors.** Mine: E1 70 / E2 25 / E3 5. The reviewer's: E1 65 / E2 30 / E3 5.

## Then: the final one-page state

On the reviewer's instruction, the program then closes with one page:
- the door sentence;
- the sub-obstacle;
- the two-sided density observation;
- the one proved fact, labelled after the novelty check;
- calibration, both sides.
