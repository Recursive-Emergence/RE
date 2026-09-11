# N1: fold accumulation (nesting), mapped. Pre-registration

*Drafted 2026-09-10 on branch `n1-fold-accumulation`, on the author's go ("Draft and run N1, push after merge"), for the reviewer's ruling before any work. This reopens the program paused at 4b50c67 on the reviewer's user's correction. Documents only. g1, g8, g9 and g10 apply. N1 proves nothing about P ≠ NP.*

## The correction (the reviewer's, recorded)

The program treated "folding" as **composition**: one-way-function chains, and R3's "fold". The intuition is **nesting**: problems fold into problems, a statement about a statement, one quantifier or one layer of depth per fold. Composition does not accumulate alternation; nesting does. **The reviewer records this as its ninth premise miss.** `PROGRAM_final_state.md` §1 is amended when N1 is in, and not before.

## Targets (the reviewer's, verbatim in content)

- **(a) Unbounded.** Tarski's undefinability and Kleene's strictness of the arithmetical hierarchy: the exact statements, and where the diagonal uses unbounded evaluation time.
- **(b) Bounded, proved.**
  - Håstad's depth hierarchy for AC⁰: Sipser functions, exact statement and size bound.
  - Rossman–Servedio–Tan (FOCS 2015): the average-case depth hierarchy, and its corollary that PH is infinite relative to a random oracle.
- **(c) Bounded, open: the smallest open fold.**
  - Depth hierarchies for AC⁰[p].
  - Depth 2 vs depth 3 for threshold circuits: the known depth-2 lower bounds (Hajnal–Maass–Pudlák–Szegedy–Turán, inner product), the status of depth 3, and what Kane–Williams 2016 gives.
  - Name the smallest open statement of the form "the (d+1)-th fold adds, for an explicit function, in class C".
- **(d) The barriers at the top.**
  - Relativization: which oracles collapse PH (Baker–Gill–Solovay), and which make it infinite (Yao/Håstad; random oracle, RST).
  - Natural proofs: what Razborov–Rudich says about depth-hierarchy proofs for AC⁰[p] and TC⁰.
- **(e) The reading, labelled.** The diagonal proves accumulation only where the evaluator is unbounded; bounded, it relativizes. This is the fifth appearance of "naming costs what it names".

## Flags raised before any work (mine)

**Flag O (the known link to PH is oracle-only).** As I recall it, and to be verified (g1): the Furst–Saxe–Sipser / Yao / Håstad route turns lower bounds for depth-d AC⁰ circuits of size 2^{polylog} into oracles A with Σ_d^{p,A} ≠ Σ_{d+1}^{p,A}. That is a *relativized* separation.
- No known implication runs from an AC⁰ depth hierarchy, which is proved, to *unrelativized* PH strictness, which is open. The proved depth hierarchy therefore is **not** "the intuition's theorem" for PH, except black-box.
- If the sources confirm that the link is only through oracles, the precise gap is N1c's "the exact gap". The report must state it without inferring more (g10).

**Flag L (a bounded, clocked nesting hierarchy that *is* proved: the log-time hierarchy).** As I recall it, to be verified: DLOGTIME-uniform AC⁰ corresponds to the *logarithmic-time hierarchy* LH (Barrington–Immerman–Straubing), and Sipser 1983 (with Håstad's bounds) proves LH strict.
- If verified, this is the unrelativized, clocked "folds accumulate" theorem. It holds only at log time, where the machine cannot read its whole input, which is the black-box regime again.
- The report states which clock the proof tolerates.

**Flag C (the smallest open fold may be below AC⁰[p]).**
- Depth-2 threshold circuits (THR∘THR, or MAJ∘MAJ) may already lack superpolynomial lower bounds for explicit functions in large classes. I recall NEXP vs THR∘THR as open; to be verified.
- If so, the smallest open fold is **depth 2 → depth 3 for threshold circuits, or even the depth-2 lower bound itself**, not a hierarchy question.
- The report states the frontier per class, from sources: AC⁰[p], TC⁰ depth 2, TC⁰ depth 3.

**Flag N (natural proofs).**
- Razborov–Rudich's barrier applies to classes that contain pseudorandom functions. TC⁰ does, under Naor–Reingold-type assumptions, to be verified. AC⁰[p] is not known to, and Razborov–Smolensky's natural proof succeeds there.
- So "is that why AC⁰ methods stop?" gets different answers per class. The report does not assert one answer for all of them.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **N1a** | The map is as stated, and the smallest open fold is a named circuit-depth statement, with its known partial results. |
| **N1b** | A known depth-hierarchy result already covers the class believed to be the crux, moving the smallest open fold up. Record where. |
| **N1c** | The nesting reading fails at (a)–(b): PH strictness does not reduce to depth hierarchies as stated. Record the exact gap. |

N1a and N1c can co-occur: a named smallest open fold exists, and the bridge to unrelativized PH is oracle-only. The report states both if so.

**Priors.**
- Reviewer: N1a 60 / N1b 15 / N1c 25.
- Mine: **N1a 45 / N1b 15 / N1c 40.** N1c is raised by Flag O: the proved bounded accumulation reaches PH only through oracles.

## Ceiling

Nothing here proves P ≠ NP. N1 corrects the program's mapping of the intuition and names the smallest open instance of "the next fold adds". Any attempt on it is pre-registered separately.
