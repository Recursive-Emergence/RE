# W6: the round complexity of the fold. Pre-registration

*Drafted 2026-09-11 on branch `w6-round-complexity`, on the reviewer's W6 specification, after its W5 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**This file is committed BEFORE any source is read for W6. Everything below is fixed in advance and is not revised retroactively. Findings are appended afterwards, below the rule at the end.**

## Ceiling (first)

Unchanged, and it is the whole W-line's ceiling. W6 studies the **round structure** of an algorithm for Avoid whose existence is already conditional. Nothing here bears on P vs NP; the best outcome is a sharper statement of which resource — rounds, not queries — the fold actually spends, plus a falsifiable form for the record's "hiding is depth" thesis. **Rounds are not hardness.** A round lower bound in a black-box model would constrain techniques, not prove a separation.

## §0. Refuted premises checked (the standing practice)

Not reused: "hidden ρ" (Y3); "no off-sample rows" (Y4); "the grid is symmetric" (Y5); "(PL) is loose-access lowness" (Y6); "the Pessiland oracle does not bar the route" (Y7, reversed by Y8); "the generator's outputs are deep" (Y9, refuted by counting); **"prefix descent must resolve a deficit of 1" (W5, mine — false; the deficit stays ≥ half the subcube, and the real obstruction is additive error ε2ⁿ against a required resolution 2^{n−k})**; **"(D1) is smaller than the door" (W4's prose, corrected in W5 — (D1) ⇒ (C₁) and is at least as strong)**.

**And one carried in from W5's own correction, still warm:** *a superscript dropped by text extraction must never be reconstructed inside quotation marks.* W5 quoted SU05 Def 2.4 as "2^{n^ε}" where the extraction had lost the exponent; the reviewer caught it. Every verbatim quote in W6 that contains an exponent is checked against a second extractor before it is written.

## §1. Why this question, stated before reading

The W-line's door is (C₁): FP^NP for Avoid ⟺ E^NP ⊄ SIZE[2^{o(n)}], with the hypothesis provably minimal (RW26 §5). W5 established that the counting route (D1) is **sufficient and at least as strong**, not a weakening. So "make it smaller" cannot mean a weaker hypothesis; it must mean a smaller object or a different kind. **(D2) — non-adaptive Avoid — is the "different kind" candidate, and rounds are its natural parameter.** W6 asks what is actually known about that parameter.

## §2. My priors, fixed now

### Q1 — the classical baseline

| code | statement | my prior |
|---|---|---|
| **Q1a** | `P^NP_tt = P^NP[O(log n)]` holds for **languages**, as Buss–Hay / Hemachandra, verbatim and with that quantifier | **90** |
| **Q1b-fail** | For **functions**, `FP^NP_tt = FP^NP[O(log n)]` is **not** known, and equality is known to force a collapse (P = NP, or NP = coNP, or similar) | **60** |
| **Q1b-open** | For functions, simply open, with no such known consequence | 25 |
| **Q1b-eq** | Equality holds for functions too | 15 |
| **Q1c** | The k-rounds-of-parallel-queries hierarchy has **known relativized separations** as k grows | **70** |

I am confident of the inclusion `FP^NP[O(log n)] ⊆ FP^NP_tt` in the function case by the path-enumeration argument (a log-query adaptive computation has poly many query paths, all askable in parallel), and I expect the *converse* to be where the content is. **I have not verified any of this and may have the attributions wrong; Hemachandra 1989 vs Buss–Hay 1991 vs Wagner are exactly the kind of credit I have previously mis-assigned.**

### Q2 — the engine's round count

| code | statement | my prior |
|---|---|---|
| **Q2a** | RW26's own text supports the attribution: the **n** term is the prefix/seed search, the **log(T/n)** term is the tree depth (= W3's fold depth) | **75** |
| **Q2b-none** | **No** round lower bound is known, in any model, for solving Avoid given a hard string | **75** |
| **Q2b-some** | Some black-box or oracle round lower bound exists (Korten survey §8.1, Korten–Pitassi FOCS'24, or GGLS25's depth-n downward self-reduction) | 25 |

The reviewer's prior on Q2b-none is 70; mine is 75, and for a stated reason: **a round lower bound would be a statement about adaptivity in a model where the hard string is given, which is close enough to the linear ordering principle's depth that if it were known, W3 would have found it.** If GGLS25's LOP self-reduction of depth n turns out to *be* such a bound, Q2b-some wins and my prior is wrong.

### Q3 — what hypotheses buy

| code | statement | my prior |
|---|---|---|
| **Q3-no** | SU05 Thm 3.11 (`BPP^{NP‖} = P^{NP‖}`) does **not** give Avoid ∈ FP^NP_tt outright, because it is a **language/decision** statement and Avoid is a **single-valued search** problem | **65** |
| **Q3-yes** | It does give it outright | 25 |
| **Q3-other** | Neither cleanly | 10 |
| **Q3-src** | RW26's "known only from [KM02; MV05]" traces to **hitting-set generators / derandomizing AM** (Klivans–van Melkebeek; Miltersen–Vinodchandran), i.e. the prMA queries are derandomized into **one** round | **70** |

**Flag A6, registered now:** the reviewer's Q3 asks whether Thm 3.11 "gives Avoid ∈ FP^NP_tt outright via the trivial FZPP^NP algorithm". I predict the honest answer is **no, and the right instrument is Thm 3.6/3.12 (the relative-error approximator / hitting-set construction), not Thm 3.11** — because turning a randomized *search* procedure into a deterministic one needs the generator, not the class equality. If the run finds otherwise, Q3-yes wins.

### Q4 — the RE test, and the counting done before the prior

The reviewer asked for the counting before a prior. **Here it is, and it changes the question's shape before I read anything.**

If Avoid ∈ FP^NP_tt is *already known under a hardness hypothesis* (Q3-src, prior 70), then **"the round count is intrinsic" is false as an unconditional claim about the problem**, because a hypothesis that nobody expects to fail already collapses it to one round. Therefore:

- the naive form — "extracting the residue from a hard history cannot be made non-adaptive" — is **already conditionally refuted**, and I register that now rather than discovering it mid-run;
- the only form that can survive is a **relativized, unconditional** one: *there is an oracle relative to which Avoid given a hard string is in FP^NP[O(n + log T)] but not in FP^NP_tt.*

| code | statement | my prior |
|---|---|---|
| **Q4-oracle** | The surviving form is the oracle statement above, and it is **open** — neither confirmed nor refuted by anything on record | **65** |
| **Q4-refuted** | Even the oracle form is refuted, or is inconsistent with a known relativizing collapse | 20 |
| **Q4-confirmed** | Something on record already confirms it | 15 |

**Flag E6 — my sharpest pre-registered prediction, and the one most likely to be wrong in an interesting way.** The Buss–Hay-type collapse covers **O(log n)** queries. The fold spends **O(n + log(T/n))** rounds. So *even for languages, and even granting every classical collapse*, the n term is out of reach of that machinery: **the obstruction is the n term (the prefix/seed search), not the log(T/n) term (the fold depth).** If that is right, then "hiding is depth" is being tested on the wrong summand — the depth term is the one the classical theory could plausibly collapse, and the *search* term is the stubborn one. **Prior that this diagnosis survives contact with the sources: 80.**

## §3. Flags (mine, before any work)

- **Flag A6** — Thm 3.11 is a language statement; see Q3 above.
- **Flag B6** — three distinct notions must never be merged, and every line of the deliverable states which one it means: (i) **adaptive queries** `P^NP[k]`; (ii) **rounds of parallel queries**, k rounds each of poly many; (iii) **non-adaptive** = truth-table = exactly one round. The W6 specification's Q1 moves between "rounds of adaptive NP queries" and "non-adaptive access" in one sentence; the run keeps them apart.
- **Flag C6** — **languages vs functions is the crux, not a footnote.** The fold is a search/function problem. A language-level collapse does not transfer to it for free, and I expect this to be the single most load-bearing distinction in the answer.
- **Flag D6** — every exponent in every verbatim quote is confirmed against a second extractor before it is written (the W5 lesson, above).
- **Flag F6** — "relativized" is claimed only where a source says it; a black-box impossibility (DS26's word) is **not** a relativization barrier, and W5 already had to draw that line once.

## §4. Kill tests

- Sizes, oracle model, adaptive/parallel, languages/functions, and i.o./a.e. on **every** tabulated line.
- Theorem numbers on every entry, or the entry says "not located".
- Check the ECCC keyword page for range avoidance, and **TR26-118 §3–§5**, before writing "open" anywhere.
- Relativization claimed only where stated (Flag F6).
- Credit checked: Buss–Hay / Hemachandra / Wagner / Krentel / Selman are easy to mis-attribute, and I have mis-attributed before.
- **If a prior is wrong, the report says so in the same sentence as the finding, not in a later section.**

---

*Findings follow below, appended after reading. Nothing above is revised retroactively.*
