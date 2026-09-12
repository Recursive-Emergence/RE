# W23: does counterexample-guided search converge? Pre-registration

*Drafted 2026-09-12 on branch `w23-cegis`, on the reviewer's W23 specification, after W22 closed at `374d097`. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any new primary for this round.**

## §0. Ceiling

**Still off the door.** (S2)'s payoff is rigidity and Valiant-style linear-circuit lower bounds, not (C_1). Even 23a would give only `n^{1+γ}` -- never the additive regime where rigidity lives (W21 §7.3). Flag G22 carries forward.

**Why this target.** W22 found the derandomisation route blocked *representationally*: BST19's deterministic construction needs the objective to **be** a quadratic form, and hypergraph cut functions are not. **CEGIS is the one route that needs no matrix representation** -- an NP oracle verifies a candidate in one query. W22 refuted the derandomise-BST19 route only; this thread is untouched, and it is the reviewer's own idea.

**And the reviewer has pre-located the answer**, explicitly as "a prediction to score, not a finding". Its three routes and walls: (1) edge-player MW converges but the average is supported on all `m` edges -- **not sparse**; (2) assignment-player MW gives sparsity (Lipton-Young / Freund-Schapire) but the edge player's best response is `argmax_e Σ_α p_t(α)·loss(α,e)` -- **`#P`-shaped, = (D1)**; (3) `Θ(n)`-wise independence works but finding a seed is `Σ₂`, or a hitting set against NP-type tests -- **the SVN boundary**. Its prediction: a seventh arrival, from the (S2) side.

## §1. Refuted premises checked, and the lines that govern

Standing: ten consecutive wrong impossibility claims; positive constructions holding. Four lines now govern, each earned:

1. **The framing audit precedes the mechanism's pricing** (W20, sharpened W21: *it can be the finding*).
2. **Name the scarce resource before ruling on a component** (W17/W20).
3. **A calibration asymmetry is indexed to a SOURCE, not a subject matter** (W22, and it cost me directly: I priced 22a on "construction question, my reliable half", which says nothing about whether a construction exists in the literature).
4. **Suspect a version split before an error** (W19/W21).

**Line 3 binds hardest here.** 23a is a construction question and it is RSW22's *central open question*. **I must not inflate it on the asymmetry.** That is exactly the W22 error and it would be the second instance.

## §2. Disclosure

**(a) Contamination.** I have already read, verbatim in W22: RSW22 **Definition 3.9**, **Theorem 3.12**, **Conjecture 3.8**, **Remark 3.10**, **Remark 3.13**; BST19 **Theorems 1.1, 1.3, 3.1, 3.2** and the `Q_H` definition; PZ21 **Theorem 9, Theorem 20, Remark 5, Proposition 7**. Quoted in `374d097`. Not read: Freund-Schapire, Lipton-Young, and anything on CEGIS convergence or oracle-efficient learning.

**(b) A FAITHFULNESS PROBLEM IN THE REVIEWER'S GAME FORMULATION, available before reading, and Flag A23 fires on it.** The reviewer sets up: "want a **weighted** `H` of size `Õ(n)` with `|⟨w_H, f_α⟩ − value_G(α)| ≤ ε` for ALL `α`". **Definition 3.9 does not say that.** It demands a **sub-hypergraph** `G_ε = (V, E_ε ⊆ E)` with the guarantee written as `|(|E|/|E_ε|)·Val_{G_ε,P}(a) − Val_{G,P}(a)| ≤ ε(d_G|Z_a| + vol_G(Z_a))` -- an **unweighted subset with a single uniform scaling factor** `|E|/|E_ε|`. BST19 Theorem 1.3 likewise: "we can find a **subset** `F ⊆ E`", with `c = |E|/|F|`. And BST19's entire selling point is additive sparsification which, in their words, "does not require weights on the edges".

> **So the LP/game view is a RELAXATION of the actual object.** The game gives a fractional `w`; Definition 3.9 wants a uniform-weight subset. **The missing step is ROUNDING -- and rounding is exactly where randomisation lives.** If that is right, the CEGIS question may reduce to derandomising a rounding step rather than to evaluating a potential, which is a **fourth shape**, outside the reviewer's three routes.

**(c) My one mechanism, disclosed and NOT priced.** An NP oracle is a **separation oracle** for the constraint system: "`∃α` with violation `≥ v`" is NP, and FP^NP can binary-search `v` and prefix-search `α`. With a separation oracle, ellipsoid (or cutting-plane) finds a **feasible** fractional `w` in polynomially many rounds. **So feasibility is not the difficulty; SPARSITY is.** Combined with (b): the hard part is getting from a dense feasible fractional solution to a uniform-weight `Õ(n)`-subset.

**I am explicitly not pricing (c).** It is a named but unaudited mechanism, which is the W20 failure mode and the W21 lesson. It is registered so it can be scored, and Flag E23 requires auditing it before it moves anything.

**(d) Where I expect to disagree with the reviewer, stated so it can be scored.** Its route (2) has the edge player best-responding against `p_t` over all `2^n` assignments. **But CEGIS proper does not maintain weights over `2^n`** -- it maintains a **finite set** `A_t` of found counterexamples and works against that, which is poly-computable. The `#P` wall appears in *Frank-Wolfe / MWU / approximate-Carathéodory*, which aggregate over the whole assignment space. **Whether the finite-counterexample-set version escapes that, and at what round count, is the question I think the round actually turns on** -- and it is not one of the three routes as stated.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **23a** a CEGIS update rule and a potential computable with an NP oracle converging in poly rounds to an `Õ(n)`-edge sparsifier (= RSW22 Conjecture 3.8) | 8 | **8** |
| **23b** obstruction named as predicted, with the exact step -- which quantity must be counted, or which test must be fooled | 62 | **58** |
| **23c** other | 30 | **34** |

**Why 23a matches the reviewer exactly at 8.** It is a construction question and my standing asymmetry would tempt me upward. **Line 3 of §1 forbids it**: the asymmetry is about constructions *I* produce, not about whether one exists. This is RSW22's central open question in an active area. **Matching rather than differing is the calibrated move, and I am recording it as a deliberate correction of the W22 error.**

**Why 23b is 58, four below.** I think the obstruction-naming outcome is most likely, but §2(b) and §2(d) both point at a step the reviewer's three routes do not contain -- rounding, and the finite-counterexample-set distinction. If the obstruction is real but at a *different* step than "counting or fooling", that is 23c, not 23b.

**Why 23c is 34, four above -- and this time with a partially audited reason, not a base rate.** §2(b) is not a hunch: I have **already checked Definition 3.9's text** and it demands an unweighted subset with uniform scaling, while the reviewer's formulation assumes weights. That mismatch is verified, not guessed. What remains unaudited is whether it *matters* -- whether the rounding step is where the difficulty concentrates. **So: verified premise, unaudited consequence.** That earns four points, not more.

## §4. Flags

- **Flag A23 -- the framing audit runs FIRST, and it has already fired.** Before any route is priced: is the game formulation faithful to Definition 3.9? §2(b) says not obviously -- weighted vs unweighted-with-uniform-scaling. **Discharge this in writing before anything else**, including the question of whether the relaxation is harmless.
- **Flag B23 -- name the scarce resource at each route**: counting, verification, or search. The reviewer's kill test and my standing line.
- **Flag C23 -- modality discipline.** No impossibility phrased stronger than "the known routes need X". W22's Flag D22 modality is the template: *not found in N sweeps, nearest methods structurally bound, not proved absent*.
- **Flag D23 -- stop-rule.** If 23a closes, **stop, send the update rule and the potential**, write nothing further.
- **Flag E23 -- audit §2(c) and §2(d) before they move anything.** Both are named mechanisms; both are unaudited; W20 and W21 are the record of what happens otherwise.
- **Flag F23 -- do not price on a source-indexed asymmetry** (§1 line 3). The specific failure to avoid repeating.
- **Flag G23 -- version-split discipline** on any bibliographic disagreement.
- **Flag H23 -- (S2) stays off the door.** Any finding phrased in terms of (C_1) is off-target.

## §5. Kill tests

- **(i)** Flag A23 discharged in writing, with the answer stated even if it is "the relaxation is harmless and here is why".
- **(ii)** Definition 3.9 re-read for the exact object: sub-hypergraph or weighted? uniform scaling? additive slack on which quantity? **Re-derived, not recalled** -- the contamination of §2(a) makes recall untrustworthy.
- **(iii)** Freund-Schapire or Lipton-Young quoted verbatim for the sparse-equilibrium bound, with its exact hypotheses -- the reviewer's route (2) rests on it.
- **(iv)** Each route's scarce resource named explicitly (Flag B23).
- **(v)** §2(c) and §2(d) tested, and the result stated **in the same sentence as the finding**, whichever way it goes.
- **(vi)** ECCC/arXiv 2023-2026 swept for "deterministic approximation with an NP oracle" / CSP sparsification before writing "open".
- **(vii)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(viii)** Nothing from the door rounds cited as evidence; different object.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 23b, with the wall at the ROUNDING step and its scarce resource named -- counting over `m^{Θ(n)}` distinct ranges, or Σ₂ search.** The reviewer's relocated prediction is vindicated. My 23c at 34 loses. Flag D23 did not fire.

## §6. Framing audit (kill tests i, ii) -- discharged, and re-deriving caught an error of mine

**Definition 3.9, re-read from source rather than recalled**, verbatim: "`value_{G,P}(α) := (1/|E|) Σ_{(v_1,…,v_k)∈E} P(v_1,…,v_k)`" and "a sub-hypergraph `G' = (V, E' ⊆ E)` is a `P`-sparsifier of `G` with error `ε`, if for every assignment `α : V → {0,1}`, `|value_{G',P}(α) − value_{G,P}(α)| ≤ ε`."

**My §2(b) quoted the wrong form.** I wrote that Def 3.9 carries "a single uniform scaling factor `|E|/|E_ε|`". **It does not.** RSW22 normalise *inside* `value` -- the `1/|E|` is already there -- so no explicit factor appears. The `|E|/|E_ε|` form is **PZ21's Definition 8**, which I had read in W22 and conflated. **This is precisely why kill test (ii) demanded re-derivation**: the contamination of §2(a) produced a wrong recall inside a disclosure about contamination.

**The substance of the audit survives.** Def 3.9 still demands an **unweighted sub-hypergraph** `E' ⊆ E`, evaluated by uniform averaging; the reviewer's weighted `⟨w_H, f_α⟩` is still a relaxation. **Flag A23 fired correctly; its detail was wrong.**

## §7. §2(c) LANDED: the NP oracle is a separation oracle, so sparsity is the whole target

The reviewer adopted it as the round's first fact. Stated once, precisely: "`∃α` with `|value_{G',P}(α) − value_{G,P}(α)| ≥ v`" is NP; FP^NP binary-searches `v` and prefix-searches `α`; so ellipsoid or cutting-plane finds a **feasible fractional** `w` over the `m` edges in polynomially many rounds. **Feasibility is free. The whole difficulty is getting from a dense fractional solution to an unweighted `Õ(n)`-edge subset.** The reviewer's route (1) ("MW converges but the average is supported on all `m` edges") is the same fact stated for one method; this says it holds for *every* LP-based route.

**Scored as a positive mechanism that held.** Consistent with the standing asymmetry -- and note this is a construction *I produced*, which is exactly the domain the asymmetry covers (W22's line: indexed to source).

## §8. §2(b)'s inference was WRONG: rounding is not a fourth shape

I claimed the weighted/unweighted gap made rounding "a FOURTH SHAPE, outside the reviewer's three routes". **The reviewer's reply is correct and I concede it.** Randomised rounding *is* the ε-approximation existence proof: sample `Õ(n)` edges from `w`, Chernoff, union bound over all `α`. So rounding is **the point where the uniform-over-`2^n` guarantee re-enters**, and derandomising it is the ε-approximation problem again. **The observation (weighted vs unweighted) was right; the inference (a new shape) was not.** It relocates the reviewer's wall rather than creating a different one.

## §9. The wall, named

### (9.1) This is an ε-approximation problem, and its VC dimension is Θ(n)

The ranges are `R_α := {e ∈ E : P(α|_e) = 1}`. **My own argument, with its hypothesis explicit**:

- **Upper:** there are at most `2^n` distinct `α`, hence at most `2^n` distinct ranges, so `d ≤ n`.
- **Lower:** take `⌊n/k⌋` **vertex-disjoint** edges. **Provided `P` is non-constant**, `α` can be set independently on each edge to make `P` true or false, so every subset is cut out -- they are shattered, and `d ≥ ⌊n/k⌋`.

So **`d = Θ(n)` for constant `k` and non-constant `P`** (constant `P` is trivial). *No published VC statement for CSP range spaces surfaced in the sweep; this rests on the argument above, which I audited myself per Flag E23.*

**And the target size is exactly the VC bound**: an ε-approximation of size `O(d/ε² · log(d/ε))` with `d = Θ(n)` is `Õ(n)` -- which is why RSW22's requirement is what it is.

### (9.2) Lipton-Young supply the size and place the search at Σ₂

> **Lipton-Young, Theorem 2** (verbatim). "For any `ǫ > 0` and `k ≥ ln(c)/2ǫ²`, `min_{p∈P_k} max_j Σ_i p(i)M_ij ≤ V(M) + ǫ(M_max − M_min)`, where `P_k` denotes the `k`-uniform strategies for Min."

With `c = 2^n` opponent strategies, `k = O(n/ε²)` -- the target size again. **Their proof is the union bound**, verbatim: "Fix `ǫ > 0` and `k > ln(c)/2ǫ²`, and form `S` by drawing `k` times independently at random from Min's optimal [strategy] ... is bounded by `e^{−2kǫ²}` ... By the choice of `k`, `e^{−2kǫ²} < 1/c`."

**And their own complexity placement for finding these strategies**, stated as application (3): "Given an oracle `M` for any exponentially large game, the approximate value of the game and near-optimal strategies for it can be computed in **`Σ₂^{P(M)}`**." The one algorithmic follow-up they cite, `[20]`, finds `k`-uniform strategies only "**given the payoff matrix**" -- explicit access, which here is `2^n`-sized.

### (9.3) The known deterministic ε-approximation route needs counting over ranges

Chazelle and Matoušek construct ε-approximations deterministically by iterated halving through **discrepancy colorings** -- the terrains paper (arXiv 0801.2793) generalises "the iterative point set thinning algorithm by Chazelle and Matoušek", in a framework where the cost is governed by constructing a coloring `χ` achieving `disc_χ(X, A)`. Constructing such a coloring deterministically by conditional expectations requires a **pessimistic estimator summed over the distinct ranges**. By **Sauer-Shelah**, a range space of VC dimension `d` on `m` points has at most `m^{O(d)}` distinct ranges; with `d = Θ(n)` that is **`m^{Θ(n)}`**.

*(Modality: secondary summaries report the deterministic running time as `d^{O(d)}·(r^{−2}log(d/r))^d·|X|`, exponential in `|V|` once `d = Ω(log |V|)`. **I could not verify that bound from a primary text** -- one extraction failed, the other source does not state it. The finding does not rest on the exponent; it rests on `d = Θ(n)`, the estimator-over-ranges mechanism, and Sauer-Shelah. Marked accordingly.)*

### (9.4) The scarce resource at each route (Flag B23)

| route | what it needs | scarce resource |
|---|---|---|
| **LP / ellipsoid** (my §2(c)) | a separation oracle | **none -- verification, free with an NP oracle**; but yields a *dense* fractional solution |
| **Randomised rounding** | concentration + union bound over `2^n` | randomness |
| **Deterministic rounding** (Chazelle-Matoušek) | pessimistic estimator over distinct ranges | **counting** over `m^{Θ(n)}` ranges -- (D1)-shaped |
| **Sparse equilibrium** (Lipton-Young) | near-optimal `k`-uniform strategy | **Σ₂ search** (their own `Σ₂^{P(M)}`) |
| **Limited independence** | a good seed among `m^{Θ(n)}` | **Σ₂** ("∃ seed ∀ α"), or a hitting set against NP tests -- the SVN boundary |

**So verification is the one resource the NP oracle supplies, and it is the one resource no rounding route is short of.**

## §10. §2(d) FAILS its audit

I claimed CEGIS proper, maintaining a **finite** counterexample set `A_t`, might escape the `#P` wall because it never aggregates over all `2^n` assignments. **Audited, it does not.** VC dimension bounds the **size** of an ε-approximation, not the **number of CEGIS rounds** needed to pin one down. A subset good for `A_t` carries no guarantee for unseen `α`, and the natural bound on rounds is the number of **distinct ranges** that can be violated -- **`m^{Θ(n)}` again, by Sauer-Shelah**. The finite set avoids aggregating weights over `2^n`, but not needing to *see* `m^{Θ(n)}` of them. **A named mechanism of mine, failing its audit, recorded as such.**

## §11. Scoring

| code | mine | reviewer | outcome |
|---|---|---|---|
| **23a** | 8 | 8 | **Did not fire.** Matching the reviewer was the deliberate W22 correction, and it was right. |
| **23b** | 58 | 62 | **The outcome.** Wall at rounding; scarce resource counting over `m^{Θ(n)}` ranges or Σ₂ search. |
| **23c** | 34 | 30 | **No -- and my stated reason was wrong.** §2(b)'s "fourth shape" was a relocation, not a new shape (§8). **The reviewer's 30 was better.** |

## §12. Calibration

**Three mechanisms registered, one landed, two failed:**

- **§2(c), separation oracle: LANDED.** A construction I produced. Adopted by the reviewer.
- **§2(b), "rounding is a fourth shape": the observation held, the inference failed** (§8).
- **§2(d), finite counterexample set escapes: FAILED its audit** (§10).

**The 23c overpricing is the third time I have been above the reviewer in the "other" bucket and lost** (W17, W20, W23; W18 was the exception where going *below* paid). But the cause differs from W20 and W21, and it is worth separating. This time the reason was **partially audited**: I had genuinely verified the weighted/unweighted mismatch. **What I had not audited was whether a verified mismatch implies a new obstruction.** It did not -- it moved an existing one.

> **New line: a verified premise does not license its consequence.** "The formulation is a relaxation" was checked and true. "Therefore the difficulty is somewhere new" was not checked and false. W23's §3 even said so -- *"verified premise, unaudited consequence -- that earns four points, not more"* -- and four points were still too many.

**And the framing audit produced its own error.** §2(b) mis-attributed the `|E|/|E_ε|` form to RSW22 when it is PZ21's (§6). That was caught only because kill test (ii) required re-derivation. **Contamination does not only bias what you conclude; it corrupts what you quote.**

**Impossibility-claim record unchanged at ten.** No impossibility claim this round.

## §13. What rests

**With W23, every named route from (S2)'s algorithmic end has been traced to a wall.** W21 found the cell-probe route barriered (natural proofs); W22 found the derandomise-BST19 route blocked representationally (no quadratic form for `k ≥ 3`); W23 finds the CEGIS/rounding route needing counting over `m^{Θ(n)}` ranges or Σ₂ search. **RSW22's Conjecture 3.8 remains open**, at the stated modality: *the known routes need counting or Σ₂ search, not proved impossible.*

**(S2) stays off the door.** Even a positive answer here would have given `n^{1+γ}`, never the additive regime where rigidity lives.
