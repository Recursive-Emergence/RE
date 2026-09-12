# W5: the counting form of the door. Pre-registration (priors fixed before reading)

*Opened 2026-09-11 on branch `w5-counting-form`, on the author's go ("Do W5 as specified"), at the reviewer's hand-off of the W-line. **Documents only; LOCAL commit only, no push; `formal/` untouched.** g1 throughout: every statement below is my prior belief, not a claim, and nothing in the reviewer's hand-off message counts until read in the source.*

**This section is committed BEFORE reading W1–W4 or any source text.** That is the point of it.

## Ceiling (first)

This door reaches **E^NP / E^{prMA}-type circuit lower bounds** — Korten's (C₁) is `FP^NP for Avoid ⟺ E^NP ⊄ SIZE[2^{o(n)}]`. That is **further from P vs NP than the line the author closed**, not nearer. Nothing here bears on `NP ⊄ BPP`, which the closed line already identified as the untouched arrow.

## Priors, fixed now (before reading)

**Q1 — what hardness is known to give approximate counting in P^NP?**
- 75: the reviewer's reading of Shaltiel–Umans is essentially right — hardness against **SV-nondeterministic** circuits, exponential size, for **E^{NP‖}** (or E^NP), yielding relative-error approximate counting with **non-adaptive** NP queries.
- 25: at least one parameter in that reading is off. **The three I expect to be the risky ones: the class (E^{NP‖} vs E^NP), the circuit notion (SV-nondeterministic vs plain nondeterministic), and the i.o./a.e. quantifier.**

**Q2 — can SV-nondeterministic hardness be traded for plain-circuit hardness of E^NP, making (D1) follow from (C₁)?**
- **85: not known**, and the obstacle is the one the reviewer names — Stockmeyer-style approximate counting has a **BPP^NP** test, so the distinguisher carries NP gates, and the Klivans–van Melkebeek relativization of IW97 therefore needs hardness against NP-oracle circuits.
- 10: a known partial trick exists (using the NP oracle in the *construction* to weaken what the *test* needs) that I will find on reading.
- 5: it is actually known and my prior is simply wrong.

**Q3 — what is the smallest counting statement that still yields the door?**
- 35: the **upper-bound form** (Ghentiyala–Li–Stephens-Davidowitz, additive ε2ⁿ upper bound on |Im(C)|) in a P^NP version **suffices directly for FP^NP Avoid**, bypassing the truth-table detour — which would make it the smallest statement on the line.
- 50: it does **not** suffice at that accuracy. **My reason, recorded now:** finding a non-image point by prefix descent needs the count to resolve a deficit of 1 among strings sharing a prefix; an additive ε2ⁿ bound has slack far larger than that at deep prefixes, and the n→n+1 stretch leaves global slack 2ⁿ but no local slack.
- 15: something else on the candidate list (AGHK11 Thm 1.2's constant gap, or the "into NP" form) turns out smaller.

**A separate checkable prediction, because the record says it is worth making:**
- **35: at least one of the statements the reviewer quoted from memory is materially off** (wrong class, wrong circuit model, wrong quantifier, or wrong theorem number). The program's history is that unverified readings fail at about this rate, and two of my own serious misses came from exactly that.

## Kill tests, fixed now

- **Sizes and oracle model on every hypothesis**; **i.o. vs a.e. on every conclusion**; **relativization claimed only where the source states it** (Y8's practice line: "non-black-box" and "non-relativizing" are different properties).
- **Before writing "open"**: check the ECCC range-avoidance keyword page and 2025–2026 reports.
- **Counting before priors** (Y9's practice line): any inequality about a specific construction gets the arithmetic done, not read off.

*Findings follow below, appended after reading. Nothing above is revised retroactively.*
