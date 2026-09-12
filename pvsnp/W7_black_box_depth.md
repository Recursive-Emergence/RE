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
