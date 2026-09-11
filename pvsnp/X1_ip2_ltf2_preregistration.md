# X1: IP2 ∉ poly-size LTF∘LTF — the first attempt. Pre-registration

*Drafted 2026-09-10 on branch `x1-ip2-ltf2`, on the author's go ("Draft and run X1, push after merge"), for the reviewer's ruling before any work. g1, g5, g8 and g9 apply. X1 is the program's first **attempt**. Its honest deliverable is the **sub-obstacle** (R5-style), not a proof. It stays documents plus proof sketches until a lemma is stated.*

## Target

**Kane–Williams, open question 2** (verified in N1): "Are there polynomial-size LTF∘LTF circuits for the function IP2?"
- IP2(x, y) = ⊕_i (x_i ∧ y_i): the parity of ANDs, two nestings.
- It has O(n)-gate MAJ∘MAJ∘MAJ circuits.
- Every LTF∘LTF circuit is efficiently simulated by MAJ∘MAJ∘MAJ (Goldmann–Håstad–Razborov, as stated in Kane–Williams).

## Targets (the reviewer's, verbatim in content)

- **(a) The floor.** Each known bound with its exact statement, and which gate's weights it assumes bounded:
  - Hajnal et al.: MAJ∘MAJ, 2^{Ω(n)};
  - Nisan: MAJ∘LTF;
  - Forster et al.: LTF∘MAJ;
  - Goldmann–Håstad–Razborov: Ω(n/log n) gates for LTF∘LTF, and LTF∘LTF ⊆ MAJ³;
  - Kane–Williams: n^{3/2} gates for Andreev's function;
  - Impagliazzo–Paturi–Saks: PARITY.
- **(b) The mechanism as a testable lemma.** A communication or sign-rank-type measure that is bounded for poly-size LTF∘LTF and large for IP2, the way discrepancy is for MAJ∘MAJ. Pre-register the known reason each candidate measure fails.
- **(c) Step by step.** Take the MAJ∘MAJ proof for IP2. Record the first step that fails when (i) the top gate, (ii) the bottom gates, or (iii) both get arbitrary weights. Say whether a verified repair exists in each case.

## Flags raised before any work (mine)

**Flag W (the repair assignment in (c) is swapped).** By the naming convention (top∘bottom), the repairs are:
- **MAJ∘LTF (Nisan)** has the *top* gate bounded and the *bottom* gates arbitrary. So Nisan repairs **(ii)**, arbitrary bottom weights.
- **LTF∘MAJ (Forster et al.)** has the *top* gate arbitrary and the *bottom* gates bounded. So Forster repairs **(i)**, an arbitrary top weight.

The reviewer's (c) has "Nisan for (i); Forster for (ii)". I expect the reverse, and the run will verify it from the statements. The reviewer's (a) column labels ("MAJ∘LTF — top gate bounded"; "LTF∘MAJ — bottom gates bounded") are consistent with my reading. Only (c)'s assignment is swapped.

**Flag M (my expected mechanism for each case; to verify, g1).**
- **MAJ∘MAJ (HMPST).**
  - A top gate with small weights gives some bottom gate correlation ≥ 1/poly with IP2 (a discriminator-type lemma).
  - A bottom gate with small weights has small deterministic communication complexity, so it is a union of few rectangles.
  - IP2 has exponentially small discrepancy, so no bottom gate correlates. Contradiction.
- **(ii) Arbitrary bottom weights (repaired by Nisan).** An arbitrary-weight LTF still has a short *randomized* protocol, so the bottom-gate step survives.
- **(i) An arbitrary top weight (repaired by Forster et al.).**
  - The discriminator step fails: an arbitrary-weight top gate need not have a correlating input.
  - The repair is **sign-rank**. Each bounded-weight bottom gate is a sum of few low-rank pieces, so the circuit's sign-rank is poly(s). Forster's bound gives IP2 sign-rank 2^{Ω(n)}.
- **(iii) Both arbitrary.**
  - The discriminator step fails, because the top is arbitrary.
  - The low-rank step fails, because a bottom LTF with exponentially many distinct partial sums is not a sum of few low-rank pieces.
  - Expected: no repair.

**Flag S (sign-rank may be refuted as the measure for LTF∘LTF — from memory, to be verified).** I recall results showing that some poly-size depth-2 threshold circuit has **exponential sign-rank** (Chattopadhyay–Mande 2018, "a short list of equalities induces large sign rank"; possibly also Hatami–Hosseini–Lovett).
- If verified for LTF∘LTF, or for a subclass of it, **sign-rank cannot be the separating measure for (iii)**, since the class itself contains functions of exponential sign-rank. Poly-size LTF∘MAJ has poly sign-rank (the Forster et al. mechanism), so it would also separate LTF∘MAJ ⊊ LTF∘LTF.
- The sub-obstacle is then sharper: the next measure must be bounded for LTF∘LTF, although sign-rank and discrepancy both are not.
- This would *not* be X1c (a two-nesting function in small LTF∘LTF). It would be an X1a with a named failed measure.

**Flag R (the IP2-specific question).** Even if no measure works for all of LTF∘LTF, the question concerns IP2 alone. IP2 is *rank*-hard, not merely sign-rank-hard; it is bent, with all Fourier coefficients ±2^{−n/2}. Any candidate lemma is stated for IP2 specifically, not class-wide.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X1a** | The sub-obstacle is a named measure that no known technique bounds for LTF∘LTF, stated as the smallest open lemma. |
| **X1b** | A verified partial repair for (iii) exists that the map missed. Record it; the attempt continues on it. |
| **X1c** | The mechanism reading in (b) is refuted by a known construction: an explicit function with two nestings computed by small LTF∘LTF. Then the fold count is the wrong measure at this depth. |

**Priors.**
- Reviewer: X1a 60 / X1c 25 / X1b 15.
- Mine: **X1a 65 / X1c 15 / X1b 20.**
  - X1c is lowered: Flag S, if verified, refutes a *measure*, not the fold-count reading.
  - X1b is raised slightly: the post-2016 literature on sign-rank and threshold circuits may hold a partial repair the N1 map did not reach.

## Ceiling

X1 proves nothing. At best it names the smallest open lemma, with the failed measures and the first failing step in each case written out. Any proof attempt on that lemma is pre-registered separately.
