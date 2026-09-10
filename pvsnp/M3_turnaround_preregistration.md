# M3: the turnaround at the object that survives. Pre-registration

*Drafted 2026-09-10 on branch `m3-turnaround`, on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. It is a document only; guards g1, g8, g9 and g10 apply, plus a new g11.*

## What M2 established (as the reviewer weighs it, recorded here)

1. **Davis–Robere refutes the "Gödel's second theorem" reading** in its general form. A proof system *can* prove strong lower bounds against itself, as depth-d Frege does on Prf^{Frege_d}(PHP). Counted at the reviewer's request as its **eighth wrong outcome prior**.
2. **Where the reading survives: typical objects.** Pich–Santhanam: no propositional proof system efficiently proves certain hardness statements about *random* truth tables (M1, abstract verified).
3. **The observation, stated once, with its three verified instances.** In every layer examined, the obstruction concerns *typical* objects, never *named* ones:
   - instances: R2's density barrier;
   - adversaries: R4/R5, compressibility versus density;
   - tautologies: here, named PHP families versus random truth tables.

   This is an observation from three instances, not a theorem.
4. **The stall.** It is at constant-depth Frege with modular counting gates, below Frege (M2).

## The question

Pich–Santhanam's unprovability is **unconditional**. Can it be turned into a hardness statement about an **explicit** family, which is what a lower bound needs? What exactly blocks it?

**Pre-registered expectation (the reviewer's):** the block is explicitness itself. The turnaround needs a named f_n, and a named f_n is by density not typical, so it falls where a system may well prove things. In short: Gödel's move needs a name; the residue has none.

## Flag G (raised before the run): provability versus proof length

- **Gödel's move** turns *unprovability* of a Π₁ sentence's negation into the sentence's *truth*, given Σ₁-completeness (M1, Claim 2).
- **Pich–Santhanam's result** is about *proof length*: certain tautologies have no *short* proofs.
- A tautology is true by definition, so there is no unprovability-to-truth step to take on it. The only Π₁ sentences in play are proof-size statements H_{P,s} (M1), such as "P has no s-size proof of τ_n".
- **The run must write down exactly which sentence is unprovable in which system, and what the turnaround would convert it into**, before attempting the turnaround. If the mismatch between provability and length breaks the argument *before* explicitness does, the outcome is **T3**. New guard **g11:** at every step, state whether it concerns provability (existence of any proof) or proof length.

## What the run must deliver

1. **Pich–Santhanam stated exactly.** The theorem's precise statement, its quantifier form (g9), what "random truth table" means (distribution, and "for most f" versus "for a random f with high probability"), which proof systems it covers, and what "efficiently" means. From the paper's text.
2. **The turnaround as an attempted argument,** step by step, with g9 and g11 at each step and the first failing step named.
3. **Derandomization (g8).** Does any explicit family with Pich–Santhanam-type unprovability exist? Look in Pich's later work and in Krajíček on the hardness of proof-complexity generators.
4. **If none: the exact sentence a derandomized Pich–Santhanam would be,** as the smallest form at this layer.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **T1** | The turnaround fails at explicitness, as expected. The tension is stated at its third layer, and the smallest form is a derandomized Pich–Santhanam. |
| **T2** | An explicit family with Pich–Santhanam-type unprovability exists. The turnaround is live, and its remaining steps become the programme. |
| **T3** | The turnaround fails earlier, at the quantifier, the theory, or the provability-versus-length step (Flag G). Record which. |

**Priors.** Mine: T1 55 / T3 35 / T2 10 (T3 raised by Flag G). The reviewer's: T1 65 / T3 25 / T2 10.

## Ceiling

M3 proves nothing about P vs NP. At best it names the smallest sentence at this layer, a derandomized Pich–Santhanam, and the exact step at which the turnaround fails.
