# W22: FP^NP CSP sparsifiers -- the one unbarriered statement. Pre-registration

*Drafted 2026-09-12 on branch `w22-sparsifiers`, on the reviewer's W22 specification, after W21 closed at `8d7f7d7`. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any new primary for this round.** *(The qualifier "new" is doing real work -- see §2(a).)*

## §0. Ceiling, and why this target was chosen

**Still off the door** (W21's Flag E21 carries forward): the payoff is rigidity and Valiant-style linear-circuit lower bounds, not (C_1).

**Why this and not the other end.** W21 pinned both ends of (S2) and found the algorithmic end limited by the cell-probe bound with a **Razborov-Rudich barrier** sitting on exactly the improvement it needs (KPI25 Thm 6(2)). The sparsifier route is the **one statement found with no barrier attached**, and the gap is a **derandomisation** rather than a lower bound. That is the whole reason it is the target.

**What would follow.** By RSW22 **Theorem 3.12**, an FP^NP construction gives FP^NP algorithms for `NC^0_c`-Avoid at stretch `n^{1+γ}` -- RSW22's Conjecture 3.8, which Li-Zhong call "a central open question". **That still does not reach the additive regime where rigidity lives** (W21 §7.3), so even 22a would not give Valiant's application. Saying so now, because the temptation at the end of a round is to let the payoff inflate.

## §1. The target, stated exactly

> **Definition 3.9** (RSW22). A `k`-CSP is a `k`-uniform **directed** hypergraph `G = (V,E)` with a predicate `P : {0,1}^k → {0,1}`; `value_{G,P}(α) := (1/|E|) Σ_{(v_1,…,v_k) ∈ E} P(v_1,…,v_k)`. A sub-hypergraph `G' = (V, E' ⊆ E)` is a **`P`-sparsifier with error `ε`** if `|value_{G',P}(α) − value_{G,P}(α)| ≤ ε` **for every assignment** `α : V → {0,1}`.

> **Theorem 3.12** (RSW22). "Suppose that for every constant `k ≥ 1`, there is an **FP^NP algorithm** that given any `k`-uniform directed hypergraph `G` and any predicate `P : {0,1}^k → {0,1}`, outputs a `P`-sparsifier of `G` with error `ε = 0.5` using `Õ(n)` hyperedges. Then for every constants `γ > 0` and `c ≥ 2`, there is an FP^NP algorithm for `C`-Avoid, where `C` is the family of `NC^0_c` circuits with stretch `n^{1+γ}`."

**The object to construct:** for each constant `k` and predicate `P`, an NP-oracle algorithm outputting `Õ(n)` hyperedges preserving the satisfied fraction to within **additive `0.5`**, **uniformly over all `2^{|V|}` assignments**.

## §2. Disclosure

**(a) CONTAMINATION, and it is substantial -- larger than W21's.** I have **already read, verbatim, in W21**: Definition 3.9, Remark 3.10, Theorem 3.11's *statement*, Theorem 3.12, and Conjecture 3.8. They are quoted in `8d7f7d7`. So the reviewer's named primary "RSW22 §3.3 verbatim" is **mostly already in hand**, and this round cannot claim to have discovered any of it. What I have **not** read: **Theorem 3.11's proof**; **BST19**'s exact guarantee; **PZ21** and what randomness its construction actually uses; the deterministic-hypergraph-sparsification literature.

**(b) My one observation, disclosed before pricing because it moves my 22a above the reviewer's.** The required error is **additive `0.5` on a quantity in `[0,1]`**. That is enormous slack -- a 50% additive error. So the difficulty cannot be approximation *quality*; it must be entirely the **uniformity over `2^{|V|}` assignments** with only `Õ(n)` edges. If that reading is right, the obstruction is a **covering/union-bound** question rather than a counting one, which is *not* where the reviewer expects 22b to land (it expects approximate counting, i.e. (D1)). **This is a guess about which constraint binds, and it is exactly the kind of guess W21 taught me to test rather than price.** Flag F22.

**(c) The reviewer's expected wall, recorded as its prediction, not inherited.** It expects: counterexample-guided construction with the NP oracle as violation oracle, hitting the wall that Spencer-style pessimistic estimators are sums over all `2^n` assignments, hence `#P`-shaped and unavailable to an NP oracle -- so the derandomisation would need approximate counting, i.e. (D1), "unless the additive-0.5 slack lets a hitting-set argument replace it". **That parenthetical is my §2(b), and it is the crux between us.**

**(d) A route that could close 22a by literature rather than by construction.** Theorem 3.11 uses **BST19 hypergraph cut sparsifiers as a black box**, so a *deterministic* hypergraph cut sparsifier would close 22a through RSW22's own proof. Whether one exists is a question in spectral graph theory, not complexity -- deterministic **spectral** sparsifiers for *graphs* are known (Batson-Spielman-Srivastava); the hypergraph constructions I am aware of by name (Chen-Khanna-Nagda; Kapralov-Krauthgamer-Tardos-Yoshida; Jambulapati-Liu-Sidford) are randomised. **I have not checked whether any is deterministic, and "22a closes by citation" is a real outcome**, which is part of why my 22a is above the reviewer's.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **22a** an FP^NP or deterministic construction of Definition 3.9 sparsifiers (by construction **or by citation**) | 12 | **18** |
| **22b** a reduction of the construction to one named derandomisation or discrepancy statement, with the exact obstruction | 55 | **52** |
| **22c** other | 33 | **30** |

**Why 22a is 18, six above the reviewer.** Three stated reasons, and I want to be scored on each separately. (1) It is a **construction** question, my reliable half. (2) The **additive-0.5 slack is enormous** (§2(b)) -- the required guarantee is far weaker than a cut or spectral sparsifier, and RSW22's Remark 3.10 says so themselves: their definition is weaker than PZ21's and "using a weaker definition of sparsifiers makes it potentially easier to construct them". (3) **It can close by citation** (§2(d)) -- a deterministic hypergraph cut sparsifier already in the literature would finish it through Theorem 3.11's own proof, and I have not checked.

**Why 22b is 52, three below.** It is the "do the work" outcome and should carry most of the mass. I am marginally below the reviewer only because §2(b) and §2(d) move probability into 22a, not because I doubt the shape.

**Why 22c is 30, three below.** **I have no named mechanism for it.** W21's lesson was that a base-rate justification can be right about the bucket and wrong about the reason; the corollary is that without a mechanism I should not be above the reviewer here. The 30 is residual, not a view.

## §4. Flags

- **Flag A22 -- the uniform guarantee is the whole difficulty, and every step must account for it.** The requirement is over **all `2^{|V|}` assignments simultaneously**. Any construction, mine or quoted, must state explicitly how each step handles that quantifier. The reviewer set this as a kill test and it is the right one.
- **Flag B22 -- premise audit first, bookkeeping steps first.** Standing since W17.
- **Flag C22 -- framing audit before pricing any mechanism.** Standing since W20, sharpened in W21: the audit can *be* the finding.
- **Flag D22 -- stop-rule.** If 22a appears to close -- by construction *or by citation* -- **stop, send the construction or the reference, write nothing further** until the reviewer has checked it.
- **Flag E22 -- version-split discipline.** Earned twice (W19, W21). Any bibliographic disagreement is presumed an edition difference until shown otherwise; the fix is a dual citation.
- **Flag F22 -- test §2(b), do not assume it.** My "the slack is enormous, so the obstruction is covering not counting" is a **guess about which constraint binds**. It is the same species as the W20 mechanism that died of framing collapse. It gets tested against Theorem 3.11's actual proof before it is allowed to move anything.
- **Flag G22 -- do not let the payoff inflate.** Even 22a gives only `n^{1+γ}`, not the additive regime. (S2)'s rigidity payoff stays out of reach either way (§0).

## §5. Kill tests

- **(i)** RSW22 §3.3 read **including Theorem 3.11's proof**, which is the part I have not seen and the part that says what the randomness is actually doing.
- **(ii)** BST19's guarantee quoted verbatim, since it is the black box; and PZ21 checked for what its randomness is used for.
- **(iii)** The deterministic-hypergraph-sparsification literature swept (ECCC + arXiv, 2023-2026) **before** writing that no deterministic construction exists -- Flag D22 means this could close the round.
- **(iv)** Every construction step audited against Flag A22's `2^{|V|}` quantifier, in writing.
- **(v)** §2(b) tested explicitly and the result stated **in the same sentence as the finding**, whichever way it goes.
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Nothing from the door rounds (W15-W20) cited as evidence; different object.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 22b, with the obstruction named -- and it is REPRESENTATIONAL, which is neither the reviewer's prediction (counting) nor mine (covering). Both of us were wrong, and §2(b) is scored against me.** Flag D22 did not fire.

## §6. The chain is algorithmic, and my §2(a) suspicion was wrong

I suspected mid-round that the chain might be existential-only, because PZ21's theorems all read "G **admits** P-sparsification". **That is wrong at the link that matters, and I record it as wrong.**

> **BST19 Theorem 1.3** (verbatim). "Given an `n`-vertex hypergraph `H = (V,E)` of rank `r` and a parameter `ǫ > 0`, **in probabilistic polynomial time we can find** a subset `F ⊆ E` of size `|F| = O(nr · (1/ǫ²) log(r/ǫ))` such that, if we let `d = r|E|/|V|` be the average degree of `H`, and `c = |E|/|F|`, the following holds **with probability at least `1 − n^{−2}`**: `|ce_F(S) − e_E(S)| ≤ ǫd|S| + ǫvol(S)` `∀S ⊆ V`."

> **PZ21 Remark 5** (verbatim). "Throughout this paper we only discuss the existence of sparsifiers and do not mention the time complexity to find them. However, the (implicit) time complexity results from [7] apply in our more general setting as well since the sparsifiers we find are in fact the same sparsifiers for all predicates, including cuts."

So PZ21 is existential *in statement* and algorithmic *by inheritance*, and what it inherits from BST19 is **randomised**. **RSW22's Theorem 3.11 characterisation is fair** and needs no correction. *(Kill test (i) as I wrote it was unsatisfiable: RSW22 contains no proof of Theorem 3.11 -- it is a bare black-box citation. My §2(a) said the proof was what I hadn't read; it isn't there to read.)*

## §7. The obstruction, and neither of us predicted it

### (7.1) The deterministic route already exists -- for graphs

BST19 do not merely have a randomised construction. They have a deterministic one, in the same paper:

> **Theorem 1.1 (Deterministic Polynomial Time Construction)** (verbatim). "Given a graph `G = (V,E)` and a parameter `ǫ > 0`, **in deterministic polynomial time** we can find a subset `F ⊆ E` of size `|F| = O(n/ǫ²)` such that, if we let `L_G = D_G − A_G` be the Laplacian of `G` ... we have `2cD_G̃ − 2D_G − ǫD_G − ǫdI ⪯ cL_G̃ − L_G ⪯ ǫD_G + ǫdI`."

And its mechanism, verbatim: "Our proof is based on the online convex optimization techniques of Allen-Zhu, Liao and Orecchia", with **Theorem 3.1** playing adversary using the **PSD cost matrix** `C_t := 2d_max I + [[mL_{a_t,b_t} − L_G, 0], [0, mSL_{a_t,b_t} − SL_G]]`, and Theorem 3.2 (Allen-Zhu-Liao-Orecchia) supplying the regret bound over **density matrices**.

**So the target is not "invent a derandomisation". It is "extend BST19's own deterministic §3 construction from graphs to hypergraphs".**

### (7.2) Why it stops at graphs: there is no quadratic form

BST19's cut guarantee is extracted from the matrix inequality, verbatim: "The first inequality follows by **computing the quadratic forms** of (4) with the `±1` indicator vector `x := 1_S − 1_S̄` of `S`, and noting that `x^T L_G x = 4e_E(S)`".

For hypergraphs, they can only define an **analog**, verbatim:

> "In order to define a notion of spectral sparsification, we associate to a hypergraph `H = (V,E)` **the following analog of the Laplacian quadratic form, namely a function `Q_H`** such that `Q_H(x) = Σ_{e∈E} w_e · max_{a,b∈e} (x_a − x_b)²`."

**The `max` is the obstruction.** At `k = 2` each hyperedge has a single pair and `Q_H(x) = x^T L_G x` exactly. At `k ≥ 3` it is a **maximum of quadratic forms** -- convex, piecewise quadratic, and **not `x^T M x` for any matrix `M`**. The cut function is no better: `e_E(S)` counts hyperedges meeting both sides, which as a function of the indicator vector has degree `k`, not degree 2.

> **THE FINDING. The deterministic route is a matrix/PSD argument and requires its objective to BE a quadratic form. Hypergraph cut functions are not quadratic forms, only maxima of them, so there is no cost matrix to hand the regret-minimisation framework. Random sampling needs no such representation -- only a concentration bound, which applies directly to the set function. Hence: SAMPLING WORKS ON SET FUNCTIONS; THE KNOWN DERANDOMISATION WORKS ONLY ON QUADRATIC FORMS.**

### (7.3) This answers Flag A22, and reframes both predictions

Flag A22 demanded that every step say how it handles the `2^{|V|}`-assignment quantifier. The answer is the sharpest possible and it is the same fact:

- **Randomised route:** concentration plus a union bound over the `2^n` sets -- hence BST19's "with probability at least `1 − n^{−2}`".
- **Deterministic route:** the quantifier **collapses**. The single PSD inequality (4) implies the guarantee for **all `2^n` sets simultaneously**, because each set's guarantee is that one inequality evaluated at an indicator vector.

**So the `2^n` quantifier is handled REPRESENTATIONALLY, not by counting and not by covering.** The reviewer predicted the wall would be Spencer-style pessimistic estimators, `#P`-shaped sums over assignments. I predicted (§2(b)) a covering/union-bound obstruction licensed by the additive-`0.5` slack. **Neither is right.** The slack is genuinely large and genuinely irrelevant; the difficulty was never the error parameter or the union bound, but whether the objective has a matrix representation at all.

## §8. Flag D22 did not fire, and precisely why

Two citation-closure routes were checked and both are closed:

- **arXiv 2408.06146, "Spectral Sparsification by Deterministic Discrepancy Walk"** (Lau-Wang-Zhou): a unified **matrix** discrepancy framework, applications listed as unit-circle approximation, singular-value approximation, graphical spectral sketching, effective resistance sparsification. **Graphs and matrices only; no hypergraphs.** Consistent with §7.2 -- it is a matrix-discrepancy method, so it inherits the same representational requirement.
- **arXiv 2601.08111, "Derandomizing Matrix Concentration Inequalities from Free Probability"** (Wang-Lau-Zhou): deterministic matrix-Spencer and near-Ramanujan graphs. **No sparsification, no hypergraphs.**

**And BST19 do not pose the question.** Their Questions 1-4 concern unweighted sparsification for graphs, polynomial-time MSS sparsifiers for expanders, `Õ_{r,ǫ}(n)` weighted hypergraph spectral sparsifiers, and unweighted sparsification for hypergraphs -- "We provide a positive answer to all the above questions." **None asks for a *deterministic* hypergraph construction.** The `FP^NP` form is posed only by RSW22, as Conjecture 3.8 via Theorem 3.12.

*Stated with the right modality (kill test iii): no deterministic hypergraph construction surfaced in three targeted sweeps and neither lead reaches hypergraphs. That is "not found, and the two nearest methods are structurally graph-bound", not "proved not to exist".*

## §9. Scoring

| code | mine | reviewer | outcome |
|---|---|---|---|
| **22a** | 18 | 12 | **Did not fire.** **The reviewer's lower number was better, and my three stated reasons were each wrong or irrelevant** -- see §10. |
| **22b** | 52 | 55 | **The outcome**, with the obstruction named: **representational**, not counting (reviewer) and not covering (mine). |
| **22c** | 30 | 33 | No. |

## §10. Calibration, and this one costs me

**My 22a at 18 was too high, and each of the three reasons I recorded fails separately.** I want them scored individually because I asked for that in §3.

1. *"It is a construction question, my reliable half."* -- **Irrelevant here.** The standing asymmetry is about constructions **I produce**, not about the base rate that *someone* has produced one. I stretched a calibration line past its domain.
2. *"The additive-0.5 slack is enormous."* -- **True and irrelevant** (§7.3). The slack is real; the obstruction is orthogonal to it. This is my §2(b), and it is wrong in the specific way Flag F22 warned about: a guess about which constraint binds, priced before being tested.
3. *"It can close by citation."* -- **Legitimate, and it did not.** The only one of the three that was sound reasoning; it just came out negative (§8).

**So two of my three reasons were bad reasoning, not bad luck.** Reason 1 in particular is a new failure mode worth naming:

> **New line: a calibration asymmetry is indexed to a source, not to a subject matter.** "My constructions are reliable" is a statement about *my* output. It says nothing about whether a construction exists in the literature, and using it to price the latter is a category error. The asymmetry is about **who is making the claim**, not about **what kind of claim it is**.

**The reviewer's prediction was also wrong**, and symmetrically: it named counting, I named covering, and the answer was representation. **Neither of us considered that the objective might not have the right algebraic *type*.** That is the same class of miss as W21's -- both times the framing question ("is this the right kind of object?") mattered more than the quantitative one, and both times we reached for quantitative walls first.

**Impossibility-claim record unchanged at ten.** No impossibility claim of mine this round; §2(b) was a *mechanism* guess, which is the W20 category, and it failed the same way -- untested at pricing time.

## §11. What this leaves open, and the natural W23

1. **The precise question:** is there a deterministic (or `FP^NP`) construction of additive cut sparsifiers for **hypergraphs**? By §7.2 this needs either a matrix representation of hypergraph cuts, or a derandomisation technique that does not require one.
2. **The sharper version, which is the better target:** *does the Allen-Zhu-Liao-Orecchia regret framework extend to objectives that are maxima of quadratic forms?* That is a question about online convex optimisation, not about complexity, and it is where the (S2) route now terminates.
3. **An `FP^NP` shortcut that bypasses §7.2 entirely.** RSW22 ask for `FP^NP`, not determinism. An NP oracle *verifies* a candidate sparsifier in one query -- "`∃α` with `|value_G(α) − value_H(α)| ≥ 0.5`" is NP -- so counterexample-guided search is available even without a matrix form. **This is the reviewer's original idea, and §7.2 does not refute it**; it refutes the *derandomisation-of-BST19* route. Whether counterexample-guided search converges in polynomially many rounds is untouched by this round and is the one live thread.
4. **(S2) remains off the door** (Flag G22 / E21). Even 22a would give only `n^{1+γ}`, never the additive regime where rigidity lives.
