# W20: (D3) -- a history-hardness notion whose easiness is NP-certifiable. Pre-registration

*Drafted 2026-09-12 on branch `w20-history-hardness`, on the reviewer's W20 specification, after W19 closed at `b159497`. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. The target, verbatim, and the ceiling

**The target is RW26 §5's own question**, quoted on the W19 page and repeated here so this page is self-contained:

> "Let `Π` be an encoded computational history, then either `Π` is 'hard enough' to solve AVOID, or `Π` is 'easy' so that one can 'reconstruct' `Π` efficiently. **Is there a suitable definition of 'hardness' so that any 'hard enough' `Π` can be used to solve AVOID in `FP^NP_tt`, while `Π` being 'easy' implies an efficient MA algorithm for reconstructing `Π`?**"

**Ceiling.** A positive answer would give a better uniform reconstruction and hence a better near-maximum circuit lower bound -- RW26 say so in the sentence introducing it. It would not by itself open the door: (C_1) is `FP^NP`, this asks for `FP^NP_tt`. But it is the authors' own open question, so **the prior that this round closes it should be low, and the prior that this round says something precise about why it is hard should be high.**

**This round is an ATTACK, not a survey.** The deliverable is either a candidate notion with both halves checked, or the tension between the halves named at named parameters.

**The two constraints any candidate must respect** -- and they are this line's own results, so they are the one part of the round I am not re-deriving:

- **Theorem W16.2** (bc60bd8): relative to the W16.0 oracle, `Avoid ∈ FP^{NP^A}` but `Avoid ∉ FP^{NP^A}_tt`. So **the "hard enough ⇒ `FP^NP_tt`" half cannot be proved from plain-circuit hardness by a relativizing argument.** Any candidate notion that relativizes and is implied by plain hardness is dead on arrival.
- **Theorem W18.1** (4150bb8): a string hard enough to derandomise stage `i`'s reconstruction is already hard enough to run Korten at stage `i+1` directly. So **the "easy ⇒ efficient MA reconstruction" half cannot be strengthened to a deterministic reconstruction by using the residue's own hardness.** The MA in RW26's question is not laziness; W18.1 says the obvious way to remove it is circular.

## §1. Refuted premises checked

Not reused: the four W16 errors, the three W17 errors, **Lemma W17.1**, and the three W18 errors (the base-hardness margin, the `d ≥ ℓ` kill of the chained version, the refutation of fact (a)). **Ten consecutive wrong impossibility claims.**

**The bias runs at this round in a specific way I want named in advance.** The natural shape of a negative result here -- "the two halves are in tension" -- is an impossibility claim, and that is the category in which I have been wrong ten times running. The natural shape of a positive result -- "here is a notion, here is why each half holds" -- is a construction, and that is the category in which I have not yet been wrong. **Flag A20 and the priors below are both set with that asymmetry deliberately applied.**

## §2. Disclosure: what I already believe, and one real contamination

**(a) CONTAMINATION, declared rather than buried.** In W19's PATH line, written *before* this round opened, I already recorded a prior on this very question:

> "the likeliest destination of (D3) is the same wall, because NP-certifiable easiness demands a short certificate for a statement whose natural certificate is a circuit -- which is where both SU05 Thm 4.10's equivalence queries and RW26's Merlin sit. If W20 lands there it is a sixth arrival and the conclusion is that the wall is the problem, not the route."

I flagged it to the reviewer as strikeable so this round could open clean, and it has not ruled yet. **I am not going to pretend I do not hold it.** It is disclosed here, it is an impossibility intuition, and by §1 it is therefore suspect. **If the round lands on the wall, the finding must be checked against the possibility that I steered it there.**

**(b) The mechanism I expect, stated so it can be wrong.** The "easy" half wants: `Π` easy ⇒ an *MA* algorithm reconstructs `Π`. The "hard" half wants: `Π` hard ⇒ AVOID in `FP^NP_tt`, i.e. **non-adaptive**. I expect the tension to be that the easiness *witness* is a circuit, and "this circuit is wrong here" has no short certificate -- so certifying easiness needs either an equivalence-query oracle (SU05 Thm 4.10) or Merlin (RW26), and Merlin is exactly what the `FP^NP_tt` half is trying to remove. **This is a guess at a mechanism, not a checked claim, and it is the same guess as (a).**

**(c) What I expect to be the live design freedom.** RW26 say "a *suitable* definition of hardness". The freedom is in the *notion*, not the algorithm -- e.g. hardness against a restricted circuit class, hardness of a *padded* or *encoded* history rather than the raw one, or a promise/average-case variant. **I have not thought about which, and I am deliberately not doing so before the priors are committed.**

**(d) Not done -- no primary read for this round.** Already read in earlier rounds and therefore not "new": RW26 §5 (the target itself, W18/W19); RW26's construction §4 (W18); SU05 Def 2.4, Thm 3.6, Cor 3.7, Thm 4.10 (W5, W19); Shaltiel-Viola Prop 1.8 / Open Problem 1.9 (W18); DS26 Informal Thm 1.8 (W5). **Not yet consulted for this round:** Korten 2021's hardness notion in its own terms; CHR24 / Li24's dichotomy as they state it; anything on NP-certifiable circuit-easiness or succinct refutation certificates; the MA-reconstruction literature; ECCC 2024-2026 for this specific question.

## §3. Priors, fixed now

| code | outcome | **mine** |
|---|---|---|
| **20a** a candidate notion is produced and both halves are checked to hold, at named parameters | **12** |
| **20b** the two halves are shown to be in tension, with the obstruction named at named parameters and checked against W16.2 and W18.1 | **53** |
| **20c** other -- e.g. a specific candidate class is ruled out without a general tension, or (D3) is shown to reduce to a named open problem | **35** |

**Why 20a is 12 and not 2.** W17's 17a and W18's 18a were both priced at 2 because they would have been *unconditional breakthroughs*. **This is not that.** (D3) is a definitional design question its own authors pose as answerable, a positive answer improves a reconstruction rather than proving a new separation, and -- decisively -- **a positive outcome here is a construction, which is the half of my output that has been reliable.** Pricing it at 2 would be importing a number from rounds whose ceiling was categorically different.

**Why 20b is 53 and not higher.** It is the impossibility-shaped outcome, and §1 says that is where I have been wrong ten times running. I hold the belief (§2(a)-(b)) and I am discounting it *because* I hold it.

**Why 20c is 35.** Between them, the most likely concrete result of an honest attack is a partial one: a named class of candidate notions ruled out, or a reduction to something already open. That is neither 20a nor 20b as stated.

## §4. Flags

- **Flag A20 -- the asymmetry is applied, not just noted.** A tension claim needs an inequality or a construction with both sides named; a construction claim needs both halves checked. **The tension claim gets the harder audit**, because it is the category with the ten-for-ten failure record.
- **Flag B20 -- verbatim with numbers, and the W19 method line.** No statement from memory or from the reviewer's paraphrase. **When a cited theorem number will not resolve, search for what the theorem says, not what it is called** -- that is how SU05 Thm 4.10 was found after "3.16" failed, and how W5's apparently-missing 3.11/3.15 were explained.
- **Flag C20 -- both constraints checked explicitly.** Every candidate notion is tested against **W16.2** (does it relativize? is it implied by plain hardness? if both, it is dead) and **W18.1** (does the MA half secretly need the residue's hardness? if so, it is circular).
- **Flag D20 -- the stop-rule, inherited and binding.** If 20a appears to close, stop, send the exact parameters, and write nothing further until the reviewer has checked it. A positive answer to a published open question gets a second pair of eyes before it gets prose.
- **Flag E20 -- score against §2(a).** If the outcome is the wall, the write-up must say explicitly whether the round *found* it or *steered* to it, and what would have distinguished the two.

## §5. Kill tests

- **(i)** RW26's question quoted verbatim and answered as asked -- both halves, not one.
- **(ii)** Every candidate notion stated precisely enough that "hard enough" and "easy" are complementary; a gap between them is a failure of the candidate, not a detail. *(This is W18's exhaustiveness point, which is why the win-win's thresholds coincide.)*
- **(iii)** W16.2 and W18.1 applied to every candidate (Flag C20), and **not** cited as evidence for anything else -- different models, they do not transfer.
- **(iv)** ECCC 2024-2026 swept before writing "open" about any sub-question.
- **(v)** If the outcome is a tension, it is stated as an inequality or a construction, never as an intuition -- and its **premises are audited before its arithmetic, bookkeeping steps first** (the standing W17 line).
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Flag E20's steering question answered explicitly, whatever the outcome.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
