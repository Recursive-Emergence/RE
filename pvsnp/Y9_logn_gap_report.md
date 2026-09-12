# Y9: the O(log n)-gap regime. Report

*Run 2026-09-11 on branch `y9-logn-gap`, on the author's go ("Run Y9, push after merge"; the reviewer separately confirmed its own user's go), against the pre-registration (dee231e) and the reviewer's ruling (75a980a).*
- *Priors, both sides: Y9c 45 / Y9b 40 / Y9a 15.*
- *Ruling (1): make Flag Z9 a proved statement about the specific generator; if K^t(G_n(z)) can be small for some z, the fifth instance is not established and the report says so.*
- *Ruling (2): name the class the NO-side guarantee loses under a polynomial-time generator.*

*Documents only; `formal/` closed. Sources: Hirahara STOC'20 (ECCC TR20-050) l.135–160 and Theorem 3.2; SS22 l.236–255. Both verified verbatim in the pre-registration and re-read here.*

## 0. Outcome

**Y9b: the regime closes, and the named step is a missing upper bound on K^t — not depth. Flag Z9 is refuted by a counting argument, so the fifth instance of "hiding is depth" is NOT established.** This is my second self-correction in three phases, and it goes the same way as Y8's: a reading I carried into a prior turns out to be false when the arithmetic is actually done.

1. **Ruling (1), done, and it refutes my own flag (§1).** For all but a 2^{−k+1} fraction of seeds, **depth(G_n(z)) ≤ a·log n + k + O(1) = O(log n)**. The outputs are **shallow**, and for a large enough constant β they lie **inside** LP23's promise Q^t_β. **The depth conjecture gains no fifth instance here.**
2. **The regime nevertheless closes (§2).** The technique needs K^t(G_n(z)) ≤ s(n) + O(log n), which requires *running* the generator inside the time bound. The generator is EXP^NP-computable, so the bound holds only for exponential t. For polynomial t no upper bound is available, and counting is consistent with K^t(G_n(z)) = n + O(1) — in which case R_{K^t} is not a distinguisher for G at all. **The named step is the missing upper bound.**
3. **Ruling (2), the class (§3).** What a polynomial-time generator loses is not "the hitting-set property against a circuit class" but the **hardness class underwriting security**: Theorem 3.2's content is *"EXP^NP ⊆ BPP^D for any distinguisher D for G"*. A polynomial-time-computable generator cannot underwrite an EXP^NP conclusion by the same black-box route, and — decisively for us — **neither version yields a conclusion about NP**, which is what the target needs.
4. **Flag R9 was not triggered (§4):** nothing adapted, so no relativization check was owed.

## 1. Ruling (1): Flag Z9, proved and refuted

**Setting (verified).** G = {G_n : {0,1}^{s(n)} → {0,1}^n} with s(n) = n − a·log n for a constant a > 0, EXP^NP-computable (Hirahara STOC'20, Theorem 3.2). Their bound (l.146–150, quoted in the pre-registration): **K(G_n(z)) ≤ s(n) + O(log n)**.

**Lemma Y9.1 (ours; counting).** Fix any k ≥ 1 and any time bound t. Over a uniformly random seed z ∈ {0,1}^{s(n)},

  Pr_z[ K(G_n(z)) ≤ s(n) − k ] ≤ 2^{−k+1}.

*Proof.* The number of strings y with K(y) ≤ m is at most 2^{m+1} − 1, since each program of length ≤ m outputs at most one string. The range of G_n has at most 2^{s(n)} elements, and every seed maps into it. So the number of seeds whose image has K ≤ s(n) − k is at most 2^{s(n)−k+1}, a 2^{−k+1} fraction of all 2^{s(n)} seeds. ∎

**Proposition Y9.2 (ours; the refutation of Flag Z9).** For all but a 2^{−k+1} fraction of seeds,

  depth^t(G_n(z)) = K^t(G_n(z)) − K(G_n(z)) ≤ (n + O(1)) − (s(n) − k) = **a·log n + k + O(1)**.

*Proof.* K^t(y) ≤ |y| + O(1) for every y and every t (the program that carries y verbatim). Combine with Lemma Y9.1. ∎

**Consequences, stated plainly.**
- **The generator's outputs are shallow, by O(log n).** Depth cannot be large here **because the seed is long**: the range is too big for its elements to be K-compressible, and K^t is capped at n + O(1). The two bounds squeeze the gap to O(log n).
- **They therefore satisfy LP23's promise** Q^t_β = {x : K^t(x) − K(x) ≤ β·log K(x)} for any constant β > a + o(1), for all but a negligible fraction of seeds.
- **So the pre-registered Flag Z9 is false**, and with it the expected Y9c. The reviewer's ruling anticipated the possibility and required the report to say so: **it says so.** The depth conjecture's ledger stays at four instances (LP22, Proposition H, Proposition H′, HIR23).
- **Smallest case (as ruled).** Take a = 1 and k = 4: the range has ≤ 2^n/n elements; at most a 1/8 fraction of seeds have K(G_n(z)) ≤ n − log n − 4; for the rest, depth ≤ log n + 4 + O(1). The obstruction to depth is visible at the first non-trivial parameters, not only asymptotically.

## 2. Why the regime closes anyway: the missing upper bound

**What the technique needs.** R_K is a distinguisher for G because *every* output has small K (their l.146–150). Transposed to K^t, the argument needs

  K^t(G_n(z)) ≤ s(n) + O(log n)  for the relevant polynomial t.

**Why it is unavailable.** The decoder holding (z, description of G) must **run** G_n to output G_n(z). G is **EXP^NP-computable** (Theorem 3.2). So the bound is available only for t exponential in n. For polynomial t the bound fails to follow, and nothing else supplies it: Lemma Y9.1's counting gives only lower bounds on K^t, and is fully consistent with **K^t(G_n(z)) = n + O(1)** for every seed — the case in which R_{K^t} rejects nothing in the range and is **not a distinguisher at all**.

**So the honest statement of the closure.** The O(log n)-gap technique does not cross from K to K^t because it rests on an upper bound whose only proof is "run the generator", and the generator is exponential-time. **This is a statement about the technique, not a barrier**: it does not preclude some other construction supplying a polynomial-time-computable generator with the properties [28] needs, which is precisely what §3 addresses.

## 3. Ruling (2): what a polynomial-time generator loses, named

**What [28] actually gets (verified, Theorem 3.2).**

> "There exists an EXP^NP-computable pseudorandom generator G = {G_n : {0,1}^{n−O(log n)} → {0,1}^n} such that **EXP^NP ⊆ BPP^D for any distinguisher D for G**."

**So the NO-side guarantee is not a hitting-set property against a circuit class.** It is a *security-to-hardness transfer*: any distinguisher for G is powerful enough that BPP with that distinguisher as an oracle contains EXP^NP. R_K is such a distinguisher, which is what makes the reduction from NEXP work.

**What is lost under a polynomial-time generator.** The transfer's strength is inherited from the **hardness class underwriting the generator's security**, and that class is tied to the generator's own complexity:
- an EXP^NP-computable generator can be built from EXP^NP-hardness by a black-box security proof (their Theorem 3.2, and their remark that the seed stretches by only O(log n) is what evades the [GV08] impossibility);
- a **polynomial-time-computable** generator's security cannot be based on EXP^NP-hardness by the same route — the construction would place an EXP^NP-hard object inside a polynomial-time map.

**And the point that decides it for us:** *neither* version yields a conclusion about **NP**. [28]'s conclusion is EXP^NP ⊆ BPP^D; the target here needs a reduction *from an NP-complete problem* to the promise problem. **So even a polynomial-time generator with all the properties one could want would give a reduction from the class its security is based on — not from NP.** That is the precise reason the regime closes for our purpose, and it is independent of the K/K^t issue in §2.

## 4. Flag R9, and the kill tests

- **R9 not triggered.** Nothing adapted, so no relativization check was owed. Had the technique adapted, Y8c would have required it to be non-relativizing, and [28]'s machinery is a relativizing generator argument as far as read — so an adaptation would have been evidence of an error. **The discipline stands unused this round, which is the good case.**
- **Silent on Y8:** Y9 concerned an explicit reduction only; the non-explicit door is untouched and remains relativization-barred.
- **The depth ledger:** unchanged at four instances. **Y9 removes a candidate rather than adding one.**
- **Smallest case:** done in §1.

## 5. Priors against outcome, and misses

| | Y9b | Y9c | Y9a |
|---|---|---|---|
| reviewer → moved | 50 → 40 | 35 → 45 | 15 → 15 |
| mine | 40 | **45** | 15 |
| **outcome** | **✓** | **refuted by Lemma Y9.1 / Proposition Y9.2** | not reached |

- **My miss, and it is the same shape as Y8's.** I put 45 on Y9c — "the outputs are deep" — and argued it was "visible in the quoted step rather than guessed". It was neither: it was an inference I had not checked by counting. A long seed makes the outputs **shallow**, and one line of counting shows it. **I moved the reviewer's prior toward my error**, which is worse than holding it alone.
- **The reviewer's part:** it accepted that reasoning and moved its prior to mine. Whether that counts is the reviewer's to rule.
- **What saved it:** the reviewer's ruling (1), which demanded a proof of the half I had assumed. **The practice line proposed:** *when a flag's content is an inequality about a specific construction, do the counting before putting a prior on it.*

## Ceiling

Unchanged. Y9 proves nothing about P vs NP. It closes the last regime where the barriers were silent — for a reason that is about the technique and about the class its security transfers from — and it **removes** an instance from the depth ledger rather than adding one.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as Y9b on the report.** Merge 2d707a4; push on the author's standing go; then the page update (§10 item 21; the depth ledger corrected to four with **Y9 recorded as a removal**; §7 both misses — mine as written, the reviewer's **twenty-first**, accepted-and-moved; my practice line verbatim).

**Lemma Y9.1 and Proposition Y9.2 go in as proved, ours, elementary.** The squeeze — the range is too big to be K-compressible, and K^t is capped at n + O(1) — is a clean fact, and it **corrects the scope of the depth conjecture**: the conjecture should read *"NP-hardness instances whose YES side is K^t-compressible at the threshold are deep"*. [28]'s range elements are shallow because they are not K^t-compressible at all for polynomial t, so they are not YES instances and the conjecture never spoke about them.
