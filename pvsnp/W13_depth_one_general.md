# W13: depth 1 in full generality — Korten's Problem 1 in the black-box model. Pre-registration

*Drafted 2026-09-12 on branch `w13-depth-one-general`, on the reviewer's W13 specification, after its W12 ruling. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE the attack.**

## Ceiling (first — and it needs more care this round than any previous one)

This is the closest the line has come to the thing Korten actually asked. **Stated exactly:** §8.1 says an unconditional negative answer to Problem 1 is unavailable without P ≠ NP, and that *"it would be interesting to show a negative result in a restricted black box model of reducibility"*. **A full 13a would supply that** — for depth 1, one bit of stretch. It would still **not** be Problem 1: it says nothing about depth > 1, nothing about non-black-box reductions, and by **Flag H7** nothing about randomised ones, since guess-and-test at this stretch sits in FZPP^{NP^C} at depth 0. **It would be a statement about one technique in one restricted model, and it must be reported as that.**

## §1. Refuted premises checked

Not reused: "pick a hint with a local certificate" (W8); "non-injective q_i is the obstruction" (W9, mine, backwards); "each singleton clause forbids one value" (the reviewer's); "α < 1/3" (W10, mine, slack); "Z(x) uniform means W10.3 transfers" (W11, mine — pigeonhole was the point); **"odd cycles break the coupled device" (W11, mine)**; **"two coupled coordinates with different σ break the product structure" (W12, mine)**. **The last two are the same error twice: I keep predicting cross-input coupling is harder than it is. Registered as a standing bias to correct against this round.**

**Standing practice lines:** Definition 9's DNF model only; check the combinatorial step, not only the distribution feeding it; report slack rather than adjusting a definition; quantify every "small".

## §2. Disclosure: what I derived before pricing

**(a) The per-input mass is smaller than the ruling's framing suggests.** For a free u, Φ_u(y) = ∪_{x reads u, f_x = 1} F_{x,u}(y). For fixed forced values, v ↦ G_x(forced, v) is a map {0,1}^{n+1} → {0,1}^{n+2}, so Σ_y |F_{x,u}(y)| = 2^{n+1} and **E_y|F_{x,u}(y)| = 1/2**. With multiplicity ≤ 2k this gives **E_y|Φ_u(y)| ≤ k** — negligible against 2^{n+1}. So an individual free input is almost never blocked; the difficulty is entirely in the **max over v**.

**(b) The crux is not a nuisance — it is the theorem, and this is the reframing I am registering.** "Some v lies in Φ_u(y) for **every** free u" says precisely that the hint forces v ∉ range(C): the template **certifies** v, i.e. it works as a reduction on that hint. Therefore

> **13a ⟺ every depth-1 template admits a hint (with forced values) that is NON-CERTIFYING; 13b ⟺ some template's every valid hint certifies.**

The max-over-v obstacle is not in the way of the proof; **it is the dichotomy itself**. That is why (iv) cannot be finished by averaging: averaging bounds total mass, and certification is a statement about concentration.

**(c) I verified the reviewer's successor example.** For C′(x) = (C(x), C(x+1)₁) and hint (z,c): at a free u, x = u contributes {z} only if C(u+1)₁ = c, and x = u−1 contributes {v : v₁ = c} only if C(u−1) = z. Setting C(u+1)₁ = ¬c and C(u−1) ≠ z at the forced neighbours empties Φ_u for every free u. **The example works, and it works because every "other input" of a 1-free x is forced** (immediate from f_x ≤ 1), so the adversary controls all of them.

**(d) What I have NOT done:** whether the neighbour-conflict CSP is always solvable. A forced input w can be an "other input" for many x's, and the multiplicity cap was imposed only when **choosing U_free**, not on forced inputs — so a forced w may be read by very many x's, each constraining it. **That is the open step and it is where 13a is won or lost.**

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **13a** proved in full generality | 35 | **25** |
| **13b** a depth-1 template with arbitrary glue that is a total reduction | 15 | **15** |
| **13c** obstruction named, with the exact resisting family | 50 | **60** |

**Why I am below the reviewer on 13a.** §2(b) says the remaining step is not a clean-up but the entire content, and §2(d) says the CSP that would discharge it is unconstrained precisely where the construction placed no cap. **Every previous round closed because a device made the constraint a product or a single forbidden value; here the constraint couples forced inputs across many x at once, and no previous device addresses that.** Rounds W8–W12 each closed a family whose structure I could see before attacking; this one I cannot.

**Why I match on 13b.** The successor template is not a reduction (§2c), and every concrete template tried since W7 has fallen. But Miles–Viola's Theorem 1.3 shows that on the PRG side **rich post-processing does buy a non-adaptive construction** where projections cannot, and arbitrary glue with k = poly(n) is exactly "rich". That is suggestive, not binding — Avoid demands total correctness, not indistinguishability (W7's obstruction) — so 15, not higher.

## §4. Flags

- **Flag Z13 — the standing bias.** Twice now I predicted cross-input coupling would be harder than it is. **If I find myself predicting that the neighbour conflicts are fatal, I must test it before believing it**, at n = 3 and 4 by exact GF(2)/brute force.
- **Flag A13 — the multiplicity asymmetry is the suspected obstruction.** U_free is drawn among inputs of multiplicity ≤ 2k; forced inputs carry no cap. If a family resists, I expect it to be one where a few forced inputs are read by Θ(N) many x's, each demanding an incompatible value. **That family is the 13c deliverable.**
- **Flag B13 — a 13b candidate must be checked for totality over ALL valid hints**, by hand and by brute force at n = 3, 4. "It certifies on the hints I tried" is not 13b.

## §5. Kill tests

- **(i)** Definition 9 / Theorem 12 DNF model only; no value queries.
- **(ii)** Determinism in every statement (Flag H7), and the ceiling restated with any 13a.
- **(iii)** The successor template and one two-to-one-call template checked by hand.
- **(iv)** Every constant with its comparison bound beside it; |U_free| = N^{1−δ} tracked against qw explicitly.
- **(v)** Consistency: W12.1 must be the k = 1 special case; if the general argument beats it there, something is wrong.
- **(vi)** Exact vs sampled labelled.
- **(vii)** If the CSP step does not close, name the exact resisting family — do not report "obstruction" without a template.
- **A prior wrong is said in the same sentence as the finding.**

---

*Findings follow below, appended after the attack. Nothing above is revised retroactively.*
