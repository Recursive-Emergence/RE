# Y5: close (PL′). Report

*Run 2026-09-11 on branch `y5-close`, on the author's go ("Run Y5, push after merge"), against the pre-registration (ae258b9) and the reviewer's ruling (466047c).*
- *Priors, both sides: Y5b 50 / Y5c 30 / Y5a 20.*
- *Ruling (1): (iii-b) gets the effort, with three checks (α, β, γ).*
- *Ruling (2): find which side of the entropy protocol is verifier-sampled.*

*Documents only; `formal/` closed.*

**Sources tried for Goldreich–Vadhan** (SS22's [24], the source of Lemma 21), per the ruling's order:
- the Weizmann copy: connection reset on this run's attempt, the third on record;
- Goldreich's textbook: no freely reachable copy located (the search found only a ResearchGate listing);
- secondary descriptions, read as text:
  - **Haitner–Mahmoody–Xiao (HMX10)**, "A New Sampling Protocol and Applications to Basing Cryptographic Primitives on the Hardness of NP", l.283–310 and 459–530: the protocol VerifyHist, a constant-round public-coin, two-sided histogram (hence entropy) certification;
  - **Holenstein–Künzler**, arXiv:1312.2483, l.150–175: a survey of the set lower-bound (GS86) and upper-bound (Fortnow, Aiello–Håstad) protocols;
- Watson's min-entropy survey: **not read**. Its certificate failed verification over https, and http redirects to https; TLS verification was not bypassed.

**So Goldreich–Vadhan itself stays unread. Arm (ii) is settled on HMX's protocol, labelled secondary.**

## 0. Outcome

**Y5b: (PL′) fails at a named step.** The failure is image-side deflation in the two-sided entropy certification. The coarse grid (iii-b) does not collapse it: the asymmetry is proved, and an explicit M realizes it.

1. **Ruling (2), which side is verifier-sampled (secondary, HMX10 l.505–530, verified text):** neither. In the regular case, VerifyHist's soundness uses two GS **lower-bound** tests:
   - *"Preimage test: The verifier runs the lower-bound protocol … to check that k = |f^{−1}(f(x))| ≥ k′"*. This prevents claiming k′ ≫ k.
   - *"Image test: The verifier runs the lower-bound protocol to check that 2^n/k = |f({0,1}^n)| ≥ 2^n/k′ … We are able to use the lower-bound protocol in the image test because membership in the image of f"* is certified by an exhibited preimage. This prevents claiming k′ ≪ k.

   **Both sides are prover-exhibited**, so Flag N is confirmed on HMX's protocol. HMX l.300–307 add that two-sided estimates via the upper-bound protocols need secret samples from the domain, which the relevant setting cannot provide.
2. **(α), the scaled Proposition 16:** proved (§1). **Its cost is Θ(k₂·D/ε) bits, not D**, so the window it needs is polynomial for inverse-polynomial ε. It fits (PL′)(i)'s margin only for constant advantage and O(1) round-2 queries.
3. **(β), a grid drawn per round after commitment, with compounding:** holds. The kill test is passed (§2).
4. **(γ), does the grid also collapse Flag N's steerable side?** **No, and the asymmetry is proved (§3).**
   - Lemma B bounds steering **into existing** honest queries: mass, on average over the honest measure.
   - The image test lets Merlin create **new** image points on rows he chooses, and their number relative to a small canonical image is unbounded.
   - An explicit robust M deflates the output row's round-2 answers by c′ − c bits for any c′ ≤ r, beyond any grid scale.
5. **What (PL′) reduces to.** (PL′)(ii) holds only if image-side membership in the round-2 entropy certification uses **canonical** round-1 answers. That is (PL)'s canonical-certification requirement, restricted to the image test. **So (PL′) is not weaker than (PL) in the respect that matters**, and the bounded-round barrier remains ⟸ (PL).

## 1. (α): the coarse-grid collapse (proved)

**Definition.** For a grid scale L > 0 and an offset θ ∈ [0, L), let

  ϕ_{L,θ}(s) := θ + L·⌈(log(|Γ|/s) − θ)/L⌉,

the value log(|Γ|/s) rounded up to the grid θ + Lℤ. At L = 1, θ = 0 this is SS22's ϕ up to the floor/ceiling convention.

**Proposition 16′ (ours).** Let s, t > 0 with |log s − log t| ≤ D. For θ uniform on [0, L),

  Pr_θ[ϕ_{L,θ}(s) ≠ ϕ_{L,θ}(t)] ≤ D/L.

*Proof.* ϕ_{L,θ}(s) ≠ ϕ_{L,θ}(t) iff some grid point θ + jL lies in the half-open interval between log(|Γ|/s) and log(|Γ|/t), whose length is ≤ D. For fixed endpoints, the set of θ ∈ [0, L) placing a grid point in an interval of length D has measure ≤ D. ∎

(SS22's Proposition 16 is the case L = 1 with D ≈ log(1+τ) ≤ τ, and the bad set O(τ).)

**Cost.**
- The output row's k₂ round-2 answers must all collapse, except with probability ≤ ε/16. That needs k₂·D/L ≤ ε/16, i.e. **L ≥ 16·k₂·D/ε**.
- The answers are then canonical only up to the grid: they differ from J₂ by up to L bits. So **the window cost is L = Θ(k₂·D/ε)**, with D = log(1 + A/δ) from Lemma B.
- For inverse-polynomial ε this is polynomial and exceeds any β = n^{o(1)}.
- So (iii-b) fits (PL′)(i) **only for constant ε and k₂ = O(1)**, where L = O(D) = O(k₁·log n).

## 2. (β): one grid per round after commitment, and the kill test (verified by construction)

- Drawing the round-j grid offset θ_j after Merlin's round-j commitment is necessary. Otherwise Merlin can pick deviations straddling the grid points.
- It is also sufficient for Proposition 16′'s probability, which is over θ_j alone.
- The grids do not reset the reach. A_j ≥ (r + log k)^{Σ_{i<j} k_i}, so D_j = log(1 + A_j/δ) grows with j, and L_j ≥ 16k_j·D_j/ε compounds.
- The total window Σ_j L_j exceeds any ω(log n) tolerance after ω(1) rounds, even for constant ε. **The argument is silent on IW98's n stages.** ✓

## 3. (γ): image-side deflation, the asymmetry with Lemma B (proved)

**The two sides, relativized to round 2.** Round-2 membership f₂(x) = y is certified with Merlin-supplied round-1 answers for x. Per entry only round-1 **over**claims are blocked (GS on f₁ is objective); round-1 **under**claims, which raise J-answers, pass on Merlin-chosen rows (Y4 §6.1–6.2).
- **Preimage side:** exhibited x′ with steered f₂(x′) = y can **inflate** |f^{−1}(y)| for existing honest y. That is bounded by Lemma B, factor ≤ A/δ for all but δ of honest y, and the coarse grid could absorb it at the cost of §1.
- **Image side:** exhibited x with steered f₂(x) = y **for y outside the canonical image** inflates |Im f₂|. Its size is bounded only by |Im f_{2,B}| ≤ Σ_ρ |Reach(ρ)| ≤ A·|Γ|, so **the relative inflation |Im f_{2,B}|/|Im f₂| is unbounded when the canonical image is small.** Lemma B's Markov argument does not apply, because there is no honest mass on the new image points to average against.

**The explicit M (proved).**
- Round 1: a flat query with canonical answer a.
- Round 2: if the answer is ≥ a − 1, query prefix_c(ρ); otherwise query prefix_{c′}(ρ), with c < c′ ≤ r.
- The output is a function of the round-1 answer only, so **M is robust (H5)**.
- Canonical round 2: image size 2^c, every preimage of size 2^{|Γ|-bits − c}, and J₂ = c for every honest query.

**Merlin's strategy.**
1. Claim the round-2 histogram "all mass at weight 2^{−c′}".
2. **Image test:** exhibit steered rows ρ′, with their round-1 counts underclaimed by a factor ≥ 4 so that the answer is < a − 1, covering 2^{c′} distinct prefixes prefix_{c′}(ρ′). The lower bound |Im| ≥ 2^{c′} passes.
3. **Preimage test:** for honest x, the true |f₂^{−1}(f₂(x))| = 2^{·−c} ≥ the claimed 2^{·−c′}. The lower bound passes (it only prevents overclaims).
4. Claim every sampled round-2 count at 2^{·−c′}. That is an underclaim by 2^{c′−c}, which no per-entry test blocks and which the histogram (verified through the steerable image test) now supports.
5. **Result:** every round-2 answer on the output row is c′ instead of c. The shift c′ − c ranges up to r, beyond β and beyond any grid scale L. ∎

**The symmetry the reviewer expected fails, for the reason just shown.**
- Inflation lives on the honest support, where Markov applies.
- Deflation is supported by *new* image points **off** the honest support, where nothing bounds it.
- The coarse grid collapses deviations of bounded size D. Image-side deflation has no bounded D.

## 4. What (PL′) reduces to, and the door after Y5

- (PL′)(ii) holds only if the round-2 two-sided entropy certification is **not steerable on the image side**, i.e. image-membership witnesses are checked with **canonical** round-1 answers.
- That is Flag L's / (PL)'s canonical-certification requirement, restricted to the image test.
- **So after Y5, the bounded-round adaptive barrier is ⟸ (PL), and the (PL′) route does not avoid (PL).** The only regime where the (PL′) route's other parts fit is constant advantage and O(1) round-2 queries, and there too (γ) fails.
- **Caveat (g8):** this is proved against HMX's VerifyHist. Goldreich–Vadhan's Lemma 21 protocol (unread) could differ. **If its H ≥ h side avoids image-membership witnesses, (γ) must be re-checked there.**

## 5. Priors against outcome, and misses

| | Y5b | Y5c | Y5a |
|---|---|---|---|
| reviewer (pre-reg → ruling) | 45 → 50 | 20 → 30 | 35 → 20 |
| mine | 50 | 30 | 20 |
| **outcome** | **✓** ((γ) image-side deflation, with the asymmetry proved; (α)'s cost polynomial) | partly: GV unread, (ii) settled on HMX (secondary) | not reached |

- **No miss on either side** on the outcome.
- The reviewer's expectation that the grid "should be symmetric" is shown not to hold (§3). Whether that counts as a premise miss is the reviewer's to score.
- My pre-registered candidate repair (iii-b) was right on (α) and (β) and failed on (γ).

## Ceiling

Y5 proves nothing about P vs NP or OWF. It closes the (PL′) route: **the bounded-round adaptive barrier needs (PL), canonical certification, at least on the image side of the entropy protocol.** The door's address after Y5 is: bounded-round adaptive reductions barred ⟸ (PL); (PL) open; unbounded adaptivity PSPACE-hard and deep (H′).

## Formal record

Untouched (the author's decision).

## Ruling (the reviewer's, recorded at acceptance)

**Accepted as Y5b on the report.** Merge 2835de2; push on the author's standing go; then the page update (§10 item 17).

**Scoring:** "it should be symmetric" is the reviewer's **wrong outcome prior**, counted. The asymmetry — inflation on the honest support, deflation off it via prover-exhibited image witnesses — is the finding, and goes in as proved against HMX's VerifyHist (secondary), with the GV caveat and the three connection resets logged.

**(α) and (β) go in as proved:** the grid collapses inflation at cost Θ(k₂·D/ε); the per-round draw; the compounding that kills ω(1) rounds.

**Y6 ((PL) at two rounds)** is named, on the author's go, as a draft for ruling.
