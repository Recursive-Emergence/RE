# Y6: (PL) at two rounds, as a question in interactive proofs. Pre-registration

*Drafted 2026-09-11 on branch `y6-pl`, on the author's go ("Draft Y6 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply:*
- *smallest case first;*
- *every bound beside the record and the literature;*
- *every flag's implication carried into the priors;*
- *every expected failing step checked against the source's actual protocol;*
- *every new pre-registration checked against the previous report's refuted premises;*
- *when a printed inequality and the cited protocol disagree, the protocol wins, and the disagreement is logged.*

## Ceiling (first)

**Y6a would be a barrier, not a construction.** The construction arm stays where Y2 left it: it needs non-deep NO instances, which no known mechanism produces. Y6 says nothing about P vs NP.

## §0. Refuted premises checked (the practice)

Not reused here: "hidden ρ" (SS22 is public-coin); "no off-sample rows" (GS has the prover exhibit them); "(1+ζ) inflation" (Lemma B gives A/δ); SS22's printed Lemma 22 direction (the GS reading holds); "the grid is symmetric" (Y5: inflation sits on the honest support, deflation off it).

## §1. The literature map (arm (a)), done at drafting

| statement | status | bearing on (PL) |
|---|---|---|
| **Low(AM) = AM ∩ coAM** (Arvind's column l.233; verified in Y3) | for **languages** | (PL)'s oracle is a promise object: the canonical count J[γ] is defined only on the good γ (SS22's Propositions 15–16) |
| **GGH17:** psdAM = search-P^{promise-(AM∩coAM)}, "for valid inputs x, **all queries to the oracle must be in the promise**" (verified in Y4 §3) | **smart** access | steering produces out-of-promise queries by construction, so this does not apply |
| **Smart versus loose access** (Grollmann–Selman; from the drafting search, **secondary**, to be verified in the run): smart access forbids out-of-promise queries; loose access permits them, and the machine must be correct **irrespective of the oracle's behaviour** there | the distinction | **(PL) is a loose-access question**, and worse: the prover both chooses which queries leave the promise and supplies the answers there |
| **GS86 private → public coins** (Yale notes, verified in Y4; Holenstein–Künzler l.150–175, verified in Y5) | theorem | the candidate bridge for arm (b) |
| **Fortnow; Aiello–Håstad set upper bound** (Holenstein–Künzler l.158–161; HMX l.286–292, both verified) | needs a **verifier-secret uniform element** of the set | the image side would be fixed by secret samples, which public coins do not provide |
| **HMX l.300–307** (verified): for post-selected distributions "it is unknown how to get two-sided estimates using the upper bound protocol … the difficulty is to obtain secret samples" | open | our round-2 map is exactly post-selected (conditioned on round-1 answers) |

**So the map has a named gap: loose-access lowness for a promise AM ∩ coAM oracle whose off-promise queries are prover-chosen. Nothing read states it.**

## §2. Arm (b): the two-round attempt, with my flags

**The plan (the reviewer's).** Run round 1 with **private** coins, so the image side can be certified by a Fortnow/Aiello–Håstad upper bound against verifier-secret samples; then convert the whole protocol to public coins by GS86.

**Flag S2 (my expected first failing step: the conversion preserves acceptance, not secrecy).**
- GS86 converts a private-coin interactive proof into a public-coin one **with the same language**, by simulating the private-coin verifier's acceptance probability through set lower bounds.
- The image-side upper bound's soundness does not rest on the acceptance probability alone. It rests on the prover **not knowing** the verifier's sample while the protocol runs.
- After conversion, every coin is public, so the sample is known to the prover at the moment the round-2 map is evaluated, and the steering of Y4/Y5 returns.
- **Expected: the conversion is sound as a simulation of the private-coin protocol's verdict, and useless for the property the image side needs.** To be stated exactly: which step of the GS86 simulation reveals the sample, and whether a hybrid (private coins only inside round 1, public elsewhere) is even well defined in SS22's Theorem 14 setting, where all randomness ρ is the reduction's own.

**Flag D2 (the private-coin protocol may not exist before any conversion).**
- The image side would need a secret uniform element of f₂^{−1}(y), or of the domain conditioned on the steered map.
- **HMX say this is open** for post-selected distributions (l.300–307, verified).
- So arm (b) may fail before the conversion step, at "the verifier cannot sample the conditioned set secretly".
- **Expected order of failure: Flag D2 first, Flag S2 second.** If D2 blocks, the run states (PL) as: *a two-sided count certification for post-selected distributions, without secret samples* — i.e. exactly HMX's open problem, restricted to our setting.

**Flag C2 (what a positive answer would have to beat).** Y5's explicit deflating M: round 2 asks prefix_c(ρ) at answers ≥ a − 1 and prefix_{c′}(ρ) below, with Merlin's histogram all at weight 2^{−c′}. **Any protocol that closes must reject that strategy**, and the run checks it explicitly.

## §3. Kill tests (the reviewer's)

- **Silent on ABKMR:** the conversion's cost must compound with rounds, so nothing closes at n rounds (IW98's Lemma 16, verified in Y4).
- **Catches Y5's M:** as in Flag C2.
- **Smallest case first:** one round-1 query (k₁ = 1) and one round-2 query (k₂ = 1), where A = r + log k. If the attempt fails even there, the failure is not a parameter artefact.

## §4. Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y6a** | (PL) proved at two rounds. The bounded-round barrier follows for all few-bits-of-adaptivity reductions: a new theorem. Re-derive twice, and pass both kill tests. |
| **Y6b** | Fails at a named step in the private → public conversion (expected Flag S2), or before it (expected Flag D2). (PL) is then reduced to that step. |
| **Y6c** | A known lowness or transformation result already gives it: cite and climb. |

**Priors.**
- Reviewer: Y6b 55 / Y6a 25 / Y6c 20.
- Mine: **Y6b 60 / Y6c 25 / Y6a 15.** Carrying the flags in:
  - Flag D2 points at an open problem stated in HMX, which makes Y6a unlikely.
  - Y6c is raised to 25 because the smart/loose distinction is standard, and some loose-access lowness statement may exist in the promise-problem literature that I have not read.

## Ruling (the reviewer's, recorded at acceptance as a draft)

**Accepted as a draft.** No run until the author's separate go.

**Priors** moved to mine: Y6b 60 / Y6c 25 / Y6a 15.

**§1's reformulation goes in as the page's statement of (PL):**

> "(PL) is loose-access lowness of AM with respect to a promise AM ∩ coAM oracle where the prover both chooses the out-of-promise queries and supplies their answers."

Grollmann–Selman's smart/loose definitions are to be **verified in the run and cited**. GGH17's smart-access condition is exactly what steering violates.

**Ruling (1), if Flag D2 blocks.** The private-coin image-side upper bound needs a verifier-secret uniform sample from the post-selected set, which HMX l.300–307 state as open. Then Y6b is:

> "(PL) at two rounds reduces to HMX's open problem, restricted to our setting"

with the citation, and **that is the barrier arm's terminal**. State it so that a reader of HMX would recognize it.

**Ruling (2), Flag S2.** Name the exact step of the GS86 conversion at which the sample becomes prover-visible, and say whether a hybrid (private coins inside round 1 only) is well defined when all randomness is the reduction's own (Theorem 14's setting). **If the hybrid is not even well defined, that is the finding**, and it is stated rather than attempted.

**C2 and the smallest case (k₁ = k₂ = 1)** stand as drafted.
