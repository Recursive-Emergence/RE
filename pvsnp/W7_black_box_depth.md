# W7: Korten's Problem 1 in the black-box model, at the smallest instance. Pre-registration

*Drafted 2026-09-12 on branch `w7-black-box-depth`, on the reviewer's W7 specification, after its W6 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE any attack work and before reading the survey's reference [36]. Nothing above the rule at the end is revised retroactively.**

## Ceiling (first, and it needs restating because this is an attack round)

**A black-box depth lower bound separates nothing.** It would say that one *technique* — building a higher-stretch Avoid instance from a lower-stretch one by oracle calls with glue — cannot be sped up, in a model where the instance is treated as a black box. Korten's own framing (§8.1) is that an unconditional negative answer is unavailable without P ≠ NP, which is precisely why the black-box restriction is where the question is posed. **W7 cannot prove P ≠ NP, cannot prove Avoid ∉ FP^NP, and cannot establish "hiding is depth" as a theorem about computation.** The most it can do is settle a combinatorial question about one reduction template at its smallest parameters.

## §0. Refuted premises checked (the standing practice)

Not reused: "(PL) is loose-access lowness" (Y6); "the Pessiland oracle does not bar the route" (Y7, reversed in Y8); "the generator's outputs are deep" (Y9); "prefix descent must resolve a deficit of 1" (W5); "(D1) is smaller than the door" (W4 prose, corrected in W5); **"the n term is the stubborn summand" (W6, mine — refuted: the n term is the search-to-decision cost and is removable under searchSAT ∈ FP^NP_tt; the depth term is what survives)**.

**Practice lines now standing, both earned the hard way:** never reconstruct a dropped superscript inside a quotation; and **do the counting before the prior — including the counting of *removability*, not only of origin.** W6's miss was that I counted where the two terms came from and not whether either could be deleted. W7's counting must therefore ask, for every obstruction I find, *what would remove it*, not only *why it is there*.

## §1. The target, stated from what W6 already verified

**Korten §8.1, Problem 1** (verbatim, verified in W6): *"Is there an FP^NP reduction from stretch n ↦ αn to m ↦ βm with depth complexity significantly better than log_α β?"* — with depth complexity defined (his line 711) as *"the depth of the longest chain of oracle calls C′ makes to C"*, and with his note that a negative answer *"cannot be refuted unconditionally without proving P ≠ NP"*, so the target is *"a negative result in a restricted black box model of reducibility"*.

**Lemma 6** (verified in W6): *"Let n₂ ≥ n₁ > n be given. If Δ_d(n₁ | n) ≥ n₂, then Avoid with stretch n ↦ n₁ can be reduced to stretch n ↦ n₂ in poly(n₂) time and depth complexity d with an NP-oracle."* With **Definition 4**: Δ₁(n′|n) = n′ and Δ_{d+1}(n′|n) = ⌊Δ_d(n′|n)/n⌋·(n′−n) + Δ_d(n′|n).

**The smallest instance, and its arithmetic (done now, not later).** Take n₁ = n+1. Then Δ₁(n+1|n) = n+1, and for n > 2, Δ₂(n+1|n) = ⌊(n+1)/n⌋·1 + (n+1) = **n+2**, and inductively Δ_d(n+1|n) = n+d. So Lemma 6 reaches stretch n ↦ n+2 only at **depth 2**. **A depth-1 reduction from stretch n ↦ n+1 to stretch n ↦ n+2 would beat it.** That is the instance.

**What depth 1 already does, and why it only goes down.** Korten's proof records the base case: *"Avoid can always be reduced downward in stretch by ignoring some output bits. In the case d = 1, n₂ ≤ n₁, and so by this observation there is nothing to prove."* Truncation works because if y ∉ range(C truncated to its first n₂ output bits) then **every** extension of y is outside range(C) — the back-mapping is padding. **So the question is exactly whether depth 1 can go UP by one bit.**

## §2. Two facts I am registering now, because they constrain every outcome

**Flag H7 — the model must be deterministic, or the question is empty.** At stretch n ↦ n+1, |range(C)| ≤ 2ⁿ out of 2^{n+1}, so **at least half** of the codomain avoids the range. With an NP^C oracle, *"is y′ ∈ range(C)?"* is a **single** query. So guess-and-test solves black-box Avoid at this stretch with success probability ≥ 1/2, i.e. it is in FZPP^{NP^C} **unconditionally and at depth 0**. (GGLS25 make the same observation for Avoid in general: *"Avoid is in TFZPP^NP, via the trivial algorithm that guesses"*.)

**Consequences I am committing to in advance:**
1. Any black-box depth lower bound — Wilson's included — is about **deterministic** reductions. Wilson's Theorem 12 (qw ≥ N) is stated for a deterministic query algorithm, consistent with this.
2. **Therefore the black-box form of "hiding is depth" is weaker than its name suggests**: it cannot survive randomization at this stretch. If W7 reaches 7a, the lemma must say "deterministic" in its statement, and the report must say plainly that the thesis dies under randomness here. **I register this now so that a 7a result cannot be quietly oversold later.**

**Flag I7 — what the hint is worth, counted before the prior** (the reviewer asked for exactly this counting):
- **How many hints there are:** |range(C′)| ≤ 2ⁿ out of 2^{n+2}, so at least **3·2ⁿ** strings y satisfy y ∉ range(C′). The adversary picks which one to hand over, so the reduction must work for **every** one of them, including the least informative.
- **How many bits a hint carries:** y is n+2 bits. Its *content*, however, is a conjunction of 2ⁿ constraints ("C′(x) ≠ y for all x"), so its information about C is not bounded by its length in any simple way — this is the step where a naive counting argument would be wrong, and I flag it now.
- **What certification costs:** "y′ ∉ range(C)" is 2ⁿ constraints but **one** NP^C query. So certification is free; the difficulty is entirely in **finding** y′, which is what Wilson's theorem says deterministic black-box search cannot do unaided.
- **The immediate structural test this yields (Flag J7):** a construction fails if the adversary can hand over a *trivially* non-range y. Example: C′(x) = C(x)∘0 has every y ending in 1 outside its range, and such a y says nothing about C. **So a working depth-1 construction must make essentially all 3·2ⁿ non-range points informative.** I expect this to be the crux, and I expect it to be what kills naive constructions.

## §3. The model — what I will decide in Q1, predicted now

The reviewer asks whether the NP^C oracle may be used **while building** C′. **My reading, registered before checking: Lemma 6 does not use it** — C′ is a circuit with C-gates plus glue, and the NP oracle appears only in the back-mapping ("given any solution to C′ Avoid we can find one for C in polynomial time with an NP-oracle"). **Prediction (prior 70): allowing it changes the question materially**, because C′ would then depend on global properties of C rather than being a fixed template with C-gates, and the depth notion — "the longest chain of oracle calls C′ makes to C" — would no longer bound what C′ knows about C. I will state both variants and answer for the Lemma 6 one.

## §4. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **7a** | the smallest instance is proved impossible black-box, with a full proof | 35 | **30** |
| **7b** | a black-box reduction beating Lemma 6's depth is found | 20 | **15** |
| **7c** | neither; the exact obstruction is named | 45 | **55** |

**Why I sit below the reviewer on 7a.** The adversary argument has an obvious shape — run Wilson's partial-assignment adversary against the back-mapping's NP^C queries, then at the end extend the partial C so that the output y′ **is** in range(C), defeating it. The step I expect to fail is that this extension must *simultaneously* keep y ∉ range(C′), and those two demands are coupled through the template: setting C(x₀) = y′ changes C′ at every x whose oracle calls touch x₀. **In the truncation construction that coupling is exactly what makes the reduction correct**, so the argument cannot be template-blind — it must use that the template goes *up* in stretch. I do not yet see what forces the contradiction, and I am not going to price it as if I did.

**Why I sit below the reviewer on 7b.** Korten poses Problem 1 and writes that *"the most exciting possibility is that the answer is positive"*. The depth-1 instance is small enough to state in one line; a survey that raises the question and does not exhibit it is weak evidence that the easy constructions fail. Weak, not strong — surveys omit things.

## §5. Kill tests

- **Determinism stated on every line** (Flag H7). A lemma that says "no depth-1 reduction" without "deterministic" is false.
- **Every construction attempt tested against the trivial-hint attack** (Flag J7) before it is called a candidate.
- **Wilson's template checked for what carries over**: his adversary answers DNF queries maintaining |domain(ρ)| ≤ tw. It has **no hint**. The report must say exactly where the hint breaks his argument, not assert that it transfers.
- **Relativization sanity (Q4):** any claim must be consistent with (i) Wilson's oracle — deterministic FP^{NP^C} fails for Avoid with no hint — and (ii) the unconditional fact that **with** a hard truth table the fold works at depth log(T/n). A "lower bound" contradicting (ii) is wrong.
- **Counting before the prior, and removability too** (the W6 lesson): for any obstruction found, state what would remove it.
- **Tiny cases:** if I compute, every number is reported with the bound it is being compared against written beside it, and the script is scratch-only under the job's tmp directory — **no `formal/` changes, and no computation is presented as proof of an asymptotic claim.**
- **If a prior is wrong, it is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*

---

# Findings (written after the attack; priors above are unrevised)

*Sources read as text this run: Korten, Bull. EATCS 145 (2025), §4.1 (Definition 4, Lemma 6), §6.2 (Theorem 12), §8.1 (Problems 1–2), bibliography; **Miles–Viola**, "On the complexity of constructing pseudorandom functions (especially when they don't exist)", J. Cryptology 2013 — the journal version of Korten's [36] (see §1 on identification), §1, §4, §5. Computations run in the job scratch directory; `formal/` untouched.*

## 0. Outcome against priors

| code | prior (mine / reviewer) | outcome |
|---|---|---|
| **7a** proved impossible black-box | 30 / 35 | not achieved |
| **7b** a depth-1 construction found | 15 / 20 | not achieved |
| **7c** neither; obstruction named | **55** / 45 | **this is the outcome** |

**Registered flags:** H7 **confirmed** (§4). J7 **confirmed** (§3). The §3 model prediction (prior 70) **confirmed** (§2).

**The finding I did not anticipate (§1): the PRG analogue is not uniformly open. It is *solved at both extremes* — impossible for projection post-processing, possible for affine post-processing — and open in between. That reshapes the Avoid question from "is depth 1 possible?" to "possible *with which glue?*"**

## 1. Q1 — prior art, and a bibliographic correction I had to make twice

**Identification, stated because I got it wrong mid-run.** Korten's **[36]** is cited as *Miles–Viola, "On the complexity of non-adaptively increasing the stretch of pseudorandom generators", TCC 2011, pp. 522–539*. The file Viola serves at `papers/stre.pdf` (`stre` = stretch) carries the **different** title *"On the complexity of constructing pseudorandom functions (especially when they don't exist)"* and is dated 2013 — I first concluded it was a different paper. Viola's own homepage settles it: that entry reads *"With Eric Miles. J. of Cryptology, pp. 1-24, 2013. **Preliminary version in Theory of Cryptography Conf. (TCC), 2011**."* **The paper was retitled between conference and journal.** So what I read is [36] in journal form. **I did not see the TCC proceedings version itself**, so theorem numbers below are the journal version's.

*(A search engine twice told me `stre.pdf` was the TCC paper under its TCC title. It was right by accident and wrong in its reasoning; the resolution came from Viola's listing, not the summary.)*

**What is known — and it is a dichotomy, not an open void.**

**Possible, with affine post-processing. Theorem 1.3** (verbatim): *"For every constant c = O(1), there is a poly(n)-time oracle algorithm H: {0,1}^n → {0,1}^{n^c} that makes n^c **non-adaptive** oracle queries and satisfies the following: for some ℓ = Θ(√n) and every one-bit-stretch PRG G: {0,1}^ℓ → {0,1}^{ℓ+1}, H^G(·) is a PRG for infinitely many input lengths."* Its form is given explicitly as an **affine** function of the answers: *"H^G(x) := ⟨G(q₁(x)), r₁(x)⟩ ⊕ t₁(x) ∘ … ∘ ⟨G(q_{n^c}(x)), r_{n^c}(x)⟩ ⊕ t_{n^c}(x)"*.

**Impossible, with projection post-processing. Theorem 1.4** (verbatim): *"For all sufficiently large ℓ and for n ≤ 2^√ℓ, there is no fully black-box construction H: {0,1}^n → {0,1}^{n+s} of a generator with stretch s ≥ 5n/log n and error ε ≤ 1/4 from any one-bit-stretch generator G … of the form H^G(x) := G(q₁(x))_{b₁(x)} ∘ … ∘ G(q_{n+s}(x))_{b_{n+s}(x)} where q_i specifies the i-th query and b_i specifies the bit of the i-th answer to output."*

**And in the primitive black-box setting it becomes a separation. Theorem 4.3:** same form, *"and the q_i and b_i are computable by poly(n)-sized circuits, then **NP/poly ≠ P/poly**."*

**Their own summary of the dichotomy** (line 228): *"linear-stretch constructions require either adaptive queries or post-processing the answers in a more sophisticated way than projecting."* **And it reaches AC⁰** (line 230): *"It was pointed out to us by Benny Applebaum that Theorem 1.4 can be strengthened to rule out even AC⁰ post-processing."*

**Second prior-art item, identified:** [BJP11] = *Bronson, Juma, Papakonstantinou, "Limits on the stretch of non-adaptive constructions of pseudo-random generators", TCC 2011* — concurrent, and Miles–Viola call its results *"incomparable to ours"*. **Not read this run;** recorded as located.

**So Korten's "almost completely unsolved" is fair and I am not contradicting it:** what is settled are the two extremes of the post-processing class. The general case — arbitrary polynomial-time glue — is open, and that is the case his Problem 1 asks about for Avoid.

## 2. Q1 — the model, decided

**Lemma 6 does not use the NP oracle while building C′.** Its proof builds *"an instance C′ … computable with depth d calls to C"* and uses the oracle only afterwards: *"given any solution to C′ Avoid we can find one for C in polynomial time with an NP-oracle."* So the model is: **C′ is a fixed template of C-gates plus glue; the NP^C oracle appears only in the back-mapping.** My pre-registered reading (prior 70) is confirmed.

**Would allowing NP^C while building C′ change the question? Yes, and the depth notion stops meaning anything.** Depth is defined as *"the depth of the longest chain of oracle calls C′ makes to C"*; its purpose (his line 715) is that *"if C is given as a circuit of depth d₀, and we construct C′ by a reduction with depth complexity d, then C′ will be computed by an (explicitly given) circuit of depth d₀ · d"*. An NP^C query inside C′ is not a C-gate and destroys that accounting — C′ would no longer be a circuit built from C at all. **So the Lemma 6 model is the right one, and I answer for it.**

## 3. Q2/Q3 — the attack, and what the computation does and does not show

**The instance.** Δ_d(n+1|n) = n+d (§1 above, arithmetic pre-registered), so Lemma 6 reaches stretch n ↦ n+2 only at depth 2; a **depth-1** reduction from n ↦ n+1 to n ↦ n+2 beats it.

**Zero-query back-mappings: dead, but trivially so.** For a hint y, a back-mapping that ignores C exists iff the intersection, over all C with y ∉ range(C′), of the complements of range(C), is non-empty. Exhaustively over all 4096 functions C at n = 2, this intersection is **empty for every one of the 16 hints, for all four templates tested**. But the reason is trivial and I record it rather than dress it up: "y ∉ range(C′)" constrains C only on the inputs the template actually consults for that output value, leaving some input free to take **any** value, so every candidate y′ is killed by some consistent C. **This says nothing about depth.**

**The real measurement: how many queries the back-mapping needs.** Model: the back-mapping sees y, then adaptively asks for C(x) at inputs of its choice, then outputs y′; it must be correct for every C consistent with the hint and the answers.

**Controls first — the harness is validated.** Korten's depth-1 base cases must come out at 0, and they do:

| template | n | queries needed | bound to compare |
|---|---|---|---|
| CONTROL identity C′ = C | 2 | **0** | must be 0 |
| CONTROL truncation C′ = C ≫ 1 | 2 | **0** | must be 0 |
| A: C(x) ∘ parity(x) | 2 | **4** | N = 4 |
| B: C(x) ∘ lowbit(C(x+1)) | 2 | **4** | N = 4 |
| C: C(x) ∘ highbit(C(x+1)) | 2 | **4** | N = 4 |
| D: xor-glue of two calls | 2 | **4** | N = 4 |

*(n = 2 rows are **exhaustive** over all 4096 functions C — exact, not sampled.)*

**n = 3 (N = 8), sampled — and only the sound direction is used.** A sampled consistent set is a *subset* of the true one, so the back-mapping's task on a sample is **easier**; therefore a failure at q on the sample is a genuine failure at q, while success on a sample proves nothing. Reported accordingly:

| sample size | A: parity glue | D: xor glue | sound conclusion |
|---|---|---|---|
| 4 000 | fails at q = 2 | fails at q = 2 | true q ≥ 3 |
| 40 000 | fails at q = 3 | fails at q = 3 | **true q ≥ 4** |
| 200 000 | fails at q = 3 | fails at q = 3 | true q ≥ 4 (saturated) |

**What this does NOT establish, stated plainly.**
1. **N = 4 gives q = 4, and 4 is also the trivial maximum at N = 4** — reading all of C always suffices. So the n = 2 row alone cannot distinguish "needs everything" from "needs four". It was only the n = 3 row that gave the measurement any content, and it gives q ≥ 4 at N = 8 — **consistent with growth, and not proof of it.** I am not claiming a q = Ω(N) pattern from two points, one of which is degenerate.
2. **The query model is weaker than Korten's**, and this is the limitation that matters most. My back-mapping asks *value* queries ("what is C(x)?"). The real model grants **NP^C** queries — existential questions about C, which is what Wilson's DNF formulation captures. **A lower bound in a weaker query model does not transfer upward**, so none of these numbers bound the real question. They characterise the natural templates under value queries and nothing more.

**Why I did not reach 7a.** The adversary argument I sketched at pre-registration needs, at the end, to extend the partial C so that the back-mapping's output y′ **is** in range(C) while keeping y ∉ range(C′). Those two demands are coupled through the template, and in the truncation case the coupling is exactly what makes the reduction *correct*. I could not find the step that forces the contradiction for "up" templates in general, and — per the pre-registered honesty rule — I am not going to present the computation as if it were that step.

## 4. Q4 — relativization sanity, and Flag H7 confirmed

- **Consistent with Wilson.** Korten §6.2 **Theorem 12**: *"If Q … has query complexity q and width complexity w and solves the [N] → [M] Avoid problem, then qw ≥ N. Hence Avoid ∉ FP^NP relative to some oracle."* That is Avoid **with no hint**; nothing here contradicts it, and nothing here extends it, because the hint is precisely what his adversary does not face.
- **Consistent with the unconditional fold.** With a hard truth table the fold works at depth log(T/n) (W6, RW26 Thm 3.1). Nothing above claims otherwise; the claim under test is only about **increasing stretch black-box at depth 1**.
- **Flag H7 confirmed, and it limits every possible outcome here.** At stretch n ↦ n+1 at least half the codomain is outside range(C), and "y′ ∈ range(C)?" is one NP^C query, so **guess-and-test solves this in FZPP^{NP^C} at depth 0.** Any depth lower bound in this model is about **deterministic** reductions, and Wilson's Theorem 12 is stated for a deterministic query algorithm. **The black-box form of "hiding is depth" does not survive randomisation at this stretch.** I registered this before attacking so it could not be quietly dropped, and it stands.

## 5. The named obstruction (the deliverable for 7c)

**Why the PRG impossibility does not transfer to Avoid, precisely.**

Miles–Viola's Theorem 1.4 is driven by an oracle generator that **reveals most of its input**: Theorem 4.1 item 2, *"For every input x ∈ {0,1}^ℓ, G(x)|_T = x₁x₂ ⋯ x_{ℓ−d}."* Against a projection-only construction this hands the adversary a **distinguisher** — their A accepts the set of strings matching H^G(x)|_{I_x}, which a poly-size non-deterministic circuit can guess and check (Theorem 4.3's proof). **The entire argument is a pseudorandomness argument: it defeats a *security reduction*.**

**Avoid has no security reduction and no distinguisher.** Its back-mapping carries a **total correctness** obligation — for *every* y ∉ range(C′), produce y′ ∉ range(C) — and it is handed an NP^C oracle to do it. There is nothing for a "reveals-its-input" oracle to break, because there is no pseudorandomness to break. **That is the obstruction: the one technique that settles the PRG analogue at this extreme is inapplicable, and Wilson's technique — the right one for Avoid — has no hint in it.**

**The smallest statement that would decide it, sharpened by the prior art.** Korten's Problem 1 leaves the glue unrestricted, and the PRG dichotomy says the glue class is exactly what decides the analogous question. So the useful next target is **Problem 1 with the glue class fixed**:

> *Is there a depth-1 black-box reduction from Avoid at stretch n ↦ n+1 to stretch n ↦ n+2 whose glue is **NC⁰** (equivalently, is ruled out for AC⁰ as in Applebaum's strengthening of Theorem 1.4), with back-mapping in poly time with an NP^C oracle?*

This is strictly smaller than Problem 1, it is the exact mirror of the one PRG case that **is** settled, and — unlike Problem 1 — it names the parameter that the prior art says is decisive. **Recorded as the W7 deliverable.**

## 6. Kill tests

- **Determinism stated on every line** (H7): done, §4.
- **Trivial-hint attack applied before calling anything a candidate** (J7): done — it kills the zero-query case outright, §3.
- **Wilson's template checked for what carries over**: done — it has no hint, §4 and §5. Not asserted to transfer.
- **Numbers reported with the bound beside them**: done, both tables in §3, including the admission that 4 = N is degenerate at n = 2.
- **Sampling used only in the sound direction**: stated in §3 and enforced — success on a sample is never reported as a result.
- **Computation never presented as proof of an asymptotic claim**: §3 item 1.
- **`formal/` untouched; scripts live in the job scratch directory only.**
- **A prior wrong is said with the finding**: no prior was refuted this round; the bibliographic error in §1 is mine and is recorded where it happened.

## Ceiling

As pre-registered, and it did not move. **W7 proves nothing.** It identifies the prior art precisely, fixes the model, kills the natural depth-1 templates under value queries, and explains why the technique that settles the PRG mirror cannot be borrowed. **The question Korten asked remains open, and is now asked in a smaller and better-aimed form.**
