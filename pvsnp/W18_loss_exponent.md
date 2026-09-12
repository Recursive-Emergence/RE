# W18: the loss exponent. How much can hardness-to-randomness lose per stage? Pre-registration

*Drafted 2026-09-12 on branch `w18-loss-exponent`, on the reviewer's W18 specification, after W17 closed at `f8e78a6` (outcome 17b, accepted). Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. A correction to W17 that I am carrying forward, not burying

W17 §7'.5 concluded that the scheme "fails for every `c > 1`" and "survives only at `c = 1` exactly". **The reviewer's sharpening is right and my phrasing understated the target.** With `k = Theta(log log N)` stages, the requirement `A >= c^k` with `A = O(1)` needs `k * log c = O(1)`, i.e.

> **`c <= 1 + O(1 / log log N)`** -- not `c = 1` exactly.

My statement is true for every **constant** `c > 1`, which is what I had in mind, but the live case is a tradeoff whose loss **improves with the size it is applied at**, `s |-> s^{1 - O(1/log log s)}`. That is the "extreme high-end" regime, and it is the whole of W18. I am recording this here rather than editing the accepted W17 findings, per the standing practice of not revising a ruled page retroactively.

**A declined proposal, also recorded.** I had nominated a different W18 (does a succinctly described base evade the `n_0 = O(log N)` cap?) and drafted a pre-registration for it. The reviewer declined it in one line -- a base evaluable by a small circuit has small circuit complexity by definition, so it cannot be the hard string -- which is the same argument I had disclosed in that draft's §2. The draft is discarded uncommitted. **It cost nothing and it is not evidence that my impossibility instinct has recovered: the argument was one line and I still priced it at only 62.**

## §1. Refuted premises checked

Not reused: the four W16 errors, the three W17 flag errors, and **Lemma W17.1 itself**. That is eight consecutive wrong predictions that something would fail.

**This round's shape is different, and I note it because it changes the bias.** W18 is mostly a **literature question** -- what loss do the known tradeoffs actually incur, and what is known about the extreme high-end -- not an impossibility argument of my own. The failure mode to guard here is not pessimism but **reasoning from my own summary of a source instead of its text**, which is the W5 error (the reconstructed superscript). Flag Y18 is that guard.

## §2. Disclosure: what I believe before reading, stated so it can be scored

**(a) On the exponent.** I expect the honest answer to question (i) to be that plain-hardness tradeoffs lose a **fixed polynomial** -- Umans' Lemma 3.6 as I already quoted it needs `Y` hard for size `s^g` to fool size `s` with `g > 1` a constant bounded away from 1 -- and that nothing in the NW/IW/Umans line gives `s^{1-o(1)}`. I do **not** know this; it is what I expect.

**(b) On why.** I expect the obstruction to be the hybrid argument's `m`-fold loss (`1/2 + eps/m` correlation) plus the additive junta term `m * 2^a`, both already quoted in W17 (6.4), which together seem to force a constant-factor gap in the exponent rather than a vanishing one. **This is a mechanism I am guessing at, not one I have checked.**

**(c) On Chen-Tell.** The reviewer's 18b names a specific expected content -- that the extreme high-end requires a hypothesis of a stronger type (nondeterministic circuits, or advice, or an equivalence with a lower bound the door already needs). **I have not read Chen-Tell and I am not going to pretend to remember its theorems.** If it says something else, that is the finding and it goes in the same sentence.

**(d) The angle I think is most likely to surprise, and it is the reviewer's (iv).** We do not need a generic PRG. `V^C` is one specific uniform family, and we need to fool one verifier per candidate `C`. **Instance-wise / targeted hardness-randomness** (which RW26 themselves reference) is exactly the regime where the generic loss can be beaten, and it is the reason I am not putting 18c lower than I am.

**(e) Not done:** no primary read for this round. Not yet consulted: Chen-Tell ITCS 2022; Umans 2003 beyond Lemma 3.6 as quoted in W17; SU05 §3's nondeterministic analogue beyond Thm 3.11/3.12 as used in W5/W6; Dermer-Shaltiel 2026's multiplicative-error variant; ECCC 2024-2026 on hardness vs randomness.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **18a** an extreme-high-end tradeoff is known unconditionally in a form usable against the `V^C` family -- the recursion closes and `E^NP` near-max is unconditional | 2 | **2** |
| **18b** best known losses are a fixed polynomial, and the extreme high-end is known to REQUIRE a stronger hypothesis type, placing (C_1)'s remaining gap on the same plain-vs-nondeterministic boundary as W15/W16 | 60 | **66** |
| **18c** other | 38 | **32** |

**Why I am ABOVE the reviewer on 18b and BELOW it on 18c, deliberately.** In W17 I sat at 38 on 17c against the reviewer's 27, on the strength of two named candidates, and **both were wrong; the reviewer's lower number was the better estimate.** The diagnosis was that I inflate the "something else" bucket. Repeating that here after naming it would be the eighth instance of a bias I have already written down, so I am correcting in the opposite direction and will be scored on it. **This is a deliberate calibration move, not a change of belief about the mathematics** -- my honest read of the content is close to the reviewer's, and §2(d) is the one thing keeping 18c as high as 32.

**Why 18a is 2 and not lower.** Same reasoning as 17a: it would be an unconditional breakthrough, so its probability is essentially the probability that the literature contains something the reviewer and I would both be astonished by.

## §4. Flags

- **Flag X18 -- the premise audit runs FIRST.** W17's practice line, now standing: "both sides computed" is necessary and not sufficient; the premises of any failure inequality get the adversarial pass before the arithmetic, **and the step that looks like bookkeeping gets it first**. In W17 I even flagged the wrong premise as load-bearing.
- **Flag Y18 -- every exponent carries its theorem number**, and no exponent is reported from my memory of a source. This is the W5 guard (never reconstruct inside a quotation) applied to numbers rather than glyphs.
- **Flag Z18 -- "open" is not written until ECCC 2024-2026 has been checked** on hardness vs randomness. W15 found TR25-191 this way and W16 found TR25-104; the habit has paid twice.
- **Flag S18 -- the stop-rule, inherited and binding.** If 18a appears to close, stop, send the exact parameters, and write nothing further until the reviewer has checked it.
- **Flag V18 -- no fitting to W17.** If the loss can be driven into the `1 + O(1/log log N)` window, that reopens 17a and it is said plainly, in the same sentence as the finding.

## §5. Kill tests

- **(i)** Primaries verbatim with numbers: Chen-Tell ITCS 2022; Umans 2003 Lemma 3.6 and its statement of the loss; SU05 §3; Dermer-Shaltiel 2026 if the multiplicative-error variant bears.
- **(ii)** The four questions answered separately and explicitly: (i) the exact best known `c` for plain hardness with its theorem; (ii) whether any construction achieves `s^{1-o(1)}` and under what hypothesis; (iii) whether extreme-high-end from plain hardness is proved impossible black-box or proved equivalent to something; (iv) whether an instance-wise or targeted generator beats the generic loss **for this specific uniform `V^C` family**.
- **(iii)** The `1 + O(1/log log N)` window of §0 used as the target throughout, never `c = 1`.
- **(iv)** ECCC swept before any claim of openness (Flag Z18).
- **(v)** Nothing from the closed barrier sub-line (W16.0-W16.2) cited as evidence.
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 18b, in a stronger form than pre-registered -- the loss exponent never enters. Flag S18 did not fire.**

## §6. The primaries, verbatim, with their numbers

**(6.1) Attribution correction, confirmed from three copies of the title page.** "On Hardness Assumptions Needed for 'Extreme High-End' PRGs and Fast Derandomization" (ITCS 2022; arXiv 2311.11663) is by **Ronen Shaltiel and Emanuele Viola**, not Chen-Tell. The reviewer's 18b was phrased around "Chen-Tell's result, whatever it exactly says"; **Chen-Tell (STOC 2021) and Doron et al. (FOCS 2020) are the construction side** -- they "construct 'extreme high-end PRGs' with seed length `r = (1 + o(1)) * log m`, under qualitatively stronger assumptions". Shaltiel-Viola is the impossibility side. Their target assumption is the **extreme high-end hardness assumption**, the scaling of IW97's `0 < beta < 1 < B` to **`beta = 1 - o(1)` and `B = 1 + o(1)`**, and they "give a partial negative answer".

**(6.2) The loss is a DIVISION BY THE QUERY COUNT, not a power.** This is the round's central correction to my §2(a), and to the shape everyone in this line (me, the reviewer, W17) had been assuming.

> **Proposition 1.8 (Number of queries determines hardness loss in black-box proofs).** "Let `(Con, Red)` be a black-box hard-function => PRG (resp. hard-function => `rho'`-hard-function) proof in which `Red` makes `q` queries, and has advice length `a`. If we start from a function `f : {0,1}^l -> {0,1}` that cannot be computed by circuits of size `s`, and apply the black-box proof, one can at best obtain that `Con^f` is a PRG (resp. `rho'`-hard-function) for circuits of size `m <= (s-a)/q <= s/q`."

Their one-line reason, also verbatim: the circuit `C = Red^D(., alpha)` implied by the reduction "is of size `q * m + a`. This gives that `s >= q*m + a`".

**(6.3) Three facts about EVERY black-box proof**, stated parenthetically in Open Problem 1.9:

> **`r >= l`** ("Any black-box proof must have `r >= l`"); **`m <= 2^l`** ("Any black-box proof must have `m <= 2^l`"); **`a >= m`** ("Any black-box proof must have `a >= m`").

**My W18 premise audit -- that `d >= l` -- is therefore correct and is in the literature in far greater generality than the argument I gave for it.** I derived it from the NW design (every `S_j` has size `l`); Shaltiel-Viola state it for *all* black-box proofs, design or no design.

**(6.4) What the extreme high-end would require, and that it is open.** Open Problem 1.9 asks for a black-box proof with `r = (1+o(1))*l`, `m = 2^{(1-o(1))*l}`, `a = m^{1+o(1)}`, and **`q = m^{o(1)} = 2^{o(l)}`**. Shaltiel-Viola: "We do not know whether black-box hard-function => PRG proofs as in Open Problem 1.9 exist." They stress it is **necessary but not sufficient** for the extreme high-end.

**(6.5) The blocking result for the amplification route.** "in black-box proofs of hardness amplification to `1/2 + 1/m`, reductions must make `Omega(m)` queries, even in the extreme high-end. Known PRG constructions from hard functions are black-box and use (or imply) hardness amplification, and so cannot be used to construct a PRG `G2` from the extreme high-end hardness assumption." Combined with (6.2), `q = Omega(m)` gives **`s >= q*m + a = Omega(m^2)`**.

**(6.6) The nondeterminism escape, in their own words.** On how Doron et al. get their PEG despite Theorem 1.14 (Impossibility of black-box PEGs with `r < log m`): "their proof is black-box, but it allows the reduction `Red` to use nondeterminism". Their Theorem 1.11 is the general query lower bound; Theorem 1.12 concerns random construction maps.

**(6.7) Context, three independent arrivals at the same boundary.** Dermer-Shaltiel **TR26-017** is "Multiplicative Pseudorandom Generators for **Nondeterministic** Circuits", with `r = O(log s + log(1/eps))`. van Melkebeek-Sdroievski, **CCC 2023**, build "targeted hitting-set generators based on probabilistically checkable proofs for **nondeterministic** computations" in the **AM** setting. And (6.6). **Flag Z18 sweep done:** ECCC "hardness vs randomness" 2024-2026 is TR26-089, TR26-017, TR25-107, TR25-054, TR25-042, TR24-182; nothing there closes Open Problem 1.9.

**(6.8) Not obtained.** Umans 2003 itself. The caltech host fails certificate verification and **I did not bypass TLS**; two mirror guesses 404'd. Umans' Lemma 3.6 (`Y` hard for size `s^g` to fool size `s`, `g > 1`) is therefore cited **as quoted-via-clw20 in W17, marked secondary**, and no exponent is reported from memory (Flag Y18).

**(6.9) RW26's base is BRUTE FORCE, and there is no hard base string at all.** This overturns a premise that both the reviewer and I had been arguing from. Verbatim (TR26-118, proof of the main construction):

> "Let `n_0 = 2^q` be some fixed input length, let `T_0 = 2^{c n_0}` for a universal constant `c >= 1`, and let `r_0 = 0, s_0 = 0`. Let `BF_0` denote the Brute Force algorithm for solving AVOID on `G_{n_0}`, which simply enumerates every string in `{0,1}^{n_0}`, computes the whole range of `G_{n_0}`, and outputs the lexicographically first string not in `Range(G_{n_0})`. Then, `BF_0` runs in deterministic `T_0` time and makes no queries to the SAT oracle, so `r_0 = 0` and `s_0 = 0` suffice."

`n_0` is a **fixed constant** input length and the base stage is exhaustive search. There is no `f_0` whose circuit complexity is in question.

**(6.10) The stage recursion, verbatim, and a notational collision that had to be caught.**

> "`n_{i+1} := n_i^C` and `T_i := max{2^{cD^i n_0}, n_{i+1}}`"
>
> "let `f_i : {0,1}^{n_0} -> {0,1}^{T_i}` be the function that ignores its input and outputs the `2^{n_i}`-bit string produced by `BF_i` on `G_{n_i}`, padded with extra zeros so that the total output has length `T_i`"
>
> "`#rounds = r_{i+1} := r_i s_i^D + O(n_{i+1} + log T_i)`" and "`length = s_{i+1} := max{s_i, n_{i+1}}`"

**`s_i` is RW26's NP-query WITNESS LENGTH, not a circuit-size hardness threshold.** The reviewer and I had both been writing `s_i` for a hardness threshold throughout W17 and W18. The recursion `s_{i+1} = max{s_i, n_{i+1}}` is about query witness length; RW26's own list names `{n_i}, {T_i}, {r_i}, {s_i}` as "input lengths, running times, number of parallel rounds, and query lengths, respectively". Nothing in this round's conclusions depended on the collision, but it could have silently wrecked the analysis and is recorded so it is not re-introduced.

**(6.11) The reconstruction's budget, verbatim** -- this is what decides audit (a):

> "an algorithm `Recon_i(j) := Recon^{f_i}(x_0, j)` that runs in deterministic `poly(n_{i+1}, r_i, log T_i)` time with access to a prMA oracle. If `BF_{i+1}` fails to solve AVOID on `G_{n_{i+1}}`, then for every `j in [T_i]`, `Recon_i(j)` outputs the `j`-th bit of `f_i(x_0)` while making only smart prMA queries."

Polynomial in `n_{i+1}` and `log T_i` -- **not** in `T_i`.

**(6.12) Arthur evaluates Merlin's circuit.** Verbatim:

> "the last query is of the following form: Merlin sends Arthur a circuit `C` that succinctly represents a PCP proof `Pi_C`, Arthur verifies that `Pi_C` is accepted by the PCP verifier, has the correct prefix, and a certain bit of `Pi_C` (depending on `i`) is equal to 1; and `L(i) = 1` if and only if this query accepts."

**(6.13) RW26's own statement of the boundary.** Verbatim:

> "we only know that `searchSAT` in `FP^NP_tt` under lower bounds against single-valued nondeterministic (SVN) circuits [AK01; KM02; MV05; SU06]. It is unclear whether such a strong derandomization assumption is necessary, and we feel that it is important to understand the minimum assumption needed to put `searchSAT` into `FP^NP_tt`."
>
> "**Question 5.2.** What is the weakest circuit lower bound assumption that implies `searchSAT` in `FP^NP_tt`?"

**Numbering discrepancy, flagged not reconciled.** W15 and the program memory record this as **Question 5.3**; the copy I read (TR26-118, 10 July 2026) numbers it **5.2**. I do not know which is the version discrepancy and I am not silently harmonising them. The *content* is the same question and it is the W15/W16 boundary in RW26's own words.

*(Extraction caveat: `pdftotext` rendered several internal cross-references as `??`, so RW26 theorem numbers are not quoted here. Only prose I could read directly is quoted.)*

## §7. The finding: the residue can never supply randomness to the branch that needs it

### (7.1) What I drafted and struck, recorded because the calibration matters

Before reading RW26 I had drafted a different §7, whose core was a margin: the verifier's randomness forces `s >= m = Omega(l)` by Shaltiel-Viola Prop 1.8, against a base hardness of `Theta(l / log l)` from diagonalisation. **It is struck.** By (6.9) the construction has no hard base string -- the base is exhaustive search at constant `n_0` -- so the margin argues about an object that does not exist. The reviewer's fact (b) (base hardness `n_0/log n_0`) is struck for the same reason, and it was the reviewer that found this.

I had also **refuted** the reviewer's fact (a), claiming a succinct PCP lets the verifier spot-check one gate and never evaluate `C`. By (6.12) that is **wrong in the regime that matters**; see (7.3).

So in this round I struck one argument of my own and one of the reviewer's, and my one confident refutation was itself refuted. **Tenth consecutive wrong impossibility claim.**

### (7.2) The theorem

> **Theorem W18.1 (the branch that needs the randomness is the branch without it).** In the iterative win-win, a string hard enough to derandomise the reconstruction of stage `i` is already hard enough to run Korten at stage `i+1` directly. Hence the reconstruction can never be derandomised by the residue.
>
> **Proof shape.** By (6.11), `Recon_i` is invoked **exactly** in the branch where `BF_{i+1}` *fails* to solve AVOID on `G_{n_{i+1}}` -- that is, exactly where `f_{i+1}` is easy. Its last query is (6.12): Merlin sends a circuit `C` representing `Pi_C` and Arthur evaluates `C` at the queried positions, so the predicate to be fooled has size at least `|C|`. A generator derandomising it must therefore be built from a string hard at a threshold at least `|C|`, which is at least the easiness threshold at stage `i+1`, which is `poly(n_{i+1})` by (6.10). But a string hard at that threshold is precisely what Korten's reduction consumes to solve AVOID at length `n_{i+1}` outright -- in which case `BF_{i+1}` would have succeeded and `Recon_i` would not have been invoked at all. The hypothesis of the branch contradicts the resource the branch would need.

**Corollaries, one per version of the scheme.**

- **Chained** (use `f_i` to derandomise stage `i`). The only hard string in hand is `f_i`; requiring it to be hard at the stage-`i+1` threshold makes the thresholds non-increasing, which collapses the chain into a single string and returns us to the next case.
- **Single-string** (one string throughout). If it is hard at a high threshold, "hard" gives `FP^NP` at the top scale outright, and there is nothing to reconstruct. If it is not, the reconstruction at scale `n_0` has no hard string in hand and stays MA -- which is exactly `E^{prMA}/1`, i.e. RW26's existing result. **The status quo is the fixed point.**

### (7.3) The scale condition on fact (a), and a symmetry worth naming

My refutation of (a) is correct **only where the PCP proof is explicit**. It is not, in the regime that matters: `Recon_i` runs in `poly(n_{i+1}, r_i, log T_i)` time (6.11) while any PCP proof about a history of length `T_{i+1} = 2^{Theta(n_{i+1})}` has length `poly(T_{i+1})`, exponentially larger than the budget. So the proof **must** be presented succinctly, by a circuit, and Arthur must evaluate it (6.12). Augmenting the proof with `C`'s gate-by-gate values does not help: the augmented proof is still exponentially long and is still handed over as a circuit of size `>= Omega(|C|)`.

> **Succinctness cuts both ways, and this is the round's most transferable lesson.** In W17 it *shrank* the verifier and killed my Lemma W17.1 (`S >= t` false, because the proof is never materialised). In W18 it *forces* the verifier to evaluate a circuit and kills my refutation of (a). **The same property of the same construction, deployed against me twice in opposite directions, because both times I reasoned about the proof's representation without asking what the budget at that scale permits.** The discipline that follows: name the scale and the time budget before asserting anything about what a verifier does or does not contain.

### (7.4) Why the loss exponent never enters

No exponent appears in Theorem W18.1: no `c`, no stage count, no seed length, no base hardness. The obstruction is the **branch structure of the win-win itself**. The dichotomy produces hardness *for free* in the "not easy" branch, but the reconstruction is required in the *other* branch -- and that branch is, by definition, the one in which the string in hand is easy. **The residue is easy exactly when its randomness is needed.**

## §8. Answers to the four questions

- **(i) Best known `c` for plain hardness.** The question is mis-shaped. By Shaltiel-Viola **Proposition 1.8** the black-box loss is `m <= (s-a)/q <= s/q` -- a **division by the query count**, not a power -- because `Red^D(., alpha)` has size `q*m + a`. Routed through amplification, `q = Omega(m)` gives `s >= Omega(m^2)`, which *presents* as `c = 2`. My §2(a) expectation was right in magnitude, wrong in mechanism.
- **(ii) Does anything achieve `s^{1-o(1)}`?** Black-box, it requires `q = m^{o(1)}` (Open Problem 1.9), which is **open**, and which the `Omega(m)`-query amplification bound blocks for every construction going via amplification -- i.e. all known ones. Doron et al. and Chen-Tell achieve the extreme high-end only under "qualitatively stronger assumptions", and Doron et al.'s reduction **uses nondeterminism**.
- **(iii) Impossibility or equivalence?** Neither: **a partial negative answer** in the black-box model, isolated as a query-count lower bound (their Thm 1.11, Thm 1.14). Open Problem 1.9 stands open; the Flag Z18 ECCC sweep (TR26-089, TR26-017, TR25-107, TR25-054, TR25-042, TR24-182) found nothing closing it.
- **(iv) Instance-wise / targeted generators.** **Left open, deliberately.** Shaltiel-Viola footnote 7 states that Chen-Tell's "targeted-PRG" notion is **unrelated** to their black-box notion, so (iv) cannot be read off their impossibility results; it needs van Melkebeek-Sdroievski (CCC 2023) on its own terms. This was my §2(d) -- the one place I predicted surprise -- and it is the one place the round does not reach. **But note that Theorem W18.1 is indifferent to it:** a targeted generator with a better loss still needs a hard string, and the branch still does not have one.

**The plain-vs-nondeterministic boundary, four independent arrivals.** Doron et al.'s reduction uses nondeterminism; Dermer-Shaltiel TR26-017 is multiplicative PRGs for **nondeterministic** circuits; van Melkebeek-Sdroievski build targeted hitting-set generators from PCPs for **nondeterministic** computations in the **AM** setting; and (6.13) is RW26 themselves saying the derandomisation they lack is known only under **SVN** circuit lower bounds. This is the W15/W16 boundary, reached from four directions in one round.

## §9. Scoring

| code | mine | reviewer | outcome |
|---|---|---|---|
| **18a** | 2 | 2 | **Did not fire.** Flag S18 was armed twice by the reviewer and disarmed twice, correctly. |
| **18b** | 66 | 60 | **The outcome, strengthened past what either of us wrote.** The extreme high-end does require a stronger hypothesis type, and it is specifically **nondeterminism in the reduction**. But the residue scheme's death does not run through the loss exponent at all -- it is the win-win's **branch structure** (Theorem W18.1). |
| **18c** | 32 | 38 | **Partially.** The mechanism was not the pre-registered one (the loss is a query division, not a power), and (iv) is untouched. |

**The calibration move paid, and I am not extending it.** I went to 66/32 against 60/38 specifically to correct W17's habit of inflating the "something else" bucket, and said so in advance. 18b is the outcome. **One success is not a licence to move further in the same direction**, and the reviewer's 38 was arguably the better read given how much of the mechanism turned out to be un-pre-registered.

**Tenth consecutive wrong impossibility claim** (7.1), and this round it was three at once: my `(i)+(ii)` base margin, my `d >= l` kill of the chained version, and my refutation of fact (a). Against that, two correct positive contributions: catching the `s_i` notational collision (6.10), and the scale-condition symmetry in (7.3). **The standing line survives intact and was never better evidenced:** *my constructions are reliable; my impossibility claims are not, including ones expressed as inequalities with both sides computed.*

**What Flag X18 did and did not do.** It caught the reviewer's fact (a) as worth auditing -- correct instinct, wrong verdict. It did not catch my own `l_i = n_i` slip, because I audited the premise I had *flagged* rather than the one I had *assumed*. That is the same failure as W17 §7.4, one level up, and it is now the standing warning: **the premise you did not think to write down is the one that breaks.**

## §10. What this leaves open

1. **Question (iv)** -- instance-wise/targeted generators on their own terms. The natural W19, though Theorem W18.1 suggests it cannot rescue the scheme.
2. **Shaltiel-Viola Open Problem 1.9** -- open in the literature, not merely unresolved here.
3. **RW26's own Question 5.2/5.3** (6.13) -- the weakest lower bound putting `searchSAT` in `FP^NP_tt`. This is where W15 and W16 already are, and W18 has now arrived at it from the hardness-randomness side. **The numbering discrepancy with W15 should be resolved against a second copy of RW26 before either is cited again.**
4. **Umans 2003 primary** -- not obtained; the host fails TLS verification and I did not bypass it. Cited via clw20 as secondary and marked. Shaltiel-Viola Prop 1.8 is in any case the better primary for the loss shape.
