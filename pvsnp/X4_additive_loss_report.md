# X4: the additive-loss lemma. Report

*Run 2026-09-10 on branch `x4-additive-loss`, on the author's go ("Draft and run X4, push after merge"), against the pre-registration (5101f6f), accepted by the reviewer with Flag P's order and priors X4a 55 / X4b 35 / X4c 10. Documents plus proof sketches; `formal/` closed. g1, g5, g8 and g9 applied.*

## 0. Outcome

**X4b.**
- **The kill test (Flag K) fails for Theorem 45's actual measure, and it teaches something.**
  - OMB∘AND does have exponentially small discrepancy, but only under its *hardest* distribution (BVW's PP lower bound).
  - Under the **uniform** distribution, the one Theorem 45 uses, its discrepancy is ≥ 1/4 (§2). So the multiplicative loss is **not** shown to be necessary for uniform blocky discrepancy.
  - What K *does* refute: any **depth-independent** ELDL bound in terms of discrepancy under *arbitrary* distributions (§2).
- **The multiplicative step is located** (§3): one inequality, in the induction step.
- **The additive repair fails at one named step** (§4). The advantage bound of Lemma 44 holds for a *single* blocky system. A layer's queries form a *union* of blocky matrices; the union bound gives PP25's factor s_i, and inclusion–exclusion gives 2^{s_i}.
- **The sharpened lemma under the lemma, the Union Lemma:**
  > for f with Disc_U(f) ≤ d, the advantage of f on any union of m blocky matrices is at most poly(m) · 2^{2n}·√d.
  - With it, Theorem 45's recursion becomes additive, and L0(IP2) would follow at every alternation depth (§4).
- **A correction for the queued X5 frame** (§5): under the *uniform* distribution the three witnesses do **not** agree on discrepancy.

## 1. Sources read in this run

- **Podolskii–Prior**, ECCC TR25-143 (primary): Lemma 44 and its proof; Theorem 45 and its full proof; §1 (l.141–176, 282–300).
- **Buhrman–Vereshchagin–de Wolf**, "On Computation and Communication with Small Bias", CCC 2007 (primary, de Wolf's copy): abstract, §2 facts (l.300–312), §3 (l.440–600).
- **Sherstov**, "Halfspace matrices": only via the search summary ("discrepancy Ω(1/n⁴) under every product distribution but O(√n/2^{n/4}) under a certain non-product distribution"). **Secondary / unverified**, and not used for any claim below.

## 2. (b) The kill test: Flag K

- **The function** (BVW §3, verbatim): "let x, y ∈ {0,1}^n, and k = max{i ∈ [n] | x_i = y_i = 1} … Define f(x, y) to be the least significant bit of k … We will show here that UPP(f) = O(log n) while PP(f) = Ω(n^{1/3})."
- **The discrepancy link** (BVW §2): "PP-complexity is essentially determined by discrepancy … disc_µ(f) = max_R |µ(R ∩ f⁻¹(1)) − µ(R ∩ f⁻¹(0))|". The PP lower bound "is determined by the discrepancy of f under the hardest input distribution". BVW's own proof uses structured distributions: "x(j) and y(j) are chosen randomly subject to each having weight m/4, and having intersection size i".
- **It is a linear-size ELDL (ours, elementary):** for i = n, n−1, …, 1, "if x_i + y_i = 2 then output lsb(i)"; default 0. That is n exact linear thresholds (x_i + y_i − 2 = 0, natural weights), with alternation depth n.
- **Its uniform discrepancy is large (ours, elementary):** on R = {x_n = 1} × {y_n = 1}, which has uniform measure 1/4, f ≡ lsb(n). So Disc_U(f) ≥ 1/4.
- **Verdict.**
  - K fails against Theorem 45, which is a *uniform* statement ("we are interested in discrepancy when µ = U"). The multiplicative loss is not shown to be necessary.
  - K **does refute** any bound of the form "ELDL size ≥ g(disc_µ(f)), independent of alternation depth, for arbitrary µ" with g superpolynomial: OMB∘AND has disc_µ ≤ 2^{−Ω(n^{1/3})} for its hardest µ (via PP = Ω(n^{1/3})) and an O(n) ELDL.
  - So **any additive repair must use the uniform, or at least a product, distribution**. That is a real constraint recorded from a known function.
  - Theorem 45 itself is consistent with it: at k = n, k·d^{−1/2k} ≈ n.

## 3. (a) Where the loss becomes multiplicative

The proof of Theorem 45, as a numbered sequence (PP25 p. 20):
1. *Lemma 44* (single blocky system): Disc_U(f) ≤ d ⇒ f has advantage ≤ 2^{2n+1}√d on any blocky system. The proof splits the rectangles into "wide" and "tall" and averages over rows or columns.
2. *Layer 1* (output b): each query is a monochromatic blocky matrix, covering ≤ 2^{2n+1}√d b-entries. So s₁ queries cover ≤ 2^{2n+1}√d·s₁.
3. *The induction step, layer i* (output b). "The corresponding blocky matrix does not have to be monochromatic since it can contain ¬b-entries covered on the previous layers. The number of ¬b-entries covered on the previous layers is upper bounded by … ≤ (2^i − 2)·2^{2n}√d·∏_{j<i} s_j." Then by Lemma 44, "the number of b-entries covered by this blocky matrix is at most 2^{2n+1}√d larger."
4. **The multiplicative step:** "Since there are at most s_i queries on the i-th layer, together they cover at most 2^{2n+i}√d·∏_{j≤i} s_j b-entries."
   - **Each of the s_i queries is charged the *entire* ¬b-coverage of all earlier layers**, and the charges are summed.
   - **What is discarded:** the fact that the layer's ¬b-overlaps come from *one* fixed set P_{i−1} (the earlier coverage). Charging it s_i times multiplies it by s_i, instead of adding.
5. *End:* the final layer's b-count ≤ 2^{2n+k+1}√d·∏ s_j. With the balance assumption, ∏ s_j ≥ Ω(d^{−1/2}/2^k). AM–GM with Σ s_j = s gives s ≥ Ω(k·d^{−1/2k}).

## 4. (c) The additive repair, and where it fails

**The repair (pre-registered: a sum, not a product).** Let U_i be the region newly covered by layer i, where the list outputs b, so f ≡ b there. Aim for
  P_i ≤ P_{i−1} + poly(s_i)·A, with A = 2^{2n+1}√d,
where P_i is the coverage so far. This gives P_k ≤ k·P₀ + poly(s)·A. With balance, poly(s) ≥ Ω(d^{−1/2}/k): a depth-independent bound, polynomial in 1/d.

**Attempt.** U_i ⊆ ∪_{q∈layer i} q, and U_i is disjoint from the earlier coverage. Its b-entries are
  |U_i| ≤ |∪_q q ∩ f⁻¹(b)| = |∪_q q ∩ f⁻¹(¬b)| + Adv(f, ∪_q q),
and |∪_q q ∩ f⁻¹(¬b)| ≤ P_{i−1}, since the ¬b-entries inside the union were all covered earlier, where the list is correct. This term is charged **once**, not s_i times. The additive form therefore holds **iff**
  **Adv(f, ∪_{q∈layer i} q) ≤ poly(s_i)·A.**

**The first step where it fails to go through:** Lemma 44 bounds advantage on a *single blocky system*. The union of s_i blocky matrices is not a blocky system. The two known ways to bound it:
- **the union bound**, Adv(∪) ≤ Σ_q (¬b-overlap + A), which re-charges P_{i−1} per query. That is exactly step 4, the multiplicative loss.
- **inclusion–exclusion**, Adv(∪) = Σ_{∅≠S} (−1)^{|S|+1}·Adv(∩_S q), which gives |Adv(∪)| ≤ (2^{s_i} − 1)·A.
  - *Ours, elementary:* an intersection of blocky matrices is blocky. {a(x) = b(y)} ∩ {a′(x) = b′(y)} = {(a, a′)(x) = (b, b′)(y)}.
  - The loss is 2^{s_i}, worse than s_i.

**The named lemma (X4b's sharpened sub-obstacle), the Union Lemma:** for f with Disc_U(f) ≤ d and any m blocky matrices q₁…q_m,
  |Adv(f, q₁ ∪ … ∪ q_m)| ≤ poly(m)·2^{2n}√d.
- **What is known:** the trivial bound m·(ν + A), and 2^m·A by inclusion–exclusion.
- **One check on IP2 (ours, elementary):** take the n rectangles R_j = {x_j = 1} × {y_j = 1}.
  - Their union is the complement of disjointness, and IP2's ±1-advantage on it is 2^n − 3^n. The 3^n disjoint pairs all have ⟨x, y⟩ = 0, and the total sum over the cube is 2^n.
  - |2^n − 3^n| ≈ 2^{1.585n}, which is **below** A ≈ 2^{1.75n+1} (with d = 2^{−n/2} for IP2 under U, from the Hadamard bound).
  - No violation. The Union Lemma is not refuted on this family, and it is **open** (g8: not found stated).

## 5. Correction to the queued X5 frame (the witnesses under the uniform distribution)

The reviewer's queued X5 guidance says "OMB∘AND (tiny disc …), F_n (tiny disc …), IP2 (tiny disc …)". Under the **uniform** distribution, the measure Theorem 45 uses:
- **OMB∘AND:** Disc_U ≥ 1/4 (§2).
- **CM's F_n = OMB∘(OR∘XOR):** the top block is unequal with probability 1 − 2^{−(block length)}, so F_n is nearly constant under U. Disc_U(F_n) ≥ 1 − o(1), and F_n is not approximately balanced. *Ours, elementary, from CM's definition.*
- **IP2:** Disc_U ≤ 2^{−n/2}, and balanced.

So **uniform discrepancy already separates IP2 from both list witnesses.** The witnesses agree with IP2 only under their *hardest* distributions, which is the PP notion. The replacement measure X5 was to seek is therefore not needed *on the witnesses*. What fails is the recursion, at the Union Lemma. **X5's premise should be re-read before drafting.** This bears on "the measure must change", which was X5's opening condition (X4a). X4 did not land there.

## 6. (d) The open statement, quoted with its scope (Podolskii–Prior)

- Abstract: "for the related model of exact linear decision lists, no strong lower bounds are known."
- §1 (l.175): "for the size of ELDLs, no strong lower bound techniques for explicit functions are currently known."
- l.282: "it remains an open problem to show strong lower bounds for explicit functions in this class. Under bounded depth, however, some lower bounds do follow".

**Scope:** *size*, *explicit functions*, *unbounded alternation depth*. Bounded depth is the exception they then prove. The sharpened open statement stands as recorded: IP2 against ELDL of alternation depth ≳ n/log n. The Union Lemma would close it.

## 7. Priors against outcome

| | X4a | X4b | X4c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 35 → 55 | 50 → 35 | 15 → 10 |
| mine | 55 | 35 | 10 |
| **outcome** | | **X4b** | |

**My miss:** the X4a weight (55). Flag K was pre-registered without checking *which* distribution the small discrepancy is under. Theorem 45's measure is uniform; BVW's is the hardest distribution.

## Formal record

Untouched (the author's decision). `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.
