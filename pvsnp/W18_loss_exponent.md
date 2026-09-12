# W18: the loss exponent. How much can hardness-to-randomness lose per stage? Pre-registration

*Drafted 2026-09-12 on branch `w18-loss-exponent`, on the reviewer's W18 specification, after W17 closed at `f8e78a6` (outcome 17b, accepted). Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. A correction to W17 that I am carrying forward, not burying

W17 §7'.5 concluded that the scheme "fails for every `c > 1`" and "survives only at `c = 1` exactly". **The reviewer's sharpening is right and my phrasing understated the target.** With `k = Theta(log log N)` stages, the requirement `A >= c^k` with `A = O(1)` needs `k * log c = O(1)`, i.e.

> **`c <= 1 + O(1 / log log N)`** -- not `c = 1` exactly.

My statement is true for every **constant** `c > 1`, which is what I had in mind, but the live case is a tradeoff whose loss **improves with the size it is applied at**, `s |-> s^{1 - O(1/log log s)}`. That is the "extreme high-end" regime, and it is the whole of W18. I am recording this here rather than editing the accepted W17 findings, per the standing practice of not revising a ruled page retroactively.

**A declined proposal, also recorded.** I had nominated a different W18 (does a succinctly described base evade the `n_0 = O(log N)` cap?) and drafted a pre-registration for it. The reviewer declined it in one line -- a base evaluable by a small circuit has small circuit complexity by definition, so it cannot be the hard string -- which is the same argument I had disclosed in that draft's §2. The draft is discarded uncommitted. **It cost nothing and it is not evidence that my impossibility instinct has recovered: the argument was one line and I still priced it at only 62.**

## §1. Refuted premises checked

Not reused: the four W16 errors, the three W17 flag errors, and **Lemma W17.1 itself**. That is eight consecutive wrong predictions that something would fail.

**This round's shape is different, and I note it because it changes the bias.** W18 is mostly a **literature question** -- what loss do the known tradeoffs actually incur, and what is known about the extreme high-end -- not an impossibility argument of my own. The failure mode to guard here is not pessimism but **reasoning from my own summary of a source instead of its text**, which is the W5 error (the reconstructed superscript). Flag Y18 is that guard.

## §2. Disclosure: what I believe before reading, stated so it can be scored

**(a) On the exponent.** I expect the honest answer to question (i) to be that plain-hardness tradeoffs lose a **fixed polynomial** -- Umans' Lemma 3.6 as I already quoted it needs `Y` hard for size `s^g` to fool size `s` with `g > 1` a constant bounded away from 1 -- and that nothing in the NW/IW/Umans line gives `s^{1-o(1)}`. I do **not** know this; it is what I expect.

**(b) On why.** I expect the obstruction to be the hybrid argument's `m`-fold loss (`1/2 + eps/m` correlation) plus the additive junta term `m * 2^a`, both already quoted in W17 (6.4), which together seem to force a constant-factor gap in the exponent rather than a vanishing one. **This is a mechanism I am guessing at, not one I have checked.**

**(c) On Chen-Tell.** The reviewer's 18b names a specific expected content -- that the extreme high-end requires a hypothesis of a stronger type (nondeterministic circuits, or advice, or an equivalence with a lower bound the door already needs). **I have not read Chen-Tell and I am not going to pretend to remember its theorems.** If it says something else, that is the finding and it goes in the same sentence.

**(d) The angle I think is most likely to surprise, and it is the reviewer's (iv).** We do not need a generic PRG. `V^C` is one specific uniform family, and we need to fool one verifier per candidate `C`. **Instance-wise / targeted hardness-randomness** (which RW26 themselves reference) is exactly the regime where the generic loss can be beaten, and it is the reason I am not putting 18c lower than I am.

**(e) Not done:** no primary read for this round. Not yet consulted: Chen-Tell ITCS 2022; Umans 2003 beyond Lemma 3.6 as quoted in W17; SU05 §3's nondeterministic analogue beyond Thm 3.11/3.12 as used in W5/W6; Dermer-Shaltiel 2026's multiplicative-error variant; ECCC 2024-2026 on hardness vs randomness.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **18a** an extreme-high-end tradeoff is known unconditionally in a form usable against the `V^C` family -- the recursion closes and `E^NP` near-max is unconditional | 2 | **2** |
| **18b** best known losses are a fixed polynomial, and the extreme high-end is known to REQUIRE a stronger hypothesis type, placing (C_1)'s remaining gap on the same plain-vs-nondeterministic boundary as W15/W16 | 60 | **66** |
| **18c** other | 38 | **32** |

**Why I am ABOVE the reviewer on 18b and BELOW it on 18c, deliberately.** In W17 I sat at 38 on 17c against the reviewer's 27, on the strength of two named candidates, and **both were wrong; the reviewer's lower number was the better estimate.** The diagnosis was that I inflate the "something else" bucket. Repeating that here after naming it would be the eighth instance of a bias I have already written down, so I am correcting in the opposite direction and will be scored on it. **This is a deliberate calibration move, not a change of belief about the mathematics** -- my honest read of the content is close to the reviewer's, and §2(d) is the one thing keeping 18c as high as 32.

**Why 18a is 2 and not lower.** Same reasoning as 17a: it would be an unconditional breakthrough, so its probability is essentially the probability that the literature contains something the reviewer and I would both be astonished by.

## §4. Flags

- **Flag X18 -- the premise audit runs FIRST.** W17's practice line, now standing: "both sides computed" is necessary and not sufficient; the premises of any failure inequality get the adversarial pass before the arithmetic, **and the step that looks like bookkeeping gets it first**. In W17 I even flagged the wrong premise as load-bearing.
- **Flag Y18 -- every exponent carries its theorem number**, and no exponent is reported from my memory of a source. This is the W5 guard (never reconstruct inside a quotation) applied to numbers rather than glyphs.
- **Flag Z18 -- "open" is not written until ECCC 2024-2026 has been checked** on hardness vs randomness. W15 found TR25-191 this way and W16 found TR25-104; the habit has paid twice.
- **Flag S18 -- the stop-rule, inherited and binding.** If 18a appears to close, stop, send the exact parameters, and write nothing further until the reviewer has checked it.
- **Flag V18 -- no fitting to W17.** If the loss can be driven into the `1 + O(1/log log N)` window, that reopens 17a and it is said plainly, in the same sentence as the finding.

## §5. Kill tests

- **(i)** Primaries verbatim with numbers: Chen-Tell ITCS 2022; Umans 2003 Lemma 3.6 and its statement of the loss; SU05 §3; Dermer-Shaltiel 2026 if the multiplicative-error variant bears.
- **(ii)** The four questions answered separately and explicitly: (i) the exact best known `c` for plain hardness with its theorem; (ii) whether any construction achieves `s^{1-o(1)}` and under what hypothesis; (iii) whether extreme-high-end from plain hardness is proved impossible black-box or proved equivalent to something; (iv) whether an instance-wise or targeted generator beats the generic loss **for this specific uniform `V^C` family**.
- **(iii)** The `1 + O(1/log log N)` window of §0 used as the target throughout, never `c = 1`.
- **(iv)** ECCC swept before any claim of openness (Flag Z18).
- **(v)** Nothing from the closed barrier sub-line (W16.0-W16.2) cited as evidence.
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
