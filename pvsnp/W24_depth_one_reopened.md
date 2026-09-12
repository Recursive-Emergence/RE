# W24: Korten's Problem 1 at depth 1, reopened with the 2-cover. Pre-registration

*Drafted 2026-09-12, on the reviewer's W24 specification, queued behind W23. Branch `w24-depth-one-reopened`. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.** *(Every primary here is one I wrote -- see §2(a).)*

## §0. Ceiling, and what changed since W14

**Ceiling.** Everything in the black-box sub-line (W7-W14) is **deterministic-only**: by Flag H7, guess-and-test sits in `FZPP^{NP^C}` at depth 0, so no black-box depth bound survives randomisation. **Even 24a would not survive it.** And Korten's Problem 1 in full is about *all* depths; this round is depth 1. **A positive result here is a deterministic depth-1 black-box theorem, not a resolution of Problem 1.**

**What changed.** W14 closed as 14c with the obstruction named as **"the absence of a selection principle"** across four interacting choices:

1. a **valid, non-certifying hint** `y`;
2. a **sparse free set** among inputs carrying `≤ 4k` rigid `x`'s, with `δ ≥ 1/2`;
3. **forced values chosen after the hint** -- the freedom W13 identified as unexploited;
4. **hosts** for the `≤ k` dangerous strings, each imposing `≤ 2k` constraints back on (3).

Two rounds later, **W16.1** produced a **deterministic** selection principle: the 2-cover, via a Bad-closure fixpoint, no randomness. The reviewer's proposal is that this is the missing tool.

## §1. The governing lines

Standing record: ten consecutive wrong impossibility claims; my constructions holding. Five lines now govern, and **two of them were earned in the last two rounds and bear directly here**:

1. **A calibration asymmetry is indexed to a SOURCE, not a subject matter** (W22). **Here it legitimately applies** -- unlike W22 and W23, this *is* my construction domain: I built W16.1 and W14. So the asymmetry pushes 24a up, and correctly.
2. **A verified premise does not license its consequence** (W23, one round old). §2(b) below is exactly a verified premise with an unaudited consequence, and **W23 showed four points was too many for that category.**
3. **The framing audit precedes the mechanism's pricing, and can be the finding** (W20/W21).
4. **Name the scarce resource at each choice** (W17/W20).
5. **Contamination corrupts what you quote, not only what you conclude** (W23 -- I mis-attributed a formula inside my own contamination disclosure).

## §2. Disclosure

**(a) CONTAMINATION, and it is the heaviest of any round.** **I authored every primary this round names**: W13 (hint-averaging cannot finish), W14 (the four choices, the dangerous-string residue), W16.0 and W16.1 (the 2-cover and its deterministic fixpoint) and W16.2. I also **re-read W14's closing note and W16.1's statement during W19's consolidation**. So there is no "cold" reading available at all. **Line 5 of §1 is the operative risk**: I will be tempted to *recall* W16.1's statement and W14's choices rather than re-derive them, and W23 just demonstrated what that costs. Kill test (i) requires re-derivation from the committed pages.

**(b) Two verified premises, with unaudited consequences -- deliberately UNDER-priced per §1 line 2.**

- **"0 or ≥ 2" permits 0, and 0 is the dangerous case.** W16.1's fixpoint delivers, per property, either **0** or **≥ 2** elements. W14's dangerous strings are those **blocked at all free inputs** -- the **0** case. So the 2-cover does not *eliminate* dangerous strings; it makes the **non-dangerous ones robust** (allowed at ≥ 2 free inputs, so no single forcing makes them dangerous). The reviewer's own gloss -- "no string is dangerous **by a margin of one**" -- says exactly this, correctly. **Whether robustness of the non-dangerous strings is what W14 actually needs, or whether it needed the dangerous ones gone, is unaudited.**
- **W16.1 needs `q = poly` properties; W14 quantifies over every string `v`.** W16.1's ground set may be exponential (`{0,1}^n`) -- that is fine -- but the **number of properties `q`** is the algorithm's query count, polynomial. W14's constraints are indexed by strings `v`, of which there are exponentially many. **Whether they reduce to poly-many properties is the scarce-resource question for applying the tool at all**, and it is unaudited.

**(c) The reviewer's guess, recorded as its prediction.** It expects W16.1's fixpoint to absorb **choices (2) and (4)**, both being "choose elements so no property has exactly one", with **(1)** remaining -- the hint selection W13 proved averaging cannot supply -- and **(3)** to be attacked with post-hint forced values.

**(d) Not done.** No W13, W14 or W16 page re-read for this round. No computation run. The controls the reviewer specified -- the **successor template** and **one random arbitrary-glue template at `n = 3`** -- not yet built.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **24a** the 2-cover applied to the free set closes depth 1 for arbitrary glue -- a theorem: no depth-1 black-box reduction increases stretch by one bit deterministically | 20 | **18** |
| **24b** the 2-cover handles hosting, but hint selection (choice 1) still needs the counting W13 showed averaging cannot supply, with the exact interaction named | 50 | **52** |
| **24c** other | 30 | **30** |

**Why 24a is 18, two below the reviewer.** Two forces, stated separately so they can be scored separately. **Up:** §1 line 1 -- this is genuinely my construction domain, the one place the asymmetry is correctly indexed, and the tool is mine and deterministic. **Down:** §2(b)'s two premises, and above all that **choice (1) is W13's proof-level wall** -- hint-averaging provably cannot finish -- and nothing about a poly-property device obviously reaches an exponential hint space. **The down force is a verified premise with an unaudited consequence, so per W23 it earns two points and no more.** Net 18.

**Why 24b is 52, two above.** The most likely shape is that the 2-cover genuinely absorbs some choices while hint selection survives. That is the reviewer's own 24b and I agree with its content; the two points are simply where 24a's go.

**Why 24c matches the reviewer at 30.** **I have no audited mechanism for it.** W17, W20 and W23 are the record of what happens when I sit above the reviewer in this bucket without one, and W23 showed that even a *partially* audited reason does not justify it. Matching is the calibrated move.

## §4. Flags

- **Flag A24 -- framing audit FIRST.** Before any choice is priced: does W16.1's statement actually apply to W14's objects? Specifically **§2(b)'s two premises**: the "0 permitted" point and the "`q = poly` vs every string `v`" point. Discharged in writing, including if the answer is "harmless, and here is why".
- **Flag B24 -- name the scarce resource at each of the four choices.** Is it counting, verification, search, or a property count?
- **Flag C24 -- premises before arithmetic, bookkeeping steps first.** Standing since W17.
- **Flag D24 -- STOP-RULE.** If 24a closes -- a genuine depth-1 theorem for arbitrary glue -- **stop, send the construction to the reviewer, write nothing further** until checked. It would be the black-box sub-line's fifth theorem and the first to reach arbitrary glue at depth 1; it gets a second pair of eyes before it gets prose.
- **Flag E24 -- re-derive, do not recall** (§1 line 5, §2(a)). W13, W14 and W16.1 are re-read from their committed pages, and every statement used is quoted from the page, not from memory of having written it.
- **Flag F24 -- controls before claims.** The successor template and one random arbitrary-glue template at `n = 3` are run, **and a positive control is run first** -- W14's practice line, earned when a suspiciously uniform sweep turned out to need one.
- **Flag G24 -- deterministic-only** (Flag H7 carried forward). Every claim is stated as deterministic, and no claim is phrased as surviving randomisation.
- **Flag H24 -- modality.** Nothing stronger than "the known choices need X" for any negative; W22's Flag D22 wording is the template.

## §5. Kill tests

- **(i)** W14's four choices and W16.1's statement **quoted from their committed pages** (Flag E24), not recalled.
- **(ii)** Flag A24 discharged in writing before any choice is attacked.
- **(iii)** For each of the four choices: absorbed by the 2-cover, not absorbed, or partially -- with the reason, and the scarce resource named (Flag B24).
- **(iv)** Choice (3), post-hint forced values, attacked explicitly, since it is W13's identified unexploited freedom.
- **(v)** Controls at `n = 3` -- successor, one random arbitrary-glue template -- **with a positive control run first** (Flag F24), and exact vs sampled labelled with the soundness direction.
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Nothing from the (S2) rounds (W21-W23) cited as evidence; different object.

## §5A. Pre-registration AMENDMENT -- the two premise audits, committed BEFORE any attack

*Appended 2026-09-12 after re-deriving W13, W14 and W16.1 from their committed pages and BEFORE any construction or computation. **It revises none of §0-§5 and moves no prior.** It records the answers to the framing audit (Flag A24) that the reviewer ruled must be pre-registered before attacking.*

**(A5.1) Premise (1) audited: the 2-cover structurally cannot absorb choice (4).** W16.1's fixpoint, verbatim: *"every property has 0 or ≥ 2 elements outside C ∪ E ∪ Bad"*, with *"a property with no free non-Bad element has S ∩ Π = ∅"*. W14's closing note, verbatim, gives the four choices with *"the fourth acts on the very variables the third sets"* -- **hosting is done by setting forced values**. The 2-cover selects **free** inputs. So it cannot host the dangerous strings (the 0 case). **The reviewer guessed it absorbs (2) and (4); it absorbs (2) only.** Reviewer accepted.

**(A5.2) Premise (2) re-scoped: the operative quantity is the cascade, not `q`.** W16.1, verbatim: *"Each property marks at most once -- afterwards it has no free element -- so |Bad| ≤ q."* The argument charges each marking to a property currently at **exactly one** free element. So the operative bound is **the number of properties that ever reach exactly-one during the closure**, not the raw `q`. I first told the reviewer the literal `q` was exponential and W16.1 failed; **that was too strong, and is corrected here.** Reviewer accepted.

**(A5.3) Audit (i) -- why does a dangerous string need a host? -- READING ADOPTED: (B).** W14 §2, verbatim: *"A template is a total reduction iff every valid hint excludes some string: `E(y) = {v : no admissible C has v ∈ range(C)}`, where admissible means no x produces y."* The `≤ k` count in §2(d) is *"at most ≈ k dangerous strings per hint"*, over **all** `v`. **So W14 is Q-INDEPENDENT**: a dangerous string breaks the hint's non-certifying property regardless of what any `Q` outputs. **As written, the quantifier over `v` is real.**

**(A5.4) But (A) is available as a REFORMULATION -- and this is recorded as a hypothesis, not a reading.** The sub-line's **native** model is Q-dependent: **W8.1**, verbatim, *"there are an assignment α and a valid hint `y ∉ range(C′)` such that **Q's output** satisfies `y′ ∈ range(C)`."* W14 moved to the stronger Q-independent condition. The plausible reason is a **fixpoint**: protecting `Q`'s output changes commitments, which changes `Q`'s answers, which changes its output; protecting every string sidesteps it at the price of the all-`v` quantifier. **Under (A), properties index by (candidate `v`, hint `y`), `q` is polynomial, and `|Bad|` is polynomial by marking-once alone.**

**(A5.5) Audit (ii) -- was W14's obstruction deletion-driven? -- NO.** The strings `delet` and `cascade` do **not occur** in W14's body. Its mechanisms, verbatim, are **rigidity** (Fact (3) repaired: *"at least 3N/4 of inputs carry ≤ 4k rigid x's"*), **neighbourhood disjointness** (Fact (2): *"poly(n) only when δ ≥ 1/2"*), the **mass bound** (§2(d)), and **forced-value coupling** (hosts *"each imposing ≤ 2k constraints back on (3)"*). **The deletion trick is W16's device and postdates W14.** By the reviewer's own kill test -- *"If W14's cascade was not deletion-driven, say so and the tool is idle"* -- **the reframing "the 2-cover makes the deletion trick close in one step" is IDLE for W14 as written.**

**(A5.6) A new mechanism, disclosed and NOT priced.** Audits (i) and (ii) point in opposite directions. Under (B) there is no deletion to close. **Under (A) there is a deletion-shaped fixpoint** -- and W16.1's defining consequence is verbatim *"Deleting any single x ∈ S changes no answer"*, which is exactly the property that stops a local commitment change from propagating into a changed output. **So the 2-cover may be the tool that makes (A) work.** Named, unaudited, and priced at zero per §1 line 2 and the W20/W21/W23 record. **Open sub-question it raises:** whether protecting one output needs only *single*-deletion invariance, or several simultaneous commitment changes, which W16.1 does not provide.

**(A5.7) What the attack will therefore run, fixed now.** **Both branches, positive control first on each** (Flag F24):
- **(B)-branch:** W16.1's Bad-closure over all-`v` properties at `n = 3`; the **tail mass** `Σ_v [|A(v,y)| ≤ j]` as a function of `j`, to see whether it is geometric (cascade polynomial) or flattenable (cascade exponential).
- **(A)-branch:** the fixpoint under Q-dependent indexing, with a **simulated deterministic `Q`**, checking whether single-deletion invariance suffices.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
