# W21: (S2), the NC^0_3-Avoid stretch window. Pre-registration

*Drafted 2026-09-12 on branch `w21-nc03-window`, on the reviewer's W21 specification, after W20 closed at `13cb4b7` and the program page was narrowed at `908c3e3`. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. Ceiling, first -- and this round's ceiling is different in kind

**(S2) is OFF the door.** Every round from W15 to W20 was about (C_1) or its neighbours. This one is not, and the page must not drift into door-talk because the habit of twenty rounds pulls that way.

**What (S2) actually buys**, as the reviewer states it: rigidity and linear-circuit lower bounds in Valiant's sense -- GGNS23 Thm 1, `FP^NP` for NC^0_3-Avoid at stretch `m = n + O(n^{2/3})` gives an explicit rigid matrix, hence a linear map with no `o(n log log n)`-size linear NC^1 circuit. **That is a real payoff and it is not (C_1).** Nothing proved here moves the door.

**Flag E21 exists to enforce that**: if a finding is stated in terms of (C_1), it is either wrong or off-target.

## §1. Refuted premises checked, and the two lines that now govern

Not reused: the four W16 errors, the three W17 errors, Lemma W17.1, the three W18 errors. **Ten consecutive wrong impossibility claims**, with positive contributions holding.

**Two practice lines earned in W20 govern this round specifically:**

1. **The framing audit precedes the mechanism's pricing.** A mechanism can die by losing its framing without ever being refuted. Twice I inflated the "other" bucket on a named mechanism (W17: 38 against 27; W20: 38 against 32) and both times the mechanism was invalidated by its framing collapsing rather than by being wrong.
2. **Name the scarce resource before ruling on a component.** The same component gave opposite verdicts in W17 and W20 depending on whether the scarce resource was fooling or enumeration.

**Both bear directly here.** A "window" between a hardness end and an algorithmic end is a *framing*, and it is only a gap if both ends are statements about the **same object** at the **same parameters**. In W20 the reviewer's route conflated the GGM range with the Reed-Muller encoding of the witness, and I nearly priced a gap between two different things. **Flag F21 is that audit, and it runs first.**

## §2. Disclosure

**(a) Contamination, declared.** Earlier this session, while verifying the "two doors are one" attribution, I read the reviewer's **W3 page**, which contains (S2)'s window and several of this round's citations -- including the bracket `(n + n^{2/3}, n^{1.4})`, GGNS23, KPI25 (TR25-030), HLZ26, RSW22, and Korten's survey. I did not read it *for* this round, but I have read it, and the window I am about to "pin" is one I have already seen asserted. **That is exactly the position in which a mapping round can confirm a number rather than check it**, and Flag C21 is the guard.

**(b) What I believe before reading, stated so it can be scored.** I expect the hardness end to be limited by the **rigidity target** rather than by the perfect-encoding step -- i.e. that `n^{2/3}` is where *Valiant's application* sits rather than where the AIK06 degree-2 to NC^0_3 encoding gives out. That is a guess about which of two constraints binds, and it is the reviewer's question (ii). I have no view yet on question (i).

**(c) What I do NOT have a mechanism for.** Nothing. Unlike W20 I am opening with no candidate idea of my own, and per §1 line 1 that is a reason to keep the "other" bucket **low**, not high: absence of a named, framing-audited mechanism is absence of evidence for 21c.

**(d) Not done -- no primary read for this round.** Not yet consulted: GGNS23 (Thms 1 and 2, §3 and the `n^{12/17-ε}` remark); KPI25 TR25-030 §5 and its barrier section; HLZ26 §1.1.3; RSW22 §5.2; Kuntewar-Sarma TR25-034; Huang-Li-Zhong ITCS 2026 on local algorithms; the ECCC 2025-2026 sweep.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **21a** an `FP^NP` algorithm for NC^0_3-Avoid at stretch strictly below `Õ(n^{1.4})`, **or** an extension of the hardness reduction to stretch strictly above `n + O(n^{2/3})` | 8 | **10** |
| **21b** both ends pinned to named quantities with the exact gap -- rigidity parameters `(r, s)` reachable as a function of stretch on one side, the verbatim 3-probe static cell-probe bound behind `Õ(n^{1.4})` on the other | 60 | **60** |
| **21c** other | 32 | **30** |

**Why 21a is 10, slightly above the reviewer's 8.** It is a **construction** question, and the standing asymmetry says my constructions are the reliable half of my output while my doubts are not -- so pricing it near the floor would be importing a doubt I have no grounds for. But only slightly above: this is an **active area with specialists**, not a model I built myself, and the W-line's own theorems were produced inside a black-box model of my own construction. Producing a new result in an area where Korten, Pitassi, Impagliazzo and others are actively working is a materially lower base rate than producing one in a setting I defined.

**Why 21b matches the reviewer exactly at 60.** I have no reason to differ, and inventing a difference to look independent would be noise. **This is the "do the work properly" outcome and the primaries exist**, so it should carry most of the mass.

**Why 21c is 30, below the reviewer's 32, and the reasoning is the point.** I have **no named mechanism** (§2(c)). By the W20 line, a mechanism is what earns mass in this bucket, and only after its framing is audited. What keeps 21c as high as 30 rather than lower is a base-rate consideration rather than an idea of mine: **this is an active area with 2025-2026 results** (KPI25, HLZ26, Kuntewar-Sarma, Huang-Li-Zhong), so there is a real chance the window as stated on the W3 page is **stale** -- which would be 21c by default and is the single most likely way this round surprises.

## §4. Flags

- **Flag F21 -- the framing audit, and it runs FIRST.** Before any "gap" is computed: are the two ends statements about the **same problem** at the **same parameters**? Same `Avoid` variant, same stretch convention (`m` as output length vs `m - n` as stretch), same circuit class (NC^0_3 vs 3-local vs degree-2), same algorithm class (`FP^NP` vs `FP` vs `FP^NP` list). **W20's near-miss was exactly this failure**, and a window is a subtraction that silently assumes commensurability.
- **Flag E21 -- (S2) is off the door.** Payoff is rigidity/Valiant. Any finding phrased in terms of (C_1) is off-target.
- **Flag C21 -- verbatim with numbers, against the contamination of §2(a).** The window `(n + n^{2/3}, Õ(n^{1.4}))` is a number I have already seen asserted on the reviewer's page. **It gets re-derived from the primaries, not confirmed from memory.** When a cited label will not resolve, search for what the statement *says*, not what it is *called* (the W19 method line).
- **Flag D21 -- stop-rule.** If 21a appears to close -- a genuine new algorithm or a genuine extension of the reduction -- **stop, send exact parameters, write nothing further** until the reviewer has checked it. A new result in an active area gets a second pair of eyes before it gets prose.
- **Flag G21 -- do not inflate 21c on an unaudited mechanism.** If one occurs to me mid-round, its framing is audited before it is allowed to move anything.

## §5. Kill tests

- **(i)** Both ends quoted verbatim with their theorem numbers: GGNS23 Thm 1 and Thm 2; KPI25's 3-probe cell-probe statement; HLZ26's `2^{n^{1-ε/2+o(1)}}`-time algorithm at `n^{1+ε}`.
- **(ii)** Flag F21 discharged explicitly and **in writing** before the gap is named -- with the answer stated even if it is "yes, commensurable".
- **(iii)** The reviewer's three questions answered separately: (i) is the algorithmic end limited by the **cell-probe bound itself** or by the **correspondence's loss**; (ii) is the hardness end limited by the **perfect-encoding step** (AIK06 degree-2 to NC^0_3) or by the **rigidity target**; (iii) what single statement would move either end by a polynomial factor.
- **(iv)** ECCC 2025-2026 swept before writing "open" or "best known".
- **(v)** Whether the known 3-probe bound is **tight** is answered, not assumed -- the reviewer flagged it and it is the difference between "the algorithm is at the barrier" and "the algorithm is at the current bound".
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Nothing from the door rounds (W15-W20) is cited as evidence here; different object, and Flag E21 forbids the drift.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
