# X3: four paths toward the missing measure. Report

*Run 2026-09-10 on branch `x3-measure-paths`, on the author's go ("Draft and run X3, push after merge"; "No, keep formal/ closed"), against the pre-registration (9c8b646), accepted by the reviewer with all five flags; priors X3b 55 / X3a 25 / X3c 20. g1, g5, g8 and g9 applied. `formal/` untouched.*

## 0. The specification, as Flag S sharpened it (stated first, per the ruling)

μ must be:
- **exponential-scale**, because log-scale measures are at most n + 1 on IP2 and can certify only linear list length;
- **polynomial on Equality-type gates;**
- **additive over the list;**
- **small on Chattopadhyay–Mande's F_n**, where sign-rank is not.

Every candidate is tested in the order EQ → F_n → IP2 (Flag B).

## 1. Outcome

**X3a, partially.**
- **One measure survives, in a restricted form, and it was not found by the map before now.** Podolskii–Prior 2025 prove that blocky-matrix discrepancy, applied recursively over *alternation blocks*, gives superpolynomial exact-threshold decision-list lower bounds for IP2 at alternation depth o(n/log n).
- **It stops at alternation, not at Equality.** The loss is additive *within* a block of constant output and multiplicative *across* alternations. So the measure meets (3) only within blocks, and fails exactly when the list alternates ≳ n/log n times.
- **The sharpened open statement:**
  > **IP2 has no polynomial-size decision list of exact thresholds with alternation depth ≳ n/log n.**
  - Bounded alternation is now known.
- **X3c does not occur.** No THR∘THR function with sign-rank 2^{Ω(n)} is found (Path D), so L1 survives.
- **A miss of mine in X2 is corrected here.** X2 said "the only known lower bound is the linear one proved here" and that L0's status was "not found stated either way". Podolskii–Prior's bounded-depth theorem existed, and my X2 search did not find it. X2 §4.1's Equality counterexample was also already observed in the literature (Podolskii–Prior's [2], using [17]). X2 marked it "not claimed new"; it now has its attribution.

## 2. Sources read in this run (primaries unless noted)

- **Chattopadhyay–Lovett–Vinyals**, "Equality Alone Does not Simulate Randomness", ECCC TR18-206 / CCC 2019.
- **Pitassi–Shirley–Shraibman**, "The Strength of Equality Oracles in Communication", ITCS 2023 (author PDF).
- **Göös–Harms–Riazanov**, "Equality is Far Weaker than Constant-Cost Communication", arXiv:2507.11162.
- **Podolskii–Prior**, "Alternation Depth of Threshold Decision Lists", ECCC TR25-143: abstract, §1, Theorems 45 and 50.
- **Chen–Santhanam–Srinivasan**, arXiv:1806.06290; **Alman–Chan–Williams**, arXiv:1608.04355; **Impagliazzo–Paturi–Schneider**, arXiv:1212.4548. Abstracts read on arXiv; the search summaries were checked against them.
- **Chattopadhyay–Mande** and **CMMS**: carried from X1/X2.

## 3. Path A: Equality-oracle communication (the scale kill; the blocky object survives)

**Statements.**
- *CLV (abstract):* "a total function on n bits with randomized one-sided communication complexity O(log n), but such that every deterministic protocol with access to 'Equality' oracle needs Ω(n/log n) cost to compute it."
- *PSS (abstract):* nondeterministic communication with an Equality oracle is a strict subclass of MA. "Integer Inner Product … cannot be computed using sublinear communication in the nondeterministic Equality model", via "a covering number based on the blocky matrices of Hambardzumyan, Hatami, and Hatami, as well as a natural variant of the Gamma-2 factorization norm."
- *GHR 2025 (abstract):* "an n-bit communication problem with a constant-cost randomized protocol but which requires n^{Ω(1)} deterministic (or even non-deterministic) queries to an Equality oracle."

**Does it survive exact thresholds? Yes, trivially.** An exact-threshold query a(x) = b(y) is one Equality-oracle call on (a(x), b(y)), and its 1-set is a *blocky* matrix: block-diagonal up to permutation. Podolskii–Prior's Lemma 15: "a query on this layer defines a blocky matrix". So a length-ℓ exact-threshold decision list is an Equality-oracle protocol with ℓ calls. The containment worry of Flag A is moot at linear scale.

**The kill is scale (Flag S).** Oracle-*cost* measures are at most n + 1 on every function (Alice sends x). They certify ℓ = Ω(n/log n) at best, for IP2 via its randomized cost. **Path A dies as a cost measure.** This is distinct from a measure kill and from a containment kill.

**The blocky matrices survive as an object.** PSS's blocky covering characterizes the *nondeterministic* model: OR of blocky matrices, i.e. alternation depth 1. Podolskii–Prior carry blocky matrices with discrepancy through *decision lists* (§5). That is the surviving form.

## 4. Path D: the fold-exponent hierarchy (L1 survives)

- **The best known sign-rank inside THR∘THR is still 2^{Ω(n^{1/4})}** (CM, linear-size ELDL/THR∘THR). Podolskii–Prior (2025, §1) restate this as the reason "Sign-rank also cannot prove lower bounds against ELDLs".
- No 2^{Ω(n)} example was found: two searches, plus the 2025 survey paragraph (g8). Sherstov–Wu's exp(Ω(n^{1−ε})) is for AC⁰, and would not kill L1 even inside THR∘THR (Flag D).
- **D's form of L1, stated:**
  - *weak (L1):* every poly-size THR∘THR circuit has sign-rank 2^{o(n)};
  - *strong (CM's question):* 2^{O(n^ε)} for some ε < 1.
  - The known exponent is 1/4 from below; IP2's is 1.
  - "Bounded away from 1" is the strong form; L1 needs only the weak one.

## 5. Path B: L0 restated, and the invariant that survives

**The statement (in markdown, per the author), for exact thresholds.** For every polynomial p there is n₀ such that for all n ≥ n₀, no list ((w⁽ⁱ⁾, v⁽ⁱ⁾, t_i, o_i))_{i≤ℓ} with ℓ ≤ p(n) computes IP2. The list computes o_j for the least j with ⟨w⁽ʲ⁾, x⟩ + ⟨v⁽ʲ⁾, y⟩ = t_j, and a default output otherwise.
- With *arbitrary* a(x) = b(y) queries the model is decision lists of Equality-oracle calls: stronger, and its lower bounds imply L0 (Flag L).
- Podolskii–Prior's ELDL uses exact linear thresholds, "w₀ + Σ wᵢxᵢ = 0" with natural weights.

**Candidates, in the order EQ → F_n → IP2:**

| Candidate | EQ | F_n | IP2 | Verdict |
|---|---|---|---|---|
| distinct row patterns | **dies**: the identity has 2^n rows | — | — | killed at step 1 (Flag B) |
| randomized / oracle cost (log-scale) | small | small | Θ(n) | killed by scale: certifies only Ω(n/log n) (Flag S) |
| sign-rank | small | **dies**: 2^{Ω(n^{1/4})} | 2^{Ω(n)} | killed at step 2 (CM) |
| monochromatic rectangles (additive) | **dies** ([2]/[17]; X2 §4.1) | — | — | killed at step 1 |
| **blocky discrepancy, recursive over alternation blocks** (Podolskii–Prior Theorem 45) | passes: a single ETHR is one blocky layer | consistent: F_n is a linear-size ELDL, which Theorem 45 does not contradict | **size ≥ Ω(k·d^{−1/(2k)})** at alternation depth k, with d = Disc_U(IP2) | **survives for k = o(n/log n); stops at alternation** |

**Theorem 45, verbatim in content:** "Let f … and Disc_U(f) ≤ d … Assume that f is approximately balanced … Then the size of ELDL of depth k computing f is at least Ω(k·d^{−1/2k})."
- The proof bounds, layer by layer, the number of f⁻¹(b)-entries that the blocky queries of layer i cover by √(2^{2n+i}·d) times the product of the layer sizes.
- The loss per layer is multiplicative, which is exactly why the bound decays as the alternation depth grows.
- Also Theorem 50 (hierarchy): "Any ELDL_{k,1} computing INT⁽ᵏ⁾_n has size 2^{Ω(n/k)−O(k)} … exponential for k = O(√n)."

**The sub-obstacle, named (the lemma under the lemma, sharpened):** *a measure over blocky matrices whose loss across output alternations is additive rather than multiplicative.* With it, Theorem 45's recursion would give L0(IP2) at every alternation depth.

## 6. Path C: the algorithmic frontier (verified; no attempt)

- **IPS 2013:** SAT for **cn-wire** depth-2 threshold circuits, saving 2^{sn} with s = 1/c^{O(c²)}.
- **CSS 2016:** Parity has correlation ≤ n^{−ε_d}, and Generalized Andreev ≤ exp(−n^{ε_d}), with depth-d threshold circuits of **n^{1+ε_d} wires**; plus SAT algorithms in that regime.
- **ACW 2016:** 2^{n−n^ε} SAT for AC⁰[m]∘LTF∘LTF with a **subquadratic number of bottom LTF gates**, "This also implies new circuit lower bounds for threshold circuits."
- **The gap is scale and target.**
  - *Scale:* the frontier is at n^{1+ε} wires, or subquadratic bottom gates, against the arbitrary polynomial the fold statement needs.
  - *Target:* SAT-to-lower-bound transfers yield hard functions in NEXP-type classes, not IP2 specifically. Path C cannot settle *IP2* ∉ THR∘THR even at full strength; it would give *some* explicit function outside the class.

## 7. Filter F (a reading, as labelled)

By Book's transfer, the general fold hierarchy needs a non-relativizing ingredient. IP2 ∉ THR∘THR is a fixed-class statement and is not subject to that. Podolskii–Prior's measure (Path A/B) is a fixed-class tool, and Path C's algorithms are the short-description ingredient the general hierarchy would need.

## 8. Priors against outcome

| | X3a | X3b | X3c |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 35 → 25 | 45 → 55 | 20 → 20 |
| mine | 25 | 55 | 20 |
| **outcome** | **X3a (restricted)** | | |

**Misses:**
- *mine:* the X3b weight (55). The surviving measure was in the literature, and X2's search missed it. X2's "only known lower bound" line is corrected here.
- *both sides:* the spec's "additive" clause (3). The one measure that works is additive only within alternation blocks. The spec should have asked about alternation, and the literature had already made that its parameter.

## Formal record

Untouched. `formal/` and `appendix_M_formal_system.md` are unchanged since b88c18b (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as X3a, restricted.** Both misses of mine are recorded as written:
- X2's "only known lower bound";
- the X3b weight.

The spec-clause (3) miss ("additive", where the literature's parameter is alternation) is **joint, and scored on both sides**.
