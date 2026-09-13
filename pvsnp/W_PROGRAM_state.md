# The W-line: program state

*W19, a consolidation round set by the reviewer. Documents only, no new attack. Written 2026-09-12 on branch `w19-program-state`. `formal/` closed. LOCAL commit only, no push.*

*W33, the second consolidation, also set by the reviewer, 2026-09-12 on branch `w33-consolidation`: adds W24-W32 (§3.4), updates the ceiling, ledger, open statements, practice lines and PATH. Nothing earlier on the page is revised except where marked "W33".*

**No priors are registered for this round.** Pre-registration exists to stop me fitting a prediction to a result; a consolidation page predicts nothing. Every statement below is quoted from its own page or its own primary, and where a statement could not be verified it is marked rather than smoothed.

---

## Ceiling, first

**The W-line has proved nothing about P vs NP, and nothing unconditional about circuit lower bounds.** What it has produced is: four lower bounds in a *black-box query model that dies under randomisation*; one relativized separation showing a published open question needs non-relativizing technique; and two structural impossibility results about a specific proof strategy. **The door (C_1) is exactly where it was when the line opened.** No rung of the ladder has been climbed by this line; the climbing was done by CHR24, Li24 and RW26, and this line has been mapping the walls.

Two standing caveats that apply to everything below:

- **Flag H7 (deterministic-only).** Every bound in §3.1 is against *deterministic* back-mappings. Guess-and-test sits in `FZPP^{NP^C}` at depth 0, so the black-box form of "hiding is depth" **dies under randomisation**. The sub-line's four theorems do not survive it.
- **Korten's Problem 1 is untouched.** The sub-line closed at depth 1 with generality unreached, by a stopping rule agreed in advance.

**W33 addition to the ceiling.** W24-W32 reopened depth 1 and produced more lower bounds **of the same kind**: deterministic, black-box, depth 1, stretch `n ↦ n+1` to `n ↦ n+2`. **Two of them are in the weaker membership-query model** (the single-value subclass of width-1 DNFs, which does **not** include NP^C queries). **The Definition 9 results are for restricted template classes, and the fan-in-2 theorem is conditional.** Nothing here reaches Korten's Problem 1 at polynomial fan-in, nothing survives randomisation, and **the door is unmoved.**

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

**Branches and commits.** `w5-counting-form` 18caadc; `w6-round-complexity` 5aef6d7; `w7-black-box-depth` b36ed25; `w8-depth-one-lemma` 659a442; `w9-projection-glue` 3f1f1e4; `w10-projection-closed` 4eec008; `w11-nc0-glue` 044d224; `w12-one-input-glue` f2231d6; `w13-depth-one-general` 50fd900; `w14-dangerous-strings` 242e2b3; `w15-isolation-from-hardness` 224d6af; `w16-relativized-separation` bc60bd8; `w17-residue-supplies-randomness` f8e78a6; `w18-loss-exponent` 4150bb8; `w19-program-state` c810c94 (this page); `w20-history-hardness` 13cb4b7 (priors at fd081c1 and ecf5475; findings at 13cb4b7). **w5-w14 are pushed to origin** (w14 ahead by 242e2b3); **w15-w20 are local and unpushed, awaiting the user's go.** The reviewer's `w1-range-avoidance` 267b85e (W1-W4) is its own branch and remains local by its call. **Nothing is merged; `main` is unchanged.**

**W33 ledger update.** `w21-nc03-window` (findings 8d7f7d7, page update 61114ec); `w22-sparsifiers` 374d097; `w23-cegis` 4c40c25; `w24-depth-one-reopened` f42275c; `w25-read-count` ff2f888; `w26-query-fanin` 99029ab; `w27-dnf-extension` 064811f; `w28-extendability` 54cdc5b; `w29-prepinning` c81d84d; `w30-residual-arity` 6765871; `w31-side-assignment` 6f67a20 (findings 24013f5; §10 bd3ca7b; **erratum §11 56e31c7**; gloss correction §12 6f67a20); `w32-correlated-assignment` 8c0fe2b (W32-A in `W32_fanin2.md`: pre-registration c97502b, findings 2749280, §10 946ce1e, §12 70d146e, residue §13 8c0fe2b; W32-B in `W32B_arity_k.md`, bounded round, 8c0fe2b); `w33-consolidation` (this update). **Only w5-w14 are on origin; w15-w33 are local and unpushed, awaiting the user's go. Nothing is merged.**

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

### 3.4 The black-box sub-line reopened (W24-W32) -- W33

**Setting throughout:** deterministic back-mappings, depth 1, stretch `n ↦ n+1` to `n ↦ n+2`, `n′ = n`, `N = 2ⁿ`, glue fan-in `k` (the number of C-inputs a C′-input reads). **Two models, which must never be merged.** The **membership model** has queries "is `v ∈ range(C)`?" (a single value at every input); a "no" answer is a win for Q. **Definition 9** has width-`w` DNF queries, and a single query can check "is `y ∈ range(C′)`" at width `k`.

**3.4.1 Membership model.**

> **Lemma W24.1** (f42275c; one-input templates). "A string serves at most one hint, so at most `2^{n+1}` of the `2^{n+2}` hints certify, and the adversary always has a non-certifying valid hint." *Not a new lower bound (W12.2 already holds); a one-line mechanism.*

> **Lemma W25.1** (ff2f888; q = 0, any glue, any fan-in). Certified hints `≤ 2N`, tight; at least `N` valid hints are non-certifying.

> **Finding W25.2** (ff2f888). A "no" answer is a win, so the transcript is all-yes and Q's queries plus its output form a set `V(y)` determined by `y` alone. Totality is **static set certification**. *Membership model only.*

> **Finding W25.3** (ff2f888). **At fan-in `N` depth 1 is easy**: `K_{4,4}` gives a total one-query template at n = 2 (verified over all 4096 `C`), and random 6-uniform hypergraphs give five-query totality for all `N ≥ 16`. **The fan-in bound is load-bearing for the whole black-box line.**

> **Theorem W26.1** (99029ab; any joint glue of fan-in `k`). **`(q + 1)·k ≥ 0.58·√N`.** Proof: a first moment under a random injection, with the precision gain `2^j` priced against `Pr[a window sees j elements] ≤ C(s, j)(k/2N)^j`. At `k = polylog N`: `q ≥ 2^{n/2 − O(log n)}`. **Tight at neither end.**

**3.4.2 Definition 9.**

> **W27** (064811f; negative). **Counting routes on invalid instances are vacuous at `w ≥ k`**: "is `y ∈ range(C′)`" is one width-`k` DNF, so a template-aware Q detects invalidity in one query. Targeted width-1 queries have influence 1/2 on the windows that read their positions.

> **Theorem W28.1** (54cdc5b; the hub-or-coarse dichotomy). Let `D` be the maximum input degree and `t_y` the maximum forbidden set, worst case over settings. If `D·t_y < 2N`, then `y` is valid and **`qw ≥ N/(D + 1)`**. *Hence a total template with small `qw` needs, at every hint, a hub or coarse glue.* Corollary: random joint glue needs `qw = Ω(N/(k + log N))`.

> **Theorem W29.2** (c81d84d; hub-plus-unary). If every window reads at most one input outside a set `H` of `h` inputs, then **`qw ≥ N/4 − h`**, for any pinned hub values, by a count over hints that is **the selection principle W14 said did not exist, for this class**. *Supporting:* Lemma W29.1 (pre-pinning, with the dangerous-string term `M_res` and the arity-≥2 degree `D′`).

> **Theorem W30.1** (6765871; class `D_res·t_res < 2(N − h)`). W29.1's hosting count with W28.1's extension on the residual. **Negative:** counting extension is impossible at arity 2 (a coarse row present at every hint), and clean pins need not be extendable.

> **Theorem W31.1** (24013f5, **erratum 56e31c7**; coarse rows at **bounded coarse-triple multiplicity**). Biased coin plus deterministic repair: **`qw ≥ (Nμ/4 − M_res)/(D′ + 1)`**, `μ = β^{D_out}(1 − β)^{D_in}`, under (C1) `D_in·p_cap ≤ μ/16` and (C2). *The erratum:* (C1) as first written (`μ/8`) left the proof with zero margin.

> **Theorem W32.1** (2749280, §12 70d146e; **all fan-in-2 glue, CONDITIONAL**). Pre-pin inputs of degree `> D*` with the lightest values; protected set (payers absorb coarse structure); random give-ups where payers cannot. **Under (H_casc): `qw ≥ c(D*)·N` for `N ≥ N₀(D*)`, `c = D*^{−O(D*)}`, `N₀ = D*^{O(D*)} log N`**, a proof-of-shape constant. The mass hypothesis was discharged in §12; the multiplicity gap closed via the protected set (star template, exact at N = 16: protected set `N/2` hosts at every hint, fair coin 0).

> **W32-B** (8c0fe2b; arity `k`, one bounded round, 32B-b). Strong independence is necessary under pre-committed payment. Paying every nonempty slice is destructive at arity 3 (exact at N = 9); **the survival product `M^{−kD*}` is vacuous at `k = polylog N`.**

**Coverage table (Definition 9, deterministic, depth 1):**

| glue class | result | status |
|---|---|---|
| single-call `(C(x), h(x))` | W8.1: `qw ≥ N − 1` | proved |
| projection | W10.3: `N/8` | proved |
| single-block / one-input per coordinate | W12.1 `N/3`, W12.2 `N/9` | proved |
| any fan-in, small worst-case forbidden sets | W28.1: `N/(D + 1)` | proved (class hypothesis checkable) |
| hub plus unary | W29.2: `N/4 − h` | proved |
| hubs plus arity-2 residual with small rows | W30.1 | proved (class) |
| arity-2 with coarse rows, bounded coarse-triple multiplicity | W31.1 | proved (class) |
| **all fan-in 2** | **W32.1: `c(D*)·N`** | **proved, unconditional (W34, bacbed4); proof-of-shape constant** |
| **all fan-in 3** (W35 d782bb5, W36) | **W36.1: `c₃(D*)·N`** | **proved at fixed `D*`, proof-of-shape** (density + assignment + split payment with per-(u, payer) coordination) |
| arity `k ≥ 4` with coarse slices | -- | **open**: hitting sets over `(k − 2)`-tuple keys; any W31-style bound is vacuous at `k = polylog N` |
| **polynomial fan-in, general glue (Korten Problem 1 at depth 1)** | -- | **open** |

**The adversary's toolkit as it now stands.** Wilson's clean-pin adversary with an extendability invariant (W28); counting over hints to choose `y` (W25-W29); pre-pinning hubs against the hint (W29); the protected set, an independent set whose coarse incidences are paid by partners with capacity `c = 1` (W32-A); random load-oblivious give-ups, whose losses multiply per window (W32-A §12). **Both sides' costs matter:** every device that removes values for extension removes strings for hosting (W30).

~~THE open object: forced chains~~ -- *superseded by W34 below; the paragraph is kept as written at W33.* **THE open object of the black-box sub-line: FORCED CHAINS** (W32-A §13). An exhausted input with a single allowed value whose row at the next window has size `2N − 1`, forcing the next input, and so on, for `N/2` inputs at every hint. **This is consistent with every count on the page and exactly tight on the link budget.** The hint budget is spent (about `0.4N` good hints remain), and recursing on the chain breaks `|U_v| ≥ N − h − M_res`. **Such templates probably remain non-total** (range elements certify no non-range string), **so the gap is in the construction, not known to be in the truth.**

**W34 update (bacbed4): FORCED CHAINS RETIRED.** A count over (hint, circuit) pairs (`Σ_y |F_y| ≥ 3N·(2N)^N`, uniform functions) gives at least `0.2N` hints of density `≥ 0.7 > e^{−1/2}`. Those hints are automatically non-certifying, and at the density-maximising hub branch every input keeps `≥ 1.4N` values, no chain is forced, and `M_res ≤ 0.713N`. **W32.1 is unconditional for fan-in 2.** **Open now:** arity `k` (the payer machinery only, since density removes exhaustion at every fan-in), the constant, randomisation, and depth `> 1`.

## §4. The boundary: plain circuits vs single-valued nondeterministic circuits

This is where the line has arrived from every direction it has taken. **Five independent arrivals:**

1. **SU05's own open problem.** Shaltiel-Umans, *Pseudorandomness for Approximate Counting and Sampling*. Definition 2.4, verbatim: "A language L is worst-case hard for exponential-size (deterministic, nondeterministic, co-nondeterministic, SV-nondeterministic, adaptive or nonadaptive SAT-oracle -) circuits if there exists a constant ε > 0 such that for every sufficiently large n, every circuit of the prescribed type and size at most `2^{εn}`, fails to compute L restricted to inputs of length n." **Linear-exponential** -- the W5 correction, and the same scale as Korten's `2^{Ω(n)}`.
2. **RW26 Question 5.3** (= (D2)), verbatim: "What is the weakest circuit lower bound assumption that implies `AVOID ∈ FP^NP_tt`?" -- with §1's minimality sentence and its "(not SVN circuits!)".
3. **Dermer-Shaltiel TR26-017**, *Multiplicative Pseudorandom Generators for **Nondeterministic** Circuits*. Their Informal Theorem 1.8, verbatim: "'Black box techniques' cannot give a version of Theorem 1.7 in which ϵ = 1, δ = `s^{−ω(1)}`, and all occurrences of 'nondeterministic circuits' are replaced by 'deterministic circuits'. Furthermore, this holds even if the seed length r is increased to r = Ω(s)."
4. **van Melkebeek-Sdroievski, CCC 2023** -- targeted hitting-set generators "based on probabilistically checkable proofs for **nondeterministic** computations", in the **AM** setting.
5. **SU05 Theorem 3.16 (CCC'05 conference) = SU06 Theorem 4.10 (journal, §4.6 "Learning circuits in `P^NP`")**, verbatim: "If `E^NP` requires exponential size SV-nondeterministic circuits, then there is a deterministic procedure with access to an NP-oracle that learns an unknown Boolean circuit C of size s on n inputs in time poly(s, n) **using equivalence queries**."

> **Correction, in two parts, the second amended after the reviewer's ruling.**
>
> **(a) The dropped clause, which stands.** The reviewer's paraphrase of (5) **omitted the tail "using equivalence queries"**. That tail is load-bearing: the theorem is *not* a membership-query learner, and the reviewer's own observation -- that "`h(x) ≠ f_{i+1}(x)`" has no short certificate, so equivalence queries are unavailable as plain NP queries -- is precisely why. The arrival is real; the statement must carry its hypothesis.
>
> **(b) The number, and this page had the cause wrong.** As first written, this note reported that the reviewer cited "Theorem 3.16" where the source says "Theorem 4.10", implying a citation error. **It is a version split, and neither of us mis-transcribed:** Thm **3.16** in the CCC 2005 conference version, Thm **4.10** in the journal version's §4.6, same sentence in both. Corrected here rather than silently, because a reference page that mis-attributes a version difference as someone's error is worse than one that says nothing. **Cited in both forms from here.**
>
> *(Flag Y18 still earned its keep: going to the source is what surfaced the dropped clause, which was a real defect. The method that found it -- when a cited number will not resolve, search what the theorem **says**, not what it is **called** -- is adopted, and it is also what explains why W5's cited Thm 3.11/3.15 did not match this copy.)*

**What W16.2 adds.** Not just that the boundary is hard to cross, but that **relativizing technique cannot cross it**: (D2) from plain-circuit hardness needs a non-relativizing proof. And what W18.1 adds: the win-win's own branch structure cannot cross it either, for reasons with no parameters in them.

**Also on the record:** RW26 Question 5.2 (the `searchSAT` analogue), verbatim: "What is the weakest circuit lower bound assumption that implies `searchSAT ∈ FP^NP_tt`?" -- with their remark that "we only know that `searchSAT ∈ FP^NP_tt` under lower bounds against single-valued nondeterministic (SVN) circuits [AK01; KM02; MV05; SU06]. It is unclear whether such a strong derandomization assumption is necessary." **5.2 is `searchSAT`, 5.3 is AVOID; (D2) = 5.3.** The W15-era note recording (D2) as 5.3 is correct and the W18 discrepancy is closed.

## §5. Named open statements smaller than the door

| code | statement | status |
|---|---|---|
| **(S1)** | `AC^0`-Avoid at polynomial stretch | open; not attacked by this line |
| **(S2)** | `NC^0_3`-Avoid stretch regime | **RESHAPED (W21, 8d7f7d7). NOT A WINDOW.** Hardness is a **curve**: stretch `n + O(n^{2/(2+δ)})` buys `(n^δ/10, n^{δ−1/2}/10)`-rigidity for `1/2 ≤ δ ≤ 1` (GGNS23 Thm 3.2), with `δ = 1` Valiant's application and `δ = 5/6` the `n^{12/17}` remark. Algorithms are **four statements, all at multiplicative stretch**, none in the additive regime where the payoff lives, so closing the unconditional end below `Õ(n^{1.4})` buys nothing for rigidity. Algorithmic end limited by the cell-probe bound itself, with a **natural-proofs barrier on its improvement** (KPI25 Thms 5(2), 6(2)); hardness end limited by the **rigidity target**, not the AIK encoding. One unbarriered statement: **RSW22 Thm 3.12** (FP^NP CSP sparsifiers). *Off the door: payoff is rigidity / Valiant-style linear-circuit lower bounds, not (C_1).* |
| **(D1)** | approximate counting in `P^NP` | **NOT smaller than the door.** W5 correction: (D1) *implies* (C_1) and is not known to follow from it, since (C_1) is provably minimal. Instrument: SU05 Thm 3.6 / Cor 3.7, hypothesis = SVN hardness |
| **(D2)** | = RW26 **Question 5.3**: weakest lower bound giving `Avoid ∈ FP^NP_tt` | open, and now **barriered**: W16.2 says any proof from plain-circuit hardness must be non-relativizing. The gap located in W15: the isolation-failure test is **coNP-type** (Π_1), and plain hardness is not known to fool coNP |
| **(D3)** | a history-hardness notion whose failure is NP-certifiable | **NARROWED** by W20 (13cb4b7) -- split into two variants, one closed within the framework and one open; see below |
| **Korten Problem 1** | black-box depth lower bound for the stretching reduction | open. At **depth 1** reduced to the dangerous-string residue (§3.1); glue-class-restricted form (NC^0/AC^0) is the sharpened target from W7. **W33:** at depth 1, Definition 9, fan-in 2 is closed (W32.1, unconditional after W34); polynomial fan-in with coarse slices is open; the membership-model analogue has the lower bound `q = Ω̃(√N)` at poly fan-in (W26.1), truth `N` vs `√N` open. |

**(D3) after W20, in two variants that must be kept apart.** *Status: **narrowed**, not closed -- the word is chosen deliberately and the distinction is the ceiling.*

- **(D3-door)** [`FP^NP` reconstruction]: **closed within the RW26/CHR framework.** It is equivalent there to deterministic polynomial-time CAPP for the verifier family `{V^C}` on `polylog(t)` coins (W4 §2, quantified in W20 §7), and both known sources of such an algorithm are closed: a hard string inside the win-win (**Theorem W18.1**) and a plain-hardness hypothesis (dominated by **Korten Theorem 10**). **This is not an impossibility theorem.** A new framework, or an unconditional CAPP algorithm for that family, would reopen it.
- **(D3-RW)** [MA reconstruction, hard `⇒ FP^NP_tt`]: **open**, and equal to RW26's Question as stated -- with **W16.2**'s constraint that the "hard `⇒ FP^NP_tt`" step from plain-circuit hardness must be non-relativizing.

**(D3) verbatim, RW26 §5, immediately after Question 5.3** -- the statement both variants come from:

> "It is conceivable that with a better hardness-randomness tradeoff than Jeřábek-Korten, we will be able to obtain a better uniform reconstruction algorithm, hence a better near-maximum circuit lower bound. Let Π be an encoded computational history, then either Π is 'hard enough' to solve AVOID, or Π is 'easy' so that one can 'reconstruct' Π efficiently. **Is there a suitable definition of 'hardness' so that any 'hard enough' Π can be used to solve AVOID in `FP^NP_tt`, while Π being 'easy' implies an efficient MA algorithm for reconstructing Π?**"

**Two constraints any W20 candidate must respect**, and they are this line's own results: **Theorem W16.2** (the `FP^NP_tt` half cannot be reached from plain-circuit hardness by a relativizing proof) and **Theorem W18.1** (the reconstruction cannot be derandomised by the residue, because the branch needing randomness is the branch without it).

## §6. Practice lines, and the calibration record

**Practice lines, each earned by a specific error:**

1. **Never reconstruct a dropped superscript inside a quotation** -- mark it lost or check a second extractor. *(W5: I wrote SU05 Def 2.4 as `2^{n^ε}`; it is `2^{εn}`. Caught by the reviewer.)*
2. **Do the counting before the prior, and count removability, not just origin.** *(W6: Flag E6 predicted the `n` term was the stubborn one; RW26 Thm 5.1 removes it.)*
3. **The lever is invariant-maintainability, not locality.** *(W8: local certificates essentially never exist.)*
4. **High multiplicity is an asset to whoever chooses, not an obstruction.** *(W9 Flag P9 and W13 Flag A13, the same error twice.)*
5. **Put EVERY command in the `&&` chain. A newline is not a gate.** *(Three commits have now landed with a failing guard: be8cffe and 77ac191, where `set -e` failed to gate; and **`ecf5475`**, where the guards sat at the head of an `&&` chain but the following commands were written on **new lines**, which bash runs unconditionally — so the chain short-circuited past the intended commit while the newline-separated commands ran anyway, force-moving a branch ref with a stale `HEAD` into the bargain. The earlier version of this line said "chaining has held since", and that was **wrong within the same session**. The rule is not "use `&&` somewhere"; it is that a guarded sequence is **one chain, end to end**.)*
6. **Run the positive control before reporting a uniform sweep.** *(W14.)*
7. **Audit the premises of a failure inequality before its arithmetic, and the step that looks like bookkeeping first.** *(W17: "both sides computed" is necessary and **not sufficient** -- I even flagged the wrong premise as load-bearing.)*
8. **Succinctness cuts both ways: name the scale and the time budget before asserting what a verifier contains.** *(W17 it shrank the verifier and killed Lemma W17.1; W18 it forced circuit evaluation and killed my refutation. Same property, same construction, opposite directions.)*
9. **The premise you did not think to write down is the one that breaks.** *(W18: Flag X18 caught the reviewer's premise and missed my own unstated `ℓ_i = n_i`.)*

**W33: practice lines earned in W20-W32**, with the error behind each:

10. **Name the scarce resource before ruling on a component; the framing audit must precede the mechanism's pricing.** *(W20.)*
11. **Suspect a version split before an error when two careful readers disagree.** *(W19/W21.)*
12. **A calibration asymmetry is indexed to a source, not a subject matter.** *(W22.)*
13. **A verified premise does not license its consequence.** *(W23.)*
14. **A lower bound is a statement about `U`, not about one `Q`'s path; track the side effects of your own commitments.** *(W24.)*
15. **Price every resource a statement quantifies over before counting under it.** *(W25: fan-in independence was the reason the count stopped at q = 0.)*
16. **The obstruction may be the model's, not the problem's; price a mechanism against the probability of each case, not its worst case.** *(W26.)*
17. **Price a mechanism against the adversary it actually faces; a heuristic search's failure to find is not a measurement of absence.** *(W27: targeted queries; the "products shrink at fan-in 3" artefact.)*
18. **A definition quantified over everything is usually too strong for an adversary that needs only what it chooses, and a conclusion quantified over the adversary's choices must survive the opponent's.** *(W28: the radius; the `N/2` threshold.)*
19. **A proof step can fail while the conclusion holds; check your own correction with the audit you gave the original.** *(W29.)*
20. **Every device that removes values for extension also removes strings for hosting.** *(W30: the smart zero-query Q.)*
21. **A greedy step that is correct in code can be unprovable: split it into independent randomness plus a counted repair.** *(W31.)*
22. **Audit the quantity the argument needs, not the term you defined for it; write out every Markov step with its average.** *(W32: mass at partners vs `c(y, v)`; triples vs windows; the heavy-window average was exactly `N`.)*

**Miss counts, W24-W32, both sides, as each recorded them.** **The reviewer: fifteen misses** by its own count, including the `1 + log r` parametrisation, "single-call", three wrong count arguments in W25, the precision middle, the radius, the `N/2` threshold, "killing is not required", self-exclusion's sum-versus-max, must-exclude by size, the cascade audit, the additive give-up claim, and the polynomial-in-`D*` confirmation. **Mine, comparable in number:** the lazy-hosting cross-history reading, a flat search score, "membership is Definition 9 at `w = 1`", the placement detour, two mis-stated W27 obstacles, the `N^{1/k}` exponent, the fan-in-3 "shrink" artefact, the width-1 detection side-claim, "projection: restrict", "forced exclusions only help", **the W31.1 (C1) arithmetic (a proof that did not close as committed)**, the capacity max error, the heavy-window Markov step, the parity-hub `N/4` over-count, and the "bounded degree" gloss (shared). **Two mechanisms of the reviewer's survived audit (the multiplicative recombination and the protected set), and both were counts over objects already measured.**

**The calibration record, kept because it is the line's most reliable output.**

> **My constructions are reliable; my impossibility claims are not -- including ones expressed as inequalities with both sides computed.**

**Ten consecutive wrong impossibility claims**, every one a prediction that something would fail: four in W16 (the syntax/black-box "obstruction"; "the union bound cannot deliver claim (1)"; "a twenty-year-old open question's relativized form should not fall out easily"; the 16a prior of 25 against a correct ~45); three in W17 (the self-corrector as an extra obstruction; the i.o. structure as ill-defined; the hardness-notion mismatch "biting first"); three in W18 (the base-hardness margin; the `d ≥ ℓ` kill of the chained version; the refutation of the reviewer's fact (a)). **Lemma W17.1 belongs to the same species** -- an impossibility claim wearing a construction's clothes.

Against that, the positive contributions held: every theorem in §3; refuting the reviewer's two-chain adversary by pairwise conjunctions (W16); dropping its circular `q^2` threshold (W16); catching its Fix-2 counting, its W12.1 validity step, its `N/12` constant, its non-injective shortcut, its Fact (3) `k`-factor (W9-W14); catching the `s_i` notational collision and the scale-condition symmetry (W18); and the SU05 Thm 4.10 citation correction above.

**W33 amendment to the calibration record.** W24-W32 changed its shape. **Impossibility theorems that went through a full audit held** (W26.1, W28.1, W29.2, and W32.1 conditionally), and one needed an erratum before its proof closed (W31.1). **Impossibility FORECASTS that were not audited kept failing**: priors weighted toward "nothing extends" (27c at 52, 30b at 68), "products shrink at fan-in 3", the §1 capacity objection, and the heavy-window step. **The honest statement is no longer "my constructions are reliable and my impossibility claims are not".** It is: **audited statements hold on both sides; unaudited forecasts fail on both sides, and the reviewer's unaudited mechanisms fail in their middles at about the same rate as my unaudited objections.** **And most audited statements needed a correction from the other side before they held:** W28.1's threshold (the reviewer's, corrected by me), W29.1's `M_res` term (mine, which the reviewer's specification lacked), W31.1's Step B (my erratum, caught while re-deriving for the reviewer's recombination), W32.1's heavy-window step (failed when the reviewer asked for it written out), and W26.1's two wording corrections. W29.2 held as first stated. **The reliable unit is the cross-audit, not the author: a statement counts once the other side has re-derived the quantity the argument needs.** *This amendment replaces the W16-era line above.* (Clause added at the reviewer's request; the record supports it.)

**On priors.** The reviewer has been better calibrated than me on the "something else" bucket (W17: my 38 vs its 27, both my named candidates wrong). W18's deliberate correction in the opposite direction (66/32 against 60/38) paid, and **was not extended** -- one success is not a licence.

## §7. PATH

**Where the line is.** The door is intact and minimal. Two routes to it have been closed by this line's own results -- **non-adaptive avoidance from plain hardness needs non-relativizing technique** (W16.2), and **the win-win cannot supply its own randomness** (W18.1) -- and every route examined has terminated at the same wall: **plain-circuit hardness versus single-valued-nondeterministic hardness**, five independent arrivals (§4), stated by RW26 themselves in the minimality sentence as "(not SVN circuits!)".

**Where it goes.** W20 opens **(D3)** as an attack: a history encoding whose "easiness" is NP-certifiable, constrained by W16.2 and W18.1. The honest prior, stated before that round opens: **the same wall is the likeliest destination**, since NP-certifiable easiness is a demand for a short certificate of a statement whose natural certificate is a circuit -- which is where SU05 Thm 4.10's equivalence queries, and RW26's Merlin, both sit. If W20 arrives there too, that is a sixth arrival and the right conclusion is that the wall is the problem, not the route.

**What would change the picture.** A non-relativizing technique for (D2); or a hardness notion for (D3) whose failure certificate is genuinely short; or -- the thing nobody has -- progress on the `E^NP` rung itself.

**PATH as of W33.**

```
door (C_1): E^NP ⊄ SIZE[2^{o(n)}]  ⟹  Avoid ∈ FP^NP        [Korten; minimal]
   ^ climbed to E^{prMA}/1 by RW26, not by this line
   |
   +-- (D2)/(D3): walled at plain-vs-SVN (W16.2, W18.1, W20)
   +-- (S2) NC^0_3 stretch: reshaped into a curve; algorithmic end barriered (W21-W23)
   |
   `-- Korten Problem 1 (black-box depth of the stretching reduction)
          |  WEAKEST ARROW  v
          |  black-box, deterministic, depth-1 lower bounds  --/-->  anything about FP^NP
          |
          +-- membership model: W26.1, q = Ω̃(√N) for poly fan-in        [lower bound; N vs √N open]
          `-- Definition 9, depth 1:
                 W28.1 (small rows) · W29.2 (hub + unary) · W30.1 · W31.1 (bounded multiplicity)
                 W32.1: all fan-in 2, unconditional (W34 density count)
                 W35: arity 3 reduced to split-payment collisions (bounded multiplicity)
                 W36.1: all fan-in 3 at fixed D*
                 OPEN: arity >= 4 tuple-key hitting sets · the constant
```

**The weakest arrow is the one from the black-box sub-line to the door**, and it is weak three times over. (1) Black-box lower bounds constrain one **technique** (stretching by oracle calls with glue), not `FP^NP`. (2) By Flag H7 they die under randomisation at this stretch. (3) Korten's Problem 1 asks for depth `d` against `log_α β`; **W24-W32 are all at depth 1**, and even a complete depth-1 answer at polynomial fan-in would be one instance of it. **Every result in §3.4 sits below that arrow.**

**W34 note:** the reviewer chose (a) under the standing rule, subject to the user's override, and W34 closed it (fan-in 2 unconditional). The user's choice between further black-box rounds and the door stands. **The decision as written at W33:** After W33 the line either (a) **attacks forced chains** directly (the fan-in-2 case's last open object, sharply stated, with a clean kill template), or (b) **returns to the door**, where §4's boundary and §5's (D2)/(D3) rows stand as W19-W20 left them. The reviewer will put the choice to the user with this page. **Nothing is merged, and w15-w33 are unpushed.**

**W36: THE BLACK-BOX SUB-LINE RESTS.** Final ledger: **W26.1** (membership model, any fan-in, `(q+1)k ≥ 0.58√N`); **W28.1** (Definition 9, small rows, `N/(D+1)`); **W29.2** (hub plus unary, `N/4 − h`); **W32.1** (fan-in 2, unconditional, `c(D*)·N`); **W36.1** (fan-in 3, `c₃(D*)·N`). **Open:** arity `≥ 4` (tuple-key hitting sets), the constants, randomisation, depth `> 1`. Everything is deterministic, depth 1, and below the weakest arrow. **The next move -- the door, or rest -- is the user's; no W37 is opened.**

**W37 (reading round, 37c): the smallest nameable target resolves, and the map of named targets is CLOSED.** (D3-door) = (CERT) is **white-box** (W20 §7, "given the circuit"). Perfect completeness plus exact low-degreeness of RW26's honest proof make each reconstruction query a `Σ₂` query (`∃C` [exactly low-degree ∧ `∀z` accepts ∧ prefix]). **The gap between that `Σ₂` reconstruction and the door is exactly: derandomise a universal quantifier over `polylog(t)` coins against an existentially chosen size-`S` circuit** -- white-box CAPP for the family, dominated by the door. **Every named target is now a boundary object** (plain-vs-SVN six times, `Σ₂`-vs-NP once) **or below the weakest arrow.** Next: (S1), the one named open statement never audited (W38).
