# R1: the reduction chain, pre-registration

*Drafted 2026-09-10 on branch `r1-chain`, for the reviewer's ruling before any work. The author's go was given for "T1"; the reviewer's user then withdrew T1–T3 and replaced them with R1–R3, which are the same kind of work (a literature document, ruled before it runs). The draft treats the go as covering the replacement and says so here. This is a document, not Lean, and it contains no RE content.*

## Target

The chain, as proposed:

> P ≠ NP ⇐ MCSP ∉ P ⇐ MCSP average-hard (uniform) ⇐ OWF exist ⟺ K^t mildly average-hard (Liu–Pass 2020)

Every arrow must be stated in full:

- the problem variant, with its threshold or time bound as a function of input length;
- the distribution, and the error fraction;
- the adversary class: deterministic, BPP, or non-uniform;
- the direction of the implication;
- a citation with the exact theorem number, **checked against the paper's text**;
- a status: unconditional, conditional (on what), or requiring a change of variant.

The deliverable is that table, plus a record of the derandomization obstruction at the bottom of the chain.

## The arrows, and what each must pin down

**A1. MCSP ∉ P ⇒ P ≠ NP.** Expected to be immediate. MCSP[s] is in NP for every polynomial-time computable threshold s(N), where N = 2^n is the truth-table length: guess a circuit of size ≤ s and evaluate it on all 2^n inputs, which is polynomial in N. To fix: the threshold, and the fact that the input length is N, not n.

**A2. MCSP average-hard ⇒ MCSP ∉ P.** Expected to be trivial for any average-case notion that implies worst-case hardness. To fix: which average-case notion, so that A3's output literally matches A2's input.

**A3. OWF ⇒ MCSP average-hard.** Expected route: one-way functions give pseudorandom generators (Håstad–Impagliazzo–Levin–Luby), which give pseudorandom functions (Goldreich–Goldwasser–Micali). A pseudorandom function's truth tables have small circuits, so an MCSP algorithm would tell them from random truth tables (Razborov–Rudich; Kabanets–Cai 2000). **Expected finding:** the hardness obtained this way is for telling the pseudorandom-function mixture from uniform, against BPP, or against P/poly when the functions are secure non-uniformly. It is not average-case hardness over the uniform distribution on truth tables. If the chain needs "uniform" at this link, that is a change of variant and gets flagged. A source to check for a uniform-distribution version: Hirahara–Santhanam, CCC 2017.

**A4. OWF ⟺ K^t mildly average-hard.** Source: Liu–Pass, FOCS 2020. To extract exactly:
- the range of t (polynomial, and at least (1 + ε)·n);
- the error fraction (1/p(n));
- the distribution (uniform);
- which task: computing K^t, deciding a threshold, or approximating it.

**A5. The junction.** The chain as written switches from MCSP (circuit size) to K^t (time-bounded program length) between A3 and A4. A4 concerns one-way functions, so the chain actually runs through OWF, and K^t enters only as an equivalent form of its bottom. The check is whether the statements on the MCSP side and the K^t side can be substituted for each other. MCSP and MK^tP are related but distinct problems. **Expected:** they cannot be swapped without further results, so K^t describes the bottom of the chain but is not a link in it.

## The obstruction to record at the bottom

Chaitin's diagonal, moved into the time-bounded setting, goes like this. Take a recognizer for "K^t(x) ≥ n − c", search for the first string it accepts, and output that string; this gives a short description of an incompressible string, which is a contradiction. It fails here for two reasons:

- the search takes exponential time, so it bounds no K^t with t polynomial;
- with a randomized recognizer, the output isn't one fixed string, and a description would have to include the random bits.

Probabilistic time-bounded complexity pK^t (Goldberg–Kabanets–Lu–Oliveira, CCC 2022) is the measure built to tolerate the second failure. The results linking derandomization to hardness of (p)K^t are to be located and stated exactly: Liu–Pass 2022–23, and the Chen–Tell line. **All of the citations in this section are UNVERIFIED until guard g1 is run.**

## Outcomes

| Code | Outcome |
|---|---|
| **R1a** | The chain holds end to end on known results. |
| **R1b** | An arrow needs a change of variant; list them. |
| **R1c** | An arrow is not known. The chain is then a chain of conjectures, and the weak link is named. |

**Priors (mine):** R1b 65, R1a 25, R1c 10. The likeliest findings are the distribution mismatch at A3 and the junction at A5.

## Guards

- **g1:** every theorem number and statement is checked against the paper's text (arXiv or ECCC), never taken from memory. A citation that isn't checked is marked UNVERIFIED and does not count toward the outcome.
- **g2:** each arrow's output statement must literally match the next arrow's input: variant, threshold, distribution, error and adversary. Any mismatch is a finding.
- **g3:** no RE content in R1.
- **g4:** each arrow is written as an implication together with its adversary class.

## An early flag for R2, not a ruling

As stated, S looks trivially false, which would be outcome S3. A uniformly random program of length ≤ n/2 begins, with probability at least 2^(−c) for some constant c that depends on the machine, with a fixed short prefix that prints 0^n and ignores the rest. So D_t puts constant mass on 0^n, and the test "is the input all zeros?" distinguishes D_t from U_n with constant advantage. Any repair has to change the sampler, for example by conditioning on the output's K^t being close to n/2, or by using a universal distribution conditioned on length. That repair is where the question of the fixed-point distribution actually lives.

## Ceiling

Nothing here proves P ≠ NP unless R3 succeeds, and R3 is the open problem in its strongest known form. What R1 and R2 buy is a precise, structured, single target in place of "P vs NP".
