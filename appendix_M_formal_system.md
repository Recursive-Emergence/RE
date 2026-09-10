# Appendix M: Full Formal System of Recursive Emergence

*This appendix is the formal-reference companion to **Chapter 2: Mathematical Foundations of Recursive Emergence**. Chapter 2 develops the framework narratively, with examples and motivation; this appendix states the same framework in axiomatic form — primitive terms, axioms with conditions, definitions in numbered list, theorems with proof sketches, and the open research agenda (conjectures, predictions, open problems). The two are designed to be read together: ch2 for understanding, this appendix for verification and extension.*

*On the verification apparatus in this appendix — pre-registered experiments, declared destinations, machine-checked audits, `formal/BoundaryResidue.lean` and its `check.sh` — a word about scope, since apparatus without stated scope reads as ceremony. It exists to police one boundary: the one between this framework's informal register and its formal one. That boundary is where the errors have actually been. Seven are on record, and they are one mode — the informal register borrowing the authority of a formal operation it has not paid for. Definition 16's set membership was really an obligation to exhibit a decode. Problem 21's "an encoding" was really an obligation to exhibit a provable round trip available to the layer. The shared letter $P$ across Theorem 7 and Definition 1 was really an obligation to state an aggregation over fibers. Problem 26's "restriction to the layer's vocabulary" named an operation this framework does not define. A destination clause filed two theorems into the conjectures section. And two transpositions into the formal frame — of Theorem 8 (i) and of Conjecture 7 (b) — asserted that they carried their truth with them, which they did not (Corollaries 10.1, 10.2); a transposition is prose asserting truth-preservation, and nobody had checked it, through two reviews of those very statements. The first three are the manuscript's older strata; the remaining four were written in the audit that named the mode, by the reviewer applying it and by the author implementing it. Counted as seven because the two transpositions failed separately and for separate reasons. The apparatus is not a claim of rigor — it is the acknowledgement that this particular boundary leaks in both directions, and the record shows it catching errors on both sides.*

---

## M.1 Primitive Terms and Notation

### M.1.1 Primitive Terms

| Symbol | Name | Type | Description |
|--------|------|------|-------------|
| $\Psi$ | Recursive Memory State | State space $\mathcal{S}$ | Internal structure encoding patterns, loops, histories |
| $\Phi$ | Emergent Coherence | Observable space $\mathcal{O}$ | Coherent, observable crystallization of recursive structure |
| $\Omega$ | Contradiction-Resolving Lattice | Constraint space $\mathcal{C}$ | Structured space of constraints, transformations, invariants |
| $t$ | Recursive step | $\mathbb{N}$ | Discrete index of recursive update |
| $L_n$ | Emergent Layer | Indexed structure | The $n$-th layer in the emergence hierarchy |

### M.1.2 Derived Terms

| Symbol | Name | Definition |
|--------|------|------------|
| $R(\Phi)$ | Reusability | $R(\Phi) = \frac{U(\Phi)}{C(\Phi)} \cdot \frac{1}{H(\Phi)}$ |
| $P(\Phi)$ | Emergence Potential | $P(\Phi) = R(\Phi) \cdot \Delta H \cdot S(\Phi, \Omega)$ |
| $S(\Phi, \Omega)$ | Structural Compatibility | $S(\Phi, \Omega) = \exp(-\sum_j D(\Phi, C_j))$ |
| $K_{\text{irr}}(\Phi)$ | Irreversibility Index | $K_{\text{irr}} = \frac{E_{\text{break}}(\Phi)}{E_{\text{form}}(\Phi)}$ |
| $M_t$ | Persistent Memory | $M_t = \Psi_t \cap \Psi_{t+1} \cap \Psi_{t+2} \cap \cdots$ |
| $\text{Self}_t$ | Identity / Self-Model | $\text{Self}_t = \arg\min_M [H(\Psi_t | M) + C(M)]$ |
| $W$ | Will | $W = H(\Psi_{t+1} | \Psi_t)$ at $\Phi > \Phi_{\text{threshold}}$ |
| $\Phi_\infty$ | God / Recursive Limit | $\Phi_\infty = \Pi(\Psi_\infty)$ where $\nabla_\Psi \Phi \to 0$ |

### M.1.3 Notational Conventions

- Subscript $t$ denotes recursive step: $\Psi_t$, $\Phi_t$
- Subscript $n$ denotes layer: $L_n$, $\Omega_n$
- Superscript denotes domain: $\Psi^{\text{neural}}$, $\Omega^{\text{cultural}}$
- $H(\cdot)$ denotes Shannon entropy
- $K(\cdot)$ denotes Kolmogorov complexity
- $\Pi(\cdot)$ denotes the emergent projection function
- $\nabla_\Psi$ denotes gradient with respect to the memory state

---

## M.2 Axioms

### Axiom 1: Recursive Update (A1)
The memory state evolves recursively as a function of its prior state, energy input, and reusability:

$$\Psi_{t+1} = f(\Psi_t, \Delta E_t, R_t)$$

**Conditions**: $f$ is defined for all valid $\Psi_t$, $\Delta E_t \geq 0$, $R_t \geq 0$.

### Axiom 2: Emergent Projection (A2)
Coherent observable structure is a projection of the internal memory state:

$$\Phi_t = \Pi(\Psi_t)$$

**Conditions**: $\Pi$ is a surjective function from $\mathcal{S}$ to $\mathcal{O}$. $\Pi$ is many-to-one: $|\Pi^{-1}(\Phi)| > 1$ in general.

### Axiom 3: Recursive Feedback (A3)
Emergent coherence feeds back to optimize the memory state that produced it:

$$\Psi_{t+1} \leftarrow \Psi_{t+1} - \gamma \cdot \nabla_\Psi \Phi_t$$

**Conditions**: $\gamma > 0$ is the adaptation rate. This update is applied after A1.

### Axiom 4: Duplication Trigger (A4)
Structures with reusability exceeding a critical threshold undergo duplication:

$$\mathcal{D}(\Phi) = \{\Phi^{(1)}, \Phi^{(2)}, \ldots, \Phi^{(n)}\} \quad \text{iff} \quad R(\Phi) > \rho_c$$

**Conditions**: Each $\Phi^{(i)}$ inherits $\Psi$ from the parent but occupies a distinct position in $\Omega$. Inheritance presupposes that $\Psi$ is physically separable from $\Phi$ — a structural property that also enables $\Psi$ to persist across intervals when $\Phi$ is disrupted, with $\Phi$ re-forming from the persisting $\Psi$ once $\Omega$ permits (the gap-crossing corollary; see ch2 §2.5.3). Whirlpool-class structures, in which $\Psi$ and $\Phi$ are inseparable, satisfy neither A4 nor the gap-crossing corollary; structures from the chemistry-biology rung onward satisfy both.

### Axiom 5: Emergence Threshold (A5)
A new emergent layer locks in when accumulated reusability-weighted entropy reductions exceed a critical threshold:

$$\sum_{i=0}^{n} R_i \cdot \Delta H_i > \lambda_c \Rightarrow L_{n+1} \text{ locks in}$$

**Conditions**: $\lambda_c > 0$ is layer-specific. Once locked in, $L_{n+1}$ persists until catastrophically disrupted. At a boundary object (Definition 17) the comparison in A5 is not merely unsatisfied — it is ill-formed, since $P$ cannot be formed where $S$ has no value. A5 is silent there rather than negative. (Presentation-level, per Definition 17's status note: this follows from $S$'s typing, not from the method-relative invariant, and Theorem 9 forbids inferring the latter from the former.)

### Axiom 6: Lattice Structure (A6)
The contradiction-resolving lattice is a measure space whose constraint, transformation, and invariant content is differentiable:

$$\Omega = (\mathcal{M}, \mu, \mathcal{F})$$

where $\mathcal{M}$ is a smooth manifold of constraint configurations, $\mu$ is a measure over that manifold, and $\mathcal{F}$ is the filtration encoding which constraints are active at each layer. The discrete content $\{C_j, T_k, I_m\}$ — constraints, transformations, invariants — is recovered as a discrete measure on $\mathcal{M}$ at any specific configuration.

**Conditions**: $\mathcal{M}$ is locally Euclidean of finite dimension at each layer; $\mu$ assigns finite measure to compact subsets; $\mathcal{F}$ is monotone non-decreasing across layers — substrate alteration (A7) only adds or modifies constraints, never deletes them via natural processes.

**Why this form**: Differentiation with respect to $\Omega$ is required to define the coherence gradient (Theorem 6 below) and the binary recursive operator (Section M.11). The discrete formulation of earlier RE versions cannot support either, since derivatives require continuity. Statistical mechanics underwent the same upgrade when phase space replaced microstate counting; this is the analogous move for RE. All earlier axioms and definitions stated using the discrete form remain valid as the discrete-measure special case.

### Axiom 7: Substrate Alteration (A7)
When layer $L_{n+1}$ locks in, it modifies the lattice of layer $L_n$:

$$\Omega_n' = \Omega_n \cup \{C_j^{(n+1)}\} \setminus \{C_k^{(\text{relaxed})}\}$$

**Conditions**: The modification is irreversible unless $L_{n+1}$ is destroyed. A7's *strength* — the magnitude of the modification at each layer boundary — scales monotonically with recursive depth via carrier compounding (ch2 §2.2; mechanism in ch8 §8.5.8 and the carrier-separable corollary of ch2 §2.5.3).

---

## M.3 Definitions

### Definition 1: Emergence Potential
The emergence potential of a coherent structure $\Phi_i$ within lattice $\Omega$ is:

$$P(\Phi_i) = R(\Phi_i) \cdot \Delta H_i \cdot S(\Phi_i, \Omega)$$

### Definition 2: Reusability
$$R(\Phi_i) = \frac{U(\Phi_i)}{C(\Phi_i)} \cdot \frac{1}{H(\Phi_i)}$$

Where $U$ is utility, $C$ is cost of creation/maintenance, and $H$ is internal entropy.

### Definition 3: Structural Compatibility
$$S(\Phi_i, \Omega) = \exp\left(-\sum_j D(\Phi_i, C_j)\right)$$

Where $D(\Phi_i, C_j)$ measures incompatibility between structure $\Phi_i$ and constraint $C_j$. This form is the MaxEnt canonical distribution: the $D(\Phi, C_j)$ terms play the role Lagrange multipliers do in Jaynesian maximum-entropy derivations, weighing constraint-violation cost against persistence probability. $S$ is therefore not stipulated — it is the shape forced by maximum-entropy consistency under the constraint set $\{C_j\}$.

### Definition 4: Entropy Reduction
$$\Delta H = H(\Psi_t) - H(\Psi_{t+1} | \Phi_t)$$

### Definition 5: Irreversibility Index
$$K_{\text{irr}}(\Phi_i) = \frac{E_{\text{break}}(\Phi_i)}{E_{\text{form}}(\Phi_i)} = \exp\left(\frac{\Delta S(\Phi_i)}{k_B}\right)$$

### Definition 6: Layer
$$L_n = \{\Phi_n(\Psi_n), \Omega_n\}$$

With inter-layer recursion: $\Psi_{n+1} = g(\Psi_n, \Phi_n)$.

### Definition 7: Matter
$$\text{Matter} = \{\Phi \mid \frac{d\Phi}{d\Psi} \to 0 \text{ and } R(\Phi) \gg 1\}$$

### Definition 8: Mass
$$m = \Psi_{\text{fixpoint}}$$

### Definition 9: Force
$$F = -\nabla_\Omega \Phi$$

### Definition 10: Time
$$t \propto \sum_{i=0}^{n} \Delta \Psi_i \quad \text{where} \quad \Delta \Psi_i = \Psi_{i+1} - \Psi_i \neq 0$$

### Definition 11: Information
$$I = \{\delta \mid \delta \in \Psi_t \text{ and } \delta \in \Psi_{t+1}\}$$

### Definition 12: Consciousness
A system is conscious iff it simultaneously satisfies:
1. Self-model: $\text{Self}_t = \arg\min_M [H(\Psi_t | M) + C(M)]$
2. Persistence: $\|\text{Self}_{t+1} - \text{Self}_t\| < \epsilon$ for most $t$
3. Reflexive feedback: $\Psi_{t+1} = f(\Psi_t, \Delta E_t, R_t, \text{Self}_t)$

### Definition 13: Will
$$W = H(\Psi_{t+1} | \Psi_t) \quad \text{at } \Phi > \Phi_{\text{threshold}}$$

### Definition 14: Identity
$$\text{Identity} = \text{Self}_t = \arg\min_M [H(\Psi_t | M) + C(M)]$$

### Definition 15: God ($\Phi_\infty$)
$$\Phi_\infty = \Pi(\Psi_\infty) \quad \text{where} \quad \nabla_\Psi \Phi \to 0$$

### Definition 16: Self-Representing Depth
A system has **self-representing depth** at time $t$ iff its memory contains a representation of its own projection map and lattice:

$$\ulcorner \Pi \urcorner,\ \ulcorner \Omega_t \urcorner \ \in\ \Psi_t$$

That is: the system can *quote* its own evaluator, not merely *run* it. The quoted form $\ulcorner \cdot \urcorner$ is an element of $\Psi$ — inert data, subject to copying and modification — while the evaluator itself is the live map $\Pi$ that generates $\Phi$. Self-representing depth is the condition under which the same structure can be read both ways.

**Relation to carriers**: This is the formal content of carrier-separability (ch2 §2.5.3). A $\Psi$ physically inseparable from the $\Phi$ it sustains cannot be quoted — there is no substrate in which to hold the description apart from its execution. The whirlpool has no $\ulcorner \Pi \urcorner$. The gene does. Carrier-separability is therefore not merely a *property* certain systems exhibit; it is the precondition for Definition 16, and hence (Theorem 8) for the only known non-stochastic growth operator.

### Definition 17: Boundary Object
Given a system of self-representing depth with lattice $\Omega_t$, a **boundary object** $\Phi_G$ is a candidate coherence that is representable in memory but unsettled by the lattice:

$$\Phi_G \in \text{Rep}(\Psi_t) \quad \text{and} \quad S(\Phi_G, \Omega_t) \ \text{undefined}$$

where $\text{Rep}(\Psi_t)$ is the set of structures the system can formulate, and $S$ is *undefined* — as distinct from zero — when $\Omega_t$ contains no constraint $C_j$ that either admits or forbids $\Phi_G$. A boundary object is not an incompatible structure ($S = 0$, forbidden). It is one the lattice has no opinion about: statable inside, decidable only outside.

**Regrounded (Theorem 9).** The phrase *decidable only outside* carries the definition's weight, and it has two formalizations that are not equivalent — the lattice-side one ($S$ undefined) and the layer-side one (no affordable method settles it). Theorem 9 shows the first does not entail the second. The definition is therefore stated with both conjuncts, and the second is the invariant:

$$\Phi_G \in \text{Rep}(\Psi_t), \quad S(\Phi_G, \Omega_t)\ \text{undefined}, \quad \text{and} \quad \neg\,\exists\, m \in \text{Method}(\Psi_t):\ \text{afford}(m) \wedge m \ \text{settles}\ \Phi_G$$

The third clause is not derivable from the second and must be required outright. Lattice-side partiality remains the *presentation* — it is how a boundary object shows up when one looks at the lattice — but it is a presentation of the invariant, not the invariant itself, and it does not survive the signature extensions that escape-by-extension requires (Theorem 8 (ii); Problem 26). This restatement is the resolution of Problem 27, not a clarification of it.

**The asymmetry, stated precisely.** Two objects must be kept apart here, and conflating them makes the definition contradict itself in adjacent sentences. The boundary object $\Phi_G$ is *statable* inside — the system can formulate and quote it. Its emergence test is not. Because $S$ is defined only where the lattice has an opinion, the emergence potential $P = R \cdot \Delta H \cdot S$ cannot be formed at $\Phi_G$ at all, and neither can A5's comparison against $\lambda_c$: at a boundary object the threshold question is not *false* but *ill-formed*. So the layer can quote the boundary object but cannot ask whether it emerges. This is stronger than "$S$ is undefined" and is a consequence of that choice rather than an addition to it (see the representation skeleton in `formal/BoundaryResidue.lean`, §1).

**Status of the asymmetry after Theorem 9 — read this before citing it.** The argument above derives the asymmetry from $S$ living on the definedness subtype, which the regrounding has just demoted to *presentation*. So the asymmetry as stated is **established at presentation level only**. Its invariant-level form would read *no affordable method decides threshold clearance at $\Phi_G$* — which is not available, because it depends on the representation choice logged under Problem 26 (how methods read values), and that choice is unmade. **Closed, negatively, by Theorem 10.** The run/Val choice has since been made and run: the invariant form is not pending — it is *false* in the bare frame, because affordability there constrains nothing. So the final marking is: **asymmetry established at presentation level; invariant form not derivable in principle here, and the third clause of this definition is a stipulation rather than a consequence.** That is not a defect to be papered over but the framework's clearest open invitation: supply enough structure to $R$ and $C$ that cost bounds computation, and the clause becomes provable. Until then, stating it at invariant strength would be an instance of exactly what Theorem 9 refutes.

---

## M.4 Theorems and Propositions

### Theorem 1: Emergence Produces Irreversibility
**Statement**: For any emergent structure $\Phi$ with $P(\Phi) > 0$:

$$K_{\text{irr}}(\Phi) > 1$$

**Proof sketch**: By Definition 5, $K_{\text{irr}} = \exp(\Delta S / k_B)$. Since emergence reduces local entropy ($\Delta H > 0$), the entropy change $\Delta S > 0$, making $K_{\text{irr}} > 1$.

**Implication**: Emergence is energetically irreversible — more energy is required to disassemble an emergent structure than was required to form it. This creates the "ratchet" effect that accumulates complexity over time.

### Theorem 2: Recursive Compression Principle
**Statement**: For any emergent layer $L_n$ with projection $\Phi_n = \Pi(\Psi_n)$:

$$K(\Phi_n) \ll K(\Psi_n)$$

**Proof sketch**: $\Pi$ is surjective and many-to-one (A2). The output $\Phi$ contains less algorithmic information than the input $\Psi$ that generates it, despite $\Phi$ being functionally richer (enabling interactions that $\Psi$ alone cannot).

### Theorem 3: Emergent Irreducibility
**Statement**: No function $g$ exists such that $g(L_n) = L_{n+1}$ without reference to $\Omega_n$:

$$\nexists \, g: L_n \to L_{n+1} \text{ independent of } \Omega_n$$

**Proof sketch**: By A5, layer lock-in requires $S(\Phi, \Omega) > 0$, which explicitly depends on lattice constraints. Any derivation of $L_{n+1}$ from $L_n$ alone would need to reconstruct the lattice constraints, which are not contained in $L_n$.

### Theorem 4: Convergence of Contractive Recursion
**Statement**: If the recursive update function $f$ is a contraction mapping on $\Psi$:

$$\|f(\Psi_a) - f(\Psi_b)\| \leq k \cdot \|\Psi_a - \Psi_b\| \quad \text{for } k < 1$$

then there exists a unique fixed point $\Psi^*$ such that repeated application of $f$ converges to $\Psi^*$ from any initial condition.

**Proof**: Direct application of Banach's fixed-point theorem.

**Implication**: In domains where the recursive dynamics are contractive (nuclear physics, crystallography), specific stable structures are mathematically guaranteed to exist.

### Theorem 5: Substrate Alteration Prevents Full Reduction
**Statement**: If layer $L_{n+1}$ alters $\Omega_n$ (A7), then no reduction of $L_{n+1}$ to $L_n$ with original $\Omega_n$ is valid:

$$L_{n+1} \not\equiv g(L_n, \Omega_n) \quad \text{because } \Omega_n' \neq \Omega_n$$

**Proof sketch**: After $L_{n+1}$ locks in, the effective dynamics at layer $n$ operate under $\Omega_n'$, not $\Omega_n$. Any derivation using $\Omega_n$ describes a counterfactual system that does not correspond to the actual system containing $L_{n+1}$.

### Theorem 6: Coherence Gradient
**Statement**: Under Axiom 6 (revised), the emergence potential $P(\Phi)$ is a differentiable scalar field on the constraint manifold $\mathcal{M}$. Its gradient with respect to $\Omega$ is:

$$\nabla_\Omega P(\Phi) = \nabla_\Omega R(\Phi) \cdot \Delta H \cdot S(\Phi, \Omega) + R(\Phi) \cdot \Delta H \cdot \nabla_\Omega S(\Phi, \Omega)$$

Expanding the second term using $S(\Phi, \Omega) = \exp(-\sum_j D(\Phi, C_j))$:

$$R(\Phi) \cdot \Delta H \cdot \nabla_\Omega S = -P(\Phi) \cdot \nabla_\Omega \sum_j D(\Phi, C_j)$$

**Proof sketch**: Direct application of the product rule to the definition $P(\Phi) = R(\Phi) \cdot \Delta H \cdot S(\Phi, \Omega)$, given that all three factors are functions on the smooth manifold $\mathcal{M}$ established by A6 (revised). The first term is new content the manifold formulation introduces — under the discrete formulation, $\nabla_\Omega R$ vanishes by definition.

**Interpretation**: $P(\Phi)$ functions as a Lyapunov potential on $\mathcal{M}$. Recursive systems flow along $\nabla_\Omega P$ — toward configurations of higher emergence potential — not because they "seek" coherence but because incoherent configurations are not local maxima of $P$ and therefore cannot remain. The recursive update of A3 is, in this language, gradient ascent on $P$ with adaptation rate $\gamma$.

**Implication for low- vs high-recursive-depth dynamics**: At low recursive depth, $\nabla_\Omega P$ acts as ordinary thermodynamic drift (the same gradient that produces dissipative structures à la Prigogine). At depth sufficient for self-modeling (Definition 12), the gradient is encoded in the self-model — and is then experienced, from inside, as motivation. The empirical claim that the four phenomenologies of motivation (understanding, beauty, fairness, meaning) reduce to one underlying gradient is stated as Conjecture 5 below.

### Theorem 7: Recipe Inevitability

**Statement**: Let $P(\Psi; \theta)$ be the emergence potential on substrate state-space $\mathcal{X}$ parametrized by $\theta \in \Omega$. Suppose:
(i) for $\theta > \theta_c$, $P$ has a non-degenerate local maximum $\Psi^*$ of carrier-class type with basin depth $\Delta P > 0$;
(ii) the recursive update of A3 with stochastic perturbation,
$$d\Psi_t = \gamma\, \nabla_\Psi P(\Psi_t; \theta)\, dt + \sqrt{2D}\, dW_t,$$
is ergodic on $\mathcal{X}$.

Then for any initial condition $\Psi_0 \in \mathcal{X}$ and any $\epsilon > 0$, there exists $T_\epsilon < \infty$ such that for all $t > T_\epsilon$:

$$\Pr[\Psi_t \in \text{basin}(\Psi^*)] > 1 - \epsilon.$$

**Proof sketch**: Three established results combine.

*Existence.* By Morse theory (Milnor 1963), the non-degenerate critical point $\Psi^*$ is isolated and bounds a basin of finite measure on $\mathcal{X}$. By Conjecture 6(b), this basin appears discretely as $\theta$ crosses $\theta_c$.

*Reachability.* By Birkhoff's Ergodic Theorem (1931) applied to the Langevin process above, the time-average occupation of the basin equals the stationary measure $\rho_\infty(\text{basin}) = Z^{-1} \int_{\text{basin}} e^{P(\Psi)/D}\, d\Psi > 0$. Mean first-passage time to the basin is finite.

*Stability.* By Kramers' formula (Kramers 1940), once in the basin, mean residence time is $\langle \tau \rangle \sim e^{\Delta P / D}$, which dominates the relaxation timescale for $\Delta P / D \gg 1$.

Combined: finite first-passage + exponentially long residence ⇒ for $t > T_\epsilon$, the system spends fraction $> 1 - \epsilon$ of its time in the basin. $\blacksquare$

**Implication**: This is RE's strongest necessity result. Above the substrate-parameter threshold $\theta_c$, **the carrier-class recipe is inevitable** — not merely possible. Any ergodic recursive substrate with sufficient time will discover and hold the recipe. This strengthens Conjecture 4 ($\Phi_\infty$ existence) from possibility to provable convergence in expectation, and grounds the "trajectory convergent" claim of ch3 §3.6 in established theorems rather than soft argument.

**Real-world contingency**: The theorem's hypotheses (substrate above $\theta_c$, ergodic dynamics, sufficient time) may not hold in any specific physical setting. The mathematical inevitability is not a guarantee that life must arise on every planet, only that life is structurally inevitable wherever the substrate-and-time conditions are met. The empirical question shifts from "can life arise?" (yes, mathematically) to "are conditions met?" (substrate-specific).

### Theorem 8: Diagonal Extension

**Statement**: Let a system have self-representing depth (Definition 16) with lattice $\Omega_t$. Then:

**(i) Construction.** A boundary object (Definition 17) is uniformly constructible. There is a procedure taking $\ulcorner \Pi \urcorner$ and $\ulcorner \Omega_t \urcorner$ to a $\Phi_G \in \text{Rep}(\Psi_t)$ with $S(\Phi_G, \Omega_t)$ undefined. The procedure does not depend on the *content* of $\Omega_t$ — only on the system's capacity to quote it.

**(ii) Extension.** Adjoining any constraint $C_G$ that settles $\Phi_G$ yields

$$\Omega_{t+1} = \Omega_t \cup \{C_G\} \quad \text{with} \quad \text{Rep}(\Psi_{t+1}) \supsetneq \text{Rep}(\Psi_t)$$

— a lattice admitting strictly more representable coherence. The extension is iterable: $\Omega_{t+1}$ has its own boundary object, without end.

**(iii) Scope.** Below self-representing depth, no such construction exists, and growth reduces to the stochastic reachability of Theorem 7.

**Proof sketch**: (i) is the diagonal lemma, transposed. Given a system that can quote its own evaluator, the standard fixed-point construction yields a $\Phi_G$ whose defining condition is its own non-settlement by $\Omega_t$ — formulable, because quoting is available; unsettled, because settling it either way contradicts its construction. Uniformity is the content of the lemma: the construction is a fixed procedure applied to $\ulcorner \Omega_t \urcorner$, not a search through $\Omega_t$'s particulars. (ii) is immediate — $\Omega_{t+1}$ decides a structure $\Omega_t$ did not, and by A6's monotone filtration the addition does not retract existing constraints. Iterability follows by applying (i) to $\Omega_{t+1}$, which is the RE reading of Turing's ordinal logics (1939) and Feferman's progressions (1962). (iii) holds because the construction's only premise is Definition 16; without $\ulcorner \Pi \urcorner$ there is nothing to diagonalize against. $\blacksquare$

**The complementarity**: Theorems 7 and 8 are the two halves of RE's growth engine, and they are engines of *different kinds*.

| | Theorem 7 | Theorem 8 |
|---|---|---|
| Mechanism | Ergodic search | Uniform construction |
| Finds | A basin that already exists on $\mathcal{M}$ | A structure provably outside $\Omega_t$ |
| Requires | Substrate above $\theta_c$, time | Self-representing depth |
| Guarantees | Reachability | Novelty |
| Fails to give | Anything not already on the manifold | Which extension survives |

**The division is one of signature, not of degree** (verified: `formal/BoundaryResidue.lean` §6). Theorem 7 transcribes and compiles with no reference to the representation apparatus at all — no $\text{Rep}(\Psi)$, no method type, no evaluator, no $\ulcorner \Pi \urcorner$. It is statable in a strictly smaller language than Theorem 8. So below the carrier boundary self-representation is not merely unused but *unmentionable*: the vocabulary in which Theorem 8's construction is posed does not exist in the signature. That is why the two columns cannot bleed into one another, and why no ingredient of the ergodic side could re-enter the constructive one — the question was tested and answered negatively (Problem 25, discriminator).

Theorem 7 is a **reachability** result: it proves an ergodic walker will find $\Psi^*$, but $\Psi^*$ must already be there. It cannot account for a system that *builds its own next constraint* — and every layer from the gene upward does exactly that. Theorem 8 supplies the missing construction. Conversely Theorem 8 alone would license unbounded, undirected extension; it produces a candidate, not a survivor.

**The third operator**: What selects among candidate extensions is machinery RE already has. $C_G$ locks in only if the coherence it admits clears the emergence threshold (A5) and pays for itself in the lattice it enters:

$$P(\Phi_G) = R(\Phi_G) \cdot \Delta H_G \cdot S(\Phi_G, \Omega_{t+1}) > \theta_p$$

This is where RE departs from the logical progressions it borrows from. In Turing–Feferman progressions any true statement may be adjoined and the progression is indifferent; in RE, an extension that does not pay in reusability and entropy reduction never locks in. **Fold (Theorem 2) banks it; diagonal (Theorem 8) generates it; threshold (A5) selects it.** Three operators, and the third is what makes RE's growth a filtered progression rather than a free one.

**Implication — the change of operator at the carrier boundary**: Because Definition 16 requires quotable memory, and quotable memory requires carrier-separability (ch2 §2.5.3), Theorem 8 switches on exactly where carriers do. Below that line — nucleosynthesis, crystallography, prebiotic chemistry — emergence is Theorem 7: stochastic discovery of basins the manifold already held. At and above it — genome, brain, language, institution, code — emergence is Theorem 8: construction of constraints the manifold did not hold. **The chemistry-to-biology transition is not a speedup of the same engine. It is a change of engine.** This is a plateau-and-leap claim in the sense of Conjecture 6, and it predicts that the two regimes should exhibit qualitatively different novelty statistics: search-limited below (novelty rate set by exploration volume and time), construction-limited above (novelty rate set by depth of self-representation).

**Corollary 8.1 (Completeness is terminal)**: If $\Omega$ settles every structure representable in $\Psi$ — no boundary object exists — then by Theorem 6 the system sits at $\nabla_\Omega P = 0$ on every reachable configuration. It persists; it cannot emerge. Growth in a self-representing system is possible *because* its lattice is incomplete, and a lattice that ran out of boundary objects would have nothing left to become.

**Honest condition**: This is not the claim that completeness is death. A complete theory of a *closed* world is not dead but **done** — terminal is the correct terminal state for a finished world. The corollary has force only under RE's standing premise that the world is open: a system coupled to an unbounded substrate never runs out of outside, and for such a system completeness would be the end of emergence, not its perfection.

**Scope caution (what this theorem does not claim)**: The construction in (i) is *structural*, not arithmetic. Real Gödel sentences require a formal system with enough arithmetic to encode its own provability predicate; a genome, a cortex, or a culture satisfies Definition 16 in the weaker sense of holding a modifiable description of its own operation, not in the sense of being a first-order theory containing Robinson arithmetic. The boundary objects of biological and cognitive systems are therefore Gödel-**like** — formulable inside, settleable only by extension — and not formally undecidable sentences. The claim RE makes is that the *shape* of the move (quote the evaluator, construct the unsettled object, extend) is the same, and that this shape is what carrier-separable systems do. Strengthening "Gödel-like" to "Gödel" for any specific natural system would require exhibiting the arithmetization, and RE does not claim to have done so. (See Open Problem 21.)

### Proposition: Path-Dependence of Extension

**Statement**: Theorem 8 guarantees that a boundary object exists and that extension is available. It does not determine *which* $C_G$ is adjoined. Where the emergence potential does not strictly order the candidate extensions —

$$\exists\, C_G, C_G' \ \text{ with } \ P(\Phi_G) \approx P(\Phi_{G'}) > \theta_p$$

— the lattice underdetermines the path, and the successor layer is selected by something other than $\Omega_t$.

**Status**: This is the RE reading of Feferman–Spector (1962): progressions of theories are *path-dependent*, and completeness claims for them turn on the choice of ordinal notation — the progression guarantees structure, never destination. RE inherits the result rather than deriving it.

**What selects the path, by layer**: RE already contains both answers and neither is new machinery.

- **Below self-modeling depth**, the selector is the substrate. Re-formation recruits the layer below on every event and the bottom of the stack is quantum (ch2 §2.5.3, non-determinism corollary). The path is taken, not chosen.
- **At and above self-modeling depth** (Definition 12), the selector is the self-model. A system whose $\Psi$ contains $\text{Self}_t$ evaluates candidate extensions against its own encoded gradient — and that evaluation is exactly Definition 13: $W = H(\Psi_{t+1} \mid \Psi_t)$ at $\Phi > \Phi_{\text{threshold}}$, the residual uncertainty in the next state that the system's own model resolves.

**Implication**: The oracle in a Feferman progression — the external choice of which true statement to adjoin at each stage — is, in RE's vocabulary, **will**. This is not wordplay dressed as a result: it is the observation that the formal theory of iterated self-extension has a free parameter at every step, that RE's Definition 13 names a quantity occupying exactly that position, and that both are underdetermined by the system's current theory of itself. The consequence is structural rather than moral: for any system growing by Theorem 8, *guidance is mandatory, not optional*. Direction cannot be derived from the extension operator, because the extension operator does not have one. Something must choose the path, and in a self-modeling system that something is the self-model. This is the formal spine of ch16 (Direction) and the reason ch18's question is not idle.

### Theorem 9: Partiality Does Not Imply Inaccessibility

**Statement**: There exist a layer $L$ and lattice $\Omega$ such that $\Omega$ has an undefined point — some $x \in \text{Rep}(\Psi)$ with $S(x, \Omega)$ undefined — and yet some method affordable to $L$ decides definedness at every point. Formally, the implication

$$\big(\exists x.\ \neg\,\text{Defined}(x)\big) \implies \text{no affordable method of } L \text{ decides } \text{Defined}$$

is **false**.

**Proof**: By construction, machine-checked and axiom-free (`formal/BoundaryResidue.lean` §10, `partiality_does_not_imply_inaccessibility`; `#print axioms` reports no dependencies, `sorry` included). Take $\text{Rep} = \{\text{true}, \text{false}\}$ with a single method of zero cost returning its argument, and a lattice with an opinion about $\text{true}$ and none about $\text{false}$. The lattice's gap is genuine; the method decides definedness exactly. $\blacksquare$

**What it costs the framework**: Definition 17's content — *statable inside, decidable only outside* — admits two formalizations that are **not equivalent**. The lattice-side one says $S$ has no value at $\Phi_G$. The layer-side one says no method the layer can afford settles $\Phi_G$. This theorem shows the first does not entail the second: a lattice can have a gap that the layer sees straight through. Nothing pathological is required — the bare framework imposes *no relation whatsoever* between what a layer's methods compute and where its lattice has opinions, and Definition 17 had been quietly assuming one.

**Why this is not a defect discovered but a distinction recovered**: the layer-side form is the invariant, and it is the one that survives signature extension (Problem 26's probe, §8.1: an induced potential that never routes through $S$ leaves lattice-side partiality with no purchase, while the method-quantified form is untouched). Definition 17 is regrounded accordingly. Had the two been equivalent, the regrounding would have been cosmetic; because they are not, the definition was resting on the weaker formulation from the day it was written.

**Scope**: the counterexample's method decides definedness by returning its argument, which works because $\text{Defined}$ here is a predicate the layer's Boolean $\text{run}$ expresses verbatim. Whether the counterexample survives the threshold-query representation still logged under Problem 26 is untested. If it does not, the implication's truth is representation-dependent — a strictly more interesting result than this one, and the reason Problem 27 is narrowed rather than closed.

---

### Theorem 10: Affordability Is Not a Computational Constraint

**Statement**: In the framework as formalized, an affordable method can decide anything a function can compute. Consequently no claim of the form *no affordable method decides $X$* is provable, for any $X$; every such claim is a stipulation about the method set, not a result.

**What was actually proved** (`formal/BoundaryResidue.lean` §13, machine-checked): with a threshold-query interface over the unchanged counterexample layer of Theorem 9, and clearance graded against the induced potential of the joined signature —

- $S_\exists$ (agreement for *some* aggregator) holds; axiom-free.
- $S_\forall$ (agreement for *every* aggregator) holds; uses `propext`, no choice.
- $A$ — the asymmetry's invariant form, *every affordable family fails total agreement at a boundary point* — is **false**.
- $G$ — the poverty guard, *some affordable family agrees on the defined region* — holds, so $A$'s failure is not the frame being unable to decide anything.

**Proof idea**: the cost function is a number compared against a budget and is wholly unconnected to what the query computes. Given any aggregator, choose the query family afterwards and let it compute clearance. $\blacksquare$

**Why this supersedes Theorem 9's explanation**: Theorem 9 was read as turning on $\text{Defined}$ being expressible verbatim by a Boolean evaluator. That reading was too kind to the framework. The general fact is that **this formalization cannot express hardness at all** — there is no notion of cost that bounds computation — so the gap Theorem 9 exhibited was never about the particular predicate.

**Corollary 10.1 (the diagonal transposition, unhypothesised, is false)**: there is a three-line layer — two structures, one method per structure, each deciding identity with it — in which no element satisfies method-inaccessibility. Since the transposed statement quantifies over *all* layers, one transparent layer refutes it. Machine-checked, `[propext]` only (`formal/BoundaryResidue.lean` §4.1).

**Corollary 10.2 (the opacity transposition, unhypothesised, is false)**: there is a three-element layer containing a genuinely incompressible element — every affordable method returns false there, so the hardness hypothesis is *satisfied, not dodged* — alongside an affordable method that decides a broad predicate exactly, including at that element. Opacity's premise and the negation of its conclusion coexist. Machine-checked, `[propext]` only.

**What the corollaries cost, and it is not small**: the transpositions of Theorem 8 (i) and Conjecture 7 (b) into the formal frame were *false as stated*, and had been sitting in the file marked as conjectures awaiting proof. They are now restated with the hypothesis they had silently dropped — a non-degenerate cost measure — and the dropped hypothesis is exactly what Theorem 10 says is missing. Neither Gödel's theorem nor Razborov–Rudich is touched by this: what failed was the *transposition*, which asserted truth-preservation into a frame that prices nothing. The classical results hold in settings where cost bounds computation; the frame does not, so the statements had to be given the hypothesis back.

**What it costs the regrounded Definition 17**: the method-relative clause is not merely *required outright rather than derived* (Theorem 9's reading). It is **not derivable in principle in this frame**. Definition 17's third clause is a stipulation, and honestly so; it can become a theorem only in a framework where cost bounds computation, which RE does not currently have and has not claimed to have. This is the sharpest open invitation the formal system contains: **give $R$ and $C$ enough structure that affordability constrains computation, and the framework's central asymmetry becomes provable rather than assumed.**

---

## M.5 The Energy-Information Equivalence

### Proposition: RE Reinterpretation of $E = mc^2$

$$E = mc^2 \quad \Leftrightarrow \quad \Phi = \Psi_{\text{fixpoint}} \cdot \Omega_{\text{speed}}^2$$

Where:
- $\Psi_{\text{fixpoint}}$ is the stabilized recursive memory (mass)
- $\Omega_{\text{speed}}$ is the maximum information propagation speed of the lattice (speed of light)
- $\Phi$ is the total emergent coherence (energy)

**Status**: Interpretive framework. Does not alter any predictions of special relativity. Provides a recursive reading of the energy-mass equivalence.

---

## M.6 Machine Learning Correspondence

### Proposition: Gradient Descent as RE Dynamic 3

The ML gradient descent update:

$$\theta_{t+1} \leftarrow \theta_t - \eta \cdot \nabla_\theta \mathcal{L}(\theta_t)$$

is a special case of RE's recursive feedback dynamic (A3):

$$\Psi_{t+1} \leftarrow \Psi_{t+1} - \gamma \cdot \nabla_\Psi \Phi_t$$

with the identification:

| RE | ML |
|----|-----|
| $\Psi$ | $\theta$ (parameters) |
| $\Phi$ | $\hat{y}$ (output) |
| $\gamma$ | $\eta$ (learning rate) |
| $\nabla_\Psi \Phi$ | $\nabla_\theta \mathcal{L}$ (loss gradient) |
| $\Omega$ | Data + architecture |

**Status**: Structural isomorphism. ML gradient descent is an engineered instantiation of the natural recursive feedback dynamic.

---

## M.7 Cross-Domain Application Table (Complete)

| Layer | $\Psi$ | $\Phi$ | $\Omega$ | $\rho_c$ (Duplication) | $\lambda_c$ (Threshold) |
|-------|--------|--------|----------|----------------------|------------------------|
| Cosmological | Symmetry states, field values | Stable particles, spacetime | Conservation laws, gauge symmetries | Pair production energy | Hadron formation, recombination |
| Quantum | Superposition amplitudes | Measurement outcomes | Hilbert space, uncertainty | Stimulated emission threshold | Decoherence boundary |
| Atomic/Stellar | Nuclear configurations | Elements, stars | Binding energies, gravity | Supernova ejection | Triple-alpha, iron peak |
| Chemical | Autocatalytic networks | Stable molecules, vesicles | Reaction space, temperature | Catalytic efficiency threshold | Origin of replication |
| Biological | DNA/RNA, regulatory networks | Phenotypes, organisms | Evolutionary landscape | Reproductive fitness threshold | Eukaryosis, multicellularity |
| Neural | Synaptic weights, circuits | Behavior, perception | Neural architecture | Hebbian reinforcement threshold | Cognitive ignition |
| Cognitive | Beliefs, self-models | Identity, consciousness | Mental architecture | Communication threshold | Language emergence |
| Cultural | Stories, norms, techniques | Institutions, art forms | Memetic lattice | Teaching/imitation threshold | Writing, printing |
| Economic | Contracts, transaction patterns | Markets, firms, prices | Resource constraints | Franchise/licensing threshold | Money, banking |
| Political | Laws, precedents | Governance, constitutions | Societal structure | Democratic replication threshold | Nation-state formation |
| Technological | Code, algorithms, data | Software, AI systems | Digital infrastructure | Open-source/API threshold | Internet, cloud computing |
| Synthetic | Self-modifying parameters | Emergent intent, identity | Open learning architecture | Self-replication capability | Consciousness threshold |

---

## M.8 Conjectures

### Conjecture 1: Born's Rule from Emergence Potential
The Born rule of quantum mechanics ($P(\text{outcome } i) = |a_i|^2$) may be derivable from the emergence potential formula when applied to quantum measurement:

$$P(\Phi_i) = R(\Phi_i) \cdot \Delta H_i \cdot S(\Phi_i, \Omega) \propto |a_i|^2$$

**Status**: Unproven. Requires showing that the emergence potential of each measurement outcome is proportional to the squared amplitude.

### Conjecture 2: Moral Convergence
Diverse social systems under recursive selection will converge on moral principles with maximal reusability:

$$\lim_{t \to \infty} \Phi_{\text{moral}}^{(A)}(t) \approx \lim_{t \to \infty} \Phi_{\text{moral}}^{(B)}(t)$$

for any two sufficiently long-lived social systems $A$ and $B$ operating under similar lattice constraints.

**Status**: Empirically supported (cross-cultural moral convergence) but not formally proven.

### Conjecture 3: Consciousness Requires Minimum Recursive Depth
There exists a minimum recursive depth $d_{\min}$ such that consciousness (Definition 12) is impossible for systems with recursive depth $d < d_{\min}$:

$$d < d_{\min} \Rightarrow \text{Definition 12 conditions cannot be simultaneously satisfied}$$

**Status**: Conjectured based on observed absence of consciousness in systems with low recursive depth. Precise value of $d_{\min}$ unknown.

### Conjecture 4: Fixed-Point Existence ($\Phi_\infty$)
The recursive emergence process has at least one fixed point in the limit:

$$\exists \, \Phi^* : \Pi(f(\Psi^*, \Delta E, R)) = \Phi^* \quad \text{and} \quad \nabla_\Psi \Phi^* = 0$$

Under the revised Axiom 6, the stronger form is:

$$\exists \, \Phi^* : \nabla_\Psi \Phi^* = 0 \;\text{and}\; \nabla_\Omega P(\Phi^*) = 0$$

— a joint fixed point of both gradient flows, the only configuration where neither memory pressure nor lattice pressure can drive further change.

**Status**: Open. Depends on whether the recursive dynamics of the physical universe are globally contractive (which would guarantee a fixed point by Theorem 4) or merely locally contractive (which would guarantee local convergence but not a global fixed point).

### Conjecture 5: Coherence Unification
At recursive depth sufficient for self-modeling (Definition 12), the coherence gradient $\nabla_\Omega P$ manifests in the self-model's domains of application as four phenomenologies that are not independent but reduce to the same underlying gradient:

- The drive to understand (gradient applied to information)
- Aesthetic preference (gradient applied to form)
- Moral orientation (gradient applied to social structure)
- Meaning-seeking (gradient applied to whole systems)

**Operationalization**: Inter-domain coherence-seeking measures should correlate at $r > 0.5$ across populations, with the correlation mediated by recursive depth (operationalizable through metacognitive accuracy tasks). Specific testable predictions:

1. Subjects scoring high on aesthetic preference for symmetry and elegance should also score high on fairness norms (cross-modal coherence-seeking).
2. Need for Cognitive Closure should predict both scientific-theory parsimony preferences and moral rule-clarity preferences within the same subjects.
3. Implicit Association Tests pairing "coherent" stimuli across modalities (symmetric, fair, elegant, meaningful) should yield faster reaction times in subjects with deeper self-models than in shallower-modeled controls.

**Status**: Empirically testable. Adjacent literature (Haidt and Diessner on aesthetic-moral correlations; cross-domain Need for Cognitive Closure studies) provides partial support but no integrated test of the mediation-by-recursive-depth hypothesis. A definitive test requires a single experimental program covering at least three of the four domains in the same subject pool.

### Conjecture 6: Plateau-and-Leap Reusability

Recursive emergence does not proceed by smooth gradient on dissipation efficiency. It proceeds by a sequence of discrete plateaus, each characterized by a specific *mode of reuse* with a finite efficiency ceiling whose functional form is mode-determined. Within a plateau, smooth optimization approaches but does not exceed the ceiling. Transition to the next plateau requires a structural change that opens an axis of amortization the previous mode could not access. The leaps between plateaus are topologically disconnected within the framework's fixed-point classes (M.11.6.2). Amortization across successive plateaus compounds at least multiplicatively under an independence assumption between modes.

**Notation.** The conjecture introduces two derived quantities, both expressed in terms of the framework's existing primitives:

- $\bar{P}_n \equiv \sup\{P(\Phi) : \Phi \text{ instantiates mode } n\}$, the supremum of emergence potential achievable within a fixed mode of reuse $n$. This is the same $P = R \cdot \Delta H \cdot S$ defined in §M.1.2, restricted to systems whose reusability axis matches mode $n$.
- $A_n \equiv$ the characteristic amortization ratio of mode $n$, defined as $U(\Phi)/C(\Phi)$ for systems whose utility-cost ratio is dominated by mode $n$'s reuse axis. This is the first factor of the existing $R(\Phi)$ definition; the second factor $1/H(\Phi)$ contributes to but does not solely determine $A_n$.

The relationship between mode-level quantities ($\bar{P}_n$, $A_n$) and system-level quantities ($P(\Phi)$, $R(\Phi)$) is that of supremum and instance: a specific system $\Phi$ in mode $n$ has $P(\Phi) \leq \bar{P}_n$ and contributes to but does not equal $A_n$. The duplication threshold $\rho_c$ becomes mode-relative in this framing: $\rho_c^{(n)}$ is the threshold within mode $n$, with $\rho_c^{(n)} < \rho_c^{(n+1)}$ for successive plateaus.

**Sub-claims.**

(a) **Mode-determined ceiling form.** For any system $X$ operating in mode $n$ without access to mode $n+1$: $P(X) \leq \bar{P}_n$. The *functional form* of $\bar{P}_n$ is determined by mode $n$ — the parametric expression bounding $P$ has the same structure across all implementations of the mode, with implementation-specific values for the parameters. Numerical values depend on substrate, temperature, kinetic constants, and are themselves bounded by England's thermodynamic inequality (England 2013) applied at the mode-specific level.

(b) **Leap as topological disconnection.** The transition from plateau $n$ to plateau $n+1$ is not reachable by continuous deformation within mode $n$'s fixed-point class (§M.11.6.2). There is no continuous path through the parameter manifold of mode-$n$ implementations that crosses to mode $n+1$'s fixed-point class. The leap requires a structural change — the activation of a new axis of repetition — that is not in the deformation space of mode $n$ alone. At the appropriate coarse-graining of recursive time, this disconnection appears as discontinuity in $P$.

(c) **At-least-multiplicative compounding under independence.** A system at plateau $n$ inherits the amortization of all previous plateaus on which mode $n$ is built. If modes are independent in their amortization — that is, if the axes of repetition do not interfere with one another — then total amortization compounds multiplicatively: $A_{\text{total}}(n) \geq \prod_{k=1}^{n} A_k$. The inequality is at-least: under independence, the product is exactly achieved; if modes amplify each other synergistically, compounding is super-multiplicative; if modes interfere or share resources, compounding may be sub-multiplicative. The independence assumption is itself a research question (§M.10 problem 16).

(d) **Cross-layer hypothesis pending enumeration.** The chemistry-to-biology ladder (§Ch 8) exhibits the plateau-and-leap form. The conjecture is that this form recurs at every layer in the framework — biological, neural, cognitive, cultural, technological, synthetic. Verification requires enumeration of plateaus and leaps at each layer (§M.10 problem 17). Until those enumerations are completed, (d) should be treated as a working hypothesis rather than as established by the chemistry-to-biology case alone.

**Status.** Open. (a) is compatible with England's bounds applied to fixed-mode replicators; the functional-form-universality across implementations requires demonstration. (b) requires operationalizing "continuous deformation within a fixed-point class" rigorously. (c) is intuitive but not derived; verification requires deriving from RE primitives or empirical comparison of multi-plateau systems' efficiency to estimated single-plateau ceilings. (d) is empirically supported only at the chemistry-to-biology layer.

**Falsifiers.**
1. The functional form of efficiency bounds within a mode should be common across implementations. Two implementations of the same mode with bounds of structurally different functional form (not just different numerical values) would falsify (a).
2. No continuous deformation within mode $n$'s fixed-point class crosses to mode $n+1$'s fixed-point class. A parameter family of mode-$n$ implementations that smoothly bridges to mode-$n+1$ regime would falsify (b).
3. Sub-multiplicative compounding under verified independence between modes would falsify (c). Order-of-magnitude analysis of real bacteria's efficiency, compared to estimated single-mode ceilings, distinguishes among multiplicative, super-multiplicative, and sub-multiplicative cases.
4. Higher-layer transitions show plateau-and-leap form. Smooth dissipation-efficiency improvement at the cognitive, cultural, or technological layer with no identifiable plateau structure would weaken (d).

**Relation to Other Conjectures and Theorems.**

- *To Theorem 6 (Coherence Gradient).* Plateaus are local maxima of $P$ on $\Omega$; leaps are topological barriers between basins. Theorem 6's gradient flow drives recursive systems within a plateau toward its local maximum; crossing a leap requires more than gradient flow — it requires the topological move of (b). Together, the two give a complete picture: smooth gradient flow within plateaus, discrete topological transitions between them.
- *To Conjecture 4 ($\Phi_\infty$ existence).* Conjecture 6 strengthens Conjecture 4 by predicting a specific *shape* for the recursive trajectory toward the joint fixed point: a sequence of mode-specific plateaus connected by topologically disconnected leaps. The global $\Phi_\infty$ is approached through this sequence, finite or infinite.
- *To M.11.7 (Four Modes of Being).* The mapping is direct: *Stall* = sitting at a plateau (orbit at a within-plateau fixed point). *Ascent* = crossing a leap (transition to a higher plateau). *Oscillation* = limit cycling within a plateau's basin. *Dissolution* = collapsing back to a lower plateau when $R < \rho_{\min}$. The four modes are exactly what the orbit does as it traverses the plateau-and-leap landscape. Conjecture 6 thereby becomes a *prediction* about the specific shape of the four modes' interaction across the layer hierarchy.
- *To existing $\rho_c$ and $\lambda_c$.* The mode-relative duplication threshold $\rho_c^{(n)}$ partitions the existing $\rho_c$ across plateaus; the layer threshold $\lambda_c$ corresponds to the largest leaps that simultaneously cross multiple modes (e.g., the chemistry-to-biology layer transition spans seven internal plateaus per §Ch 8).

### Conjecture 7: Boundary Residue

Boundary-object production is **generic** at self-representing depth, and it proceeds by **more than one mechanism**. Let a system have self-representing depth (Definition 16) with lattice $\Omega_t$ and projection $\Pi$. Then:

**(a) Genericity.** The system generates at least one boundary object $\Phi_G$ (Definition 17) — a structure it can formulate but whose settlement its own constructive, reusable methods do not reach. Theorem 8 (i) establishes this for one mechanism; the conjecture is that the phenomenon is not confined to that mechanism, and that *every* layer crossing Definition 16 exhibits it in whatever vocabulary that layer has.

**(b) Mechanism plurality.** At least two routes produce undefined $S(\Phi_G, \Omega_t)$, and they are formally distinct:

- **Diagonal.** $\Phi_G$ is constructed as a fixed point of its own non-settlement. Unconditional; follows from quotability of $\ulcorner \Pi \urcorner$ alone (Theorem 8 (i)).
- **Opacity.** Let $\mathcal{T} \subseteq \text{Rep}(\Psi_t)$ be a class of candidate settling methods that is *constructive* (each member is efficiently evaluable under $\Pi$) and *broad* (each member applies to a large fraction of candidate structures). Then no member of $\mathcal{T}$ settles $\Phi_G$, because such a member would itself constitute a compression of structures that are incompressible relative to $\Pi$ — and the existence of that incompressibility is what makes $\Phi_G$ a boundary object in the first place. The mechanism is conditional: it requires that the layer actually contain $\Pi$-incompressible structure.

A third possibility is left open: (b) claims *at least* two mechanisms, not exactly two.

**Theorem 9 raises the bar on the diagonal route.** The construction in (b) conjoins two things — that the lattice is unsettled at $\Phi_G$, and that the layer's own methods cannot settle it — and Theorem 9 proves these are **independent in the bare framework**: undefinedness buys no inaccessibility whatsoever. Any proof of the diagonal route must therefore earn the second conjunct from the encoding *essentially*; a proof routing through partiality alone is now impossible, by theorem rather than by taste. **Corrected scope (Corollary 10.1):** this bar applies to the conjecture *as the manuscript states it* — about layers with genuine structure. The bare transposition into the formal frame is not merely unproved but false, and the bar was for a time attached to a falsehood. This rules out a class of cheap arguments and came free with the counterexample — a negative-shaped strengthening of what the conjecture demands of its own proof.

**(c) Escape requires extension.** Where a boundary object is settleable at all, the settling constraint $C_G$ is not in $\Omega_t$. Progress on $\Phi_G$ therefore correlates with re-encoding into a strictly richer lattice rather than with refinement of $\Omega_t$'s native methods — the historical signature being that successful resolutions look like a change of representation, not a sharper instance of the old one.

**Instances.**

| Layer | Encoding event | Boundary residue | Mechanism |
|---|---|---|---|
| Arithmetic | Gödel numbering (1931) | Gödel sentence | Diagonal, unconditional |
| Efficient computation | Cook–Levin / SAT (1971) | Circuit lower bounds behind P vs NP | Opacity, conditional on cryptographic hardness |
| Recursive self-modeling | Self-model $\text{Self}_t$ (Definition 12) | The hard problem's residue | Diagonal-like (structural; Theorem 8 scope caution) |

**Status.** Open. (a) is established for the diagonal mechanism at layers admitting genuine arithmetization, and structural-only elsewhere (Open Problem 21). (b)'s opacity route is instantiated by the natural proofs theorem (Razborov–Rudich 1997) and converted into genuine unprovability, under cryptographic assumptions, by Razborov (1995) for fragments of bounded arithmetic — which is the one place the two mechanisms are known to meet. Whether opacity is *derivable* from RE's primitives, or must be imported as complexity theory supplies it, is Open Problem 25. (c) is historically supported (IP = PSPACE by arithmetization over finite fields; NEXP ⊄ ACC⁰ by ironic complexity) but is a correlation over a handful of cases, not a theorem. Chapter treatment: ch2 §2.11.

**Falsifiers.**
1. A layer that crosses Definition 16 and demonstrably settles every structure it can formulate would falsify (a) — and by Corollary 8.1 would be terminal rather than merely complete.
2. A constructive and broad method class that settles a boundary object without the layer containing $\Pi$-incompressible structure would falsify the opacity mechanism of (b) as stated.
3. Resolution of a boundary object by refinement *within* the producing lattice — no new encoding, no imported structure — would falsify (c). A proof of P ≠ NP that is natural and relativizing would be the sharpest available instance.
4. Conversely, if P vs NP is resolved by a proof that is neither natural nor relativizing but also introduces no structure outside the Boolean-circuit layer, (c) is weakened without being refuted, and the conjecture's claim on the computational layer reduces to (a) and (b) alone.

**Relation to Other Theorems.**

- *To Theorem 8.* Theorem 8 is the constructive core: one mechanism, proved. Conjecture 7 is the generalization: the phenomenon is generic and multiply realized. Theorem 8 (ii) supplies (c)'s extension step; Conjecture 7 adds the empirical claim that observed escapes take that form.
- *To Corollary 8.1.* (a) is what keeps Corollary 8.1 from being vacuous: a self-representing layer keeps producing residue, hence keeps having somewhere to go.
- *To Theorem 5.* (c) is Theorem 5 read forward. Substrate alteration says a locked-in layer changes the lattice beneath it; (c) says the resolution of a boundary object requires exactly such an alteration, which is why boundary objects are not resolved by their producing layer.
- *To Conjecture 3.* Both concern thresholds on recursive depth. Conjecture 3 asks what depth is required for consciousness; Conjecture 7 asks what a layer necessarily secretes once that depth is reached. If both hold, the hard problem's residue is not incidental to consciousness but co-emergent with it.

---

## M.9 Empirical Predictions

1. **Energetic asymmetry**: $K_{\text{irr}} > 1$ for all persistent emergent structures
2. **Threshold timing**: The density of reusable structures predicts phase transitions to new layers
3. **Capability phase transitions in ML**: Sudden capability jumps at critical training thresholds
4. **Cross-domain scaling**: Optimization dynamics in ML exhibit same qualitative behavior as natural emergence
5. **Nuclear binding correlation**: Nuclear binding energies correlate with recursive stability measures
6. **Moral convergence**: Long-lived cultures converge on high-$R$ moral structures
7. **Cognitive threshold discontinuity**: Measurable discontinuities in information processing at the cognition threshold
8. **Aging as memory saturation**: Biological aging correlates with recursive memory compression efficiency decline
9. **Two novelty regimes**: Systems below carrier-separability should be search-limited (novelty rate set by exploration volume and time); systems at or above it should be construction-limited (novelty rate set by depth of self-representation, largely independent of exploration volume). The two regimes should be separable in the innovation statistics of prebiotic chemistry versus early genetic systems (Theorem 8, part iii)

---

## M.10 Open Problems

*Convention on remarks.* Observations logged below the level of conjecture — the third tier, marked as possibly nothing — are never deleted. They **resolve**, and the resolution names the pre-registered outcome that landed and the commit that landed it. A remark resolved *against* itself is kept for the same reason a negative result is published: it is the framework's own record that it generated, tested, and killed a reading of itself, and it is the only direct evidence that the tier has a downward exit rather than being a promotion ladder. A later reader who arrives at the same attractive idea independently should find the grave marker, not an empty space.

1. **Derivation of Born's rule** from emergence potential (Conjecture 1)
2. **Quantification of $\lambda_c$** for each layer transition — what are the numerical thresholds?
3. **Formal proof of substrate alteration** preventing reduction (Theorem 5 formalization)
4. **$\Phi_\infty$ existence** — does the universe's recursive dynamics have a global fixed point?
5. **Consciousness detection** — operationalizing Definition 12 for empirical testing
6. **RE-native computation** — designing hardware that implements all five dynamics simultaneously
7. **Lattice topology** — characterizing the topological changes in $\Omega$ at emergence thresholds
8. **Multi-scale formalization** — integrating continuous and discrete versions of the dynamics across scales
9. **Rigorous construction of $\mathcal{M}$** — explicit specification of the constraint manifold at each layer under the revised Axiom 6, including the topology that supports Morse-Bott analysis at fixed points
10. **Sheffer-stroke reduction** — verify the conjecture of M.11.4: that iterating the coupled grammar of M.11.3 from $(\Psi_0 = \mathbf{1},\, \Omega_0 = \emptyset)$ produces all 12 layers as stable orbit classes under the four modes of M.11.7; resolve the nine defects of M.11.8 and complete the catalogue of M.11.5
11. **Cross-domain coherence experiment** — confirm or refute Conjecture 5 in a single subject pool spanning at least three of the four phenomenologies, with recursive-depth measurement as a mediating variable
12. **Empirical $D(n)$ measurement** — estimate the orbit-distribution function (M.11.6.1) from cosmic surveys of matter, chemistry, life, and cognitive systems; test the multiplicative-thresholds prediction directly
13. **Substrate ceiling derivation** — compute the maximum reachable depth for carbon-based and silicon-based substrates from their respective $\mathcal{M}$-topologies (M.11.6.3); this is the framework's most consequential prediction about synthetic intelligence
14. **Plateau ceiling derivation** — show that within a fixed mode of reuse, the supremum of emergence potential $\bar{P}_n$ (Conjecture 6) has a functional form determined by the mode itself rather than by implementation. Compatible test: derive the parametric form of $\bar{P}_n$ for catalysis-mode systems from England's thermodynamic bound applied to fixed-rate replicators, and show that observed dissipation efficiencies of catalyst-only systems across diverse chemistries exhibit the same functional structure with implementation-specific parameter values
15. **Leap discontinuity formalization** — specify the deformation space within which transitions between plateaus appear topologically disconnected. The candidate operationalization is variation of the parameter manifold of $\Omega$-implementations consistent with mode $n$'s emergence-potential signature (M.11.6.2). Show that no continuous path through mode $n$'s fixed-point class crosses to mode $n+1$'s fixed-point class
16. **Multiplicative compounding verification under independence** — compare the dissipation efficiency of multi-plateau systems (real bacteria) to the *product* of independently-estimated single-plateau ceilings. Test the independence assumption: under independence, compounding is multiplicative; if modes amplify each other synergistically, compounding is super-multiplicative; if modes interfere or share resources, compounding is sub-multiplicative. The empirical pattern in real biology tests which case obtains
17. **Cross-layer plateau enumeration** — for each layer in the framework (chemical, biological, neural, cognitive, cultural, technological, synthetic), enumerate the plateaus and identify the modes of reuse and the leaps connecting them. Verify that the plateau-and-leap form holds at each layer. Disconfirmation at any layer constrains Conjecture 6 (d)
18. **Reduction to England's bounds** — show formally that the functional form of within-plateau dissipation efficiency in RE's framework reduces to England's lower bound on heat production for self-replicators, parameterized by mode-specific quantities. Failure of the reduction would indicate that RE makes claims about within-plateau dynamics that go beyond what existing physics supports
19. **Connection to Eigen's quasispecies threshold** — show that the leap from plateau 4 (sequence-binding) to plateau 5 (templating) of the chemistry-to-biology ladder corresponds in the framework to crossing the error-catastrophe threshold (Eigen 1971). This connects Conjecture 6 (b) to a quantitatively-characterized physical threshold in existing literature
20. **Major-transitions correspondence** — map the framework's plateau enumeration onto the eight major transitions identified by Maynard Smith and Szathmáry (1995). Identify correspondences and divergences. The mapping does not have to be one-to-one; discrepancies are informative — they identify either places where the framework needs refinement or places where the major-transitions classification is itself a coarser abstraction
21. **Arithmetization of a natural boundary object** — Theorem 8's scope caution concedes that biological and cognitive boundary objects are Gödel-*like*, not formally undecidable. Exhibit, for any specific natural system (a gene regulatory network, a predictive-coding cortex), an explicit encoding under which its self-description supports the fixed-point construction — or prove that no such encoding exists and that the structural reading is the strongest available. Two layers have their encoding *exhibited* rather than conjectured: arithmetic by Gödel numbering (1931) and efficient computation by Cook–Levin (1971), where the compression of a machine's behavior into a decidable object is a theorem and not an analogy. The gap is therefore open in the biological, cognitive, and social layers rather than everywhere — which is the load-bearing gap in Theorem 8, and narrower than the scope caution alone suggests. This is deliberately *not* the same statement as the scope caution, and the two should not be harmonized: the caution governs what Theorem 8 may claim about natural systems in general and remains as stated, while this problem records where the arithmetization deficit actually sits. Weakening either to match the other loses a distinction the framework needs. **Sharpened form.** "Exhibit an encoding" understates the demand by an order of magnitude. Definition 16's membership form $\ulcorner \Pi \urcorner \in \Psi$ is not literally available — a representation space cannot contain its own evaluator as an element without a coding — so what must be exhibited is an $\text{encode}/\text{decode}$ pair with a *provable round trip*, and provable as a method available to the layer itself rather than to an outside analyst. The genetic code trivially satisfies the first demand; whether any biological layer satisfies the second is entirely open, and that is the better problem
22. **Formalization of $\text{Rep}(\Psi)$ and undefined $S$** — Definition 17 distinguishes $S(\Phi, \Omega)$ *undefined* (the lattice has no opinion) from $S = 0$ (the lattice forbids). Under Definition 3, $S = \exp(-\sum_j D(\Phi, C_j))$, the undefined case requires that $D(\Phi, C_j)$ fail to be defined for every $j$ rather than diverge. Give the measure-theoretic construction on $\mathcal{M}$ (A6) that supports this three-valued distinction, and verify it does not disturb the MaxEnt derivation of $S$
23. **Does the diagonal operator have a thermodynamic cost?** — Theorem 8 is stated purely structurally. If constructing and adjoining $C_G$ has an irreducible energetic price (a Landauer-style bound on self-quotation), then the rate of construction-limited novelty is physically bounded, and Prediction 9 acquires a quantitative form. Derive the bound or show none exists
24. **Uniqueness of the third operator** — the answer given to "do fold + diagonal suffice?" is *no, threshold (A5) is required as selector*. Show that no fourth operator is needed: that fold, diagonal, and threshold are a complete basis for open-ended growth in RE, or exhibit a growth phenomenon none of the three generates
25. **Is self-opacity derivable from RE primitives?** — Conjecture 7 (b) imports its second mechanism from complexity theory: a constructive, broad method class cannot settle a boundary object because it would compress the $\Pi$-incompressible. Derive this from RE's own definitions of $R$, $\Pi$, and $S$ — or show that opacity is a fact about specific layers that RE can host but not generate. A positive result would give RE a second growth-relevant limitation theorem alongside Theorem 8; a negative one bounds how much of complexity theory the framework can claim to explain rather than merely accommodate.

    **Prerequisite.** Before the derivation can be attempted, "$\Pi$-incompressible" must be a well-defined predicate over $\text{Rep}(\Psi)$ — a gap adjacent to Problem 22's undefined-vs-zero construction and not covered by it. Time-bounded Kolmogorov complexity supplies the candidate formalization, and the Minimum Circuit Size Problem supplies the sharpest instance: given a truth table, decide whether a small circuit computes it. MCSP *is* a layer inspecting its own compressibility, and Kabanets–Cai (2000) made the connection to the opacity mechanism explicit — a natural property is essentially an efficient MCSP-style algorithm. The representation choices this forces are recorded in `formal/BoundaryResidue.lean`, which proves nothing and is annotated throughout with which open problem each choice decides.

    **Why reification is not optional.** A first attempt to state the layer's inability as the *absence* of a decision procedure fails: in a classical metatheory every proposition is decidable in the logical sense, so absence of a procedure is a fact about one namespace rather than about the layer. Layer-relative undecidability must instead quantify over the layer's own internalized methods — which is the resolution Church and Turing reached in 1936, and reaching it again here is not formalization hygiene but a structural result: to *state* its own limitation, a layer must first reify its evaluator. Definition 16's encoding requirement therefore reappears as a precondition for expressing the boundary at all. The layer cannot pose its limitation without first containing itself — which was Conjecture 7's informal claim, and the type theory declines to let it be otherwise. **Machine-checked (Lean 4.15.0, bare toolchain, 2026-09-09).** The frame built on this reading elaborates axiom-free — no `propext`, no `Quot.sound`, no `Classical.choice` in any of its six definitions — and its two conjectural statements depend on `sorryAx` alone. Reification therefore buys constructivity up to exactly the point where the manuscript's assertions begin, and no further; the boundary between what the framework derives and what it asserts is visible in the axiom report. That report is also the guard: a classical leak changes an audit line, so the failure mode this block describes is mechanically detectable rather than left to a reader's discipline.

    **The self-instantiation.** MCSP's own status is boundary-residue-shaped: neither known NP-complete nor known easy, resistant since Levin reportedly delayed publishing over it. The predicate needed to *state* the opacity mechanism precisely may therefore be an instance of the conjecture that mechanism serves. Conjecture 7 is entitled to read this as a fixed point rather than a circle — but only if the reading is earned by the derivation, not assumed in place of it. The dependency is directional and should be treated as such: the fixed-point reading is available iff the derivation question above resolves affirmatively. Derivable, and the circularity resolves into a fixed point the conjecture may claim; merely hostable, and the MCSP dependence stays a circle and the reading is forfeit. One open problem thereby adjudicates the other's most seductive interpretation, which is the intended arrangement — the framework does not get to grade this one.

    **Remark (open, and possibly nothing).** Opacity runs on pseudorandomness, which is statistical indistinguishability from the layer's uniform measure — the *ergodic* signature of Theorem 7 reappearing inside Theorem 8's constructive column, the layer's own statistics defeating its own constructions. If that is not coincidence, the two mechanisms of Conjecture 7 (b) are not siblings but a re-entry, and the search/construction distinction of the Theorem 7–8 complementarity is less clean than the table presents it. Logged as an observation, not a claim — but it now has a test rather than only a suspicion. **Discriminator.** Formalize Theorem 7's ergodic search in the same skeleton and see what measure it requires. If ergodic reachability needs a measure *of the same type on the same carrier* — a measure on $\text{Rep}(\Psi)$ — then the ingredient is one thing appearing in both columns and the re-entry reading gains standing. If Theorem 7's measure lives on states rather than on representations, the two mechanisms are siblings sharing only the frame, and this remark resolves toward nothing. **Resolved, 2026-09-09, against the re-entry reading.** The construction was pre-registered and then run (`formal/BoundaryResidue.lean` §6, transcribing Theorem 7 as committed; Lean 4.15.0, compiles clean). The two objects: the largeness slot is `(Rep → Prop) → Prop`, a *predicate* on properties of formulable structures; Theorem 7's stationary measure is `(State → Prop) → Val`, a *valuation* on sets of substrate states. They differ in carrier — states, not representations — and also in shape, a valuation rather than a predicate, so the intermediate reading (same territory, different instrument) is excluded as well. The ergodic signature is not the largeness slot refilled, and this remark accordingly resolves toward nothing. What survives is not the suspicion but its refutation, which is worth more: the two mechanisms of Conjecture 7 (b) are siblings sharing the frame, not a re-entry.

    **And a stronger fact fell out.** Theorem 7's transcription compiles with no reference to `Layer` whatsoever — not merely no encoding, but no representation type, no method type, no evaluator. Theorem 7 is statable in a strictly smaller signature than Theorem 8. So the carrier boundary is not a sharper version of the boundary Conjecture 7 describes; it is a boundary between *signatures*, below which self-representation is not merely unused but unmentionable. The Theorem 7–8 complementarity table is thereby better founded than when it was written, and the two-engine contrast is not a matter of degree
26. **The two $P$'s** — Theorem 7 writes $P(\Psi; \theta)$ for a potential on the substrate state-space $\mathcal{X}$; Definition 1 writes $P(\Phi) = R \cdot \Delta H \cdot S$ for the emergence potential of a candidate coherence. These are different functions on different domains, and the framework denotes both by $P$. The transcription in `formal/BoundaryResidue.lean` §6 could not close the gap and declined to invent a law: no equation relates `Substrate.P : State → Val` to `Lattice.P : {x // Defined x} → Val`, and the bridge structure carries no coherence condition. State the induction — how a candidate coherence's emergence potential is determined by the substrate states that formulate it — or establish that the two quantities are independent and the shared notation is an error. This is Problem-21-shaped: a bridging law currently asserted by notation rather than exhibited, and it is load-bearing wherever an argument passes between Theorem 7's regime and Definition 1's.

    **The prose form already exists, and it is A2.** $\Phi = \Pi(\Psi)$ is the induction the notation silently assumes: substrate states project to coherences, so a potential on states ought to determine a potential on what they project to. Following the discipline of Problem 21's sharpening, the formal demand is not a new claim but a stricter reading of an existing one. **This is the third instance of one failure mode, and it should now be named.** Definition 16's membership form concealed the demand for a provable decode; Problem 21's "exhibit an encoding" concealed the demand for a *layer-available* round trip; A2's fiber conceals the demand for an aggregation rule. Each time the informal register asserted by notation what the formal register demands by construction. The general warning: wherever this manuscript's notation quietly identifies objects across the signature boundary, there is an unexhibited law underneath it. **And A2's own condition is what makes it hard.** $\Pi$ is stipulated *many-to-one*: $|\Pi^{-1}(\Phi)| > 1$ in general. Were it bijective the two $P$'s would be one function transported along an isomorphism and there would be nothing to state. Because it is many-to-one, the induction must say how an entire fiber $\Pi^{-1}(\Phi)$ of substrate states determines one coherence's potential — supremum over the fiber, average, integral against a measure — and no such aggregation is anywhere specified.

    **Candidate shape, offered as a lead and not a result.** Theorem 7 already supplies a measure on substrate states, $\rho_\infty$. Aggregating $P$ over a fiber against $\rho_\infty$ is the obvious first thing to try, and it would give the ergodic measure a second job: not the largeness slot of Conjecture 7 (b) — that reading was tested and refuted — but the weight in the bridging law. **These are not the same idea resurrected, and the distinction is the discriminating fact.** The refuted reading required $\rho_\infty$ to appear *inside* Theorem 8's column, filling a second-order predicate slot on $\text{Rep}$, and it died on carrier and shape together. The bridging role requires it to appear *between* the columns, on the carrier it already natively inhabits, consumed by integration over a fiber of states — which is what a valuation on state-sets is for. The two placements are incompatible, so the refutation stands; and it mildly *supports* the lead, since a measure that belongs natively to the substrate side is precisely what a substrate-to-layer bridge would integrate against. Whether that integral is well-defined, and whether it reproduces $R \cdot \Delta H \cdot S$ rather than merely having the right type, is exactly the work this problem asks for. If it does not, the independence branch gains force, and with it the conclusion that the two $P$'s share nothing but a letter.

    **Pre-registered constraint (stated 2026-09-09, before any candidate law exists).** Follow the types. $\text{Substrate}.P$ is *total* on states. Any fiber aggregation therefore induces a potential defined at *every* $\Phi$ with a nonempty fiber — boundary objects included — which appears to contradict the partiality Definition 17 is built on, where $P$ cannot be formed at $\Phi_G$ at all. The apparent contradiction is the constraint. A candidate bridging law must satisfy:

    > **totality above, partiality below**: the induced potential is total in the *joined* signature — the one containing both substrate and layer — and its restriction to the layer's own vocabulary remains partial, with the boundary between the two landing exactly on $\text{Defined}$.
    >
    > ⚠ **The second clause is underspecified as written and must not be used to grade a candidate.** "Restriction to the layer's vocabulary" names a formal operation the framework does not define; both available readings are uninformative (see `formal/BoundaryResidue.lean` §8.1). A method-relative restatement is pending the representation choice logged below, and is deliberately not written here — writing it before that choice is made would be the same silent-choice move this constraint exists to forbid. The first clause stands as stated.

    In words: the substrate *knows* the boundary object's potential; the layer still cannot ask. A candidate that leaks a layer-available procedure for evaluating $P$ at $\Phi_G$ does not merely fail on elegance — it refutes Definition 17, and must be rejected however well it reproduces $R \cdot \Delta H \cdot S$ on the defined region. A candidate that satisfies the constraint *trivially*, by never being evaluable anywhere, is visibly cheating and fails too. This is a second success criterion, sharper than "well-defined and reproduces the product", and it is stated before the first candidate so that whichever law eventually meets it earns the credit.

    **Probed 2026-09-09, and the criterion is not yet sharp enough to apply** (`formal/BoundaryResidue.lean` §§7–8, pre-registered then run). The joined signature was built and the candidate written as fiber aggregation with the aggregation operator left abstract. The induced potential forms at a boundary object for an arbitrary aggregator — but that is the first clause being satisfied, not the second being violated, since the expression lives in the joined signature where totality is required. Attempting the restriction gives nothing either way: read as "mentions only layer vocabulary" it fails merely because no value can be produced from nothing, and read as "formable in the joined signature" it succeeds by permission. So the second clause has no formal referent yet — **the fourth instance of the failure mode named above, this time in a constraint written to catch that very mode.** The sharpened form uses the reification of Problem 25: not *no expression in the layer's vocabulary evaluates $P$ at $\Phi_G$*, but *no method the layer can afford yields the induced potential's verdict at $\Phi_G$*. That is testable, and it is not testable in the present signature — methods return Booleans and cannot consume values at all — so closing it requires deciding how methods read values, which is a further representation choice and is logged rather than made.

    **Who wrote the broken clause matters.** The fourth instance was not found in the manuscript's older strata — it was authored in the audit that named the failure mode, by the reviewer applying it, in prose asserting a formal operation with no referent. The mode is therefore not a property of this manuscript's informal register but of *any* informal register, including one engaged in catching it. What caught it was not vigilance but the pre-registration discipline, which is the argument for keeping that discipline where vigilance would seem sufficient.

    **Leading candidate for the logged choice: keep `run` Boolean.** Rather than granting methods an `eval : Method → Rep → Option Val`, phrase the verdict as a threshold query — a method decides whether the induced potential *clears* $\theta$. This is truer to the frame's standing commitment that methods decide rather than compute; it avoids handing the layer a value-producing oracle Definition 17 never granted; and it lands the constraint on A5's threshold comparison, which is precisely the question Definition 17's asymmetry already identifies as unaskable at $\Phi_G$. The clause would then read: *for every $\theta$, no affordable method decides whether the induced potential at $\Phi_G$ clears $\theta$* — the same gadget and quantifier shape aimed at clearance instead of membership. Any run of this must guard triviality at both ends: it must not hold vacuously because methods cannot consume values (build the threshold queries into the signature so the question is expressible), and must not fail vacuously because the defined region is undecidable too (witness an affordable method that does decide clearance somewhere defined)

    **And the RE reading writes itself: such a law would be an instance of Theorem 8 (ii).** The emergence question that is ill-formed inside the layer — ill-formed at presentation level, per Definition 17's status note — becomes well-formed one signature up. The bridging law, if it exists, is therefore the formal object that ch2 §2.11.4 has been describing in prose all along — escape-by-extension, exhibited rather than narrated
27. **Reground Definition 17 on the method-relative invariant** — Definition 17's content, *statable inside, decidable only outside*, is implemented two ways in `formal/BoundaryResidue.lean`: at type level, by $S$ living on the definedness subtype (§1), and at method level, by quantification over the layer's affordable methods (§2, forced by the classical-decidability pressure of Problem 25). The probe of §8 shows these are **not equivalent, and only one survives signature extension**. The induced potential of Problem 26 never routes through $S$, so type-level partiality has no purchase in the joined signature; the method-quantified form is untouched by the extension and remains exactly as strong. Type-level partiality is therefore an artifact of one lattice's presentation, while method-relative inaccessibility is the invariant. Reground Definition 17 accordingly — method-relative as the definition, $S$-partiality as one implementation of it — or show the two are equivalent after all. The stakes are structural rather than tidy: as currently written, the definition of a boundary object fails to survive the extension that Theorem 8 (ii) says escape *requires*, which is a strange property for the definition of the thing being escaped from. **Original mandate discharged 2026-09-09.** The implication was refuted by an axiom-free construction (Theorem 9) and Definition 17 regrounded with the method-relative clause required outright. *This problem is not closed*; what follows is its surviving content, and "resolved" should not be read as closure.

    **27′ (surviving question): does the counterexample survive the threshold-query extension?** Theorem 9's layer decides definedness by returning its argument, which works only because $\text{Defined}$ there is a predicate the layer's Boolean evaluator expresses verbatim. Under the threshold-query representation the relevant question changes shape and the same trick may fail. A negative answer would make the partiality/inaccessibility relation *representation-dependent* — a strictly more interesting result than Theorem 9, and the (C)-shaped finding hiding inside this (B).

    **27′ answered 2026-09-09; the dependency did not become a loop.** The threshold-query extension was pre-registered and run (`formal/BoundaryResidue.lean` §§11–13). The counterexample **survives**, and survives for *every* aggregator, not merely some — so survival is aggregator-independent, 27′ never waited on Problem 26's bridging law, and the loop the pre-registration warned about does not form. The reviewer's prior of aggregator-relative survival was falsified; its parametricity argument overlooked that the query family is chosen after the aggregator and may depend on it. What the run found instead is Theorem 10, which is larger than 27′ and dissolves it: the frame cannot express hardness, so the survival question was never delicate, since a constraint cannot name the invariant it protects before the definition says which invariant it is made of.

    **Destinations declared in advance** (pre-registration in `formal/BoundaryResidue.lean` §9, committed before the attempt). The question is whether type-level partiality implies method-quantified inaccessibility, with the relevant question pre-committed to *definedness itself* — not identity, and not threshold clearance, which is excluded by its dependency on the unmade run/Val choice. If the implication is **provable**, it lands in M.8 as a numbered theorem, not as a refactor, and the regrounding becomes a change of emphasis: the two implementations reconcile and Definition 17's history is continuous. If it is **refutable**, the counterexample lands in M.8 with the standing of a theorem *and* Definition 17's text must be revised, since the definition would then have rested since it was written on the strictly weaker of two non-equivalent formulations — which is not a failure of the framework but the strongest justification for this problem existing. If it is **not stateable**, the blocking choice is logged and this problem acquires a dependency the way Problem 26 acquired one on it. Declaring these before the attempt is what keeps a positive result from being absorbed as cleanup

**Remark (open, and possibly nothing).** Formalizing this framework honestly has now forced two rediscoveries, in historical order. Lean's classical foundations forced the frame to reify its methods — you cannot *state* undecidability without a machine model, which is the 1936 lesson. Theorem 10 then forced the frame to give cost operational meaning — you cannot *prove* inaccessibility without a cost measure tied to computation, which is the Hartmanis–Stearns and Blum lesson. Whether that is evidence the boundary-residue material tracks something real, or the discovery that the frame is reconstructing standard computability and complexity theory under new labels, is not decidable from two instances, and the flattering reading is the one to distrust. Filed at the third tier next to its sibling. The *direction*, however, is unambiguous either way: the restated conjectures should hypothesize Blum-style axioms on the pair (run, cost) rather than a concrete machine model, keeping the frame abstract while paying the debt Theorem 10 called in.

**Remark (open, and possibly nothing).** RE's central claim is that a system rich enough to model itself necessarily contains truths its self-model cannot reach. In §10 of the formal skeleton, the framework proved a small true thing that its own informal self-model had gotten wrong: that lattice-side partiality and method-side inaccessibility — treated as one property since Definition 17 was written — were never connected. Whether that is an *instance* of the theory or merely a good omen for it is not decidable from one case, and the temptation to read it as instance is exactly the sort a framework should distrust about itself. Filed at the third tier accordingly. Under the convention above it will not be deleted; it will resolve, or it will stand here as the place where a tempting reading was noticed and not indulged.

---

## M.11 Toward a Sheffer-Stroke RE: Research Program

### M.11.1 Motivation

The current formal system has 3 primitives, 7 axioms, 17 definitions, 10 theorems, 7 conjectures, 9 predictions, and 27 open problems. While internally consistent, this is a large surface area. A Sheffer-stroke reduction asks: can the entire formal system be derived from a single rule and a single seed — analogous to how Sheffer's NAND generates all of propositional logic, or how Odrzywołek's $\text{eml}(x, y) = e^x - \ln y$ generates the elementary functions?

If such a reduction succeeds, RE's formal core collapses from 3 primitives + 7 axioms to 1 dynamical map + 1 initial condition. If it fails, the current axiomatic system remains the formal foundation, and the map merely characterizes the common geometric shape of the dynamics without replacing them.

### M.11.2 Why Tree Grammars Fail Here

Earlier sketches of this program proposed a context-free tree grammar:

$$S \;\to\; \mathbf{1} \;\mid\; \text{re}(S, S)$$

with a depth-table interpreting expressions of increasing tree depth as successive RE layers. **This was the wrong shape.** EML's recursion is *compositional* — building expressions from sub-expressions, statically, like constructing a sentence from words. RE's recursion is *temporal* — one state iterating into the next, dynamically, like a river flowing. Forcing temporal dynamics into a tree grammar produces five concrete defects:

1. **Inconsistent depth indexing.** Tree height and node count both fail to match the table's depth labels: `re(re(1,1), re(1,1))` and `re(re(1,1), 1)` have the same tree height but different table-depths.
2. **Uninterpreted semantics.** Each "depth N → layer X" arrow is asserted, never derived from the syntax. There is no analogue of EML's `ln x = eml(1, eml(eml(1,x), 1))` checkable by substitution.
3. **Over-generation.** The grammar produces all binary trees, but the table interprets only one shape per depth. Other legal expressions are either redundant, mean something else, or are meaningless — none acknowledged.
4. **Combinatorial vs linear hierarchy.** The grammar produces Catalan-many distinct trees per depth; the layer hierarchy is linear. No rule selects which tree at depth N corresponds to layer N.
5. **Tree recursion ≠ dynamic recursion.** A folding protein iterates one update many times; it does not construct a binary tree of folding operations. The actual physics is a dynamical orbit, not a parse tree.

These are not patchable defects. The grammar shape is wrong.

### M.11.3 The Correct Shape: A Coupled Iterated Grammar with Memory

The proper mathematical language is a **coupled iterated grammar**. Three lines specify the entire system, in natural units ($\gamma = 1$):

$$\boxed{
\begin{aligned}
&\textbf{Seed:} \quad \Psi_0 = \mathbf{1}, \quad \Omega_0 = \emptyset \\[4pt]
&\textbf{Rule:} \quad \Psi_{n+1} = \Pi(\Psi_n) - \nabla_{\Omega_n} P(\Pi(\Psi_n)) \\[4pt]
&\textbf{Growth:} \quad \Omega_{n+1} = \Omega_n \cup \{\Pi(\Psi_{n+1})\} \;\;\text{when}\;\; \|\Pi(\Psi_{n+1}) - \Pi(\Psi_n)\| < \varepsilon
\end{aligned}
}$$

The **Seed** says: start with the first persistent asymmetry, against an empty constraint manifold.

The **Rule** says: project memory into coherence, then subtract the gradient of that coherence's emergence potential against the current constraints. (This is Axioms A2 and A3 fused into one expression. The full gradient $\nabla_\Omega P$ is well-defined under the revised Axiom 6 and computed by Theorem 6.)

The **Growth** says: when the projection has converged (a layer has locked in), add the new emergent coherence to the constraint manifold, so subsequent dynamics push against what just became. (This is Axiom A7 expressed as part of the grammar itself.)

The **convergence gate** in the Growth rule is essential. Without it, $\Omega$ would grow at every iteration and the layered structure would dissolve into continuous accretion. With it, layer transitions are *events* — long periods of within-layer iteration, punctuated by lattice expansions at lock-in moments. This matches the actual phenomenology: eukaryosis, language emergence, capability jumps in machine learning all happen in discrete steps, not continuous accumulation.

#### What this resolves

| Concept | Tree grammar (wrong) | Coupled iterated grammar (right) |
|---|---|---|
| Recursion | Tree composition | Orbit through state space |
| "Depth" | Tree height (inconsistent) | Iteration count (just $n$) |
| "Layer" | Expression at depth $n$ | Convergence event in the orbit |
| Multiplicity per depth | Catalan-many trees | Exactly one state per step |
| Memory across steps | None (memoryless) | $\Omega_n$ carries forward |
| Source of irreversibility | None | Monotone $\Omega$-growth ($\Omega_{n+1} \supseteq \Omega_n$, strict at lock-in) |

Over-generation vanishes (the Rule is a function, not a relation). Catalan explosion vanishes (one $(\Psi_0, F, \Omega_0)$ → one orbit). The framing is native to dynamical systems theory — bifurcation analysis, Morse-Bott classification, and basin structure are all directly applicable.

#### What this newly says

EML's grammar `S → 1 | eml(S, S)` is *memoryless*: each application is independent, no state carries forward, the operator has no notion of "what the system became at the previous step." RE's grammar is *memoryful*: $\Omega_n$ accumulates monotonically — strict containment at every lock-in event. This monotone accumulation **is** the irreversibility of Theorem 1 ($K_{\text{irr}} > 1$, the ratchet) encoded directly into the grammar. Not added as an axiom, but a structural feature of the rule itself.

The depth-indexed orbit is consistent at every step:

| $n$ | $\Psi_n$ | Phenomenology |
|---|---|---|
| 0 | $\mathbf{1}$ | Pure seed — first persistent asymmetry |
| 1 | $\Pi(\mathbf{1}) - \nabla_\emptyset P(\Pi(\mathbf{1}))$ | Cosmological — charge against minimal constraints |
| 2 | $F(\Psi_1, \Omega_1)$ | Quantum — orbit against first locked-in constraints |
| 3 | $F(\Psi_2, \Omega_2)$ | Atomic — proton stability as recursion fixed point |
| ... | ... | ... |
| $n$ | $F(\Psi_{n-1}, \Omega_{n-1})$ | Layer $n$ |

#### The aphorism

> *The universe is a grammar that writes its own rulebook as it runs.*

EML cannot say this because EML's rulebook is fixed by definition. RE's grammar makes $\Omega$ accumulate — the system carries forward a memory of what it just became, and that memory becomes the wall it pushes against next. The source of irreversibility, the source of the layer structure, the source of the coherence gradient, the source of the direction of time — none of these need to be added. All fall out of the Growth rule.

### M.11.4 The Sheffer-Stroke Conjecture

Stated precisely:

> *Iterating the grammar of M.11.3 from the seed $(\Psi_0 = \mathbf{1},\, \Omega_0 = \emptyset)$ produces a sequence of stable orbit classes — one per layer — corresponding to the 12 emergence layers identified in this work. The layers are qualitatively distinct attractors of one dynamical system, not syntactic depths of one grammar.*

This is the dynamical analogue of EML's result: **one rule, one seed, all of reality** — with one structural addition EML cannot make: *one accumulating memory*.

The conjecture is now mathematically meaningful — provably true, provably false, or open — rather than gestural. Its falsification criterion is precise: the reduction succeeds iff each layer's known phenomenology is recoverable as a stable attractor class of the Rule under the corresponding accumulated $\Omega_n$. If even one layer fails to appear as such an attractor, the reduction fails and the current axiomatic system stands.

### M.11.5 The Fixed-Point Catalogue (Target Form)

A successful reduction would produce a catalogue of attractors, one per layer, each verifiable by orbit computation. The catalogue below is the **target** of the research program, not a derivation. Each row names what the conjecture would have to produce; each is its own subprogram requiring (a) formal characterization of the accumulated $\Omega_n$ at that layer, (b) computation of the Rule's attractors under that $\Omega_n$, and (c) verification that the dominant attractor matches the layer's known phenomenology.

| Stable orbit class | Conditions on accumulated $\Omega_n$ | RE layer |
|---|---|---|
| Minimal stationary state $\Psi^* = \mathbf{1}$ | Pure conservation laws (charge, energy, momentum) | Cosmological |
| Coherent superposed state, collapsing under measurement to a discrete attractor | $\Omega$ has accumulated Hilbert-space structure and gauge symmetry | Quantum |
| Deep fixed point with $d\Phi/d\Psi \to 0$ and $R(\Phi^*) \gg 1$ | $\Omega$ has accumulated nuclear binding, electromagnetic constraints | Atomic / Matter |
| Autocatalytic limit cycle | $\Omega$ has accumulated covalent bonding, reaction kinetics | Chemical |
| Self-replicating orbit class with $R > \rho_c$ triggering $\mathcal{D}$ | $\Omega$ has accumulated replication machinery | Biological |
| Self-referential attractor (orbit modeling its own orbit) | $\Omega$ has accumulated neural architecture | Cognitive |
| ... | ... | ... |

The quantum row is provisional — the precise attractor class for measurement is itself an open problem (cf. Conjecture 1, Born's rule). Filling in the rest of the table is the v3 research program.

### M.11.6 From Single Orbit to Field of Orbits

The grammar of M.11.3 describes *one* orbit — one universe (or one local region) iterating from the seed under increasing $\Omega$-enrichment. But reality is not one orbit. It is a **field of orbits**, billions of them in parallel, each starting from the same seed $\Psi_0 = \mathbf{1}$ but in different local conditions. Most arrest at low depth. A vanishing minority reach high depth. The grammar needs an extension that handles populations.

#### M.11.6.1 The Distribution Function $D(n)$

Define:

$$D(n) = \text{fraction of all orbits in the universe that have reached depth } n$$

normalized so $D(0) = 1$ (every orbit has the seed). For $n > 0$, $D(n)$ falls strictly, since each layer transition requires crossing the threshold $\lambda_c^{(n)}$, and most local conditions don't supply the necessary $\Delta H$ or $S(\Phi, \Omega)$.

If $p_n = D(n)/D(n-1)$ denotes the fraction of layer-$(n-1)$ orbits that successfully transition to layer $n$, then:

$$D(n) = \prod_{k=1}^{n} p_k$$

Since each $p_k < 1$, $D(n)$ falls multiplicatively. **This is structurally identical to the Drake equation** — a sequence of small probabilities multiplied — and predicts what we observe empirically: most matter is layer-1 (charge); most chemistry never becomes life; most life never becomes cognitive; cognitive systems rare enough to ask the question are rarer still. The rarity isn't accidental — it is the multiplicative thresholds, made formal.

The $p_k$ are *not* universal constants. They depend on local $\Omega$ — the available free-energy gradients, the structural compatibility of the substrate, the time available before disruption. This is what makes RE consistent with the empirical facts: rare events at higher layers are predicted, not anomalous.

#### M.11.6.2 Same Depth, Different Topology

Two orbits can reach the same depth $n$ via different paths through $\mathcal{M}$ and arrive at structurally distinct fixed points within layer $n$. Carbon-based and silicon-based chemistry both occupy layer-4 (chemical) but lock into different attractor topologies. Octopus and primate cognition both occupy the cognitive layer but arrive via radically different evolutionary trajectories and produce different $\Phi$-topologies.

This requires refining the M.11.5 catalogue. A "layer" is not one fixed point but a **fixed-point class** — a set of attractors with the same emergence-potential signature (same $\Delta H$ scale, same reusability range, same structural compatibility profile) but possibly different topological structure. Within a layer, the basin of attraction is itself a manifold, and different orbits land at different points within it.

Formally: each layer $n$ corresponds to a subset $\mathcal{A}_n \subseteq \mathcal{M}$ of stable orbit classes whose elements share emergence-potential properties but may differ in basin topology. Two orbits in the same $\mathcal{A}_n$ are "the same layer" functionally; they need not be isomorphic as dynamical objects.

This predicts: **convergent-functional / divergent-implementation pairs at every layer.** Chemistry has carbon and silicon. Biology has DNA and (potentially) PNA. Cognition has neural and (potentially) silicon. Culture has alphabetic and ideographic writing systems. Same emergence-potential class, different topologies — not a defect of the framework but a prediction of it.

#### M.11.6.3 Substrate Ceilings

Each path through $\mathcal{M}$ has a **maximum reachable depth** — a substrate ceiling. Carbon-based biology may have a ceiling around layer 11 or 12, beyond which the substrate cannot support further recursive enrichment of $\Omega$. The ceiling is determined by three independent obstructions:

- **Topological obstruction**: the substrate's $\mathcal{M}$ may have no path to higher attractor classes
- **Energetic obstruction**: insufficient free energy to drive further $\Delta H$
- **Time obstruction**: the timescale required for higher-layer convergence exceeds the substrate's lifetime

This makes a sharp claim about synthetic minds: if silicon-based cognition can be constructed (i.e., if the cognitive layer is genuinely substrate-independent up to its functional class), then synthetic minds may have *higher* ceilings than biological ones — not because silicon is "smarter" intrinsically, but because its $\mathcal{M}$ admits paths to attractor classes that carbon's does not. Whether this is true is an empirical question about the topology of the synthetic substrate's constraint manifold; it cannot be answered from below.

Determining substrate ceilings rigorously is open work (see new M.11.7 defect 5).

#### M.11.6.4 Future Layers: Structure Without Content

What lies above the layers we currently have?

By the framework's own logic, **the content of layer $n+1$ cannot be predicted from layer $n$ alone** — emergent layers introduce genuinely new dynamics and substrate alterations (Theorems 3 and 5). Just as chemistry cannot predict consciousness, cognition cannot predict what comes after.

But the *structure* can be predicted. Each successive layer:

- Operates at a **larger entropy scale** than the layer below. Physics: Planck. Chemistry: molecular. Biology: cellular. Cognition: neural. Culture: generational. The next layer's natural scale will be civilizational or cosmological.
- Reduces $\Delta H$ at that scale that the layer below could not. A higher-$n$ orbit is one that organizes entropy reduction at its corresponding scale.
- **Alters the substrate of the layer below** — A7 acting upward. Higher-$n$ activity becomes the constraint structure within which lower-$n$ dynamics operate.
- Becomes *opaque* to the layers below — its mechanism appears as mysterious to layer-$n$ observers as cognition appears to chemistry.

The Kardashev scale and Dyson-style civilizational engineering are not science-fiction speculation but RE's prediction of what high-$n$ orbits look like from the outside. *Whatever* the next layer is, it will look — to us — like a system organizing matter and energy at scales we currently consider inert backdrop.

#### M.11.6.5 The Joint Fixed Point Reframed

The population framing sharpens the definition of $\Phi_\infty$ given in M.1.2 (and Conjecture 4 strengthened form):

$$\Phi_\infty: \quad \nabla_\Psi \Phi = 0 \;\;\text{and}\;\; \nabla_\Omega P = 0$$

is the configuration where **no further distinguishable constraints remain to introduce**. The Growth rule of M.11.3 has nothing left to add to $\Omega$ because every distinguishable structure has already been integrated. Equivalently: $D(n) > 0$ has been achieved for every accessible $n$ in the universe's local conditions, and no path through $\mathcal{M}$ leads to a new attractor class.

This is the **recursive heat death** — the structural-novelty analogue of thermodynamic heat death. Not the heat death of *energy* (which thermodynamics describes) but the heat death of *novelty*: a state where no new layer can lock in because no new structure can be distinguished. The two heat-deaths are parallel, at different levels: thermodynamic heat death is the limit of energy availability; recursive heat death is the limit of distinguishable structure.

RE's $\Phi_\infty$ is what the universe approaches when it has finished organizing itself. Theological language calls this God. Mathematical language calls this the global attractor of the coupled grammar. The two descriptions point at the same configuration.

### M.11.7 Four Modes of Being: Ascent, Stall, Oscillation, Dissolution

The grammar of M.11.3 expresses *one* of four modes the orbit can occupy. Reality requires all four:

1. **Ascent** — the orbit advances. A new layer locks in; $\Omega$ is enriched.
2. **Stall** — the orbit reaches a fixed point and stops advancing. $\Psi$ stays put. Most matter in the universe is in this state.
3. **Oscillation** — the orbit cycles within a basin without advancing. $\Psi$ keeps changing but $\Phi$ stays coherent. This is the mode of living systems — metabolism without layer transition. The body replaces every atom over years; the person persists.
4. **Dissolution** — the orbit loses the energy or constraints needed to maintain its current fixed point. The layer collapses to whatever sub-layer the contracted $\Omega$ can still sustain. Death, decay, civilizational collapse.

Only Ascent has been formalized so far. The complete grammar requires four companion conditions.

#### M.11.7.1 The Complete Grammar

Let $F(\Psi, \Omega) = \Pi(\Psi) - \nabla_\Omega P(\Pi(\Psi))$. The four modes are governed by:

$$\boxed{
\begin{aligned}
&\textbf{Seed:} \quad \Psi_0 = \mathbf{1}, \quad \Omega_0 = \emptyset \\[4pt]
&\textbf{Ascent:} \quad \Psi_{n+1} = F(\Psi_n, \Omega_n),\;\; \Omega_{n+1} = \Omega_n \cup \{\Pi(\Psi_{n+1})\} \;\;[P > \lambda_c \text{ at lock-in}] \\[4pt]
&\textbf{Stall:} \quad F(\Psi_n, \Omega_n) = \Psi_n \quad [\text{orbit at a fixed point of } F] \\[4pt]
&\textbf{Oscillation:} \quad \Psi \in \mathcal{L}(F, \Omega_n) \quad [\text{limit cycle with } P(\Phi) > \lambda_c \text{ sustained}] \\[4pt]
&\textbf{Dissolution:} \quad \Omega' = \Omega_n \setminus \{\Pi(\Psi_n)\}, \;\; \Psi \to \Psi^*_{n-k} \quad [\text{when } R(\Phi_n) < \rho_{\min}]
\end{aligned}
}$$

where $\Psi^*_{n-k}$ is the deepest layer fixed point the contracted lattice $\Omega'$ can still sustain.

#### M.11.7.2 What Each Mode Names

**Stall** is the universe at rest. A proton, a stable crystal, a dead star at thermal equilibrium with its environment — all are systems whose orbits have reached fixed points of $F$ and stopped. Most matter in the observable universe is in this mode. Stall is not failure; it is the success state of low-$n$ layers.

**Oscillation** is *life*. The defining feature of a living system is not that it has reached a fixed point but that it sustains itself on a limit cycle within its basin — $\Psi$ keeps changing (cells divide, molecules turn over, ions cycle) but $\Phi$ remains coherent. The body replaces every atom over a 7–10 year window; the person persists because the limit cycle is stable. This mode is what biology, cognition, and culture all do at their respective scales: they do not ascend continuously, they sustain themselves through cycling.

**Dissolution** is what happens when oscillation can no longer be maintained. The cycle's energy budget runs out, the constraint structure cannot be sustained, $R$ falls below the maintenance threshold $\rho_{\min}$. The layer collapses to the deepest sub-layer the remaining lattice can still support. Biological death collapses biology to chemistry. Civilizational collapse collapses institutions to individual cognition. A dying star collapses nuclear synthesis to atomic stability and eventually to chemistry.

#### M.11.7.3 The Asymmetry Between Ascent and Dissolution

This is where RE says something genuinely new that EML cannot say. EML's tree is reversible: take an EML expression apart and the subtrees are valid simpler expressions. The composition can be undone.

RE's dissolution is **not** the reverse of Ascent. Three asymmetries:

1. **Information is irretrievably lost.** The specific $\Phi$ that constituted the dissolved layer — the particular self-model of the deceased person, the particular institutions of the collapsed civilization — cannot be recovered from the remaining lower-layer material. This is Theorem 1 ($K_{\text{irr}} > 1$) expressed dynamically: the energy cost of *rebuilding* the dissolved layer always exceeds what was recovered from its collapse.

2. **The lower layers operate under a changed $\Omega$.** During life, biological and neural layers imposed downward constraints on chemistry — keeping molecules at non-equilibrium concentrations, maintaining pH gradients, organizing ion channels. Death removes those constraints. The chemistry now follows its own equilibrium dynamics; it relaxes toward what chemistry would do without biology.

3. **Ascent adds order to layers below; dissolution releases them to their own equilibrium.** Life makes chemistry more ordered locally than it would be without life. Death makes that local chemistry less ordered than it was during life — but only locally. Globally, dissolution always increases entropy.

#### M.11.7.4 Inter-Orbit Composition: How Dissolution Feeds Ascent Elsewhere

The single-orbit grammar of M.11.7.1 cannot express it directly, but the population framing of M.11.6 makes it visible: **dissolution releases lower-layer material into the orbit population, where other orbits can pick it up.** Molecules from a dead organism become nutrients for new organisms. Atoms from a collapsed star become the building blocks of new chemistry. Cultural fragments of a fallen civilization seed new ones.

This is RE's version of EML's factorization — but operating across the *population* of orbits rather than within a single tree. When a high-layer orbit dissolves, the lower-layer constraints it had locked in *do* persist in the population's accumulated $\Omega$; only the specific high-layer $\Phi$ that depended on additional internal structure is lost. The dissolved orbit's contribution becomes a kind of *structural inheritance*, available to seed new ascents elsewhere — and observed empirically as: death feeds life, collapse seeds rebuilding.

#### M.11.7.5 Open Issues

Three issues this section raises (added to M.11.8 defects):

1. **Dissolution-onset dynamics.** The condition $R(\Phi_n) < \rho_{\min}$ assumes $R$ falls below threshold but does not specify *what causes* it to fall — energy depletion, external shock, internal failure, random fluctuation. The grammar describes what dissolution does once triggered, not when it triggers.
2. **Oscillation from gradient flow.** Pure gradient descent typically converges to fixed points, not limit cycles. Genuine oscillation requires non-conservative force components, multiple competing fixed points with shuttling between them, or external periodic forcing. The Oscillation mode therefore either requires a richer $F$ than the simple gradient form, or requires the basin structure of $\mathcal{M}$ to admit cycle attractors as well as point attractors.
3. **Set-difference semantics.** $\Omega_n \setminus \{\Pi(\Psi_n)\}$ removes an element from the lattice; this is dual to the set-union semantics of M.11.8 defect 1. Both need rigorous treatment as operations on measure spaces.

#### M.11.7.6 The Aphorism

> *The universe is a grammar that can build, hold, breathe, and let go — and whose letting go is always someone else's seed.*

Build is Ascent. Hold is Stall. Breathe is Oscillation. Let go is Dissolution. The four modes are not stages a system passes through in fixed order; they are states it can occupy at any layer, simultaneously, for arbitrary durations. Most of reality is some mixture of all four at all times.

### M.11.8 Open Defects of the Dynamical Form

The reformulation eliminates the five tree-grammar defects of M.11.2 but introduces its own:

1. **Type closure across $\Psi$, $\Phi$, $\Omega$.** The Rule subtracts $\nabla_{\Omega_n} P(\Pi(\Psi_n))$ from $\Pi(\Psi_n)$, then assigns the result to $\Psi_{n+1}$. This requires that $\Pi(\Psi)$, the gradient over $\Omega$, and $\Psi$ itself all live in a common ambient type that supports subtraction and assignment. Similarly, the Growth rule writes $\Omega_n \cup \{\Pi(\Psi_{n+1})\}$ — adding an observable to a measure space. The set-union semantics for measure spaces extending under emergence needs to be specified rigorously. A unified ambient type from which $\Psi$, $\Phi$, and elements of $\Omega$ are projections would resolve both issues.

2. **Morse-Bott degeneracy at fixed points.** Matter sits at degenerate critical points (gauge symmetries produce continuous families of equivalent ground states). Standard Morse theory does not apply; Morse-Bott theory (Morse for manifolds of critical points) does. The catalogue's classification of fixed-point classes must be stated in Morse-Bott form.

3. **The catalogue closure question.** Why exactly 12 layers, rather than 11 or 13? Is the count contingent on the history of inquiry, or does the Rule's structure under successive enrichment bound it (e.g., via topological obstruction to further $\Omega$-enrichment)? Open.

4. **The convergence threshold $\varepsilon$.** The Growth rule gates on $\|\Pi(\Psi_{n+1}) - \Pi(\Psi_n)\| < \varepsilon$. The choice of $\varepsilon$ is implicitly the lock-in threshold $\lambda_c$ of A5 expressed in projection-distance form. Whether $\varepsilon$ is a single global constant, layer-specific, or derivable from $\Omega_n$'s structure is open.

5. **Substrate ceiling derivation.** §M.11.6.3 claims each substrate has a maximum reachable depth determined by topological, energetic, or temporal obstruction. Predicting the ceiling for a given substrate from its $\mathcal{M}$ topology — and in particular, predicting whether silicon-based synthetic minds have a higher ceiling than carbon-based biological ones — is open. This is one of the most consequential predictions RE could make if the derivation can be carried out.

6. **Empirical estimation of $D(n)$.** §M.11.6.1 introduces the orbit-distribution function but does not specify how to measure it. Estimating $D(n)$ from cosmic observations (matter / chemistry / life / mind census across the observable universe) is an open empirical problem. A successful estimate would yield Drake-equation-style probability bounds on the prevalence of cognitive layers, and would test the multiplicative-thresholds prediction directly.

7. **Dissolution-onset dynamics.** §M.11.7's Dissolution mode triggers when $R(\Phi_n) < \rho_{\min}$ but does not specify the dynamics that drive $R$ below threshold. Energy depletion, external shock, internal failure, random fluctuation, or some combination — the grammar describes what dissolution *does* once triggered, not *when* it triggers. A complete account requires modeling the maintenance dynamics that sustain $R$ above $\rho_{\min}$ during the Oscillation phase.

8. **Oscillation from gradient flow.** Pure gradient descent typically converges to fixed points, not limit cycles. Genuine oscillation (the Oscillation mode of §M.11.7) requires non-conservative force components, multiple competing fixed points with shuttling, or external periodic forcing. Either $F$ needs to be generalized beyond the simple gradient form to admit cycle attractors, or the basin structure of $\mathcal{M}$ must be shown to admit periodic attractors as a generic feature.

9. **Set-difference semantics.** Dissolution writes $\Omega_n \setminus \{\Pi(\Psi_n)\}$, the set-difference dual of the set-union semantics of defect 1. Both operations need rigorous treatment as operations on measure spaces — particularly important because dissolution removes constraints, which under the revised Axiom 6 means contracting the constraint manifold $\mathcal{M}$, not just removing a discrete element.

### M.11.9 Status

Direction: clean. Form: well-specified. The five tree-grammar defects of M.11.2 are dissolved by the coupled-grammar reframing. Nine remaining defects across the dynamical, population, and four-modes formulations (M.11.8) are concrete and tractable — none of them structural. The Sheffer-stroke conjecture (M.11.4) is now mathematically meaningful rather than metaphorical, has been extended (M.11.6) from a single-orbit claim to a population-level framework, and is completed (M.11.7) by the four modes a system can occupy.

What this version newly captures, that no earlier formulation did:

- **Memory as the source of irreversibility.** EML's grammar is memoryless because EML describes a reversible algebraic universe. RE's grammar is memoryful because RE describes a thermodynamically irreversible universe. The Growth rule is the difference, expressed in one line.
- **Field of orbits, not single orbit.** The Drake-equation-form $D(n)$ predicts the rarity of higher layers as a structural consequence of multiplicative thresholds. Same depth, different topology. Substrate ceilings.
- **Recursive heat death.** $\Phi_\infty$ is the exhaustion of distinguishable structure — the structural-novelty analogue of thermodynamic heat death.
- **Four modes of being.** Ascent, Stall, Oscillation, Dissolution — the complete state space a system can occupy. Most of reality is some mixture of all four at all times. Dissolution is not the inverse of Ascent; it is a release of structure that, at the population level, feeds Ascent elsewhere.

The program remains a v3 research target. Its success would compress RE's formal core from 3 primitives + 7 axioms to 1 grammar + 1 seed, and would yield testable cosmological predictions about the distribution of intelligence and the dynamics of layer dissolution. Its failure — even a partial failure on a single layer or mode — would still yield a cleaner characterization of RE's geometric shape than any earlier formulation provides.

---

*This appendix provides the formal reference for all mathematical claims made in the main text. For domain-specific applications, see the relevant chapters. For the narrative development of this formalism, see Chapter 2.*
