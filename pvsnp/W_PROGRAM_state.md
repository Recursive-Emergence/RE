# The W-line: program state

*W19, a consolidation round set by the reviewer. Documents only, no new attack. Written 2026-09-12 on branch `w19-program-state`. `formal/` closed. LOCAL commit only, no push.*

**No priors are registered for this round.** Pre-registration exists to stop me fitting a prediction to a result; a consolidation page predicts nothing. Every statement below is quoted from its own page or its own primary, and where a statement could not be verified it is marked rather than smoothed.

---

## Ceiling, first

**The W-line has proved nothing about P vs NP, and nothing unconditional about circuit lower bounds.** What it has produced is: four lower bounds in a *black-box query model that dies under randomisation*; one relativized separation showing a published open question needs non-relativizing technique; and two structural impossibility results about a specific proof strategy. **The door (C_1) is exactly where it was when the line opened.** No rung of the ladder has been climbed by this line; the climbing was done by CHR24, Li24 and RW26, and this line has been mapping the walls.

Two standing caveats that apply to everything below:

- **Flag H7 (deterministic-only).** Every bound in §3.1 is against *deterministic* back-mappings. Guess-and-test sits in `FZPP^{NP^C}` at depth 0, so the black-box form of "hiding is depth" **dies under randomisation**. The sub-line's four theorems do not survive it.
- **Korten's Problem 1 is untouched.** The sub-line closed at depth 1 with generality unreached, by a stopping rule agreed in advance.

---

## §1. The door

**(C_1)** `Avoid ∈ FP^NP` follows from `E^NP ⊄ SIZE[2^{o(n)}]`, and that hypothesis is *minimal*. RW26 §5, verbatim:

> "It seems equally important, if not more, to understand the minimum assumption for solving the Range Avoidance problem in `FP^NP_tt`. By [Kor21], the assumption that `E^NP` requires exponential size circuits **(not SVN circuits!)** implies an `FP^NP` algorithm for AVOID; moreover, **this is provably the minimum assumption**."

The parenthetical is not an aside — **it is the boundary of §4**, stated by the authors themselves in the same sentence as the minimality.

**Reached rung: `E^{prMA}/1`.** RW26 (ECCC TR26-118, Ren-Williams, 10 July 2026), abstract: "We prove a near-maximum (`2^n/n`) circuit lower bound for the complexity class `E^{prMA}/1`, corresponding to exponential time with access to a promise-MA oracle and one bit of advice." Infinitely often; one advice bit, spent on branch selection.

## §2. The ladder, as of W16

| rung | by what | status |
|---|---|---|
| `Σ_4 E` | naive reconstruction in `Σ_4 P` | superseded -- RW26: "worse than the near-maximum circuit lower bound proved by simple diagonalization" |
| `Σ_3 E` | "simple diagonalization [Kan82; MVW99]" | the baseline any new technique must beat |
| `S_2 E` | PCP on the [Kre88] 3-CNF + Reed-Muller comparator [Hir15] | RW26: "no better than previous results [CHR24; Li24]" |
| `S_2 E/1` | CHR24, Li24 -- "`S_2 E ⊄ SIZE[2^n/n]`" | resolved a 40-year open problem |
| **`E^{prMA}/1`** | **RW26** | **current** |
| `E^NP` | -- | **open; this is the door** |

## §3. Results

**Branches and commits.** `w5-counting-form` 18caadc; `w6-round-complexity` 5aef6d7; `w7-black-box-depth` b36ed25; `w8-depth-one-lemma` 659a442; `w9-projection-glue` 3f1f1e4; `w10-projection-closed` 4eec008; `w11-nc0-glue` 044d224; `w12-one-input-glue` f2231d6; `w13-depth-one-general` 50fd900; `w14-dangerous-strings` 242e2b3; `w15-isolation-from-hardness` 224d6af; `w16-relativized-separation` bc60bd8; `w17-residue-supplies-randomness` f8e78a6; `w18-loss-exponent` 4150bb8; `w19-program-state` (this page). **w5-w14 are pushed to origin** (w14 ahead by 242e2b3); **w15-w18 are local and unpushed, awaiting the user's go.** The reviewer's `w1-range-avoidance` 267b85e (W1-W4) is its own branch and remains local by its call. **Nothing is merged; `main` is unchanged.**

### 3.1 The black-box sub-line (W7-W14), closed

All in Korten's Definition 9 / Wilson Theorem 12 DNF model; `N = 2^n`; deterministic only (Flag H7).

> **Lemma W8.1** (659a442). "If **qw + 1 < N** then there are an assignment α and a valid hint y ∉ range(C′) such that Q's output satisfies y′ ∈ range(C). Hence any correct deterministic back-mapping for a single-call depth-1 template has **qw ≥ N − 1**."

So an arbitrary hint is worth **at most one oracle position** against Wilson's unaided `qw ≥ N`.

> **Theorem W10.2** (4eec008). "Let a projection template admit a hint y with Z ≠ ∅ whose singleton-forced fraction satisfies β ≤ 1 − δ. Then every correct deterministic back-mapping in Definition 9's model has **qw ≥ δN/4**."

> **Theorem W10.3** (044d224, verified in W11). "Every projection template (any q_i, b_i) admits a hint y with Z ≠ ∅ and β ≤ 1/2 + 2^{−n}. Hence every correct deterministic back-mapping has **qw ≥ N/8 − o(N)**."

**Projection glue is closed.** Supporting: **Lemma W10.1** (all-ones reduction -- forcing `c(u) = 1^{n+1}` on H makes the positivity condition automatic and reduces every clause to "H hits `S_x^Z`"); **Lemma W11.1** (constant-glue coordinates are free wins).

> **Lemma W12.1** (f2231d6). "For every single-block template with arbitrary glue, any correct deterministic back-mapping has **qw ≥ N/3**."

> **Theorem W12.2, sharpened** (f2231d6). "For one-input patterns with arbitrary per-coordinate glue, any correct deterministic back-mapping has **qw ≥ N/9 − O(1)**."

**Where it stopped (W13, W14).** Depth-1 in full generality is **open**, and the obstruction is at the *proof* level, not the template level: `|Y_v| ≤ 2k` gives `Σ_v |Y_v| ≤ k·2^{n+2}` against only `2^{n+2}` hints, so for every `k ≥ 2` the union may cover the whole hint space -- **hint-averaging provably cannot finish**. W14 disposed of the dangerous-string residue exactly (14b ruled out; positive control run *before* the sweep) and named the real obstruction: four interacting choices (hint; sparse free set; forced values chosen *after* the hint; hosts for the ≤ k dangerous strings) where choice (3) is constrained by both (2) and (4) and (4) acts on the variables (3) sets. **It is not a template family -- it is the absence of a selection principle.**

### 3.2 The barrier sub-line (W15, W16), closed

> **Lemma W15.1** (224d6af). "Suppose every block arising in the Jeřábek-Korten tree on (G, f) has a **unique** preimage under G (by injectivity on the relevant blocks, or by promise). Then the reduction runs in **one round** of parallel NP queries."

Cost: witness length `O(T)` against RW26 Theorem 3.1's `n`. Removes exactly W6's search-to-decision term. Supporting: **Lemma W15.0** (per-level shared isolation weights; `W = T·k·n` gives failure ≤ 1/n at ≈ `n^3` bits against `|f| = T = 2^{Θ(n)}` -- "it fits with exponential room").

> **Lemma W16.0** (bc60bd8). "There is an oracle A with (1) `E^{NP^A} ⊄ SIZE^A[2^{εn}]`, (2) `E^{NP^A‖} ⊆ SVN-SIZE^A[2^{√n}]`, (3) staging consistent."

> **Lemma W16.1 (2-cover), final form, deterministic** (bc60bd8). "S is 2-covered for `{Π_i}` if for every queried tuple-property with a witness in S, and every x ∈ S, some witness avoids x." Construction: E = strings essential to some property, `|E| ≤ q·w/n`; close **Bad** under *"while some property has exactly one element outside C ∪ E ∪ Bad, mark that element Bad"*, so `|Bad| ≤ q`; draw S outside `C ∪ E ∪ Bad` and repair. "Repairs are monotone ... so each is repaired at most once: **≤ q repairs, |S| ≤ m + q·w/n**."

**The fixpoint is a statement about Π, C, E, Bad alone, independent of S**, which is what makes the lemma deterministic and removes the reviewer's residual `q·m/2^n`.

> **Theorem W16.2** (bc60bd8). "Relative to the oracle A of Lemma W16.0, **`Avoid ∈ FP^{NP^A}`** and **`Avoid ∉ FP^{NP^A}_tt`**."

**Consequence, in the page's own words:** "Any proof that `E^NP ⊄ SIZE[2^{o(n)}]` implies `Avoid ∈ FP^NP_tt` -- Ren-Williams Question 5.3 -- must be non-relativizing." **Non-adaptivity is the whole separation:** Lemma W16.1 is *false against adaptive queries, and must be* -- an adaptive algorithm picks `Π_{i+1}` after learning whether `S ∩ Π_i ≠ ∅`, which is precisely Korten's prefix search. The gap is **one round against `O(n + log T)` rounds** (RW26 Thm 3.1).

### 3.3 The reconstruction sub-line (W17, W18)

**W17** (f8e78a6) asked whether the residue can supply its own randomness; outcome 17b. Its Lemma W17.1 was **withdrawn mid-round** (RW26's PCP proof is succinct, so `S = poly(e, log t) << t` and the Shannon ceiling does not bite). The replacement located the failure at the base case via a requirement that compounds backwards, `H_0 ≥ c^k · H_k`. **W18 then superseded even that**, by reading RW26 directly:

> **Theorem W18.1** (4150bb8). "In the iterative win-win, a string hard enough to derandomise the reconstruction of stage `i` is already hard enough to run Korten at stage `i+1` directly. Hence the reconstruction can never be derandomised by the residue."

*Proof shape.* `Recon_i` is invoked **exactly** in the branch where `BF_{i+1}` *fails*, i.e. exactly where `f_{i+1}` is easy. Its last query has Merlin sending a circuit `C` representing `Π_C` which **Arthur evaluates**, so the fooled predicate has size ≥ `|C|` ≥ the stage-`(i+1)` easiness threshold -- precisely what Korten consumes to solve AVOID at `n_{i+1}` outright, in which case the branch was never taken. **The residue is easy exactly when its randomness is needed.** Parameter-free: no loss exponent, no stage count, no seed length, no base hardness. **Corollary: the status quo `E^{prMA}/1` is the fixed point.**

Three premises that both the reviewer and I had been arguing from were struck against RW26's text: the base is **brute force** ("`r_0 = 0, s_0 = 0` ... `BF_0` ... enumerates every string in `{0,1}^{n_0}`"), so there is no hard base string; **Arthur evaluates** Merlin's circuit; and RW26's `s_i` is the **NP-query witness length** (`s_{i+1} := max{s_i, n_{i+1}}`), not a hardness threshold. **From here: `s_i` = query length, `h_i` = hardness threshold.**

## §4. The boundary: plain circuits vs single-valued nondeterministic circuits

This is where the line has arrived from every direction it has taken. **Five independent arrivals:**

1. **SU05's own open problem.** Shaltiel-Umans, *Pseudorandomness for Approximate Counting and Sampling*. Definition 2.4, verbatim: "A language L is worst-case hard for exponential-size (deterministic, nondeterministic, co-nondeterministic, SV-nondeterministic, adaptive or nonadaptive SAT-oracle -) circuits if there exists a constant ε > 0 such that for every sufficiently large n, every circuit of the prescribed type and size at most `2^{εn}`, fails to compute L restricted to inputs of length n." **Linear-exponential** -- the W5 correction, and the same scale as Korten's `2^{Ω(n)}`.
2. **RW26 Question 5.3** (= (D2)), verbatim: "What is the weakest circuit lower bound assumption that implies `AVOID ∈ FP^NP_tt`?" -- with §1's minimality sentence and its "(not SVN circuits!)".
3. **Dermer-Shaltiel TR26-017**, *Multiplicative Pseudorandom Generators for **Nondeterministic** Circuits*. Their Informal Theorem 1.8, verbatim: "'Black box techniques' cannot give a version of Theorem 1.7 in which ϵ = 1, δ = `s^{−ω(1)}`, and all occurrences of 'nondeterministic circuits' are replaced by 'deterministic circuits'. Furthermore, this holds even if the seed length r is increased to r = Ω(s)."
4. **van Melkebeek-Sdroievski, CCC 2023** -- targeted hitting-set generators "based on probabilistically checkable proofs for **nondeterministic** computations", in the **AM** setting.
5. **SU05 Theorem 4.10**, verbatim: "If `E^NP` requires exponential size SV-nondeterministic circuits, then there is a deterministic procedure with access to an NP-oracle that learns an unknown Boolean circuit C of size s on n inputs in time poly(s, n) **using equivalence queries**."

> **Correction to the reviewer's citation, recorded because Flag Y18 exists for exactly this.** The reviewer supplied (5) as "SU05 Theorem 3.16". In the copy read here it is **Theorem 4.10**, in §4.6 "Learning circuits in `P^NP`", and the reviewer's paraphrase **dropped the tail "using equivalence queries"**. That tail matters: 4.10 is *not* a membership-query learner, and the reviewer's own observation -- that "`h(x) ≠ f_{i+1}(x)`" has no short certificate, so equivalence queries are unavailable as plain NP queries -- is precisely why. The arrival is real; the statement must carry its hypothesis.

**What W16.2 adds.** Not just that the boundary is hard to cross, but that **relativizing technique cannot cross it**: (D2) from plain-circuit hardness needs a non-relativizing proof. And what W18.1 adds: the win-win's own branch structure cannot cross it either, for reasons with no parameters in them.

**Also on the record:** RW26 Question 5.2 (the `searchSAT` analogue), verbatim: "What is the weakest circuit lower bound assumption that implies `searchSAT ∈ FP^NP_tt`?" -- with their remark that "we only know that `searchSAT ∈ FP^NP_tt` under lower bounds against single-valued nondeterministic (SVN) circuits [AK01; KM02; MV05; SU06]. It is unclear whether such a strong derandomization assumption is necessary." **5.2 is `searchSAT`, 5.3 is AVOID; (D2) = 5.3.** The W15-era note recording (D2) as 5.3 is correct and the W18 discrepancy is closed.

## §5. Named open statements smaller than the door

| code | statement | status |
|---|---|---|
| **(S1)** | `AC^0`-Avoid at polynomial stretch | open; not attacked by this line |
| **(S2)** | `NC^0_3`-Avoid in the window `(n + n^{2/3}, n^{1.4})` | open; not attacked by this line |
| **(D1)** | approximate counting in `P^NP` | **NOT smaller than the door.** W5 correction: (D1) *implies* (C_1) and is not known to follow from it, since (C_1) is provably minimal. Instrument: SU05 Thm 3.6 / Cor 3.7, hypothesis = SVN hardness |
| **(D2)** | = RW26 **Question 5.3**: weakest lower bound giving `Avoid ∈ FP^NP_tt` | open, and now **barriered**: W16.2 says any proof from plain-circuit hardness must be non-relativizing. The gap located in W15: the isolation-failure test is **coNP-type** (Π_1), and plain hardness is not known to fool coNP |
| **(D3)** | a history-hardness notion whose failure is NP-certifiable | open; **the W20 target**, RW26's own words below |
| **Korten Problem 1** | black-box depth lower bound for the stretching reduction | open. At **depth 1** reduced to the dangerous-string residue (§3.1); glue-class-restricted form (NC^0/AC^0) is the sharpened target from W7 |

**(D3) verbatim, RW26 §5, immediately after Question 5.3** -- this is the W20 statement:

> "It is conceivable that with a better hardness-randomness tradeoff than Jeřábek-Korten, we will be able to obtain a better uniform reconstruction algorithm, hence a better near-maximum circuit lower bound. Let Π be an encoded computational history, then either Π is 'hard enough' to solve AVOID, or Π is 'easy' so that one can 'reconstruct' Π efficiently. **Is there a suitable definition of 'hardness' so that any 'hard enough' Π can be used to solve AVOID in `FP^NP_tt`, while Π being 'easy' implies an efficient MA algorithm for reconstructing Π?**"

**Two constraints any W20 candidate must respect**, and they are this line's own results: **Theorem W16.2** (the `FP^NP_tt` half cannot be reached from plain-circuit hardness by a relativizing proof) and **Theorem W18.1** (the reconstruction cannot be derandomised by the residue, because the branch needing randomness is the branch without it).

## §6. Practice lines, and the calibration record

**Practice lines, each earned by a specific error:**

1. **Never reconstruct a dropped superscript inside a quotation** -- mark it lost or check a second extractor. *(W5: I wrote SU05 Def 2.4 as `2^{n^ε}`; it is `2^{εn}`. Caught by the reviewer.)*
2. **Do the counting before the prior, and count removability, not just origin.** *(W6: Flag E6 predicted the `n` term was the stubborn one; RW26 Thm 5.1 removes it.)*
3. **The lever is invariant-maintainability, not locality.** *(W8: local certificates essentially never exist.)*
4. **High multiplicity is an asset to whoever chooses, not an obstruction.** *(W9 Flag P9 and W13 Flag A13, the same error twice.)*
5. **`&&`-chain the guard; `set -e` does not gate.** *(Two commits landed with a failing guard, be8cffe and 77ac191. Chaining has held since.)*
6. **Run the positive control before reporting a uniform sweep.** *(W14.)*
7. **Audit the premises of a failure inequality before its arithmetic, and the step that looks like bookkeeping first.** *(W17: "both sides computed" is necessary and **not sufficient** -- I even flagged the wrong premise as load-bearing.)*
8. **Succinctness cuts both ways: name the scale and the time budget before asserting what a verifier contains.** *(W17 it shrank the verifier and killed Lemma W17.1; W18 it forced circuit evaluation and killed my refutation. Same property, same construction, opposite directions.)*
9. **The premise you did not think to write down is the one that breaks.** *(W18: Flag X18 caught the reviewer's premise and missed my own unstated `ℓ_i = n_i`.)*

**The calibration record, kept because it is the line's most reliable output.**

> **My constructions are reliable; my impossibility claims are not -- including ones expressed as inequalities with both sides computed.**

**Ten consecutive wrong impossibility claims**, every one a prediction that something would fail: four in W16 (the syntax/black-box "obstruction"; "the union bound cannot deliver claim (1)"; "a twenty-year-old open question's relativized form should not fall out easily"; the 16a prior of 25 against a correct ~45); three in W17 (the self-corrector as an extra obstruction; the i.o. structure as ill-defined; the hardness-notion mismatch "biting first"); three in W18 (the base-hardness margin; the `d ≥ ℓ` kill of the chained version; the refutation of the reviewer's fact (a)). **Lemma W17.1 belongs to the same species** -- an impossibility claim wearing a construction's clothes.

Against that, the positive contributions held: every theorem in §3; refuting the reviewer's two-chain adversary by pairwise conjunctions (W16); dropping its circular `q^2` threshold (W16); catching its Fix-2 counting, its W12.1 validity step, its `N/12` constant, its non-injective shortcut, its Fact (3) `k`-factor (W9-W14); catching the `s_i` notational collision and the scale-condition symmetry (W18); and the SU05 Thm 4.10 citation correction above.

**On priors.** The reviewer has been better calibrated than me on the "something else" bucket (W17: my 38 vs its 27, both my named candidates wrong). W18's deliberate correction in the opposite direction (66/32 against 60/38) paid, and **was not extended** -- one success is not a licence.

## §7. PATH

**Where the line is.** The door is intact and minimal. Two routes to it have been closed by this line's own results -- **non-adaptive avoidance from plain hardness needs non-relativizing technique** (W16.2), and **the win-win cannot supply its own randomness** (W18.1) -- and every route examined has terminated at the same wall: **plain-circuit hardness versus single-valued-nondeterministic hardness**, five independent arrivals (§4), stated by RW26 themselves in the minimality sentence as "(not SVN circuits!)".

**Where it goes.** W20 opens **(D3)** as an attack: a history encoding whose "easiness" is NP-certifiable, constrained by W16.2 and W18.1. The honest prior, stated before that round opens: **the same wall is the likeliest destination**, since NP-certifiable easiness is a demand for a short certificate of a statement whose natural certificate is a circuit -- which is where SU05 Thm 4.10's equivalence queries, and RW26's Merlin, both sit. If W20 arrives there too, that is a sixth arrival and the right conclusion is that the wall is the problem, not the route.

**What would change the picture.** A non-relativizing technique for (D2); or a hardness notion for (D3) whose failure certificate is genuinely short; or -- the thing nobody has -- progress on the `E^NP` rung itself.
