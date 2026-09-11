# X10: the bias-to-monochromatic bridge. Report

*Run 2026-09-11 on branch `x10-bias-bridge`, on the author's go ("ya"), against the pre-registration (08011dd), accepted by the reviewer with Flag Z, the affine-subspace-pair enlargement, and priors fails at a named step 80 / below the threshold 15 / proved 5. Documents plus computation (`x10_gain.py` in the job's scratch directory); `formal/` closed. **The X8 practice:** smallest case first, and the compared quantity beside every number.*

## 0. Outcome

**The bridge fails at a named step: the endpoint mismatch.**
- **R1 is dead** by the AND kill test (§2).
- **R2's density increment works where it can be checked.**
  - The relative bias grows under the best restriction by ≥ 4/3 per step for every tensor family (proved, §3), and by 1.33–39 in every tested family (numerics, §4). Hyperplane-pair restrictions give at least as much.
  - But **Z2 needs purity 1 − O(1/m)** (C within ε ≤ 1/(8m) of an entire sign class). A multiplicative increment delivers only **constant** relative bias.
  - The statement that would close the gap, "constant relative bias forces 2^{Ω(n′)} constraints", **is the loose Union Lemma itself at the top bias scale**. So the bridge is circular exactly at its last step.
- **Flag Z** (the X9 correction) is proved in full here (§1). **Z2 is new** (ours, elementary): a robust covering bound.
- **Priors:** outcome "fails at a named step" (mine 80, the reviewer's 80 after moving).

## 1. Flag Z: the correction, with proofs (g5)

**Setting.** H is the IP2 sign matrix (N = 2^n). M⁻ = {H = −1} with |M⁻| = S := (N² − N)/2, and M⁺ = {H = +1}. U = ∪_{j≤m} q_j with q_j blocky. Each q_j is a union of rectangles R_{j,t} that are row-disjoint and column-disjoint within j. So **every row, and every column, lies in at most m of U's rectangles**, and so does every cell.

**The X9 error.** Pitassi–Shirley–Shraibman's Theorem 29 bounds the number of blocky matrices, each contained in A, that cover A's ones. The AND family's U contains every −1 entry *and* +1 entries, so it is not such a cover. Its complement C = DISJ is all +1, with 3^n entries, and m = n. **"Polynomially many constraints cannot make C monochromatic" is false; withdrawn.**

**Z1 (exact).** If C is an entire sign class, then U is exactly the other class. U's rectangles then lie inside that class and form a valid 1-cover, and PSS gives m ≥ Ω(2^{n/2}), by X9 §3's arithmetic with the −1-rectangle theorem. ∎

**Z2 (robust; new).** If |U ∩ M⁻| ≥ (1 − ε)S and |U ∩ M⁺| ≤ εS with ε ≤ 1/(8m), then m ≥ (N² − N)/(8N^{1.5}) ≈ √N/8. Symmetrically for the +1 class.

*Proof.*
1. Each cell lies in ≤ m rectangles, so Σ_R |R ∩ M⁺| ≤ m·εS.
2. Call R *impure* if |R ∩ M⁺| ≥ |R|/4. Then |R ∩ M⁻| ≤ 3|R ∩ M⁺|, so impure rectangles contain ≤ 3mεS entries of M⁻.
3. Hence the *pure* rectangles cover ≥ (1 − ε − 3mε)S ≥ S/2 entries of M⁻, using 4mε ≤ 1/2.
4. A pure R has −Σ_R H = |R ∩ M⁻| − |R ∩ M⁺| > |R|/2. Lindsey gives |Σ_R H| ≤ √(N|R|), so |R| < 4N.
5. For a pure R with r rows and c columns: r + c ≥ 2√|R| ≥ |R|/√N. Summing, Σ_pure (r + c) ≥ (S/2)/√N.
6. But Σ_all (r + c) ≤ 2mN (each row and column lies in ≤ m rectangles).
7. So m ≥ S/(4N^{1.5}). ∎

**The corrected §3(iv) sentence for the next page update.** "Covering either sign class of IP2 by blocky sets needs Ω(2^{n/2}) sets (Z1). The same holds for unions within ε ≤ 1/(8m) of an entire sign class (Z2). So polynomially many constraints cannot make C an entire sign class, or nearly one. They *can* make C monochromatic: disjointness, with m = n."

## 2. Reading R1 is refuted by the kill test (the AND family)

R1 says: if C is ε-monochromatic with density δ on a sub-cube of dimension n′, then m ≥ Ω(2^{n′/2}·δ).
- DISJ is monochromatic at n′ = n with δ = (3/4)^n and m = n.
- R1 would give m ≥ Ω((3/(2√2))^n) = Ω(1.0607^n). **False.** ∎

## 3. Reading R2: the increment step (proved for tensor families)

**The splitting identity.** Restrict on a coordinate pair (x_i, y_i) = (s, t), or on an affine hyperplane pair {u·x = s} × {w·y = t} with u·w = 1, so that the pairing stays nondegenerate. IP2 becomes ±IP2_{n−1}, and C restricts to a co-blocky conjunction with the same m. Then Adv(C) = Σ_{s,t} ±Adv(C_{s,t}), so **max_{s,t} |Adv(C_{s,t})| ≥ |Adv(C)|/4**. The relative bias β := Adv/4^{n′} never decreases under the best branch. The **gain** is g := 4·max|Adv_branch|/|Adv|.

**Tensor families gain ≥ 4/3 per coordinate step (ours, proved).**
- For C = ⊗_i c_i with 2×2 masks c_i, we have Adv(C) = ∏_i a_i with a_i = ⟨H₂, c_i⟩ ∈ {0, ±1, ±2, 3}.
- Restricting coordinate i to a cell of c_i multiplies by ±1 in place of a_i, so g = 4/|a_i| ≥ 4/3. It equals 4/3 exactly for a_i = 3, the AND mask.
- The AND family is therefore the slowest tensor family. ∎

**The kill tests.**
- **AND:** g = 4/3 at every step (coordinate and hyperplane pairs alike, §4). β = (3/4)^{n′} reaches near-class level (≈ 1/2) only at n′ ≈ 2, so n′ = O(1) ≤ 2·log₂n. ✓
- **Block-Equality:** Adv(C) = 2^n = Adv(J), the trivial level. Its excess over J is 1, so it reaches near-class only at n′ = O(1) and gives nothing. ✓

## 4. Numerics (the gain g, beside the relative bias; exploratory)

| family | n | Adv(C) (vs 3^n; vs 2^n = trivial) | relative bias β | coordinate gain | best hyperplane-pair gain |
|---|---|---|---|---|---|
| AND / DISJ | 6 | 729 (= 3^n) | 0.178 | 1.333 | 1.333 |
| AND / DISJ | 8 | 6561 (= 3^n) | 0.100 | 1.333 | 1.333 |
| block-EQ complement | 6 | 64 (= 2^n: U has 0) | 0.016 | 2.0 | 3.0 |
| block-EQ complement | 8 | 256 (= 2^n) | 0.004 | 2.0 | 3.0 |
| random conjunctions, m = 6–13 | 6 | 6 – 32 | 0.001 – 0.008 | 3.7 – 24 | 5.6 – 39 |
| random conjunctions, m = 9–20 | 8 | 75 – 301 | 0.001 – 0.005 | 2.3 – 7.9 | 3.3 – 8.6 |

The gain is ≥ 4/3 everywhere, and hyperplane pairs (the Bogolyubov-type move) are never worse than coordinates. Random conjunctions have *small* bias because of cancellation, which is exactly what splitting undoes, and so they show large gains. The numbers are small-n and exploratory.

## 5. The named failing step: the endpoint mismatch

- **The increment delivers constant bias.** From β₀ = 2^{−n/4} (the loose Union Lemma's scale) with gain ≥ g₀ > 1 per step, the relative bias reaches a constant after O(n/log g₀) steps, at dimension n′ = n − O(n) (linear, for the AND rate g₀ = 4/3: n′ ≈ 0.4n).
- **But Z2 needs purity 1 − O(1/m).** "C within ε ≤ 1/(8m) of an entire sign class" is relative bias ≥ 1/2 − O(1/m). That is **not** a multiplicative gain in β: it is a gain in purity from constant to 1 − 1/(8m).
- **The statement that would bridge constant bias to a lower bound on m** is "|Adv(IP2_{n′}, U)| ≥ c·4^{n′} forces m ≥ 2^{Ω(n′)}". **That is the loose Union Lemma at the top bias scale**, so the bridge is circular exactly here.
  - The Z2 argument does not extend to constant bias. With |U ∩ M⁺| = Θ(4^{n′}), impure rectangles can hold all of U's −1 entries once m ≳ 1/c, since the bound 3m·|U ∩ M⁺| no longer forces pure rectangles to cover.
- **A second, independent gap:** the per-step gain is proved only for tensor families (g ≥ 4/3). For general co-blocky conjunctions it is only observed. A proof would need: every co-blocky conjunction with relative bias ≥ 2^{−n/4} has a coordinate or hyperplane-pair split with g ≥ 1 + Ω(1). **Not proved.**
- **So:** X10's bridge fails at the endpoint (constant bias versus 1 − O(1/m) purity), and its increment step is proved only for tensor families. **The lemma under X10 is the loose Union Lemma at the top scale:** constant relative bias against IP2 forces 2^{Ω(n)} co-blocky constraints. X9's B(n, 2n) values (relative 0.45 at n = 6, 0.26 at n = 8) are exploratory data on it.

## 6. Priors against outcome

| | fails at a named step | below the threshold | proved |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 60 → 80 | 25 → 15 | 15 → 5 |
| mine | 80 | 15 | 5 |
| **outcome** | **✓ (the endpoint mismatch)** | | |

**Misses:** the Flag Z miss (X9's overstated sentence) is scored on both sides, as ruled. It is the reviewer's eleventh accepted-without-checking, and mine as the author of the sentence. The X8 practice applied again: the AND family was the smallest case, and the sentence was never put beside it.

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted.** The following go in as stated:
- Z1 and Z2 (proved, ours);
- the corrected §3(iv) sentence;
- the per-step gain (≥ 4/3 for tensor families, with AND the slowest) and its numerics;
- the endpoint mismatch as the named failing step.

**The live lemma is now the constant-bias lemma:** a conjunction of m co-blocky constraints with |Adv(IP2, C)| ≥ c·4^n has m ≥ 2^{Ω(n)}.
- Z2's method fails there: once m ≳ 1/c, impure rectangles can hold all the −1 entries.
- The increment cannot help: it delivers constant bias, not purity.
- The second gap is recorded: the per-step gain is proved only for tensor families.

**X11 is named, not drafted, on the author's go only.** It needs a Lindsey-type statement for the −1 set of a *conjunction* of co-blocky constraints: that impure rectangles arranged by m constraints cannot align with H's sign pattern on a constant fraction of the matrix. The kill tests are the same two families.

**The trail, in the reviewer's words:** "a measure that sees alternation" → the loose Union Lemma → its bias version of PSS Theorem 29 → the constant-bias lemma. Each step is a proved reduction or a refuted route.
