# R2: the smallest statement, pre-registration

*Drafted 2026-09-10 on branch `r2-smallest`, on the author's go, for the reviewer's ruling before any work. It is a document with no Lean. RE language appears in one sentence only: the one about what RE contributed.*

## The frame, after R1 (reviewer's ruling)

The target is P ≠ NP, not MCSP hardness. The mainline is **uniform**:

**A0. OWF (PPT-secure) ⇒ NP ⊄ BPP ⇒ P ≠ NP.**
- *Verified statement:* Arora–Barak, *Computational Complexity* (draft), Chapter 10, Exercise 10.1: "Show that if P = NP then one-way functions and pseudorandom generators do not exist." It is stated as an exercise, so the proof is given here.
- *Proof (P form).* If P = NP, let f be computable in polynomial time. The language {(y, w) : ∃x extending w with f(x) = y} is in NP, hence in P. Extend w one bit at a time to find a preimage of any y in the image of f. This inverts f everywhere, so f is not one-way.
- *Proof (BPP form).* Suppose NP ⊆ BPP. The same search, with each decision amplified to error 2^{−2n} and a union bound over the n steps, inverts f with probability ≥ 1 − 2^{−n} by a PPT algorithm. This contradicts security against PPT (Liu–Pass Definition 2.1, verified in R1).
- NP ⊄ BPP ⇒ P ≠ NP because P ⊆ BPP.

**A4. OWF ⟺ K^t mildly hard-on-average** (Liu–Pass 2020, Theorem 1.1, verified in R1).

**The smallest verified sufficient condition, in one sentence:** *for some polynomial t(n) ≥ (1+ε)n, every PPT algorithm fails to compute K^t exactly on at least a 1/p(n) fraction of uniform n-bit strings.*

MCSP and the non-uniform branch are kept only as a side note. R1's gap F2 lies on a route the mainline no longer uses.

## Findings made while drafting, before any run (flags, not rulings)

**Flag 1: the proposed candidate S_a fails test t2, and so does every candidate of its form.**

S_a is: *no PPT distinguishes U_n from the uniform distribution on {x ∈ {0,1}^n : K^t(x) ≤ n/2} with 1/poly advantage.*

*Claim.* For every threshold k with c·log n ≤ k ≤ n − 2, the uniform distribution on S_k = {x : K^t(x) ≤ k} is distinguishable from U_n with advantage ≥ n^{−c}/4. Here c is a constant that depends on the machine.

*Proof.*
- **Padded strings are cheap.** For |y| = k − c·log n, the program "print y, then zeros up to length n" has length ≤ |y| + c·log n = k. The c·log n pays for a self-delimiting y and for n. The program runs within t(n) ≥ (1+ε)n steps for large n. That assumption is the role the bound t ≥ (1+ε)n plays in Liu–Pass (the program that prints n bits must run within t); it is **to be checked in the run**.
- **Count.** So S_k contains all 2^{k − c log n} strings y·0^{n−|y|}. There are at most 2^{k+1} programs of length ≤ k, so |S_k| ≤ 2^{k+1}.
- **Test.** "Are the last n − k + c·log n bits all zero?" accepts a uniform element of S_k with probability ≥ 1/(2n^c), and U_n with probability 2^{−(n−k)} · n^{−c} ≤ n^{−c}/4.
- **Advantage.** At least n^{−c}/4. ∎

Every low-K^t set is dominated by structurally simple members, in exactly the way the universal distribution is dominated by simple strings. Conditioning on low complexity does not escape the "print 0^n" failure; it moves it into the padding.

**Flag 2: "S_a ⇒ mild hardness" is not immediate.**
- A heuristic allowed a 1/p(n) error on uniform strings can put *all* its errors on S_k, whose density is ≤ 2^{k+1−n}.
- That is why Liu–Pass derive K^t hardness from a *conditionally entropy-preserving* PRG. Their Definition 5.1 (verified) requires H(G(U_n | E_n)) ≥ n − α·log n, and Theorem 5.2 (verified) gives mild average-case hardness, even to approximate, from such a generator. A distribution with only ~k bits of entropy can't carry that argument.
- This corrects the ruling's "a distinguisher from a K^t computer is immediate". It was a claim about an argument, so I don't count it as a premise miss; the reviewer decides whether to count it as an outcome prior, as at (xiii).

**Flag 3: the tension between samplability and heaviness.**
- The self-referential sampler, "run a uniformly random short program for t steps", is efficient but fails t1: constant mass on 0^n.
- The uniform distribution on S_k passes t1 (each string has mass ≤ 2^{−k+c log n}), but it fails t2 by Flag 1 and is not known to be efficiently samplable. Sampling it seems to need K^t itself.
- The only object in reach that passes both tests is **U_n** itself, which is the Liu–Pass endpoint.

## Candidates for R2, after the flags

**S₁ (the endpoint):** K^t mildly hard-on-average on U_n (Liu–Pass Theorem 1.1, and Theorem 1.2 for approximation). Expected outcome: (S1).

**S₂ (conditioning on high entropy instead of low complexity):** the output distribution of a conditionally entropy-preserving PRG. By Liu–Pass Theorem 5.2 together with their theorem that OWF imply condEP-PRGs (Theorem 5.6), this is equivalent to OWF. It too collapses onto (S1), and the run must confirm Theorem 5.6's exact statement.

**The surviving question, asked of S₁:** does self-reference buy a reduction? The set S_k has a canonical exponential-time enumerator that is itself a short program. Does that give downward self-reducibility, hardness amplification, or a worst-case-to-average-case step?
- The nearest known result is Hirahara (FOCS 2018), *Non-black-box worst-case to average-case reductions within NP*. The run must state exactly what it proves:
  - which problem (a GapMINKT-type promise problem, **to verify**);
  - which gap parameters;
  - which direction;
  - and what it does *not* give. In particular, whether it reaches the mild average-case hardness of Liu–Pass or stops short, and why.

## Outcomes

| Code | Outcome |
|---|---|
| **S1** | The smallest statement is the Liu–Pass endpoint and there is no extra structure. The shrink ends there, and RE's contribution is the choice of endpoint, nothing more. |
| **S2** | A candidate carries a reduction the endpoint lacks. R3 attacks it. |
| **S3** | A new candidate fails t1 or t2. Replace it and report the failure mode. S_a is already S3, by Flag 1. |

**Priors (mine):** S1 75 / S3 20 / S2 5. S3 is for any further candidate proposed in the ruling.

## Guards

- **g1:** as in R1. No citation from memory, and an UNVERIFIED citation counts as none.
- **g5:** tests t1 and t2 are applied to every candidate, with a proof or a counterexample, not an estimate.
- **g6:** every claimed implication between candidates is proved in the document or cited with a verified theorem number.
- **g7:** RE language is confined to the one sentence above.

## Ceiling

As in R1. Nothing here proves P ≠ NP. If (S1) holds, the program's honest yield is a verified single-sentence target and the knowledge that RE's move adds no structure to it. That is worth having, and it must not be dressed up as more.
