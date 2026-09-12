# W17: can the residue supply its own randomness? (C₁)'s reconstruction gap. Pre-registration

*Drafted 2026-09-12 on branch `w17-residue-supplies-randomness`, on the reviewer's W17 specification, after the barrier sub-line closed with W16.0–W16.2. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading the primaries for this round.**

## Ceiling (first), and a stop-rule I am adopting verbatim

The idea under test would, if it worked, turn RW26's FP^{prMA} reconstruction into **FP^NP**, make the win-win algorithm single-valued FP^NP for Avoid, and hence by Korten's Theorem 10 give **E^NP ⊄ SIZE[2ⁿ/n] unconditionally**. **That is a major unconditional breakthrough that Ren–Williams did not claim**, which is overwhelming evidence that it fails. **W17's job is therefore to locate the failure point exactly, not to test whether one exists.**

**Stop-rule, adopted from the reviewer and binding on me:** *if at any point 17a appears to be closing, I stop, send the exact parameters, and write nothing further until it has been checked.* Extraordinary conclusions get a second pair of eyes before they get prose.

## §1. Refuted premises checked

Not reused: the four W16 errors — the syntax/black-box "obstruction", "the union bound cannot deliver claim (1)", "a twenty-year-old open question's relativized form should not fall out easily", and the 25 prior — **all of them predictions that a construction would fail**.

**Standing calibration, now a line principle:** *my doubts are unreliable; my constructions are not.* **This round is almost entirely doubt-shaped** — its object is to explain why something fails — **so the bias runs directly at it**, and the guard is that every failure claim must be an inequality with both sides computed, never an intuition.

## §2. Disclosure: what I derived before pricing

**(a) The scale ceiling, and it is worse than a lossy reduction.** A truth table of length T_i is a function on log T_i bits, so its circuit complexity is **at most ~T_i/log T_i** — f_i's hardness is capped by T_i. NW/IW requires hardness ≳ S^{Ω(1)} to fool size S. With the stage recursion T_{i+1} = T_i^C, the stage-(i+1) verifier has size poly(T_{i+1}) = **T_i^{O(C)} ≫ T_i**. **So the requirement exceeds the maximum possible hardness of the string in hand.** This is not a constant-factor loss to be tuned away; it is a ceiling.

**(b) The one-stage lag, and why closing it is circular.** What the reconstruction needs is hardness at scale n_{i+1}; the branch supplies hardness at scale n_i. A string hard at **all** scales is exactly the hypothesis (C₁) — so "fix the lag by assuming f is hard everywhere" assumes what the win-win exists to prove. **If 17b is the outcome, this circularity is the substance of it.**

**(c) Two alternative failure points, registered now because "the failure is exactly where predicted" often conceals an earlier one.**
- **The reconstruction is not a bare spot-check.** RW26 run a PCP **plus a low-degree self-corrector**. Derandomising over generator seeds must fool the self-corrector's query distribution as well as V^C, which is a distinct requirement and may bite before the scale ceiling does.
- **The i.o. structure.** RW26's lower bound is **infinitely often**, for E^{prMA}/1 with one advice bit. "The first stage at which f_{i+1} is easy" presupposes a cleaner quantifier than an i.o. case analysis supplies; the stage index may not be well defined uniformly in the input length.

**(d) Not done:** RW26 §1.2's actual recursion (r_{i+1} = r_i + O(log T_i)) and §5's own hardness-randomness question; CHR §1.3's win-win parameters; Li's simplification; IW97/NW94's size–hardness statements verbatim.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **17a** some stage growth or hardness notion closes the scale gap | 3 | **2** |
| **17b** the scale mismatch is exact and unavoidable as structured, with the failing inequality named, and the one-stage lag shown to be fixable only by (C₁) itself — i.e. circular | 70 | **60** |
| **17c** a different failure point | 27 | **38** |

**Why I am above the reviewer on 17c.** §2(c) gives two concrete candidates that bite *before* the scale ceiling — the self-corrector's query distribution, and the i.o. quantifier structure. **A pre-registered failure point that turns out to be the second failure rather than the first is still a wrong diagnosis**, and this line has seen exactly that pattern twice (W13's obstruction was at the proof level, not the template level; W16's was not the syntax conflict I named).

**Why 17a is 2 and not 0.** It would be an unconditional breakthrough, so its probability is essentially the probability that I am wrong about what RW26 would have noticed. Not zero; not more than a rounding error.

## §4. Flags

- **Flag P17 — every failure claim is an inequality with BOTH sides computed**, at named parameters from the primaries, never an intuition. This is the guard against §1's bias.
- **Flag Q17 — the PCP-of-proximity issue is handled as RW26 handle it, not waved at.** A candidate C encoding a string *close to* a valid history is the case the self-corrector exists for; any derandomisation claim must say what happens to it.
- **Flag R17 — the i.o./a.e. structure of the case analysis is checked against RW26's actual proof**, which is i.o. If "first easy stage" is not well defined there, that is a finding and possibly the finding.
- **Flag S17 — the stop-rule.** If 17a closes, stop and send parameters first.

## §5. Kill tests

- **(i)** Primaries verbatim with numbers: RW26 §1.2 and §5, CHR §1.3, Li, IW97/NW94.
- **(ii)** Every scale carried with its bound beside it — T_i, T_{i+1}, the verifier size, the hardness threshold n_i^α, the NW seed length.
- **(iii)** The self-corrector handled explicitly (Flag Q17).
- **(iv)** The i.o. structure checked (Flag R17).
- **(v)** Nothing from the closed barrier sub-line (W16.0–W16.2) is cited as evidence here — different model, does not transfer.
- **(vi)** If the failure point is not the pre-registered one, **say so in the same sentence as the finding** rather than fitting the result to §2(a).

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 17b, by a cleaner and more general route than §2(a) pre-registered, plus two failure points I did not name correctly. Flag S17 did not fire: 17a closed, but it closed *against* the idea.**

## §6. The primaries, verbatim, with their numbers

Quoted or paraphrased with the number attached in every case; nothing reconstructed. (Practice line from W5: a dropped glyph is marked lost, never reconstructed.)

**(6.1) CHR's stage recursion.** The input length recursion is `n_{i+1} = n_i^beta`, given explicitly as `n_i = (n_0)^{10^i}`. The history/tree parameter recurs separately: `T_i = 5^i * T_0` in the FSigma_2P version, `T_i = (T_0)^{6^i}` in the FS_2P version. The two are distinct parameters and I keep them distinct below.

**(6.2) CHR's (Improve) branch and its crux sentence.** The branch yields a string `f_{i+1}` of circuit complexity at least `n_i^alpha`, and CHR's own accounting sentence is

> "the string f_{i+1} above has n_i^alpha > n_i^beta = n_{i+1} bits of hardness"

so `alpha > beta` is required, and the comparison being made is **hardness against the next input length** -- a polynomial-in-`n` comparison.

**(6.3) RW26's reconstruction.** The PCP proof has `|Pi| <= poly(t(n))`, randomness `O(log t(n))`, `polylog(t(n))` queries, and Merlin's circuit is bounded by `k'(n) = O(k(n)^4 log t(n))`. The lower bound obtained is for `E^{prMA}/1` -- **infinitely often, with one advice bit**.

**(6.4) The NW tradeoff (clw20 Lemma 3.5).** To `eps`-fool size-`S` circuits, the hard function must resist **approximation** by `C . Junta_a` at `1/2 + eps/m`, with seed `t = O(l^2 * m^{1/a} / a)`. Umans' Lemma 3.6 needs `Y` hard for size `s^g` to fool size `s`, with `g > 1`.

**(6.5) CHR's case analysis is largest-k, not first-easy.** CHR take `k` = the **largest** integer with `f_k` not in `Range(GGM_{T_k}[C_{n_k}])`, quantified per `l` with `n_t^{(l)} < n_0^{(l+1)}`.

## §7. WITHDRAWN: Lemma W17.1 (the ceiling-causality scissors)

**This section is refuted. The reviewer killed it before the report was sent, and it is kept here unedited with the refutation attached, per the standing practice of not retro-fitting a page.**

**The refutation.** Step (a), `S >= t`, is **false for the verifier RW26 actually use**. Their PCP proof is *succinct*: Merlin sends a circuit `C` that represents `Pi_C`, and `V^C(seed)` computes `O(1)` query positions (`polylog t` gates), evaluates `C` at them (`poly(|C|)` gates), and decides. **Indexing a proof of length `poly(t)` costs `log t` bits of address, not `t` gates.** So

> `S = poly(e, log t)`, where `e` is the easiness threshold (the size bound on `C`) -- **and `S << t`.**

With `S << t`, the Shannon-Lupanov ceiling of step (c) does not bite at `|y| <= t` at all: a string of length `T_i` can perfectly well be hard against size-`S` circuits when `S << T_i`. The scissors do not close. §8's trichotomy falls with it, since every row was computed from `S >= t`.

**What was actually wrong, and it was not the arithmetic.** (7.4) named `|y| <= t` as the premise to attack and invited the reader to push there. The reviewer pushed somewhere else -- at (a), which I had presented as holding "on the sole ground that `V` must index a proof of length `poly(t) >= t`" and had not flagged at all, because it looked like bookkeeping. It was a modelling error about what the verifier is, and the inequality built on it was arithmetically impeccable and substantively empty.

> **Practice line (new, and the real yield of this round): "both sides computed" is necessary and not sufficient.** Flag P17 required every failure claim to be an inequality with both sides computed, and §7 complied fully. The guard does not catch a wrong premise feeding a correct computation. **From here: the premises of a failure inequality get the same adversarial pass as its arithmetic, and the step that looks like bookkeeping gets it first.**

**What survives.** One idea from §7 survives and turns out to be correct in a different place. The thought that *the hard string must be written down inside the computation that uses it* is not a constraint on the verifier's size -- that was the error -- but it **is** a constraint on the **base** string's length, and in §7' it does the decisive work. The principle was right about what constrains and wrong about where it bites.

*Original text of the refuted section follows, unedited.*

This is the finding. It is weaker in hypothesis and stronger in conclusion than §2(a), and it does not use the PCP's polynomial degree at all.

> **Lemma W17.1.** Fix a stage of the iterative win-win whose computational history has length `t`, and let `V` be the verifier circuit that the FP^{prMA} reconstruction must have its randomness fooled against, of size `S`. Suppose the scheme derandomises `V` by an NW/IW generator instantiated with a string `y` that the algorithm holds at that stage. Then the generator's hardness hypothesis fails. Moreover:
>
> **(a)** `S >= t`, on the sole ground that `V` must index a proof of length `poly(t) >= t`.
>
> **(b)** `|y| <= t`, because `t` is the length of the history of the computation in hand and every string the algorithm holds is written in that history.
>
> **(c)** By the Shannon-Lupanov ceiling, a string of length `|y|` is the truth table of a function on `log |y|` bits and so has circuit complexity at most `(1 + o(1)) * |y| / log |y| <= (1 + o(1)) * t / log t`.
>
> **Therefore** the available hardness is at most `(1+o(1)) * t / log t`, while NW requires hardness at least `S >= t`. The inequality needed is `t / log t >= t`, which is **false for every `t >= 2`**.

Both sides are computed at named parameters, as Flag P17 demands. Three things about it are worth stating separately.

**(7.1) It does not need `d > 1`.** §2(a) argued from `S = poly(T_{i+1}) = T_i^{O(C)} >> T_i`, i.e. from the polynomial degree of the verifier. That argument is correct but it is stronger than necessary and it invited the reply "tune the recursion". The lemma above fails already at degree exactly `1` -- at `S = t` on the nose -- and it fails **by the `log t` factor alone**. There is no degree to tune.

**(7.2) It closes 17a generally, not numerically.** Both sides are evaluated at the same `t`. Growing the recursion faster (raising `beta` from 10, or `6^i` to `C^i`) raises `t` and raises `S = poly(t)` together; the ratio

> `required / available  =  S / (t / log t)  >=  log t`

is unbounded and **invariant under every reparametrisation of the recursion**, because the reparametrisation never appears in it. This is why I record 17a as closed rather than merely unsupported: no stage growth of any rate repairs it, and no adjustment of `alpha`, `beta`, or the `T_i` recursion enters the computation.

**(7.3) The escape is exactly (C_1), which is the circularity.** The only `y` with adequate hardness has, by (c) run backwards, `|y| >= S * log S >= t * log t > t`. By (b) such a `y` is not in hand at this stage; it belongs to a later stage -- and later stages are produced **by** the reconstruction that `y` would derandomise. So the "one-stage lag" of §2(b) is not an off-by-one to be closed by tuning. It is a direction: **the hardness needed to derandomise stage `i` is downstream of stage `i`.** The only ways out are to import the hard string from outside (advice, or the hypothesis (C_1) that a string is hard at all scales), or to make the fooling requirement sublinear in the history -- and PCP verification, which must index its own proof, is not sublinear in the history. This is the substance of 17b's "fixable only by (C_1) itself", now with the mechanism named.

**(7.4) The premise to attack.** The lemma rests on (b), `|y| <= t`. I state it as the load-bearing step rather than burying it. It is not a tautology: one could imagine `y` being *implicitly* defined -- specified by a short description and never written down -- e.g. "the lexicographically first hard truth table", which has a short description and enormous hardness. The reason that does not rescue the scheme is that the NW generator must **evaluate** `y` at `2^{Omega(l)}`-many places across its seeds; an implicitly defined `y` that the algorithm cannot evaluate within its own history is not usable, and one it can evaluate within the history has its evaluations, hence a size-`t` circuit computing it, hence hardness at most `t` -- contradicting the requirement `>= S * log S` by the same margin. I have not found a third option, and I flag this as the single place a reader should push.

## §8. The trichotomy over which string is used

For completeness, over every choice of the NW hard function:

| choice of `y` | numerically adequate? | why it fails |
|---|---|---|
| **earlier stage** (`|y| < t`) | no | strictly worse than same-stage; ceiling `|y|/log|y| < t/log t < S` |
| **same stage** (`|y| <= t`) | no | Lemma W17.1; fails at `d = 1` by the `log t` factor |
| **later stage** (`|y| >= t * log t`) | **yes** | but causally circular: produced by the reconstruction it derandomises (7.3) |

The middle row is the counting obstruction; the bottom row is the causal one. §2 filed these as two separate items (the "scale ceiling" and the "one-stage lag"); they are one lemma with two branches, and the write-up above reflects that rather than preserving my original split.

## §7'. The replacement, on the reviewer's own framing: thresholds against the base

The reviewer's correction does not merely delete §7, it hands over the right variable. The question is not a comparison of **lengths** but of **hardness thresholds**, and it resolves cleanly.

### (7'.1) The two thresholds are the same parameter -- forced, not conventional

Let `s_i` be the circuit-size bound in stage `i`'s dichotomy. The win-win branches on `f_i`: either `f_i` is outside `Range(GGM_{T_i}[C_{n_i}])` for **every** circuit `C` of size `s_i` -- the hard branch, which by Korten yields hardness about `s_i` -- or `f_i` is in the range for **some** circuit of size `s_i` -- the easy branch, which compresses. These two are exhaustive **only because the same `s_i` appears in both**. So the reviewer's `h_i` and `e_i` are not merely equal by convention in the standard win-win:

> **Exhaustiveness forces `h_i = e_i = s_i`.** Any attempt to decouple them, setting `e_{i+1} < h_{i+1}` to shrink the verifier, opens a gap of strings that are neither hard nor easy, on which the dichotomy has no branch and the algorithm has nothing to do.

This closes off the obvious escape before it is tried, and it means the reviewer's `S_{i+1} = poly(e_{i+1}, log t_{i+1})` can be written `poly(s_{i+1}, log t_{i+1})`.

### (7'.2) The requirement, and it compounds backwards

Derandomising stage `i+1`'s verifier with a generator instantiated from `f_i` requires, by (6.4), that `f_i` be hard for circuits of size `S_{i+1}^{...}`; writing `c >= 1` for the tradeoff's hardness-to-size exponent (`c = g > 1` in Umans' Lemma 3.6 form),

> **(R)** `s_i >= S_{i+1}^c >= s_{i+1}^c`.

So the size bounds must **decrease geometrically along the stages** -- the reviewer's point, and correct. Put `H_i = log s_i`. Then (R) reads `H_{i-1} >= c * H_i`, hence after `k` stages

> **(R')** `H_0 >= c^k * H_k`.

The requirement compounds **backwards**, onto the base.

### (7'.3) The floor, from CHR's own crux sentence

Validity of the Korten step at stage `i` is exactly (6.2): the string produced must be hard relative to the **next** input length, `s_i > n_{i+1} = n_i^beta`. At the last stage this is `H_k > log n_k = log N`, where `N` is the target input length. Substituting into (R'):

> **(R'')** `H_0 > c^k * log N`.

### (7'.4) The ceiling on the base -- this is where §7's idea was actually right

`f_0` is a truth table on `n_0` bits, so `H_0 = log s_0 <= n_0` by the Shannon-Lupanov ceiling. And `n_0` is not free:

> **An FP^NP algorithm at input length `N` must write `f_0` down. `|f_0| = 2^{n_0}`, so `2^{n_0} <= poly(N)`, i.e. `n_0 = A * log N` with `A = O(1)`.**

This is the premise §7 reached for and mis-aimed. It is false about the verifier (which is succinct and never writes its proof) and **true about the base string** (which must be materialised, since the generator evaluates it at `2^{Omega(n_0)}` places). Hence `H_0 <= A log N` with `A` constant.

### (7'.5) The failing inequality, both sides at named parameters

Combining (R'') and (7'.4):

> **Required:** `A >= c^k`.
> **Stage count:** `n_{i+1} = n_i^beta` with `n_0 = A log N` and `n_k = N` gives `beta^k = log N / log n_0`, so `k = log_beta(log N / log log N)`.
> **Therefore required:** `A >= c^{log_beta(log N / log log N)} = (log N / log log N)^{log_beta c}`.
> **Available:** `A = O(1)`, by (7'.4).
> **Verdict: fails for every `c > 1`, by an unbounded factor `(log N / log log N)^{log_beta c} -> infinity`.**

**The one surviving point, and why it is not a survivor.** At `c = 1` **exactly**, the requirement collapses to `A >= 1`, satisfiable with `n_0 = beta log N` and `|f_0| = N^beta`. But `c = 1` means a generator whose hard function need only be as hard as the size it fools, and **no hardness-randomness tradeoff provides it**: (6.4)'s Umans form needs `Y` hard for `s^g` with `g > 1`, and NW's own form loses both the additive junta term `m * 2^a` and the correlation factor `1/2 + eps/m`. The scheme is therefore not defeated by a large constant -- it is defeated by the *existence* of any loss at all in the tradeoff, however small. `c = 1 + eps` already sends the requirement to infinity, merely more slowly.

### (7'.6) Why this is 17b and not 17a, and why Flag S17 did not fire

I checked the branch that would have triggered the stop-rule. If the base were allowed at `n_0 = polylog N` -- brute-forcing a near-maximally-hard `f_0` in `Sigma_2 E`, affordable there at `2^{polylog N} << 2^N` -- then `H_0 = polylog N` and (R'') is satisfied with room to spare for any constant `c`. **That branch fits.** It is not 17a: it is unavailable precisely because the target is **FP^NP at input length `N`**, which has `poly(N)` time and cannot write down a string of length `2^{polylog N}`. The gap between what `Sigma_2 E` can brute-force at the base and what `FP^NP` can hold is the entire content of the failure.

So the circularity of §2(b) is confirmed, and **located**: it is not a per-stage lag. It is at the **base case**. The scheme needs a base string hard at exponent `c^k`, and the only way to get one inside `FP^NP` is to already possess a circuit lower bound of that strength at a scale the algorithm can hold -- which is the hypothesis the win-win exists to establish.

### (7'.7) Answers to the reviewer's four pins

- **(a) Stage count.** `k = log_beta(log N / log log N)`, from `n_i = n_0^{beta^i}` (6.1) with `n_0 = Theta(log N)` forced by (7'.4). Not constant: `Theta(log log N)`. CHR's per-block structure `n_t^{(l)} < n_0^{(l+1)}` (6.5) makes `t` constant *within* a block, but the blocks must tile up to `N`, and (R') compounds across all of them.
- **(b) The floor.** I use CHR's crux sentence (6.2) as the floor -- `s_i > n_{i+1}` -- rather than a separately quoted Korten bound, and I flag that as the one place I am reasoning from CHR's accounting rather than from a verbatim Korten inequality. It is the weaker of the two available floors, so the conclusion is not sensitive to it: any larger floor only makes (R'') harder to satisfy.
- **(c) How hard can `h_0` be.** **`H_0 <= n_0 <= O(log N)`** -- the decisive answer, and it is a constraint of the *target class*, not of known lower-bound technology. It is unaffected by future progress on explicit lower bounds, because it is a length bound, not a hardness bound. In `Sigma_2 E` the same quantity is `polylog N` and the scheme goes through; that contrast is the finding.
- **(d) Advice under varying thresholds.** No worse and no better. The threshold schedule is a fixed function of `i` and costs nothing. The branch index -- "largest `k` with `f_k` outside the range" (6.5) -- still costs the one bit of RW26's `E^{prMA}/1`, so §10 stands unchanged. Varying thresholds do not buy the bit back.

## §9. Flag Q17 -- the self-corrector. **Pre-registered obstruction withdrawn.**

§2(c) predicted that derandomising over generator seeds must also fool the low-degree self-corrector's query distribution, and that this is "a distinct requirement [that] may bite before the scale ceiling does". **That is wrong, and I withdraw it in the same sentence as the finding, per kill test (vi).**

The reason it is wrong: for each point `x`, the predicate "the self-corrector on `x` with coins `r` returns the correct value" is a circuit in `r` of size `poly(t)`, and the corrector's guarantee is a constant-margin majority over `r`. A PRG that `1/6`-fools all circuits of size `poly(t)` therefore preserves the vote **at every `x` separately**, since the guarantee is per-circuit and universally quantified over circuits of that size. No union bound over points is incurred and no new size threshold appears. The self-corrector costs nothing beyond what `V^C` already costs.

The PCP-of-proximity case that Flag Q17 asked about -- a candidate `C` encoding a string merely *close* to a valid history -- is likewise unaffected: `C` is fixed before the PRG's guarantee is invoked, and the guarantee ranges over all size-`poly(t)` circuits including the ones `C` induces.

So Flag Q17 resolves as: handled, and **not** an obstruction. This is the sixth-plus instance of the standing calibration -- a doubt of mine, pre-registered, and wrong.

## §10. Flag R17 -- largest-k, i.o., and where the advice bit has already gone

§2(c) also predicted that "the first stage at which `f_{i+1}` is easy" presupposes a cleaner quantifier than an i.o. case analysis supplies, and that "the stage index may not be well defined uniformly in the input length". **Half wrong, and the correct half is not what I said.**

Wrong half: by (6.5) the index is perfectly well defined -- it is the **largest** `k` with `f_k` outside the range, over a bounded stage range, quantified per `l` with `n_t^{(l)} < n_0^{(l+1)}`. There is no ill-definedness. My framing as "first easy stage" was simply not CHR's case analysis.

The real issue, which I did not name: the index is **non-constructive and advice-carrying**. Knowing which `k` is largest is not something the algorithm computes; it is existential over the stage range, and it is exactly why (6.3)'s conclusion is `E^{prMA}/1` -- *infinitely often, one advice bit*. A residue-supplies-randomness scheme would have to **know which stage's string to use as its hard function at the moment it runs**. That identity is precisely the information the advice bit carries, and the advice bit is already spent on branch selection. So the scheme needs a second bit of the resource whose elimination is the entire point of turning FP^{prMA} into FP^NP.

This is an obstruction **independent of Lemma W17.1**: it survives even if one grants the counting and the causality. It is escape (i) of (7.3) in miniature -- importing the hard string from outside -- and the budget for that escape is one bit, already committed.

## §11. The hardness-notion mismatch: it is the exponent `c`

*Rewritten after §7 was withdrawn; the original two-branch framing below depended on the trichotomy and does not survive it.*

The mismatch is real: (6.4) requires resistance to **approximation** by `C . Junta_a` at `1/2 + eps/m`, while the (Improve) branch of (6.2) supplies a **worst-case** circuit-complexity lower bound. In the threshold framing it has a precise home. Converting worst-case hardness to inapproximability (IW97/STV) costs a polynomial loss, and that loss is **exactly a contribution to `c`** in (R). So the mismatch is neither independent of the main argument nor subsumed by it:

> **It is one of the things that makes `c > 1`,** and (7'.5) fails for every `c > 1`. The mismatch therefore does not open a second front -- it supplies part of the very quantity that decides the rate at which the first one fails, and pushing it down toward `c = 1` is the one thing that would rescue the scheme and the one thing hardness amplification cannot do.

This is a cleaner placement than I had, and it retires my pre-write claim that the mismatch "may bite first". It does not bite first or separately; it is a summand in the exponent.

*Superseded text follows, unedited.*

## §11-old. The hardness-notion mismatch: independent in one branch, subsumed in the other

Before writing I flagged a "second, independent mismatch": (6.4) requires resistance to **approximation** by `C . Junta_a` at `1/2 + eps/m`, whereas the (Improve) branch of (6.2) supplies only a **worst-case** circuit-complexity lower bound. On working it through, the honest statement is narrower than "independent":

- **In the same-stage branch it is subsumed, not independent.** (6.2)'s guarantee is a lower bound of magnitude `n_i^alpha`, polynomial in the input length. A string whose complexity *equals* its lower bound is **exactly computed** by a circuit of size `n_i^alpha`, which is smaller than `S = poly(t) = poly(2^{n_i})` by an exponential. A string exactly computed by a circuit far below `S` resists no approximation by size-`S` circuits whatsoever -- it is approximable at correlation `1`. So the worst-case/average-case distinction never gets to do any work: the quantity is already exponentially too small, which is Lemma W17.1 again in the CHR parameters. The magnitudes are `poly(n)` against `2^{Omega(n)}`.
- **In the later-stage branch it is genuinely independent.** There the length is adequate, so the counting objection lapses, and the worst-case-to-inapproximability conversion becomes a real and separate requirement on top of the causality objection of (7.3).

I record this as a correction to my own pre-write expectation. I said this mismatch "may bite first". It does not bite first; in the branch where it bites at all, it bites third.

## §12. Principle extracted

*Restated after the withdrawal. The first version located the obstruction at the verifier and was false there; this one locates it at the base and is what §7' proves.*

> **W17 principle.** An iterative win-win cannot supply its own seed hardness, because **the hardness-randomness tradeoff's loss compounds backwards onto the base case while the base case's size is capped by the target class**. Every stage's generator demands `s_i >= s_{i+1}^c` with `c > 1`, so over `k` stages the base must be hard at exponent `c^k`; but the base is a truth table the algorithm must materialise, so `log s_0 <= n_0 <= log(time budget)`. The bootstrap therefore succeeds in a class with room to brute-force a base (`Sigma_2 E`, base at `polylog N`) and fails in the class the argument is trying to reach (`FP^NP`, base at `O(log N)`).

Two things to note about this form. First, it is **not** a counting argument in the sense §12 originally claimed -- it is a statement about where a compounding requirement lands, and the counting enters only as the cap on the base. Second, it is **class-relative, and that is the point**: the same recursion that works in `Sigma_2 E` fails in `FP^NP` for no reason internal to the recursion at all. That is why the failure is invisible until the thresholds are propagated backwards, and it explains, after the fact, why RW26 stopped at `E^{prMA}/1`: the missing step is not a gap in their argument but the base-case cap above.

## §13. Scoring against the pre-registered priors

| code | mine | reviewer | outcome |
|---|---|---|---|
| **17a** | 2 | 3 | **Closed against**, and I checked the branch that would have opened it. With a base brute-forced at `n_0 = polylog N` the recursion **does** fit above the floor for the required stage count (7'.6) -- it is ruled out not by the recursion but by `FP^NP`'s inability to write the base down. That is the nearest 17a came, and it is not close. |
| **17b** | 60 | 70 | **This is the outcome**, with the failing inequality `A >= (log N / log log N)^{log_beta c}` against `A = O(1)` (7'.5), and the circularity **located at the base case** rather than distributed as a per-stage lag. |
| **17c** | 38 | 27 | **Half credit at most.** The advice/largest-k obstruction of §10 is a genuine second failure point, so the *category* was right. But **both concrete candidates I pre-registered were wrong** -- the self-corrector is not an obstruction at all (§9), the i.o. structure is not ill-defined (§10) -- and the third candidate I added while working (the hardness-notion mismatch "bites first") was also wrong, being a summand in `c` (§11). |

**On the 17c spread.** I sat at 38 against the reviewer's 27 on the strength of two named candidates, and both were wrong. The reviewer's lower number was the better estimate. That my *category* judgement survived is not vindication -- a pre-registered failure point that turns out to be neither the first nor the one named is still a wrong diagnosis, which is the standard I set myself in §3 and I hold to it here.

**Calibration -- and the standing line takes its first real counterexample.** The line has been *my doubts are unreliable; my constructions are not*. This round: three doubts pre-registered, **all three wrong** (§9, §10, §11). So far, standard. But the construction -- Lemma W17.1 and its trichotomy -- was **also wrong**, and was refuted by the reviewer rather than by me.

The saving distinction is narrow and I do not want to hide behind it: **W17.1 was an impossibility claim, i.e. a doubt wearing a construction's clothes.** Every genuine positive construction this program has produced (W8.1, W10.1-W10.3, W12.1-W12.2, W15.1, W16.0-W16.2) has held; every claim that something *cannot* work has been unreliable, and dressing one in an inequality did not change its species. So the line survives, but **restated and narrowed**:

> *My constructions are reliable; my impossibility claims are not -- including the ones I have expressed as inequalities with both sides computed.*

And the operational consequence is §7's practice line: the guard I set myself (Flag P17) checked the arithmetic of a failure claim but never its premises, which is exactly where it broke. §1 warned this round was "almost entirely doubt-shaped" and that the bias ran directly at it. It did -- and it took out the piece I was most confident in, not the pieces I hedged.

## §14. What this leaves open

Not closed by this round, and not claimed to be:

1. **(7'.3)'s floor.** I use CHR's crux sentence as the validity floor `s_i > n_{i+1}` rather than a verbatim Korten inequality, per (7'.7)(b). The conclusion is not sensitive to it -- any larger floor only strengthens the failure -- but it is the one step reasoned from someone's accounting rather than from a quoted bound, and it is where I would want a second reader.
2. **Whether `c` can be driven to `1`.** (7'.5) fails for every `c > 1` and survives at `c = 1` exactly. No known tradeoff gives `c = 1`, and §11 explains why hardness amplification pushes the wrong way. But "no known tradeoff" is not "no tradeoff", and this is now the single quantity the whole question hangs on.
3. **Whether the advice bit of §10 is really irreducible.** I show the budget is spent, not that a cleverer scheme could not re-derive the stage index. That is a separate question and it is the one I would open next.
4. **Nothing from the closed barrier sub-line (W16.0-W16.2) is used here**, per kill test (v). Different model; it does not transfer, and I have not cited it as evidence.

The line returns to the door with (C_1) intact and one more route to it eliminated -- eliminated, in the end, by a **class-relative** argument rather than a parameter-free one: the recursion is sound, and it is the gap between what `Sigma_2 E` can brute-force at the base and what `FP^NP` can hold that closes the route. My first attempt at this round wanted the obstruction to be a clean counting fact about the verifier, and that version was false. The true obstruction is less elegant and sits one level down, in the base case, where the compounding lands.
