# M4: succinct diagonal tautologies. Report

*Run 2026-09-10 on branch `m4-diagonal`, after the author reviewed the draft and said to run it, against the pre-registration and the reviewer's sharpened (c). g1, g5, g8, g9, g10 and g11 apply. "Verified" means checked against the source text or official abstract. Derivations of mine are marked and proved.*

## Outcome: **D1**

The succinct diagonal can be stated, and its catch has two parts, one proved here and one a known conjecture:
- **(proved) Self-reference is size-bounded in the referring system's own measure.** A diagonal sentence can exclude only proofs whose size, in the proof system's own measure, is at most polynomial in the sentence's size. Compression changes the measure, not the ratio.
- **(verified) The succinct question is Pudlák's finite-Gödel conjecture.** Asking whether a weaker system has short proofs of a stronger system's consistency statements is Pudlák's **CON^N⁺**, stated by Pudlák himself. Its sibling CON^N is equivalent to the nonexistence of a length-optimal proof system and implies NP ≠ coNP.

The smallest form is an **explicit** tautology family whose conjectured hardness is exactly the frontier (§(d)).

Priors: mine D1 65; the reviewer's D1 60.

## (a) The diagonal construction, and where it lives

- **First-order form (verified, Pudlák 1986).** The lower bound on Con_T(n) is proved "using finitistic counterparts of the well-known derivability conditions for the 2nd incompleteness theorem" (paper text, l.303–305), with T ⊇ Q.
- **Propositional ρ_n(π) := ¬Prf_P(π, ⌜ρ_n⌝):** a verified statement of it as such was **not found** (g8). Searches: Pudlák 1986, Pudlák 2017, and Krajíček's abstracts. Its soundness argument is elementary. If π were a P-proof of ρ_n of size ≤ s, then ρ_n(π) would be false, so P would have proved a non-tautology, contradicting soundness.

## (b) The cost: Flag S, proved and generalized

**Claim (mine).** Let Q be any Cook–Reckhow proof system: a polynomial-time f onto TAUT. Let ρ be a formula that asserts, of a string variable π with |π| ≤ s, that π is not a Q-proof of ρ. Then:
1. |ρ| ≥ s, because ρ contains the s variables of π;
2. every Q-proof x of ρ has |x| ≥ |ρ|^{1/c} ≥ s^{1/c}, where n^c bounds f's running time, because |f(x)| ≤ |x|^c;
3. soundness yields "no Q-proof of size ≤ s".

So the diagonal's bound improves on the trivial bound (2) by at most a polynomial. For systems whose proofs contain their conclusion (Frege-type), it adds nothing at all. ∎

**Generalization to implicit systems (mine).**
- An implicit system iP is itself a Cook–Reckhow system. Its proofs are circuits β together with a P-proof that β describes a correct P-proof; Wang's definition for implicit resolution is quoted below. So the Claim applies to iP *in iP's own measure*.
- A diagonal referring to implicit proofs of size ≤ n has size ≥ n, and excludes only iP-proofs of size ≤ n.
- The exponentially long P-proofs those circuits describe are excluded only when they *have* small circuit descriptions, and that is exactly iP-proof size.
- **Compression changes the measure, not the ratio.** No superpolynomial lower bound for an arbitrary sound system follows, which is why the "if compression were free, NP ≠ coNP" argument has no force. The catch is located.

**The first-order analogue, verified (Pudlák 1986).**
- Con_T(n) has length O(log n): n is written in binary, and the sentence quantifies over proofs.
- The lower bound is n^ε. The upper bound is n^k "for reasonable T" (intro, l.40–46; "The lower and the upper bound are only polynomially distant").
- The upper bound needs *sequential* theories, in which "finite pieces of information about the universe are coded in natural numbers" (§5 definition). It is proved through a partial truth definition: in Theorem 5.5's proof, Tr_n is defined via Sat_n.
- It holds "also for PA and ZF" (l.1308).

So quantifier compression already works, and the gap stays polynomial in n.

## (c) Implicit proofs: the reviewer's sharpened question

**Definitions (verified).**
- Krajíček, *Implicit proofs*, JSL 69(2) 2004, official abstract: from a proof system P one constructs iP, which "operates with exponentially long P-proofs described 'implicitly' by polynomial size circuits".
- Wang, *Implicit Resolution*, arXiv:1308.5608, abstract verbatim: "an implicit resolution refutation of Ω is a circuit β with a resolution proof {α} of the statement 'β describes a correct tree-like resolution refutation of Ω'".

**(i) Is Con_{iP}(n) definable in size poly(n)?** Yes, by the definition: an iP-proof is a pair (β, α) checkable in polynomial time, so "no iP-proof of size ≤ n proves ⊥" is a Π₁ statement, and a tautology family, of size poly(n). *(My reading of the verified definition.)*

**(ii) Its proof complexity in P, iP and EF:**
- Krajíček's official abstract says iEF "corresponds to bounded arithmetic theory [image]", "polynomially simulates the quantified propositional calculus G", and "the soundness of iEF is not provable in [image]". The theory names are images on the page; the search summary gives them as **V¹₂** and **S¹₂**, which is **secondary**.
- Under the standard meaning of correspondence, the theory proves the soundness of its system (Cook–Nguyen, verified in M2).
- Whether iEF has polynomial-size proofs of its *own* Con_{iEF}(n) is **not found stated** (g8). By g10 it is not inferred.

**(iii) Is it equivalent to a known open question? Yes, as a restatement.**
- **Implicit resolution is EF.** Wang, verbatim: "We show that such system is p-equivalent to Extended Frege", with "[EF,P] ≤_p [R,P] for arbitrary Cook-Reckhow proof system P". Lower bounds for implicit resolution *are* EF lower bounds, the known frontier.
- **The consistency question is Pudlák's conjecture.** Pudlák, *Incompleteness in the finite domain*, BSL 2017 (paper text, verified):
  - **CON^N:** "For every S ∈ T, there exists T ∈ T such that the lengths of S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n."
  - **CON^N⁺:** "for every S, T ∈ T, if T proves Con_S, then S-proofs of Con_T(n̄) cannot be bounded by a polynomial in n."
  - CON^N is **equivalent to** "There exists no length-optimal proof system" ([27], cited there). CON^N implies RFN^N_1, "and we will prove that Conjecture RFN^N_1 implies NP ≠ coNP". The uniform version, CON, is equivalent to "There exists no p-optimal proof system".
  - Pudlák: "If Conjecture CON^N were proven true, we would certainly advocate calling it the finite Gödel theorem."

## (d) The smallest form at this layer

> **EF has no polynomial-size proofs of Con_{iEF}(n).**

- This is an **explicit** tautology family, one of polynomial size for each n.
- Its superpolynomial EF-hardness is an instance of **CON^N⁺**: the theory corresponding to iEF proves the consistency of EF's theory, and the secondary-verified correspondence facts place the pair accordingly. It is an open conjecture.
- It is the precise object behind the Gödelian reading. Its truth would be the "finite Gödel theorem" for the pair (EF, iEF), and a superpolynomial EF lower bound for an explicit family, the frontier M2 located.
- *This instance is formed from the verified pieces; Pudlák states the general conjecture, not this instance.*

## The obstruction at its fourth layer

**Naming costs size** (Claim §(b)): the diagonal sentence is as large as what it excludes, in the referring system's own measure. Compression moves the question from "short P-proofs" to "short iP-proofs", and it arrives at Pudlák's finite-Gödel conjecture, a known frontier statement. This is consistent with the observation recorded in M3's pre-registration, "the obstruction concerns the typical, never the named", now in the form: a self-reference *names*, and naming is paid for in size.

## Readout additions (on the reviewer's acceptance)

**1. CON^N⁺ is escape-by-extension stated as a proof-complexity conjecture.**
- Its hypothesis is that T proves Con_S; its conclusion is that S-proofs of Con_T(n̄) are not polynomially bounded.
- So the layer above, a theory that settles S's consistency, is exactly the layer whose finitistic consistency S cannot reach cheaply.
- On the name, Pudlák: *"If Conjecture CON^N were proven true, we would certainly advocate calling it the finite Gödel theorem."*
- In the originating framework's terms, this is its prediction that a residue is settled one layer up, stated here once. *(The single interpretive line.)*

**2. Compression and reuse meet at the proof layer.**
- The verified theorem is Wang's: implicit resolution, meaning compression through circuits that describe proofs, "is p-equivalent to Extended Frege".
- EF's defining power is its *extension* rule, which introduces abbreviations that are then reused.
- *Reading, not theorem:* at the proof layer, succinct description and reusable abbreviation have the same strength. The verified content is the p-equivalence of the two systems. The identification of the two *operations* is an interpretation of it, the closest this programme has come to the Gödel-numbering intuition it started from.

## Calibration

- **The reviewer:**
  - its catch (b) was right, and sharpened here;
  - its sharpened (c) led directly to CON^N⁺;
  - its D1-through-(iii) expectation held, restatement included.

  No premise misses.
- **Me:** Flags S and F held, and D1 held.

## Sources (checked this run)

- Krajíček, *Implicit proofs*, JSL 69(2) 2004: <https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/implicit-proofs/B6E778CBA3308E4A172F66FFDEB07054> (official abstract; theory names secondary)
- Wang, *Implicit Resolution*: <https://arxiv.org/abs/1308.5608> (abstract)
- Pudlák, *Incompleteness in the finite domain*, BSL 2017: <https://users.math.cas.cz/~pudlak/inco.pdf> (text)
- Pudlák 1986: <https://users.math.cas.cz/~pudlak/fin-con.pdf> (text: intro, §3 l.303–305, §5, Theorem 5.5, l.1308)
- Cook–Nguyen (M2) for the meaning of correspondence
