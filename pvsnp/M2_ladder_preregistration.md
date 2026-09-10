# M2: assembly. The theory / proof-system ladder and its fixed point. Pre-registration

*Drafted 2026-09-10 on branch `m2-ladder`, on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. It is a document only; guards g1, g8 and g9 apply.*

## Target (the reviewer's shape)

The per-system Π₁ sentences H_{P,s} (from M1) assemble toward NP ≠ coNP only through the correspondence between theories and proof systems. M2 verifies four things:
- **(a)** the correspondence;
- **(b)** the finitistic-Gödel fixed-point theorems;
- **(c)** the ladder of known lower bounds and where it stalls;
- **(d)** the prediction that a system's lower bound is provable "one layer up".

## Flags raised before any run

**Flag P (polynomial versus superpolynomial).** Pudlák's 1986 lower bounds on proofs of finitistic consistency statements Con_T(n) are expected to be **polynomial** (of the form n^ε), not superpolynomial. If so, "a system cannot cheaply prove its own consistency" is a *polynomial-gap* statement. It is then not the superpolynomial hardness that NP ≠ coNP needs. The run records the exact bound.

**Flag O (optimality versus self-reference).** Krajíček–Pudlák 1989 is expected to concern the *existence of an optimal (or p-optimal) proof system*, linked to NE vs coNE and to finitistic consistency, rather than a literal self-reference obstruction. If the primaries do not have the fixed-point shape the ruling describes, the outcome is **A3**, and it is recorded as such.

**Flag L ("one layer up" needs a definition).** Pre-registered here:
- a lower bound for P is *one layer up* if it is provable in a theory T′ whose corresponding proof system P_{T′} is the *next known rung* above P;
- "far above" means provable only in a theory whose proof system is several rungs up, or only in theories of unknown or strong position such as PA.

Where the literature does not say in which theory a lower bound is provable, the answer is "not found" (g8), never inferred.

## What the run must verify

**(a) The correspondence.**
- Cook 1975: PV and Extended Frege.
- The general form (Krajíček–Pudlák; Buss): to a theory T corresponds a proof system P_T such that T ⊢ Ref(P_T), and P_T p-simulates every P whose reflection principle T proves.
- Exact statements, and the known pairs, for example: EF ↔ S¹₂ / PV; Frege ↔ a theory for NC¹; bounded-depth Frege ↔ bounded arithmetic with Δ₀ induction (IΔ₀) / V⁰; resolution ↔ a relativized theory. All to verify, not assume.

**(b) The fixed point.**
- Krajíček–Pudlák 1989, *Propositional proof systems, the consistency of first-order theories and the complexity of computations*: what is proved about (i) short P-proofs of Con_T(n), (ii) optimal proof systems, and (iii) NE vs coNE and finitely axiomatized theories.
- Pudlák 1986: bounds on lengths of proofs of finitistic consistency statements.
- For each: exact statement, conditional or not, and quantifier form.

**(c) The ladder.** For each of resolution, Res(k), polynomial calculus, bounded-depth Frege, Frege and Extended Frege:
- the strongest verified lower bound for an explicit family;
- the theory in which that lower bound is provable, where stated;
- quantifier form (at a fixed bound, Π₁, as in M1).

The stall to confirm: no superpolynomial lower bound is known for Frege or Extended Frege. Record the strongest known Frege lower bound; is anything beyond linear or quadratic known?

**(d) The prediction, checked against (c).** Classify each known lower bound as one layer up, far above, or not found (Flag L).

## The deliverable

- **The ladder as a table:** system | corresponding theory | known lower bound | theory proving it | quantifier form.
- **The fixed-point theorems of (b),** stated exactly.
- **The stall, named.**

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **A1** | The ladder is as predicted up to the stall, and (b) characterizes the stall as a self-reference obstruction. |
| **A2** | The ladder exists, but the lower bounds live far above their systems. Escape by extension is real but not one step; record the gap. |
| **A3** | (b) does not have the fixed-point shape described. Record it. |

**Priors.** Mine: A2 50 / A3 30 / A1 20. The higher A3 is from Flags P and O. The reviewer's: A2 50 / A1 30 / A3 20.

## Guards

- **g1:** no citation from memory.
- **g8:** "not found" and "unknown" are admissible answers.
- **g9:** every statement carries its quantifier form.
- **g10 (new):** the provability of a lower bound in a theory is recorded only where a source states it; placements on the ladder are never inferred.

## Ceiling

M2 proves nothing about P vs NP. It locates the stall and states exactly the theorems that govern it.
