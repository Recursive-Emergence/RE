# M5: the finite Gödel theorem. Pre-registration

*Drafted 2026-09-10 on branch `m5-finite-godel`, on the author's go (draft, run, push after merge), for the reviewer's ruling before any work. It is a document only; guards g1, g8, g9, g10 and g11 apply.*

## Target

M4 landed on Pudlák's **CON^N⁺**, "the finite Gödel theorem", with the smallest instance **"EF has no polynomial-size proofs of Con_{iEF}(n)"**. M5 maps that conjecture and how far toward it the verified record reaches.

## Flags raised before any run

**Flag I: the shape of an instance.**
- CON^N⁺ is about a **pair** of theories: "if T proves Con_S, then S-proofs of Con_T(n̄) cannot be bounded by a polynomial".
- Its instances therefore need **T strictly stronger than S, with T ⊢ Con_S**, and the statement concerns S-proofs of the *stronger* system's finitistic consistency.
- Garlík (resolution on its own refutation statements) and Davis–Robere (depth-d Frege on its own Prf formulas) concern a **single system reasoning about itself**. That is closer to a second-incompleteness shape than to the CON^N⁺ pair shape.
- **So they are not assumed to be instances.** The run must check, for each candidate, whether it has the pair form (possibly through a propositional translation Pudlák states) before counting it toward G2. Its expectation is that they do not, which lowers G2.

**Flag N: which NE / coNE implication.** A search summary in M2 put Krajíček–Pudlák 1989 as "E = NE ⇒ *p-optimal* proof systems exist". The ruling states "NE = coNE ⇒ *optimal* proof systems exist", from which CON^N (no length-optimal system) ⇒ NE ≠ coNE would follow. The run must verify the exact statements from a text before deriving any consequence for CON^N.

**Flag D: the diagonalization paper.** Krajíček, *Diagonalization in proof complexity* (Fundamenta Mathematicae), is to be read for what it proves and what it rules out. It is neither assumed to close nor to open the lever.

## What the run must deliver

**(a) Pudlák 2017, mapped.** CON, CON^N, CON^N⁺ and RFN^N_1: exact statements (partly verified in M4), the class 𝒯 of theories they range over, the verified implications among them and to NP ≠ coNP, NE ≠ coNE (Flag N), and "no (p-)optimal proof system". Quantifier forms (g9).

**(b) What is known toward CON^N⁺, for any pair (S, T).** Every verified partial result:
- Krajíček–Pudlák 1989;
- Köbler–Messner–Torán on optimal proof systems;
- Pudlák 2017's own partial results;
- any unconditional instance for a weak S, **in the pair form** (Flag I).

**(c) Krajíček, *Diagonalization in proof complexity*.** What it proves about whether diagonal arguments can yield tautologies that are hard for strong systems, iEF in particular, and what it says cannot be done that way.

**(d) The smallest instance, exactly:** EF ⊬_poly Con_{iEF}(n). What a proof would need: which of the derivability conditions Pudlák 1986 uses survive for iEF, which fail, and whether a partial truth definition applies to implicit proofs. M4 could not find the last point stated; it stays "not found" unless a source states it (g8, g10).

**(e) The cost, honestly.** What CON^N (and the EF/iEF instance) implies that is itself open, for example NE ≠ coNE (if Flag N verifies), and an EF lower bound for an explicit family (M2's frontier).

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **G1** | CON^N⁺ for EF/iEF is stated in the literature with its obstacles named. The smallest form is Pudlák's conjecture, and the path is his. |
| **G2** | An unconditional instance exists at the bottom of the ladder, *in the pair form*. The finite Gödel theorem is a theorem for weak systems, and the question is how far up it climbs. |
| **G3** | Krajíček's diagonalization paper shows that diagonalization cannot yield iEF-hard tautologies under standard assumptions. The lever is closed at the top, and the reason is the finding. |

**Priors.** Mine: G1 50 / G3 25 / G2 25, with G2 lowered by Flag I. The reviewer's: G2 40 / G1 35 / G3 25.

## Ceiling

M5 proves nothing. It locates the programme's endpoint on a named conjecture with Gödelian content, and reports how far up the ladder it is already a theorem, in the correct pair form.
