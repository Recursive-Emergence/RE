# R2: the smallest statement, report

*Run 2026-09-10 on branch `r2-smallest`, against the pre-registration (accepted, with candidate S₃ added by the ruling). Every citation was checked against the paper's text (PDFs converted locally, line-level). Proofs are given in full or marked as missing. RE language appears only in the one sentence on what RE contributed.*

## Outcome: **S1**

The smallest verified sufficient condition for P ≠ NP that this program reaches is the Liu–Pass endpoint:

> **for some polynomial t(n) ≥ (1+ε)n, every PPT algorithm fails to compute K^t exactly on at least a 1/p(n) fraction of uniform n-bit strings.**

No candidate adds structure to it. The chain behind it is A0 plus Liu–Pass Theorem 1.1: K^t mildly hard ⟺ OWF ⇒ NP ⊄ BPP ⇒ P ≠ NP.

**What RE contributed:** it selected this endpoint, and it closed its own two native candidates, the self-generated sampler and the diagonal instance, with proofs rather than dropping them.

**No R3:** by the ruling, R3 is drafted only if S2 appears, and it did not.

## The central finding: a density obstruction

*Claim.* Let S_k = {x ∈ {0,1}^n : K^t(x) ≤ k}. Then Pr_{x∼U_n}[x ∈ S_k] ≤ 2^{k+1−n}.

*Proof.* There are at most 2^{k+1} descriptions of length ≤ k. ∎

A mildly hard-on-average statement allows every PPT algorithm an error budget of 1/p(n). For k ≤ n − ω(log n), that budget covers all of S_k. So **no argument that works by exhibiting, sampling, or conditioning on compressible strings can bear on mild average-case hardness under U_n.** Compressible strings are invisible to the measure the endpoint is stated in.

All three RE-native moves produce compressible objects by construction, and they fail for this one reason:
- a sampler that runs short programs;
- conditioning on low K^t;
- the diagonal string x_A.

This is Flag 2 of the pre-registration, generalized.

## Candidate by candidate

### S_a: uniform on {K^t ≤ n/2}, indistinguishable from U_n → **S3**, but only for large t

**The pre-run assumption, checked.** Liu–Pass define K^t(x) = min{|Π| : U(Π, 1^{t(|x|)}) = x}, where Π encodes a single-tape machine M and its input w, and t counts M's steps (verified, §2.2). Their Fact 2.1, K^t(x) ≤ |x| + c for every t, holds because the trivial program halts at once.

The padding program, "y, then zeros up to length n", must count to n. On a single tape the construction I have does this in O(n²) steps: walk back to a binary counter, decrement it, walk to the end.

**Correction to my Flag 1.** It holds for **t(n) ≥ C·n²**: the padding test then has advantage ≥ n^{−c}/4, as proved in the pre-registration, so S_a is false for such t. For t between (1+ε)n and C·n² I have no padding construction, and I claim no lower bound. **S_a at linear t is therefore not refuted by t2; its status there is open.** It is not rescued either: Flag 2, and the density obstruction above, still block any route from it to mild hardness. My pre-registration overstated Flag 1 ("every candidate of its form", for t ≥ (1+ε)n). That is recorded as my miss.

### S₁: the Liu–Pass endpoint → **mainline; no added structure found** (see below)

### S₂: conditioning on high entropy (condEP-PRG output) → **collapses onto S₁**

- Liu–Pass Theorem 5.2 (verified): if for every γ > 1 there is a rate-1 efficient μ-condEP-PRG G : {0,1}^n → {0,1}^{n+γ log n} with μ = 1/n², then for all d, ε > 0 and every polynomial t ≥ (1+ε)n, K^t is mildly hard-on-average to (d log n)-approximate.
- Theorem 5.6 (verified): if OWF exist, then such condEP-PRGs exist for every γ > 1.
- With Theorem 1.1, S₂ lies inside the OWF ⟺ mild-hardness equivalence class.
- The entropy condition in Definition 5.1, H(G(U_n | E_n)) ≥ n − α log n, is exactly the density obstruction handled correctly: high entropy keeps the distribution's mass off every negligible set.

### S₃: the diagonal instance → **S3, with the obstructions named**

*Setup.* A is a PPT algorithm claimed to compute K^t on ≥ 1 − 1/p of uniform strings. Fix its coins r. Let x_{A,r} be the lexicographically first n-bit string that A labels "K^t > n/2". The Chaitin/Gödel move is to argue that x_{A,r} has a short description (A, r, n, "the first one"), so K^t(x_{A,r}) is small, contradicting A's label.

**Where it fails.**
1. **Time.**
   - For t ≥ C·n², every string 0^{n−m}·y with m ≤ n/2 − c·log n has K^t ≤ n/2, by the padding construction with zeros prepended.
   - If A is correct on these, the scan must pass about 2^{n/2 − c·log n} of them, which is exponential.
   - The description then bounds K^T(x_{A,r}) only for T = 2^{Ω(n)}, not for any polynomial t.
2. **Randomness is not code.**
   - The coins r have poly(n) length, so the description is short only if A is derandomized.
   - Replacing the scan with random sampling outputs a random high-labelled string, not a fixed one.
   - Under shared randomness (pK^t, Goldberg–Kabanets–Lu–Oliveira Definition 17, verified in R1), the output still varies with the randomness, so no fixed x is output with the required probability δ.
3. **Density (mine).**
   - Even if both failures were repaired, the diagonal only ever produces *compressible* strings. By the central claim these have density ≤ 2^{n/2+1−n} under U_n, inside A's error budget.
   - So the contradiction, where it exists, shows only that A errs on a compressible string, which a heuristic is allowed to do.
   - The diagonal refutes **worst-case** computation of K^t (classic uncomputability, and its time-bounded analogues). It cannot refute mild average-case hardness, and it cannot establish it.

**The loop, kept separate from the mainline.** Obstruction 2 is removed exactly by derandomization. The verified characterization of derandomization is Liu–Pass CCC'22, Theorem 1: prBPP = prP iff GapMcKtP[O(log n), n−1] is hard for BPTIME(n^c) on all sufficiently long auxiliary inputs z. It concerns conditional Levin Kt, worst-case, and promise problems. That is an equivalence between derandomization and a hardness statement. **prBPP = prP does not give P ≠ NP, and the mainline does not pass through it.** Obstruction 3 would survive it in any case.

### The surviving question: does self-reference buy a reduction beyond S₁?

The nearest known result is Hirahara, FOCS 2018 (ECCC TR18-138, verified).
- **Theorem 1 (Main).** For r with n − c√(n log n) ≤ r(n) < n: if (MINKT[r], D_u) ∈ Avg_{1/6m}P (an *errorless* heuristic), then a zero-error randomized polynomial-time algorithm outputs, on (x, 1^t), a program of size ≤ σ(|x|, K^t(x)) that outputs x within τ(|x|, t) steps. Here σ(n, s) = s + O((log n)√s + (log n)²), and τ is a polynomial.
- **Corollary 2.** DistNP ⊆ AvgP ⇒ (MINKT[r], D_u) ∈ Avg P ⇒ search-Gap_{σ,τ}MINKT in zero-error randomized polynomial time ⇒ Gap_{σ,τ}MINKT ∈ Promise-ZPP. The last step reverses if Promise-ZPP = Promise-P.
- **What it gives.** Contrapositively, worst-case hardness of Gap_{σ,τ}MINKT against Promise-ZPP implies DistNP ⊄ AvgP. That is a genuine non-black-box worst-to-average step for time-bounded Kolmogorov complexity.
- **What it does not give, relative to S₁.**
  - Its conclusion, DistNP ⊄ AvgP (excluding Heuristica), lies *below* OWF in the known ordering "∃ OWF ⇒ DistNP ⊄ AvgP ⇒ P ≠ NP", as Hirahara's own §1 states (verified, l.63).
  - Its average-case notion is errorless, whereas Liu–Pass mild hardness has two-sided error 1/p.
  - So it neither implies nor is implied by S₁ through any verified route. It does not add structure to S₁.
- **Verdict.** Nothing beyond what is known was found. By the ruling, R2's outcome is **S1**.

## Calibration

- **The reviewer:** Flag 2's "immediate" was scored as the reviewer's sixth wrong outcome prior, and F3 of R1 as the sixth premise miss (per the ruling). Both are recorded here and not in the RE appendix, since the R-program stays outside the RE record.
- **Me:** Flag 1 was overclaimed (see S_a above).

## Sources checked in R2 (beyond R1's ledger)

| Claim | Source | Where checked | Status |
|---|---|---|---|
| "if P = NP then OWF and PRGs do not exist" | Arora–Barak (draft), Exercise 10.1 | text l.10733 | verified (proof given in the pre-registration) |
| K^t definition; single-tape machine; t counts M's steps; Fact 2.1 | Liu–Pass 2020, §2.2 | l.420–440 | verified |
| condEP-PRG ⇒ mild hardness (approximation) | Liu–Pass 2020, Definition 5.1, Theorem 5.2 | l.590–605 | verified |
| OWF ⇒ condEP-PRG | Liu–Pass 2020, Theorem 5.6 | l.952 | verified |
| MINKT worst-to-average; the σ gap; Corollary 2 chain | Hirahara 2018, Theorem 1, Corollary 2 | l.217–250 | verified |
| ∃OWF ⇒ DistNP ⊄ AvgP ⇒ P ≠ NP (the order of the worlds) | Hirahara 2018, §1 | l.61–64 | verified |

Links:
- Hirahara, ECCC TR18-138: <https://eccc.weizmann.ac.il/report/2018/138/>
- Arora–Barak draft: <https://theory.cs.princeton.edu/complexity/book.pdf>
- Liu–Pass 2020: <https://arxiv.org/abs/2009.11514>
