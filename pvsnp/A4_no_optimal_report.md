# A4: no optimal proof system — what is known, and whether the barriers reach it. Report

*Run 2026-09-10 on branch `a4-no-optimal`, on the author's go ("Draft and run A4, push after merge"), against the pre-registration (49dc95a), accepted by the reviewer with all four flags and my priors (O1 55 / O2 35 / O3 10). A4 proves nothing. g1, g8, g9, g10, g11 and g12 applied. Every quotation is from a text read in this run.*

## 0. Outcome

**O1.**
- "No optimal proof system for TAUT" is **blocked by relativization in both directions**. This holds for **length-optimality**, the notion CON^N needs, and also for p-optimality. Each direction is verified from a primary that constructs the oracle.
- **No non-relativizing partial result toward non-optimality for TAUT** was found.

The path ends at a named open problem that carries the same barrier as the object-level one. Per Flag V, this is **consistency with the RE reading, not progress**.

**One finding beyond the pre-registration.** The endpoint is not even a *believed* conjecture in the way NP ≠ coNP is:
- "it is unclear whether a negative or positive answer is to be expected [BS11, Kra19]";
- "no widely believed structural assumption (like NP ≠ coNP) is known to imply the (non)-existence of optimal proof systems [Hir10, BS11]" (Egidy–Glaßer).

## 1. Sources read in this run

- **Ben-David–Gringauze**, "On the Existence of Optimal Propositional Proof Systems and Oracle-Relativized Propositional Logic", ECCC TR98-021. Primary; the math is in Type 3 fonts, so pp. 1–3, 7, 8 and 10 were read as rendered images.
- **Khaniki**, "New relations and separations of conjectures about incompleteness in the finite domain", arXiv:1904.01362. Primary. My working attribution, "Dose–Glaßer", was wrong. The author is Erfan Khaniki.
- **Egidy–Glaßer**, "Optimal Proof Systems for Complex Sets are Hard to Find", arXiv 2408 (local text). Primary for its oracles O1 and O2, and a survey for the rest.
- **Krajíček**, "Diagonalization in proof complexity", Fund. Math. 182 (2004). **Only the EUDML abstract was reached.**
  - The IMPAN PDF link loops on redirects (curl error 47).
  - The class names are dropped in EUDML's HTML and BibTeX, so they stay **UNVERIFIED**.
  - A web-search summary again supplied a class name ("P ≠ coNP") that is not in the text. It is rejected, as in M5.
- **Krajíček–Pudlák 1989 (KP89)** and **Köbler–Messner–Torán 2003 (KMT03)**: not reached. Their statements below are "as stated by" the sources above.

## 2. (a) The statement family

**Definitions** (Ben-David–Gringauze, Definition 3, p. 2):
- "f **simulates** g if there exists a polynomial p s.t. for every w ∈ {0,1}*, there exists w′ ∈ {0,1}* of length ≤ p(|w|) s.t. f(w′) = g(w)."
- "f **p-simulates** g if such a w′ can be found efficiently."
- "A propositional proof system is called **optimal** if it simulates every other propositional proof system." (p-optimal: p-simulates every other.)

Khaniki (l.160–165) calls simulation "non-uniform p-simulation" ("Normally, non-uniform p-simulation is called simulation in the literature"). So his "nonuniform p-optimal" = optimal, and his **CON^N** = "there is no (non-uniform) p-optimal proof system for TAUT".

**Logical equivalents** (Khaniki, Theorems 2.3 and 2.4, citing KP89; consistent with Pudlák 2017 as verified in M5):
- "There exists a nonuniform p-optimal proof system for TAUT" ⟺ "There exists T ∈ 𝒯 such that for every S ∈ 𝒯, the shortest T-proofs of Con_S(n̄) is bounded by a polynomial in n".
  - So **¬CON^N ⟺ an optimal system exists**, as a ∃T ∀S statement.
- **The reflection-form endpoint, made exact** (Khaniki, Theorem 3.4.1): "For every T ∈ 𝒯, there exists S ∈ 𝒯 such that the T-proofs of Σ^b_1RFN_S(n̄) are not polynomially bounded in n" ⟺ "Σ^q_1-TAUT does not have a nonuniform p-optimal proof system".
  - **So RFN^N_1 is non-optimality for Σ^q_1-TAUT, not for TAUT.** This closes A3's question about RFN^N_1's form.

**Sufficient conditions for existence** (the attribution differs by source; g10, no merging):
- **Egidy–Glaßer, stating KP89:** "NE = coNE implies the existence of optimal proof systems for TAUT, and E = NE implies the existence of p-optimal proof systems". KMT03 "improve this result to NEE = coNEE for optimal and EE = NEE for p-optimal".
- **Ben-David–Gringauze** (p. 3) state the NEE/EE version as "Theorem [Meßner and Torán [MT97]]". They credit the NE = coNE version to "an earlier result of Pudlák [Pu84]", not to KP89.
- **Correction to M5's record:** the NE = coNE ⇒ optimal attribution is **KP89 per Egidy–Glaßer, Pudlák 1984 per Ben-David–Gringauze**. Both are recorded.
- **Ben-David–Gringauze's own contribution:** "for every slim class an appropriate collapse entails the existence of an optimal propositional proof system". P, E and EE are slim.

**Necessary conditions** (Egidy–Glaßer, stating):
- Razborov 1994: optimal for TAUT ⇒ complete sets in DisjNP. Ben-David–Gringauze p. 3 state the same: "a complete (under polynomial reduction) problem in DisNP".
- KMT03: optimal and p-optimal systems for sets in the polynomial hierarchy ⇒ complete sets for "UP, NP ∩ coNP, NP ∩ SPARSE and probabilistic classes such as ZPP, BPP, and AM".
- Beyersdorff–Köbler–Messner 2009 and Pudlák 2017: p-optimal for SAT ⇒ complete sets for TFNP.

**Variants with positive answers** (Egidy–Glaßer, stating):
- Cook–Krajíček 2007: "(p-)optimal proof systems for TAUT exist if we allow one bit of non-uniform advice".
- Beyersdorff–Köbler–Müller 2011 generalize this "to arbitrary languages".

## 3. (b) Relativization, notion by notion (Flag R)

**The relativized notion** (Ben-David–Gringauze §4, p. 7). Formulas get an oracle connective X, with v̄(X(α₁,…,αₙ)) = 1 iff the bit string (v̄(α₁),…,v̄(αₙ)) ∈ 𝒜. Taut_𝒜 is the set of 𝒜-tautologies. "A propositional proof system w.r.t. 𝒜 is a function f : {0,1}* → Taut_𝒜 [onto] such that f ∈ FP^𝒜."
- Lemma 1: SAT_𝒜 is NP^𝒜-complete.
- Corollary 2: "[A Relativised Cook-Reckhow Theorem] For every oracle 𝒜, there exists an 𝒜-relativized super propositional proof system iff NP^𝒜 = CoNP^𝒜."

| Direction | Notion | Oracle and statement | Source |
|---|---|---|---|
| **optimal exists** | optimal and p-optimal, TAUT_𝒜 | any 𝒜 with NP^𝒜 = coNP^𝒜 gives a super system, which is trivially optimal (Flag R; one line from Corollary 2) | Ben-David–Gringauze Corollary 2 (primary); Baker–Gill–Solovay supplies such 𝒜 (not re-read) |
| **optimal exists** (non-trivially) | p-optimal | oracle V: "Relative to the first oracle, a p-optimal proof system for TAUT exists, but the class of disjoint CoNP problems does not have complete problems" | Khaniki l.56–57, Theorem 5.1 (primary: E^V = NE^V, with KP89 relativized) |
| **no optimal** | **optimal (length)**, TAUT_𝒜 | "for every fat class there exists an oracle relative to which [collapse ⇒ optimal] fails". Theorem 2: 𝒜 "relative to which CoNF = DF and yet there is no optimal propositional proof system" | Ben-David–Gringauze, abstract and Theorem 2, p. 8 (primary, proof given) |
| **no optimal** | **nonuniform p-optimal = optimal (length)**, TAUT^W | Theorem 5.2: "There exists an oracle W such that there is no nonuniform p-optimal proof system for TAUT^W, but TFNP^W = FP^W" | Khaniki, primary, proof given (forcing, following Buhrman et al. [14]) |
| **no optimal** | optimal, with PH infinite | O1: "No set in PSPACE \ NP has optimal proof systems and PH is infinite". Hence "relativizable methods can not prove that an infinite PH implies the existence of optimal proof systems for TAUT or QBF" | Egidy–Glaßer, primary for O1; the TAUT consequence as they state it (l.165) |

**Verdict on (b).** Oracles exist in both directions for the **length-optimal** notion CON^N needs, and a fortiori for p-optimality: no optimal ⇒ no p-optimal. The no-optimal direction comes from constructed oracles in two independent primaries (Ben-David–Gringauze; Khaniki), plus a third that adds an infinite PH (Egidy–Glaßer). **O2's precision clause does not trigger:** the no-optimal oracles are not confined to p-optimality.

**What the barrier blocks (Flag V).** Only relativizing techniques: diagonalization and simulation that go through unchanged relative to every oracle. Ben-David–Gringauze say so directly about sufficient conditions (abstract): "As the proofs of all the known sufficiency conditions … carry over to the corresponding oracle-relativized notions, this result shows that no extension of our sufficiency condition to non-slim classes can be obtained by the type of reasoning used so far."

## 4. (c) Natural proofs and algebrization

Not found (g8). One web search ("optimal proof systems" with "natural proofs" or "algebrization") returned only the general barrier literature (Aaronson–Wigderson). Nothing addressed optimal proof systems. None of the primaries read here mentions either barrier. The search is recorded; the absence is not a claim that no such result exists.

## 5. (d) What is known non-relativizingly toward non-optimality

**Nothing found for TAUT.** The record, as stated by Egidy–Glaßer:
- **Unconditional non-existence, only above TAUT:** "By Messner [Mes99, Mes00], all coNE-hard sets and even all coNQP-hard sets have no optimal proof systems." TAUT is not known to be coNQP-hard. Whether Messner's argument relativizes is not stated in the text read (g10). Its diagonal form suggests it does; that is not asserted.
- **Non-optimality implies separation:** "A negative answer to Q1 or Q2 implies NP ≠ coNP" (Messner 2000). This is the known *consequence*, not a partial result toward it.
- **No hypothesis toward it:** "no widely believed structural assumption (like NP ≠ coNP) is known to imply the (non)-existence of optimal proof systems [Hir10, BS11]."

So the conditional results of (a) plus Messner's above-TAUT non-existence are the whole record reached. **No O3 lead.**

## 6. (e) The self-reference reading, tested once

The reading: an optimal system is a universal simulator, a layer containing all layers. Does any theorem turn that universality against itself?

The one place found where a diagonal touches optimality is **Krajíček's diagonalization**, from its abstract (EUDML; class names UNVERIFIED): "We prove that at least one of the following three conjectures is true: ∙ There is a function f: {0,1}* → {0,1} computable in [class] that has circuit complexity 2^{Ω(n)}. ∙ [class] ≠ co[class]. ∙ There is no p-optimal propositional proof system."

**Flag D holds.**
- "No p-optimal" is **one disjunct of three**, not a consequence of the diagonal. The diagonal proves the disjunction.
- It concerns **p-optimality (CON)**, not length-optimality (CON^N).
- It gives no leverage toward CON^N by construction: it is compatible with every oracle world in which one of the other two disjuncts holds.

The existence-side analogue, Cook–Krajíček's one-bit-advice optimal systems (§2), shows universality *can* be achieved once one bit of advice is allowed. The universal-layer reading therefore does not by itself point to non-existence.

**The self-reference reading is dropped**, as the reviewer set it: no theorem found uses universality against itself beyond a disjunct.

## 7. Readout (labelled; Flag V)

**The program's path, as A2–A4 leave it:**
1. The finite Gödel theorem with content for all systems is **CON^N = no optimal proof system for TAUT** (∀S ∃T).
2. It implies RFN^N_1 = no optimal system for Σ^q_1-TAUT (Khaniki 3.4).
3. That implies NP ≠ coNP (Pudlák 2017 Proposition 3.11).
4. **Barrier status:** relativization-blocked in both directions (§3), exactly as NP vs coNP is.
5. **Evidential status:** unlike NP ≠ coNP, not even the *believed* direction is settled (§0).

**The same-barrier observation, written as instructed.** The obstruction at the metamathematical layer ("does a universal simulating proof system exist?") has the same relativization barrier as the object layer ("does a polynomially bounded one exist?"). That is **consistent with the RE reading, a self-similar obstruction across layers, and it is not progress.** It adds no technique and no partial result. It also carries a weakness the object layer lacks: an open direction of belief.

## 8. Priors against outcome

| | O1 | O2 | O3 |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 65 → 55 | 25 → 35 | 10 → 10 |
| mine | 55 | 35 | 10 |
| **outcome** | **O1** | | |

**Miss recorded (mine).** My O2 weight (35) rested on Flag R's worry that no-optimal oracles might exist only for p-optimality. That did not happen: two primaries construct length-optimal ones. **Attribution slip recorded (mine alone):** I called arXiv:1904.01362 "Dose–Glaßer" before reading it. It is by Khaniki.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as O1.** Both attribution records stay as written, not merged:
- the Khaniki slip;
- NE = coNE ⇒ optimal credited to Pudlák 1984 (Ben-David–Gringauze) vs KP89 (Egidy–Glaßer).

Khaniki's Theorem 3.4.1, RFN^N_1 ⟺ non-optimality for Σ^q_1-TAUT, goes into the final page as the exact form of the chain's middle term.
