# X1: IP2 ∉ poly-size LTF∘LTF — the first attempt. Report

*Run 2026-09-10 on branch `x1-ip2-ltf2`, on the author's go ("Draft and run X1, push after merge"), against the pre-registration (11a1c56), accepted by the reviewer. The reviewer adopted Flag W and counts its swapped (c) as a slip; Flag S is the centre of the run; priors X1a 65 / X1b 20 / X1c 15. g1, g5, g8 and g9 applied. X1 proves nothing. It names the sub-obstacle and the smallest open lemma.*

## 0. Outcome

**X1a.** The sub-obstacle is named, and so is the smallest open lemma. Both are stated by Chattopadhyay–Mande themselves, which matches the program's pattern: the frontier was already mapped by the field, and our work is locating it exactly.

- **Flag S resolved: S-yes qualitatively, but not the full "ruled out".**
  - A *linear-size* THR∘THR formula computes a function of sign-rank 2^{Ω(n^{1/4})} (Chattopadhyay–Mande). So sign-rank is **not** polynomially bounded on the class, and it cannot be used the way Forster et al. use it for THR∘MAJ.
  - Sign-rank **survives quantitatively.** IP2 has sign-rank 2^{Ω(n)}, so an upper bound of 2^{o(n)} on the sign-rank of every poly-size THR∘THR function would already give IP2 ∉ THR∘THR. This is Chattopadhyay–Mande's own open question.
  - The reviewer's S-yes branch ("sign-rank is ruled out") is therefore refined: it is ruled out as a *polynomial* measure, and remains open as a *2^{o(n)}* measure.
- **The smallest open lemma (L1):**
  > **every polynomial-size THR∘THR circuit, under the natural partition, has sign-rank 2^{o(n)}.**
  - Known toward it, in the negative direction: 2^{Ω(n^{1/4})} is attained (Chattopadhyay–Mande).
- **A necessary step, weaker than L1 (L0), also stated by Chattopadhyay–Mande:** size lower bounds for *decision lists of exact thresholds* computing an explicit function. That subclass of THR∘THR "already inherits the curse of large sign-rank."
- **X1b: no.** No partial repair for case (iii) was found. The one post-2016 result on IP2 itself (Amano 2020) adds *upper* bounds and an LTF∘SYM lower bound, not an LTF∘LTF repair (§2).
- **X1c: not scored** (§5), as the ruling instructed.

## 1. Sources read in this run

- **Chattopadhyay–Mande**, "A Short List of Equalities Induces Large Sign-Rank", SIAM J. Comput. 51(3) (2022), 820–848; FOCS 2018; earlier titled "Weights at the Bottom Matter When the Top is Heavy". Primary, the CWI open copy.
- **Amano**, "On the Size of Depth-Two Threshold Circuits for the Inner Product Mod 2 Function", LATA 2020. Primary, the PMC HTML. The math is images, so the abstract's formulas were read as images (M1–M15).
  - **A web-summarizer fabrication was caught.** The WebFetch summary gave "O(2^{n/2})", "O(n^13)" and "Ω(n^1.34)". The images read O(1.682^n), O(1.899^n) and Ω((1.5−ε)^n). This is the third such fabrication in the program, after the two in M5 and A4. Nothing from the summary is used.
- **Hatami–Hatami–Pires–Tao–Zhao**, "Lower Bound Methods for Sign-rank and their Limitations", ECCC TR22-079. Primary, abstract only.
- **Sherstov–Wu**, "Near-optimal lower bounds on the threshold degree and sign-rank of AC⁰", arXiv:1901.00988. Primary, abstract only.
- **Kane–Williams**: carried from N1.
- **Not reached:** Hajnal et al., Nisan, Forster, Forster et al., Goldmann–Håstad–Razborov, Hansen–Podolskii. They are stated as quoted by Chattopadhyay–Mande, Amano or Kane–Williams.
- **Unverified and unused:** a search summary's "2^{n^{1/3}}" sign-rank bound for an LTF-of-LTF function. It was not found in any text read.

## 2. (a) The floor, with the weight column

The depth-2 structure, from Chattopadhyay–Mande (l.175–190 and the conclusion). Here LT̂_d is poly-weight depth d, LT_2 = THR∘THR, and the equalities and inclusions are Goldmann–Håstad–Razborov's except the new strict one:

  LT̂₁ ⊊ LT₁ ⊊ **LT̂₂ = MAJ∘THR ⊊ THR∘MAJ ⊊ LT₂** ⊆ LT̂₃.

The last strict inclusion, THR∘MAJ ⊊ THR∘THR, is Chattopadhyay–Mande's. IP2 ∈ LT̂₃ with O(n) gates.

| Result (as stated by) | Class | Bounded weights | Unbounded | Statement | What it uses |
|---|---|---|---|---|---|
| Hajnal et al. (KW; CM; Amano) | MAJ∘MAJ = LT̂₂ | both | — | IP2 needs 2^{Ω(n)} | discriminator lemma (top) and discrepancy (bottom) |
| Nisan (KW; Amano) | MAJ∘LTF | top | **bottom** | IP2 needs exponential size | "a communication complexity argument"; GHR: MAJ∘THR = LT̂₂ |
| Forster et al. (KW; CM Lemma 2.11) | THR∘MAJ | bottom | **top** | "computed by a THR∘MAJ circuit of size s. Then sr(M_F) ≤ sn"; with Forster, IP has sign-rank 2^{Ω(n)} | sign-rank: bounded-weight bottoms |
| Goldmann–Håstad–Razborov (KW) | LTF∘LTF | — | both | IP2 needs Ω(n/log n) gates, and LTF∘LTF ⊆ MAJ³ | — |
| Kane–Williams | LTF∘LTF | — | both | Andreev's function needs Ω(ε³n^{3/2}/log³ n) gates | random restrictions, Littlewood–Offord |
| Amano 2020 | THR∘SYM | — | top | IP2 needs Ω((1.5−ε)^n), improving the sign-rank bound Ω(√2^n/n) | the dual of an LP (Amano, MFCS '05) |
| Amano 2020 (upper bounds) | THR∘THR / MAJ∘THR | — | — | IP2 ∈ THR∘THR of size O(1.682^n); MAJ∘THR of size O(1.899^n) | computer-found base formulas |

**Flag W confirmed.** Nisan's model is MAJ∘LTF, top bounded, so it repairs **(ii)**, arbitrary *bottom* weights. By GHR's MAJ∘THR = LT̂₂, bottom weight buys nothing under a light top. Forster et al.'s model is THR∘MAJ, bottom bounded, so it repairs **(i)**, an arbitrary *top* weight. The reviewer's (c) had them swapped; **the reviewer's slip**, as it asked.

**The IP2 gap itself:** Ω(n/log n) gates (GHR) against O(1.682^n) (Amano). Amano, verbatim: "It is a long standing open question whether [IP] has a polynomial size depth-two threshold circuit with unbounded weights threshold gates in both layers."

## 3. (c) Step by step: the first failing step, and the repair

We take the MAJ∘MAJ proof as a two-step template. **This template is ours, labelled; g5 at sketch level.**
1. **Top step:** if a gate with weights summing to W computes f from bottom gates g_j, then some g_j has correlation at least 1/W with f (discriminator).
2. **Bottom step:** each g_j has correlation at most s·2^{−Ω(n)} with IP2. A small-weight threshold is a union of few rectangles, and IP2 has discrepancy 2^{−Ω(n)}.

- **(ii) Bottom weights arbitrary, top light.**
  - *The first failing step is 2:* an arbitrary-weight bottom gate is not a union of few rectangles.
  - *Repair, verified as stated:* Nisan's communication argument, and GHR's MAJ∘THR = LT̂₂. **Repaired.**
- **(i) Top weight arbitrary, bottom light.**
  - *The first failing step is 1:* with W exponential, the correlation guaranteed to some g_j is 2^{−Ω(n)}, which step 2 no longer contradicts.
  - *Repair:* Forster et al. change the measure from correlation to sign-rank. A THR∘MAJ circuit of size s has sr ≤ sn (CM Lemma 2.11), and IP has sign-rank 2^{Ω(n)} (Forster, as stated in CM l.194). **Repaired.**
- **(iii) Both arbitrary.**
  - *Step 1 fails, as in (i).*
  - *The sign-rank repair fails at its own first step.* The sr ≤ sn bound needs bottom gates of small sign-rank *in combination*. Chattopadhyay–Mande show linear-size THR∘THR reaches sign-rank 2^{Ω(n^{1/4})}, so no poly(s) bound exists.
  - **No repair. This is the sub-obstacle.** In Chattopadhyay–Mande's words (§1.4):
    - the natural unbounded-error protocol samples a bottom gate in proportion to its weight, and "ε can be inverse exponentially small in the input size";
    - it would need "a small cost randomized protocol for the bottom THR gate that errs with probability significantly less than ε";
    - "there does not seem to exist any such efficient randomized protocol for THR, when ε = 1/2^{n^{Ω(1)}}";
    - "The simplest such canonical function is Equality."
  - **The sub-obstacle, named:** *a heavy top gate leaves only an exponentially small advantage. A heavy bottom gate (Equality, an exact threshold) can be computed by randomized protocols only at a cost that grows with log(1/error). Composed, they make both known measures, correlation/discrepancy and polynomial sign-rank, fail at once.*

## 4. (b) The candidate lemmas

- **L1 (Chattopadhyay–Mande's open question, verbatim):** "Is it possible that the sign-rank of all functions in THR∘THR is 2^{O(n^ε)} for some constant ε < 1? Even an upper bound of 2^{o(n)} is enough to show IP is not in THR∘THR."
  - *Known:* 2^{Ω(n^{1/4})} is attained within THR∘THR (CM Theorem 1.1). Sherstov–Wu's exp(Ω(n^{1−ε})) sign-rank is for AC⁰ circuits. Their membership in poly-size THR∘THR is not stated in the text read (g10). If they were members, it would still be 2^{o(n)}, so it would not refute L1.
  - *What would refute L1:* a poly-size THR∘THR function of sign-rank 2^{Ω(n)}. CM: "finding a function of sign-rank 2^{Ω(n)} would also be quite interesting!"
- **L0, a necessary step, weaker (CM conclusion):** "can we prove strong lower bounds on the size of decision lists of exact thresholds for computing an explicit (say, in NP) function? This is a subclass of THR∘THR." CM also note: "Proving lower bounds on the size of such decision lists is a necessary step for proving lower bounds against both THR∘THR circuit size and PMA communication cost."
  - Hansen–Podolskii (CM Theorem 2.7): THR∘ETHR of size s ⊆ THR∘THR of size 2s.
- **Per Flag R.** L1 is class-wide. An IP2-specific route would need a measure that separates IP2's 2^{Ω(n)}, the sign-rank of a bent function, from THR∘THR, and that is not sign-rank itself. None is stated in the sources read (g8).
- **The limits of the lower-bound side** (Hatami et al., abstract): "there are only three known methods for proving lower bounds on the sign-rank of explicit matrices". These are VC-dimension, Forster's margin method, and monochromatic-rectangle density. L1 is an *upper* bound on sign-rank for a circuit class, so those limits bear on refuting L1, not on proving it.

## 5. The fold-count reading (not scored, per the ruling)

The ruling: the reading "weight substitutes for at most one fold, and IP2 needs two" is tested only by whether the surviving measure tracks fold count.
- **If L1 holds**, sign-rank gives the reading a formal referent: the exponent of the sign-rank is 0 (poly) up to THR∘MAJ, strictly between 1/4 and 1 on THR∘THR, and 1 at LT̂₃ ∋ IP2. Arbitrary weights would then buy a strict but *partial* fold. GHR (LT₂ ⊆ LT̂₃) and CM (THR∘MAJ ⊊ LT₂) already show the partial fold as containments.
- **Without L1 there is no referent yet**, and the reading is not scored.
- **An observation, not a score:** CM's F_n = OMB∘OR∘XOR₂ has three Boolean nestings and is computed by linear-size THR∘THR. Heavy weights absorb Boolean nesting; ODD-MAX-BIT is a single heavy threshold. So fold count in the Boolean basis is not the depth measure for threshold circuits. Whether any measure counts folds here is exactly L1.

## 6. Priors against outcome

| | X1a | X1b | X1c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 60 → 65 | 15 → 20 | 25 → 15 |
| mine | 65 | 20 | 15 |
| **outcome** | **X1a** | | not scored |

**Misses:**
- *My Flag S wording*, "sign-rank may be refuted as the measure", was too strong. It is refuted only as a polynomial measure, and CM's quantitative question keeps it alive.
- *The reviewer's slip:* the (c) repair assignment (Flag W).

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b.

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as X1a.** The third fabrication is recorded as caught. Reading the math images, not the summary, is the practice. The misses stand as written: Flag S's "may be refuted" is mine, and the (c) swap is the reviewer's.

1. **L1 is the attempt's result.** "Every poly-size THR∘THR circuit has sign-rank 2^{o(n)}" (Chattopadhyay–Mande §8). Its status is two-sided: 2^{Ω(n^{1/4})} is attained, and a 2^{Ω(n)} example would refute it. It is the smallest open lemma the program has produced at any layer that meets all three of these conditions:
   - it is stated by the field;
   - it would settle a named fold statement (IP2 ∉ THR∘THR);
   - it has a named necessary sub-step (L0, lower bounds for decision lists of exact thresholds).
2. **The fold measure at this layer is the sign-rank exponent, not Boolean depth.** Chattopadhyay–Mande's F_n has three Boolean nestings and linear THR∘THR size, so heavy weights absorb Boolean nesting outright. The exponent runs 0 (up to THR∘MAJ) → [1/4, 1) (THR∘THR, if L1) → 1 (IP2). This is an observation that gives the nesting reading a candidate referent *conditional on L1*, and nothing more.
