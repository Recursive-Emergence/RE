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
