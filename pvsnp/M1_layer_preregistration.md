# M1: the metamathematical layer, mapped. Pre-registration

*Drafted 2026-09-10 on branch `m1-layer`, on the author's go (draft, run, push after merge; M2 and M3 each need their own go), for the reviewer's ruling before any work. It is a document only, and guards g1 and g8 apply. It reopens the closed R-program on the reviewer's user's correction: the aim is to find a path, not only to shrink the problem to a known statement.*

## The frame (the reviewer's reading, stated once)

A proof of P ≠ NP is a certificate: polynomial-time to check, found by search (Gödel's 1956 letter). Razborov–Rudich can be read the same way: a hardness proof whose technique is efficient would be an efficient recognizer of hardness, contradicting what it proves. On this reading it is Gödel's second incompleteness theorem in the complexity register, so the proof must come from a layer above, and characterizing that layer is the path. *This is interpretive; M1 verifies only the theorems.*

## Flags raised before any run

**Flag Q: the quantifier level.**
- P ≠ NP is **Π₂**: for every polynomial-time machine M (and every polynomial bound), there is an input on which M fails to decide SAT.
- Gödel's positive move, "unprovable inside, therefore true", works for **Π₁** sentences, because a false Π₁ sentence has a checkable counterexample that the theory proves. For Π₂ sentences, unprovability does not imply truth.
- So M2's outcome G3, where the Gödel move fails at the quantifier, is a live possibility and must be tested first. **M1 records, for each theorem it maps, the logical form of the sentences involved.**

**Flag C: citations to settle, not assume.**
- *Ben-David–Halevi (1992).* The exact theory (PA plus all true Π₁ sentences, or another), and the exact function f in "NP ⊆ DTIME(n^{f(n)})". The expectation is a very slowly growing f; it is to be verified.
- *"Kurtz–O'Donnell–Royer".* Proposed by the ruling with a question mark. It is to be located and verified, or dropped under g1.

## What M1 maps (each item to be verified against the source text)

| Item | Question for the run | Source to check |
|---|---|---|
| (a) | Which theory; which formalization of natural proofs; which pseudorandomness assumption; the exact statement | Razborov 1995, *Unprovability of lower bounds on circuit size in certain fragments of bounded arithmetic* |
| (b) | The exact theorem: if P ≠ NP is independent of theory T, then NP ⊆ DTIME(n^{f(n)}) for which f and which T; and any strengthenings or relatives | Ben-David–Halevi 1992, *On the independence of P versus NP*; the Kurtz–O'Donnell–Royer item if it exists |
| (c) | The exact statement of the barrier one layer up | Pich–Santhanam, FOCS 2019, *Why are proof complexity lower bounds hard?* |
| (d) | Proof-complexity generators; the tautologies τ(f), "truth table f has no circuit of size s" (true exactly on MCSP's No-instances, the R2 object reappearing as tautologies); which proof systems are known or conjectured not to prove them efficiently, under which assumptions | Krajíček; Razborov (to locate the primary texts) |
| (e) | Which independence results exist and which do not | Aaronson 2003, *Is P versus NP formally independent?* |

## The deliverable

One page:
- the layer's objects: a theory T, its proof system P_T, the tautologies τ(f), and a generator;
- its verified theorems, each with its logical form;
- **the fixed point, circled:** the relation between "T proves P ≠ NP" and "P ≠ NP", as given by (b).

## Outcomes for M1

| Code | Outcome |
|---|---|
| **L1** | All five items are verified, and the layer map is complete. |
| **L2** | Some item cannot be verified (g1/g8). The map is partial and says which. |
| **L3** | A premise of M2 is already refuted by what M1 finds, for example Flag Q in a form that closes the Gödel move. M1 then records G3 early. |

**Priors (mine):** L1 45 / L2 35 / L3 20. Access to the 1990s papers is the main risk for L2.

## Guards

- **g1:** no citation from memory; UNVERIFIED counts as none.
- **g8:** "not found" and "unknown" are admissible answers.
- **g9 (new):** every mapped statement carries its quantifier form (Π₁, Π₂, Σ₂…), so that M2 can apply the Gödel test mechanically.

## Ceiling

M1 does not prove P ≠ NP. It maps the layer where the problem is about its own provability, with each statement's logical form attached.
