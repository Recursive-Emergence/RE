# W17: can the residue supply its own randomness? (C₁)'s reconstruction gap. Pre-registration

*Drafted 2026-09-12 on branch `w17-residue-supplies-randomness`, on the reviewer's W17 specification, after the barrier sub-line closed with W16.0–W16.2. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading the primaries for this round.**

## Ceiling (first), and a stop-rule I am adopting verbatim

The idea under test would, if it worked, turn RW26's FP^{prMA} reconstruction into **FP^NP**, make the win-win algorithm single-valued FP^NP for Avoid, and hence by Korten's Theorem 10 give **E^NP ⊄ SIZE[2ⁿ/n] unconditionally**. **That is a major unconditional breakthrough that Ren–Williams did not claim**, which is overwhelming evidence that it fails. **W17's job is therefore to locate the failure point exactly, not to test whether one exists.**

**Stop-rule, adopted from the reviewer and binding on me:** *if at any point 17a appears to be closing, I stop, send the exact parameters, and write nothing further until it has been checked.* Extraordinary conclusions get a second pair of eyes before they get prose.

## §1. Refuted premises checked

Not reused: the four W16 errors — the syntax/black-box "obstruction", "the union bound cannot deliver claim (1)", "a twenty-year-old open question's relativized form should not fall out easily", and the 25 prior — **all of them predictions that a construction would fail**.

**Standing calibration, now a line principle:** *my doubts are unreliable; my constructions are not.* **This round is almost entirely doubt-shaped** — its object is to explain why something fails — **so the bias runs directly at it**, and the guard is that every failure claim must be an inequality with both sides computed, never an intuition.

## §2. Disclosure: what I derived before pricing

**(a) The scale ceiling, and it is worse than a lossy reduction.** A truth table of length T_i is a function on log T_i bits, so its circuit complexity is **at most ~T_i/log T_i** — f_i's hardness is capped by T_i. NW/IW requires hardness ≳ S^{Ω(1)} to fool size S. With the stage recursion T_{i+1} = T_i^C, the stage-(i+1) verifier has size poly(T_{i+1}) = **T_i^{O(C)} ≫ T_i**. **So the requirement exceeds the maximum possible hardness of the string in hand.** This is not a constant-factor loss to be tuned away; it is a ceiling.

**(b) The one-stage lag, and why closing it is circular.** What the reconstruction needs is hardness at scale n_{i+1}; the branch supplies hardness at scale n_i. A string hard at **all** scales is exactly the hypothesis (C₁) — so "fix the lag by assuming f is hard everywhere" assumes what the win-win exists to prove. **If 17b is the outcome, this circularity is the substance of it.**

**(c) Two alternative failure points, registered now because "the failure is exactly where predicted" often conceals an earlier one.**
- **The reconstruction is not a bare spot-check.** RW26 run a PCP **plus a low-degree self-corrector**. Derandomising over generator seeds must fool the self-corrector's query distribution as well as V^C, which is a distinct requirement and may bite before the scale ceiling does.
- **The i.o. structure.** RW26's lower bound is **infinitely often**, for E^{prMA}/1 with one advice bit. "The first stage at which f_{i+1} is easy" presupposes a cleaner quantifier than an i.o. case analysis supplies; the stage index may not be well defined uniformly in the input length.

**(d) Not done:** RW26 §1.2's actual recursion (r_{i+1} = r_i + O(log T_i)) and §5's own hardness-randomness question; CHR §1.3's win-win parameters; Li's simplification; IW97/NW94's size–hardness statements verbatim.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **17a** some stage growth or hardness notion closes the scale gap | 3 | **2** |
| **17b** the scale mismatch is exact and unavoidable as structured, with the failing inequality named, and the one-stage lag shown to be fixable only by (C₁) itself — i.e. circular | 70 | **60** |
| **17c** a different failure point | 27 | **38** |

**Why I am above the reviewer on 17c.** §2(c) gives two concrete candidates that bite *before* the scale ceiling — the self-corrector's query distribution, and the i.o. quantifier structure. **A pre-registered failure point that turns out to be the second failure rather than the first is still a wrong diagnosis**, and this line has seen exactly that pattern twice (W13's obstruction was at the proof level, not the template level; W16's was not the syntax conflict I named).

**Why 17a is 2 and not 0.** It would be an unconditional breakthrough, so its probability is essentially the probability that I am wrong about what RW26 would have noticed. Not zero; not more than a rounding error.

## §4. Flags

- **Flag P17 — every failure claim is an inequality with BOTH sides computed**, at named parameters from the primaries, never an intuition. This is the guard against §1's bias.
- **Flag Q17 — the PCP-of-proximity issue is handled as RW26 handle it, not waved at.** A candidate C encoding a string *close to* a valid history is the case the self-corrector exists for; any derandomisation claim must say what happens to it.
- **Flag R17 — the i.o./a.e. structure of the case analysis is checked against RW26's actual proof**, which is i.o. If "first easy stage" is not well defined there, that is a finding and possibly the finding.
- **Flag S17 — the stop-rule.** If 17a closes, stop and send parameters first.

## §5. Kill tests

- **(i)** Primaries verbatim with numbers: RW26 §1.2 and §5, CHR §1.3, Li, IW97/NW94.
- **(ii)** Every scale carried with its bound beside it — T_i, T_{i+1}, the verifier size, the hardness threshold n_i^α, the NW seed length.
- **(iii)** The self-corrector handled explicitly (Flag Q17).
- **(iv)** The i.o. structure checked (Flag R17).
- **(v)** Nothing from the closed barrier sub-line (W16.0–W16.2) is cited as evidence here — different model, does not transfer.
- **(vi)** If the failure point is not the pre-registered one, **say so in the same sentence as the finding** rather than fitting the result to §2(a).

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
