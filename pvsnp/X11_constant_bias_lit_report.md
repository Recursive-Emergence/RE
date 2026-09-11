# X11-lite: the constant-bias lemma, as a bounded literature check. Report

*Run 2026-09-11 on branch `x11-lite`, on the author's go ("Run it, push after merge"), against the pre-registration (c49e54b). The reviewer accepted it with these terms:*
- *priors X11c 55 / X11b 40 / X11a 5;*
- *Flags A and L as expectations to verify under g8;*
- *Flag R as a proved partial with the exact chain, one search for a stated source, and the open window named exactly.*

*Documents only, plus one exact smallest-case computation (`x11_small.py` in the job's scratch directory). `formal/` closed. Sources read as text this run:*
- *Hambardzumyan–Hatami–Hatami (HHH), ECCC TR21-066;*
- *Pitassi–Shirley–Shraibman (PSS), ITCS 2023 (local `pss.txt`);*
- *Chattopadhyay–Lovett–Vinyals (CLV), ECCC TR18-206 (local `clv.txt`);*
- *Balla–Hambardzumyan–Tomon (BHT), arXiv 2506.23989;*
- *Göös–Harms–Riazanov, arXiv 2507.11162;*
- *Harms–Riazanov, arXiv 2410.00838.*

*The X8 practice applies: smallest case first, and the compared bound beside every number.*

## 0. Outcome

**Proposed: X11c. The recorded regime is m ≥ n/2 − log₂(1/c), and nothing in the literature closes the window, so the program pauses as under X11b.** The reviewer rules the code.

**1. Flag R is proved as ruled (§2), but it is superseded.** A second chain is sharper and elementary:
- |Adv(IP2, C)| ≤ γ₂(C)·2^{1.5n} ≤ 2^m·2^{1.5n} (§3), proved two ways.
- It gives **m ≥ n/2 − log₂(1/c)** at bias c·4^n, against Flag R's m·log m ≥ Ω(n).
- The key inequality is stated in the literature: log γ₂(M) ≤ D^EQ(M) (BHT §2.1, attributing it to HHH23).
- **It is X5's Lemma S / T′ mechanism read at the constant-bias scale.** So the pre-registered window's lower end, n/log n, was below what the program already had. This is my miss, as the author of Flag R and of the window.

**2. The window, exactly:**

  **n/2 − log₂(1/c) ≤ m*(n, c) ≤ 2^n** for c ≤ 1/2 − 2^{−n}.

Here m*(n, c) is the least m such that some conjunction of m co-blocky constraints has |Adv(IP2, C)| ≥ c·4^n.
- **The lower end is the end of the γ₂/discrepancy method.** Identity-encoded NEQ^m already has γ₂ ≥ (2 − 2/k)^m (§5), so a bound through γ₂(C) alone cannot improve it by more than a constant factor.
- **The upper end is an explicit construction** (§4).
- The constant-bias lemma asserts m* ≥ 2^{Ω(n)}. That is known only near purity (Z1/Z2, m ≥ √N/8).

**3. The checks:**
- **Flag A is confirmed, in a sharper form.** C already *has* an explicit 2^m-term blocky decomposition, so HHH's structural statements, which produce such decompositions in the bounded regime, add nothing.
- **Flag L is confirmed.** No lifting theorem addresses correlation of a *cheap class* with a fixed function. The encoding-invariant tool that does exist (γ₂) is exactly the lower-end bound.

## 1. Smallest cases first (exact; `x11_small.py`)

Maximum |Adv(IP2, C)| over all conjunctions of m co-blocky constraints, found by exhaustive enumeration of the distinct blocky sets:

| N | blocky sets | m | max \|Adv\| | vs bound 2^m·N^{1.5} | vs N² | relative bias |
|---|---|---|---|---|---|---|
| 2 | 12 | 1 | 3 | 5.7 | 4 | 0.750 |
| 2 | 12 | 2 | 3 | 11.3 | 4 | 0.750 |
| 2 | 12 | 3 | 3 | 22.6 | 4 | 0.750 |
| 4 | 2100 | 1 | 8 | 16.0 | 16 | 0.500 |
| 4 | 2100 | 2 | 10 | 32.0 | 16 | 0.625 |
| 4 | 2100 | 3 | 10 | 64.0 | 16 | 0.625 |

- The bound of §3 holds at every entry, with slack. At N = 2 the AND mask reaches 3 = 3^n, the DISJ value.
- At these sizes constant bias is reached with m = 1–2, consistent with the lower end n/2 − O(1) (0.5 and 1 here).
- The smallest cases say nothing about the exponential claim, as the X9 practice note already records.

## 2. Flag R, as ruled: the fingerprinting chain (proved; folklore-shaped)

**Setting.** C = NEQ^m ∘ (F, G) = {(x, y) : f_j(x) ≠ g_j(y) for all j ≤ m}. H is the IP2 sign matrix, N = 2^n, and Adv(IP2, C) := ⟨H, 1_C⟩.

1. **Protocol.** Use public random functions h_j : Σ → {0,1}^k. For each j, Alice sends h_j(f_j(x)), and Bob sends one bit saying whether it equals h_j(g_j(y)). The protocol outputs 1 iff all m tests report "different".
   - Cost: c = m(k + 1).
   - Error is one-sided: it can only output 0 on C, when a hash collides. Pr[error] ≤ m·2^{−k} ≤ δ for k = ⌈log₂(m/δ)⌉.
2. **The discrepancy method** (the version used here, with constants). For each fixing r of the randomness, π_r is a deterministic cost-c protocol, and its 1-set is a disjoint union of ≤ 2^c rectangles.
   - By Lindsey, |Σ_R H| ≤ √(N·|R|) ≤ N^{1.5} for every rectangle R.
   - So |⟨H, 1_{π_r=1}⟩| ≤ 2^c·N^{1.5}, i.e. Disc_U(IP2) ≤ 2^{−n/2} normalised by N².
3. **Averaging.** 1_C = E_r[1_{π_r=1}] + e with 0 ≤ e(x, y) ≤ δ, so |⟨H, 1_C⟩| ≤ max_r |⟨H, 1_{π_r=1}⟩| + δN² ≤ 2^{m(k+1)}·N^{1.5} + δN².
4. **Constant bias.** Take |Adv| ≥ c₀N² and δ = c₀/2. Then 2^{m(⌈log₂(2m/c₀)⌉+1)} ≥ (c₀/2)·2^{n/2}, so **m·(log₂(2m/c₀) + 2) ≥ n/2 − log₂(2/c₀)**, i.e. m·log m ≥ Ω(n). ∎

**Label: folklore-shaped.** The simulation step is stated in CLV ("P^EQ ⊆ BPP"; CLV p. 2). The discrepancy step is the standard discrepancy method. The combination is ours-elementary.

**The single search** (the reviewer's "search once"). It found no source stating this chain for correlation. It did find a stated source for the *sharper* inequality used in §3: BHT §2.1 states "log γ₂(M) ≤ D^EQ(M) ≤ D(M), where the first inequality is proven in [HHH23]". HHH's ECCC text proves the blocky-norm form, ½·log‖M‖_Blocky ≤ D^EQ(M) (Proposition 3.1).

## 3. The sharper partial (proved two ways; supersedes Flag R)

**Claim.** For every conjunction C of m co-blocky constraints, **|Adv(IP2, C)| ≤ 2^m·N^{1.5} = 2^{m + 1.5n}**. At bias c·4^n this forces **m ≥ n/2 − log₂(1/c)**.

**Derivation 1 (inclusion–exclusion; elementary).**
- 1_C = ∏_j (1 − 1_{q_j}) = Σ_{S⊆[m]} (−1)^{|S|}·1_{B_S}, where B_S = ∩_{j∈S} q_j.
- Each B_S is blocky: B_S = {(f_j(x))_{j∈S} = (g_j(y))_{j∈S}}, with B_∅ = J.
- For a blocky B = ∪_t A_t × B_t, with the A_t disjoint and the B_t disjoint, Lindsey and Cauchy–Schwarz give |⟨H, 1_B⟩| ≤ Σ_t √(N·|A_t|·|B_t|) ≤ √N·√(Σ_t|A_t|·Σ_t|B_t|) ≤ N^{1.5}.
- Summing the 2^m terms gives the claim. ∎

**Derivation 2 (γ₂ duality).**
- |⟨H, M⟩| ≤ γ₂(M)·γ₂*(H), and γ₂*(H) ≤ N·‖H‖ = N^{1.5}, by Cauchy–Schwarz on the dual (Linial–Shraibman's standard bound).
- γ₂ is Schur-submultiplicative: it is the Schur-multiplier norm, and HHH's "‖M₁ ∘ M₂‖_m ≤ ‖M₁‖_m·‖M₂‖_m" together with their Theorem 1 gives this.
- Blocky matrices have γ₂ ≤ 1 (the contractive idempotents, Livshits, as quoted in HHH §1). So γ₂(J − q_j) ≤ 2 and **γ₂(C) ≤ 2^m**.
- This also follows from BHT's stated log γ₂ ≤ D^EQ, since D^EQ(C) ≤ m. ∎

**It was already in the program.** X5's Lemma S (Adv(f, blocky) ≤ 4K_G·4^n·d), applied to the 2^m inclusion–exclusion terms, is Lemma T′'s mechanism. At bias c·4^n it gives m ≥ n/2 − O(1) with a K_G constant; the Lindsey form above removes that constant for IP2.

**The comparison with the other chains (the same bias c·4^n):**

| chain | bound on \|Adv\| | forced m |
|---|---|---|
| §3 (γ₂ / inclusion–exclusion) | 2^m·N^{1.5} | **n/2 − log₂(1/c)** |
| §2 (fingerprinting, Flag R) | 2^{m(log₂(2m/c)+2)}·N^{1.5} | Ω(n/log n) |
| CLV Lemma 3.2 + Lindsey | ≤ 2^{1.5n}·(2n)^{2m} (P^EQ ⊆ P^GT at 2 calls per query, then perimeter p ≤ 2^{n+1}(2n)^{2m}, then Σ√(N·r·c) ≤ √N·p/2) | Ω(n/log n) |

## 4. The upper end: an explicit construction (exact)

- Take q_j = {j} × {y : H_{jy} = +1} for each row j ∈ [N]. Each is a single rectangle, hence blocky.
- Then C = ∩_j (J − q_j) is exactly the −1 class, with |Adv| = (N² − N)/2, i.e. relative bias 1/2 − 1/(2N), at m = N.
- So m*(n, c) ≤ 2^n for c ≤ 1/2 − 2^{−n}.

Near purity (within ε ≤ 1/(8m) of a whole sign class), Z2 gives m ≥ √N/8. **The constant-bias lemma is the claim that the lower end jumps from n/2 to 2^{Ω(n)} already at constant, non-pure bias.**

## 5. The checks

**(a) Hambardzumyan–Hatami–Hatami** (ECCC TR21-066; text read). Three statements are relevant.

| statement | what it says | why it stops here |
|---|---|---|
| **Proposition 3.1** (theorem) | ½·log rk(Blocky, M) ≤ D^EQ(M) ≤ rk(Blocky, M), and ½·log‖M‖_Blocky ≤ D^EQ(M) | For C it gives ‖C‖_Blocky ≤ 2^{2m}, a *weaker* form of the 2^m decomposition of §3. |
| **Conjecture III** (open) | Σ\|λ_i\| ≤ c over rank-one Boolean terms ⇒ M is a ±1-combination of ≤ k_c blocky matrices | Dimension-free, with c = O(1). Our C has γ₂ up to ≈ 2^m, and it already has an explicit ±1-combination of 2^m blocky matrices. So even a proof would add nothing. |
| **Theorem 4** (theorem) | R¹(M) ≤ c ⇒ an all-0 or all-1 δ_c·n × δ_c·n submatrix | The monochromatic submatrix is monochromatic for C, not for H. A C-rectangle R of that size has \|Σ_R H\| ≤ δ_c·N^{1.5} (Lindsey), which gives no bias. And δ_c is dimension-free only for c = O(1), while C's cost grows with m. |

**Flag A: confirmed, and sharper than expected.** The obstruction is not that HHH's structure is unavailable at γ₂ ≈ 2^m. A 2^m-term blocky decomposition is *already explicit*, and using it without cancellation is exactly what caps the method at m ≈ n/2.

**(b) PSS and CLV** (texts read).
- **PSS** characterises covering and partition measures:
  - NP^EQ is characterised by the binary γ₂^∞ and C1B;
  - UP^EQ by γ₂,B (their Theorem 2).
- Its only correlation-type sentence is the γ₂^∞ ↔ discrepancy link for PP^cc, attributed to Linial–Shraibman.
- **CLV's lower-bound technique for P^EQ** is a partition into C-monochromatic rectangles with perimeter ≤ 2^{n+1}(2n)^c (Lemma 3.2, stated for P^GT).
- Neither paper has a correlation bound for Equality-oracle protocols beyond 2^{cost}·disc. CLV's perimeter lemma, turned into a correlation bound, is the weakest row of §3's table.
- The two recent Equality-oracle papers (Göös–Harms–Riazanov 2025; Harms–Riazanov 2024) contain no discrepancy or correlation statement; a grep for "discrepan", "correlat" and "margin" found only reference-list entries.

**(c) Lifting and pattern-matrix (Flag L).**
- Lifting theorems lower-bound the cost of a *specific composed function* f ∘ g^m, through f's query complexity, for a fixed hard gadget g.
- Our question is different in kind: an upper bound on the *correlation* between a fixed hard function (IP2) and a *class* of cheap functions (m-query EQ protocols, i.e. NEQ^m ∘ (F, G) with arbitrary F, G). C is cheap by construction (D^EQ ≤ m), so no lifting statement about C's cost bears on it.
- The encoding-invariant quantity that does exist for this class is γ₂ (or the blocky norm), and it gives exactly §3's lower end.
- *Recalled, not source-checked this run:* the gadgets in the lifting theorems we know of have small discrepancy themselves (Index, IP on Θ(log) bits), whereas EQ's matrix I has γ₂(I) = 1, so EQ is not such a gadget. This line is not used in any conclusion.
- **Flag L: confirmed.**

**(d) NEQ^m under the identity encoding (proved).**
- On Σ with |Σ| = k, identity-encoded NEQ^m is (J_k − I_k)^{⊗m}.
- J_k − I_k has eigenvalues k − 1 (once) and −1 (k − 1 times), so its trace norm is 2(k − 1).
- The trace norm is multiplicative under ⊗, and γ₂(M) ≥ ‖M‖_tr/√(#rows·#cols). So **(2 − 2/k)^m ≤ γ₂(NEQ^m) ≤ 2^m**.
- At k = 2 this is a permutation matrix (γ₂ = 1). For k ≥ 3 it grows exponentially.
- **So the 2^m in §3 is tight up to its base.** A γ₂-only argument cannot push the lower end past (n/2)/log₂(2 − 2/k) = (1 + o_k(1))·n/2.
- **The bias under the identity encoding.** Take IP2 in blocks of b bits and Σ = {0,1}^b. Then Adv = ∏ ⟨H_b, J − I⟩ = ∏ (2^b − tr H_b) = ∏ 2^b = 2^n, since tr H_b = Σ_x (−1)^{|x|} = 0. That is the trivial level (Adv(J) = 2^n): block-Equality, bias ≈ 0. ✓

**Kill tests.**
- **AND (m = n):** Adv = 3^n, against the bound 2^n·2^{1.5n} = 2^{2.5n}. ✓ (The bound is necessary, not sufficient: m = n ≥ n/2 does not produce constant bias, and none is claimed.)
- **Block-Equality:** relative bias 2^{−n}. ✓

## 6. The window, and why both ends are the ends (X11b's closing, as ruled)

**The constant-bias lemma, in NEQ^m-pullback form:** for all encodings F, G, if |Adv(IP2, NEQ^m ∘ (F, G))| ≥ c·4^n then m ≥ 2^{Ω(n)}. **Known:**

  n/2 − log₂(1/c) ≤ m*(n, c) ≤ 2^n.

- **The lower end is the end of the discrepancy/γ₂ method.**
  - Every known tool (§3's three chains, HHH Proposition 3.1, PSS's measures) bounds |Adv(C)| by (number of blocky or rectangle pieces, or 2^{cost}) × (maximum correlation per piece).
  - With per-piece correlation N^{1.5} (Lindsey), this cannot exceed m ≈ n/2.
  - It is tight for the γ₂ route by (d).
  - Moving the lower end requires **cancellation among the 2^m inclusion–exclusion terms**, i.e. using the signs of the Σ_S (−1)^{|S|}·⟨H, 1_{B_S}⟩. None of the sources read has a statement of that kind.
- **The top-side bound applies only near purity.** Z1/Z2, via PSS's covering count, give m ≥ √N/8 when C is within ε ≤ 1/(8m) of a whole sign class.
  - At constant bias that argument fails at the step already named in X10: impure rectangles can hold all the −1 entries once m ≳ 1/c.
  - The upper end 2^n is the construction of §4.

## 7. Priors against outcome

| | X11c | X11b | X11a |
|---|---|---|---|
| reviewer (pre-reg → accepted) | 20 → 55 | 70 → 40 | 10 → 5 |
| mine | 55 | 40 | 5 |
| **outcome (proposed)** | **✓ (regime m ≥ n/2 − log₂(1/c); the literature closes nothing)** | pause, as under X11b | |

**Miss (mine; scoring for the reviewer's ruling).** Flag R and the pre-registered window's lower end (n/log n) were weaker than X5's own Lemma S / T′ mechanism, which gives n/2 − O(1) at constant bias. The window was pre-registered without putting it beside X5's lemma: the "compared bound beside every number" practice, missed at the level of a whole flag.

## Ceiling

X11-lite proves nothing about P vs NP. On this branch, the program's descent ends at the constant-bias lemma in NEQ^m-pullback form, with the window above.

## Formal record

Untouched (the author's decision).
