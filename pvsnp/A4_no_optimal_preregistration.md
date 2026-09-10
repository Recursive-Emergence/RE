# A4: no optimal proof system — what is known, and whether the barriers reach it. Pre-registration

*Drafted 2026-09-10 on branch `a4-no-optimal`, on the author's go ("Draft and run A4, push after merge"), for the reviewer's ruling before any work. g1, g8, g9, g10, g11 and g12 apply. A4 is the last mapping item: it proves nothing. After it comes one consolidated page (`pvsnp/PROGRAM_final_state.md`), and then the loop pauses.*

## Why A4

A3 left the path at the cross form. The finite Gödel theorem in its only form with content for all systems is
- **CON^N**: ∀S ∃T, S-proofs of Con_T(n̄) are not polynomially bounded;
- equivalently, **no length-optimal proof system** (Pudlák 2017, verified in M5).

That implies RFN^N_1 and then NP ≠ coNP (verified in A3). A4 maps what is known about that statement, and whether the relativization barrier reaches it.

## Targets (the reviewer's, verbatim in content)

- **(a) The statement family**, exact, with quantifier forms:
  - optimal (simulation) vs p-optimal (p-simulation);
  - CON^N ⟺ no optimal, and CON ⟺ no p-optimal (Pudlák 2017, verified);
  - Krajíček–Pudlák 1989: NE = coNE ⇒ an optimal system exists, and E = NE ⇒ a p-optimal one exists. M5 held this only at secondary; reach the primary if possible;
  - Köbler–Messner–Torán 2003: p-optimal ⇒ complete sets for which promise classes;
  - Messner, and Beyersdorff–Köbler–Müller, on converses and nondeterministic variants.
- **(b) Relativization.** Oracle worlds in both directions. Ben-David–Gringauze 1998 (ECCC) is the candidate source, plus any oracle remarks in KP89 and KMT.
- **(c) Natural proofs and algebrization.** Anything analogous for proofs of non-optimality, and a record of the search (g8).
- **(d) Non-relativizing results** toward non-optimality, if any. If the conditional results of (a) are the whole record, say so.
- **(e) The self-reference reading, tested once.** An optimal system is a universal simulator. Does any theorem use that universality against itself, i.e. a diagonal over all systems? The place to read is Krajíček's "Diagonalization in proof complexity" trichotomy, whose arms include "no p-optimal system": read exactly how it arises. If the diagonal gives only the trichotomy, the reading gives no leverage.

## Flags raised before any work (mine)

**Flag R (one direction is expected to be automatic; the finding is the other one).**
- Under any oracle A with P^A = NP^A (Baker–Gill–Solovay), TAUT^A has a polynomially bounded proof system, which is trivially optimal and p-optimal. This holds provided the relativized notion is "proof systems for TAUT^A computed with oracle A". So the "optimal exists" direction should be automatic and uninformative.
- **The substantive question is an oracle relative to which no optimal (or no p-optimal) system exists.** The report states which notion each source relativizes: TAUT^A vs plain TAUT, and optimal vs p-optimal. It does not merge them (g9).
- If the only no-optimal oracles are for p-optimality, or for a different relativization, the outcome is **O2**, not O1.

**Flag V (what a barrier shows).** Relativization in both directions shows only that *relativizing* techniques cannot settle the statement. The report says what it blocks and nothing more. If confirmed, the "same barrier at the metamathematical layer" observation is written as **consistency with the RE reading, not progress** (the reviewer's instruction, adopted).

**Flag P (primaries).**
- Reached in earlier phases: none.
  - KP89 was secondary in M5.
  - Krajíček's diagonalization paper was reached only as EUDML HTML, whose class names were UNVERIFIED because the HTML and BibTeX drop them.
- This run tries arXiv, ECCC and the authors' pages. Where only a secondary is reached, the claim carries the tag.
- No TLS bypass.

**Flag D (the diagonal).** In Krajíček's trichotomy, the arm "no p-optimal system" may appear as one of three *possibilities*, not a consequence of the diagonal. If so, (e) fails by construction: a trichotomy whose arms include the target gives no leverage toward it. The report quotes the statement and says which it is.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **O1** | Barrier-blocked both ways ((b) verified), and no non-relativizing partial result. The path ends at a named open problem with the same barrier as the original. |
| **O2** | An oracle exists in one direction only, or the relativization status is unsettled. Record which. |
| **O3** | A non-relativizing partial result toward non-optimality exists: the first live lead at this layer. |

**Priors.**
- Reviewer: O1 65 / O2 25 / O3 10.
- Mine: **O1 55 / O2 35 / O3 10.** O2 is raised by Flag R: the no-optimal oracle may exist only for one notion (p-optimal, or a non-standard relativization), and a primary may be unreachable.

## Ceiling

A4 proves nothing. At best it names "no optimal proof system" as the endpoint of the program's path, with its barrier status stated exactly. Anything further is mathematics on one of the named open statements, pre-registered as an attempt.
