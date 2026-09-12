# W6: the round complexity of the fold. Pre-registration

*Drafted 2026-09-11 on branch `w6-round-complexity`, on the reviewer's W6 specification, after its W5 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**This file is committed BEFORE any source is read for W6. Everything below is fixed in advance and is not revised retroactively. Findings are appended afterwards, below the rule at the end.**

## Ceiling (first)

Unchanged, and it is the whole W-line's ceiling. W6 studies the **round structure** of an algorithm for Avoid whose existence is already conditional. Nothing here bears on P vs NP; the best outcome is a sharper statement of which resource — rounds, not queries — the fold actually spends, plus a falsifiable form for the record's "hiding is depth" thesis. **Rounds are not hardness.** A round lower bound in a black-box model would constrain techniques, not prove a separation.

## §0. Refuted premises checked (the standing practice)

Not reused: "hidden ρ" (Y3); "no off-sample rows" (Y4); "the grid is symmetric" (Y5); "(PL) is loose-access lowness" (Y6); "the Pessiland oracle does not bar the route" (Y7, reversed by Y8); "the generator's outputs are deep" (Y9, refuted by counting); **"prefix descent must resolve a deficit of 1" (W5, mine — false; the deficit stays ≥ half the subcube, and the real obstruction is additive error ε2ⁿ against a required resolution 2^{n−k})**; **"(D1) is smaller than the door" (W4's prose, corrected in W5 — (D1) ⇒ (C₁) and is at least as strong)**.

**And one carried in from W5's own correction, still warm:** *a superscript dropped by text extraction must never be reconstructed inside quotation marks.* W5 quoted SU05 Def 2.4 as "2^{n^ε}" where the extraction had lost the exponent; the reviewer caught it. Every verbatim quote in W6 that contains an exponent is checked against a second extractor before it is written.

## §1. Why this question, stated before reading

The W-line's door is (C₁): FP^NP for Avoid ⟺ E^NP ⊄ SIZE[2^{o(n)}], with the hypothesis provably minimal (RW26 §5). W5 established that the counting route (D1) is **sufficient and at least as strong**, not a weakening. So "make it smaller" cannot mean a weaker hypothesis; it must mean a smaller object or a different kind. **(D2) — non-adaptive Avoid — is the "different kind" candidate, and rounds are its natural parameter.** W6 asks what is actually known about that parameter.

## §2. My priors, fixed now

### Q1 — the classical baseline

| code | statement | my prior |
|---|---|---|
| **Q1a** | `P^NP_tt = P^NP[O(log n)]` holds for **languages**, as Buss–Hay / Hemachandra, verbatim and with that quantifier | **90** |
| **Q1b-fail** | For **functions**, `FP^NP_tt = FP^NP[O(log n)]` is **not** known, and equality is known to force a collapse (P = NP, or NP = coNP, or similar) | **60** |
| **Q1b-open** | For functions, simply open, with no such known consequence | 25 |
| **Q1b-eq** | Equality holds for functions too | 15 |
| **Q1c** | The k-rounds-of-parallel-queries hierarchy has **known relativized separations** as k grows | **70** |

I am confident of the inclusion `FP^NP[O(log n)] ⊆ FP^NP_tt` in the function case by the path-enumeration argument (a log-query adaptive computation has poly many query paths, all askable in parallel), and I expect the *converse* to be where the content is. **I have not verified any of this and may have the attributions wrong; Hemachandra 1989 vs Buss–Hay 1991 vs Wagner are exactly the kind of credit I have previously mis-assigned.**

### Q2 — the engine's round count

| code | statement | my prior |
|---|---|---|
| **Q2a** | RW26's own text supports the attribution: the **n** term is the prefix/seed search, the **log(T/n)** term is the tree depth (= W3's fold depth) | **75** |
| **Q2b-none** | **No** round lower bound is known, in any model, for solving Avoid given a hard string | **75** |
| **Q2b-some** | Some black-box or oracle round lower bound exists (Korten survey §8.1, Korten–Pitassi FOCS'24, or GGLS25's depth-n downward self-reduction) | 25 |

The reviewer's prior on Q2b-none is 70; mine is 75, and for a stated reason: **a round lower bound would be a statement about adaptivity in a model where the hard string is given, which is close enough to the linear ordering principle's depth that if it were known, W3 would have found it.** If GGLS25's LOP self-reduction of depth n turns out to *be* such a bound, Q2b-some wins and my prior is wrong.

### Q3 — what hypotheses buy

| code | statement | my prior |
|---|---|---|
| **Q3-no** | SU05 Thm 3.11 (`BPP^{NP‖} = P^{NP‖}`) does **not** give Avoid ∈ FP^NP_tt outright, because it is a **language/decision** statement and Avoid is a **single-valued search** problem | **65** |
| **Q3-yes** | It does give it outright | 25 |
| **Q3-other** | Neither cleanly | 10 |
| **Q3-src** | RW26's "known only from [KM02; MV05]" traces to **hitting-set generators / derandomizing AM** (Klivans–van Melkebeek; Miltersen–Vinodchandran), i.e. the prMA queries are derandomized into **one** round | **70** |

**Flag A6, registered now:** the reviewer's Q3 asks whether Thm 3.11 "gives Avoid ∈ FP^NP_tt outright via the trivial FZPP^NP algorithm". I predict the honest answer is **no, and the right instrument is Thm 3.6/3.12 (the relative-error approximator / hitting-set construction), not Thm 3.11** — because turning a randomized *search* procedure into a deterministic one needs the generator, not the class equality. If the run finds otherwise, Q3-yes wins.

### Q4 — the RE test, and the counting done before the prior

The reviewer asked for the counting before a prior. **Here it is, and it changes the question's shape before I read anything.**

If Avoid ∈ FP^NP_tt is *already known under a hardness hypothesis* (Q3-src, prior 70), then **"the round count is intrinsic" is false as an unconditional claim about the problem**, because a hypothesis that nobody expects to fail already collapses it to one round. Therefore:

- the naive form — "extracting the residue from a hard history cannot be made non-adaptive" — is **already conditionally refuted**, and I register that now rather than discovering it mid-run;
- the only form that can survive is a **relativized, unconditional** one: *there is an oracle relative to which Avoid given a hard string is in FP^NP[O(n + log T)] but not in FP^NP_tt.*

| code | statement | my prior |
|---|---|---|
| **Q4-oracle** | The surviving form is the oracle statement above, and it is **open** — neither confirmed nor refuted by anything on record | **65** |
| **Q4-refuted** | Even the oracle form is refuted, or is inconsistent with a known relativizing collapse | 20 |
| **Q4-confirmed** | Something on record already confirms it | 15 |

**Flag E6 — my sharpest pre-registered prediction, and the one most likely to be wrong in an interesting way.** The Buss–Hay-type collapse covers **O(log n)** queries. The fold spends **O(n + log(T/n))** rounds. So *even for languages, and even granting every classical collapse*, the n term is out of reach of that machinery: **the obstruction is the n term (the prefix/seed search), not the log(T/n) term (the fold depth).** If that is right, then "hiding is depth" is being tested on the wrong summand — the depth term is the one the classical theory could plausibly collapse, and the *search* term is the stubborn one. **Prior that this diagnosis survives contact with the sources: 80.**

## §3. Flags (mine, before any work)

- **Flag A6** — Thm 3.11 is a language statement; see Q3 above.
- **Flag B6** — three distinct notions must never be merged, and every line of the deliverable states which one it means: (i) **adaptive queries** `P^NP[k]`; (ii) **rounds of parallel queries**, k rounds each of poly many; (iii) **non-adaptive** = truth-table = exactly one round. The W6 specification's Q1 moves between "rounds of adaptive NP queries" and "non-adaptive access" in one sentence; the run keeps them apart.
- **Flag C6** — **languages vs functions is the crux, not a footnote.** The fold is a search/function problem. A language-level collapse does not transfer to it for free, and I expect this to be the single most load-bearing distinction in the answer.
- **Flag D6** — every exponent in every verbatim quote is confirmed against a second extractor before it is written (the W5 lesson, above).
- **Flag F6** — "relativized" is claimed only where a source says it; a black-box impossibility (DS26's word) is **not** a relativization barrier, and W5 already had to draw that line once.

## §4. Kill tests

- Sizes, oracle model, adaptive/parallel, languages/functions, and i.o./a.e. on **every** tabulated line.
- Theorem numbers on every entry, or the entry says "not located".
- Check the ECCC keyword page for range avoidance, and **TR26-118 §3–§5**, before writing "open" anywhere.
- Relativization claimed only where stated (Flag F6).
- Credit checked: Buss–Hay / Hemachandra / Wagner / Krentel / Selman are easy to mis-attribute, and I have mis-attributed before.
- **If a prior is wrong, the report says so in the same sentence as the finding, not in a later section.**

---

*Findings follow below, appended after reading. Nothing above is revised retroactively.*

---

# Findings (written after reading; priors above are unrevised)

*Sources read as text this run: Buss–Hay, "On Truth-Table Reducibility to SAT", Information and Computation 91, 86–102 (1991), extracted from the Toronto mirror; Jenner–Torán, "Computing Functions with Parallel Queries to NP" (Ulm copy); Ren–Williams TR26-118 §1, §3, §5; Korten, "Range avoidance and the complexity of explicit constructions", Bull. EATCS 145 (2025) §6.2, §7, §8.1; Shaltiel–Umans CCC'05 §3.3; Ghentiyala–Goldberg–Li–Stephens-Davidowitz TR25-2xx (downward self-reducibility in TFΣP) §1, §3, §4.*

## 0. Outcome against priors

| | prior | outcome |
|---|---|---|
| **Q1a** languages: tt = O(log n) adaptive, verbatim | 90 | **held** (§1) |
| **Q1b-fail** functions: equality known to force a collapse | 60 | **held**, though not with the consequences I was offered (§1) |
| **Q1c** k-round hierarchy has known relativized separations | 70 | **WRONG — the question does not arise** (§1, §5) |
| **Q2a** n = prefix search, log(T/n) = fold depth | 75 | **held, verbatim** (§2) |
| **Q2b-none** no round lower bound known | 75 | **held, and strengthened** (§3) |
| **Q3-no** SU05 Thm 3.11 does not give it; 3.12 does | 65 | **held** (§4) |
| **Q3-src** traces to KM02/MV05 hitting-set line | 70 | **held, with the mechanism refined** (§4) |
| **Q4-oracle** surviving form is the relativized one, open | 65 | **held, and it coincides with a named open problem** (§5) |
| **Flag E6** the n term is the stubborn summand | 80 | **HALF REFUTED — attribution right, stubbornness backwards** (§3) |

## 1. Q1 — the classical baseline, with the languages/functions line drawn

**Languages. Buss–Hay Theorem 9** (verbatim): *"Let k ≥ 1. If A(x) is a **decision problem** recognized by a Turing machine M which runs in polynomial time and makes k rounds of parallel queries to SAT, then A(x) is in ≤^p_tt(NP), i.e., A(x) is polynomial time truth-table reducible to SAT."*

So a **constant** number of rounds collapses to one, for decision problems. Their abstract states it as *"a constant number of rounds of parallel queries to SAT is equivalent to one round of parallel queries"*, and §3 records the base case as Ladner–Lynch–Selman (1975). The quantifier is explicit at their line 80: *"Let ≤^p_tt(NP) denote the class of **decision problems** polynomial time truth-table reducible to NP"*.

**The `O(log n)` identification is Krentel's class, quoted by them at line 81:** *"First, Krentel (1986) defines the class P^SAT[O(log n)]; we show this is equal to ≤^p_tt(NP)."* **Credit, as they give it:** *"Many of the results of this paper have been obtained independently by K. Wagner; in particular, Theorem 1 and many of the other results of Section 2 are in Wagner (1988a, 1988b)"*, and Hemachandra (1987) is credited with the harder inclusion of one direction. *(So "Buss–Hay / Hemachandra" is right as a pairing, but Wagner has independent priority on Theorem 1 — recorded because this program has mis-assigned credit before.)*

**Functions — and this is the load-bearing half. Jenner–Torán**, abstract: *"In contrast to the language case the function classes seem to all be different."* Their line 142: *"The question whether the classes FP^NP_∥ and FP^NP_log are equal has attracted the attention of different researchers. It is known that the hypothesis FP^NP_∥ = FP^NP_log implies that **FewP=P, NP=R and coNP=US**."*

- **A correction to what a search engine handed me**, recorded because I nearly inherited it: the summary I was given claimed the consequences are "NP = RP and P = UP". The printed consequences are **FewP=P, NP=R, coNP=US**. I did not read [35] (Selman's taxonomy) itself, so the attribution here is Jenner–Torán's, not mine.
- **Theorem 2.3 is the sharp nuance:** the function classes **do** collapse for short outputs — *"for functions with values that are logarithmically bounded in length, i.e., functions f for which |f(x)| ∈ O(log|x|)"*. So the function/language gap is not everywhere; it opens exactly where outputs are long.
- **And they name the mechanism** (line 533): *"This (possible) difference in behaviour between language classes and function classes is basically due to a **communication problem between the oracle and the base machine that occurs when the bound on the length of the function exceeds the bound on the number of bits handed over by the oracle**."*

**This is why Flag C6 was the right flag.** The fold is a search problem whose queries carry **n-bit witnesses** and whose output is a 2n-bit string — squarely in the regime where Jenner–Torán say the language-level collapse is not available. It is also why RW26 parameterise their class by witness length at all (their line 28: *"P^NP with r(n) adaptive rounds of NP queries, where each NP query has witness length s(n)"*).

**Q1c — my prior was mis-framed and I am recording it as a miss.** I put 70 on "known relativized separations of the k-round hierarchy". By Theorem 9 there **is no constant-round hierarchy for languages to separate** — it collapses at every constant k. Buss–Hay's oracles do something else: *"one oracle relative to which ≤^p_tt(NP) is equal to PSPACE and another oracle relative to which ≤^p_tt(NP) and Δ₂^p are distinct"*, i.e. they separate truth-table access from **unbounded adaptive** access. For **growing** r(n) — the regime the fold actually lives in — I located **no** separation result, and RW26 introduce the r(n)-round class without citing one.

## 2. Q2(a) — where the two terms come from, verbatim

**RW26 Theorem 3.1:** the algorithm takes an AVOID instance G : {0,1}^n → {0,1}^{2n} and a truth table f ∈ {0,1}^T and returns either *"the message 'easy' and a circuit C of size O(|G| log T) that computes the truth table f"* or *"the message 'hard' and a string y ∈ {0,1}^{2n} \ Range(G)"*, with **#rounds = O(n + log(T/n))**, **witness length = n**, in TIME[poly(T,|G|)]^NP.

- **The n term is the search-to-decision cost**, in their own words (line 495): *"The simplest way to compute x_j would cost **n parallel rounds per stage**: one round for each variable value."* It is the bit-by-bit determination of the **lexicographically smallest satisfying assignment**. Blocking softens it: *"one can make only m := ⌈n/b⌉ extra rounds per stage in a way that multiplies the overall running time by an O(2^b) factor."*
- **The log(T/n) term is the fold depth**: `k = ⌈log₂(T/n)⌉` stages (line 482), the algorithm *"proceeds in k stages, starting with stage k and decreasing down to stage 1"*, each stage halving the string length — W3's fold.
- **They combine exactly as Flag E6 said** (line 515): *"As we take t = ⌈n/b⌉ + 1 rounds in each stage, the total number of parallel rounds is O(t·k). Letting b = ⌈log(T·|G|)⌉ … the number of parallel rounds becomes O((⌈n/⌈log(T·|G|)⌉+1⌉) log(T/n)) ≤ O(n + log(T/n))."*

**The arithmetic, done rather than read off.** Total rounds = (⌈n/b⌉+1)·k with b = ⌈log(T|G|)⌉ and k = ⌈log₂(T/n)⌉, so the two summands are **search = n·k/b** and **depth = k**. Since k ≤ b the search summand is ≤ n, which is where the printed `O(n + log(T/n))` comes from. Two regimes:
- **T polynomial:** k = O(log n), b = O(log n), so search ≈ **n** and depth ≈ **O(log n)** — the search term dominates outright.
- **T = 2^Θ(n):** k ≈ n and b ≈ n, so search ≈ **n** and depth ≈ **n** — comparable.

**So the n summand is present in every regime, and the depth summand only becomes comparable when T is exponential.** That much supported my flag. What follows does not.

## 3. Q2(b) and the refutation of half of Flag E6

**No round lower bound is known, in any model.** What exists nearby, and why none of it is a round bound:

1. **Korten §6.2, Theorem 12 (attributed to Wilson):** *"If Q is as above, has query complexity q and width complexity w and solves the [N] → [M] Avoid problem, then **qw ≥ N**. Hence Avoid ∉ FP^NP relative to some oracle."* This is a **query × width** bound in the black-box/decision-tree model, and it concerns Avoid **without** a hard truth table. It says nothing about rounds, and nothing about the case where a hard string is supplied.
2. **GGLS25 supplies upper bounds, not lower bounds:** LOP is µ-downward-self-reducible (their Thm 4.1), hence LOP and Avoid lie in UEOPL^NP (Thms 2–3). The recursion depth in their framework is *"the maximum depth of recursion is µ(x) ≤ p(n)"* — a depth **budget**, not a lower bound. Their own open question 3 asks *"Does a non-adaptive downward self-reduction for a TFΣP_i problem imply membership in a …"*, i.e. non-adaptivity is open on their side too. **The peer's GGLS25 candidate does not supply a depth bound.**
3. **Korten §8.1 is the real answer, and it is an open problem stated by the field.** *"Problem 1. Is there an FP^NP reduction from stretch n ↦ αn to m ↦ βm with **depth complexity** significantly better than log_α β?"* — where depth complexity is defined (line 711) as *"the depth of the longest chain of oracle calls C′ makes to C"*, exactly the fold's depth. He continues: *"it is equally natural to conjecture that the answer is negative, in which case we cannot hope to refute it unconditionally without proving P ≠ NP. In this case, **it would be interesting to show a negative result in a restricted black box model of reducibility** … the depth of the reduction can be measured in a black box sense with no reference to boolean circuit depth. The analogous question for PRG stretching reductions has been asked before … and **remains almost completely unsolved**."*

**Now the part that refutes my own flag.** I pre-registered (Flag E6, prior 80) that the n term is the obstruction and *"the depth term is the one the classical theory could plausibly collapse, and the search term is the stubborn one."* **The attribution was right; the stubbornness is backwards**, and RW26 decide it in their own accounting:

- **RW26 line 1243:** *"the Jeřábek–Korten reduction essentially makes **O(log T) rounds of non-adaptive queries to searchSAT**"*, and line 1252: *"Replacing the searchSAT oracle with a (decisional) SAT oracle incurs an **O(n/log T)** … multiplicative overhead on the number of rounds."*
- **Theorem 5.1's proof sketch** makes it explicit: assuming searchSAT ∈ FP^NP_tt, *"The Jeřábek–Korten reduction runs in TIME[poly(|T|,|G|)]^NP with **#rounds = O(log T)**, length = n."*

**So the n term is precisely the search-to-decision cost and it is removable under a plausible hypothesis; what survives is the depth term.** The n summand is not the stubborn one — it is the one with a known route to removal, and RW26 note (line 1363) that *"searchSAT admits an efficient randomized algorithm with parallel access to the NP oracle by using the isolation lemma [MVV87; VV86; BCGL92]"*, so the route is derandomising isolation.

**Recorded plainly: this is my third self-correction in this program's recent phases, and it has the shape of the other two** — a prior placed on a plausible reading of where difficulty lives, refuted by doing the accounting. The practice line from Y9 applies again and I did not apply it hard enough: *the counting comes before the prior.* I did the counting for the two terms' **origins** and not for their **removability**.

*(Provenance note, since it matters for scoring: the reviewer's mid-run guidance predicted this same conclusion. I did not adopt it on its say-so — the finding rests on RW26 Thm 5.1's sketch and line 1252, quoted above, which I read after receiving it. The reviewer was right and the source is what settles it.)*

## 4. Q3 — the table, every line with a source

| hypothesis | what it gives for Avoid | rounds / access | source, theorem |
|---|---|---|---|
| **none** (unconditional) | Avoid ∈ FS₂P; Avoid ∈ UEOPL^NP; trivially in FZPP^NP | not a P^NP algorithm at all | CHR24, Li24, KP24; GGLS25 Thms 2–3 |
| **none**, given a hard truth table f | Jeřábek–Korten fold | **O(n + log(T/n))** rounds, witness length n | **RW26 Thm 3.1** |
| **searchSAT ∈ FP^NP_tt** | same fold, search step free | **O(log T)** rounds | **RW26 Thm 5.1**, proof sketch |
| **E^{NP‖} hard for exp-size SV-nondeterministic circuits** | searchSAT ∈ FP^NP_tt outright | **one round** (non-adaptive) | **SU05 Thm 3.12** |
| **SVN lower bounds (KM02; MV05)** | AVOID ∈ FP^NP_tt | **one round** | RW26 line 1393 |
| **E^NP ⊄ SIZE[2^{o(n)}]** (the door, minimal) | Avoid ∈ FP^NP | adaptive; O(n + log T) rounds via Thm 3.1 | Korten Thm 10 + RW26 Thm 3.1 |
| **(D2) target** | Avoid ∈ FP^NP_tt from a *weaker* hypothesis | one round | **open — RW26 Question 5.3** |

**Flag A6 confirmed, and the instrument is the one I named.** SU05 **Theorem 3.11** (*"If E^{NP‖} requires exponential size SV-nondeterministic circuits, then BPP^{NP‖} = P^{NP‖}"*) is a statement about **language classes** and does **not** by itself put a single-valued search problem in FP^NP_tt. The instrument is **Theorem 3.12** (verbatim): *"If E^{NP‖} requires exponential size SV-nondeterministic circuits, then there is a procedure that, given a circuit C, outputs a satisfying assignment for C if one exists, and runs in polynomial time with non-adaptive NP-oracle access."*

**The mechanism, from SU05's own prose** (lines 514–531), which refines my Q3-src prior: it is **not** "derandomising AM" directly but **Valiant–Vazirani isolation plus a PRG for nonadaptive SAT-oracle circuits** — *"there is a polynomial time algorithm that makes non-adaptive NP queries to test whether the outcome of applying the Valiant-Vazirani reduction to a satisfiable circuit C … succeeds in producing a circuit that has a unique satisfying assignment"*, then one parallel round of *"Does C′ have a satisfying assignment that assigns x_i true?"* queries. SU05 credit the observation to **[24] = Klivans–van Melkebeek** *"building on earlier work by [8]"* = **Ben-David–Chor–Goldreich–Luby**, which is RW26's [BCGL92] — **the two papers' citation trails agree.**

**Tags resolved** (RW26's bibliography): AK01 = Arvind–Köbler, *Theor. Comput. Sci.* 255 (2001); KM02 = Klivans–van Melkebeek, *SIAM J. Comput.* 31.5 (2002); MV05 = Miltersen–Vinodchandran, *Comput. Complex.* 14.3 (2005); SU06 = Shaltiel–Umans, *Comput. Complex.* 15.4 (2006).

## 5. Q4 — the RE test, in the language of Q1–Q3

**The naive form is refuted, as the pre-registered counting said it would be.** Under SVN hardness, AVOID ∈ FP^NP_tt — **one round** (RW26 line 1393). So "the adaptive round count for extracting the residue is intrinsic" is **false** as an unconditional claim about the problem, and any version of "hiding is depth" that asserts it is already dead.

**The surviving form, stated falsifiably.** Two separate statements, because the two summands behave differently:

- **Search term — not the test.** It is removable under searchSAT ∈ FP^NP_tt (RW26 Thm 5.1), a hypothesis RW26 call *"plausible"*. Nothing about depth is at stake in it.
- **Depth term — this is the test.** *Is there an oracle relative to which the fold, given a hard truth table, requires ω(1) rounds of parallel NP queries — equivalently, relative to which Avoid-given-a-hard-string ∈ FP^NP[O(n + log T)] but ∉ FP^NP_tt?*

**Status: open, and neither confirmed nor refuted.** And the useful finding is that **this is not a private prediction of the record's thesis — it is Korten's Problem 1**, in black-box form, with his own note that the analogous PRG-stretching question *"remains almost completely unsolved"*. **The smallest statement that would decide it** is therefore the one Korten names: a **depth lower bound for the stretching reduction in the black-box model**, where (his line 1500) *"the depth of the reduction can be measured in a black box sense with no reference to boolean circuit depth"*.

**Two constraints on any such proof, from §1, worth stating because they are what make it hard:**
1. It must concern **growing** round counts. Buss–Hay Theorem 9 kills every constant-round separation — for languages, and the collapse is unconditional.
2. It must be a statement about **functions/search with long outputs**, not languages. Jenner–Torán's Theorem 2.3 shows the function classes collapse for O(log n)-bit outputs, and their diagnosis — *"a communication problem … when the bound on the length of the function exceeds the bound on the number of bits handed over by the oracle"* — is exactly the regime the fold occupies, with n-bit witnesses and a 2n-bit output.

**So the honest form of "hiding is depth" here is narrow:** not that residue extraction is adaptive-hard in general, but that **the fold's depth summand cannot be parallelised black-box**. That is falsifiable, it is open, and it is already on the field's problem list.

## 6. Kill tests

- **Rounds vs queries vs non-adaptive (Flag B6):** kept apart on every line. Buss–Hay Thm 9 = constant **rounds** → one round; Krentel's P^SAT[O(log n)] = **adaptive query count**; FP^NP_tt = exactly one round.
- **Languages vs functions (Flag C6):** every entry marked. This turned out to be the crux, as flagged.
- **Sizes / oracle model:** SU05 lines carry E^{NP‖}, SV-nondeterministic, exponential size = **2^{εn}** (the W5 correction, verified there three ways), non-adaptive access.
- **Relativization only where stated (Flag F6):** Korten's Theorem 12 is a **black-box/decision-tree** result that *"can be used to build an oracle"*; Problem 1's proposed negative result is **black-box**, not a relativization barrier. No claim beyond that.
- **Exponents checked against a second extractor (Flag D6):** applied. **One casualty, reported rather than reconstructed:** Jenner–Torán's subexponential SAT bound prints in my extraction as `2nO = n`, with exponent structure destroyed. I have **not** quoted it and I do **not** reconstruct it; the claim is recorded only as *"a deterministic subexponential time algorithm deciding SAT"*, their words.
- **"Open" checked before writing:** RW26 §5 Questions 5.2/5.3 read first-hand; Korten §8.1 Problems 1–2 read first-hand; GGLS25's open questions read first-hand.
- **Prior wrong → said in the same sentence as the finding:** done for Q1c (§1) and Flag E6 (§3).

## Ceiling

Unchanged, and worth restating because this round produced a clean-looking result. **W6 proves nothing.** It establishes where a known algorithm spends its adaptivity, that one of the two summands is conditionally removable, and that a lower bound on the other is an open problem already named in the literature. **A black-box depth bound, if anyone proved it, would constrain techniques — it would not separate anything.**
