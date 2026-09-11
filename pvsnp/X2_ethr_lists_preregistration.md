# X2: L0 — lower bounds for decision lists of exact thresholds. Pre-registration

*Drafted 2026-09-10 on branch `x2-ethr-lists`, on the author's go ("Draft and run X2, push after merge"), for the reviewer's ruling before any work. g1, g5, g8 and g9 apply. X2 names the lemma under the lemma. It proves nothing.*

## Where X1 left it

- **The fold statement:** IP2 ∉ poly-size THR∘THR.
- **L1** (Chattopadhyay–Mande §8): every poly-size THR∘THR circuit has sign-rank 2^{o(n)}. L1 implies the fold statement via Forster's 2^{Ω(n)}.
- **L0** (Chattopadhyay–Mande's conclusion): strong size lower bounds for *decision lists of exact thresholds* (DL-ETHR) computing an explicit function. They describe it as "a necessary step for proving lower bounds against both THR∘THR circuit size and PMA communication cost."

## Targets (the reviewer's, verbatim in content)

- **(a)** The exact statement of L0, and which containment makes it necessary for L1. What is known about DL-ETHR: Hansen–Podolskii; sign-rank and communication results for exact-threshold lists (g8, with the search stated).
- **(b)** The canonical case, Equality: why EQ obstructs bottom-gate protocols at error 2^{−n^{Ω(1)}}. Does any known measure other than discrepancy and polynomial sign-rank separate DL-ETHR from IP2? Start with the measure Chattopadhyay–Mande use, and say what stops it from covering all of THR∘THR.
- **(c)** Step by step: the Chattopadhyay–Mande lower-bound proof, the first step that fails for DL-ETHR, and whether a verified repair exists.

## Flags raised before any work (mine)

**Flag N (necessity is "implied by", and an upper bound would cut both ways).**
- DL-ETHR ⊆ THR∘THR ("a subclass", per Chattopadhyay–Mande). So a THR∘THR lower bound for f gives a DL-ETHR lower bound for f, and L1 ⇒ IP2 ∉ poly-size DL-ETHR. "Necessary" here means *implied by L1* (and by the fold statement). It is not a stepping stone that implies L1.
- **Conversely:** if IP2 had poly-size DL-ETHR, then IP2 ∈ THR∘THR, which **refutes L1 and settles the fold statement negatively**.
- (a) must therefore also ask whether IP2 is known to have short exact-threshold decision lists.

**Flag P (the PMA route may already give L0 for IP2: the X2b risk).** Chattopadhyay–Mande: "every function expressible as a short decision list of exact thresholds is in PMA" (communication), and "the sign-rank lower bound technique remains the strongest known … it suggests that new techniques need to be developed for proving bounds against PMA."
- **The check:** is PMA^cc contained in a communication class against which IP2 has a *known* lower bound? The candidates are PP^cc, via discrepancy, and PostBPP^cc.
  - If PMA^cc ⊆ PP^cc and IP2 ∉ PP^cc, then IP2 has no short DL-ETHR. **That is L0 for IP2, known: X2b.**
  - If PMA^cc ⊄ PP^cc, or the relation is not stated, record which (g8/g10).
- Sources: Göös–Pitassi–Watson's landscape of communication classes, and Chattopadhyay–Mande's own Appendix A definitions (PMA; BPP^NP).
- Note: F_n ∈ PMA with large sign-rank gives PMA ⊄ UPP (CM). That rules out *UPP* as the containing class, not PP.

**Flag C (the curse is immediate).**
- Chattopadhyay–Mande's measure is sign-rank, via a modified Forster theorem and approximation theory for XOR functions.
- Their own F_n is a *linear-size* decision list of Equalities with sign-rank 2^{Ω(n^{1/4})}. So sign-rank cannot give DL-ETHR size lower bounds beyond what poly-size lists already exceed. **The first failing step for (c) is the base step:** "small DL-ETHR ⇒ small sign-rank" is false.
- Expected unless Flag P changes the picture: X2a, with that as the failing step.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X2a** | L0's first failing step is named, with the measure Chattopadhyay–Mande's proof uses and why it stops: the sub-lemma under L1. |
| **X2b** | A known result the map missed already gives L0, or a case of it. Record it and climb toward L1. |
| **X2c** | Under a closer reading, L0 is not necessary for L1. Record the correction. |

**Priors.**
- Reviewer: X2a 60 / X2b 20 / X2c 20.
- Mine: **X2a 45 / X2b 35 / X2c 20.** X2b is raised by Flag P: the PMA ⊆ PP question may already answer L0 for IP2, even though Chattopadhyay–Mande ask for "an explicit (say, in NP) function" and may not have considered IP2.

## Ceiling

X2 proves nothing. If X2a holds, the attempt phase ends with a two-level open statement, L0 under L1 under IP2 ∉ THR∘THR, each level verified from the literature. If X2b holds, the known result is recorded and the next open level is named instead.
