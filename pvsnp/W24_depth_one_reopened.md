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

## §5B. Pre-registration AMENDMENT 2 -- reformulation (A) authorised; the t-cover; separate priors -- committed BEFORE any (A) run

*Appended 2026-09-12. Revises none of §0-§5A and moves none of §3's priors.*

**(B5.1) The harness crash, recorded because it bears on integrity.** My first combined (A)/(B) harness **crashed on a Python `TypeError` before printing any result** (`dict(seen, **{u: vstar})` requires string keys). **No output of any kind was seen before this amendment**, so the pre-registration is intact.

**(B5.2) Reformulation (A) authorised -- the sentence the reviewer asked to be pre-registered, verbatim:**

> "(A) is the sub-line's NATIVE model (W8.1's statement), and W14's switch to `E(y) = empty` was a device to escape the fixpoint, not part of the question. Returning to (A) is not moving the goalposts; a theorem under (A) is a theorem about the depth-1 problem as W7/W8 posed it."

**Recorded here so that the reformulation cannot later be read as a weakening.** W8.1's own statement is Q-dependent ("such that **Q's output** satisfies `y′ ∈ range(C)`"); W14's `E(y) = ∅` was the stronger device.

**(B5.3) The reviewer's framing: under (A) the 2-cover is a DEFERRAL principle, not a selection principle.** Under (B) every hosting decision is made before `Q` runs, for every string at once, which is why (4) coupled back onto (3) and (2). Under (A) the invariance lets the adversary **defer (4) until `Q`'s output is known** -- "not a rule for choosing, but a licence to choose last".

**(B5.4) The one-sided caveat (the reviewer's), and its resolution.** W16.1's invariance is one-sided, verbatim: *"false answers cannot become true as S shrinks."* Hosting `v` puts it into `range(C)` and **can flip a false answer to true**. A `Q` that asks "is `v ∈ range(C)`?" before outputting `v` defeats a naive after-the-fact host. **Resolution: host mid-run**, answering TRUE to membership queries on hostable candidates and committing forced values as queries arrive.

**(B5.5) The t-cover.** Up to `q` mid-run hosts plus one at the end, each imposing `≤ 2k` forced constraints (W14 §2(d)), gives a free-side deletion budget of `≤ 2k(q+1)`. Required: a **t-cover** with **`t = 2k(q+1) + 1`**, marking rule *"a property with `≤ t` free non-Bad elements marks them all"*. **My pre-read, stated before any run: the fixpoint argument generalises mechanically** -- each property still marks at most once, so `|Bad| ≤ t·q = O(kq²)`; the fixpoint becomes "0 or `≥ t+1`", so `≤ t` deletions leave a witness. **Prior that it is mechanical: 85, matching the reviewer. The crux is not here.**

**(B5.6) MY AUDIT, POINT 1 -- a conflation in "hosting is an addition".** The 2-cover's ground set is the **free** inputs. Hosting at a **forced** input -- which is where W14 hosts (A5.1) -- **does not touch the free set at all**. Hosting at a **free** input commits it, which is a **DELETION** from the free set. **The false-to-true answer flip is real in both cases, but the 2-cover's invariance protects against the free-input case only.** Which kind of host the construction needs is unaudited.

**(B5.7) MY AUDIT, POINT 2 -- the deferral framing does not address choice (1), and W13's wall likely survives under (A).** Deferral handles (4); the t-cover handles (2). **Choice (1), the hint, is untouched.** Under (B) the constraint was a hint outside `∪_v Y_v`. **Under (A) it becomes the fixpoint `y ∉ Y_{v*(y)}`**, where `v*(y)` is `Q`'s output on hint `y`. Each `|Y_v| ≤ 2k` is small -- but **W13's own bound, verbatim, is `Σ_v |Y_v| ≤ 2k · 2^{n+1} = k · 2^{n+2}` against only `2^{n+2}` hints**, which does **not** prevent an adversarial `Q` from routing every hint `y` into its own `Y_{v*(y)}`. Such a `Q` is exactly a certifying reduction. **So W13's wall plausibly persists under (A), in fixpoint form.** Verified premise (the bound is W13's); unaudited consequence (whether `Q` can actually route that way) -- **priced at a few points only, per the W23 line.**

**(B5.8) The reviewer's expected crux, recorded.** Forced-neighbourhood disjointness -- W14 §2(c), verbatim, *"poly(n) only when δ ≥ 1/2"* -- between the `≤ q+1` hosts and against the hint's validity constraint. Its expected landing: a **partial** theorem, *"Theorem W24.1 (conditional on t-cover, δ ≥ 1/2)"*. **B5.7 adds a second, independent candidate crux: choice (1).**

**(B5.9) SEPARATE PRIORS on the (A)-reformulated codes -- a different proposition, so its own priors, as in W20.**

| code | outcome under (A) | reviewer | **mine** |
|---|---|---|---|
| **24a(A)** Theorem W24.1: a deterministic depth-1 black-box lower bound under (A) via t-cover deferral, possibly conditional on δ ≥ 1/2 | 20 | **16** |
| **24b(A)** the t-cover deferral works but a named step fails -- disjointness, the one-sided flip, or hint selection | 55 | **59** |
| **24c(A)** other | 25 | **25** |

**Why 24a(A) is 16, four below.** Up: t-cover mechanical (B5.5), deferral genuinely handles (4) (B5.3), and W14 itself called δ ≥ 1/2 "harmless for the target". Down: **B5.7 -- choice (1) is unaddressed and W13's counting bound transfers to the fixpoint form.** That down force is a verified premise with an unaudited consequence, so it is worth a few points and no more. **24c(A) matches at 25: no audited mechanism.**

**(B5.10) Run order and kill test, fixed now.** **(A) first; (B)'s tail-mass only if time remains.** At `n = 3`: a deterministic `Q` that **queries membership "is `v ∈ range(C)`?" of its own candidate before outputting `v`**. **Positive control:** a t-cover free set under which the adversary hosts mid-run and **all `q` answers stay consistent**. **Negative control:** `t = 2` (single-deletion), where **the second mid-run host must break an answer**. *Modality: membership queries are NP-type and closer to Definition 9 than W14's value queries, but this is still a single-query-form simulation at `n = 3`, not the full DNF model; labelled as such.*

## §5C. Pre-registration AMENDMENT 3 -- the construction order, U(y), and a dependency cycle -- committed BEFORE any run

*Appended 2026-09-12. Revises nothing above, moves no prior. The (A)-branch harness `w24_deferral.py` has been WRITTEN but NOT RUN; no result of any kind has been seen.*

**(C5.1) The construction order, as the reviewer set it -- "the deferral framing made exact".** (1) choose the hint `y` → (2) compute the dangerous set `D(y)`, `|D| ≤ k` → (3)/(4) host `D(y)` **forced-side, up front, before `Q` runs** -- "so they can flip no answer: there are no answers yet" → (5) build the **t-cover on the REMAINING free set** → (6) `Q` runs → (7) **free-side** hosts of `Q`'s candidates, mid-run. **This resolves my audit point 1 (B5.6)**: forced-side hosts (for `D`) and free-side hosts (for `Q`'s output) happen at different times, and the t-cover guards exactly the free-side ones because `D` is finalised first. Accepted.

**(C5.2) `U(y)` IS W14's `E(y)` -- verified by definition, not assumed.** The reviewer defines `U(y)` as strings for which "every `C` that puts `v` in range also puts `y` in range, so hosting `v` breaks the hint's validity". That is: no `C` with `v ∈ range(C)` is admissible for `y`. **W14 §2, verbatim:** *"`E(y) = {v : no admissible C has v ∈ range(C)}`, where admissible means no x produces y."* **Identical.**

**(C5.3) So half the reviewer's census is ALREADY in W14's record -- and it is the optimistic half.** W14 computed `E(y)` **exhaustively at `n = 3`** and found it **empty on every valid hint** for successor, hub, double projection and random glue; only the positive control `C′(x) = (C(x), 0)` was nonempty (16 of 32 hints). **But W14's computation left every input free** (a single pin per test). That is the **most permissive** case. **The construction pins forced values** -- to host `D(y)` and keep `y` valid -- so the **operative** `U(y)` under the construction can only be **larger**. **All-free `E(y) = ∅` is necessary for choice (1) to close, not sufficient.** The decisive census is under a **sparse** free set, and that is what will be run.

**(C5.4) A DEPENDENCY CYCLE in the construction order -- my audit, verified from C5.1 itself.** The reviewer's escape for choice (1) is to make `Q`'s view t-invariant, hence "a function of the commitments only", and **then choose `y` after seeing which strings that function can reach**. But C5.1 makes the forced values **depend on `y`** (they host `D(y)`), and `Q`'s view depends on the forced values. So:

> **`y → D(y) → forced values → t-cover → Q's view → choose y`.**

**The escape needs `y` chosen last; the order needs `y` chosen first.** Breaking the cycle requires forced values that are **`y`-independent** -- i.e. hosting every string dangerous for **every** candidate hint up front, which **reintroduces the all-`y` quantifier** that made (B) exponential. **This cycle is W13's wall** -- "the adversary cannot use hint-averaging because `U(y)` and `Q`'s view of `y` are correlated" -- **made visible as an ordering constraint.** Verified structurally; whether it actually blocks is the round's question.

**(C5.5) A forced-side cascade the order assumes away.** C5.1 treats `D(y)` as "fixed" before the cover is built. But hosting `D(y)` forced-side **changes forced values**, which can make other strings blocked at every free input -- **enlarging `D(y)`**. That is the forced-side twin of W16.1's Bad-closure cascade. Unaudited; the census will record it.

**(C5.6) The reviewer's new residue, recorded: mid-run-dangerous strings.** A string whose allowed free inputs all lie in `Bad` or in already-committed inputs is unhostable mid-run. Its count is `#{v : |A(v,y)| ≤ |Bad| + 2k(q+1)}` -- **a polynomial threshold, not a cascade**, which the reviewer rightly calls a better question: under W13's mass bound, is it polynomial for a typical hint?

**(C5.7) The information question, with my prior.** Reviewer's question: *does t-invariance make `v*(y)` a function of (forced values, cover) that is independent of `U(y)`'s identity?* **Reviewer's prior: 35. Mine: 25.** Down ten because C5.4's cycle means forced values -- and so `Q`'s view -- depend on `y` through `D(y)`. **That cycle is a verified structural consequence of the stated order**, which is why it moves ten points rather than the three or four an unaudited consequence would earn; what remains unaudited is whether the dependence is strong enough to matter.

**(C5.8) Run order, revised and fixed now.**
1. **Sparse-free-set census** (cheapest; can void point 2): for each valid hint, all-free `E(y)` versus, under a half-free set, the dangerous set `D_F(y)` and the unhostable set `U_F(y)`; the forced-side cascade (C5.5); and the mid-run-dangerous tail (C5.6).
2. **The (A) kill test** (`w24_deferral.py`, robust vs naive).
3. **Routing data per hint** -- whether `Q`'s output lands in the operative `U(y)`.

**Priors on (A) unchanged** from B5.9 (mine 16/59/25; reviewer now 15/60/25).

## §5D. Pre-registration AMENDMENT 4 -- lazy hosting, the single crux, and the commitment-count census -- committed BEFORE that census runs

*Appended 2026-09-12. Revises nothing above, moves no prior. **Unlike §5A-§5C, two results are ALREADY SEEN and are disclosed here so this amendment is honest about what it knows.***

**(D5.1) Results already seen -- both from runs pre-registered at §5B.10 and §5C.8, and run only after those amendments committed.**

*The (A) kill test* (`w24_deferral.py`, single-query-form membership model, `n = 3`, **not** full Definition 9 DNF):

| template | robust: certified / survives | naive: certified / survives |
|---|---|---|
| CONTROL(C,0) | 4 / 28 | 4 / 28 |
| succ | 0 / 32 | 0 / 32 |
| **hub** | **0 / 32** | **3 / 29** |
| rand | 0 / 32 | 0 / 32 |

**Hub is where host placement matters**: naive placement lets `Q` certify on 3 hints; robust (lookahead-3 damage-minimising) placement holds it to 0 -- the reviewer's predicted positive/negative control split. **Correction to my own earlier report**: I had told the reviewer "my negative control failed to be negative" because hub was inert in the *static* census. That was premature; hub is exactly the discriminating template in the *dynamic* game. Withdrawn. *Weight: a 3-hint gap on one template at `n = 3`, and "robust" is not a literal t-cover.*

*The sparse census at `|F| = 2`* (labelled "the `δ ≥ 1/2` regime" when run -- **that label is WRONG and corrected here before commit: with `|F| = 2` every string has `|A| ≤ 2`, "0 or ≥ 2" collapses to "both or neither", and a t-cover with `t ≥ 2` is impossible; at `n = 3`, `√N ≈ 2.8 < t + 2`, so `δ ≥ 1/2` is degenerate for the cover. The reviewer caught it. The `D_F`/`U_F` measurements stand; the regime label does not.*): rand acquires a **dangerous string on one hint** (`D_F ≠ ∅`), and the near-dangerous tail rises sharply (`T(1)` = 0.75, 0.97, 1.81 for succ, hub, rand) -- **so the half-free census was optimistic, as C5.3 warned.** **But `U_F` stays empty on every template.** *This is the up-front framing with a pre-chosen sparse set, which lazy hosting (below) does not use, so it does not bear on the `δ ≥ 1/2` subsumption prediction.*

**(D5.2) The reviewer retracts up-front hosting in favour of LAZY hosting.** Under (A) the adversary never hosts `D(y)` before `Q` runs. It maintains one invariant -- *"every string Q could name is hostable in some completion that respects validity and every answer given so far"* -- and hosts **on demand**. Order: `y` → **validity** (the one universal, `y`-dependent commitment: no `x` produces `y`) → `Q` runs, each query answered by the minimal commitment keeping the invariant → output hosted. **The reviewer also records "choose `y` last" as incoherent -- `Q` reads `y` as its input, so `y` is first by definition -- and counts it as its third miss this round.**

**(D5.3) Consequences, recorded.** C5.4's dependency cycle is an artefact of up-front hosting and **dissolves under lazy hosting**: nothing `y`-dependent is committed beyond validity, which is the same for every strategy. C5.5's forced-side cascade is **void**: `D(y)` is never hosted up front. **`w24_deferral.py` already implements lazy hosting** -- it answers TRUE and commits only when `Q` queries a hostable candidate -- so D5.1's kill test is a lazy-hosting result.

**(D5.4) THE SINGLE CRUX -- the reviewer's reduction.** The adversary answers TRUE whenever the queried set contains a hostable string (a *local* commitment); FALSE only when it is entirely unhostable (a *universal* commitment). If `U(y)` is empty, the only FALSE `Q` can extract is "is `y ∈ range(C′)`", which it already knows. **So choice (1) under lazy hosting reduces to: CAN `q` LOCAL COMMITMENTS MAKE `U(y)` NONEMPTY?** -- the tail-mass question at a polynomial threshold, the same residue as C5.6's mid-run-dangerous count. **Two cruxes become one, by reduction rather than by coincidence of hypotheses.**

**(D5.5) The reviewer's three pre-registration points, with my audit.**

- **(i) Is hostability decidable by the adversary's bookkeeping in poly time per query? -- MY AUDIT: THIS IS NOT A SCARCE RESOURCE.** A black-box query lower bound (Wilson Theorem 12; W8.1) uses an **unbounded** adversary. It is a proof device exhibiting a hard instance, not an algorithm that must run. Its bookkeeping need not be efficient. The question would matter only for a *constructive* adversary, which the theorem does not require.
- **(ii) Is a TRUE answer's minimal commitment always one input? -- ONE for membership queries** (as in the harness). **For Definition 9 DNF queries, W16.1 §11.2 verbatim: "A width-w DNF term can name up to w/n preimages of P at once"** -- so **≤ w/n inputs** per TRUE answer, and the t-cover budget becomes **≤ (w/n)(q+1)**.
- **(iii) The invariant's failure mode is `|U(y)| > 0` after some query**, and the tail mass is its price. Agreed.

**(D5.6) The reviewer's prediction on `δ ≥ 1/2`, recorded.** Under lazy hosting there are no forced hosts to be disjoint from `Q`'s footprint, only validity, so **`δ ≥ 1/2` should NOT appear**. *"If it does appear in the data, that is evidence lazy hosting is missing something."*

**(D5.7) The commitment-count census, pre-registered now.** Start all-free (`|U_0(y)| = |E(y)|`, W14's record); apply on-demand commitments in `Q`'s candidate order, each committing one input to one value; after each `t = 0..q`, measure **`U_t(y) = {v : no uncommitted input u admits C(u) = v given all commitments}`**. Robust and naive placement. **Report per template the maximum `|U_t|` over hints at each `t`, and whether `|U_t| > 0` ever occurs** (the invariant's failure). *Prediction (mine, before running): `|U_t| = 0` for all `t ≤ q` on succ and rand under both placements, and on hub under robust placement only -- because D5.1 already shows hub's naive failures.*

**Priors on (A) unchanged** (mine 16/59/25; reviewer 15/60/25). **Routing: reviewer 35, mine 25.**

## §5E. Pre-registration AMENDMENT 5 -- mask-share, a designed resisting template -- committed BEFORE it runs

*Appended 2026-09-12. Revises nothing above, moves no prior. No mask-share computation has been run.*

**(E5.1) Why `hub` failed to resist -- the reviewer's diagnosis, accepted.** Allowedness is a property of the **output map per input**: `v` is blocked at `x` iff `h(v, x) = y`. Input multiplicity cannot make many strings blocked at one input; only a **many-to-one** output map can, and sharing across inputs needs a **shared fibre**. That is the `(C,0)` control's mechanism, which is why it was the only nonzero row.

**(E5.2) The reviewer's design, mask-share.** Group `G ⊆ F` of all but two free inputs: `h(v, x) = v AND M` (mask with `z` zero bits, `2^z`-to-one shared fibre). The two remaining inputs `a, b`: `h(v, a) = v XOR e_a`, `h(v, b) = v XOR e_b`, with `e_a ≠ e_b` unit vectors inside the masked positions. The XOR, not identity, is what keeps the hint non-certifying while the cascade is present.

**(E5.3) MY AUDIT -- A TYPE ERROR in the design as stated.** `v` is a `C`-output (`n+1` bits); `h(v, x)` is compared against the hint `y`, a `C′`-output (`n+2` bits). The design then places **"y itself"** in the fibre and argues the hint is non-certifying because the XOR "keeps `y` allowed at `a` and `b`". **A hint is not a candidate output**, so that step is ill-typed. **Repair**: embed `h_x(v) = (…) << 1` into `n+2` bits and let **`v₀ := y >> 1`** play `y`'s role. The fibre structure then survives exactly: `{v : v AND M = v₀}` has `2^z` strings (when `v₀`'s low `z` bits are zero), `v₀ ⊕ e_a` and `v₀ ⊕ e_b` sit at `|A| = 1`, the rest at `|A| = 2`. **Non-certification must be re-derived with correct types, not inherited** -- and it does hold: non-fibre strings are allowed at every `G` input, and every fibre string is allowed at `a` or `b`.

**(E5.4) A property that makes this cheap and exact.** mask-share is a **single-call** template -- `C′(x) = h_x(C(x))` depends only on `C(x)`. So admissibility is **per-input independent**: a partial assignment is extendable iff every pinned value avoids `y`. **No backtracking is needed**, so `n = 5` (32 inputs) is exhaustive and fast.

**(E5.5) PREDICTIONS, registered before running.**

- **Positive control for the row**: on the attack hints, `E_all(y) = ∅` (non-certifying at all-free) and tail `T(2) = 2^z − 2` at `t = 0`. If `E_all` is nonempty, `y` is being blocked and the template is not resisting; if `T(2) = 0`, the mask is not shared.
- **Mask-share DEFEATS lazy hosting on its attack hints.** With `F` = all inputs and `G` = all but `{a, b}`: `Q` asks about `v₀ ⊕ e_a`, allowed only at `b`, so the adversary **must** commit `b`; then `v₀ ⊕ e_b`, now allowed only at `a`, so it **must** commit `a`; then `v₀`, blocked at every `G` input with `a, b` committed -- **unhostable, so `Q` certifies**. **Predicted `|U₂| = 2^z − 2`.** Placement cannot help: every host is forced.
- **BUT ONLY ON A `2^{−(z+1)}` FRACTION OF HINTS.** The attack needs `y`'s low bit zero and `v₀`'s `z` masked bits zero. On every other hint the fibre is empty and the adversary wins. **So mask-share is `(C,0)`-shaped -- it certifies on some hints -- not a total reduction, and the adversary escapes by hint choice.**
- **Consequence, predicted: choice (1) is LOAD-BEARING, not closed.** This runs *against* D5.4's hope that lazy hosting reduces choice (1) to a tail-mass question: a designed template makes `U` nonempty on the hints it targets, and only the freedom to pick a different hint saves the adversary.

**(E5.6) A rescue variant, testing the reviewer's unspecified forced side.** The design left forced inputs as "whatever". **`U` depends on them.** So a second variant adds one extra input `c` with `h_c(v) = (v XOR e_c) << 1`, `e_c` **outside** the mask: it blocks only `v₀ ⊕ e_c`, which is not in the fibre. **Predicted: `U` stays EMPTY** -- the fibre is hosted at `c`. **So whether mask-share resists is decided entirely by whether some non-`G` input has a map that does not block the fibre.** An identity map at `c` would **not** rescue: it blocks `v₀`, leaving `U = {v₀}`.

**(E5.7) Runs, fixed now.** `n = 3` (`z = 2`) as the harness check, then `n = 5` (`z = 2` and `z = 3`). For each: the certifying-hint fraction (predicted `2^{−(z+1)}`), `E_all` and `T(2)` on attack hints (the positive control), and `|U_t|` for `t = 0..3` under an **adversarial `Q`** querying `v₀ ⊕ e_a`, `v₀ ⊕ e_b`, `v₀` -- for both the tight and the rescue variant.

## §5F. Pre-registration AMENDMENT 6 -- the hub mechanism, and a three-way cover test -- committed BEFORE the cover rule runs

*Appended 2026-09-12. Revises nothing above, moves no prior.*

**(F5.1) The hub trace -- a diagnostic of the §5B.10 kill test, already seen, testing no new hypothesis.** Naive placement lets `Q` certify on hints **`[2, 4, 6]`**; robust on **none**. On `y = 2`, verbatim from the run:

```
NAIVE  step 0: Q asks "is 0 in range?"  hostable at: [0..7]  -> TRUE, host at u=0 [first hostable]
       step 1: Q asks "is 1 in range?"  hostable at: []      -> FALSE -> Q OUTPUTS 1 (certified)
ROBUST step 0: Q asks "is 0 in range?"  hostable at: [0..7]  -> TRUE, host at u=1 [scores {0: 2, 1..7: 3}]
       steps 1-3: 1, 2, 3 all hostable -> survived (budget exhausted)
```

**(F5.2) The mechanism.** Hub is `C′(x) = (C(x), C(0)₁)`: **every `x` reads `C(0)`'s low bit.** Committing `C(0) = 0` fixes that bit to 0. Hint `y = 2` encodes `(C(x) = 1, bit 0)`, so any `x` with `C(x) = 1` now produces `y`. **String 1 becomes unhostable at every input in one commitment.** Robust sees it (hosting at `u = 0` keeps only 2 of the next 3 candidates hostable) and hosts elsewhere.

**(F5.3) Practice line (the reviewer's), recorded: A STATIC CENSUS AND A DYNAMIC GAME TEST DIFFERENT THINGS.** A template inert in one can discriminate in the other. Hub is inert statically -- input multiplicity creates no shared blocking -- and live dynamically, because a **commitment** to the high-multiplicity input sets a bit every `x` reads.

**(F5.4) MY STRUCTURAL PREDICTION -- W16.1's invariant does not model a high-multiplicity commitment.** W16.1's arithmetic treats a commitment as a **deletion: it removes one element** from each property containing it. **The hub commitment took property(1) from 8 to 0 in a single step** -- it removed every element whose validity depends on the hub bit. So literal W16.1 misses this hazard for **two independent reasons**:

1. **Arithmetic** -- single-deletion counting gives `8 → 7`, not `8 → 0`.
2. **Threshold** -- W16.1 marks a property at **exactly one** free element, so a jump straight to **zero** is never caught, however the size is computed.

**(F5.5) The cover rule, as three variants designed to separate those two causes.** Properties: for each remaining candidate string `w`, `P(w)` = the free inputs where `w` is hostable. At each TRUE answer, choose a host `u` for `v`:

| variant | size after committing `u` | refuse `u` if some `P(w)` becomes | predicted on hub |
|---|---|---|---|
| **cover-literal** | `|P(w)| − [u ∈ P(w)]` (W16.1 single-deletion) | exactly 1 | **certifies on `[2, 4, 6]`** -- both causes miss |
| **cover-recompute=1** | recomputed after a tentative commitment | exactly 1 | **certifies on `[2, 4, 6]`** -- threshold still misses `8 → 0` |
| **cover-recompute≤1** | recomputed after a tentative commitment | 1 or 0 | **certifies on `[]`** -- catches the collapse |

**If the table holds, W16.1's single-deletion invariant is not the right invariant for high-multiplicity templates**, and what lookahead is doing is precisely recomputing true sizes with a threshold that includes zero. By the reviewer's own criterion -- *"if cover loses hints robust holds, the lemma is not the right invariant"* -- that would be the finding. **If instead cover-literal certifies on `[]`, my F5.4 analysis is wrong** and the lemma is the right invariant.

**(F5.6) Mask-share under all three placement rules, predicted.** On mask-share's attack hints **every host is forced** (E5.5), so **all three variants -- and naive and robust -- certify identically** there. Placement should matter only on hub-like templates, never on mask-share.

**(F5.7) A precision point on the reviewer's draft proposition, to be resolved with data.** Draft: *"a lazy-hosting adversary with cover placement defeats every tested depth-1 template, including the designed mask-share family, **iff** `U_t(y)` stays empty for `t ≤ q`."* If E5.5 holds, `U_t` goes **nonempty** on mask-share's attack hints while the adversary still **defeats** the template by choosing another hint. So a per-hint "iff" would be false, and the statement needs **"∃ a valid hint on which `U_t(y)` stays empty"**. Recorded, not asserted.

**Priors on (A) unchanged** (mine 16/59/25; reviewer now 18/57/25).

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*
