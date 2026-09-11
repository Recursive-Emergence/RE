# N1: fold accumulation (nesting), mapped. Report

*Run 2026-09-10 on branch `n1-fold-accumulation`, on the author's go ("Draft and run N1, push after merge"), against the pre-registration (599c0db). The reviewer accepted it with all four flags as verification targets; priors N1a 50 / N1c 35 / N1b 15. Documents only. g1, g8, g9 and g10 applied. Nothing here bears on P ≠ NP beyond location.*

## 0. Outcome

**N1a and N1c, together**, as both sides expected.
- **N1a: the smallest open fold is named.** "The inner product mod 2 (IP2) has no polynomial-size LTF∘LTF circuits." In words: depth-3 majority circuits are strictly stronger than depth-2 arbitrary-weight threshold circuits on an explicit function.
  - It is open, and stated so in Kane–Williams' own list of open questions.
  - For *majority* gates the depth 2 → 3 fold is already proved (§3).
- **N1c: the exact gap.** The proved accumulation, the AC⁰ depth hierarchy, reaches the polynomial hierarchy **only through oracle constructions**. The one known transfer between random-oracle and unrelativized PH runs the wrong way: Book's theorem transfers *collapse* down, not strictness.
  - So "folds accumulate" is a theorem exactly in the black-box world.
  - Its white-box form is PH strictness itself.

## 1. Sources read in this run

- **Rossman–Servedio–Tan**, "An average-case depth hierarchy theorem for Boolean circuits", arXiv:1504.03398 (FOCS 2015). Primary.
- **Kane–Williams**, "Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits", arXiv:1511.07860. Primary for its results. Its §2 history is secondary for Hajnal et al., Goldmann–Håstad–Razborov and Allender–Koucký.
- **Limaye–Sreenivasaiah–Srinivasan–Tripathi–Venkitesh**, "A Fixed-Depth Size-Hierarchy Theorem for AC⁰[⊕] via the Coin Problem", arXiv:1809.04092. Primary.
- **Oliveira–Santhanam**, "Conspiracies between Learning Algorithms, Circuit Lower Bounds and Pseudorandomness", arXiv:1611.01190. Secondary, stating Razborov–Rudich and Naor–Reingold.
- **Pudlák 2020** (local), for Tarski. **Wikipedia** "Arithmetical hierarchy" and "LH (complexity)": **secondary, and tagged wherever used**.
- **Not reached:** Håstad's thesis, Sipser 1983, Barrington–Immerman–Straubing, Book 1994, Baker–Gill–Solovay (BGS). Each is stated only as quoted by the sources above.

## 2. (a) Unbounded nesting: accumulation is a theorem

- **Tarski** (Pudlák 2020, l.309–313): "By Tarski's Theorem (which is easily provable using the fix-point lemma) it is not possible to define truth for all formulas. In particular, in an arithmetical theory we can define truth for classes Π_n, but not for all arithmetical formulas."
- **Strictness** (secondary, Wikipedia): "The inclusions Π⁰_n ⊊ Π⁰_{n+1} and Σ⁰_n ⊊ Σ⁰_{n+1} hold for all n … Thus the hierarchy does not collapse. This is a direct consequence of Post's theorem."
- **Where the diagonal uses unbounded evaluation.** Level n has a *universal* member: a truth definition for Σ_n (or Π_n), as Pudlák says. The diagonal is taken against that universal predicate. The predicate evaluates every level-n formula on every input with **unbounded** search inside each quantifier. That is the step that will not survive a clock.
  - With a clock, the only diagonal available is the time-hierarchy diagonal (Cook–Nguyen, Theorem 11.9). It separates by *time within one level*, and it relativizes.
  - This explanation is ours, labelled. No source is quoted for it beyond the two statements above.

## 3. (b) Bounded nesting, proved: circuit depth

**Håstad's depth hierarchy** (RST, Theorem 4, stating [Hås86a]): "For every d ∈ ℕ, there exists a Boolean function F_d : {0,1}ⁿ → {0,1} such that F_d is computed by a linear-size depth-d circuit, but any depth-(d − 1) circuit computing F_d has size exp(n^{Ω(1/d)})."
- F_d are the Sipser functions: read-once monotone formulas with alternating AND/OR layers of fan-in n^{1/d}.
- Sipser's own bound was Ω(n^{log^{(3d)} n}).

**The average-case version** (RST abstract): "for every d ≥ 2, there is an explicit n-variable Boolean function f, computed by a linear-size depth-d formula, which is such that any depth-(d − 1) circuit that agrees with f on (1/2 + o_n(1)) fraction of all inputs must have size exp(n^{Ω(1/d)})."

**The corollary** (RST, Theorem 2): "The polynomial hierarchy is infinite relative to a random oracle: with probability 1, a random oracle A satisfies Σ_d^{P,A} ⊊ Σ_{d+1}^{P,A} for all d ∈ ℕ."

**Threshold circuits, depth 2 → 3 for majority: proved** (Kane–Williams §2, stating Hajnal et al. [HMP+93]). IP2 "requires 2^{Ω(n)} size when the weights of each LTF are small … often cited as saying that the inner product does not have subexponential-size MAJ∘MAJ circuits", while "IP2 has MAJ∘MAJ∘MAJ circuits with O(n) gates". **For majority gates, the third fold adds, on an explicit function.**

## 4. (c) Bounded nesting, open: the frontier per class (Flag C)

| Class | The fold | Status | Source |
|---|---|---|---|
| AC⁰ | depth d → d+1 | **proved**, worst case and average case | Håstad; RST |
| AC⁰[p] | depth d → d+1 | **not found stated** (g8). The only AC⁰[⊕] hierarchy found is a *fixed-depth size* hierarchy, for uniform AC⁰[⊕] formulas. Razborov–Smolensky bounds MOD_q from outside the class. | Limaye et al. (abstract; open problems at l.2800ff) |
| MAJ∘MAJ → MAJ∘MAJ∘MAJ | depth 2 → 3 | **proved** (IP2) | Kane–Williams, stating HMP+93 |
| LTF∘LTF (arbitrary weights) → MAJ³ | depth 2 → 3 | **open**: "Are there polynomial-size LTF∘LTF circuits for the function IP2? … Amano and Maruoka [AM05] point out that any answer to this question, yes or no, would imply new separations of some threshold circuit classes." Every LTF∘LTF circuit is efficiently simulated by MAJ∘MAJ∘MAJ (Goldmann–Håstad–Razborov, as stated). | Kane–Williams, open question 2 |
| MAJ³ = TC⁰₃ → deeper | depth 3 → 4 | **open**. Kane–Williams give the *first* super-linear gate bound for depth-3 majority, Ω(n^{3/2}/log³ n), and "prior to our work, it was open whether every function in nondeterministic 2^{O(n)} time could be computed by LTF∘LTF … (or TC⁰₃) families with O(n) gates". Superpolynomial bounds are not claimed by any source read. | Kane–Williams abstract, §1 |
| TC⁰, all constant depths | size | Allender–Koucký, as stated: "in order to separate NC¹ from TC⁰, we only need to exhibit a function in NC¹ that does not have n^{1.1} gates for every depth d ≥ 2" | Kane–Williams §1 |

**The smallest open "next fold adds" statement:**

> **IP2 has no polynomial-size LTF∘LTF circuits.**

Since IP2 has O(n)-gate MAJ∘MAJ∘MAJ circuits, this says the third layer strictly adds over arbitrary-weight depth 2, for an explicit function.
- It is **a size lower bound and a depth separation at once**. As the reviewer instructed, that changes what "attack" means: an attempt is a lower-bound proof against LTF∘LTF, and Kane–Williams' n^{3/2}-gate bound for Andreev's function is the current best of that kind.
- **Known partial results, as stated in Kane–Williams §2:**
  - IP2 needs exponential size for MAJ∘LTF (Nisan) and for LTF∘MAJ (Forster et al.);
  - IP2 needs Ω(n/log n) gates for LTF∘LTF (Goldmann–Håstad–Razborov);
  - PARITY needs o(n^{3/2}) wires … "nor can they have o(n^{1/2}) gates" (Impagliazzo–Paturi–Saks).
- **Where it sits.** This is below AC⁰[p] in the reviewer's list, and below the threshold depth-3 question.

## 5. (d) The barriers at the top

**Relativization (Flag O), confirmed as the exact gap.**
- **The bridge is oracle-only.** RST §2.2: "Following [FSS81], Sipser noted the analogous connection between Meyer's question and circuit lower bounds [Sip83]: to answer Meyer's question in the affirmative, it suffices to exhibit, for every constant d ∈ ℕ, a Boolean function F_d computable by a depth-d AC⁰ circuit such that any depth-(d − 1) circuit computing F_d requires super-quasipolynomial size."
  - Meyer's question is "Is there a relativized world within which the polynomial hierarchy is infinite?"
  - Håstad's hierarchy answers it "in the affirmative for all d".
  - **The theorems that construct the oracle:** FSS81 / Sipser 1983, with Håstad for all d; and RST Theorem 2 for random oracles.
- **The one downward transfer goes the wrong way.** RST §2.3: "a surprising result of Book, who proved that the unrelativized polynomial hierarchy collapses if it collapses relative to a random oracle [Boo94]."
  - Collapse transfers down; strictness does not.
  - So RST's random-oracle strictness gives **no** unrelativized consequence. That is the precise gap (g10: nothing beyond the quoted implication is inferred).
- **The collapse side.** BGS "prove the existence of an oracle A such that P^A ≠ NP^A ≠ coNP^A" (RST §2.2), with the d = 2 case due to Baker–Selman. The collapsing oracle, P^A = NP^A, is the standard BGS companion. It is **not re-read here** (nor in A4).

**Natural proofs (Flag N), per class** (Oliveira–Santhanam l.427–431): "There are natural properties against AC0[p] circuits, when p is prime [RR97]. But under standard cryptographic assumptions, there is no natural property against TC0 [NR04]. Consequently, the situation for classes contained in AC0[p] and for those that contain TC0 is reasonably well-understood." They add: "the existence of natural properties against ACC0 has become one of the most intriguing problems in connection with the theory of natural proofs."
- **AC⁰, AC⁰[p]:** natural proofs succeed, and no PRFs are known there.
- **TC⁰:** natural proofs are barred, assuming Naor–Reingold PRFs.
- **ACC⁰:** the frontier.
- **Whether the barrier reaches the named open fold** (depth-2 LTF, and depth 3) depends on the depth at which Naor–Reingold-type PRFs live. That is not stated in the sources read (g10), so the report does not claim that the smallest open fold is natural-proofs-barred.

## 6. Flag L: the log-time hierarchy

- **Partly verified.** Wikipedia, LH page (secondary, citing Immerman, *Descriptive Complexity*, p. 85): LH "is equal to FO and to FO-uniform AC0".
- **LH's strictness is not found stated** in any source reached (g8). Sipser's uniform depth hierarchy plus this equality would give it, but that combination is **my inference** (g10) and is not recorded as verified.
- **Why it would still be the black-box regime** (the reviewer's line, adopted as a reading): at log time the machine cannot read its whole input. The evaluator is bounded below the object's size. That is the M4 tension in the opposite direction: the fold is larger than what can name it.

## 7. (e) The reading (labelled)

**Accumulation is proved exactly where the evaluator is not bounded by the object.**
- *Unboundedly*, the diagonal names every level-n formula through a universal truth predicate. It pays unbounded search to do so, and it proves strictness.
- *With a clock*, what is proved is depth accumulation for explicit functions in weak circuit classes, and the only bridge to PH is an oracle.
  - An oracle is a black box whose contents the machine does not name.
  - Relative to it, the fold's content is typical (random-oracle strictness, RST), not named.

This is the fifth appearance of "naming costs what it names". It was a reading in M4 (size), A1 (⊥ vs all proofs), and A3/A4 (self-evaluation; a relativization that is the same at both layers). It is recorded as a reading and not counted as a new instance under g12, since no sourced pair formulation is involved.

## 8. Priors against outcome

| | N1a | N1b | N1c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 60 → 50 | 15 → 15 | 25 → 35 |
| mine | 45 | 15 | 40 |
| **outcome** | **✓** | | **✓** (co-occurring) |

- **Flag O confirmed.**
- **Flag C confirmed and sharpened.** The smallest open fold is depth-2 arbitrary-weight threshold vs depth-3 majority, on IP2.
- **Flag N confirmed per class.**
- **Flag L only half verified**: the equality is found, the strictness is not.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.
