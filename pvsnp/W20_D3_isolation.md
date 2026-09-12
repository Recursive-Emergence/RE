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
