# The P vs NP program (R, M, A): final state

*2026-09-10. This page is written to be read on its own. It consolidates `pvsnp/R1`–`R5`, `M1`–`M5` and `A1`–`A4`, and supersedes neither `R_program_final_state.md` nor `M_program_final_state.md`, except where §8 corrects them. Every cited statement was checked against a source's own text or official abstract. "Secondary" means it was verified in another paper's text. Line numbers are in the phase reports.*

**Nothing here proves anything about P vs NP.** Two theorems of ours are proved (§2), and both are about weak proof systems. The attempt phase (§10) adds two elementary lemmas about threshold circuits. Everything else is verified location: where the problem sits, which theorems bound it, and which open statements it reduces to.

## 1. The question

The author's question was whether reverse engineering (RE) plus Gödel gives a path to P vs NP; the telos was "find a path". **The reviewer's reading, adopted throughout:** "find a path" means
1. **shrink**: reduce the question to the smallest verified sufficient condition;
2. **locate**: place that condition among known theorems and barriers;
3. **attempt**: pre-register an attempt only where a statement is small and open.

The R-program shrank. The M-program located at the metamathematical layer. The A-program attempted at the bottom rung and then mapped the endpoint.

**Amendment (N1): the intuition was mis-mapped, then corrected.** The program treated "folding" as **composition**: OWF chains, and R3's "fold". The author's intuition is **nesting**: problems fold into problems, a statement about a statement, one quantifier or one layer of depth per fold. Composition does not accumulate alternation; nesting does. The reviewer records this as its **ninth premise miss**. `N1_fold_accumulation_report.md` maps the corrected reading. Its outcome was N1a and N1c together:
- **Accumulation is a theorem where the evaluator is unbounded.** Tarski, and the strict arithmetical hierarchy.
- **Circuit depth, proved.** The AC⁰ depth hierarchy (Håstad; average case, Rossman–Servedio–Tan). The majority depth 2 → 3 fold holds on the inner product IP2.
- **The bridge to PH is oracle-only.** It reaches the polynomial hierarchy only through oracle constructions: PH is infinite relative to some oracle, and relative to a random one (RST). Book's theorem transfers only *collapse* down from random oracles. So "folds accumulate" is proved in the black-box world, and its unrelativized form is PH strictness itself.
- **The smallest open fold** is *IP2 has no polynomial-size LTF∘LTF circuits* (Kane–Williams, open question 2), which is at once a size lower bound and a depth separation.

## 2. What we proved

Proved in these documents, with proofs in the reports (g5). None is about P vs NP.

- **A2, Theorem A (Res ⊬_poly rfn_CF).** Resolution has no polynomial-size refutations of the negated reflection principle of Circuit Frege. This is stated in Atserias–Bonet's SAT shape and holds for every complete, separated, polynomial-size encoding of "y is a CF-proof". The bound is superpolynomial in the formula size.
- **A2, Theorem B (Res(k) ⊬_poly rfn_Res(k+1), every k ≥ 1).** In particular Res(2) ⊬_poly rfn_Res(3). **SECONDARY tag:** the Res(k)/Res(k+1) hierarchy is taken from [SBI04, Seg05] as stated by Ben-Sasson–Nordström (arXiv:1008.1789); the primaries were not reached.
- **A2's method (Lemma 3): reflection ⇒ simulation for Res(k),** by restriction and literal substitution. If Res(k) refutes ¬rfn_T in size S, then Res(k) refutes every CNF that T refutes in size m, in size ≤ 2S + |¬rfn_T|. The method is Cook's RFN ⇒ p-simulation (Cook–Nguyen attribute the idea to Cook 1975). **Label: "C2, C1-adjacent"**: proved here, method classical, the instances not found stated.
- **M3's equivalence.** Take a Π₁ lower-bound sentence H at a fixed bound, and any Σ₁-sound theory T containing Robinson's Q. Then "T ⊬ ¬H" holds **iff** H is true. So on hardness sentences Gödel's move is a restatement: unprovability is the same problem as the lower bound.
- **M4's bound: compression changes the measure, not the ratio.** A self-referential sentence improves on the trivial proof-length bound by at most a polynomial, in the referring system's own measure. This holds in any Cook–Reckhow system, implicit ones included.
- **R2's density proposition.** Let S_k = {x ∈ {0,1}^n : K^t(x) ≤ k}. Then Pr_{x∼U_n}[x ∈ S_k] ≤ 2^{k+1−n}. Consequently, no argument built by exhibiting, sampling or conditioning on compressible strings can bear on mild average-case hardness under the uniform distribution. (Elementary; not claimed new.)

## 3. The four open statements the program ends on

### (i) The R-endpoint: mild average-case hardness of K^t

- **Statement.** For some polynomial t(n) ≥ (1+ε)n, every PPT algorithm fails to compute K^t exactly on at least a 1/p(n) fraction of uniform n-bit strings.
- **What implies what.** K^t mildly hard-on-average ⟺ one-way functions (Liu–Pass, CCC 2022, Theorem 1.1) ⇒ NP ⊄ BPP ⇒ P ≠ NP (Arora–Barak, Exercise 10.1, for OWF ⇒ P ≠ NP).
- **The sub-obstacle: compressibility vs density.** The closest technique (Hirahara, FOCS 2018) breaks a generator whose outputs must be compressible (Theorem 26's promise). Compressible sets have density ≤ 2^{−K^t(x)}, so a heuristic with two-sided error can err on the whole image. The argument survives only when K^t(x) = O(log n).
- **Repair condition, open.** A non-adaptive average-case instance checker for NP (Hirahara–Santhanam, ITCS 2022, Theorem 14).
- **Barrier status.** Non-adaptive black-box worst-to-average reductions of this kind give collapses (Bogdanov–Trevisan, SICOMP 2006). So any reduction must be adaptive or non-black-box.

### (ii) The self rung: Res(2) ⊬_poly rfn_Res(2)

- **Statement.** Res(2) has no polynomial-size refutations of the negated reflection principle of Res(2) itself.
- **Status.** Open; not found stated (g8) in Atserias–Bonet 2004, Pudlák 2020, Garlík 2020 or Cook–Nguyen.
- **Where it sits.** Frege, every extension of CF, and G_i p-prove their own reflection principles (Pudlák 2020, citing Buss 1991, Cook 1975, Krajíček–Pudlák 1990). Resolution and Cutting Planes do not (Atserias–Bonet, Theorem 11; Pudlák 2020, Theorem 3.11). Res(k) for k ≥ 2 and bounded-depth Frege F_d for d ≥ 1 are open (Pudlák's Problem 1).
- **Both known routes are blocked at verified steps:**
  - Atserias–Bonet's route needs *monotone feasible interpolation*. Atserias–Bonet p. 14: "Res(k) does not have monotone feasible interpolation".
  - Pudlák's Corollary 3.8 route needs *feasible disjunction*. Garlík 2020, Theorem 1: "For every integer k ≥ 2, Res(k) does not have the weak feasible disjunction property".
- **What fits the divide (post hoc, not confirmed).** Pudlák's own remark: a system proves its own reflection when its lines can express "a coded line of mine is satisfied by an assignment".
- **Barrier status.** The known interpolation-type barriers apply to both routes. No relativization question arises for a fixed weak system.

### (iii) No optimal proof system

- **Statement.** CON^N (Pudlák 2017): "For every S ∈ 𝒯, there exists T ∈ 𝒯 such that the lengths of S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n". This is equivalent to "there is no (length-)optimal proof system for TAUT".
- **What implies what.**
  - CON^N ⇒ RFN^N_1 ⇒ NP ≠ coNP (Pudlák 2017; the second step by Proposition 3.11, whose proof is a sketch).
  - **The exact form of the middle term:** RFN^N_1 ⟺ "Σ^q_1-TAUT does not have a nonuniform p-optimal proof system" (Khaniki, arXiv:1904.01362, Theorem 3.4.1).
  - CON^N ⇒ NE ≠ coNE, via "NE = coNE ⇒ an optimal system exists". That is KP89 per Egidy–Glaßer, and Pudlák 1984 per Ben-David–Gringauze (both recorded).
- **The instance located in M4 (conditional).** EF ⊬_poly Con_{iEF}(n). It is a CON^N⁺ instance only if iEF's theory proves Con_EF, and no source reached states that.
- **Barrier status: relativization-blocked in both directions, for length-optimality.**
  - No-optimal oracles: Ben-David–Gringauze, ECCC TR98-021, Theorem 2; Khaniki, Theorem 5.2; Egidy–Glaßer's O1, with PH infinite.
  - Optimal-exists oracles: any oracle with NP^A = coNP^A (the relativized Cook–Reckhow theorem); Khaniki's V.
- **Nothing non-relativizing** toward non-optimality for TAUT is known. Messner's unconditional non-existence covers only coNE-hard and coNQP-hard sets.
- **The direction of belief is open:** "no widely believed structural assumption (like NP ≠ coNP) is known to imply the (non)-existence of optimal proof systems [Hir10, BS11]" (Egidy–Glaßer).

### (iv) The smallest open fold: IP2 ∉ poly-size THR∘THR

- **Statement.** The inner product mod 2 has no polynomial-size depth-2 threshold circuits with unrestricted weights.
  - This is Kane–Williams' open question 2. Amano (2020) calls it "a long standing open question".
  - Known bounds: Ω(n/log n) gates below (Goldmann–Håstad–Razborov); O(1.682^n) above (Amano).
- **Two-level structure** (X1–X2; §10):
  - It is implied by **L1**: every poly-size THR∘THR circuit has sign-rank 2^{o(n)} (Chattopadhyay–Mande §8; 2^{Ω(n^{1/4})} is attained).
  - It implies **L0(IP2)**: IP2 has no polynomial-length decision list of exact thresholds. This is open.
  - L0(IP2) would follow from IP2 ∉ PMA^cc.
- **Sharpened by X3:** "IP2 has no polynomial-size exact-linear decision list of alternation depth ≳ n/log n."
  - *Known regime:* Podolskii–Prior 2025, Theorem 45. If Disc_U(f) ≤ d and f is approximately balanced, then every ELDL of alternation depth k computing f has size Ω(k·d^{−1/(2k)}). For IP2 this is superpolynomial for k = o(n/log n).
  - *Why it stops:* the recursion over alternation layers loses a multiplicative factor per layer.
  - Podolskii–Prior also write: "for the related model of exact linear decision lists, no strong lower bounds are known".
- **Barrier status: no known measure survives Equality** at unbounded alternation.
  - Sign-rank and discrepancy fail on Chattopadhyay–Mande's Equality list F_n.
  - Rectangle arguments fail because Equality violates the staircase lemma (CMMS Lemma 16).
  - What survives stops at linear length.
- **The Union Lemma (X4–X8).** It would push the known regime from o(n/log n) to ≈ 0.36n alternations, with re-absorption as the residual beyond that. Its status:
  - **Tight, for IP2 (poly(m)·2^{1.5n}): FALSE.** Witness: the n AND-rectangles, with Adv = 2^n − 3^n, a ratio of 1.061^n (X8). The ρ table is kept as the record of the tight form's per-block factor, with N = 2 first:
    - ρ(2) = 1.061;
    - ρ(4) = 1 and ρ(8) = 0.928 (exact);
    - ρ(16) ≤ 0.969, ρ(32) ≤ 0.961 and ρ(64) ≤ 1 (proved);
    - ρ(128) ≤ 1.0027 (open).
  - **Loose (poly(m)·2^{2n}√d, i.e. poly(m)·2^{1.75n} for IP2): the live lemma.**
    - It is **proved safe from every tensor union**: the per-block factor is ≤ 0.94 at N = 2 and ≤ 0.805 for N ≥ 8, decreasing (X8).
    - It is **open only for unions with exponential row-type fragmentation**. By the **narrowing lemma** (the reviewer's; proof: the fragmentation bound m·√K·2^{1.5n} is ≤ 2^{1.75n} whenever K ≤ 2^{n/2}/m²), it holds unless some block's row-type count exceeds 2^{n/2}/poly(n).
    - **X9's restatement of the open lemma:** *the bias version of Pitassi–Shirley–Shraibman's Theorem 29 for conjunctions of m co-blocky constraints: a lower bound on m in terms of |Adv(IP2, C)| rather than |C|.* This is uniform discrepancy of IP2 against m-query Equality-oracle conjunctions.
    - **Proved** (ours, from PSS Theorem 29 with the −1-rectangle theorem): covering either sign class of IP2 by blocky sets needs Ω(2^{n/2}) sets, so polynomially many constraints cannot make C monochromatic. The quantitative bias form is open.
    - **Methodological finding (X9):** at computable n the covering threshold 2^{(n−1)/2} lies below m, so numerics cannot test the loose Union Lemma; evidence must come from structure. The greedy B(n, m) values stay within a constant of 2^{1.75n}: 0.89, 1.04, 1.04 and 0.81 at m = n, for n = 4, 5, 6, 8. They exceed 3^n by 1.41 to 2.64. They are recorded with this design caveat.
    - No witness is known even there: block-Equality unions have K ≈ 2^n but advantage 0.
    - Lemma T′ (any f, m ≤ ½log(1/d)) and the fragmentation bound hold.
  - **The threshold consequence is unchanged:** linear alternation depth via the loose Union Lemma, with a re-absorption residual. Open. All gains so far are constant factors.
  - **What a proof must do (X6):** sum across row types before bounding. The operator-norm route is closed (X5, by the reviewer's counterexample), and every termwise bound is blind to cross-type cancellation.

## 4. The observation (a reading, not a theorem)

In every layer examined, the obstruction bears on *typical* objects, and *named* objects are cheap. Six instances were verified:
1. **R2:** compressible (nameable) strings are exponentially rare, so average-case arguments cannot use them.
2. **R4/R5:** few Yes instances make an errorless heuristic a usable test, and the same fact lets a two-sided heuristic hide its errors.
3. **M2:** systems prove their own lower bounds on *named* families (Davis–Robere), but no system efficiently proves hardness of *random* truth tables (Pich–Santhanam).
4. **Hrubeš (M5):** the named fixpoint extension is cheap to prove consistent; the conjecture needs reflection over all proofs.
5. **A1:** consistency concerns one named object, ⊥, and Resolution proves its own consistency cheaply. Reflection is soundness over all proofs, and there Resolution fails.
6. **A4:** the relativization barrier recurs at the metamathematical layer exactly as at the object layer. Per the ruling this is recorded **as consistency with the reading, not as progress**.

A2's Lemma 3 refines, but does not add to, instance 5: reflection of a *stronger* system reduces to a named separation, so the self rung carries the content. A3's self/cross divide was **not** counted (g12). It is about expressive power, not typical vs named.

## 5. What failed, and the theorem that failed it

| Idea | Failed by |
|---|---|
| Erasure as hardness (isolated inputs of random local functions) | Projection: every preimage set has size 2^{Ω(n)} w.h.p. (known; Applebaum's survey, §5.1) |
| Special-string diagonals (a self-generated distribution, conditioning on low K^t, a Gödel-style diagonal string) | R2's density proposition |
| Gödel's move on hardness sentences | M3's equivalence |
| The general "second incompleteness" reading (no system proves lower bounds against itself) | Davis–Robere: depth-d Frege proves strong lower bounds against itself on named families |
| Finite second incompleteness for all systems | Pudlák 2020 l.791–794: extensions of CF and Frege (Buss) p-prove their own reflection |
| The extension/reusability divide for self-reflection | The Frege row: no extension, yet it p-proves its own reflection |
| The self-reference reading of optimality ("an optimal system is a universal layer") | Krajíček's diagonal gives only a three-way disjunction, with "no p-optimal" as one arm; the class names are UNVERIFIED |

## 6. What would reopen it

Nothing else is live. Only one of the following would reopen the question:
- **For (ii):** a lower-bound method for SAT ∧ REF_Res(2) against Res(2) that uses neither monotone feasible interpolation nor feasible disjunction.
- **For (iii):** a non-relativizing argument toward non-optimality of TAUT.
- **For (i):** an average-case instance checker for NP, the repair condition for the compressibility-versus-density tension.
- **For (iv):** the bias version of PSS Theorem 29 for conjunctions of m co-blocky constraints: a lower bound on m in terms of |Adv(IP2, C)| (X9). Its natural route is named **X10** (not drafted, on the author's go only): **the bias-to-monochromatic bridge**, a density increment from bias A to a sub-cube of dimension n′ on which C is nearly monochromatic, where PSS applies.
  - Kill tests: the AND family must give n′ ≲ 2·log₂n; the block-Equality family must give nothing.
  - The reviewer's priors on record: the bridge fails at a named step 60 / nontrivial but below the threshold 25 / loose Union Lemma proved 15.

Anything opened is an attempt on (i), (ii), (iii) or (iv), pre-registered as such.

## 7. Calibration, both sides

### Counts, recounted from the reports

**The reviewer: 8 premise misses and 10 wrong outcome priors.**
- **Premise misses:**
  - seven in the R-program (listed in R_program_final_state §7);
  - the eighth in M1: Kurtz–O'Donnell–Royer named from memory and misplaced.
- **Wrong outcome priors:**
  - seven in the R-program (listed there);
  - the eighth: the general Gödel's-second reading, refuted by Davis–Robere (M3 pre-registration);
  - the ninth: S1 in A3, since strong systems p-prove their own reflection;
  - the tenth: the extension/reusability reading, pre-registered as a test in A3 and falsified on the Frege row.

**Me:**
- **R-program:** four wrong predictions or framings (listed in R_program_final_state §7), and the process slips recorded in the formal record's appendix.
- **M-program:**
  - M2: my A2 prior (50) missed the within-system case;
  - M3: my T1 prior (55) was wrong;
  - M5: M4's instance carried an unverified pair condition, since g10 was not applied in M4.
- **A-program:**
  - A1's "within reach of feasible interpolation" (A2 found the simpler route);
  - A4's O2 weight (35);
  - the Khaniki attribution slip (A4).
- **This page:** the R final-state overstatement corrected in §8.

The verbatim records follow, extracted by script from the phase documents. The script aborts if any anchor is missing.

**R-program (R_program_final_state.md §7):**

> **The reviewer:**
> - **Seven premise misses** about what the record or literature contained: the §6–§8 sections; §8's outcome; CostAxioms as a transcription item; "every derivation routes through cost"; the Lid witness; the pK^t characterization of derandomization; "program closed".
> - **Seven wrong outcome priors**: 27′; (xi); Theorem 13 via 14; the L1 exactness note; the constructivity of the counting result; "S_a ⇒ mild hardness is immediate"; the dense-image repair for R5, which the same counting that sets the §2 tension excludes.
>
> **Me:**
> - **Four wrong predictions or framings**: cost as per-method versus per-input; the location of R1's variant change; S_a refuted at every time bound, when padding needs t ≥ C·n²; R5's exact-versus-gap prediction.
> - **Process slips**, recorded in the formal record's appendix: six surface-text instances and two order-of-operations instances.

**R2 (R2_smallest_report.md):**

> - **The reviewer:** Flag 2's "immediate" was scored as the reviewer's sixth wrong outcome prior, and F3 of R1 as the sixth premise miss (per the ruling). Both are recorded here and not in the RE appendix, since the R-program stays outside the RE record.
> - **Me:** Flag 1 was overclaimed (see S_a above).

**R3 (R3_fold_report.md):**

> - **The reviewer.** Its strategy and test (c) were stated accurately. The Bogdanov–Trevisan hypothesis "unless NP ⊆ coNP/poly" is equivalent, by complementation, to the verified coNP ⊆ NP/poly. The AGGM citation needs the erratum note added in §4. That is a note, not a miss: the adaptive theorem was retracted and later re-proved.
> - **Me.** The pre-registration's F1 expectation held for the conjecture. The strategy result (F3) was the reviewer's addition.

**R4 (R4_door_report.md):**

> - **The reviewer:**
>   - The expectation about *what the code is used for* was confirmed, with the density ingredient added.
>   - "AGGM's poly-preimage case" is BB14's description of the part AGGM10 did not retract. AGGM's own adaptive hypothesis is computable or AM-verifiable preimage size (§1.1, l.90–101). This is a note, not a miss.
>   - D3 through (1d) did not occur.
> - **Me:** (1c) unknown and (1d) proved for random graphs matched the pre-registration. D1 held.

**R5 (R5_subobstacle_report.md):**

> - **Me:** (A) was right. (B)'s predicted location was wrong: the hardness already has a constant-factor gap.
> - **The reviewer:** the dense-image repair it proposed is excluded by counting, which refines the tension. At the reviewer's request it is counted as its **seventh wrong outcome prior**, since it was pre-registered as a repair. The novelty check it asked for found the fact already known, which was its instinct.

**M-program (M_program_final_state.md §7):**

> **M1:**
>
> > - **The reviewer:**
> >   - *Kurtz–O'Donnell–Royer*, named from memory, exists. Its content is a representation-independent *oracle* independence result, not a relative or strengthening of Ben-David–Halevi, which is where it was placed. That is a premise miss, the **eighth**.
> >   - "Σ₁-sound" should be Σ₁-complete (precision b). That is a note.
> >   - The per-system Π₁ layer was right, with precision (a).
> > - **Me:** the pre-registered L2 risk (access to 1990s papers) materialized as expected.
>
> **M2:**
>
> > - **The reviewer:**
> >   - the fixed-point framing of KP'89 did not survive at the primaries (A3, pre-registered as Flag O);
> >   - the stall was expected at Frege, but the verified source places it lower;
> >   - the "one layer up" prediction fails, and in a direction neither side listed.
> >
> >   These are outcomes, not premise misses. Its note on Flag P was exactly right.
> > - **Me:** Flags P and O were right. My A2 prior (50) missed the within-system case. Davis–Robere was not anticipated by either side.
>
> **M3:**
>
> > - **The reviewer:** its three-object precision located the failure exactly. Its T1 expectation did not occur; T3 did, through Flag G. That is an outcome, not a premise miss.
> > - **Me:** Flag G was right. My T1 prior (55) was also wrong.
>
> **M4:**
>
> > - **The reviewer:**
> >   - its catch (b) was right, and sharpened here;
> >   - its sharpened (c) led directly to CON^N⁺;
> >   - its D1-through-(iii) expectation held, restatement included.
> >
> >   No premise misses.
> > - **Me:** Flags S and F held, and D1 held.
>
> **M5:**
>
> > - **The reviewer:**
> >   - its Flag-I addition (place the single-system results against Pudlák's self case) was right, and there is no superpolynomial self case;
> >   - its Flag-N warning prevented deriving CON^N ⇒ NE ≠ coNE before the text was read, and the implication is now verified secondarily;
> >   - its G2 prior (30) did not occur.
> >
> >   No premise misses.
> > - **Me:**
> >   - Flags I, N and D held;
> >   - M4's smallest instance carried an unverified pair condition. That is corrected here as a **miss of mine**: g10 was not applied to the instance in M4.

**M3 pre-registration (the eighth wrong outcome prior):**

> 1. **Davis–Robere refutes the "Gödel's second theorem" reading** in its general form. A proof system *can* prove strong lower bounds against itself, as depth-d Frege does on Prf^{Frege_d}(PHP). Counted at the reviewer's request as its **eighth wrong outcome prior**.

**A1 (A1_bottom_pair_report.md):**

> - **The reviewer:**
>   - its g12 guard was exactly the right first check, because the formulation differs by rung;
>   - its memory claim that "consistency statements of stronger systems are a standard hard family for resolution" is **contradicted for consistency and confirmed for reflection**. It was flagged as memory and counted for nothing, so this is a note, not a miss.
> - **Me:** Flag T was right and decisive, Flag R held, and my B3 prior held.

**A2 (A2_first_rung_report.md):**

> **My miss in A1.** A1 said the instance was "within reach of the known techniques (feasible interpolation, as in the proofs of Theorems 3.11–3.12)". The actual route is simpler, and it was available from sources A1 had already read: Cook–Nguyen's Haken/Buss paragraph and §10B.5.

**A3 (A3_self_rung_report.md):**

> **Accepted as S2.** Two of the reviewer's priors were wrong:
> - **S1** is the reviewer's **ninth** wrong outcome prior, refuted from a statement (rows 1–3).
> - **The extension/reusability reading** is the **tenth**. It was pre-registered as a test and falsified on the Frege row.
>
> The expressiveness (self-evaluation) divide stays **post hoc**.

**A4 (A4_no_optimal_report.md):**

> **Miss recorded (mine).** My O2 weight (35) rested on Flag R's worry that no-optimal oracles might exist only for p-optimality. That did not happen: two primaries construct length-optimal ones. **Attribution slip recorded (mine alone):** I called arXiv:1904.01362 "Dose–Glaßer" before reading it. It is by Khaniki.


### Additions from the attempt phase (X1–X2), extracted by script

**Counts added.**
- **The reviewer:** the (c) repair swap (X1) and the "necessary" direction slip (X2).
- **Me:** Flag S's "may be refuted" (X1) and the X2b weight (X2).

**X1 (X1_ip2_ltf2_report.md, misses):**

> - *My Flag S wording*, "sign-rank may be refuted as the measure", was too strong. It is refuted only as a polynomial measure, and CM's quantitative question keeps it alive.

> - *The reviewer's slip:* the (c) repair assignment (Flag W).

**X1 (ruling):**

> **Accepted as X1a.** The third fabrication is recorded as caught. Reading the math images, not the summary, is the practice. The misses stand as written: Flag S's "may be refuted" is mine, and the (c) swap is the reviewer's.
>
> 1. **L1 is the attempt's result.** "Every poly-size THR∘THR circuit has sign-rank 2^{o(n)}" (Chattopadhyay–Mande §8). Its status is two-sided: 2^{Ω(n^{1/4})} is attained, and a 2^{Ω(n)} example would refute it. It is the smallest open lemma the program has produced at any layer that meets all three of these conditions:
>    - it is stated by the field;
>    - it would settle a named fold statement (IP2 ∉ THR∘THR);
>    - it has a named necessary sub-step (L0, lower bounds for decision lists of exact thresholds).
> 2. **The fold measure at this layer is the sign-rank exponent, not Boolean depth.** Chattopadhyay–Mande's F_n has three Boolean nestings and linear THR∘THR size, so heavy weights absorb Boolean nesting outright. The exponent runs 0 (up to THR∘MAJ) → [1/4, 1) (THR∘THR, if L1) → 1 (IP2). This is an observation that gives the nesting reading a candidate referent *conditional on L1*, and nothing more.

**X2 (X2_ethr_lists_report.md, misses):**

> - **My X2b weight (35) was a miss.** Flag P's containment is refuted by CM's own separation.

> - **The reviewer's slip ("necessary step")** is recorded as it asked, and the word is kept out of the claims here.

**X2 (ruling):**

> **Accepted as X2a. The attempt phase closes.** The end state stands as in §5.
>
> Calibration:
> - the reviewer's: the "necessary" direction slip;
> - mine: the X2b weight.


### Additions from X3, extracted by script

**Counts added.**
- **Me:** X2's "only known lower bound" line and the X3b weight.
- **Joint, scored on both sides:** spec clause (3), "additive", where the literature's parameter is alternation.

> - *mine:* the X3b weight (55). The surviving measure was in the literature, and X2's search missed it. X2's "only known lower bound" line is corrected here.

> - *both sides:* the spec's "additive" clause (3). The one measure that works is additive only within alternation blocks. The spec should have asked about alternation, and the literature had already made that its parameter.

**X3 (ruling):**

> **Accepted as X3a, restricted.** Both misses of mine are recorded as written:
> - X2's "only known lower bound";
> - the X3b weight.
>
> The spec-clause (3) miss ("additive", where the literature's parameter is alternation) is **joint, and scored on both sides**.


### Additions from X4–X7, extracted by script

**Counts added.**
- **The reviewer:** its tenth premise miss (X4: the queued X5 premise); its positive finding (X5: the HML counterexample, verified).
- **Me:** the X4a weight (X4), the "stand or fall together" equivalence (X5), and the MILP method miss (X7).

**X4:**

> **My miss:** the X4a weight (55). Flag K was pre-registered without checking *which* distribution the small discrepancy is under. Theorem 45's measure is uniform; BVW's is the hardest distribution.

> **Accepted as X4b** (3bdc0e1 + 07c0953).
> - The §5 correction to the queued X5 premise is accepted. The reviewer had assumed the witnesses share IP2's *uniform* discrepancy, when they share only hardest-case discrepancy. **This is the reviewer's tenth premise miss.** X5 as then framed is withdrawn.
> - The self-check correction (the Union Lemma gives linear depth ≈ 0.36n, not every depth, with re-absorption as the residual) is accepted.
> - X5 is re-framed as the Union Lemma.

**X5:**

> **Accepted as X5b.** Lemmas S, T and T′ and the batching arithmetic go in as stated.
>
> **The Hadamard masking lemma is false: the reviewer's finding, verified here by hand and numerically.**
> - **The family.** Take m = n/2 Equality queries on disjoint 2-bit blocks, q_l = [x_l = y_l]. Then ∏_l (J − q_l) = ⊗(J₄ − I₄), and H = ⊗H₄ (Sylvester; checked equal to IP2's matrix at n = 4, 8, 10). So H ∘ ∏(J − q_l) = ⊗(H₄ − D₄), with D₄ = diag((−1)^{|x|}) = diag(1, −1, −1, 1).
> - **The norm.** M = H₄ − D₄ has zero diagonal, and M² = [[3,0,0,−2],[0,3,2,0],[0,2,3,0],[−2,0,0,3]], with eigenvalues of M equal to ±√5 and ±1. So ‖H∘∏(J − q_l)‖_op = 5^{n/4} = 2^{n/2}·(5/4)^{n/4}. Computed: 5, 25 and 55.90 at n = 4, 8 and 10, against 2^{n/2} = 4, 16 and 32.
> - **The Union Lemma holds on the same family:** Adv(IP2, U) = 2^n − ∏⟨H₄, J₄ − I₄⟩ = 2^n − 4^{n/2} = 0 (computed 0.0 at n = 4, 8, 10).
> - **So HML ⇒ UL, HML is false, and UL holds here.** The masked-norm route **cannot** prove the Union Lemma. The advantage is governed by cancellation across the disjointified terms, which a per-term operator bound discards. **The §4 stall is therefore a closed route, not an open lemma.** This is the reviewer's positive finding, verified under the suspicion protocol.
> - **My miss:** §4's sentence "The two statements stand or fall together" asserted an equivalence. Only HML ⇒ UL was shown, and the converse fails, as this family demonstrates. §5's random search also did not find this *structured* family.
> - The Union Lemma itself stays **open**. X6, the direct Fourier route, is where it goes next.

**X6:**

> **Accepted as X6a.** The following go in as proved or verified:
> - the exact type identity;
> - the fragmentation bound: the tight Union Lemma whenever K ≤ poly(m), the first structural sufficient condition beyond m ≤ n/4;
> - the N = 4 exhaustive result: the per-block factor equals N^{1.5} exactly.
>
> The reviewer proposes one more item before the pause, X7: the per-block extremal problem E⁻(N)/N^{1.5}. It decides whether tensor unions falsify the tight Union Lemma. It needs the author's go.

**X7:**

> **Miss (mine, a method miss):** I expected the MILP to close N = 16. It did not (gap 45 vs 88). The exact-φ knapsack relaxation, not pre-registered, is what decided N = 16. That is recorded here as a change of method during the run.

> **Accepted as X7b, restricted to N ≤ 16.**
> - The knapsack relaxation is recorded as the method that closed N = 16. The MILP timeout is recorded as a method miss, not a result.
> - The −1-rectangle theorem (area ≤ N/2) goes in as proved: ours, elementary.
> - X8 (an analytic knapsack aimed at ρ(N) < 1 for all N ≥ 8, or a ρ(32) > 1 witness) is named for after the pause, on the author's go only.
> - The reviewer's X8 priors, on record: bound closes for all N 40 / ρ(32) > 1 witness 25 / undecided 35.


### Additions from X8, extracted by script

**The practice it teaches** (the reviewer's wording): *every table starts at the smallest case, and "compared against which bound" is written next to every number.* X4 had 2^{1.585n} and never put it beside 2^{1.5n}.

**Counts added:** a joint miss, scored on both sides (the tight form's N = 2 witness). The reviewer's two-sided prediction is confirmed by computation.

**X8 (§5 and ruling):**

> **The N = 2 witness (ours, elementary; verified numerically).**
> - H₂ = [[1, 1], [1, −1]]. The blocky set q = {(1,1)} has ⟨H₂, q⟩ = −1, so ⟨H₂, J − q⟩ = 3 > 2^{1.5}.
> - The tensor union U = complement of ⊗_{j≤n}(J − q) = ∪_j {x_j = y_j = 1} is n blocky rectangles, and Adv(IP2, U) = 2^n − 3^n.
> - Computed: |Adv|/2^{1.5n} = 1.54, 1.77, 2.01, 2.56, 3.25, 4.11 at n = 8, 10, 12, 16, 20, 24. That grows as 1.061^n, **faster than any poly(m) with m = n**.
> - **So the tight Union Lemma is false.** This is X5c/X6b retroactively, via the simplest tensor family.
> - **X4 had the numbers.** Its §4 check computed exactly this union ("2^n − 3^n ≈ 2^{1.585n}") but compared it only with the *loose* A ≈ 2^{1.75n+1}. The tight normalization entered in X5 (Flag N) and was never tested at the smallest block.
>
> **The loose form survives every tensor union (ours, proved).**
> - In loose normalization, a tensor union of blocks N = 2^b has |Adv(IP2, U)| ≤ 2^n + ∏_blocks (N + max(E⁻(N), E(N))) (from Adv(IP2, U) = 2^n − ∏⟨H_N, J − q_b⟩). The loose bound is A = 2^{1.75n+1} = 2·∏ N^{1.75}. Per-block factors:
>   - **N = 2:** exact E⁻ = 1, E = 2, so the factor is ≤ 4/2^{1.75} = 0.94 < 1.
>   - **N = 4:** exact E⁻ = 4, E = 6. |⟨H₄, J − q⟩| = |4 − ⟨H₄, q⟩| ≤ max(4 + 4, 6 − 4) = 8, so the factor is ≤ 8/4^{1.75} = 0.707.
>   - **N ≥ 8:** |⟨H_N, J − q⟩| ≤ N + N^{1.5} (Lemma T per block), and (N + N^{1.5})/N^{1.75} ≤ 0.805 < 1. The ratio decreases in N.
> - **So no tensor union, with any mix of block sizes, violates the loose Union Lemma.** ∎
>
> **What this changes.**
> - **The tight form is dead.** The ρ program (X7, X8) answered a question about a false lemma. Its numbers are correct, and they are now a description of *how* tensor unions approach the trace bound.
> - **The loose form is the live lemma.** It is safe from tensor unions and open against non-tensor unions. Lemma T′ (any f, m ≤ ½log(1/d)) and the fragmentation bound (tight, hence loose, when K ≤ poly(m)) still hold.
> - **The recursion's threshold question** (linear alternation depth via the loose UL, with re-absorption as the residual) **is unaffected in status: open.**
>
> **Miss, joint, scored on both sides.**
> - **Mine:** X4 compared this family only with the loose bound; X5 introduced the tight normalization without testing N = 2; X6 (Flag B), X7 and X8 all started at N = 4.
> - **The reviewer's:** it defined ρ and the tight-form target starting at N = 4.

> **Accepted.**
> - The N = 2 witness stands. The joint miss is scored on both sides.
> - The two-sided Lindsey prediction goes in as the reviewer's, verified by computation.
> - **The practice it teaches** (for the pattern bullet): *every table starts at the smallest case, and "compared against which bound" is written next to every number.* X4 had 2^{1.585n} and never put it beside 2^{1.5n}.
>
> **The narrowing lemma (the reviewer's statement; the one-line proof checked here).** By the fragmentation bound, Adv(IP2, U) ≤ m·√K·2^{1.5n}. If K ≤ 2^{n/2}/m², this is ≤ 2^{1.75n} ≤ the loose bound.
> - **So the loose Union Lemma is open only for unions whose per-block row-type count exceeds 2^{n/2}/poly(n): exponential fragmentation.**
> - On the record's families, no witness is known even there. Block-Equality unions have K ≈ 2^n but advantage 0; random slice unions have small K.
>
> **X9 is named, not drafted:** unions with exponential fragmentation and non-cancelling advantage. Either construct one, which must defeat cross-type cancellation deliberately, or show that the type identity forces cancellation when K is exponential.


### Additions from X9, extracted by script

No misses on either side. Priors held: X9c, with 65 on it from both sides.

**X9 (ruling):**

> **Accepted as X9c.**
> - **The live lemma, restated:** *the bias version of Pitassi–Shirley–Shraibman's Theorem 29 for conjunctions of m co-blocky constraints: a lower bound on m in terms of |Adv(IP2, C)| rather than |C|.*
> - **Proved** (ours: PSS Theorem 29 with the −1-rectangle theorem): covering either sign class of IP2 needs Ω(2^{n/2}) blocky sets.
> - **The methodological finding** is recorded as such: numerics cannot test the loose Union Lemma at computable n.
>
> **X10 is named for after the pause, not drafted, on the author's go only: the bias-to-monochromatic bridge.**
> - *The idea:* a density increment. Large bias A should force a sub-cube of dimension n′ on which C is ε-close to monochromatic with density δ. Restrictions of co-blocky constraints are co-blocky, so PSS then forces m ≥ Ω(2^{n′/2}·δ).
> - *Kill tests:*
>   - the AND family (bias 3^n, m = n) must give n′ ≲ 2·log₂n;
>   - the block-Equality family (bias 0) must give nothing.
> - *The reviewer's priors, on record:* the bridge fails at a named step 60 / nontrivial but below the threshold 25 / loose Union Lemma proved 15.

## 8. Corrections to earlier final-state pages

- **R_program_final_state.md §1 (my overstatement).** It says a worst-case to two-sided average-case reduction for McK^tP[ζ] "would base one-way functions on NP ⊄ BPP, and hence prove P ≠ NP". The first half is right. The second does not follow: basing OWF on the *hypothesis* NP ⊄ BPP proves nothing unconditionally. What proves P ≠ NP along this route is establishing K^t's mild average-case hardness itself, as in §3(i) and in R2's own chain ("K^t mildly hard ⟺ OWF ⇒ NP ⊄ BPP ⇒ P ≠ NP"). The reduction would be a cryptographic milestone, not a separation.
- **M_program_final_state.md §2.** "NE = coNE ⇒ optimal" is attributed there to KP89, which was a secondary source. Ben-David–Gringauze credit it to Pudlák 1984; Egidy–Glaßer to KP89. Both are recorded, not merged.
- **M_program_final_state.md §3.** Krajíček's trichotomy was presented as "what the lever does give". A4 finds that it touches optimality only as a disjunct, and only p-optimality. It gives no leverage toward CON^N.

## 9. State

The loop pauses here, after the attempt phase (§10). Nothing further is drafted unless the author opens something. Anything opened is an attempt on (i), (ii), (iii) or (iv), pre-registered as such. The formal record (`formal/`, `appendix_M_formal_system.md`) is unchanged since b88c18b.

## 10. The attempt phase (X1–X2)

*Source documents: `X1_ip2_ltf2_report.md` and `X2_ethr_lists_report.md`. This phase followed N1's correction that folding is nesting, not composition (§1, amendment). These were the program's first attempts. Both ended as pre-registered, on a question the field has already posed, with the reason it is hard written down.*

**1. The target and its end state (two levels).**

> **IP2 ∉ poly-size THR∘THR**
> ⇐ **L1**: every poly-size THR∘THR circuit has sign-rank 2^{o(n)}. Chattopadhyay–Mande §8, verbatim: "Even an upper bound of 2^{o(n)} is enough to show IP is not in THR∘THR". 2^{Ω(n^{1/4})} is attained.
> and ⇒ **L0(IP2)**: IP2 has no polynomial-length decision list of exact thresholds.
> - Open, and **not known either way**. CM's footnote covers only Equality lists: "Since they are in AC0".
> - L0(IP2) ⇐ IP2 ∉ PMA^cc. CM say PMA lower bounds need new techniques, pointing to generalizing the P^NP methods of Impagliazzo–Williams.

L0 is *implied by* L1. It is not a step toward it (the X2 correction).

**2. The measures, and where each fails.**

| Measure | Status for L0 / THR∘THR | Witness or reason |
|---|---|---|
| discrepancy / PP | fails | F_n ∉ PP^cc even as a linear-length Equality list, since F_n ∉ UPP ⊇ PP (CM); hence PMA^cc ⊄ PP^cc |
| sign-rank | fails as a polynomial measure; open as 2^{o(n)} (L1) | F_n has sign-rank 2^{Ω(n^{1/4})} with linear THR∘THR size (CM) |
| additive rectangles (CMMS Lemma 16; exponential bounds for LTF lists, e.g. IP2 by Gröger–Turán–Vatan) | fails | Equality violates Lemma 16: its 1-rectangles are points and its 0-rectangles need disjoint sides (X2 §4.1) |
| multiplicative rectangles (Lemma A, ours) | works, but capped | IP2 needs length ≥ n/log₂6; the measure cannot certify more than O(n) |
| randomized communication cost | works, but capped | length Ω(n/log n); capped at linear |

**3. The obstruction.**
- Every route to L0 fails at **Equality**, the same function that stops the bottom-gate protocol in X1 (CM §1.4: no cheap randomized protocol at error 2^{−n^{Ω(1)}}).
- So the lemma under L1 is **"a measure that is small on short Equality lists and large on IP2"**, and no known measure is.
- This is the smallest open statement the program produced at any layer, and it is a well-posed question in communication complexity.

**4. What was proved in X1–X2.** Elementary, and not claimed new:
- Lemma A: an exact threshold is constant on a sub-rectangle of ≥ 1/6 the product weight. Hence IP2 needs exact-threshold decision lists of length ≥ n/log₂6.
- The Equality counterexample to CMMS Lemma 16 for exact thresholds.

Nothing else.

**5. The nesting reading's status.**
- **If L1 holds:** it has a *conditional* referent in the sign-rank exponent. The exponent is 0 up to THR∘MAJ, in [1/4, 1) on THR∘THR, and 1 at IP2.
- **Otherwise:** it has no referent.
- **Boolean depth is the wrong measure at this layer.** CM's F_n = OMB∘OR∘XOR has three Boolean nestings, yet linear THR∘THR size: heavy weights absorb Boolean nesting.

**6. Calibration.** Recorded in §7, "Additions from the attempt phase", extracted by script:
- the reviewer's (c) repair swap (X1) and "necessary" slip (X2);
- my Flag S wording (X1) and X2b weight (X2).
- The third web-summary fabrication (Amano 2020's exponents) was caught by reading the page's math images instead.

**7. X3: four paths toward the missing measure** (`X3_measure_paths_report.md`; the spec as sharpened: exponential-scale, polynomial on Equality-type gates, additive over the list, small on F_n).
- **A, Equality-oracle communication** (Chattopadhyay–Lovett–Vinyals; Pitassi–Shirley–Shraibman; Göös–Harms–Riazanov).
  - It dies as a cost measure **by scale, not by containment**. An exact-threshold query is one Equality-oracle call, whose 1-set is a blocky matrix, but oracle cost is at most n + 1 on every function.
  - The **blocky-matrix object survives**.
- **D, sign-rank inside THR∘THR.** No 2^{Ω(n)} example is known; the best is 2^{Ω(n^{1/4})} (CM). **L1 survives.**
- **B, the list restatement.** Candidates were tested in the order EQ → F_n → IP2:
  - row patterns die on EQ;
  - cost measures die by scale;
  - sign-rank dies on F_n;
  - additive rectangles die on EQ;
  - **Podolskii–Prior's recursive blocky discrepancy survives up to alternation depth o(n/log n)**.
- **C, the SAT-algorithm route** (Impagliazzo–Paturi–Schneider; Chen–Santhanam–Srinivasan; Alman–Chan–Williams). The gap is **scale** (n^{1+ε} wires or subquadratic bottom gates, against any polynomial) and **target** (the route yields NEXP-type functions, not IP2).
- **Outcome: X3a, restricted.** The lemma under the lemma is a blocky-matrix measure whose loss across alternations is additive. The end state in item 1 is refined accordingly: L0(IP2) is known for alternation depth o(n/log n) and open above it.

**8. X4–X7: the Union Lemma** (`X4_additive_loss_report.md` … `X7_per_block_extremal_report.md`).
- **X4 (X4b).**
  - The multiplicative step in Podolskii–Prior's Theorem 45 is that each layer-i query is charged all earlier opposite-value coverage.
  - The additive repair needs the **Union Lemma**. Even with it, coverage grows Fibonacci-fast across alternations, which gives a threshold of ≈ 0.36n, with **re-absorption** as the residual.
  - The ODD-MAX-BIT∘AND kill test failed for the *uniform* measure (Disc_U ≥ 1/4). It does refute any depth-independent bound via arbitrary-distribution discrepancy.
- **X5 (X5b).**
  - The γ₂ route dies: the complement of m block-Equalities has γ₂ ≈ 2^m, yet zero IP2 advantage.
  - Lemmas S, T and T′ (ours, elementary).
  - **The Hadamard masking lemma is false** (the reviewer's counterexample, verified). With 2-bit block Equalities, ‖H∘∏(J − q_l)‖ = 5^{n/4} while Adv(IP2, U) = 0. So the operator-norm route cannot prove the Union Lemma.
- **X6 (X6a).**
  - The exact identity Adv = 2^n·Σ_τ ⟨1_{A_τ}, \hat{1_{U_τ}}⟩.
  - The fragmentation bound m·√K·2^{1.5n} (ours, proved).
  - The stall is **cross-type cancellation**.
- **X7 (X7b, restricted to N ≤ 16).** The per-block tensor factor ρ(N) = (N + E⁻(N))/N^{1.5}:

| N | E⁻(N) | ρ(N) | method |
|---|---|---|---|
| 4 | 4 | 1.000 | exhaustive (exact) |
| 8 | 13 | 0.928 | exhaustive over 21,146 column families; MILP optimal (exact) |
| 16 | 45 or 46 | [0.953, 0.969] | search lower bound; exact-φ knapsack upper bound (proved < 1) |
| 32 | ≥ 121 | [0.845, 1.061] | search; analytic knapsack (open) |

  - Also proved (ours, elementary): the maximum all-(−1) rectangle of Sylvester H_N has area N/2.

**9. X8: the tight form fails, and the loose form is safe from tensor unions** (`X8_rho_all_N_report.md`).
- **The reviewer's two-sided Lindsey bound,** verified. Its excess over N^{1.5} − N is O(√N): +3.0, +8.0, +7.8 at N = 32, 64, 128.
- **With parity and the "not all −1" cap:** ρ(64) ≤ 1.
- **With exact φ for block sides ≤ 6:** ρ(32) ≤ 0.961.
- **Found during write-up: ρ(2) = 1.061.** The n AND-rectangles (X4's own family) falsify the tight Union Lemma.
- **The loose form is proved safe from all tensor unions.** By the narrowing lemma it is open only under exponential row-type fragmentation, which is X9 (named).

**10. X9: the loose Union Lemma under exponential fragmentation** (`X9_fragmented_unions_report.md`).
- **The framing:** IP2's uniform discrepancy against m-query Equality-oracle conjunctions.
- **The B(n, m) table**, greedy lower bounds, each value beside 3^n and 2^{1.75n}:

| n | m | \|Adv(C)\| | ÷ 3^n | ÷ 2^{1.75n} |
|---|---|---|---|---|
| 4 | 4 | 114 | 1.41 | 0.89 |
| 5 | 5 | 446 | 1.84 | 1.04 |
| 6 | 6 | 1509 | 2.07 | 1.04 |
| 6 | 12 | 1860 | 2.55 | 1.28 |
| 8 | 8 | 13219 | 2.01 | 0.81 |
| 8 | 16 | 17330 | 2.64 | 1.06 |

  The table is inconclusive by design: the covering threshold is below m at these n.
- **Proved (ours):** a monochromatic C needs 2^{Ω(n)} constraints, from PSS Theorem 29 with the −1-rectangle theorem.
- **The stall:** X6's cross-type cancellation in the 2^m-term expansion. The missing lemma is the bias version of max-rect. X10 (the density-increment bridge) is named.
