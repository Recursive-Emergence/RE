# X4: the additive-loss lemma. Pre-registration

*Drafted 2026-09-10 on branch `x4-additive-loss`, on the author's go ("Draft and run X4, push after merge"), for the reviewer's ruling before any work. Documents plus proof sketches; `formal/` stays closed (the author's standing decision). g1, g5, g8 and g9 apply. X4 proves nothing about P vs NP; at best it moves the alternation threshold.*

## Target (the reviewer's, verbatim in content)

Podolskii–Prior 2025, Theorem 45: if Disc_U(f) ≤ d and f is approximately balanced, then every ELDL of alternation depth k computing f has size Ω(k·d^{−1/(2k)}). The per-alternation loss is multiplicative.

- **(a)** Locate the multiplicative step: which inequality, applied to which sub-block, and what it discards. Record it as a numbered step together with the quantity lost.
- **(b) Kill test first.** Is the multiplicative loss *necessary* for blocky discrepancy? Look for a small ELDL of depth k whose blocky discrepancy genuinely decays like d^{1/2k}.
- **(c)** If the loss is not shown necessary, try one repair: a *global potential*, a sum over layers of a blocky quantity rather than a product. Name the first step where it fails to control the next layer.
- **(d)** Quote Podolskii–Prior's "no strong lower bounds are known" remark, with its scope.

## Flags raised before any work (mine)

**Flag K (a concrete kill candidate for (b), from memory, to verify).**
- I recall that ODD-MAX-BIT composed with pairwise AND, OMB_n(x₁∧y₁, …, x_n∧y_n), has *exponentially small discrepancy*, something like 2^{−Ω(n^{1/3})}. The sources I have in mind are Buhrman–Vereshchagin–de Wolf (CCC 2007, "On computation and communication with small bias") and/or Sherstov, as the function separating PP^cc from UPP^cc.
- **It is a linear-size ELDL.** Each query x_i ∧ y_i is the exact threshold x_i + y_i = 2, and ODD-MAX-BIT is a decision list over them (length n, alternation depth up to n).
- **If both facts are verified:** a function with Disc ≤ 2^{−Ω(n^{c})} has an ELDL of size O(n). *No depth-independent discrepancy bound can hold*, since it would force size 2^{Ω(n^c)}.
  - So **the additive-loss lemma is false for the discrepancy measure**, and "the measure must change, not the recursion". That is **X4a**, reached from a known function without reading the recursion.
  - Theorem 45 is consistent with it: at k ≈ n the bound k·d^{−1/2k} is ≈ n.
- **The quantitative question, if X4a holds:** how fast *must* the loss grow with k for discrepancy? OMB∘AND shows that at k = n, d = 2^{−n^c} is compatible with size O(n). The report states the implied constraint on any discrepancy-based bound f(s, k, d).

**Flag P (the order of work).** (b) runs before (a) and (c), as ruled.
- If Flag K verifies, (c)'s repair is moot *for discrepancy*. Only (a) (where the loss enters) and (d) remain, and the next measure has to be non-discrepancy.
- If Flag K fails (the discrepancy is not small, or the function is not an ELDL), then (a), then (c).

**Flag S (what "additive" can mean).** An "additive potential" bound of the form Σ_i s_i ≥ g(d) is depth-independent. If Flag K holds, any such bound with g superpolynomial in n is refuted on OMB∘AND, whatever the potential. The only additive forms that survive are ones whose potential is not a function of discrepancy alone.

## Outcomes (the reviewer's)

| Code | Outcome |
|---|---|
| **X4a** | The multiplicative loss is tight (or necessary) for blocky discrepancy; the measure must change. |
| **X4b** | The loss is not tight, and the additive potential fails at a named step: the lemma under the lemma, sharpened once more. |
| **X4c** | The additive potential goes through beyond o(n/log n). Check it with suspicion; if it survives, it is the program's first new bound. |

**Priors.**
- Reviewer: X4b 50 / X4a 35 / X4c 15.
- Mine: **X4a 55 / X4b 35 / X4c 10.** X4a is raised by Flag K, which, if verified, decides (b) from a known function.

## Ceiling

X4 proves nothing about P vs NP. If X4a holds, the lemma under the lemma is restated as "a non-discrepancy measure over blocky matrices", with OMB∘AND as the witness that discrepancy cannot work at high alternation.
