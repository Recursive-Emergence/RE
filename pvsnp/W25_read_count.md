# W25: the read-multiplicity count. Pre-registration

*Drafted 2026-09-12 on branch `w25-read-count`, on the reviewer's W25 specification, queued behind W24. Documents and scratch computation only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round -- including W7 and W8.**

## §0. The target, and the ceiling

**The candidate (the reviewer's).** Lemma W24.1 counted one-input templates: a string serves at most one hint, so certifying hints `≤ 2^{n+1}`. The proposed generalisation to multi-read glue: `v` is blocked at `x` for hint `y` only if some **reader** `x′` of `x` has its glue forced to `y` on the slice `C(x) = v`; so the hints `v` can serve **via `x`** number at most `readers(x)`, hence certifying hints `≤ r · 2^{n′+1}` against `2^{n′+s}` hints at stretch `s`.

> **Lemma W25.1 (candidate).** In the membership-query model, a depth-1 template whose glue has fan-in `r` cannot be total at stretch `s > 1 + log r`.

**If it held, the count would replace `δ ≥ 1/2`** -- a density-free depth-1 statement.

**Ceiling.** Membership-query model only, deterministic-only (Flag H7), depth 1. **Not Korten's Problem 1**, and not the Definition 9 DNF model.

## §1. Governing lines

Standing: ten wrong impossibility claims; my positive constructions holding. **Two lines from W24 bind directly here**:

1. **A lower bound is a statement about `U`, not about one `Q`'s path** (the reviewer's, W24). A count of served hints is the right object; a trajectory is not.
2. **Track the side effects of your own commitments** (mine, W24). W25's count is static, over completions, so this bites less than in W24 -- but any adversary-dependent reading of "served" reintroduces it.

And the older ones: framing audit before pricing any mechanism, and it can *be* the finding (W20/W21); a verified premise does not license its consequence (W23); calibration asymmetry is indexed to source (W22); suspect a version split before an error (W19/W21).

## §2. Disclosure

**(a) CONTAMINATION, partial and specific.** W24's commitment-count census already showed me **served-hint counts on hub (12 robust, 15 naive) and two-hub (11 robust, 14 naive)** under lazy hosting. **That is not the same measurement** as W25's -- W24 counted hints where a string becomes served along a `Q`'s commitment trajectory; W25 counts, statically, hints served under every completion -- but it is the same templates and a closely related quantity. **So my priors on hub and two-hub are not cold.** **The split-reader template is clean**: never built, never run. I deliberately did *not* run the exhaustive-versus-constant-reader count inside W24 for exactly this reason, and I record that the protection is partial rather than complete.

**(b) AN UNREAD PREMISE THAT DECIDES WELL-POSEDNESS.** The reviewer's tightness argument: the `m`-copy padding `C′(x, i) = (C(x), i)` has fan-in 1, serves every hint at `s = 1 = 1 + log 1`, and **is** a total reduction -- so the bound is tight at its boundary, and Korten's Problem 1 survives padding because "padding buys inputs, not output bits". **That argument rests on how stretch `s` and `n′` enter Problem 1, which I have not read in W7 or W8.** If the line's stretch bookkeeping differs, the bound could be trivial, vacuous, or ill-posed. **I told the reviewer I would price this in rather than assume it**, and it is priced in §3.

**(c) A FRAMING AMBIGUITY IN THE SPECIFICATION.** The W25 target reads *"a **single-call** depth-1 template whose glue has fan-in `r`"*. But the count is defined through **readers** `x′` of `x` -- which is **multi-read** glue, the case W24 established is structurally different from single-call. **Which class the lemma quantifies over has to be fixed before any data**, because single-call is W24.1's already-settled case.

**(d) AN OVERLAP IN THE OUTCOME CODES, disambiguated now, before data.** As specified: **25a** "the lemma holds with *some* count"; **25b** "the crux exhibited by split-reader *and the count reshaped*". These overlap: if split-reader breaks the constant-reader count but Q3's **distinct-values** count survives **unconditionally**, that is arguably both. **Proposed disambiguation, registered now:**
- **25a** -- *some* unconditional count holds (constant-reader **or** distinct-values or other), giving a density-free statement at stretch `> 1 + log r`.
- **25b** -- the crux is exhibited **and no count survives unconditionally**; the count reshapes into a conditional statement.
- **25c** -- neither.

**If the reviewer rejects this disambiguation, the original codes stand and I will score against both.**

**(e) What I expect on the crux, stated so it can be scored.** Split-reader is **designed** to exhibit the gap: two readers of `x` each output `y` on complementary halves of the completions, so `x` is blocked for `v` while **no single reader is constant** on the slice. **So I expect exhaustive > constant-reader there**, which refutes the constant-reader count as stated. **The live question is then Q3.** And I already see a subtlety in Q3 that I have not resolved: in split-reader **neither reader is constant on the slice**, so a "distinct *constant* values" count is **zero**, not one; the reviewer's "distinct values = 1" must mean values the readers **can produce**, and **that set can be as large as the output space**. So a distinct-values rescue is not obviously small. Registered as a concern, not a claim.

**(f) Not done.** No primary read: not W7, not W8. No template built. No computation run.

## §3. Priors, fixed now

| code (disambiguated, §2(d)) | reviewer | **mine** |
|---|---|---|
| **25a** some unconditional count holds -- density-free depth-1 statement at stretch `> 1 + log r` | 20 | **17** |
| **25b** crux exhibited and no count survives unconditionally | 55 | **58** |
| **25c** neither | 25 | **25** |

**Why 25a is 17, three below.** **Up:** this is a derived count I would verify myself -- the standing asymmetry legitimately applies, since it is indexed to my own output (W22). **Down, two separate forces, stated separately:** (i) **§2(b)** -- the stretch bookkeeping is unread, and it decides whether 25a is well-posed at all; an unread premise that can make the statement vacuous is a real down-force. (ii) **§2(e)** -- split-reader is built to break the constant-reader count, which leaves 25a riding on the distinct-values rescue, and I have already noticed that rescue may not be small. **Both are unaudited, so per the W23 line they earn a few points, not more.**

**Why 25b is 58, three above.** The designed kill test should exhibit the crux (§2(e)), and 25b is where the round lands if the rescue fails.

**Why 25c matches at 25.** No audited mechanism for it.

## §4. Flags

- **Flag A25 -- framing audit FIRST, on three counts.** (i) §2(b): how `s` and `n′` enter Korten's Problem 1 in W7/W8, and whether `m`-copy padding is excluded by the stretch requirement. (ii) §2(c): single-call or multi-read? (iii) §2(d): the code disambiguation. **All three discharged in writing before any template is counted.**
- **Flag B25 -- exhaustive means EVERY admissible completion.** "`v` served at `x` for `y`" = every admissible completion with `C(x) = v` puts `y` in `range(C′)`. **Constant-reader** = some single reader of `x` is constantly `y` on the slice. The round is the gap between them.
- **Flag C25 -- split-reader is the kill test, and it runs WITH a positive control.** A control where exhaustive and constant-reader must agree (a single reader constantly `y`), run **first** -- the W14 practice line.
- **Flag D25 -- stop-rule.** If 25a closes -- an unconditional density-free count -- **stop and send the count and its proof sketch to the reviewer before writing.**
- **Flag E25 -- contamination is partial (§2(a)).** Results on hub and two-hub are reported as *not cold*; only split-reader is.
- **Flag F25 -- re-derive, never recall.** W7/W8 read from the committed pages; W24 statements quoted from `W24_depth_one_reopened.md`.
- **Flag G25 -- modality.** Nothing stronger than "the known counts need X" for any negative.

## §5. Kill tests

- **(i)** Flag A25's three audits discharged in writing first.
- **(ii)** Positive control run before split-reader (Flag C25).
- **(iii)** Exhaustive versus constant-reader served-hint counts at `n = 3` on hub, two-hub and split-reader -- with hub and two-hub labelled not cold.
- **(iv)** Q3's distinct-values count computed on split-reader, with "distinct values" defined precisely (constant, or producible) **before** the number is seen -- §2(e) says the two definitions give very different sizes.
- **(v)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vi)** Flag H7 carried: deterministic-only.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

## §5A. Amendment -- the framing audits, discharged in writing before any template is counted

*Appended after the priors commit (4fc6f61) and after two reviewer messages that CROSSED it: the first sharpened the statement and said "read this before committing priors"; it arrived after the commit. **The §3 priors were set against the fan-in-`r` statement and are not revised.** Supplementary priors against the sharpened statement are registered below, labelled as set after the reviewer's argument but before any data.*

### A25(i) -- stretch bookkeeping: DISCHARGED, and the §0 statement is retired

From my own committed pages, not the reviewer's reading: W7 §1 (Korten Problem 1 verbatim; Lemma 6 keeps the input length, `Δ₂(n+1|n) = n+2`; the instance is depth 1 from `n ↦ n+1` to `n ↦ n+2`), and W8's model line: *"C′ : {0,1}ⁿ → {0,1}^{n+2} is a fixed template of C-gates ... depth 1"*. **So `n′ = n` in the instance.** The reviewer's `s > 1 + log r` parametrisation excludes only `r < 2` at `s = 1` -- W24.1 again -- and is **retired on the reviewer's own concession**. Padding `C′(x, i) = (C(x), i)` is `n+1 ↦ n+2`: the same additive stretch, excluded by input length, not by a stretch threshold. §2(b)'s down-force is discharged: the statement is well-posed.

**The sharpened statement (the reviewer's), which W25 now tests:**

> **Lemma W25.1 (candidate, sharpened).** Membership-query model, deterministic, depth 1, **any glue fan-in**, under the constant-reader characterisation of blocking: certifying hints `≤ 2^{n′+1}(1 + o(1))`; hence at `n′ = n` no template is total.

**The argument, re-derived by me, and it checks -- on a product domain.** If reader `x′` is constant on slices at two positions `i ≠ j` (constants `y_i(v)`, `y_j(v′)`), the point with `v` at `i` and `v′` at `j` forces `y_i(v) = y_j(v′)` for all such pairs: **a reader alive at ≥ 2 positions serves one hint in total** (covering ≤ `r` inputs); a reader alive at one position serves ≤ `2^{n+1}` (hint, input) pairs. With `r ≤ 2ⁿ`, pairs ≤ `2^{n′} · 2^{n+1}`, and a certifying hint needs `2ⁿ − q` of them. **The step that uses "product": the other positions range over ALL values independently.**

### A25(ii) -- "single-call": the reviewer's ruling is CORRECTED from the committed page

The reviewer ruled that in the line's vocabulary "single-call" means one call to the Avoid oracle. **W8 says otherwise**: *"Single-call template C′(x) = (C(x), h(x))"* -- **one C-gate per C′-input** -- contrasted in Flag L8 with *"k parallel calls with projection glue"*. So in the line's vocabulary:
- **single-call** = one C-gate per C′-input (W8.1's family);
- **one-input** = fan-in-1 glue (W12.2 / W24.1);
- **every template in the line is one Avoid instance `C′` with one hint** -- that is the depth-1 setting itself, not a template class.

**W25 is the MULTI-CALL (k-call, fan-in k) depth-1 case -- W13's "depth one general".** The two-axis sentence the reviewer asked for is above, with the axis names taken from W8 rather than from the ruling.

### A25(iii) -- codes: ACCEPTED as amended by the reviewer

25a = some unconditional count holds, giving **"at `n′ = n` no depth-1 template of any fan-in is total"** in the membership model; 25b = crux exhibited and no count survives unconditionally; 25c = neither. The original `1 + log r` wording is scored only as a footnote.

### PRIOR ART the round must not contradict silently -- W13 §2 and W14 kill test (v)

W13 §2: *"no averaging argument over hints alone can produce a free hint"*; W14 kill test (v): *"any argument that appears to finish by averaging alone is wrong, since W13 proved averaging cannot."* **The sharpened Lemma W25.1 is a count over hints. So either it has a hole, or W13's sentence is broader than what W13 proved.** What W13 proved is narrower: ITS bound (`|Y_v| ≤ 2k` with a **sparse** free set, each reader carrying ≤ 1 free position) is vacuous, `Σ_v |Y_v| ≤ k · 2^{n+2}` against `2^{n+2}` hints. **The sharpened count uses a different lever -- the full free set, where readers keep ≥ 2 free positions and the cross-position argument bites.** So there is no contradiction of what W13 *proved*; there is a contradiction of what W13 *wrote*. **Per the W23 line (a verified premise does not license its consequence), W13's general sentence is the suspect**, and if the sharpened count survives, W13/W14's sentence must be corrected in the findings, not quietly bypassed.

### The hole I expect, registered BEFORE data: admissibility is not a product

"Blocked at `x` for `y`" quantifies over **admissible** completions -- those with `y ∉ range(C′)` -- and that set is **not a product** of per-position domains. The cross-position argument needs the product. **So the constant-reader characterisation must say which domain it is constant over, and the two readings differ:**
- **constant-P** (unrestricted product): the reviewer's argument applies, the count holds, but blocking can occur with no constant-P reader;
- **constant-A** (admissible slice only): characterises more blocking, but the cross-position argument fails, because the admissible set depends on `y`.

**A second cold kill template, mine, built to separate them -- VALIDITY-SPLIT.** Reader A reads `x` and `z`: outputs `y` iff `C(x) = v` and `C(z)₁ = 0`. Reader B reads only `z`: outputs `y` iff `C(z)₁ = 1`. Then `y` is valid (take `C(z)₁ = 0`, `C(x) ≠ v`), `v` is blocked at `x`, **no reader of `x` is constant-P on the slice**, yet A **is** constant-A -- because B's validity constraint removed the other half. **This is split-reader with one half moved OUTSIDE `x`'s readers**, so even the reviewer's Q3 pattern definition (covering by `x`'s readers) needs its weights measured on admissible completions.

**Q3's weighted count, arithmetic done now rather than priced.** With a `y`-independent measure (uniform on the product), a reader's pattern mass at position `i`, value `v`, summed over `y`, is exactly 1; over `v` and `i`, `r · 2^{n+1}`. Summed over `2^{n′}` readers and divided by the `2ⁿ − q` units a certifying hint needs: **certifying ≤ `r · 2^{n′+1}(1+o(1))` -- vacuous at `n′ = n` for every `r ≥ 2`.** So the union-bound version of Q3 is dead by arithmetic; any surviving Q3 must use **admissible-measure** weights, which are `y`-dependent and break the per-reader budget. **That is why I do not expect Q3 to rescue the count.** Reported to the reviewer as arithmetic, not as a prediction.

### Definitions fixed for the computation (before any number)

At history `H` (q = 0 unless stated): **exhaustive-blocked** `(x, v, y)` iff no admissible `C` has `C(x) = v`. **constant-P** iff some reader of `x` has glue constantly `y` on `C(x) = v` over all values of its other positions. **constant-A** iff some reader of `x` equals `y` on every admissible completion with `C(x) = v`. A hint **certifies at slack q** iff it is valid and some `v` is exhaustive-blocked at ≥ `N − q` inputs. Reported per template: #valid hints; #certifying at q = 0, 1, 2; the counts of blocked triples under each of the three definitions; and every triple blocked exhaustively but not constant-P.

Templates, in order: **(1) positive control** -- a fan-in-1 reader per input, where all three definitions must coincide; **(2) hub, (3) two-hub** -- labelled NOT cold; **(4) split-reader, (5) validity-split** -- cold.

### Supplementary priors, against the sharpened statement (set after the reviewer's argument, before data)

| | reviewer | **mine** |
|---|---|---|
| count holds under constant-P (product domain) | 80 | **85** -- I re-derived it |
| the crux: blocking ⟺ constant-P, or a count that survives split-reader AND validity-split | 25 | **15** -- validity-split is built to break it, and the Q3 union bound is vacuous by the arithmetic above |
| **25a (amended)** / 25b / 25c | 20 / 55 / 25 | **13 / 62 / 25** |

**Prediction scored in advance:** exhaustive > constant-P on split-reader and on validity-split; constant-A = exhaustive on validity-split but constant-A < exhaustive on split-reader; all three equal on the positive control.

## §5B. Amendment -- set certification, and the q = 1 search, pre-registered before it runs

*Appended after the reviewer's rulings on the first-moment argument and before any q = 1 computation. Everything in this section that is a derivation was done by hand, with no data; it is labelled as derived, and each derivation has its own check below.*

### Accepted from the reviewer, re-derived

**All-yes collapse (the reviewer's correction of my (b)-(d)).** In the membership model a "no" to "is `u ∈ range(C)`?" is a win: Q outputs `u`. So the adversary answers yes throughout, the transcript is all-yes, and Q's queries plus its output form a set `V(y)` of size `q + 1` **determined by `y` alone**. The adversary's task is static: one `C` with `V(y) ⊆ range(C)` and `y ∉ range(C′)`. **My "history dependence" was an artefact of lazy hosting**, and (c) is withdrawn: W14's selection obstruction is dissolved in this model, not reached. This is membership-model specific: in the Definition 9 DNF model a "no" is not a win.

**Sharpened q = 0 constant (mine, from the reviewer's injective distribution).** Take `C` injective with a uniform `N`-subset as range. Then `Pr[v ∈ R] = 1/2` exactly, so certified hints `≤ 2N` **exactly**, for any glue and fan-in. The positive control reaches 8 = 2N at n = 2, **so the constant is tight.** Unavoidably invalid hints number `≤ N`, hence **at least `N` valid non-certifying hints** -- better than the uniform distribution's `0.46N`.

### THE REDUCTION, derived -- and it makes the reviewer's specified search degenerate

With glue of **fan-in `N`** (every C′-input may read all of `C`), the range of `C′` can be **any** set of `≤ N` hints, as a function of `C`. Totality at `q` depends on `C` only through `R = range(C)`, so a total template exists **iff** there is an assignment `y ↦ V(y)` (sets of size `≤ q+1`) with, for every `R` of size `≤ N`,

  `|I| + |{y valid : V(y) ⊆ R}| ≤ N`,  where `I` = hints in every `T(R)` (invalid).

**At q = 1 this is a graph problem: `4N` edges (multi-edges and loops allowed) on `2N` vertices, every `N`-set spanning `≤ N` of them.**

**At n = 2 (N = 4) it has a solution by hand: `K_{4,4}`.** 16 edges on 8 vertices; a 4-set split `(a, 4−a)` spans `a(4−a) ≤ 4` edges. So **a total q = 1 depth-1 template exists at n = 2 with fan-in-N glue**: `V(y)` = the `y`-th edge, and `range(C′) = {y : V(y) ⊆ range(C)}`, padded. **The reviewer's search (arbitrary fan-in, n = 2) would find this, and it would mean nothing:** fan-in `N = 2ⁿ` glue is an exponential-size `C′`, outside Korten's poly-time reduction, and outside every template class W7-W14 bounded (all poly fan-in). **The black-box question must keep fan-in `k = poly(n)`.**

**Derived sketch, NOT checked: at fan-in N, O(1) queries suffice for ALL N.** Take a random `s`-uniform hypergraph with `4N` edges on `2N` vertices. A fixed `N`-set contains `Bin(4N, ≈2^{−s})` edges; the tail bound `(e·μ/t)^t` at `t = N`, `μ = 4N·2^{−s}` gives `(e·2^{2−s})^N`; against `C(2N, N) ≤ 4^N` sets this closes at `s = 6` (`e/16 ≈ e^{−1.77}` < `e^{−1.39}`). **So with fan-in-N glue, 5 membership queries give a total depth-1 template.** If this holds, **the fan-in restriction is load-bearing for the whole black-box line**, not a technicality. I record it as a sketch because it is my impossibility-adjacent arithmetic, on a record of eleven errors of that kind.

### What runs, in order (nothing run yet)

- **(i) Verify `K_{4,4}` as an actual template** at n = 2 over all 4096 `C`, using the static set-certification check. *Prior: 95.*
- **(ii) n = 3, fan-in N, q = 1:** search graphs with 32 edges on 16 vertices, every 8-set spanning `≤ 8` (equivalently, bisection width `≥ 16` when no hint is invalid). A random bisection cuts 17.07 edges in expectation, so this is tight. Hill-climb = evidence only. *Prior that one exists: 20.*
- **(iii) Bounded fan-in, the real question, n = 2:** glue fan-in `k = 1` and `k = 2` (each C′-input picks `k` reads and a table), hill-climbing on the number of valid hints admitting a non-covered pair, exact totality check over 4096 `C`. **Evidence only, and at n = 2 even `k = 2` is half of all inputs, so a positive is weak evidence and a negative is weaker.** *Priors that a total q = 1 template is found: k = 1: 25; k = 2: 40.*
- **(iv) The s = 6 hypergraph sketch** checked numerically at the smallest `N` where the union bound applies, or reported unchecked.

**Lemma W25.1's novelty check against W7-W14 and Wilson's Theorem 12 runs before the page calls it new.**

---

# W25 Findings

*Appended after the work and after the reviewer accepted the record (25c, W25.1, W25.2, W25.3, boundary restated). Nothing above is revised. **Membership-query model on every line; deterministic back-mappings only (Flag H7); depth 1.***

## §6. Outcome against priors

| code (amended, §5A) | priors: §3 mine / reviewer; §5A supplementary | outcome |
|---|---|---|
| **25a** some unconditional count gives "at `n′ = n` no depth-1 template of any fan-in is total" | 17 / 20; 13 | **not reached -- and cannot be: at unbounded fan-in such templates EXIST (§9)** |
| **25b** crux exhibited AND no count survives unconditionally | 58 / 55; 62 | **first clause yes, second clause false: a count survives at q = 0** |
| **25c** neither | 25 / 25; 25 | **the outcome, with the obstruction renamed: the first moment is exact at q = 0 and must fail from q = 1, because totals exist at unbounded fan-in** |

*Footnote, the original `1 + log r` wording:* ill-posed at the line's instance (§5A), not scored.

**The designed kill tests landed as predicted, and the round's answer did not come from them.** The crux the round opened on -- does blocking reduce to a constant reader? -- was exhibited (§7) and then turned out not to matter for the count (§8). **What mattered was which resource the statement quantified over: fan-in.**

## §7. The characterisations of blocking (n = 2, exhaustive, history-free)

Blocked triples `(x, v, y)` under four definitions (§5A, plus the reviewer's constant-PP, whose predictions were registered before it ran):

| template | exhaustive | constant-P | constant-A′ | constant-PP | status |
|---|---|---|---|---|---|
| positive control | 32 | 32 | 32 | 32 | all equal, as predicted |
| hub | 8 | 8 | 8 | 8 | warm |
| two-hub | 0 | 0 | 0 | 0 | warm |
| **split-reader** | **32** | 16 | 16 | 16 | cold; **gap under every local definition** |
| **validity-split** | **26** | 24 | 26 | 26 | cold; P's gap closed by propagation |

"P-not-exhaustive" and "PP-not-exhaustive" are 0 in every row (soundness control). **Every advance prediction landed: mine (§5A) and the reviewer's four for constant-PP.** A definitional fix, made before any number: literal "constant on the admissible slice" is **vacuous** -- a blocked slice has no admissible completion -- so A′ is constancy after propagating the non-readers' constraints, which is the reviewer's constraint-set picture. The n = 3 rows were still running at commit time and are not reported.

## §8. Lemma W25.1 and Finding W25.2

**Finding W25.2 (set certification; the reviewer's correction of my first reading).** In the membership model a "no" to "is `u ∈ range(C)`?" is a win: Q outputs `u`. So the adversary answers yes throughout, and Q's `q` queries and its output form a set `V(y)` of size `≤ q + 1` **determined by `y` alone**. Totality is static: **for every valid `y`, every `C` with `V(y) ⊆ range(C)` has `y ∈ range(C′)`.** No pins, no histories. **My intermediate claim that the difficulty was cross-history selection (W14's obstruction) was an artefact of lazy hosting and is withdrawn.** *Membership-model specific: in Korten's Definition 9 DNF model a "no" is not a win, and this collapse does not happen.*

**Lemma W25.1 (q = 0, any glue, any fan-in).** *Certified hints `≤ 2N`; this is tight (the positive control reaches `2N`); hence at least `N` valid hints are non-certifying, and no zero-query depth-1 back-mapping is total.*

*Proof.* Draw `C` injective with uniformly random range `R`, `|R| = N` among `2N` strings, so `Pr[v ∈ R] = 1/2`. If `y` certifies `v`, then `{v ∈ R} ⊆ {y ∈ range(C′)}`, so `Pr[y ∈ range(C′)] ≥ 1/2`. Summing over certified `y`: `#certified/2 ≤ E|range(C′)| ≤ N`. A hint in `range(C′)` for **every** `C` numbers `≤ min_C |range(C′)| ≤ N`, so `≥ 3N` hints are valid. ∎ *(The uniform distribution gives `2.54N`; the injective one is exact. The first step of the argument is mine, the injective distribution is the reviewer's, and the reviewer audited the valid-hint step.)*

**Novelty, checked against the committed pages.** W14 §3 defines q = 0 totality ("total iff every valid hint excludes some string"); W12.1 has the `k = 1` mass bound `Σ_y max_v ≤ N·2^{n+1}`. **W25.1 is the any-fan-in, exact-constant version: new to the line, small.** Wilson's Theorem 12 has no hint (a membership query is width 1, so `q ≥ N`), so there is no overlap.

**Correction to W13 (the reviewer's request, carried).** W13 §2 wrote *"no averaging argument over hints alone can produce a free hint"*, and W14's kill test (v) relied on it. **Refuted as written**: W25.1 is an averaging argument over hints, weighted by probability, and it produces a free hint at q = 0 for every glue. **What W13 proved stands**: its specific bound (`|Y_v| ≤ 2k`, sparse free set) is vacuous. What survives of the sentence is §9's point: no argument blind to fan-in can go past q = 0.

## §9. Finding W25.3 -- THE FAN-IN BOUND IS LOAD-BEARING

**The reduction (derived before any run, §5B).** With glue of fan-in `N`, each C′-input may read all of `C`, so `range(C′)` can be any set of `≤ N` hints as a function of `range(C)`. **Totality at q then holds iff there is `y ↦ V(y)`, `|V(y)| ≤ q + 1`, with at most `N` sets `V(y)` inside every `N`-subset `R`** (subsets of size `< N` contain fewer).

**n = 2, q = 1: `K_{4,4}`.** Its 16 edges on 8 vertices, one per hint; a 4-set split `(a, 4 − a)` spans `a(4 − a) ≤ 4` edges. **Verified as an actual template over all 4096 `C`: 0 valid hints left unhandled -- a total depth-1 template with one membership query.**

**All N ≥ 16, q = 5: a random 6-uniform hypergraph.** Take `4N` random 6-subsets of the `2N` strings. A fixed 6-set lies in a fixed `N`-set with probability `C(N,6)/C(2N,6) ≤ 2^{−6}`, so an `N`-set contains `X ~ Bin(4N, ≤ 2^{−6})` edges, mean `λ ≤ N/16`. Chernoff: `Pr[X ≥ t] ≤ (eλ/t)^t` with `t = N + 1`. Union over `≤ C(2N, N)` sets, natural logs, recheckable:

| N | ln C(2N,N) | ln tail | sum |
|---|---|---|---|
| 16 | 20.21 | −31.16 | **−10.95** |
| 32 | 42.05 | −59.51 | −17.46 |
| 64 | 86.07 | −116.23 | −30.16 |
| 1024 | 1415.53 | −1817.90 | −402.38 |

Asymptotically `ln C(2N,N) ≈ 1.386N` against `ln tail ≈ N(1 + ln(1/16)) ≈ −1.773N`. **So for every `N ≥ 16`, some 6-uniform hypergraph works, and with fan-in-N glue five membership queries give a total depth-1 template.**

**Why nothing in the line breaks.** Fan-in-`N` glue is an **exponential-size** `C′`, outside Korten's poly-time reduction. **W13 line 41's "arbitrary glue with k = poly(n)" is exactly the hypothesis W25.3 shows cannot be dropped**, and W7-W14's four theorems all live inside it.

**The boundary restated.** The first moment (W25.1) is blind to fan-in. **It is exact at q = 0 and must fail from q = 1, because at unbounded fan-in total templates exist at q = 1 (n = 2) and q = 5 (all N ≥ 16).** Any lower bound for poly fan-in has to use the fan-in.

## §10. Searches reported as evidence only

- **n = 3, fan-in N, q = 1** (graph form: 32 edges on 16 vertices, every 8-set spanning `≤ 8`): hill-climb for 240 s, best maximum **11**. None found; my prior on existence was 20. Consistent with the picture: pairs are too dense for halves, 6-sets are not.
- **n = 2, bounded fan-in `k = 1, 2`, q = 1:** no total template found. **Method disclosure:** the pre-registered 0/1 score (#valid hints left unhandled) was **flat**, 16 from every start in 6 runs, so those runs are **uninformative**, not negative evidence. A graded rerun, with score `Σ_y min_pair #{C avoiding y, pair ⊆ range(C)}`, got stuck at 4032 (`k = 1`) and reached 2657-3085 (`k = 2`), with every hint still unhandled. **Weak evidence; at n = 2, `k = 2` already reads half of the inputs.** Priors 25 (`k = 1`) and 40 (`k = 2`) on a total being found: none found.

## §11. Errors and misses, on the record

**Mine.** (1) My cross-history-selection reading (§8) was an artefact of lazy hosting; the reviewer caught it. (2) My §0 (fan-in-`r`) statement rested on unread stretch bookkeeping; the audit retired it. (3) The flat 0/1 search score was not checked before registering; disclosed in §10.
**The reviewer's** (four in W24-W25, recorded in its own words): the `1 + log r` parametrisation; the "single-call = one Avoid call" ruling (corrected from W8's definition); two false premises in the constant-PP cross-position argument (one excluded value per hint, and `r·2^{n′−n}` readers per input, are **averages**); and the q = 1 search specified at unbounded fan-in without pricing what fan-in buys.
**Shared, and the round's practice line:** **PRICE EVERY RESOURCE A STATEMENT QUANTIFIES OVER BEFORE COUNTING UNDER IT.** Both of us treated W25.1's fan-in independence as generality; it was the reason the count could not pass q = 0.

## §12. Closing

**W25 proves nothing about P vs NP**, nothing about Avoid in `FP^NP`, and by Flag H7 nothing randomised. It records one small lemma (W25.1), one reformulation that retires lazy hosting in the membership model (W25.2), and one structural fact (W25.3): **at depth 1, black-box hardness lives entirely in the glue's fan-in bound.** Next, the reviewer's W26: the query-versus-fan-in tradeoff.
