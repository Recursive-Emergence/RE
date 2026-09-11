# Y2: hiding is depth: barrier or construction. Report

*Run 2026-09-11 on branch `y2-hiding`, on the author's go ("Run Y2, push after merge"), against the pre-registration (407b478) and the reviewer's ruling (6ae225a): literature first, then the gaps, then the statement, then the escapes. Priors (both sides): Y2a 45 / Y2c 40 / Y2b 15, with "Y2a-as-known" the likeliest form. Documents only; `formal/` closed.*

*Sources read as text this run:*
- *Goldberg–Kabanets, APPROX/RANDOM 2024 (**GK24**): abstract, Theorems 1 and 4–8, and the proof idea at l.425–450;*
- *Saks–Santhanam, CCC 2022 (**SS22**): abstract, Theorems 1–3, the honesty and advantage definitions, and the non-adaptivity remark;*
- *Allender–Hirahara–Tirumala, ITCS 2023 (**AHT23**): abstract, the summary of Theorems 15, 28 and 32, the definition of R̃_K, Definition 9 (Promise-EA) and Theorem 10;*
- *Hirahara, ECCC TR20-050 (STOC'20): abstract;*
- *Allender–Hirahara, ECCC TR17-073: abstract;*
- *LP23 (l.84–124) and LP25 (l.99–180), for the hardness notion and the boundary promise.*

*Not read: Goldreich–Sahai–Vadhan (the download failed; EA's completeness is taken from AHT23's Theorem 10, secondary) and Hirahara–Watanabe (search summary only; secondary).*

## 0. Outcome

**Y2a-as-known, in the low-threshold regime. The door is now located: the top-threshold regime (an O(log n) gap in K) and adaptive reductions.**

1. **Flag E is known.** GK24 proves it, by the same coding-theorem counting argument (l.425–450: "for any samplable distribution D, K(x) ≤ log(1/D(x)) + O(log n)"):
   - **Theorem 5:** "If MKP is hard for SAT under a randomized polynomial time many-one reduction running in time t_R(n) and with failure probability at most 1/p(t_R(n)), then NP ⊆ coAM."
   - **Theorem 6:** the same hypothesis gives L ⊆ NISZK.

   SS22's **Theorem 3** is the non-adaptive form: an honest reduction with inverse-polynomial advantage to ω(log n)-approximating K gives L ∈ AM ∩ coAM.
2. **The only new content is the application to LP23's promise** (§2, Observation O, proved). For thresholds s ≤ n − 2 − β·log n, a reduction into MK^tP[s]|Q^t_β *is* a reduction into MKP. So GK24 and SS22 apply, and Flag E (§3) covers constant error under a length condition.
3. **At the top threshold s = n − 2** (LP23's Theorem 1.1, second bullet), the K-gap on the promise is only β·log n + 1. **GK24's Theorem 5, SS22's Theorem 3 and Flag E all fail to apply** (§4).
   - SS22's own dichotomy says that at an O(log n) gap, randomized non-adaptive reductions to K-approximation are powerful enough for all of NEXP.
   - **So the two OWF-complete problems not touched by any barrier read, MK^tP[n−2]|Q^t_β and LP25's boundary-MINK^poly, both sit exactly in that regime.**
4. **Hiding is depth, as an evasion rather than a barrier** (§5): planted reductions keep the NO side low-K (deep), which keeps output entropy equal on YES and NO. A conditional **Proposition H** adds: SS22's NEXP-hardness reductions must query deep strings unless NEXP ⊆ BPP^NP.

**Priors.** Y2a (as known): 45 on both sides. **This is the outcome.** No miss on the outcome; one citation correction (§7).

## 1. Literature (item 1 of the ruling), statement by statement

| source | exact statement (verified) | hypotheses | what it covers here |
|---|---|---|---|
| **GK24 Theorem 5** | MKP hard for SAT under a randomized poly-time many-one reduction with failure ≤ 1/p(t_R) ⇒ NP ⊆ coAM (and NP ⊆ BPP if no OWF) | many-one; **tiny** failure probability; no honesty; any threshold | via Observation O: reductions into LP23's promise at s ≤ n − 2 − β log n with tiny error |
| **GK24 Theorem 6** | same hypothesis, for decidable L ⇒ L ⊆ NISZK | as above | as above |
| **GK24 Theorem 8** | L ⊆ NISZK ⟺ MKP-hard for L (failure 1/p(t_R)) ⟺ Approx_{n^{o(1)}}-K[n/2]-hard under honest many-one reductions (failure 2^{−poly}) | many-one | robustness in the tiny-error regime |
| **SS22 Theorem 3** | randomized poly-time **non-adaptive**, polynomially honest (queries of size \|x\|^{Ω(1)}), inverse-polynomial advantage, to **ω(log n)**-additively approximating K ⇒ L ∈ AM ∩ coAM. Conversely, **every L ∈ NEXP** has such a reduction to **O(log n)**-approximating K (constant advantage). | non-adaptive; honest; gap ω(log n) | constant-error, honest reductions at s ≤ n − ω(log n) |
| SS22 remark | "All our results in this paper have to do with non-adaptive reductions — analysing adaptive reductions is an interesting open question." | — | **adaptive reductions are open** |
| **AHT23 Theorem 15** | a decidable promise problem is randomly reducible to R̃_K (YES: K(y) ≥ \|y\|/2; NO: K(y) ≤ \|y\|/2 − e(\|y\|), with e = ω(log n) and e = n^{o(1)}) by an honest poly-time reduction ⟺ it is in NISZK | honest; gap ω(log n) | the SZK/NISZK characterization |
| AHT23 Definition 9 / Theorem 10 | Promise-EA: YES H(C) > k + 1, NO H(C) < k − 1; EA is NISZK-complete under honest ≤ᴾₘ reductions (citing GSV) | — | gap (ii) of Flag E |
| **Hirahara STOC'20** (abstract) | NP-hardness of MINcKT^SAT (conditional, SAT-oracle, poly-time-bounded K) under **deterministic** reductions; EXP^NP ⊆ P^{R_K} | conditional plus oracle | **evades by changing the problem** (conditional, oracle), not the reduction class. LP23's problem is unconditional and oracle-free, so this escape does not reach it. |
| Allender–Hirahara 2017 (abstract) | n^{1−o(1)}-approximate MCSP/MKTP is NP-intermediate if OWF exist; MKTP is DET-hard under non-uniform NC⁰ | — | **not the SZK-barrier source** (§7) |
| LP23 l.86–99 | "Π is OWF-hard if … if Π can be decided (in the worst-case) for infinitely many input lengths by 'efficient attackers', then all poly-time functions can be inverted"; OWF-completeness is defined "w.r.t. non black-box reductions — … even non explicit reductions" | — | **the holy grail needs only "Π ∈ ioBPP ⇒ NP ⊆ ioBPP"**: adaptive BPP-Turing reductions, and even non-explicit arguments, suffice (§4) |
| LP25 l.99–114, 158–176 | boundary-MINK^{t₁,t₂}: YES K^{t₁} ≤ n − 2 and K^{t₂} > n − log n; NO K^{t₂} ≥ n − 1. OWF ⟺ boundary-MINrK^poly ∉ ioBPP (Theorem 1.2; plain K^t under E ⊄ ioSIZE[2^{εn}], Theorem 1.1). The stated motive: the conditioning in LP23/HN23 "is not decidable" | — | immune to every barrier read (§4); the design motive is naturality, **not** barrier-avoidance |

## 2. Observation O: reductions into LP23's promise are reductions into MKP (proved)

**Claim.** Let s(n) ≤ n − 2 − β·log(n + c), where c is the constant in K ≤ n + c. Every randomized many-one reduction R from L to MK^tP[s]|Q^t_β with failure probability γ (the output is outside the promise, or on the wrong side, with probability ≤ γ) is a randomized many-one reduction from L to MKP (instances (x, s)) with failure probability ≤ γ.

*Proof.*
- YES outputs: K(x) ≤ K^t(x) ≤ s, so (x, s) ∈ MKP.
- NO outputs inside the promise: K^t(x) ≥ n − 1 and K^t(x) − K(x) ≤ β·log K(x) ≤ β·log(n + c). So K(x) ≥ n − 1 − β·log(n + c) > s, and (x, s) ∉ MKP. ∎

**Consequences (from the verified statements).**
- **(a)** With γ ≤ 1/p(t_R), GK24's Theorem 5 gives NP ⊆ coAM for L = SAT.
- **(b)** With constant or inverse-polynomial advantage, a polynomially honest non-adaptive R, and s ≤ n − ω(log n) (so the K-gap (n − 1 − β log n) − s is ω(log n)), SS22's Theorem 3 gives L ∈ AM ∩ coAM. It requires L computable, and SAT is.

## 3. Flag E, with the gaps checked (items 2–3 of the ruling)

**Flag E (ours; a variant of GK24's argument for constant error).** Let R be a randomized poly-time many-one reduction from SAT to MK^tP[s]|Q^t_β with failure ε < 1/2. Suppose that for every φ,

  (1 − ε)·(|x| − K(φ) − β·log|x| − O(log|x|)) > s + 5 + ε·|x|    (the length condition).

Then SAT ≤ᴾₘ Promise-EA (complemented), so NP ⊆ SZK ⊆ coAM.

*Proof.*
1. D_φ := R(φ; ·) is computable from φ (enumerate ρ). By the coding theorem (as used in GK24 l.447–450), K(x) ≤ log(1/D_φ(x)) + K(φ) + O(log|x|).
2. **NO φ.** With probability ≥ 1 − ε, x is in the promise and on the NO side, so K(x) ≥ |x| − 1 − β log|x| (as in §2). So log(1/D_φ(x)) ≥ |x| − K(φ) − β log|x| − O(log|x|) on that mass, and since log(1/D) ≥ 0 everywhere, **H(D_φ) ≥ (1 − ε)(|x| − K(φ) − β log|x| − O(log|x|))**.
3. **YES φ.** With probability ≥ 1 − ε, K(x) ≤ K^t(x) ≤ s, and at most 2^{s+1} strings have K ≤ s. Split on the indicator: **H(D_φ) ≤ 1 + (s + 1) + ε·|x|**.
4. Set k := s + 4 + ε|x|, which is **computable** from |x|, s and ε, and does not involve K(φ). YES φ gives H ≤ k − 2 < k − 1, and NO φ gives H > k + 1 under the length condition. So φ ↦ (R(φ; ·), k) is a Karp reduction from SAT to the complement of EA (AHT23's Definition 9).
5. EA is NISZK-complete (AHT23's Theorem 10, citing GSV; secondary), NISZK ⊆ SZK ⊆ AM ∩ coAM (GK24 l.296, citing [17, 14, 1]), and SZK is closed under complement. So NP ⊆ coAM. ∎

**The gaps, as pre-registered:**
- **(i) Error mass:** handled by the (1 − ε) factors. The YES bound charges the ε-mass at the full ε|x|.
- **(ii) EA's form:** Shannon entropy, additive gap 2 (AHT23's Definition 9). The gap in step 4 exceeds 2 by the length condition. ✓
- **(iii) Computable versus samplable:** D_φ is exactly computable from φ by enumerating the finitely many ρ. The coding theorem needs only a computable D (GK24 uses it for samplable D). ✓
- **(iv) Padding / K(φ)**, the reviewer's precision: the condition involves K(φ), while the threshold k does not, so the Karp reduction is well defined. Padding φ raises |φ| but not K(φ), so it cannot help.
  - **The escape class is compact reductions: |x| ≤ (K(φ) + s + O(log|x|))/(1 − 2ε).** LP22 is not compact (n⁴ against n log n; Y1′). **No compact reduction from SAT is known to us**, and we did not search specifically.

**Relation to the literature.** Flag E is GK24's mechanism, traded differently: constant error ε plus the length condition, in place of GK24's failure ≤ 1/p(t_R). SS22 covers constant error under honesty and an ω(log n) gap. **Flag E is not a new theorem.** At most it is a variant with different side conditions, labelled ours-elementary.

**The barrier, as it now stands** (the ruling's item 3, assembled from §2 and §3). There is no randomized poly-time many-one reduction from SAT to MK^tP[s]|Q^t_β with s ≤ n − 2 − β log n, unless NP ⊆ coAM (so PH = Σ₂^p), whenever **any one** of the following holds:
- (a) failure ≤ 1/p(t_R) (GK24's Theorem 5, via O);
- (b) the reduction is non-adaptive and polynomially honest, and s ≤ n − ω(log n) (SS22's Theorem 3, via O);
- (c) Flag E's length condition holds, at constant error.

**Consistency checks (written proofs).**
- **The identity on random strings.** All three statements have "a reduction from SAT (or from a decidable L)" as their hypothesis. The identity is a map from MK^tP[s]|Q to itself, and that promise problem's promise is undecidable (Q involves K), so it is not a decidable L. None of the statements applies, and the barrier is silent. ✓
- **LP22.** Its target is conditional McK^tP, not MK^tP. Read unconditionally, its outputs are not in Q^t_β (depth Ω((n/γ)·log n), Y1′ §2.3), and its NO outputs are not K-random (K(A | z) = O(n log n), Y1′ §2.1). So the hypothesis of O fails ("outputs in the promise on a 1 − ε fraction"), and neither GK24 (which concerns *unconditional* MKP) nor Flag E applies. The barrier is silent. ✓

## 4. The escapes (item 4 of the ruling): where the door still is

| escape | status (verified or proved) | what it means |
|---|---|---|
| **Top threshold s = n − 2** (LP23's Theorem 1.1, second bullet: OWF ⟺ MK^tP[n−2]\|Q^t_β ∉ ioBPP) | **All three barriers fail.** O needs s ≤ n − 2 − β log n. SS22 needs an ω(log n) gap, but the promise's K-gap here is ≤ β log n + 1. Flag E's YES bound s + 2 + ε\|x\| ≈ \|x\| meets the NO bound. | **The door.** A reduction into the top-threshold version must separate YES from NO by only O(log n) bits of K. That is exactly the regime where SS22 shows randomized non-adaptive reductions reach all of NEXP. |
| **LP25's boundary promise** | **Immune:** its NO side (K^{t₂} ≥ n − 1) has no depth promise, so NO outputs need not be K-random and neither O nor Flag E starts; its thresholds sit at n − 2 versus n − 1 (and n − log n), an O(log n) regime, so SS22 does not apply. The stated design motive is decidability and naturality (l.108–114), **not** barrier-avoidance. | **The door, in a second form**, at the same regime |
| **Adaptive (BPP-Turing) reductions** | LP23's OWF-hardness notion requires only "Π decided by efficient attackers ⇒ all poly-time functions invertible" (l.86–99), so adaptive reductions suffice for the holy grail. SS22: adaptive is "an interesting open question"; GK24 treats many-one (Theorems 5–8) and non-adaptive (Theorems 1, 2, 4) reductions only. | **Open door** |
| **Non-explicit / non-black-box arguments** | Allowed by LP23's definition (l.92–93: "even non explicit reductions") | **Open door**, with no technique on the record |
| **Compact reductions** (\|x\| ≲ K(φ) + s) | escape Flag E; still caught by GK24 at tiny error, and by SS22 if honest at s ≤ n − ω(log n) | a narrow door; none known |
| **Conditional / oracle problems** (Hirahara STOC'20: MINcKT^SAT; LP22: McK^tP) | NP-hard under deterministic or randomized reductions, and outside these barriers | **not LP23's problem.** A worst-case OWF characterization for a conditional or oracle version is not stated in anything read. |

**Proposition H (conditional; ours; a sketch, labelled).** Suppose SS22's NEXP-hardness reduction (Theorem 3, second part), for some L ∈ NEXP, tolerates any oracle within c·log n of K, and with high probability makes only queries q with K^t(q) − K(q) ≤ c·log|q| for a fixed polynomial t. Then answering its queries with K^t (computable in P^NP by binary search) decides L. So L ∈ BPP^NP ⊆ Σ₃^p.
- **So, unless NEXP ⊆ Σ₃^p, the O(log n)-gap reductions that do exist query deep strings.**
- Hiding is depth again, now at the powerful end.
- *Not verified:* the constant c of SS22's converse and the depth of its queries; this needs Hirahara STOC'20's construction. Recorded as a check, not a result.

## 5. Arm (b) and "hiding is depth", stated exactly

- **Flag W stands:** a reduction never holds the witness. So a YES side compressible "for a non-hidden reason" means low YES-entropy against high NO-entropy.
- **At thresholds s ≤ n − 2 − β log n** that is Flag E's (and GK24's) case, and it collapses PH.
- **At the top threshold**, the YES and NO entropies can both be ≈ |x|, differing in K by O(log n). There, the construction shape needs:
  1. YES and NO outputs both near-random, with entropy ≈ |x| on both sides;
  2. YES outputs compressible by ≥ 2 bits in K^t, NO outputs not compressible by 1 bit;
  3. all outputs non-deep.
  - No reduction read meets (1)–(3).
  - Proposition H suggests that the known O(log n)-gap reductions violate (3).
- **"Hiding is depth" is the evasion, not the barrier.** Planted reductions (LP22) make NO outputs low-K and deep, which keeps entropy equal on YES and NO and so escapes the entropy/SZK argument. The low-depth promise removes exactly that evasion, **except at the top threshold**, where the entropy argument has only O(log n) bits to work with.

## 6. Priors against outcome

| | Y2a | Y2c | Y2b |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 30 → 45 | 50 → 40 | 20 → 15 |
| mine | 45 | 40 | 15 |
| **outcome** | **✓ as known** (GK24 Theorems 5–6; SS22 Theorem 3), applied to LP23's promise via O | | the construction shape is stated only for the top threshold (§5); not met |

## 7. Misses and corrections

- **No outcome miss.** "Y2a-as-known" was named as likeliest by the reviewer and held.
- **Citation correction (the reviewer's list):** Allender–Hirahara 2017 (MFCS; ToCT 2019) is not the SZK-barrier source; its abstract concerns NP-intermediateness under OWF and DET-hardness. The SZK/NISZK statements are SS22, AHT23 and GK24. GK24 was not on either side's list, and the search found it. Scoring is the reviewer's to make.
- **The practice line held:** Flag E was put beside the literature before being called new, and it is recorded as known.

## Ceiling

Y2 proves nothing about P vs NP or OWF. It locates the door of LP23's holy grail more exactly. **Many-one reductions into the low-threshold promise are barred (NP ⊆ coAM) in three overlapping regimes. What remains open is the top threshold / boundary regime (an O(log n) K-gap) and adaptive or non-explicit reductions.**

## Formal record

Untouched (the author's decision).
