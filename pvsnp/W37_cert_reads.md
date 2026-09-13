# W37: (CERT), coins versus reads. Pre-registration (one bounded round, reading-heavy)

*Drafted 2026-09-12 on branch `w37-cert-reads` (from `w36-arity3-collisions` at 1a9468a), on the reviewer's specification after its user said to move along. The black-box sub-line stays at rest. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed cold: before reading RW26 §3 or W20 §§6-8 for this round.** The reviewer's semantic-redissection page (`W_semantic_redissection.md`, fad1e69) is on its branch and is not read here.

## §0. Target (the reviewer's)

(D3-door) = **(CERT)**: a deterministic `poly(S)`-time acceptance-probability estimate for the circuit `z ↦ V^C(x, z)`, of size `S = poly(k, r, log t)`, on `polylog(t)` coins. **The reviewer's claim:** enumeration is dead at any coin count that addresses a `poly(t)`-size proof, so the fold must be over **reads**. (Q2) is a fooling lemma for estimators reading `polylog(t)` positions of a generic proof; (Q3) says the estimator using the history's local computability is a Merlin committing to a circuit, so W18.1 applies and this is a **seventh arrival**; (Q4) asks whether the history's low-degree encoding gives daylight.

## §1. Framing audit before the prior -- the reads framing looks wrong

**(a) The estimator is WHITE-BOX.** As the reviewer states (CERT), the estimator's input is **the circuit** `z ↦ V^C(x, z)` of size `S`. The proof is accessed through `C`, and the estimator has `C`'s **full description**, not oracle access to proof positions. **A fooling argument over unread positions does not apply to an algorithm that is handed the whole circuit.** (Q2)'s lemma, if true, is about a black-box read model that (CERT) does not use.

**(b) White-box (CERT) is CIRCUIT ACCEPTANCE PROBABILITY (CAPP) for small circuits with many inputs.** The input length is `m ≥ r ≥ Θ(log t)` coins, and the size is `S = poly(log t)`. Enumeration costs `2^m ≥ t`, against a budget of `poly(S) = polylog(t)`: dead, as the reviewer says, **but for the familiar reason that CAPP in time `poly(S)` on `m = S^{Ω(1)}` inputs is general derandomization**, not because of read counts.

**(c) General CAPP is the standard hardness-versus-randomness object**, and the standard route to it is a **plain** circuit lower bound for `E`. *Stated from memory and marked for verification against a primary, not used as a premise:* Impagliazzo-Wigderson-type results give CAPP in polynomial time from `E ⊄ SIZE[2^{εn}]`; Impagliazzo-Kabanets-Wigderson give the converse direction toward `NEXP ⊄ P/poly`. **Plain `E` hardness implies `E^NP` hardness, which already opens the door by Korten.** So the derandomization route to (CERT) is **dominated by the door**, which is W20's recorded "Korten Theorem 10 dominance" in another form. **To be checked on W20's page (§§6-8) before any conclusion: whether W20 already recorded exactly this, in which case W37's contribution is a framing correction, not an arrival.**

**(d) What (Q3) and (Q4) become under (a)-(c).** (Q3): "estimable from the history's structure" means CAPP for the **specific** circuit family `{V^C}`, not general CAPP. The real question is whether that family is easier than general circuits. **That is W20 §7's question as recorded**, not a new arrival. (Q4): the low-degree encoding is part of the family's structure. Whether it makes the family's acceptance probability computable (e.g. because a self-corrector's acceptance on a genuinely low-degree codeword is 1, or is determined by a few evaluations) is the **one** place a family-specific algorithm could live. **Daylight, if any, is there.**

## §2. Priors

| code (the reviewer's) | reviewer | **mine** |
|---|---|---|
| 37a a coin or read reduction makes (CERT) poly(S)-computable | 5 | **3** |
| 37b non-enumerative at every coin count; reduces to a short certificate; seventh arrival | 70 | **27** |
| **37c** something else: daylight in (Q4), or a mis-reading of the budget | 25 | **70** |

**Why 37c at 70:** §1(a) says the reads framing mis-reads (CERT)'s access model, and §1(b)-(c) say the coin count is the standard derandomization wall, already dominated. **The most likely outcome is a framing correction that returns (CERT) to W20 §7's statement, plus a check of (Q4)'s family-specific daylight.** **Why 37b at 27, not lower:** if RW26 or W20 define the estimator's access as oracle reads (not white-box), the reviewer's framing is right and 37b follows its reasoning.

## §3. Reading order and flags

1. **W20 §§6-8** from its committed page: the access model of (CERT), what "Korten Theorem 10 dominance" covered, and the §8 counting.
2. **RW26 §3** (extracted text in the job scratch directory): the self-corrector's coin source (dimension × log field size, or repetition), the verifier's `r`, and **what Recon does with the self-corrector's outputs** (Q4).
3. **Flags.** A37: settle white-box versus oracle access from the sources before pricing anything. B37: every statement from memory in §1(c) verified or marked unverified. C37: one round.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# W37 Findings

*Appended after the reviewer's ruling (37c). Nothing above is revised.*

## §4. Ceiling

**Nothing proved.** A reading round on (D3-door) = (CERT). No statement about `FP^NP`, `E^NP`, or P vs NP. The door is unmoved.

## §5. Outcome against priors

| code | mine / reviewer | outcome |
|---|---|---|
| 37a coin or read reduction | 3 / 5 | -- |
| 37b non-enumerative, seventh arrival | 27 / 70 | -- |
| **37c** something else, or a mis-reading of the budget | **70** / 25 | **the outcome: the reads framing mis-read (CERT)'s access model; W20's sixth arrival restated, plus one new sentence (§8)** |

## §6. The miss that produced the round (the reviewer's nineteenth, in its words)

The specification re-derived W20 §7 **from memory instead of from the page** and got its quantifier wrong. W20 §7, verbatim: *"(CERT) A deterministic algorithm that, **given the circuit** `z ↦ V^C(x, z)` of size `S = poly(k, r, log t)` on `m = polylog(t)` input bits, decides whether `Pr_z[accept] = 1` or `Pr_z[accept] ≤ 1/2`, in time `poly(S)`."* **The estimator is white-box**, so a fooling argument over unread proof positions does not apply. W20 §8's counting (*"any position never queried under any seed can be set adversarially by the prover. Hence ... `r ≥ log(proof length) − log q`"*) is **PCP soundness against the verifier's coins**, not a bound on an estimator.

## §7. The numbers (Q1), from RW26 §3 and Theorem 2.3

- **PCP verifier:** *"Arthur samples randomness `z ← O(log t(n))` (for the PCP verifier)"*.
- **Self-corrector:** *"`z_Corr ← {0,1}^{polylog(t(n))}` (for the Low-Degree Self-Corrector)"*. Theorem 2.3's `Corr` *"runs in time `poly(∆, log |F|, m)` and outputs `P(x)` with probability at least 2/3"*, and *"the correct probability can be boosted to `1 − 1/poly(t(n))` by repetition"*. **Decomposition: `polylog(t) = (m·log|F|` coins per call, one random line`) × O(log t)` repetitions `× (r′(n) + 1)` evaluated bits** (the prefix bits and the output bit).
- **Both confirm W20 §7 exactly.** (Q3): the sources of white-box (CERT) are W20 §9's two, both closed (W18.1; Korten dominance). **Sixth arrival restated, not a seventh**; the "two doors are one" attribution to W4 §2 (2026-09-11) stands.

## §8. The finding (Q4)

RW26's YES case: *"Since `Π_x = (w̃_x, Π′_x)` for some polynomial `w̃_x` of total degree at most `m|H|`, the Low-Degree Self-Corrector always returns the correct value ... with probability 1"*, and *"`Pr_z[V^C(x, z) accepts] = 1`"*. **Perfect completeness plus exact low-degreeness of the honest proof means Arthur's coins matter only against a cheating `C`.** An NP-oracle machine can check both exact properties deterministically: "`C` restricted to every line has degree `≤ m|H|`" and "`∀z V^C(x, z)` accepts" are each coNP. After those checks, decoding is direct evaluation. **So each reconstruction query becomes a `Σ₂` query:**

> **`∃C` [exactly low-degree on every line ∧ `∀z V^C(x, z)` accepts ∧ prefix condition].**

> **THE GAP BETWEEN THE Σ₂ RECONSTRUCTION AND THE DOOR IS EXACTLY: derandomise a universal quantifier over `polylog(t)` coins against an existentially chosen size-`S` circuit.** That is white-box CAPP for the family, dominated by the door. **A `Σ₂`-versus-NP boundary object, not plain-versus-SVN.**

*Precision note (mine, not re-derived):* a `Σ₂`-oracle reconstruction yields a lower bound for exponential time with a `Σ₂` oracle, a class above the known `S₂E ⊆ Σ₂E` rung (CHR24, Li24). The reviewer calls this "the known `Σ₂E` rung". **Which class exactly the `Σ₂` win-win lands in is not re-derived here**; the finding is the gap statement, which does not depend on it.

## §9. Practice line

**RE-DERIVE A CLOSED STATEMENT FROM ITS PAGE, NOT FROM MEMORY: its quantifier is the part memory drops** (white-box "given the circuit" became "reads of the proof").
