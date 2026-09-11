# X9: the loose Union Lemma under exponential fragmentation. Report

*Run 2026-09-11 on branch `x9-fragmented`, on the author's go ("Draft and run X9, push after merge"), against the pre-registration (7d2c438), accepted by the reviewer with all five flags, priors X9c 65 / X9b 20 / X9a 15, the discrepancy framing, and the B(n, m) deliverable. Documents plus computation (`x9_B.py` in the job's scratch directory); `formal/` closed. **The X8 practice:** smallest case first, and the compared bound beside every number.*

## 0. The framing (the reviewer's, stated first)

**The loose Union Lemma is a bias-versus-constraints trade-off.**
- C = ∩_{j≤m} (J − q_j) is the 1-set of a conjunction of m non-equality constraints "a_j(x) ≠ b_j(y)", i.e. a set decided by m Equality-oracle queries joined by AND.
- Since Adv(IP2, U) = 2^n − Adv(IP2, C), the loose UL says: **no such C has |Adv(IP2, C)| ≫ 2^n + poly(m)·2^{1.75n}.** It is a uniform-discrepancy statement for IP2 against m-query Equality-oracle conjunctions.
- **Landmarks:**
  - disjointness (m = n) gives 3^n = 2^{1.585n};
  - Lemma T′'s inclusion–exclusion settles m ≤ n/4;
  - so all the content is at m ≫ n, with cancellation.

## 1. Outcome

**X9c: neither a witness nor a proof. The stall is named inside (b), and arm (a) is shown inconclusive by design at feasible n.**
- **(a)** A greedy/annealed search at n ≤ 8 finds conjunctions C with |Adv(IP2, C)| ≈ 2^{1.75n}, already at m = n, exceeding 3^n by a factor that grows with n.
  - That is **not a witness**, since the lemma allows poly(m)·2^{1.75n}.
  - **And it cannot become one at feasible n.** The covering obstruction (§3) is m ≳ 2^{(n−1)/2}. It lies *below* m = 2n for n ≤ 9, and below m = n² until n ≈ 25. So at any computable n the search sits in the regime where most of IP2's −1 set can be carved out, which is not the poly(m) regime the lemma is about.
- **(b)** The Fourier expansion of ∏_j (J − q_j) against H is inclusion–exclusion with 2^m blocky-intersection terms, each bounded by 2^{1.5n}. **A poly(m) bound needs cancellation among those terms: the same cross-type cancellation named in X6.** No new tool was found.
- **A proved fact that bounds the monochromatic extreme** (ours: Pitassi–Shirley–Shraibman's Theorem 29 applied with X7's −1-rectangle theorem):
  > carving a *monochromatic* C out of IP2 (so that the union U covers every +1 entry, or every −1 entry) needs m ≥ Ω(2^{n/2}) blocky sets.
  - So **polynomially many constraints cannot make C monochromatic.** The loose UL is the *bias* version of this covering bound, and the bias version is what is open.

## 2. Arm (a): B(n, m), searched (lower bounds; each beside 3^n and 2^{1.75n})

Method: greedy removal of the blocky set maximizing the gain in |Adv(C)|. Each step is solved by the decoupled column-label local search on H∘C, trying both signs. K is the maximum row-type count within one block.

| n | m | |Adv(C)| | ÷ 3^n | ÷ 2^{1.75n} | K | |C| |
|---|---|---|---|---|---|---|
| 4 | 4 | 114 | 1.41 | 0.89 | 6 | 126 |
| 5 | 5 | 446 | 1.84 | 1.04 | 10 | 500 |
| 6 | 6 | 1509 | 2.07 | 1.04 | 17 | 2235 |
| 6 | 12 | 1860 | 2.55 | 1.28 | 17 | 1860 (all −1) |
| 8 | 8 | 13219 | 2.01 | 0.81 | 33 | 32551 |
| 8 | 16 | 17330 | 2.64 | 1.06 | 33 | 23156 |

- **The AND reference** (m = n): Adv(C) = 3^n exactly, at every n (computed).
- **Reading:** at m = n the greedy value stays within a constant of 2^{1.75n} (ratios 0.89, 1.04, 1.04, 0.81 at n = 4, 5, 6, 8; n = 8 used fewer restarts). It exceeds the AND family by a growing factor (1.41 → 2.01), and at m = 2n it reaches 1.28 and 1.06. At n = 6, m = 12, it carves an all-(−1) C of 1,860 entries, out of the 2,016 −1 entries in total.
- **Why this is not evidence either way.** At these n the whole −1 set, 2^{2n−1}, is within a small factor of 2^{1.75n} (a factor 2^{0.25n−1} ≈ 1.41 at n = 6). The covering threshold m* ≈ 2^{(n−1)/2} is 5.7 at n = 6 and 11.3 at n = 8, so m = 2n already exceeds it. **Brute-force numerics cannot reach the regime m ≪ 2^{n/2} with 2^{1.75n} ≪ 2^{2n}**, which needs n in the tens.

## 3. The covering bound (proved; ours, from two sourced/proved facts)

- **Pitassi–Shirley–Shraibman, Theorem 29** (primary text, read in X3/X9): "Let A be a {0,1}-valued m × n matrix. Then C1B(A) ≥ Ω(max-rect(A))." Here C1B is the minimum number of blocky matrices covering A's ones.
  - Their proof gives |cover| ≥ 2α(A)/(√β(A)·(rows + cols)), where α counts the ones and β is the area of the largest all-ones rectangle. It uses that each row lies in at most |cover| rectangles, so Σ(rows + cols of R_i) ≥ Σ 2√|R_i| ≥ 2α/√β.
  - The theorem is stated for **any** 0/1 matrix, so it applies to IP2 (mod 2), not only to Integer Inner Product (the function of their separation).
- **X7's theorem:** IP2's largest −1 rectangle has area N/2, and its largest +1 rectangle has area N.
- **Hence:**
  - covering IP2's −1 set (α ≈ N²/2, β = N/2) needs ≳ 2·(N²/2)/(√(N/2)·2N) = √(N/2) = Ω(2^{n/2}) blocky sets;
  - covering the +1 set (β = N) needs Ω(2^{n/2}) as well.
- So a monochromatic C of either sign, with |C| ≈ 2^{2n−1}, needs m = 2^{Ω(n)}. ∎ (The constants are not optimized.)

## 4. Arm (b): the structure, and the stall

- **Exact:** Adv(IP2, C) = Σ_{S⊆[m]} (−1)^{|S|}·Adv(IP2, ∩_{j∈S} q_j), with ∩_{j∈S} q_j blocky, each term ≤ 2^{1.5n} (Lemma T).
- **Tests (as ruled):**
  - *Block-Equality family:* by X5–X6, Adv(C) = 2^n, so Adv(U) = 0. The 2^m terms cancel to exact balance.
  - *AND family:* the terms are the subcube rectangles {x_S = y_S = 1}. On each, IP2 = |S| + IP2(rest), so Adv(∩_{j∈S} q_j) = (−1)^{|S|}·2^{n−|S|}. The alternating sum is Σ_S 2^{n−|S|} = 3^n, with no cancellation: every term enters with the same sign (also computed).
- **The stall:** a bound of poly(m)·2^{1.75n} needs the 2^m-term alternating sum to cancel down to poly(m) terms' worth.
  - This is the reviewer's expectation: the same cross-type cancellation as X6, now written as the inability to bound the high-order terms of ∏(J − q_j) without inclusion–exclusion.
  - The covering bound (§3) controls only the *monochromatic* extreme. **A bias version of Pitassi–Shirley–Shraibman's max-rect argument is the named missing lemma:** a lower bound on m in terms of |Adv(IP2, C)| rather than |C|.

## 5. Priors against outcome

| | X9a | X9b | X9c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 25 → 15 | 20 → 20 | 55 → 65 |
| mine | 15 | 20 | 65 |
| **outcome** | | | **X9c** |

**A methodological finding, recorded for any future attempt:** arm (a)'s numerics cannot test the lemma at computable n, because the covering threshold 2^{(n−1)/2} is below any poly(n) for n ≲ 25. Evidence about the loose UL must come from structure, not search.

## Formal record

Untouched (the author's decision).
