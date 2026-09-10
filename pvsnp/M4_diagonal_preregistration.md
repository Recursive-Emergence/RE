# M4: succinct diagonal tautologies. Pre-registration (draft only)

*Drafted 2026-09-10 on branch `m4-diagonal`. **The author's instruction is "draft only": this pre-registration goes to the reviewer for its ruling, and the run waits for the author's review.** It is a document only; guards g1, g5, g8, g9 and g11 apply.*

## Target (the reviewer's shape)

M3 showed that on hardness sentences Gödel's move is a restatement, not a lever: for a Π₁ H at a fixed bound, "T ⊬ ¬H" is equivalent to H. The lever is the diagonal fixed point. M4 makes that concrete in four parts:
- **(a)** the diagonal tautology ρ_n(π) := ¬Prf_P(π, ⌜ρ_n⌝) for |π| ≤ s(n), which is a tautology without short P-proofs *by soundness alone*;
- **(b)** its cost;
- **(c)** whether *succinct* self-reference, through implicit proofs (Krajíček 2004), can make it pay;
- **(d)** the smallest form.

## Flags raised before any run

**Flag S (mine): in propositional logic the diagonal bound is at most polynomially above the trivial one.**
- ρ_n contains the variables of π, so |ρ_n| ≥ s(n).
- In a Cook–Reckhow proof system f, a proof x of y satisfies y = f(x) with f computable in polynomial time. So |y| ≤ q(|x|) for a polynomial q, that is, |x| ≥ |y|^{Ω(1)}.
- Every proof of ρ_n therefore has length ≥ |ρ_n|^{Ω(1)} ≥ s(n)^{Ω(1)} *trivially*.
- **So "no P-proof of ρ_n of size ≤ s(n)" improves on the trivial bound by at most a polynomial.** For Frege-type systems, where a proof contains its conclusion, it does not improve on it at all.
- This sharpens the ruling's catch (b), "the lower bound is linear in the formula size": the propositional diagonal's own size already enforces its bound. *The run must check this against the literature's account, and it is proved in the report either way.*

**Flag F: first-order self-reference is already succinct, and its catch is already known.**
- Pudlák's Con_T(n) has length O(log n) with n in binary, because it quantifies over proofs.
- The self-reference therefore excludes proofs *exponentially longer than the sentence*, and the lower bound is n^ε (verified in M2).
- But Pudlák also proves an **n^k upper bound**, "based on a partial definition of truth" (verified in M2 from the paper's text). So compression through quantifiers *works* and still gives only a polynomial gap, measured in n.
- **Expected:** the implicit-proof version meets the same kind of catch, a polynomial-size proof of the succinct consistency statement, and that is outcome **D1**.

**Flag C: the fixed-point construction is already in the verified record.** Pudlák 1986 states its main lower bound "using finitistic counterparts of the well-known derivability conditions for the 2nd incompleteness theorem" (paper text, l.303–305). The run must quote the exact statement and check whether a *propositional* version (ρ_n) is stated anywhere: Krajíček's book or Pudlák's surveys.

## What the run must verify (after the author's review and the reviewer's ruling)

**(a)** The diagonal construction as it appears in the literature (Pudlák 1986 §3; Krajíček's account of consistency statements), and exactly what is proved. The propositional ρ_n, if stated.

**(b)** The cost, and why the gap is polynomial:
- Flag S, proved;
- Pudlák's own explanation of the polynomial distance between the n^ε lower bound and the n^k upper bound.

**(c)** Implicit proofs (Krajíček, *Implicit proofs*, J. Symbolic Logic 69, 2004):
- (i) the definition, with proofs given by circuits that compute their bits, and systems such as implicit EF (iEF);
- (ii) whether a consistency or diagonal statement for an implicit system can be stated in size polynomial in n while excluding proofs of superpolynomial length;
- (iii) what is proved about implicit systems' strength and about their consistency statements, in particular any result that the compression buys nothing, such as a consistency statement for iP being provable in P, or the succinct diagonal having a polynomial-size proof.

If the compression worked at no cost, it would give superpolynomial lower bounds for every sound system, and hence NP ≠ coNP. **So there must be a catch, and the run must name which step of the (a) argument fails in the succinct version.**

**(d)** The smallest form: the exact statement "a polynomial-size self-referential tautology family for iP has no iP-proofs of size s", together with the step it needs.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **D1** | The succinct diagonal is stated, and its catch is a known theorem. The smallest form is that theorem's hypothesis. |
| **D2** | The catch is not in the literature: an open question, stated precisely. That would be the first new question this programme has produced. |
| **D3** | Implicit proofs do not admit the fixed-point construction at all. Record why. |

**Priors.** Mine: D1 65 / D2 20 / D3 15, with D1 favoured by Flags S and F. The reviewer's: D1 55 / D2 30 / D3 15.

## Ceiling

M4 proves nothing about P vs NP. It turns "Gödel's move is a restatement" into "Gödel's lever exists but is expensive", and asks whether compression pays, with a catch that can be checked.
