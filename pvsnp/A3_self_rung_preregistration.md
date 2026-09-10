# A3: finite second incompleteness, the self rung. Pre-registration

*Drafted 2026-09-10 on branch `a3-self-rung`, on the author's go ("Draft A3 only": pre-register and stop, no run until the author says so), for the reviewer's ruling before any work. g1, g5, g8, g9, g10, g11 and g12 apply. A3 is a verification-and-mapping step: it proves nothing, and an attempt at the smallest open self rung would be A4, pre-registered separately.*

## Why A3 (the reviewer's framing, adopted)

A2's Lemma 3 empties the reflection pair form on strict rungs: there, "S ⊬_poly rfn_T" is just the separation of S from T. The remaining independent content is the **self rung**: a system's inability to prove its *own* reflection principle, a finite second-incompleteness statement. The known self rungs are Resolution (Atserias–Bonet) and Cutting Planes (Pudlák, Theorem 3.11).

## Targets (the reviewer's, verbatim in content)

- **(a)** RFN^N_1's exact statement from Pudlák 2017, with its quantifier form (g9). Verify the two implications CON^N ⇒ RFN^N_1 ⇒ NP ≠ coNP from the text.
- **(b)** Which self rungs are known above Res and CP: Res(k), bounded-depth Frege F_d, Frege (Pudlák's Problem 1). g8 applies to each. Atserias–Bonet's Theorem 5 is a *cross* statement (Res(2) over Res's reflection) and settles no self rung.
- **(c)** The smallest open self rung, presumptively **Res(2) ⊬_poly rfn_Res(2)**. State what Atserias–Bonet's proof for Res uses and which step fails for Res(2), before any attempt. Lemma 3's substitution trick does not help at a self rung, because there is no stronger system to project from.
- **(d)** The typical-vs-named reading, once, and only if it survives (b)–(c).

## Flags raised before any work (mine)

**Flag S (self-for-all-P is false as literally stated).** Pudlák 2020 l.799: "so far we only know that the strong systems p-prove their reflection principles, while the weak ones probably do not."
- So "for every proof system P, P-proofs of rfn_P are not polynomially bounded" fails for strong systems such as CF, if l.799 is read as covering CF. (b) must confirm this from a statement, not from l.799's summary.
- **S1 as worded ("RFN^N_1 verified as the self-rung-for-all-P statement") therefore cannot occur** unless RFN^N_1 restricts P or changes the formula, for example Σ^b_1 reflection rather than full reflection.
- The self rung has content only on the *weak* side of Pudlák's weak/strong divide. The Gödelian question becomes where that divide falls, not a statement for all P.

**Flag X (our own record already suggests a cross form).** The merged M5 report (§(a) table, from Pudlák 2017) records:
- **CON^N**: "For every S ∈ 𝒯, there exists T ∈ 𝒯 such that …". This is a **∀S ∃T cross** statement, equivalent to "there exists no length-optimal proof system".
- **RFN^N_1**: "the finite Σ^b_1-reflection version".
- M5 §(b): "His family has no superpolynomial self-case conjecture."
- **My prediction: RFN^N_1 is also ∀S ∃T.** If so, then by A2's Lemma 3 (extended to systems closed under substitution; to be checked, not assumed) its reflection instances on strict rungs reduce to non-simulation, consistent with CON^N ⟺ no optimal proof system. That is outcome **S2**.
- (a) will quote the statement and settle this. It will also say whether the "1" is Σ^b_1 (a restriction on the formula) or something else.

**Flag O (obstructions to pre-register for (c), candidates only, unverified).**
- **The interpolation route fails.** Atserias–Bonet's Theorem 11 uses *monotone feasible interpolation of Resolution* (p. 15, read in A2). Atserias–Bonet p. 14, read in A2: "Res(k) does not have monotone feasible interpolation (see [ABE02] and Corollary 1 in this paper)". So that route fails at Res(2) at a named step.
- **The disjunction route fails too.** Pudlák's Corollary 3.8 route uses the *feasible disjunction property* of Res. arXiv:2003.10230 is titled "Failure of Feasible Disjunction Property for k-DNF Resolution …". Its content is to be read; a title is not a statement (g1).
- If both are confirmed, (c) names the obstruction as: **both known routes to the Res self rung use a feasible-interpolation-type property that Res(2) lacks.**

**Flag T (Theorem 11's form carries over).** Any self-rung lower bound imported from Atserias–Bonet carries A2's Flag Q finding: 2^{Ω(s^{1/4})} along chosen triples, not 2^{N^ε}.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **S1** | RFN^N_1 verified as the self-rung-for-all-P statement ⇒ NP ≠ coNP. The target is named; (b) gives the frontier; (c) states the smallest open self rung and its obstruction. |
| **S2** | RFN^N_1 is something else. Record what it is, and whether a self-rung-for-all-P statement appears anywhere in Pudlák's family. |
| **S3** | (b) finds Res(2)'s self rung already settled. Climb to the next rung. |

S2 and S3 can co-occur; the report states both if so. Under S2, (b)–(d) still run: the frontier and the smallest open self rung are wanted in every outcome.

**Priors.**
- Reviewer: S1 60 / S2 25 / S3 15.
- Mine: **S1 10 / S2 75 / S3 15.** S2 is raised by Flags S and X, both from texts already read and merged.

## Ceiling

A3 proves nothing. At best it locates finite second incompleteness in the weak/strong landscape and names its smallest open case. Under Flag S, that statement cannot hold for all P, so it cannot by itself be a route to NP ≠ coNP. The route to NP ≠ coNP stays the cross-form CON^N / RFN^N_1 chain (M5), whose strict-rung reflection instances A2 reduced to separations.
