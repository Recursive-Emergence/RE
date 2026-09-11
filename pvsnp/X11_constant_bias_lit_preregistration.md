# X11-lite: the constant-bias lemma, as a bounded literature check. Pre-registration

*Drafted 2026-09-11 on branch `x11-lite`, on the author's go ("Run it, push after merge"), for the reviewer's ruling before any work. **Documents only. No proof attempt.** If nothing applies (X11b), the lemma is recorded in its reformulated form and the program pauses for good on it. g1, g8 and g9 apply; for each source, the exact statement and whether it covers **arbitrary encodings**.*

## §0. The reformulation (the reviewer's; equivalence to verify)

**Blocky sets are exactly the Equality pullbacks.** A blocky q has disjoint row sets A_t matched to disjoint column sets B_t. Set f(x) = t if x ∈ A_t, else a sentinel ⊥_row, and g(y) = t if y ∈ B_t, else a different sentinel ⊥_col. Then q = {(x, y) : f(x) = g(y)}. Conversely, any {f(x) = g(y)} is blocky, with blocks the fibres of the common values.

**So a conjunction of m co-blocky constraints is a pullback of a fixed relation:**
  C = {(x, y) : f_j(x) ≠ g_j(y) for all j ≤ m} = NEQ^m ∘ (F, G),
where F = (f_j)_j and G = (g_j)_j, and NEQ^m on Σ^m × Σ^m means "all m coordinates differ".

**The constant-bias lemma, in this form:** no encodings F, G of length m = poly(n) make NEQ^m ∘ (F, G) have |Adv(IP2, ·)| ≥ c·4^n.

## Checks (the reviewer's)

- **(a) Hambardzumyan–Hatami–Hatami 2022** ("Dimension-free bounds and structural results in communication complexity"): do their structural theorems for small blocky rank, or for few Equality queries, give a poly(m)-piece blocky approximation with small error? If yes, Lemma S/T would prove the lemma.
- **(b) Pitassi–Shirley–Shraibman 2023 and Chattopadhyay–Lovett–Vinyals 2019:** any *correlation* (discrepancy-type) bound for Equality-oracle protocols.
- **(c) Pattern-matrix and lifting methods (Sherstov; Göös–Pitassi–Watson):** why "fixed outer function ∘ gadget" does not cover "fixed relation ∘ arbitrary encodings", and whether any encoding-invariant result exists.
- **(d) NEQ^m itself:** discrepancy and γ₂ as functions of m and |Σ|, i.e. the bias under the *identity* encoding.
- **Kill tests:**
  - AND (F = G = identity on bits, NEQ^n = DISJ, bias (3/4)^n, not constant);
  - block-Equality (bias 0).

## Flags raised before any work (mine)

**Flag R (an expected partial result, elementary: m ≥ Ω(n/log n)).**
- The set NEQ^m ∘ (F, G) is decided by an m-query Equality-oracle protocol. Public-coin fingerprinting simulates each query with error δ/m at cost O(log(m/δ)), so the whole protocol costs O(m·log(m/δ)) with error ≤ δ.
- By the discrepancy method, a cost-c protocol has correlation ≤ 2^c·Disc_U(IP2) ≤ 2^c·2^{−n/2} under the uniform distribution (IP2's discrepancy bound, X5).
- So constant bias c₀ needs 2^{O(m log(m/δ))}·2^{−n/2} + δ ≥ c₀. That forces **m·log m ≥ Ω(n), i.e. m ≥ Ω(n/log n)**.
- This is X2's "randomized cost caps at linear" in correlation form. If it holds, it is X11c's regime, and **the open gap is n/log n ≤ m ≤ 2^{Ω(n)}**.
- To be written as a proof with the exact discrepancy inequality (g5), and checked against X4's needs. The loose Union Lemma needs polynomial m to be impossible at bias 2^{−n/4}, not merely m ≥ n/log n.

**Flag A (the scale mismatch with Hambardzumyan–Hatami–Hatami).** Their dimension-free results concern matrices of *bounded* γ₂ or bounded blocky rank. Our C has γ₂ up to ≈ 2^m (X5, Flag G). The expectation is that (a) applies only at m = O(1), or at m = O(log n) with losses. The report states the exact regime.

**Flag L (the lifting direction).** Lifting lower-bounds f ∘ g^n through f's *query* complexity with a *fixed* gadget g. Here the relation NEQ^m is fixed and the *encodings* F, G are adversarial, so no gadget structure is available. The expectation is "no encoding-invariant lifting theorem exists" (g8).

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X11a** | A structural theorem from (a) or (b) applies: the lemma is proved and X4's threshold moves to linear depth. Re-derive twice. |
| **X11b** | Nothing applies: the lemma is stated in NEQ^m-pullback form, with the exact reason each result stops. The program pauses for good. |
| **X11c** | A partial result, e.g. sub-constant bias or m = O(n); record the regime. Flag R expects m ≥ Ω(n/log n). |

**Priors.**
- Reviewer: X11b 70 / X11c 20 / X11a 10.
- Mine: **X11c 55 / X11b 40 / X11a 5.** Flag R expects an elementary partial result, which the reviewer's outcomes count as X11c. Whether it is *new* is to be checked; it is likely folklore.

## Ceiling

X11-lite proves nothing about P vs NP. It ends the program's descent on this branch either way.
