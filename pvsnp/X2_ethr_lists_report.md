# X2: L0 — lower bounds for decision lists of exact thresholds. Report

*Run 2026-09-10 on branch `x2-ethr-lists`, on the author's go ("Draft and run X2, push after merge"), against the pre-registration (d7c58cf), accepted by the reviewer. The reviewer adopted Flag N and records its "necessary step" wording as a slip; Flag P is the main check; priors X2a 45 / X2b 35 / X2c 20. g1, g5, g8 and g9 applied. X2 names the lemma under the lemma. Its only proofs are two elementary ones of ours (§4), labelled.*

## 0. Outcome

**X2a.** The first failing step is named, with the measure, the witness and the reason it stops.
- **Flag P (the X2b risk) is closed negatively.** PMA^cc ⊄ PP^cc, because Chattopadhyay–Mande prove PMA ⊄ UPP and state PP ⊊ UPP. Short exact-threshold decision lists (DL-ETHR) are therefore *not* covered by IP2's PP-hardness. Even the subclass of Equality lists escapes: their F_n is a linear-length list of Equalities outside UPP ⊇ PP.
- **The measure that works for arbitrary-threshold lists fails at its first lemma for exact thresholds.** The Turán–Vatan / CMMS rectangle argument relies on CMMS Lemma 16: in any rectangle, an LTF has either a large 1-rectangle or a 0-rectangle that loses only an *additive* t on each side. **Equality is an exact threshold that violates Lemma 16** (§4.1).
  - This is the same witness as X1's sub-obstacle.
  - The multiplicative repair (ours, §4.2) gives IP2 ∉ DL-ETHR of length < n/log₂6. The argument **cannot certify more than O(n)**, so it stops at linear.
- **The lemma under L1 (L0 for IP2, stated without "necessary" per Flag N):**
  > **IP2 has no polynomial-length decision list of exact threshold gates.**
  - It is *implied by* L1 and by the fold statement. It would follow from IP2 ∉ PMA^cc, by CM's containment.
  - It is open (g8: not found stated either way).
  - Sign-rank (F_n), PP/discrepancy (F_n) and additive rectangles (Equality) all fail. Multiplicative rectangles and randomized cost stop at Ω(n).

## 1. Sources read in this run

- **Chattopadhyay–Mande** (SIAM J. Comput. 2022), again: §1 (l.270–352), Theorem 6.2 and the containments that follow it, the Appendix A definitions, and §8.
- **Chattopadhyay–Mahajan–Mande–Saurabh**, "Lower bounds for linear decision lists", arXiv:1901.05911. Primary: Lemmas 16 and 17, the introduction, and the conclusion.
- **Not reached:** Turán–Vatan; Gröger–Turán; Göös–Pitassi–Watson (the landscape); Impagliazzo–Williams; Hansen–Podolskii. They are stated as quoted by the two papers above.

## 2. (a) The statement, the containments, and what is known

- **L0, as CM state it (§8):** "can we prove strong lower bounds on the size of decision lists of exact thresholds for computing an explicit (say, in NP) function? This is a subclass of THR∘THR."
- **The relation to L1 (Flag N; the reviewer's slip recorded).** DL-ETHR ⊆ THR∘THR, so L1 ⇒ (fold statement) ⇒ L0-for-IP2. L0 is **implied by** L1. It is not a rung toward it.
- **The converse (Flag N).** If IP2 had polynomial-length DL-ETHR, then IP2 ∈ THR∘THR, and both L1 and the fold statement would be false.
  - Whether IP2 has short DL-ETHR: **not found stated** (g8). The only known lower bound is the linear one proved here (§4.2).
  - CM (§8, footnote): "it is not hard to show that decision lists of Equalities cannot compute IP … Since they are in AC0". That covers Equality lists only, not exact thresholds.
- **PMA** (CM Definition A.5): deterministic protocols that may, "for cost k, … compute the value of g(x, y), where g has an MA protocol of cost k."
  - CM: "every function expressible as a short decision list of exact thresholds is in PMA". Their F_n ∈ PMA, via binary search with an OR∘EQ oracle (Protocol 6.1).
  - CM (after Theorem 6.2): "It is known that PMA^cc ⊆ S₂P^cc and PMA^cc ⊆ BPP^NP^cc".
- **Flag P, closed.** CM, §1: "it is known that P^NP ⊊ UPP and MA ⊊ PP ⊊ UPP"; and Theorem 1.3 / 6.2: "PMA ⊄ UPP".
  - Hence **PMA^cc ⊄ PP^cc**. *Ours, one line:* if PMA ⊆ PP ⊆ UPP, then PMA ⊆ UPP, which is a contradiction.
  - Sharper, from the same facts: F_n is a linear-length decision list of Equalities with UPP cost Ω(n^{1/4}) (CM l.1826), so F_n ∉ PP^cc. **Even short Equality lists escape discrepancy.** Discrepancy lower bounds for PP therefore cannot give L0.
  - CM's pointer for new techniques: "there are specialized techniques for proving lower bounds against the class P^NP (see [37, 28]). Can they be generalized to PMA?" [37] is Impagliazzo–Williams, "Communication complexity with synchronized clocks", CCC 2010. [28]'s title is garbled in our extraction.
- **Arbitrary-threshold lists, known** (CMMS §1): "Lower bounds against linear decision lists … for the Inner Product modulo 2 function were proved by Gröger, Turán and Vatan". CMMS Theorem 1: MAJ∘XOR needs linear decision lists of size 2^{Ω(n)}.
- **Exact-threshold lists are not inside linear decision lists** (CMMS, conclusion): "the function from [4] separating LTF∘LTF from LTF∘MAJ … is also not in LDL — it contains the function OR∘EQ as a subfunction." So IP2 ∉ LDL does **not** give L0.

## 3. (b)/(c) Why Equality is the obstruction, and the first failing step

- **The rectangle argument.** CMMS Lemma 17: "any function with no monochromatic rectangle of weight greater than w under the distribution µ × ν … any linear decision list computing f must have size at least 1/√w."
  - Its engine is Lemma 16, which quantifies over one LTF: "Let f be an LTF … Then, one of the following is true. 1. There exists a monochromatic 1-rectangle (X′, Y′) within X × Y … such that µ(X′) ≥ t and ν(Y′) ≥ t. 2. There exists a monochromatic 0-rectangle (X′, Y′) within X × Y such that µ(X′) > m − t and ν(Y′) > m − t."
  - The proof sorts rows and columns by partial sum, "in decreasing order of a + ⟨α·x⟩ and ⟨β·y⟩". An LTF's sorted matrix is a staircase, so the loss is **additive** (m − t), and that is what yields 1/√w, i.e. exponential lower bounds.
- **The first failing step for DL-ETHR is Lemma 16.** An exact threshold's sorted matrix is 1 only on a level set u(x) + v(y) = t: an anti-diagonal, not a staircase. Equality is the extreme case (§4.1).
  - This is the same function that stops the bottom-gate protocols in X1 (CM §1.4). **One witness, two proofs, same place.**
- **Other measures, and where each stops:**
  - **sign-rank** fails on CM's F_n (sign-rank 2^{Ω(n^{1/4})}, linear-length list);
  - **discrepancy / PP** fails on F_n ∉ UPP ⊇ PP;
  - **multiplicative rectangles** stop at Ω(n) (§4.2);
  - **randomized communication** also stops at linear. A length-ℓ list is simulated by answering each query with a public-coin equality test at error 1/(3ℓ), cost O(ℓ log ℓ). IP2's randomized cost is Θ(n), which gives only ℓ = Ω(n/log n). *Sketch, ours; IP2's Ω(n) randomized bound is standard and not re-read.*
  - **What remains:** lower-bound techniques against PMA-type power, beyond P^NP (CM's pointer). Not found worked out (g8).

## 4. Proofs (ours; g5; elementary; not claimed new)

**4.1 Equality violates CMMS Lemma 16.**
- *Setting.* µ = ν uniform on {0,1}^n; X = Y = {0,1}^n, so m = 1. Take 2^{−n} < t ≤ 1/2. EQ(x, y) = [Σ 2^i x_i − Σ 2^i y_i = 0] is an exact threshold (CM: "EQ ∈ ETHR").
- *No large 1-rectangle.* A 1-rectangle X′ × Y′ has x = y for all pairs, so |X′| = |Y′| = 1 and µ(X′) = 2^{−n} < t.
- *No large 0-rectangle.* A 0-rectangle has X′ ∩ Y′ = ∅, so µ(X′) + ν(Y′) ≤ 1 and min(µ(X′), ν(Y′)) ≤ 1/2 ≤ 1 − t. So "µ(X′) > m − t and ν(Y′) > m − t" fails.
- Neither alternative holds. ∎

**4.2 A multiplicative substitute, and its cap.**
- **Lemma A.** Let q(x, y) = [u(x) + v(y) = t] be an exact threshold, and X × Y a rectangle with product measure µ × ν. Then X × Y contains a rectangle X′ × Y′ with µ(X′)ν(Y′) ≥ µ(X)ν(Y)/6 on which q is constant.
  - Let a be a µ-median of u on X, so that X_≤ = {u ≤ a} and X_≥ = {u ≥ a} each have weight ≥ µ(X)/2.
  - Split Y into Y_< = {v < t − a}, Y_> = {v > t − a} and Y_= = {v = t − a}. One of them has weight ≥ ν(Y)/3.
  - *Case Y_<:* on X_≤ × Y_<, u + v < t, so q = 0.
  - *Case Y_>:* on X_≥ × Y_>, u + v > t, so q = 0.
  - *Case Y_=:* here q = [u = a]. If {u ≠ a} has weight ≥ µ(X)/2, use {u ≠ a} × Y_=, where q = 0. Otherwise use {u = a} × Y_=, where q = 1. ∎
- **Corollary.** A DL-ETHR of length k computing f gives f a monochromatic rectangle of weight ≥ 6^{−k}.
  - Walk down the list with Lemma A. A constant-1 rectangle ends the walk, since f equals that query's output there. A constant-0 rectangle continues the walk. The last query is ≡ 1. ∎
- **IP2.** The ±1 matrix M = ((−1)^{⟨x,y⟩}) is Sylvester–Hadamard, with MMᵀ = 2^n I and ‖M‖ = 2^{n/2}.
  - A monochromatic A × B satisfies |A||B| = |1_Aᵀ M 1_B| ≤ 2^{n/2} √(|A||B|). So |A||B| ≤ 2^n: weight ≤ 2^{−n} under the uniform measure.
  - **Hence every DL-ETHR for IP2 has length k ≥ n / log₂ 6.** ∎
- **The cap.** Every f has a monochromatic rectangle of weight ≥ 4^{−n}, namely a single entry. So this measure can never certify k > 2n/log₂6. It is inherently linear.
  - The contrast with LTF lists, where Lemma 16's additive loss gives 1/√w, is exactly Equality (§4.1).

## 5. The two-level open statement (end state of the attempt phase, as pre-registered)

> **IP2 ∉ poly-size THR∘THR** (Kane–Williams OQ2; Amano: "a long standing open question")
> ⇐ **L1**: every poly-size THR∘THR has sign-rank 2^{o(n)} (CM §8; 2^{Ω(n^{1/4})} attained)
> and ⇒ **L0(IP2)**: IP2 has no poly-length decision list of exact thresholds (open)
> ⇐ IP2 ∉ PMA^cc (CM's containment; PMA lower bounds need "new techniques", per CM).

**At L0(IP2), the failing steps of every measure checked:**
- sign-rank: CM's F_n;
- discrepancy / PP: F_n ∉ UPP ⊇ PP;
- additive rectangles (CMMS Lemma 16): Equality;
- multiplicative rectangles and randomized cost: capped at Ω(n), proved here as n/log₂6 for rectangles.

**The single recurring obstruction** across X1 and X2 is **Equality**, an exact threshold. Its matrix is anti-diagonal. It has no low-error cheap randomized protocol at the error a heavy top gate requires, and no staircase structure for rectangle arguments.

## 6. Priors against outcome

| | X2a | X2b | X2c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 60 → 45 | 20 → 35 | 20 → 20 |
| mine | 45 | 35 | 20 |
| **outcome** | **X2a** | | |

- **My X2b weight (35) was a miss.** Flag P's containment is refuted by CM's own separation.
- **The reviewer's slip ("necessary step")** is recorded as it asked, and the word is kept out of the claims here.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as X2a. The attempt phase closes.** The end state stands as in §5.

Calibration:
- the reviewer's: the "necessary" direction slip;
- mine: the X2b weight.
