# Y4: the lowness lemma at two rounds. Report

*Run 2026-09-11 on branch `y4-lowness`, on the author's go ("Run Y4, push after merge"), against the pre-registration (d3f0e72) and the reviewer's ruling (70392f5).*
- *Priors, both sides: Y4b 60 / Y4a 25 / Y4c 15.*
- *Rulings: Flag I's exact statement is the object; promise-lowness is recorded as the open lemma if not stated; the kill test is load-bearing.*

*Documents only; `formal/` closed.*

*Sources read as text or as rendered page images this run:*
- *SS22 pp. 29:17, 29:20 and 29:21 as images (Lemmas 21–22, the proof of Theorem 25, Cases 1–3), and l.762–800 as text (Propositions 15–16, the definition of J[γ]);*
- *SS22's bibliography [24] (Goldreich–Vadhan 2011) and [25] (Goldwasser–Sipser, STOC'86, "Private coins versus public coins");*
- *Impagliazzo–Wigderson FOCS'98 (**IW98**, proceedings version), Lemma 16;*
- *Goldwasser–Grossman–Holden, arXiv:1706.04641 (**GGH17**), §1.1.*

## 0. Outcome

**Y4b: the two-round lemma fails at a named step.** Flag I is established as a limitation of SS22's round-1 guarantees and shown to bite on an explicit two-round M. The missing statement is recorded as the open lemma, in the form the reviewer asked for.

1. **The directions, corrected against the rendered pages (a correction to my pre-registration).**
   - SS22's Lemma 22, as printed (p. 29:17): "If s_i ≥ |f^{−1}(q_i)| for every i, then Merlin has a strategy such that the protocol rejects with probability at most δ. If s_i ≤ |f^{−1}(q_i)|/(1+ζ) for some i then … the probability that the verification is accepted is at most δ."
   - Case 1 (p. 29:20): an entry with B_{i,j} < B*_{i,j}/(1+ν) makes Step 5 reject.
   - **So underclaims are blocked per entry, and overclaims pass Lemma 22.**
   - Overclaims are controlled only by Step 4's entropy check. Case 2 (p. 29:21): more than ε(|x|)t/16 entries with B_{i,j} > (1+τ)B*_{i,j} make Step 4 reject. Case 3: **up to ε(|x|)t/16 such entries are tolerated.** Their effect is absorbed because the output reads one uniformly selected row î (bad event B1: "the selected row index î is unsafe").
   - My pre-registration had the directions reversed ("Lemma 22 protects against overclaiming only"). **The structure Flag I needs holds with the directions swapped:** one direction is checked per entry, the other only on a fraction of uniform rows.
   - As printed, Lemma 22's direction runs opposite to the usual statement of Goldwasser–Sipser's lower-bound protocol. I record it as the source's own, and do not claim an error; [25] was not read.
2. **The γ-perturbation answer, quoted (the reviewer's condition for adoption).** Proposition 16 (l.769–771): "Let s, t ∈ N and τ ∈ [0, 1) with t ∈ [s/(1+τ), s(1+τ)]. Let γ ∈ [0, 1) be such that γ ∉ [µ(s)−2τ, µ(s)+2τ] ∪ [1−2τ, 1) ∪ [0, 2τ). Then ϕ((1+γ)s)) = ϕ((1+γ)t)." It neutralizes deviations within a (1 ± τ) factor, not overclaims by a factor ≥ 2. **Adopted as verified.**
3. **Flag I, as a limitation lemma (proved, §1)** and **an explicit two-round M on which it bites (proved, §2).**
4. **The open lemma (§3), in the reviewer's form, with one direction corrected.** A bounded-round adaptive barrier would follow from promise-lowness for certified approximate counting **with prover-steerable queries** (queries that may leave the promise).
   - The nearest stated result (GGH17: psdAM = search-P^{promise-(AM∩coAM)}) requires that "for valid inputs x, all queries to the oracle must be in the promise". That is exactly the condition steering violates.
   - We show only "lowness ⟹ barrier". The reviewer's "⟺" is not established, since no converse is shown.
5. **The kill test (§4), load-bearing and passed.**
   - IW98's reconstruction (Lemma 16, verified) has n adaptive stages with error α = 1/n² each, αn = 1/n in total.
   - SS22-type certification loses a constant fraction of advantage (ε → ε/2 → ε/8…) per level and cannot be amplified per round without the missing lemma.
   - So any bounded-round barrier built on it closes at most O(1) rounds and is silent on ABKMR's n rounds. ✓

## 1. Flag I as a limitation lemma (proved)

**Lemma I (ours).** Fix SS22's protocol for the round-1 query map f₁ with t rows. Every guarantee that Theorem 25 (Cases 1–3) gives about Merlin's round-1 counts B₁ on the sampled rows is one of two kinds:
- (a) no entry is underclaimed below B*/(1+ν);
- (b) at most ε(|x|)t/16 entries are overclaimed above (1+τ)B*.

Consequently, for any set W of rows with |W| ≤ ε(|x|)t/16, **SS22's guarantees are consistent with every entry in W being overclaimed** by an arbitrary factor.

*Proof.*
- Case 1 (p. 29:20) is the only per-entry test, and it tests underclaims only.
- Case 2 (p. 29:21) rejects only when more than ε(|x|)t/16 entries are overclaimed.
- Case 3 tolerates up to ε(|x|)t/16 of them, handling them through the bad event B1 on the selected row.
- No other step constrains individual entries: Step 1 constrains h against H(π_f), and Step 4 constrains σ(B) against h. ∎

**What this means for round 2.** The round-2 query map f₂(ρ, i) depends on the round-1 answers on row ρ.
- To certify a round-2 count s₂(q) = |f₂^{−1}(q)| for a light q (π₂(q) < ε/16), a two-round protocol must know the round-1 answers on the rows in f₂^{−1}(q).
- By Lemma I, SS22's round-1 guarantees say nothing about any set of rows of measure below ε/16, and f₂^{−1}(q) is such a set.
- **So a two-round protocol whose round-1 certification is SS22's cannot certify light round-2 counts.** This is Flag I's content, stated as a limitation of the known certification rather than as a strategy against an unspecified protocol.
- The reviewer's formulation ("a Merlin strategy passing Steps 1–5 in both rounds") presupposes a two-round protocol that SS22 does not define. Y3 showed that Lemma 21 and Lemma 22 need a circuit C_{f₂}, which does not exist when round-1 answers come from Merlin. Lemma I is the precise form.

## 2. An explicit two-round M on which steering bites (proved)

Let M, on input x with random ρ:
- **Round 1:** query q₁(ρ), a fixed polynomial-time function of ρ with a flat distribution, so every q₁ has π₁(q₁) = 2^{−a}, and J(q₁) = a is canonical.
- **Round 2:** if the round-1 answer is < a − 1, query a fixed string q* ("route"); otherwise query q₂(ρ), flat.

**Under canonical answers**, no row routes (π₂(q*) = 0 up to the event of non-canonical answers, which SS22's J[γ] excludes for good γ). q* is the lightest possible round-2 query.

**Steering.** An overclaim of B₁ by a factor ≥ 4 on row ρ lowers ϕ, and hence the answer, by ≥ 2, below a − 1, and routes ρ to q*. By Lemma I this is allowed on up to ε(|x|)t/16 of the sampled rows, and on **any** rows outside Arthur's sample. So the round-2 map that a prover-driven protocol actually evaluates, f_{2,B}, has |f_{2,B}^{−1}(q*)| up to ε/16 of Arthur's rows (and unbounded off-sample), while |f₂^{−1}(q*)| = 0. **The inflation is unbounded in ratio for q*.**

*M is a legitimate robust machine (hypothesis H5).* Its final output may be taken to be any fixed robust function of the round-1 answer alone, ignoring the round-2 answer. Then M computes its language with every oracle within β of K, because answers a and a − 2 are both within β (β = ω(log n)). The example concerns only the round-2 **query distribution** that a two-round protocol must certify, and that distribution is steerable.

Kill-test compatibility: this M is 2-round and says nothing about ABKMR. ∎

**The reviewer's exact Flag I statement, adjudicated.**
- It **holds** for this M under any two-round protocol whose round-1 certification is SS22's: s₂(q*) is inflated from 0, beyond any (1+ζ), with round-1 overclaims confined to ≤ ε/16 of the sampled rows, and none required on the others.
- With the direction corrected, the statement's "underclaims" become **overclaims**.

## 3. The open lemma (the reviewer's ruling (1))

**What a bounded-round barrier needs.** An AM ∩ coAM certification of round-r approximate counts that is **canonical on every row a later round may inspect**, including rows of measure far below ε: Flag L's "exact on almost all inputs".

**As a lowness statement.** Let J be the canonical perturbed count J[γ] for a random γ. The needed statement is:

> **(PL) Promise-lowness with steerable queries.** For every constant r, AM with r rounds of adaptive oracle access to J, where the prover may influence which queries are asked, equals AM, and likewise for coAM.

- **Why the known forms do not give it.**
  - Low(AM) = AM ∩ coAM (Arvind's column l.233, verified in Y3) is for oracles that are **languages**. {(q, j) : J[γ](q) = j} is a language only on the good q (Proposition 16's window), so it is a promise problem.
  - GGH17 (§1.1, verified) gives psdAM = search-P^{promise-(AM∩coAM)} **only** under the condition "for valid inputs x, all queries to the oracle must be in the promise". Steering (§2) produces queries whose certified values are outside the canonical window, i.e. outside the promise.
- **Status:** not found stated in anything read. **Recorded as the open lemma under Y4.**
- **The sharpest form the door has (corrected from the ruling):** (PL) ⟹ a bounded-round adaptive barrier at gap ω(log n). The converse is not shown.

## 4. The kill test (the reviewer's ruling (2))

**IW98, Lemma 16 (verified):** "We recursively compute circuits C₁ ∈ C₁^f, …, C_n ∈ C_n^f … the probability that C_n ∉ C_n^f is at most α·n = 1/n, so the error is bounded." There are **n adaptive stages**, each with error α = 1/n². ABKMR's PSPACE ⊆ BPP^{R_KS} goes through this (their Theorem 18 is IW98's), so it uses unboundedly many rounds.

**The error growth of any SS22-based induction.**
- Per round, SS22's Theorem 25 turns advantage ε/2 into ε/16 (the bad events B1, B2 and the rejection probabilities, each ε/16).
- An r-round induction would lose at least a constant factor per round, advantage ε·c^{−r}. With inverse-polynomial ε this closes at most O(log n / log(1/c)) rounds, and constant-advantage bookkeeping gives O(1).
- **It cannot reach IW98's n rounds without per-round amplification**, and per-round amplification would require canonicity of the certified counts, i.e. (PL) itself.
- So any barrier built this way is silent on ABKMR. ✓ The kill test is passed by construction, not by a detail.

## 5. Priors against outcome, and misses

| | Y4b | Y4a | Y4c |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 55 → 60 | 30 → 25 | 15 → 15 |
| mine | 60 | 25 | 15 |
| **outcome** | **✓** (Lemma I and §2's M; the open lemma (PL)) | not reached | not reached: the known promise result requires in-promise queries, which steering breaks |

- **My miss:** the pre-registration's Flag I stated the directions reversed ("Lemma 22 … protects against **over**claiming only"). SS22's printed Lemma 22 and Case 1 block **under**claims per entry, and Case 2 limits overclaims on average. The Y3 practice line ("check the expected failing step against the source's actual protocol") was applied to *which step fails*, but not to *which inequality direction*; the rendered page settled it. The flag's structure survived the swap. **Scored as the reviewer rules.**
- **Reviewer:** no miss this round. The fifteenth premise miss was scored at the pre-registration.
- **The practice line, sharpened:** read inequality directions from the rendered page when the text extraction separates the superscripts, as it did for B* in Cases 1–3.

## Ceiling

Y4 proves nothing about P vs NP or OWF. It sharpens the door by one sentence:
- **Bounded-round adaptive reductions are barred if (PL) holds.**
- **(PL) is open.**
- **The known promise-oracle result excludes exactly the prover-steerable queries that (PL) must handle.**

## Formal record

Untouched (the author's decision).

## 6. The reviewer's accounting check (post-acceptance; Y4 accepted provisionally)

*Run on the author's standing go for Y4. The page waits on this section.*
- *Sources added: the Goldwasser–Sipser set lower-bound protocol, from Yale CS468 lecture notes "The Goldwasser–Sipser Lower-Bound Protocol" (text read, l.8–19).*
- *Goldreich–Vadhan (SS22's [24], the source of Lemma 21) was **unreachable**: connection reset on https and on http, and WebFetch failed. Lemma 21's internal structure is therefore not read.*

### 6.0 Outcome of the check

**Y4b′: the accounting does not close from verified statements.** It closes *conditionally* on (PL′), three named properties, one of which depends on the unread Lemma 21 source. **Not Y4a′.**

### 6.1 A source inconsistency, and a correction to my §0.1

SS22's printed Lemma 22 and Cases 1–2 (read from the rendered pages) block **under**claims per entry and limit overclaims on average. Two verified facts contradict that reading:
- **(i) SS22's own [25] (Goldwasser–Sipser) blocks overclaims.** The Yale notes, l.8–19: Merlin claims |S| ≥ K; "if |S| ≤ K/2 … Arthur rejects"; "M → A: (x, c), where c is a certificate of x ∈ S".
- **(ii) SS22's Claim 1 (p. 29:21) has the wrong sign under the printed reading.** It says σ(B) − σ(B*) ≥ τY − νt, with σ(B) = (1/t)·Σ(r − log B) (Step 4). That holds only if Y counts **under**claims (log B ≤ log B* − τ). Under the printed Case 2 (overclaims) the difference is ≤ −τY/t.

**The consistent reading is GS's:** Lemma 22 blocks overclaims per entry, and Step 4 limits underclaims on average. **That is my pre-registration's original direction.** Report §0.1's "correction" and the miss recorded for it are **withdrawn**, pending the reviewer's ruling. SS22's print appears to swap B and B* in Lemma 22 and Cases 1–2 (this is my reading; the source itself is not re-derived). **Nothing in §§1–5 depends on the direction**: one direction is checked per entry, the other only on average over uniform rows. With the GS direction, **steering uses round-1 underclaims**, which raise J-answers.

### 6.2 The reviewer's (a) is false: rows outside the sample are inside round-2 certification

Round-2 counts s₂(q) = |f₂^{−1}(q)| are certified by Lemmas 21 and 22 applied to f₂.
- In GS (Lemma 22), **Merlin exhibits** preimages x = (ρ′, i) with certificates of f₂(ρ′, i) = q. Checking such a certificate requires ρ′'s round-1 answers, which Merlin supplies.
- Those rows are Merlin-chosen, not among Arthur's t sampled rows. Round-1 overclaims on them are blocked per entry (GS on f₁ is objective). Round-1 **underclaims** on them are unchecked, since Step 4 averages over *Arthur-random* rows only.
- So steering acts exactly where the reviewer's (a) says no rows exist.

### 6.3 The reviewer's (b), corrected: inflation is bounded by the reach factor, not by (1 + ζ)

**Definitions.** For a row ρ′, let Reach(ρ′) be the set of round-1 answer vectors reachable by underclaims (coordinatewise ≥ canonical, each at most r + log k). Let A := max_ρ′ |Reach(ρ′)| ≤ (r + log k)^{k₁}. The mass routable into a round-2 query y is routed(y) ≤ Pr_ρ′[∃ a⃗′ ∈ Reach(ρ′) : g(ρ′, a⃗′) = y].

**Lemma B (ours, proved).** For every δ > 0,

  Pr_{y∼π₂}[routed(y) ≥ (A/δ)·π₂(y)] ≤ δ.

*Proof.* Each row contributes at most |Reach(ρ′)| ≤ A potential targets, so Σ_y routed(y) ≤ A. Then E_{y∼π₂}[routed(y)/π₂(y)] = Σ_y routed(y) ≤ A, and Markov's inequality gives the bound. ∎

So for all but a δ fraction of honest round-2 queries, the certified count lies within a factor (1 + ζ)(1 + A/δ) of the canonical one, and **the answer shift is ≤ log(1 + A/δ) + O(ζ)**.

**Tightness (proved).** Take M's round-2 query to be g(ρ, a⃗) = prefix_b(ρ ⊕ E(a⃗)), with E injective into {0,1}^b. Then routed(y) = |Reach|·2^{−b} = A·π₂(y) for every y. **So a shift of log A = Θ(k₁·log n) is realized**, and it exceeds the reduction's tolerance whenever β < log A.

### 6.4 The reviewer's (c)/(d): the exact property, (PL′)

The 2-round accounting closes, with error O(ε) along the lines of the reviewer's (c), if all three of the following hold:
- **(PL′-i) Margin:** β ≥ β_SS22 + log(1 + 16k₂A/ε), where β_SS22 = log(k/ε) + 2 log K(q) + α(n) + 5 (SS22's Theorem 14) and δ = ε/(16k₂). In words: **the round-1 query count k₁ must be O(β/log n).**
- **(PL′-ii) Monotonicity of the relativized Lemmas 21–22:** steering can only **inflate** proven counts. Merlin cannot under-prove a count on verifier-random points without rejection, so deflation stays average-limited as in round 1. **This depends on Lemma 21's source protocol (Goldreich–Vadhan), unread this run.**
- **(PL′-iii) Robustness against coin-adaptive oracles:** Merlin commits B² after seeing all t public rows. So the effective round-2 oracle O(y) ∈ [J₂(y) − log(1 + A/δ) − 1, J₂(y) + 1] may depend on M's random strings. H5 is robustness for context-insensitive oracles fixed before M's coins. **(PL′-iii) needs M correct against in-window oracles chosen as a function of M's coins**, or a conversion to fixed oracles in the style of SS22's Theorem 18 (its K′ construction). This is the reviewer's (d), stated exactly.

**Relation to (PL).**
- (PL′) replaces "canonical certified counting" with a quantitative robustness margin plus two structural properties.
- (PL′) is **weaker** than (PL) when k₁ = O(β/log n) and (ii) and (iii) hold.
- For k₁ ≫ β/log n, Lemma B's tightness shows that no argument of this shape closes without (PL).

### 6.5 The kill test on the conditional closure

- Iterating over R rounds compounds the reach: A_R ≥ (r + log k)^{Σ k_j} over the earlier rounds.
- It also loses a constant factor of advantage per round.
- So the closure can reach at most O(1) rounds (or O(log n) with inverse-polynomial advantage). It is silent on IW98/ABKMR's n stages. ✓

### 6.6 Priors and scoring for the check

- The reviewer put Y4b′ 55 / Y4a′ 45. **Outcome: Y4b′**, with (PL′) named as three properties. It closes conditionally for k₁ = O(β/log n).
- **The reviewer's (a)** ("off-sample rows don't exist in the protocol") and **(b)** ("inflated by (1+ζ)") were both incorrect premises (§6.2 and §6.3). Scoring is the reviewer's to make.
- **My §0.1 direction "correction"** is withdrawn (§6.1). If the reviewer agrees, the miss recorded for it becomes a miss for trusting a printed inequality over the cited source's protocol. The practice line should read: **check a printed protocol direction against the cited source's protocol, not only against the rendered page.**
