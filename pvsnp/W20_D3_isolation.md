# W20: (D3) by isolation -- can a deterministic sample isolate the seed? Pre-registration

*Drafted 2026-09-12 on branch `w20-history-hardness`, on the reviewer's sharpened W20 specification. Documents only; `formal/` closed; LOCAL commit only, no push.*

**Committed BEFORE reading any primary for this round.**

## §0. Relation to `fd081c1`, stated first because it is a protocol point

I opened W20 on the reviewer's one-line announcement at the close of W19 and committed priors at **`fd081c1`** (`pvsnp/W20_history_hardness.md`, codes 20a 12 / 20b 53 / 20c 35) **before** its full specification arrived. That page stands: its codes were mine, its contamination declaration is still in force, and it was committed before any primary was read.

**The reviewer's codes are different propositions, not a re-labelling of mine**, so they are priced separately here rather than retro-fitted:

- My `fd081c1` **20a** was broad -- "a candidate notion is produced and both halves are checked". I priced it **12**, arguing it was *not* breakthrough-ceilinged.
- The reviewer's **20a** is narrow and specific: *a deterministic isolating `J` exists for the encoded GGM family by structure alone*. **That is the door** -- it would make the reconstruction `FP^NP`, hence `Avoid ∈ FP^NP` unconditionally, hence by Korten's Theorem 10 a near-maximum `E^NP` circuit lower bound unconditionally.

**So my 12 was right for my proposition and would be wrong for the reviewer's**, and I am saying so rather than quietly carrying the number across. The reviewer's 20a is breakthrough-ceilinged and priced accordingly below.

## §1. The target, and the two variants kept apart

RW26 §5's question, verbatim, as on the W19 page:

> "Let `Π` be an encoded computational history, then either `Π` is 'hard enough' to solve AVOID, or `Π` is 'easy' so that one can 'reconstruct' `Π` efficiently. **Is there a suitable definition of 'hardness' so that any 'hard enough' `Π` can be used to solve AVOID in `FP^NP_tt`, while `Π` being 'easy' implies an efficient MA algorithm for reconstructing `Π`?**"

**(D3-RW)** hard ⇒ `FP^NP_tt`; easy ⇒ **MA** reconstruction. *(Their target, giving `prMA_E`.)*
**(D3-door)** hard ⇒ `FP^NP` (adaptive allowed); easy ⇒ `FP^NP` reconstruction. *(The door.)*

**Kept apart throughout.** W16.2 bites on (D3-RW)'s "hard ⇒ `FP^NP_tt`" step from plain hardness; (D3-door) is not subject to it, because Korten's adaptive algorithm is exactly what relativizes.

**The attack (the reviewer's, adopted).** Choose the easiness notion Korten already supplies: **easy** := `Π ∈ Range(GGM[G])`, i.e. `Π = tree(seed)`; **hard** := not. Then (1) hard ⇒ Korten solves Avoid adaptively, which is fine for (D3-door); (2) easy ⇒ the description *is the seed*, and "`∃` seed with prefix `p` such that `GGM(seed)` agrees with `Π` on positions `J`" is an NP query for `|J| = poly`. The reconstruction reads `Π` at `J` and prefix-searches the lexicographically first consistent seed, in `FP^NP`. **It is correct iff `J` isolates the true seed.**

> **So (D3-door) reduces to:** find, deterministically with an NP oracle and polynomially many positions, a set `J` on which `seed ↦ GGM(seed)|_J` isolates the true seed at `Π`.

## §2. Disclosure

**(a) Contamination, still declared, and the reviewer has ruled it stays.** W19's PATH line already records my prior that (D3) lands on the plain-vs-SVN wall, because NP-certifiable easiness wants a short certificate for a statement whose natural certificate is a circuit. The reviewer ruled: keep it as labelled, a prior to be scored; **if the round lands there it is a sixth arrival, and that is itself the finding.** Flag E20 stands -- the write-up must say whether the round *found* the wall or *steered* to it.

**(b) The reviewer's expected wall, recorded as its prediction, not mine to inherit.** It expects the obstruction at its route (ii): choosing a position that kills a constant *fraction* of consistent seeds requires counting them, which is approximate counting -- **(D1)** -- or hashing, which is **SVN**.

**(c) My one independent thought, disclosed before pricing because it is the reason my 20c is above the reviewer's.** `GGM` is a **tree**, and the seed is read along a root-to-leaf structure. The set of seeds consistent with `Π` on `J` may therefore be describable by **prefix constraints**, in which case a differing position could be located by **prefix descent with adaptive NP queries** -- which is permitted in (D3-door) and is exactly Korten's own technique -- rather than by counting or hashing. If that works it is neither 20a (not "by structure alone", it uses the oracle adaptively) nor 20b (no counting, no hashing, no randomness). **I have not checked it; it may be trivially wrong; it is registered so it can be scored.**

**(d) Not done -- no primary read for this round.** Not yet consulted: RW26 Theorem 3.1's "easy" output (whether the circuit of size `O(|G| log T)` is the tree with the seed hardwired); RW26 §3-§4 on the encoded history and its distance property; CHR §1.3.2's easy-witness argument; exact-learning-with-NP-oracle results 2023-2026; ECCC for this specific question.

## §3. Priors, fixed now

| code | outcome | reviewer | **mine** |
|---|---|---|---|
| **20a** a deterministic isolating `J` exists for the encoded GGM family **by structure alone** -- `FP^NP` reconstruction, and the door | 3 | **4** |
| **20b** sixth arrival, with the exact step named: isolating the true seed among seeds consistent on a poly-size sample needs approximate counting, hashing, or randomness | 62 | **58** |
| **20c** other | 35 | **38** |

**Why 20a is 4 and not 12.** §0: the reviewer's 20a *is* the door, so it inherits the breakthrough ceiling that 17a and 18a had, not the design-question ceiling my own 20a had. I put it a hair above the reviewer's 3 for one reason only: this is a **construction** question about a **highly structured** family, and structured families do sometimes admit deterministic isolation where generic ones do not (algebraic codes being the standard example). My constructions are the reliable half of my output. That is worth one point, not ten.

**Why 20b is 58, below the reviewer's 62.** It is the impossibility-shaped outcome, and that is the category in which I have been wrong **ten consecutive times**. I hold the belief (§2(a)) and I am discounting it *because* I hold it. **This is the same discipline as W18's calibration move, applied in the same direction, and I flag that repetition as itself a risk** -- a rule applied mechanically stops being calibration.

**Why 20c is 38, above the reviewer's 35.** Not reflex. §2(c) is a specific, named third possibility -- prefix descent exploiting the tree structure, adaptive, permitted in (D3-door), neither "by structure alone" nor counting/hashing. W17 taught me not to inflate this bucket on vague grounds; W18 taught me not to over-correct mechanically. **A named mechanism is the only thing that earns points here, and I have exactly one.**

## §4. Flags

- **Flag A20 -- the asymmetry is applied, not noted.** The tension claim (20b) gets the harder audit, because of the ten-for-ten record.
- **Flag B20 -- verbatim with numbers; content-search when a label fails.** The W19 method line, now vindicated twice over: the SU05 learner is **Thm 3.16 (CCC'05 conference) / Thm 4.10 (journal, §4.6)** -- a **version split**, not a transcription error by either of us, and it is cited in both forms from here.
- **Flag C20 -- both constraints checked on every candidate.** **W16.2**: does it relativize and follow from plain hardness? Then dead for (D3-RW). **W18.1**: does the easy branch secretly need a hard string? Then circular. **And keep (D3-RW) and (D3-door) apart** -- W16.2 bites only on the former.
- **Flag D20 -- stop-rule, binding.** If 20a appears to close, stop, send exact parameters, write nothing further. It is the door.
- **Flag E20 -- score against §2(a).** Found, or steered? Answer explicitly, and say what would have distinguished them.
- **Flag F20 -- the isolation question is about the TRUE seed, not injectivity.** "Isolates" is weaker than "`seed ↦ GGM(seed)|_J` is injective", and the weaker requirement is the one that matters. Do not prove the harder statement impossible and call the question closed.

## §5. Kill tests

- **(i)** RW26 Theorem 3.1's "easy" output verified in the source -- is it the tree with the seed hardwired? The whole attack rests on the description *being the seed*.
- **(ii)** The encoded history's **distance property** quoted verbatim, since route (i)'s union bound needs "wrong seeds disagree on a constant fraction".
- **(iii)** Every candidate `J`-construction checked against Flag C20, and (D3-RW)/(D3-door) never conflated.
- **(iv)** ECCC 2023-2026 swept before writing "open".
- **(v)** §2(c) actually tested, not left as a registered hunch -- if it fails, say so in the same sentence as the finding.
- **(vi)** If the resolution is not the pre-registered one, say so in the same sentence as the finding.
- **(vii)** Flag E20's steering question answered whatever the outcome.

---

*Findings follow below, appended after the work. Nothing above is revised retroactively.*

---

# Findings

*Appended 2026-09-12 after reading the primaries. Nothing above this line is edited.*

**Outcome: 20b, on a crux that is not the one the round opened with. The isolation framing collapsed; the round is about CERTIFICATION. Flag D20 did not fire.**

## §6. The framing collapsed: the reviewer's route (2) has an empty premise

The attack assumed the reconstruction "reads `Π` at `J`". It cannot read `Π` anywhere. Two statements, verbatim:

> "`Recon_f(x, i)` takes `x ∈ {0,1}^n` and `i ∈ [t(n)]` as input, runs in **deterministic `poly(k(n), r(n), log t(n))` time** with access to a prMA oracle `Π_f`, and outputs a bit. *(As a minor remark, `Recon_f(x, i)` does not need access to the bad AVOID instance `G`.)*"

> "an algorithm `Recon_i(j) := Recon^{f_i}(x_0, j)` that runs in deterministic `poly(n_{i+1}, r_i, log T_i)` time"

against the cost of one bit: `f_i` "outputs the `2^{n_i}`-bit string produced by `BF_i` on `G_{n_i}`", and "`BF_i` runs in `TIME[T_i]^NP`", with `T_i := max{2^{cD^i n_0}, n_{i+1}}`.

> **One bit of `Π` costs a run of `BF_i`, time `~T_i = 2^{Θ(n_i)}`. The budget is `log T_i`.** The reconstruction cannot afford a single bit, at any `J`.

**And this is not an accident of parameters — it is what "reconstruction" means.** If bits of `Π` were readable there would be nothing to reconstruct. The Jeřábek-Korten reduction of Theorem 3.1 *does* hold `f` (it runs in `poly(T, |G|)`); `Recon` is precisely the part that does not.

**Consequence.** "`Π ∈ Range(GGM[G])`" cannot be exploited by prefix search over seeds with consistency checks on a sample, because there is nothing to be consistent *with*. The membership-query learning framing is void. **The only handle on `Π` is its definition**, and the round is about whether that definition can be certified.

*(A second defect in the same route, recorded because it was mine to catch and I caught it before the collapse: the reviewer wrote that constant-fraction disagreement between wrong seeds is "what RW26's encoded (error-corrected) history guarantees". It is not. The distance property is **Theorem 3.4's PCP soundness**, a property of the Reed-Muller encoding of the witness. The GGM range is a different object: `G` is an arbitrary circuit, need not be injective, and the tree map carries no distance guarantee at all. Had the premise survived, this would have sunk route (i) separately.)*

## §7. The certification requirement, computed at named parameters

Each of the `r'(n) = O(r(n) log t(n))` rounds asks one prMA query. Verbatim:

> "Merlin provides a circuit `C : {0,1}^{log |Π_x|} → {0,1}` of size at most `k'(n)`."
> "Arthur samples randomness `z ← O(log t(n))` (for the PCP verifier) **and `z_Corr ← {0,1}^{polylog(t(n))}` (for the Low-Degree Self-Corrector)**."
> "`k'(n) := O(k(n)^4 log t(n))`"
> "the size of each query `q_pfx` and `q_{pfx,i}` is also upper bounded by `poly(k(n), r(n), log t(n))`"

**Correction to the reviewer's item (1), and it cuts against it.** It computed `m = O(log t)` coins. The text has **two** randomness sources, and the self-corrector's `polylog(t)` **dominates** the verifier's `O(log t)`. So

> **`m = polylog(t)`, and the seed space is `2^{polylog(t)}` — quasi-polynomial in `t`, against a budget `poly(k, r, log t)`.**

Enumeration is not merely over budget; it is *further* over budget than the reviewer's own estimate of `2^{m(1-δ)} = t^{1-δ}`. No hypothesis of the Williams non-trivial-savings shape reaches it.

**The requirement, stated exactly and in its own terms** (rather than by invoking an equivalence I have not verified):

> **(CERT)** A deterministic algorithm that, given the circuit `z ↦ V^C(x, z)` of size `S = poly(k, r, log t)` on `m = polylog(t)` input bits, decides whether `Pr_z[accept] = 1` or `Pr_z[accept] ≤ 1/2`, in time `poly(S)`.

Note `m` and `S` are both `polylog(t)`, hence polynomially related: this is the general acceptance-probability problem for this family, in **polynomial** time — not a non-trivial-savings statement.

**Why Flag Q17's old verdict does not transfer, and this is the round's transferable lesson.** In W17 I withdrew the self-corrector as an obstruction, *correctly*: against a **fooling** requirement it is free, because the PRG guarantee is per-circuit and universally quantified over size-`S` circuits, so the per-point majority needs no union bound. Against an **enumeration** requirement it is *not* free, because its coins must be fixed too.

> **Practice line: name the scarce resource before ruling on a component.** The same component, in the same construction, is free against fooling and dominant against enumeration. This is "succinctness cuts both ways" a second time, from the opposite side, and I have now earned it twice.

## §8. The derandomised-PCP escape is closed by counting

The reviewer asked whether the PCP's randomness could be made logarithmic in the proof's **succinct description** rather than its length, so that `2^m` fits the budget. It cannot, and the argument is arithmetic rather than bibliographic:

> A non-adaptive PCP verifier with `r` coins and `q` queries reads at most `q · 2^r` distinct proof positions **across all seeds**. Any position never queried under any seed can be set adversarially by the prover. Hence the effective proof length is at most `q · 2^r`, i.e. **`r ≥ log(proof length) − log q`**.

With `|Π| = poly(t)` this forces `m = Ω(log t)` **regardless of how succinctly `Π` is described** — succinctness does not shrink the set of positions soundness must cover. The literature sweep corroborates the same bound in the same words ("the proof length is always at most `q(n) · 2^{r(n)}`") and adds that sub-constant error drives randomness *super*-logarithmic, i.e. the wrong way. **No derandomised-PCP hatch exists.**

## §9. The two sources of such an algorithm, both closed

- **(a) A hard string from inside the win-win — closed by Theorem W18.1.** The reconstruction runs *exactly* in the branch where `BF_{i+1}` fails, i.e. where the residue is easy. The residue is easy precisely when its randomness is needed.
- **(b) A plain-hardness hypothesis — closed by Korten dominance.** Since `E ⊆ E^NP`, any IW97-strength hypothesis (Shaltiel-Viola's rendering: "functions computable in time `2^{B·n}` that cannot be computed by circuits of size `2^{β·n}`") already yields `E^NP` hardness, hence `Avoid ∈ FP^NP` directly by Korten's Theorem 10 — making the reconstruction unnecessary. RW26 §5 states the dominance themselves: "the assumption that `E^NP` requires exponential size circuits **(not SVN circuits!)** implies an `FP^NP` algorithm for AVOID; moreover, this is provably the minimum assumption."

**So the sixth arrival is of a NEW shape.** Not the plain-vs-SVN boundary of arrivals one through five, but: *the reconstruction's certification is a polynomial-time derandomisation of a PCP verifier, whose only known sources are a hard string the branch lacks or a hypothesis the door already implies.*

## §10. The structural finding is W4's, not W20's

The reviewer asked me to record "two doors are one" as this round's structural finding. **I checked its own branch before recording it, and it is already there, dated 2026-09-11.** W4 §2, verbatim:

> "each of the `O(r log t)` prMA queries of the reconstruction asks whether there is a circuit `C`, of size at most `s`, that succinctly encodes a PCP proof `Π_C` of the recursion's computational history with the correct prefix, which the PCP verifier accepts; Merlin sends `C`, Arthur runs the verifier on random seeds. An NP query would need Arthur's random check replaced by a deterministic one, i.e., a Gap-UNSAT decision for the circuit `seed ↦ V^{Π_C}(seed)` — the algorithmic method's object again (W2), **in polynomial time rather than merely non-trivially**. That is the sense in which W2's door and W4's door are one door."

And W4 had already closed source (b), in the same round:

> "any hypothesis that derandomizes the prMA queries by way of a plain-circuit lower bound for E or E^NP is dominated: it already yields FP^NP for Avoid through Korten's Theorem 10 without passing through Ren-Williams' algorithm at all."

**So W20 confirms rather than discovers, and the page says so.** What W20 adds that W4 could not have had: the demolition of the isolation framing (§6); the coin count `m = polylog(t)`, which upgrades "in polynomial time rather than merely non-trivially" to a *quantified* quasi-polynomial gap (§7); the counting closure of the derandomised-PCP hatch (§8); and **Theorem W18.1 closing source (a)**, which postdates W4 by eight rounds. W4 left the step as "can only be (a) taken unconditionally by a better algorithm, or (b) implied by hypotheses of a different kind"; W20 closes the in-framework version of (a).

**Recording it this way is the point of the exercise.** I caught the reviewer attributing SU05's learner to the wrong theorem number two rounds ago; attributing its own finding to my round would be the same error with the sign flipped.

## §11. CHR's side of the same obstruction

CHR §1.3.2 gives the other face, and names it themselves:

> "In some sense, `V_History` is a **local Π₁ verifier**: it is local in the sense that it only queries `poly(n)` bits from its oracles, and it is Π₁ since it needs a universal quantifier over `x ∈ {0,1}^{poly(n)}` to perform all the checks."

The history has a **local characterization** — constraints `{ψ_x}` each reading `poly(n)` bits, such that "for fixed `f`, `History(C, f) ∘ f` is the **unique** string making all the `ψ_x` outputting 1" — with the two universally quantified constraints being (3) "for every `z ∈ {0,1}^n`, `C(z) ≠ v_{i*+1,2j*} ∘ v_{i*+1,2j*+1}`" and (5) the lex-first condition. Their easy-witness argument then works "since all the `C_t` have size `poly(n_i)`, each check above can be implemented in `poly(n_i)` time as they only read at most `poly(n_i)` bits from their input, despite that `tt(C_{t+1}) ∘ tt(C_t)` itself can be much longer than `poly(n_i)`."

That buys **Σ₂** (`∃C ∀x`), which is why CHR land in `FΣ₂P` and need selectors for `FS₂P`. **Removing the `∀` to reach `FP^NP` is exactly the verifier's derandomisation.** So `V_History` and `V^C` are one obstruction seen from two sides.

## §12. Scoring

| code | mine (ecf5475) | reviewer (final) | outcome |
|---|---|---|---|
| **20a** | 4 | 3 | **Did not fire.** Flag D20 never armed: the isolation route died on an empty premise rather than closing. |
| **20b** | 58 | 65 | **The outcome**, on the certification reading — sixth arrival, of a new shape (§9). |
| **20c** | 38 | 32 | **No credit.** §13. |

*(The reviewer's pre-audit 3/62/35 is superseded by 3/65/32 at its request; both recorded.)*

**My `fd081c1` set (20a 12 / 20b 53 / 20c 35), on the broader codes**, scores the same way: 20b, and the 12 was correctly *not* breakthrough-priced for that proposition.

## §13. Calibration, and a new failure mode

**20c got no credit, and the reason is instructive.** I priced it at 38 — above the reviewer's 35 — on the strength of one named mechanism: prefix descent exploiting the GGM tree's prefix structure. That mechanism was **never tested on its merits**. It was aimed at the isolation crux, and the isolation crux turned out not to exist. Re-read against certification (the reviewer's item (4)), it does not bypass §7 either: `Recon` *already is* a prefix search — `r'(n)` rounds maintaining `pfx` — and every round's `q_pfx` still requires Arthur's probabilistic check. Descent finds `C` bit by bit, but each bit costs one undischarged MA query.

> **New line: a mechanism can die by having its framing removed, not by being refuted.** Twice now I have inflated the "other" bucket on the strength of a named mechanism (W17's 38 against 27; W20's 38 against 32), and both times the mechanism was invalidated by the framing collapsing rather than by being wrong. **A named mechanism is not evidence for the bucket unless the framing it lives in has itself been audited.** W18's move in the opposite direction (32 against 38) paid; the correct reading of all three is not "always go low" but that the framing audit must come *before* the mechanism is priced.

**Flag E20, answered against myself.** My W19 PATH prior said (D3) would land on the plain-vs-SVN wall "because NP-certifiable easiness demands a short certificate for a statement whose natural certificate is a circuit — which is where both SU05's equivalence queries and RW26's Merlin sit." **Half right, and the half that was right is not the half that mattered.** The certificate *is* a circuit and Merlin *does* sit there — but it does not reduce to SVN hardness; it reduces to CAPP for the verifier, a different object with a different literature. **So I did not steer the round to my predicted wall: it went somewhere I had not named.** Right about where the difficulty lives, wrong about which wall it is.

**Flag F20 is moot**, and I record that rather than quietly dropping it: "isolates the true seed" versus injectivity was a real distinction, but the isolation question itself is void by §6, so the flag never came into play.

**The impossibility-claim record is unchanged at ten** — this round produced no new wrong impossibility claim of mine. It produced one wrong *positive* registration (the 20c mechanism), which is a different category and the first of its kind; but it died of framing collapse rather than refutation, so it is weak evidence either way, and I am not adjusting the standing line on it.

## §14. What this leaves open

1. **(CERT) itself** — a polynomial-time acceptance-probability algorithm for `{V^C : |C| ≤ k'}` on `polylog(t)` coins. Open, and by §10 it is the algorithmic route's currency, so progress there is progress here.
2. **(D3-RW)**, kept separate throughout: with **MA** reconstruction the framework is RW26 as it stands, and nothing in this round disturbs it. Only the `FP^NP` variant (D3-door) is closed off by §7-§9.
3. **Whether `E^NP` plain hardness implies (CERT)** — not established anywhere read here, and the known AM-type derandomisations go through nondeterministic/SVN hardness (W4 §3, and RW26's own `searchSAT` remark). This is the one place arrivals one-through-five and arrival six might meet.
