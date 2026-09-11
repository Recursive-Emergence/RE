# Y6: (PL) at two rounds, as a question in interactive proofs. Report

*Run 2026-09-11 on branch `y6-pl`, on the author's go ("Run Y6, push after merge"), against the pre-registration (568ec6b) and the reviewer's ruling (5a1529e).*
- *Priors, both sides: Y6b 60 / Y6c 25 / Y6a 15.*
- *Ruling (1): if Flag D2 blocks, state the terminal so an HMX reader recognizes it.*
- *Ruling (2): name the exact GS86 step, and if the hybrid is not well defined, say so as the finding.*

*Documents only; `formal/` closed. Sources read as text this run:*
- *Gupta–Fortnow-style survey of promise oracle access: "Hierarchical Unambiguity" (arXiv cs/0702047), §2.2 and Definition 2.6, for Grollmann–Selman [GS88] smart access;*
- *EPFL complexity notes, Lecture 8, §3.1, for the Goldwasser–Sipser private→public simulation;*
- *HMX10 l.295–312 (verbatim below);*
- *SS22 §4 hypotheses H1–H6 and §5 Steps 1–7 (verified in Y4/Y5);*
- *GGH17 §1.1 (verified in Y4).*
- *Goldreich's promise-problem survey (ECCC TR05-018) was fetched but its text extraction is unusable (bitmap fonts; a grep for "promise" matches nothing). It is cited only through the secondary description in cs/0702047.*

## 0. Outcome

**Y6b: (PL) at two rounds fails at Flag D2, before the conversion, and the terminal is a stated open problem of HMX restricted to our setting.** Two further findings:
1. **A correction to my own §1 framing, which the reviewer has already ruled onto the page: (PL) is _not_ loose-access lowness.** §1 below gives the reason and the corrected statement. **The page sentence needs amending before it goes in.**
2. **Flag S2's hybrid is not well defined**, and for a sharper reason than expected: the object that must stay secret is not any of the protocol's coins (§3).

## 1. Arm (a): the literature map, and why the promise-oracle framing does not fit (correction)

**Smart access (verified, cs/0702047 Definition 2.6, for Grollmann–Selman [GS88]).**

> "A set L polynomial-time smart Turing reduces to a promise problem Π = (Π_yes, Π_no) … if there is a deterministic polynomial-time oracle Turing machine M such that for all x: (1) x ∈ L ⟺ M^Π(x) accepts, and (2) if M^Π(x) asks a query y to Π, then y ∈ Π_yes ∪ Π_no."

The same source records that "if a query falls outside the promise set, then it is not immediately clear how that query should be handled", that several models exist, and that [Gol05] generalizes smart reductions.

**Where each known model sits.**
- **GGH17** (verified in Y4): psdAM = search-P^{promise-(AM∩coAM)} "where for valid inputs x, all queries to the oracle must be in the promise" — **smart access**. Steering violates exactly clause (2).
- **Low(AM) = AM ∩ coAM** (verified in Y3): oracles that are **languages**.
- **Loose (permissive) access:** the machine must be correct **irrespective of the oracle's behaviour** off the promise.

**The correction.** My pre-registration called (PL) "loose-access lowness", and the reviewer ruled that phrasing onto the page. The run shows it does not fit, for a structural reason:
- Loose access is a **stronger hypothesis on the machine** (correct no matter what is answered off-promise). A stronger hypothesis would make the simulation **easier**, not harder.
- Our object is not a machine with oracle access whose correctness is assumed. It is a **protocol whose soundness is the thing to be established**, and the off-promise "answers" are supplied by the very party trying to cheat.
- So (PL) is not an instance of promise-oracle lowness in either standard model. **Neither smart nor loose access captures it.**

**(PL), corrected statement (ours).**

> **(PL)** There is an AM protocol that certifies, for a samplable map whose evaluation on a row depends on earlier certified counts, count values that are **functions of the input alone** (prover-independent) on every query the protocol may evaluate, including queries the prover steers off the canonical support.

This is a **canonicity** requirement on a certification, not a lowness statement about an oracle class. **The page's sentence should be replaced by this one.**

## 2. Arm (b), Flag D2: the blocking step, and the terminal (ruling (1))

**The two known routes to a two-sided count certification, and what stops each.**
- **Route 1, upper-bound protocols** (Fortnow; Aiello–Håstad). HMX l.295–307, verbatim:

  > "We cannot necessarily apply, however, the upper bounds of [21, 1] to do the same thing with post-selected distributions D = f(U_S). That is, even though f^{−1}(y) is efficiently decidable, it may not be possible to efficiently generate x ← U_S conditioned on x ∈ f^{−1}(y) (with x that is hidden from the prover). … Although one-sided lower-bound estimates can be obtained from the lower-bound protocol of [30], it is unknown how to get two-sided estimates using the upper bound protocol of [21, 1], where the difficulty is to obtain secret samples from U_S."

  HMX also record that for the **unconditioned** case the route works: "the verifier can sample x ← U_n, compute y = f(x) and ask the prover for an upper bound on the size of the set f^{−1}(y) without revealing x."
- **Route 2, histogram / lower-bound protocols** (HMX's VerifyHist). **Y5 showed this is steerable on the image side**, and that the steering is unbounded because it lives off the honest support.

**Why our round 2 is post-selected.** f₂(ρ, i) is the round-2 query of row ρ **given that row's round-1 answers**. The rows relevant to a count are those whose certified round-1 answers send them to a given y. That is post-selection by the certified answers, i.e. by values the prover supplies. So Route 1's blocked case is exactly ours.

**The terminal statement (ruling (1)), phrased for an HMX reader.**

> **(PL) at two rounds reduces to HMX's open problem in our setting:** obtaining a **two-sided** estimate of |f^{−1}(y)| for a **post-selected** distribution D = f(U_S), without secret samples from U_S — where the post-selection is by the prover-certified round-1 answers, and where the one-sided lower-bound route (GS86) is available but, by Y5, steerable on the image side.

**The smallest case already blocks (k₁ = k₂ = 1).** One round-1 query and one round-2 query suffice: the round-2 query y of the output row is light (π₂(y) can be 2^{−b}), so estimating |f₂^{−1}(y)| by uniform sampling is hopeless, and the conditioned secret sample that Route 1 needs is exactly what HMX say is unavailable. **The failure is not a parameter artefact.**

## 3. Arm (b), Flag S2: the GS86 step, and the hybrid (ruling (2))

**The exact step (verified, EPFL Lecture 8 §3.1).** For the general simulation the notes state:

> "the idea is to make the set S contain all the (private) random strings that makes the private-coin verifier accept."

and the set lower-bound protocol it is run through has

> "P: Try to find an x ∈ S such that h(x) = y. Send such an x to V together with a certificate that x ∈ S."

**So the conversion's mechanism has the prover exhibit an element of S, i.e. a verifier random string.** That is the step at which any secrecy the private-coin protocol relied on is destroyed: the simulation preserves the **verdict**, and it hands the prover a coin string as part of doing so.

**The hybrid is not well defined, and for a sharper reason than I pre-registered.**
- I expected the obstacle to be "all randomness in SS22's Theorem 14 setting is the reduction's own" (H1–H6, verified).
- The sharper point: **the object that would have to stay secret is not any of the protocol's coins.** Route 1 needs a uniform element of the conditioned set f₂^{−1}(y), hidden from the prover. Arthur's coins are the row samples ρ_i (Step 2, public by design so that Arthur can evaluate the query map). Making those private does not produce a conditioned sample; a conditioned sample would have to be **generated by a sampling protocol**, which is HMX's open problem again.
- **So "private coins inside round 1 only" does not name a protocol**: privacy of the existing coins is neither sufficient nor the relevant resource. **This is the finding, as the ruling permits, rather than an attempt.**

## 4. Kill tests

- **C2, Y5's deflating M:** any protocol that closes must reject it. Route 1 with conditioned secret samples would: the verifier could test the claimed light counts against its own hidden sample rather than against prover-exhibited witnesses. Since Route 1 is unavailable (§2), no protocol read rejects M. ✓ consistent with Y5.
- **Silent on ABKMR:** nothing here closes at any round count, so the requirement is met vacuously; the compounding argument of Y5 §2 stands unchanged. ✓
- **Smallest case first:** §2 shows the blockage at k₁ = k₂ = 1. ✓

## 5. Priors against outcome, and misses

| | Y6b | Y6c | Y6a |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 55 → 60 | 20 → 25 | 25 → 15 |
| mine | 60 | 25 | 15 |
| **outcome** | **✓** (Flag D2 blocks; terminal stated) | not reached | not reached |

- **My miss:** the pre-registration's framing "(PL) is loose-access lowness of AM with respect to a promise AM ∩ coAM oracle" is **wrong** (§1). Loose access is a hypothesis on a machine assumed correct; our object is a protocol whose soundness is at issue. The reviewer adopted the phrasing for the page on my statement, so **the page sentence must be amended to §1's corrected (PL)** before it is recorded.
- **The practice line this suggests:** a reformulation offered for the page is checked against the definitions it borrows **before** it is ruled in, not after.
- Flags D2 and S2 held, in the expected order.

## Ceiling

Y6 proves nothing about P vs NP or OWF. It ends the barrier arm at a citable open problem: **two-sided count certification for post-selected distributions without secret samples.** The construction arm is unchanged and still needs non-deep NO instances, which no known mechanism produces.

## Formal record

Untouched (the author's decision).
