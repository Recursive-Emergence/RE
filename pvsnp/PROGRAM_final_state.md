# The P vs NP program (R, M, A): final state

*2026-09-10. This page is written to be read on its own. It consolidates `pvsnp/R1`–`R5`, `M1`–`M5` and `A1`–`A4`, and supersedes neither `R_program_final_state.md` nor `M_program_final_state.md`, except where §8 corrects them. Every cited statement was checked against a source's own text or official abstract. "Secondary" means it was verified in another paper's text. Line numbers are in the phase reports.*

**Nothing here proves anything about P vs NP.** Two theorems of ours are proved (§2), and both are about weak proof systems. Everything else is verified location: where the problem sits, which theorems bound it, and which open statements it reduces to.

## 1. The question

The author's question was whether reverse engineering (RE) plus Gödel gives a path to P vs NP; the telos was "find a path". **The reviewer's reading, adopted throughout:** "find a path" means
1. **shrink**: reduce the question to the smallest verified sufficient condition;
2. **locate**: place that condition among known theorems and barriers;
3. **attempt**: pre-register an attempt only where a statement is small and open.

The R-program shrank. The M-program located at the metamathematical layer. The A-program attempted at the bottom rung and then mapped the endpoint.

## 2. What we proved

Proved in these documents, with proofs in the reports (g5). None is about P vs NP.

- **A2, Theorem A (Res ⊬_poly rfn_CF).** Resolution has no polynomial-size refutations of the negated reflection principle of Circuit Frege. This is stated in Atserias–Bonet's SAT shape and holds for every complete, separated, polynomial-size encoding of "y is a CF-proof". The bound is superpolynomial in the formula size.
- **A2, Theorem B (Res(k) ⊬_poly rfn_Res(k+1), every k ≥ 1).** In particular Res(2) ⊬_poly rfn_Res(3). **SECONDARY tag:** the Res(k)/Res(k+1) hierarchy is taken from [SBI04, Seg05] as stated by Ben-Sasson–Nordström (arXiv:1008.1789); the primaries were not reached.
- **A2's method (Lemma 3): reflection ⇒ simulation for Res(k),** by restriction and literal substitution. If Res(k) refutes ¬rfn_T in size S, then Res(k) refutes every CNF that T refutes in size m, in size ≤ 2S + |¬rfn_T|. The method is Cook's RFN ⇒ p-simulation (Cook–Nguyen attribute the idea to Cook 1975). **Label: "C2, C1-adjacent"**: proved here, method classical, the instances not found stated.
- **M3's equivalence.** Take a Π₁ lower-bound sentence H at a fixed bound, and any Σ₁-sound theory T containing Robinson's Q. Then "T ⊬ ¬H" holds **iff** H is true. So on hardness sentences Gödel's move is a restatement: unprovability is the same problem as the lower bound.
- **M4's bound: compression changes the measure, not the ratio.** A self-referential sentence improves on the trivial proof-length bound by at most a polynomial, in the referring system's own measure. This holds in any Cook–Reckhow system, implicit ones included.
- **R2's density proposition.** Let S_k = {x ∈ {0,1}^n : K^t(x) ≤ k}. Then Pr_{x∼U_n}[x ∈ S_k] ≤ 2^{k+1−n}. Consequently, no argument built by exhibiting, sampling or conditioning on compressible strings can bear on mild average-case hardness under the uniform distribution. (Elementary; not claimed new.)

## 3. The three open statements the program ends on

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

Anything opened is an attempt on (i), (ii) or (iii), pre-registered as such.

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

## 8. Corrections to earlier final-state pages

- **R_program_final_state.md §1 (my overstatement).** It says a worst-case to two-sided average-case reduction for McK^tP[ζ] "would base one-way functions on NP ⊄ BPP, and hence prove P ≠ NP". The first half is right. The second does not follow: basing OWF on the *hypothesis* NP ⊄ BPP proves nothing unconditionally. What proves P ≠ NP along this route is establishing K^t's mild average-case hardness itself, as in §3(i) and in R2's own chain ("K^t mildly hard ⟺ OWF ⇒ NP ⊄ BPP ⇒ P ≠ NP"). The reduction would be a cryptographic milestone, not a separation.
- **M_program_final_state.md §2.** "NE = coNE ⇒ optimal" is attributed there to KP89, which was a secondary source. Ben-David–Gringauze credit it to Pudlák 1984; Egidy–Glaßer to KP89. Both are recorded, not merged.
- **M_program_final_state.md §3.** Krajíček's trichotomy was presented as "what the lever does give". A4 finds that it touches optimality only as a disjunct, and only p-optimality. It gives no leverage toward CON^N.

## 9. State

The loop pauses here. Nothing further is drafted unless the author opens something; anything opened is an attempt on (i), (ii) or (iii), pre-registered as such. The formal record (`formal/`, `appendix_M_formal_system.md`) is unchanged since b88c18b.
