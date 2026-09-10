# M2: the theory / proof-system ladder and its fixed point. Report

*Run 2026-09-10 on branch `m2-ladder`, against the pre-registration (accepted; the reviewer's notes on Flags P and O are applied). g1, g8, g9 and g10 apply: "verified" means checked against the source text or its official abstract, and a theory placement is recorded only where a source states it.*

## Outcome: **A3 for the fixed point, and a finding outside A1/A2 for the ladder**

- **(b), the fixed point.** The theorems exist and are self-referential, but they do not characterize the stall. Pudlák's bound is polynomial (a *weak* fixed point). Krajíček–Pudlák concerns optimality. That is **A3** for the fixed-point shape the ruling described, with the theorems kept.
- **(d), "one layer up".** The prediction fails **in both directions**:
  - some known lower bounds are provable only well above their system;
  - one is provable *below* its own system.

  Neither A1 ("one step") nor A2 ("far above") describes this, so it is recorded as found. Placements on the ladder are **not monotone**.
- **(c), the stall.** The stall is stated in a verified source, and it is lower than Frege: at **constant-depth Frege with modular counting gates**.

Priors: mine A2 50 / A3 30 / A1 20; the reviewer's A2 45 / A3 30 / A1 25. The A3 part was pre-registered as Flags P and O. The non-monotone ladder was not anticipated by either side.

## (a) The correspondence (verified)

- **Cook 1975, Main Theorem (5.5)** (paper text): "a proof system f for the propositional calculus is p-verifiable iff extended resolution can simulate f efficiently, and the proof that the simulation works can be formalized in PV".
- **Cook–Nguyen**, *Logical Foundations of Proof Complexity* (2008 draft, text):
  - "translations are defined from V⁰ to bounded-depth PK-proofs (i.e. bounded-depth Frege proofs), and also from V¹ to extended Frege proofs", with each theory proving the soundness of its system (§1, Ch. 7);
  - "Universal theorems of VNC¹ translate into polynomial-size families of Frege proofs. Finally, VNC¹ proves the soundness of Frege systems, but not of any more powerful propositional proof system";
  - TV⁰ ⊢ RFN_ePK appears as an exercise (Ch. 10).
- **Resolution's theory.** A source-stated placement is T¹₂(α) + dwPHP(PV(α)), as the theory that characterizes the reasoning needed for the easiest resolution lower bounds (Li–Li–Ren, arXiv:2411.15515, abstract). That is a theory *for proving resolution lower bounds*, not the theory corresponding to resolution itself; the latter is **not found** here (g10).

## (b) The fixed point, stated exactly

| Theorem | Statement | Form | Status |
|---|---|---|---|
| **Pudlák 1986** | For reasonable T with Q ⊆ T there exist ε > 0 and k such that (1) any proof of Con_T(n) in T has length ≥ n^ε, and (2) some proof of Con_T(n) in T has length ≤ n^k. "The lower and the upper bound are only polynomially distant." The lower bound needs only Q ⊆ T. | Con_T(n) is a finitistic consistency statement for each n; the bounds are polynomial | verified (paper text, intro and §3) |
| **Krajíček–Pudlák 1989** | On "the length of proofs of the sentences saying that there is no proof of contradiction in S whose length is < n", related to propositional proof systems | self-referential (finitistic consistency) | verified (official abstract) |
| **Krajíček–Pudlák (restated)** | An optimal propositional proof system exists ⟺ a fast consistency prover exists; NP = coNP implies a fast consistency prover | optimality ↔ consistency | **secondary** (arXiv:2004.05431 abstract) |

**How to read it (the reviewer's note on Flag P, applied).** The self-reference obstruction exists at this layer and is **polynomial**: a theory cannot prove its own finitistic consistency in fewer than n^ε steps, but it can in n^k. It separates nothing at the NP ≠ coNP scale. Optimality, the layer's universal object, is tied to fast consistency provers. That is the right object, but it is not a characterization of the stall.

**The strong form, a superpolynomial lower bound in P for a self-referential family of P, per system:**
- **Resolution: yes.** Garlík (MFCS 2019, abstract verified): "For any unsatisfiable CNF formula we give an exponential lower bound on the size of resolution refutations of a propositional statement that the formula has a resolution refutation."
- **Bounded-depth Frege: the opposite.** Davis–Robere (ECCC 2026/055, abstract verified): in the regime of exponential length and polynomial line size, "depth-d Frege proofs can refute Prf^{Frege_d}_{s,l}(PHP^{n+1}_n)", giving "an example of a proof system P which seemingly can prove its own lower bounds". The upper bounds "can already be implemented in the fragment Res(log)", which is "the first example of a propositional proof system which is capable of proving strong lower bounds against itself".

So the strong self-referential obstruction holds at the resolution rung and **fails** at the bounded-depth Frege rung for this family.

## (c) and (d): the ladder

| System | Corresponding theory | Known lower bound (explicit family) | Where the lower bound is provable (g10) | Form |
|---|---|---|---|---|
| Resolution | not found (g10) | Haken: PHP needs superpolynomial size (via Pich–Santhanam, verified) | the reasoning power is characterized by T¹₂(α) + dwPHP(PV(α)) (Li–Li–Ren, abstract); **Extended Frege** proves the PHP lower-bound formulas efficiently (Cook–Pitassi, via Pich–Santhanam, verified) | Π₁ at a fixed bound |
| Res(k), polynomial calculus | not found | generators hard for Res(ε log n) and for PC (Razborov 2015; ABRW; verified in M1) | not found | Π₁ at a fixed bound |
| Bounded-depth Frege | V⁰ (Cook–Nguyen) | Ajtai: PHP superpolynomially hard, strengthened to exponential (via Pich–Santhanam, verified) | "constructive proofs … appear to be efficiently implementable within Extended Frege" (Bellantoni–Pitassi–Urquhart, via Pich–Santhanam: *appear*, not proved); and the Prf-formula lower bounds are refutable **within depth-d Frege and even Res(log)** (Davis–Robere) | Π₁ at a fixed bound |
| Constant-depth Frege with modular counting gates | not found | **none**: "significant effort … but without any success. Thus the Cook–Reckhow program is also stalled" (Pich–Santhanam, verified) | — | — |
| Frege | VNC¹ (Cook–Nguyen) | no superpolynomial bound known (implied by the stall above). The quadratic-size bound is **UNVERIFIED** (search summary only; Buss's notes unreachable) | — | — |
| Extended Frege | V¹ / PV (Cook 1975; Cook–Nguyen) | none known | — | — |

**The stall, named from a verified source:** constant-depth Frege with modular counting gates, which lies below Frege. Everything above it on this ladder has no verified superpolynomial lower bound.

**The prediction (d), checked against the table (Flag L).**
- For resolution, the verified propositional placement is **far above** (Extended Frege).
- For bounded-depth Frege, one lower-bound family is provable **below** its own system (Res(log)).
- **So the ladder is not "one layer up", and not uniformly "far above" either.** Escape by extension is real but not monotone. For some systems and families no extension is needed at all.

## Calibration

- **The reviewer:**
  - the fixed-point framing of KP'89 did not survive at the primaries (A3, pre-registered as Flag O);
  - the stall was expected at Frege, but the verified source places it lower;
  - the "one layer up" prediction fails, and in a direction neither side listed.

  These are outcomes, not premise misses. Its note on Flag P was exactly right.
- **Me:** Flags P and O were right. My A2 prior (50) missed the within-system case. Davis–Robere was not anticipated by either side.

## Sources

- Cook 1975: <https://www2.karlin.mff.cuni.cz/~krajicek/cookpv.pdf> (text)
- Cook–Nguyen draft: <https://www.cs.toronto.edu/~sacook/homepage/book/> (main.ps, text)
- Pudlák 1986: <https://users.math.cas.cz/~pudlak/fin-con.pdf> (text)
- Krajíček–Pudlák 1989: official abstract, JSL 54(3); restatement in arXiv:2004.05431
- Pich–Santhanam FOCS 2019 (text)
- Garlík, arXiv:1905.12372 (abstract)
- Davis–Robere, ECCC TR26-055 (text)
- Li–Li–Ren, arXiv:2411.15515 (abstract)
