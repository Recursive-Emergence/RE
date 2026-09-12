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
