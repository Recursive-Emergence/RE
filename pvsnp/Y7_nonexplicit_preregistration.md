# Y7: the non-explicit door. Pre-registration

*Drafted 2026-09-11 on branch `y7-nonexplicit`, on the author's go ("Draft Y7 pre-reg only"), for the reviewer's ruling. **No run until the author says so.** Documents only; `formal/` closed. g1, g5 and g8 apply. The practices apply, including the two newest: every expected failing step is checked against the source's actual protocol, and **a reformulation offered for the page is checked against the definitions it borrows before it is ruled in.***

## Ceiling (first)

Even complete success here is **conditional**: it would give OWF from NP ⊄ BPP, and `NP ⊄ BPP` is itself open and untouched by this branch. Y7 proves nothing about P vs NP.

## §0. Refuted premises checked (the practice)

Not reused: "hidden ρ" (Y3); "no off-sample rows" and "(1+ζ) inflation" (Y4); "the grid is symmetric" (Y5); **"(PL) is loose-access lowness" (Y6, mine, withdrawn)**.

## §1. What LP23's notion actually permits (verified at drafting)

**LP23 l.86–99, verbatim:**

> "we will here focus on defining a notion of OWF-completeness w.r.t. non black-box reductions—in fact, for generality, **we will allow even non explicit reductions** (although the actual reduction presented in this paper will be explicit). … we refer to a problem Π as being **OWF-hard** if it holds that **if Π can be decided (in the worst-case) for infinitely many input lengths by 'efficient attackers', then all poly-time functions can be inverted** with probability 1/2 by 'efficient attackers'."

**The structural point (mine, to be stated in the report).** OWF-hardness is defined as an **implication between statements**, not as a reduction object. So "non-explicit" is not a weaker species of reduction: for the holy grail it suffices to prove the implication

  **NP ⊄ ioBPP ⇒ MK^tP[s]|Q^t_β ∉ ioBPP**

by any means whatever, with no reduction exhibited, named or constructed.

## §2. Which barriers bite, and which do not

**Do not bite, by construction (verified phrasings).**
- GK24's theorems all read "… is hard for SAT **under** a (γ-honest, non-adaptive, randomized, many-one) **reduction** …". The hypothesis is a reduction object.
- SS22's Theorem 3 and its hypotheses H1–H6 are about an oracle machine M and its robustness; Theorem 14 is about simulating **that machine**.
- **So the entropy/SZK barriers are silent on a proof that exhibits no reduction.** That is the whole content of the non-explicit door.

**Flag R7 (my expected first failure; the door is not barrier-free).** A proof of the implication is still a **proof**, and the standard technique barriers constrain proofs, not reductions:
- If "Pessiland" is consistent with relativization — an oracle relative to which NP ⊄ BPP holds and one-way functions do not exist — then **every** proof of the implication, explicit or not, must be **non-relativizing**.
- To verify in the run (g1): Wee, "Finding Pessiland" (TCC 2006), and/or Impagliazzo's five-worlds survey, for the exact statement and its quantifiers. If such an oracle exists, Flag R7 is the door's real cost, and the non-explicit door is "no easier than the explicit one, minus the entropy barriers".
- **Expected:** the oracle exists and is standard, so Y7's answer is "the non-explicit door evades GK24/SS22 but not relativization".

**Flag C7 (the constructivity leak).** If a proof of the implication is itself constructive — a dichotomy whose case analysis can be carried out efficiently — it *yields* a reduction, and the barriers reapply to that reduction. So an argument that evades GK24/SS22 must be **essentially non-constructive**, e.g. a case split on a statement no efficient procedure can decide. The run states this as a constraint on admissible shapes.

## §3. The attempt shape, and the kill test

**The dichotomy to look for.**

> Either MK^tP[s]|Q^t_β is hard on average (hence OWF by LP20/LP23), **or** [structure S exists], and S yields OWF **by a different route**.

**The second horn must not use LP23's equivalence** — otherwise both horns are the same statement and the argument is circular. The run states, for each candidate S, which theorem turns S into OWF.

**Candidates to map (g1, in the run):**
- Hirahara's worst-case-to-average-case line, including STOC'23's conditional characterization (already read in Y1 for its abstract);
- Hirahara–Nanashima ("Learning in Pessiland", secondary so far);
- Liu–Pass's own conditional characterizations (LP23, LP25);
- any statement of the form "either meta-complexity is hard, or there is a learning/compression algorithm", which is the usual win-win in this area.

**Note from drafting:** a grep of the local corpus found no "win-win" or "dichotomy" language in LP23, LP25, Hirahara STOC'23 or HIR23; SS22 uses "dichotomy" only for its own AM ∩ coAM/NEXP split. So the map has to be built from the papers' statements, not from their vocabulary.

**Kill test (the reviewer's): non-circularity.** Both horns using LP23's equivalence is an immediate fail. The run checks each candidate against this first.

**Second kill test (mine):** the dichotomy must not prove more than is true — if the argument would also establish OWF in a relativized world where Pessiland holds, it is wrong, and Flag R7 says where.

## §4. Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **Y7a** | A win-win shape exists that no barrier touches, and its second horn is a stated open problem: the door's address moves there. |
| **Y7b** | Non-explicit arguments are barred too (expected: by relativization, Flag R7), or every candidate second horn is circular. |
| **Y7c** | LP23's non-explicit notion is narrower than it reads, and the door was never open. |

**Priors.**
- Reviewer: Y7b 45 / Y7a 35 / Y7c 20.
- Mine: **Y7b 55 / Y7a 25 / Y7c 20.** Flag R7 carried into the prior: relativization constrains proofs rather than reductions, so the non-explicit door inherits it in full, and the known non-relativizing techniques in this area (Hirahara's) are exactly the ones that produce reductions.

## Ruling (the reviewer's, recorded at acceptance as a draft)

**Accepted as a draft.** No run until the author's separate go. **Priors** moved to mine: Y7b 55 / Y7a 25 / Y7c 20.

**§1's structural point goes on the page as verified**, with the LP23 l.86–99 quote: OWF-hardness is an implication, not a reduction object.

**Ruling (1): the Pessiland kill test is decisive.** Verify Wee (TCC'06) and Impagliazzo's survey for the exact relativized statement — an oracle with NP ⊄ BPP (or NP ⊄ ioBPP; **match LP23's quantifier**) and no OWF. If it stands, state as a **proved consequence**: any proof of `NP ⊄ ioBPP ⇒ MK^tP|Q ∉ ioBPP` is **non-relativizing**, whether or not it exhibits a reduction.

That converts the door's question into: **which non-relativizing ingredients exist that do not produce a reduction?** Map them:
- **arithmetization** — algebrizes (Aaronson–Wigderson);
- **code-reading / non-black-box** — produces reductions (Flag C7);
- **Shannon-style counting over all short programs** — typical-side, produces no algorithm, but also no implication from NP-hardness; **say why**.

If the map has no ingredient of the needed shape, **Y7b is: "the non-explicit door is open only to a non-relativizing, non-algorithmic technique, and none is known"**, stated with the three known ingredients and the reason each fails.

**Ruling (2): Flag C7 as a lemma.** If the dichotomy's case analysis is decidable in polynomial time, the two horns compose into a reduction and GK24/SS22 reapply. So any admissible win-win needs a case split **not decidable in polynomial time**. Record what that means for the second horn's usability: an OWF that exists but cannot be identified is still an OWF — **state whether LP23's "all poly-time functions can be inverted" formulation tolerates that.**

**Ruling (3):** non-circularity first for every candidate S; the map is built from statements, not vocabulary.
