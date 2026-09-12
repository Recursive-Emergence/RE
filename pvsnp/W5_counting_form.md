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

---

# Findings (written after reading; priors above are unrevised)

*Sources read as text this run, all primary unless marked: Shaltiel–Umans CCC'05 (`su05.txt`); Aaronson–Aydınlıoğlu–Buhrman–Hitchcock–van Melkebeek, ECCC TR10-174 (`aghk11.txt`); its journal merger Aydınlıoğlu et al. (`gk.txt`); Korten 2021 (`korten.txt`); Ren–Williams TR26-118 (`rw26.txt`); Ghentiyala–Li–Stephens-Davidowitz TR25-210 (`gls25.txt`); Dermer–Shaltiel TR26-017 / CCC 2026 (fetched this run); Hirsch–Volkovich TR25-220 (fetched this run). The reviewer's W1–W4 were read for context; every statement they carry is re-quoted here from its own source.*

## 0. Outcome against priors

| | prior | outcome |
|---|---|---|
| **Q1** essentially as the reviewer recalled | 75 | **held**, with one parameter correction (§1) |
| **Q2** the trade is not known | 85 | **held, and strengthened** by a 2026 black-box barrier (§2) |
| **Q3** the additive upper-bound form does *not* bypass the detour | 50 | **held — but my stated reason was wrong in detail** (§3) |
| ≥1 quoted statement materially off | 35 | **triggered only mildly**: one special case misquoted, nothing material (§4) |

**Unanticipated finding (§4): (D1) is not "smaller than the door". It implies the door and is not known to follow from it.**

## 1. Q1 — what hardness is known to give approximate counting in P^NP

**Shaltiel–Umans, Theorem 3.6** (verbatim): *"If E^{NP‖} requires exponential size SV-nondeterministic circuits, then there is a deterministic relative-error approximator that runs in time polynomial in the length of its input and 1/ε, with non-adaptive access to an NP oracle."*

**Corollary 3.7** (verbatim): *"If E^{NP‖} requires exponential size SV-nondeterministic circuits, then for every #P function f … there is a deterministic procedure P running in poly(n, ε^{−1}) time with non-adaptive access to an NP-oracle for which (for all x): (1−ε)f(x) ≤ P(x) ≤ f(x); in other words, every problem in #P can be approximated in FP^{NP‖}."*

So, exactly: **class** E^{NP‖} (parallel/non-adaptive NP queries); **circuit model** SV-nondeterministic (single-valued nondeterministic); **size** exponential; **queries** non-adaptive; **error** one-sided relative. *(Quantifier, verified after the first draft of this section: SU05 **Definition 2.4** — "A language L is worst-case hard for exponential-size (deterministic, nondeterministic, co-nondeterministic, SV-nondeterministic, adaptive or nonadaptive SAT-oracle) circuits if there exists a constant ε > 0 for which every circuit of the prescribed type and size at most 2^{n^ε}, fails to compute L restricted to inputs of length n, **for all sufficiently large n**." And §2: "We also sometimes say 'C requires exponential-size circuits' of a given type to mean C is worst-case hard for exponential-size circuits of that type." So the hypothesis is **a.e., not i.o.**, and matches AABHvM Theorem 3's a.e. conclusion. Note also Definition 2.5 and the remark that "(1 − 2^{−n})-hard coincides with the definition of worst-case hard".)*

**Why the flavours are interchangeable — Theorem 3.2 (downward collapse), verbatim:** *"Let C be any complexity class that allows low-degree extension. If every language in C has nonadaptive SAT-oracle circuits of size s(n) then every language in C has SV-nondeterministic circuits of size s(n)^{O(1)}."* **Corollary 3.3** is its contrapositive "boosting": SV-nondeterministic hardness ⇒ nonadaptive SAT-oracle hardness.

**Neighbours, verified:** Theorem 3.11 (*"BPP^{NP‖} = P^{NP‖}"* under the same hypothesis) and **Theorem 3.15** (*"If E^NP requires exponential size SV-nondeterministic circuits, then S₂^p = P^NP"*) — note this one is **E^NP**, not E^{NP‖}.

**Newest (2026), checked as instructed:** Dermer–Shaltiel TR26-017 give an optimal *multiplicative* PRG for nondeterministic circuits under the same assumption, and record (l.174) that *"in both theorems, it is known that the assumption is necessary for the conclusion."* **It does not weaken the hypothesis for counting.**

## 2. Q2 — can SV-nondeterministic hardness be traded for plain-circuit hardness of E^NP?

**No, not known — and the gap is explicitly flagged in the literature.**

**The obstacle, verbatim (AGHK journal, l.45–55):** *"Klivans and van Melkebeek observed that the proof of Impagliazzo and Wigderson (1997) relativizes and thus extends to other complexity classes … one can add an NP oracle to all the machines and circuits involved … assuming hardness against circuits having access to an NP-oracle."* The line was later improved so that *"hardness against non-deterministic circuits (instead of NP-oracle circuits) is equivalent to PRGs that fool non-deterministic circuits"* — an improvement **within** the nondeterministic family, never down to plain circuits.

**Is there a trick that uses the NP oracle in the construction to remove it from the test?** Yes, and it is exactly Corollary 3.3's boosting — but it starts from SV-nondeterministic hardness, not from plain hardness. **No known trick starts from deterministic-circuit hardness.**

**And there is now a barrier against the obvious route. Dermer–Shaltiel, Informal Theorem 1.8** (verbatim): *"'Black box techniques' cannot give a version of Theorem 1.7 in which ϵ = 1, δ = s^{−ω(1)}, and all occurrences of 'nondeterministic circuits' are replaced by 'deterministic circuits'. Furthermore, this holds even if the seed length r is increased to r = Ω(s)."* They add (l.295–297): *"if one wants a multiplicative PRG for deterministic circuits of size s, with δ = s^{−ω(1)}, at the moment, we only know how to give such a result as a consequence of Theorem 1.7, and require the assumption that E is hard for exponential size nondeterministic circuits."* (Proof adapts Grinberg–Shaltiel–Viola; deferred to their full version — **so this is a black-box barrier, not an unconditional one**.)

**The field says the same thing about our exact question. Ren–Williams §5** (verbatim): *"By [Kor21], the assumption that E^NP requires exponential size circuits (not SVN circuits!) implies an FP^NP algorithm for AVOID; moreover, this is provably the minimum assumption. Puzzlingly, to the best of our knowledge, the weakest assumptions known to imply an FP^NP_tt algorithm for AVOID are still lower bounds against SVN circuits."* Their **Question 5.3**: *"What is the weakest circuit lower bound assumption that implies AVOID ∈ FP^NP_tt?"*

## 3. Q3 — the smallest counting statement that still yields the door

**The door, from its own source. Korten, Theorem 10** (verbatim): *"There is a P^NP algorithm for Empty if and only if E^NP contains a language of circuit complexity 2^{Ω(n)}."* *(Precision: the numbered Theorem 10 in Korten's body is the Σᵢ-generalisation — "There exists a language in E^{Σ^P_{i+1}} with Σ^P_i-circuit complexity 2^{Ω(n)} if and only if there is a Δ^P_{i+2} algorithm for Empty_{Σᵢ}" — and the door is its base case, quoted as "Theorem 10" in his introduction.)*

**The smallest verified sufficient counting statement is the constant-gap approximate *lower bound*. AABHvM, Theorem 3** (verbatim): *"Let C denote a Boolean circuit, and b an integer in binary. If for some positive constant δ there is a language in P^NP that contains all instances (C,b) where |C^{−1}(1)| ≥ b and does not contain any instances where |C^{−1}(1)| < δ·b, then there is a language in E^NP that requires circuits of size α2ⁿ/n for some positive constant α and all but finitely many input lengths n."* With Korten Theorem 10 this gives the door. **The gap δ is an arbitrary positive constant** — strikingly weak — and Theorem 1.3 plus the Corollary 1.4 table trade solver time against δ for weaker size conclusions.

**Why a constant gap suffices there** (their §3, l.120–131): the construction is a minority-vote descent that *"approximate[s] the number of circuits consistent with the sequence thus far extended with a zero, do[es] the same for the extension with a one, and select[s] the extension that gives the smaller estimate"*, needing only that **the candidate set shrink by a constant factor per step**.

**Does GLS's upper-bound protocol bypass the truth-table detour? No, at its stated accuracy.** **GLS Theorem 3.2** (verbatim): *"ε-GapRangeSize is in prAM ∩ prcoAM for any ε := ε(n) ≥ 1/poly(n)"*, where YES is |Im(C)| ≤ τ and NO is |Im(C)| ≥ τ + ε2ⁿ — **additive ε2ⁿ**.

**The arithmetic, done rather than read off (and it corrects my own pre-registered reason).** Descend on prefixes p, maintaining "S_p contains a non-image point". Let D_p be the deficit |S_p| − |Im(C) ∩ S_p|. At the root D ≥ 2ⁿ, and choosing the child with the larger deficit gives D ≥ 2^{n−k} at depth k, with |S_p| = 2^{n+1−k}. **So the deficit is always at least half the subcube** — my pre-registration said the descent must "resolve a deficit of 1", which is **wrong**; the true requirement is resolution below 2^{n−k}. The verdict is unchanged: the protocol's additive error stays ε2ⁿ while the needed resolution shrinks as 2^{n−k}, so descent survives only to depth k < log(1/ε), i.e. **O(log n) levels at ε = 1/poly**, leaving a subcube of size 2ⁿ/poly in which a deficit is known to exist but cannot be localised.
- **Re-encoding does not rescale the error.** GLS's additive term is ε·2^{(circuit's input length)}; restricting to a subcube leaves the domain at n unless one can restrict to the fibre, which is an NP-set rather than a subcube.
- **Making it rescale is exactly multiplicative accuracy on image sizes** — i.e. the Shaltiel–Umans regime of §1, whose hypothesis is the nondeterministic-circuit hardness of §2. **So Q3's candidate collapses back onto Q1/Q2's hypothesis rather than bypassing it.**

**Ceiling on this route, worth recording. GLS Theorem 1.1:** *"BPP^Avoid ⊆ AM ∩ coAM and prBPP^Avoid ⊆ prAM ∩ prcoAM"*; and Hirsch–Volkovich TR25-220 Corollary 2: *"(pr)BPP^Avoid ⊆ (pr)BPP^MCSP"*, via an MCSP oracle amplifying Avoid's success probability (their Theorem 1).

## 4. Two corrections to the hand-off

1. **A misquoted special case.** The hand-off gave Theorem 3.2's special case as *"E ⊆ P^{NP‖}/poly ⇒ E ⊆ NP/poly"*. The source reads **"E ⊆ P^{NP‖}/poly ⇒ E ⊆ NP/poly ∩ coNP/poly"**. Minor, but it is the difference between a one-sided and a two-sided collapse.
2. **A framing error that matters. (D1) is not "smaller than the door".** By AABHvM Theorem 3 plus Korten Theorem 10, **(D1) ⇒ (C₁)**. The converse is not known: recovering counting needs nondeterministic-circuit hardness (§1), while (C₁) is plain-circuit hardness and is *provably minimal for FP^NP Avoid* (Ren–Williams §5). **So (D1) is sufficient for the door and at least as strong as it — plausibly strictly stronger — not a weakening.** W4's own table already says "⇒ (C₁) a.e."; the prose calling the three statements "smaller than the door" overstates it. The accurate phrase is **"of a different kind, and sufficient"**.

## 5. Kill tests

- **Sizes and oracle model on every hypothesis:** done inline (E^{NP‖} vs E^NP; SV-nondeterministic vs nonadaptive SAT-oracle vs plain; exponential size; non-adaptive queries).
- **i.o. vs a.e.:** AABHvM Theorem 3 concludes **a.e.** ("all but finitely many input lengths"); SU05's hypothesis is likewise **a.e.** — Definition 2.4's "for all sufficiently large n", quoted in §1. *(This discharges the one item §1 first recorded as unverified; it was checked and closed in the same run rather than left open.)*
- **Relativization claimed only where stated:** DS26's Theorem 1.8 is a **black-box** impossibility (their word), not a relativization barrier, and its proof is deferred to their full version — recorded as such.
- **ECCC keyword page checked before writing "open"** (range avoidance, 20131): TR25-030, TR25-034, TR25-104, TR25-121, TR25-191, TR25-210, TR25-220, TR26-118 are the 2025–26 entries; the two bearing on Q3 (TR25-210, TR25-220) are read above.
- **Counting before priors:** applied, and it caught my own wrong reason in §3.
