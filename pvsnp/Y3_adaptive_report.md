# Y3: the adaptive question. Report

*Run 2026-09-11 on branch `y3-adaptive`, on the author's go ("Run Y3, push after merge"), against the pre-registration (a3d7472) and the reviewer's ruling (ea2d896).*
- *Priors, both sides: Y3b 55 / Y3a 35 / Y3c 10.*
- *Scoring rule: if Flag C holds, the reviewer's "answers as advice" expectation is a wrong prior.*

*Documents only; `formal/` closed.*

*Sources read as text this run:*
- *Saks–Santhanam CCC'22 (**SS22**): §4 (hypotheses H1–H6, Theorem 14, the definitions of J[γ]), §5 (Lemmas 21 and 22, the protocol Steps 1–7, Theorem 25, Corollary 26);*
- *Allender–Buhrman–Koucký–van Melkebeek–Ronneburger, ECCC TR02-028 (**ABKMR**): abstract, Theorems 12, 13, 17 and 18, the proofs of Theorem 12 and Lemma 23;*
- *Hirahara, ECCC TR20-050 (**Hir20**): §3, Theorems 3.1–3.3;*
- *Huang–Ilango–Ren, IACR ePrint 2023/528 (**HIR23**, full version of STOC'23): Theorems 1.1 and 1.2, Theorem 3.1 and its proof, Lemma 3.5, Corollary 3.7, and the barrier discussion;*
- *Arvind's complexity column (IMSc, column 117), l.201–233, for lowness.*

## 0. Outcome

**Y3b: the barrier's extension fails at a named step, at two rounds.** The step is the input type of SS22's protocols.

- **The failing step.** Lemmas 21 and 22 (entropy estimation [24], lower bound [25]) take as input **a circuit C_f computing f : (ρ, i) ↦ q_i(ρ)** (l.938–950). In Step 2, Arthur evaluates f himself on public coins.
  - For a non-adaptive M, f is a polynomial-time map.
  - For an adaptive M, the round-2 queries depend on the round-1 answers J[γ](q), which are approximate counts that only Merlin can supply. **f is no longer a circuit, and the protocols' input changes type.**
- **What a bounded-round barrier would need instead.** Versions of Lemmas 21 and 22 for circuits with gates for a context-sensitive, perturbed approximate-count oracle J[γ], where the oracle's values are certified by the same protocols one round earlier.
  - That is a **lowness property for SS22-style approximate-count oracles**.
  - **Low(AM) = AM ∩ coAM** (verified, Arvind's column l.233) covers oracles that are *languages* in AM ∩ coAM. J[γ] is a function whose consistency holds only for most γ (SS22's Propositions 15–16), so Low(AM) does not apply directly.
  - The needed statement is **not found stated** in anything read. A round-by-round route with independent perturbations γ₁, γ₂, … looks plausible for O(1) rounds but is **not proved here**.
- **The reviewer's (b) is proved (§2):** a barrier of SS22's shape can hold only above the window that SS22's NEXP reduction tolerates, unless NEXP ⊆ AM ∩ coAM.
- **The reviewer's (c):**
  - Proposition H′ is upgraded from a sketch to a **conditional proposition proved from ABKMR's verified statements (§3):** unless PSPACE ⊆ BPP^NP, the strings ABKMR's reduction relies on are **deep, by |y|/2 − O(|y|^{1/2})**, on infinitely many lengths.
  - Proposition H (the NEXP end) keeps its two unverified items. Hir20's non-adaptive NEXP theorem was not located in the part of the text read.
- **The door's current address (HIR23, §4).** NP-hardness *is* known at the NP level under randomized black-box **many-one** reductions, for **conditional** K^t with a NO side at n − O(1), assuming subexponentially secure witness encryption (Theorem 3.1).
  - With injective one-way functions added, the auxiliary string y is also non-deep (Corollary 3.7).
  - But **the NO outputs are maximally deep in x | y** (proved, §4): hiding is depth once more, now via witness encryption. So it is not LP23's door.

**Priors and the scoring rule.**
- Y3b holds (55 on both sides).
- **My Flag S was a wrong premise.** SS22's protocol is entirely public-coin (entropy estimation plus lower bound, Steps 1–7), with no secret-sample upper-bound protocol, so there was nothing to leak.
- **Flag C is not established.** SS22's §4 assumes H1 (non-adaptivity) throughout (l.720–728). My round-by-round argument for step (A) remains a sketch.
- **The failure the text shows is the reviewer's mechanism:** the oracle answers become inputs to the query map. It is located in step (B), not (A).
- The scoring rule's trigger ("if Flag C holds") is therefore not met. The reviewer's mechanism is, if anything, confirmed.

## 1. Arm (a): where 2-round adaptivity breaks SS22's proof (verified structure; our analysis)

**SS22's structure (verified):**
- H1: "M is a randomized nonadaptive decision OTM" (l.722). Theorem 14: under H1–H6, L ∈ AM ∩ coAM.
- The query map is q_x^M(ρ, i), the i-th query on random string ρ. S(q) is its preimage, s(q) = |S(q)|, and J[γ](q) = ϕ((1 + γ)s(q)) (l.790–800).
- The protocol (l.1045–1085):
  - Step 1: entropy estimation of π_f (Lemma 21).
  - Step 2: public ρ₁, …, ρ_t, and the matrix χ_{i,j} = f(ρ_i, j).
  - Step 3: Merlin's count matrix B.
  - Step 4: the entropy consistency check.
  - Step 5: the lower-bound protocol (Lemma 22) on (χ, B).
  - Steps 6–7: the output, with the perturbation.
- Corollary 26: failure ↦ 0 gives an AM protocol for L; failure ↦ 1 gives coAM.

**Two rounds.**
- Let M ask k₁ queries, receive answers, then ask k₂ queries that depend on those answers.
- **Step (A)**, defining J round by round, is well-defined for each fixed γ: π₁ from round 1, then π₂ from round 2 with J[γ]'s round-1 answers (Flag C). Whether SS22's K′ construction (Theorem 18) goes through is not checked, because §4 is written under H1.
- **Step (B) breaks at Step 2 / Lemmas 21–22.**
  - χ_{i,j} for j > k₁ requires J[γ](χ_{i,j′}) for j′ ≤ k₁, i.e. ϕ((1 + γ)·s(χ_{i,j′})).
  - Arthur can use Merlin's B_{i,j′} in place of s(χ_{i,j′}). But **then the map f that Lemmas 21–22 test is f_B, not f**.
  - Lemma 22's guarantee is about |f^{−1}(q)| for the circuit it is given. The entropy check (Step 4) compares against H(π_f) for that circuit.
  - A Merlin who shifts round-1 counts within the (1 + ζ) slack changes the round-2 query distribution itself. Neither lemma is stated for circuits whose gates are the prover's own claimed counts.
  - **This is the named step.**
- **The lemma that would be needed:** Lemmas 21 and 22 relativized to oracle gates computing J[γ], with the oracle certified by the same protocol one level down, and with the perturbation argument (Propositions 15–16) applied per round with independent γ_r.
  - Low(AM) = AM ∩ coAM (Arvind's column l.233: "NP∩coNP = Low(NP) ⊆ AM∩coAM = Low(AM) ⊆ Low(ZPP(NP)) ⊆ Low(Σ^P_2)") is the language version. The approximate-count version is **open as far as the sources read show**.
- **Flag U stands** (the reviewer ruled it verified): ABKMR's PSPACE ⊆ P^{R_K} (Theorem 13, verified) goes through BPP^{R_KS} and Theorem 18 ([IW98]), a "probabilistic, polynomial time Turing machine with oracle T" (l.389–393), i.e. adaptive.
  - The round count of the downward self-reduction is **not** stated in the text read.
  - So the break lies at or below ABKMR's adaptivity, which is unbounded as far as the text shows.

## 2. Arm (b): the consistency fact (proved)

**SS22's Theorem 3, second part (verified, l.205–207):** every L ∈ NEXP has a randomized polynomial-time non-adaptive reduction, polynomially honest with constant advantage, to O(log n)-additively approximating K. Let c₀·log n be the window it tolerates.

**Claim.** Let g(n) ≤ c₀·log n. Suppose a statement B holds: "every computable L with a randomized poly-time non-adaptive, polynomially honest, inverse-polynomial-advantage reduction to g-approximating K is in AM ∩ coAM". Then NEXP ⊆ AM ∩ coAM.

*Proof.*
- A reduction to g-approximating K must succeed with **every** oracle within g of K.
- An oracle within g(n) ≤ c₀·log n of K is within c₀·log n, so the NEXP reduction succeeds with it.
- So every NEXP language (all are computable) satisfies B's hypothesis, and lies in AM ∩ coAM. ∎

**Corollary.** Barriers of SS22's shape can hold only for windows above the NEXP reduction's tolerance, unless NEXP ⊆ AM ∩ coAM (⊆ Σ₂^p ∩ Π₂^p). That collapse is not known false, but no one expects it. SS22's barrier is at ω(log n), consistent with this. **The O(log n) window is open from both sides:** no barrier is possible there without the collapse, and no NP-hardness is known there under the promise.

## 3. Arm (c): Proposition H′, now proved conditionally from ABKMR's verified statements

**Verified ingredients (ABKMR):**
- f ∈ DSPACE(n) is downward and random self-reducible and hard for PSPACE (proof of Theorem 12, l.519).
- G^{BFNW}_f : {0,1}^{n^{1/2}} → {0,1}^n, and all strings in its range have KS(y) ≤ O(|y|^{1/2}) (l.520–522; the exponent is garbled in the text extraction and read from the stated seed length n^{1/2}).
- **Theorem 18 ([IW98]):** if |Pr_r[r ∈ T] − Pr_x[G(x) ∈ T]| ≥ 1/p(n) for all n large enough, then a probabilistic polynomial-time Turing machine with oracle T computes f with probability ≥ 2/3.

**Proposition H′ (ours; conditional).** Fix a polynomial t, and let T := R_{K^t} = {y : K^t(y) ≥ |y|/2}, which is in coNP. If PSPACE ⊄ BPP^NP, then for every polynomial p there are infinitely many n with

  Pr_z[K^t(G(z)) < n/2] < 1/p(n) + 2^{−n/2+1},

and so, with probability ≥ 1 − 1/p(n) − o(1) over z, **K^t(G(z)) − K(G(z)) ≥ n/2 − O(n^{1/2})**.

*Proof.*
- Random r lies outside T with probability ≤ 2^{−n/2+1}.
- If for all large n a 1/p fraction of G's outputs lay outside T, then T would distinguish, and Theorem 18 would give f ∈ BPP^T ⊆ BPP^NP. That puts PSPACE ⊆ BPP^NP, a contradiction.
- Also K(G(z)) ≤ KS(G(z)) + O(1) ≤ O(n^{1/2}). ∎

**Scope, stated exactly.** This proves that the strings whose non-randomness R_K must detect for ABKMR's argument, the range of G^{BFNW}_f, are deep (io, conditional). ABKMR's reduction's *actual queries* come from the [IW98] reconstruction and may be hybrids; their depth is not determined here. **So at the PSPACE end, "hiding is depth" is a conditional theorem about the distinguishing set, not about every query.**

**Proposition H (NEXP end, from Y2):** still conditional, with its two unverified items (the tolerance constant c₀, and the depth of the queries). Hir20's text read (§3, Theorems 3.1–3.3) states the non-adaptive NEXP result only in the overview (l.296–297); the theorem itself is in a part not read.

## 4. Literature item 5: HIR23, the door's current address, and why it is not LP23's

**Theorem 3.1 (verified, HIR23 l.944–952).** Assume subexponentially secure witness encryption for NP. Then for every c ≥ 1, with t₂(n) = 2^{n^c}, there are polynomials p and t₁ such that it is NP-hard under randomised reductions to decide the promise problem on (x, y), with |x| = n and |y| = p(n):
- YES: K^{t₁}(x | y) ≤ n^{1/c};
- NO: K^{t₂}(x | y) ≥ n − O(1).

The informal version says: "a standard, black-box, randomized many-one reduction".

**The reduction (verified, l.976–1000):** x = m ← {0,1}^n and y = Encrypt(1^λ, φ, m; r).
- YES: Decrypt with the witness gives K^{poly}(x | y) ≤ O(N).
- NO: list security of the witness encryption gives K^{t₂}(x | y) > n − 10⁵ with probability ≥ 2/3.

**Corollary 3.7 (verified, l.1103–1112).** Adding subexponentially secure injective OWF, the YES and NO sides also satisfy cd^{t₁}(y) ≤ n^{1/c} (Lemma 3.5, under Encrypt injective). This is Hirahara's [Hir22b] Heuristica problem.

**The NO outputs are maximally deep in x | y (proved, under Corollary 3.7's injectivity).**
- Given y and φ, brute force over (m, r) finds the unique m with Encrypt(1^λ, φ, m; r) = y.
- So K(x | y) ≤ K(φ) + O(log n) ≤ O(N) = O(n^{1/2c}).
- With NO's K^{t₂}(x | y) ≥ n − O(1), **the t₂-time conditional depth of x | y is ≥ n − O(n^{1/2c})**. ∎
- *Without injectivity* (Theorem 3.1 alone), K(x | y) ≤ K(φ) + log(the number of m consistent with y) + O(log n), which is not determined here.

**What this means.**
- HIR23 evades GK24/SS22 in three ways: (i) the problem is conditional; (ii) the NO bound is time-bounded (K^{2^{n^c}}), not unbounded, so NO outputs need not be K-random; (iii) the correctness rests on cryptographic assumptions. Their footnote 12 says the oracle-independence barrier "does not apply to Theorem 1.1 due to the use of cryptographic assumptions".
- **HIR23 hides m in y (witness encryption) and so outputs maximally deep NO instances in x | y.** Their Lemma 3.5 controls the depth of y, not of x | y. So HIR23's reduction is **outside a conditional analogue of LP23's promise, by the widest possible margin**.
- **This is the fourth instance of hiding as depth on the record:**
  1. LP22 (obfuscation, Y1′);
  2. Proposition H (NEXP, conditional sketch);
  3. Proposition H′ (PSPACE, conditional theorem, §3);
  4. HIR23 (witness encryption, proved under injectivity).
- **The door's current address, stated exactly:** the known NP-level evasions of the SZK barrier use **conditional** problems with **time-bounded NO sides** and hide their NO instances as depth. LP23's door needs **unconditional**, **non-deep** NO instances. No reduction read supplies them.

## 5. Priors against outcome, and misses

| | Y3b | Y3a | Y3c |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 55 → 55 | 30 → 35 | 15 → 10 |
| mine | 55 | 35 | 10 |
| **outcome** | **✓** (Step 2 / Lemmas 21–22 input type; the needed approximate-count lowness is open) | not proved (the O(1)-round route is plausible, not done) | no template: SS22's NEXP reduction is non-adaptive, and HIR23's hides by depth |

- **My miss:** Flag S (the secret sample in a coAM upper-bound protocol) was a **wrong premise**. SS22's coAM side is obtained by flipping the failure output of a public-coin protocol (Corollary 26), not by an upper-bound protocol. This could have been checked in SS22's text before the pre-registration, since the protocol was at l.1045–1085 of a file already read in Y2.
- **The reviewer's "answers as advice":** the mechanism is confirmed, located in step (B). The scoring rule's trigger (Flag C holds) is not established, so it is not counted as wrong. Scoring is the reviewer's to make.

## Ceiling

Y3 proves nothing about P vs NP or OWF.
- It locates the adaptive question to one missing lemma: approximate-count lowness for AM.
- It proves the O(log n) window is open from both sides.
- It adds a conditional theorem (Proposition H′) and a proved depth fact (HIR23's NO side) to the "hiding is depth" record.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as Y3b on the report.** Merge f940ee9; push on the author's standing go; then the page update.

**Scoring:** the Flag-S miss is mine. The reviewer's "answers as advice" mechanism is confirmed. No miss on the reviewer's side this round.

**The door's address after Y3, and "hiding is depth" as a conjecture with its proved cases,** go on the page verbatim (§3 and §6).

**Y4 (the lowness lemma at two rounds)** is named, on the author's go, as a draft for ruling.
