/-
  BoundaryResidue.lean
  Representation skeleton for Appendix M: Definition 17 (boundary object),
  Conjecture 7 (boundary residue), Open Problems 21, 22, 25.

  WHAT THIS IS
    A record of representation choices. Each choice is annotated with the open
    problem it decides. The payload is the annotations, not the theorems.

  WHAT IT HAS BECOME (2026-09-09). It began as the above and is no longer only
    that. It now proves thirteen things about the frame, holds two shapes
    awaiting faithful content, and carries no `sorry`: the three transcriptions
    it started with are gone, replaced by one proved theorem and two blocked
    problems. It asserts nothing it has not proved. That state was reached by
    REMOVING false statements as much as by proving true ones, and the contract
    below was broken once and recorded before it was repaired. It is currently
    kept.

  WHAT THIS IS NOT
    It was written to prove nothing, and the representation choices remain its
    main payload.
    Every `sorry` marks a CONJECTURE — a statement the manuscript asserts and
    has not derived — never an omitted routine step. This contract was BROKEN
    between 2026-09-09's §4 and its correction: two `sorry` sites marked
    statements that this file's own Theorem 10 refutes (§4.1). They now carry the
    hypotheses the transpositions had silently dropped. The lesson is logged in
    the manuscript's front matter as an instance of the register-boundary failure
    mode: a transposition is prose asserting truth-preservation, and nobody had
    checked it. If a `sorry` here is ever
    discharged, that is a mathematical event and belongs among the manuscript's
    numbered results, not in a refactor. (This originally read "belongs in M.8";
    M.8 is the conjectures section and M.4 holds the theorems. Corrected when §10
    produced an actual theorem and the slip would have misfiled it.)

  COMPILATION RECORD. Lean 4.15.0 (commit 11651562caae), bare toolchain, no
    Mathlib. Compiled clean 2026-09-09: exit 0, zero errors, zero linter
    complaints, warnings limited to the two intended `sorry` sites in §4.
    Reproduced independently twice — once on a trimmed copy, once on this file
    byte-exact — with identical audits. `formal/check.sh` passes. Axiom audit:

      Layer.undecidable, Layer.incompressible, Layer.available,
      Lattice.P, Lattice.clears, Broad          — no axioms
      diagonal_boundary_object                  — [sorryAx]
      opacity_boundary_object                   — [sorryAx]

    No `propext`, no `Quot.sound`, no `Classical.choice` anywhere in the six
    definitions — and the two conjectural STATEMENTS elaborate on `sorryAx`
    alone, so reification buys constructivity all the way up to the point where
    the manuscript's assertions begin. That is the machine-checked form of §2's
    argument.

  NEGATIVE RESULTS. Two objections were anticipated in this file and the
    compiler declined both; see §1 (`Lattice.P` loose parameters) and §3
    (`Layer.available` in `Prop`). Recorded because "Lean was offered this
    objection and did not take it" is information, and weaker than silence.

  Deliberately Mathlib-free. `Val` stays abstract rather than `ℝ` because the
    distinction being formalized — defined vs. undefined vs. zero — needs no
    ordered field, and importing one would hide which structure is load-bearing.
-/

namespace RE

/-! ## 0. The layer, and what "contains itself" costs

    Definition 16 writes self-representing depth as `⌜Π⌝, ⌜Ω_t⌝ ∈ Ψ_t` — a
    MEMBERSHIP claim. That cannot be taken literally here: `Rep` cannot contain
    its own evaluator as an element without a coding, and Lean will not admit
    the naive `Rep = Rep → Bool` form (negative occurrence; no such inductive).

    CHOICE (Problem 21): membership is replaced by an explicit `encode`/`decode`
    pair with a round-trip law. This is not a workaround — it is arithmetization,
    stated as the thing Definition 16 actually requires. Problem 21 asks for this
    pair to be exhibited for a natural system; the skeleton shows precisely what
    would have to be exhibited, which is less than "an encoding" and more than
    "a description": a decode that recovers the method, provably.
-/

structure Layer where
  /-- Structures the layer can formulate: `Rep(Ψ)`. -/
  Rep    : Type
  /-- The layer's own constructive, reusable procedures. Internalizing these as
      a TYPE is the skeleton's central commitment; see §2 for why absence of a
      `Decidable` instance cannot do this job. -/
  Method : Type
  /-- What a method returns on a structure. `Bool`, not `Prop`: methods decide. -/
  run    : Method → Rep → Bool
  /-- Arithmetization. `Option` is correct HERE — parsing a code is something the
      layer genuinely can decide — and wrong for `Defined` in §1, where it would
      hand the layer a decision it must not have. The asymmetry is the point. -/
  encode : Method → Rep
  decode : Rep → Option Method
  decode_encode : ∀ m, decode (encode m) = some m
  /-- Π's own resources. Opacity must be relative to these, never to an external
      clock; see §3. -/
  cost   : Method → Nat
  budget : Nat

/-- A method the layer can actually afford to run.

    NEGATIVE RESULT (verified). `Prop` rather than `Bool` is deliberate —
    affordability is a fact about the method, not something the layer computes —
    and this was expected to bite downstream in `Layer.undecidable`, where
    `L.available m → …` sits in hypothesis position. It bit nothing: `Prop` is
    exactly right there, and nothing in the file asks to compute it. Problem 22's
    classical pressure did NOT arrive at a second site, at least not within this
    file's demands. -/
def Layer.available (L : Layer) (m : L.Method) : Prop := L.cost m ≤ L.budget

/-! ## 1. `S`, and the three-valued distinction (Problem 22)

    Definition 17 turns on `S(Φ, Ω)` UNDEFINED being distinct from `S = 0`.

    REJECTED: `S : Rep → Lattice → Option Val`, and equally `WithBot Val`.
    Both make undefinedness a CONSTRUCTOR — pattern-matchable, so the layer
    decides it in one `match`. That collapses "statable inside, decidable only
    outside", which is the whole content of Definition 17.

    CHOICE (Problem 22): a definedness predicate in `Prop`, with `S` total on the
    subtype where it holds. Undefinedness is then not a value the layer can
    receive; it is the absence of an argument the layer can supply.
-/

structure Lattice (L : Layer) where
  Val     : Type
  zero    : Val
  lt      : Val → Val → Prop
  /-- The lattice's opinion about a structure. In `Prop`, not `Bool`. -/
  Defined : L.Rep → Prop
  /-- Structural compatibility, total exactly where the lattice has an opinion. -/
  S       : { x : L.Rep // Defined x } → Val

/-- CONSEQUENCE, and the skeleton's first real finding. Because `S` is only
    total on the subtype, every downstream quantity built from it inherits the
    restriction. Emergence potential cannot be written for arbitrary `Φ`. -/
def Lattice.P {L : Layer} (Ω : Lattice L)
    (mul : Ω.Val → Ω.Val → Ω.Val) (R ΔH : L.Rep → Ω.Val) :
    { x : L.Rep // Ω.Defined x } → Ω.Val :=
  fun x => mul (mul (R x.val) (ΔH x.val)) (Ω.S x)

/-- Therefore A5's threshold test is not merely false at a boundary object — it
    is UNSTATABLE there, because `P` has no argument to take. This is stronger
    than "S is undefined", and it is forced by the §1 choice rather than added
    to it: whatever else a boundary object is, it is a structure for which the
    layer cannot form the comparison that would admit or forbid it.

    NEGATIVE RESULT (verified). `mul : Ω.Val → Ω.Val → Ω.Val` refers to a
    projection of a parameter bound earlier in the same signature; this was
    expected to fail elaboration and force `mul`/`R`/`ΔH` into `Lattice` as
    fields — which would have been a claim about Definition 1, making emergence
    potential part of the lattice's DATA rather than derived from it. It
    elaborates cleanly, implicit `{L}` and all. So the claim is not compelled:
    `P` stays derivable from the lattice, by the compiler's leave rather than by
    our preference. -/
def Lattice.clears {L : Layer} (Ω : Lattice L)
    (mul : Ω.Val → Ω.Val → Ω.Val) (R ΔH : L.Rep → Ω.Val) (θ : Ω.Val)
    (x : { y : L.Rep // Ω.Defined y }) : Prop :=
  Ω.lt θ (Ω.P mul R ΔH x)

/-! ## 2. Why "no `Decidable` instance" cannot carry the claim

    The tempting move is to omit `instance : Decidable (Ω.Defined x)` and let
    that absence mean "the layer cannot decide". It does not mean that.

    (VERIFIED on 4.15.0, and a fact about Lean's foundations rather than its
    elaborator) `Classical.propDecidable a : Decidable a` exists for every
    `a : Prop`. Note the name: `Classical.dec` is a Mathlib alias and does not
    exist in core. It is `scoped`, so bare instance resolution for an arbitrary
    `Decidable p` FAILS, `open Classical` promotes it (and forces
    `noncomputable`), and explicit invocation works with no `open` at all.
    Absence of an instance is therefore a fact about instance resolution in one
    file — a namespace accident, revocable by an import. It is not a
    mathematical statement, and a reader who adds `open Classical` to make
    something compute has silently deleted Definition 17.

    THIS IS PROBLEM 22 TALKING, and the skeleton records it instead of yielding:
    the layer's inability must be a QUANTIFIED CLAIM over the layer's own
    internalized methods, not a gap in the ambient logic.

    THE GUARD IS NOT THE MISSING INSTANCE — IT IS THE AXIOM AUDIT. Anything
    touching `propDecidable` drags `[propext, Classical.choice, Quot.sound]`
    into its axiom report, so the silent-deletion failure mode above is one
    `#print axioms` from detection: the six frame definitions must report
    axiom-free, and any classical leak changes a visible audit line. That turns
    the vulnerability into a checkable invariant rather than a warning to
    readers. See `formal/check.sh`.
-/

/-- No method the layer can afford agrees with `p` everywhere. This is the
    gadget. Note what it is indexed by: the layer's own evaluator and budget. -/
def Layer.undecidable (L : Layer) (p : L.Rep → Prop) : Prop :=
  ∀ m : L.Method, L.available m → ¬ (∀ x : L.Rep, L.run m x = true ↔ p x)

/-! ## 3. Incompressibility, relative to Π (Problem 25, prerequisite)

    CHOICE: parameterized by the layer, with the resource bound read off
    `L.cost`/`L.budget` — never passed in from outside.

    A globally-parameterized `incompressible (t : Nat) (x : α)` would be
    time-bounded Kolmogorov complexity, K^t. Respectable, well-studied, and NOT
    the opacity mechanism: K^t is absolute, opacity is relative to the layer's
    own Π. Kabanets–Cai (2000) live at the global version — which is why their
    result connects natural properties to MCSP generically. Conjecture 7 needs
    the relative one. Collapsing the two is the most likely way to formalize
    something true and irrelevant.
-/

def Layer.incompressible (L : Layer) (x : L.Rep) : Prop :=
  ∀ m : L.Method, L.available m → L.run m x = false

/-- Largeness: opacity's second ingredient, and the one the diagonal mechanism
    does not need. Left abstract — a predicate on predicates — because supplying
    a measure is the substance of Problem 25, not a detail of its statement.

    NEGATIVE RESULT (verified twice), and sharper than the warning it replaces.
    This was expected to draw an unused-variable complaint on `L`, with the
    compiler thereby noticing that largeness supplies nothing layer-relative. It
    draws NO warning: the linter counts `L` as used, because it occurs in the
    TYPES of `large` and `p` (`L.Rep → Prop`). A control with a genuinely unused
    `L` in the same file DOES warn (`unused variable \`L\``), so this is the
    linter's reading, not its silence.

    The gap is therefore invisible to tooling by construction. The type system
    certifies that the STATEMENT of largeness is layer-relative while the BODY
    supplies no layer-relative content, and no linter reads that difference —
    it only reads binder occurrences. The finding is the ABSENCE of the warning:
    `Broad` passes as layer-indexed on the strength of its type alone, which is
    the unanalyzed-largeness problem stated in the compiler's own terms. -/
def Broad (L : Layer) (large : (L.Rep → Prop) → Prop) (p : L.Rep → Prop) : Prop :=
  large p

/-! ## 4. The two mechanisms, as instances of one frame -/

/-- Blum-flavoured cost axioms, as a STUB. Theorem 10 showed this frame prices
    nothing: `cost` is a number unrelated to what `run` computes, so affordable
    methods decide everything and no inaccessibility claim is provable. The debt
    Theorem 10 calls in is a genuine machine-independent cost theory (Blum 1967);
    naming it is not paying it. What is assumed here is only that the cost
    measure is non-degenerate — enough to exclude the transparent layers that
    refute the unhypothesised conjectures (§4.1), and deliberately NOT enough to
    imply their conclusions. -/
structure CostAxioms (L : Layer) : Prop where
  /-- Costs are unbounded: no finite budget buys the whole method set. -/
  unbounded : ∀ n : Nat, ∃ m : L.Method, n < L.cost m

/-- The stub has content: unbounded costs make the affordable fragment proper. -/
theorem CostAxioms.proper {L : Layer} (h : CostAxioms L) :
    ∃ m : L.Method, ¬ L.available m := by
  obtain ⟨m, hm⟩ := h.unbounded L.budget
  exact ⟨m, fun hle => absurd hm (Nat.not_lt.mpr hle)⟩

/-! ### The diagonal arm, settled

    The sorry'd restatement that stood here is GONE, and not because it was
    proved: Corollary 10.3 refutes it. `CostAxioms` was aimed at the hypothesis
    when the fault was in the PREDICATE — identity-with-a-point is cheap in every
    complexity theory, so no cost axiom could ever have rescued it. The correct
    transposition is `diagonal_self_application` (§15; Theorem 11 in M.4): proved,
    axiom-free, for EVERY method rather than only affordable ones, and using
    `decode_encode` essentially. The diagonal mechanism turns out to be cost-free
    in the literal sense — affordability never entered. -/

/-! ### The opacity arm, DEMOTED — not restated

    The sorry'd opacity conjecture is gone too, and is NOT replaced by a version
    with the missing usefulness conjunct bolted on. That would repeat the
    diagonal's error one conjunct over: fixing a statement whose `large` has no
    content and whose `hard` is point-incompressibility, which
    `blum2_kills_incompressible` shows is not Razborov–Rudich hardness at all. A
    `sorry` there would mark a SHAPE, not a belief, breaking the header contract
    the previous batch repaired.

    What IS committed is the shape, as a `def` asserting nothing — the device §12
    established for fixing a statement without believing it.

    BOUNDARY, and it must travel with the demotion: Razborov–Rudich is untouched.
    It is a theorem in the literature and Conjecture 7 (b) rests on it exactly as
    before. What failed, twice, was this frame's transcription — the logical shape
    (§15.1 clause 5) and the hardness notion (clause 4). A reader who takes this
    as the framework retracting the opacity mechanism has read a demotion of a
    transcription as a demotion of the mathematics. -/

/-- An affordable method decides `p`. The only RR ingredient with a referent. -/
def constructiveFor (L : Layer) (p : L.Rep → Prop) : Prop :=
  ∃ m : L.Method, L.available m ∧ ∀ x, L.run m x = true ↔ p x

/-- The CORRECT Razborov–Rudich logical shape, committed and asserted of nothing:
    `constructive ∧ large ⟹ ¬useful`. The frame's earlier transposition had
    `large ⟹ ¬constructive`, which is not RR's conclusion and is false for the
    trivial broad predicate.

    `Large`, `Hard` and `Useful` are PARAMETERS. All three are measure-relative:
    largeness is a measure on `Rep` (Problem 25's prerequisite), RR hardness is
    indistinguishability of distributions rather than invisibility of a point,
    and usefulness is defined relative to hardness. So the three placeholders
    wait on ONE object. Opacity is not yet hostable in this frame; it becomes
    hostable when that measure exists, and not before. -/
def RR_shape (L : Layer)
    (Large : (L.Rep → Prop) → Prop) (Hard : Prop) (Useful : (L.Rep → Prop) → Prop) : Prop :=
  Hard → ∀ p : L.Rep → Prop, constructiveFor L p → Large p → ¬ Useful p

/-! ### 4.1 The unhypothesised transpositions are FALSE

    Both statements above, WITHOUT `CostAxioms`, are refuted — by Theorem 10's
    mechanism aimed one section earlier than §13 aimed it. These are corollaries
    of Theorem 10 in force, and arguably its best statement: "affordability
    constrains nothing", made concrete twice. -/

/-- Transparent layer: one method per element, each deciding identity with it. -/
def Lid : Layer where
  Rep := Bool
  Method := Bool
  run := fun m x => decide (x = m)
  encode := fun m => m
  decode := fun x => some x
  decode_encode := by intro m; rfl
  cost := fun _ => 0
  budget := 0

def Omid : Lattice Lid where
  Val := Unit
  zero := ()
  lt := fun _ _ => False
  Defined := fun _ => False
  S := fun _ => ()

/-- COROLLARY 10.1. Every identity predicate in `Lid` has an affordable decider,
    so no `x` satisfies `undecidable (· = x)`; and the conjecture quantifies over
    ALL layers, so one transparent layer kills it. -/
theorem diagonal_refuted_as_stated :
    ¬ (∀ (L : Layer) (Ω : Lattice L),
        ∃ x : L.Rep, ¬ Ω.Defined x ∧ L.undecidable (fun y => y = x)) := by
  intro h
  obtain ⟨x, _, hu⟩ := h Lid Omid
  exact hu x (Nat.le_refl 0) (fun y => decide_eq_true_iff)

/-- A layer with a genuinely incompressible element AND an affordable decider. -/
def Lop : Layer where
  Rep := Option Bool
  Method := Unit
  run := fun _ x => decide (x = some true)
  encode := fun _ => some true
  decode := fun x => match x with | some true => some () | _ => none
  decode_encode := by intro m; cases m; rfl
  cost := fun _ => 0
  budget := 0

def Omop : Lattice Lop where
  Val := Unit
  zero := ()
  lt := fun _ _ => False
  Defined := fun _ => False
  S := fun _ => ()

/-- `none` is incompressible: every affordable method returns false on it. So
    `hard` is SATISFIED here, not dodged. -/
theorem none_incompressible : Lop.incompressible none := by
  intro m _; cases m; rfl

/-- COROLLARY 10.2, and the sharper of the two. Opacity's hypothesis and the
    negation of its conclusion coexist in a three-element layer: an
    incompressible point, and an affordable method deciding a Broad predicate
    exactly — including at that point. -/
theorem opacity_refuted_as_stated :
    ¬ (∀ (L : Layer) (Ω : Lattice L) (large : (L.Rep → Prop) → Prop),
        (∃ x : L.Rep, L.incompressible x) →
        ∀ p : L.Rep → Prop, Broad L large p →
          (∀ m : L.Method, L.available m → ¬ (∀ x, L.run m x = true ↔ p x))) := by
  intro h
  exact h Lop Omop (fun _ => True) ⟨none, none_incompressible⟩
    (fun x => x = some true) trivial () (Nat.le_refl 0) (fun x => decide_eq_true_iff)

/-! ## 5. The convergence question the build was meant to answer

    Constraint 3 asked whether the two constructions want to share machinery.
    The answer the skeleton gives is PARTIAL, and the partition is informative.

    SHARED: both are instances of `Layer.undecidable` — a `Prop` the layer can
    state but not decide, indexed by the layer's own evaluator and budget. That
    is exactly the gadget anticipated, and it is one gadget, not two.

    NOT SHARED: their premises differ, and differ in kind.
      · diagonal needs `encode` — self-quotation, and nothing more.
      · opacity needs `large` (a measure on `Rep`) plus `hard` (a hypothesis).

    So Problems 22 and 25's prerequisite are not one problem wearing two labels.
    They are one FRAME carrying two different additional structures. The frame
    is shared; the residue-producing ingredient is not.

    AND NOTE WHAT OPACITY'S EXTRA INGREDIENT IS: a measure on `Rep`. The M.10
    Problem 25 remark guessed that opacity runs on the ergodic signature of
    Theorem 7 reappearing inside Theorem 8's constructive column. The skeleton
    does not prove that, but it does say where such a thing would have to enter,
    and it enters exactly there — `large`, a measure, absent from the diagonal
    branch and required by the opacity branch. The remark is not nothing. It is
    also not yet a claim.

    DISCRIMINATOR — PRE-REGISTRATION. Written 2026-09-09 BEFORE the construction
    exists, and committed before it, so the result is evidence rather than
    narration. §6 will report against this and must not edit it.

    RIGGING RISK. This frame currently offers exactly one carrier: `Rep`. A
    measure formalized into the frame as it stands lands on `Rep` BY DEFAULT,
    for want of anywhere else to land, and would confirm re-entry vacuously. The
    experiment is therefore only an experiment if the construction is offered two
    candidate carriers — an abstract `State` alongside `Rep`, with a map between
    them — and the theorem's own content decides which one the measure attaches
    to. If the transcription cannot be written without identifying `State` with
    `Rep`, that is a finding. If the formalizer identifies them for convenience,
    that is contamination, and it must be visible in the diff.

    THREE OUTCOMES, not two. `large : (Rep → Prop) → Prop` has both a carrier
    (`Rep`) and a shape (second-order predicate). Ergodic search needs some
    measure-or-reachability structure, and it may match on either, both, or
    neither:

      (A) CARRIER AND SHAPE BOTH MATCH — the ergodic ingredient is the `large`
          slot refilled. Re-entry gains full standing; the §5 remark is promoted
          to conjecture typography AT MOST, since it still would not be derived.
      (B) CARRIER MISMATCH — measure on `State`, not on `Rep`. The two mechanisms
          are siblings sharing only the frame; the remark resolves toward
          nothing, and is to be recorded as resolving toward nothing.
      (C) CARRIER MATCHES, SHAPE DOES NOT — e.g. a transition kernel on `Rep`
          rather than a largeness predicate. Same territory, different
          instrument: neither re-entry nor nothing, and the remark's next
          revision must say that rather than round to a pole.

    SECOND QUESTION, independent of A/B/C. Does the ergodic construction need
    `encode` at all? Diagonal needed `encode` alone; opacity needed `encode` plus
    two. If ergodic search needs NO self-encoding, the carrier boundary is a
    different kind of boundary from the one Conjecture 7 describes, and the
    nesting of the two tables becomes a fact about the frame rather than a
    reading of it.

    RECORDED PRIOR (mine, after reading Theorem 7 as committed, before writing
    any Lean). Theorem 7 quantifies over a substrate state-space `𝒳` with a
    stationary measure `ρ_∞(basin)`, and never quotes anything. I expect (B),
    and I expect the answer to the second question to be no. I also expect a
    third thing the pre-registration cannot score: that `P` in Theorem 7 and `P`
    in Definition 1 are not the same function on the same domain, in which case
    the transcription will not close without a choice, and that choice gets the
    skeleton's annotation discipline.
-/

/-! ## 6. The discriminator, run

    Transcribed from Appendix M, Theorem 7 (Recipe Inevitability) as committed.
    Its statement quantifies over a substrate state-space `𝒳` with a Langevin
    update, and concludes about `Pr[Ψ_t ∈ basin(Ψ*)]` via a stationary measure
    `ρ_∞(basin) = Z⁻¹ ∫_basin e^{P/D} dΨ > 0`.

    ANTI-RIGGING (per the pre-registration). `Substrate` below is deliberately
    NOT parameterized by `Layer`. If Theorem 7 needs the layer's representation
    machinery, the transcription will not close and a `Layer` parameter will have
    to be added — visibly, in the diff. The bridge is a separate structure, so
    identifying `State` with `Rep` would also be a visible edit rather than a
    default.
-/

/-- The substrate of Theorem 7. `Val` abstract for the same reason as §1.

    CHOICE (annotated): `one` and `sub` are carried as fields because the
    theorem's conclusion is literally `> 1 - ε`, which needs an ordered field the
    manuscript assumes and this file declines to import. Abstracting them keeps
    Mathlib out; the cost is that no arithmetic law about them is available, so
    nothing here can be proved from them. That is acceptable because §6 proves
    nothing — but it is a choice, not a neutrality. -/
structure Substrate where
  State : Type
  Val   : Type
  zero  : Val
  one   : Val
  lt    : Val → Val → Prop
  sub   : Val → Val → Val
  /-- Theorem 7's `P(Ψ; θ)`: emergence potential ON A SUBSTRATE STATE. -/
  P     : State → Val
  /-- `basin(Ψ*)`, the carrier-class local maximum's basin. -/
  basin : State → Prop
  /-- The stationary measure `ρ_∞`. Note the type: a valuation on SETS OF
      STATES. This is the object the discriminator was built to inspect. -/
  rho   : (State → Prop) → Val
  rho_basin_pos : lt zero (rho basin)

/-- Birkhoff, transcribed: time-average occupation approaches `ρ_∞`. -/
def Ergodic (X : Substrate) (occupation : Nat → (X.State → Prop) → X.Val) : Prop :=
  ∀ A : X.State → Prop, ∀ ε : X.Val, X.lt X.zero ε →
    ∃ T : Nat, ∀ t : Nat, T < t → X.lt (X.sub (X.rho A) ε) (occupation t A)

/-! ### Theorem 7's transcription, DEMOTED — see §16

    The `sorry`'d transcription that stood here is gone. It was false as written
    (§16, `recipe_inevitability_refuted`), and four further conjuncts had been
    dropped in transport besides the one that refutes it. Following the opacity
    precedent, it is demoted rather than patched: the shape is committed as a
    definition asserting nothing, with every dropped ingredient present as an
    explicit parameter, so that what a faithful transcription owes is visible
    rather than remembered. -/

/-- Theorem 7's SHAPE, asserted of nothing. Each parameter is an ingredient the
    earlier transcription dropped: `θ` and its threshold, the initial condition,
    the link between `basin` and a non-degenerate maximum of `P` with positive
    depth, and normalization of the measure. `Ergodic` is passed as a parameter
    too, because the earlier version assumed Birkhoff's conclusion in place of
    the ergodicity hypothesis it is derived from. -/
def Theorem7_shape (X : Substrate)
    (Theta : Type) (aboveThreshold : Theta → Prop)
    (occupation : Theta → X.State → Nat → (X.State → Prop) → X.Val)
    (ergodicSDE : Theta → Prop)
    (basinOfMax : Theta → Prop)
    (normalized : Prop) : Prop :=
  normalized →
    ∀ θ : Theta, aboveThreshold θ → basinOfMax θ → ergodicSDE θ →
      ∀ start : X.State, ∀ ε : X.Val, X.lt X.zero ε →
        ∃ T : Nat, ∀ t : Nat, T < t →
          X.lt (X.sub X.one ε) (occupation θ start t X.basin)

/-- The bridge, kept separate so that using it is visible. Theorem 7 above does
    not mention it, which is itself the answer to the pre-registration's second
    question. -/
structure Bridge (L : Layer) (X : Substrate) where
  formulable : X.State → L.Rep → Prop

/-! ### 6.1 Readout

    The two objects the pre-registration said to compare, written side by side:

      largeness slot (§3):   `(L.Rep → Prop) → Prop`
      ergodic measure (§6):  `(X.State → Prop) → X.Val`

    OUTCOME (B), and by a wider margin than (B) required. The pre-registration
    scored carrier and shape separately. Both differ.

      · CARRIER: `State` vs `Rep`. Theorem 7's measure attaches to substrate
        states. Nothing in its statement ranges over formulable structures.
      · SHAPE: a VALUATION into `Val`, not a PREDICATE into `Prop`. `large` asks
        whether a property is broad; `rho` asks how much measure a set carries.
        Even had the carriers matched, these are different instruments — so the
        (C) branch is also excluded, rather than left ambiguous.

    The §5 remark therefore resolves toward nothing, and is recorded as doing so.
    The ergodic signature is not the largeness slot refilled.

    SECOND QUESTION: no, and more sharply than asked. `Substrate`, `Ergodic`, and
    `recipe_inevitability` compile with NO reference to `Layer` — not merely no
    `encode`, but no `Rep`, no `Method`, no `run`, no `decode`. Theorem 7 does not
    need the self-representation apparatus in any part. `Bridge` exists solely to
    show what connecting them would cost, and nothing above uses it.

    CONSEQUENCE for the two tables. The nesting correction of §5 now has a
    frame-level fact under it: Theorem 7 is statable in a strictly smaller
    signature than Theorem 8. The carrier boundary is not a sharper version of
    the boundary Conjecture 7 describes — it is a boundary between signatures,
    below which self-representation is not merely unused but unmentionable.

    UNSCORED FINDING (the prior's third clause, which the pre-registration could
    not score). `Substrate.P : State → Val` and `Lattice.P :
    {x // Defined x} → Val` are DIFFERENT FUNCTIONS ON DIFFERENT DOMAINS, and the
    manuscript writes both as `P`. Theorem 7's is a potential on substrate states;
    Definition 1's is emergence potential of a candidate coherence. The
    transcription cannot close the gap without a choice, and this file declines to
    make one: no equation relates them, and `Bridge` carries no coherence law. To
    state one would require saying how a candidate coherence's potential is
    induced by the substrate states that formulate it — which is not in the
    manuscript, and is Problem-21-shaped: a bridging law asserted informally by
    shared notation and not exhibited. Logged for M.10. -/


/-! ## 7. Problem 26's type-level half — PRE-REGISTRATION

    Written 2026-09-09 BEFORE §8 exists, committed before it, not edited by it.

    Problem 26 gives a candidate bridging law two success criteria. One is
    mathematics and belongs to the future: does the induced potential reproduce
    `R · ΔH · S` on the defined region. The other is a TYPE-LEVEL claim and is
    testable now:

      TOTALITY ABOVE, PARTIALITY BELOW — the induced potential is total in the
      joined signature (`Substrate` + `Layer` + `Bridge`), and its restriction to
      the layer's own vocabulary remains partial, with the boundary landing
      exactly on `Defined`.

    THE PROBE. Define the joined signature. Write the candidate induced potential
    as fiber aggregation against `ρ_∞`, with the aggregation operator left
    ABSTRACT — a stub, exactly as `large` is left abstract in §3, so that no
    property of any particular aggregator can be smuggled in. Then attempt to
    form the restriction to the layer's vocabulary AT AN UNDEFINED POINT.

    TWO OUTCOMES, pre-registered:

      (I) RESTRICTION ILL-FORMED FOR EVERY ABSTRACT AGGREGATOR. The constraint is
          satisfiable by the candidate family's SHAPE, independent of which
          aggregator is chosen. Problem 26's remaining work is then purely the
          mathematics of product-reproduction, and the type-level criterion is
          discharged in advance for the whole family.
     (II) RESTRICTION FORMS ANYWAY. Totality leaks through the types regardless
          of aggregator. The entire fiber-aggregation family then fails the
          pre-registered constraint BEFORE a single integral is computed, and
          Problem 26's obvious first candidate dies for the price of a compile.
          Under the M.10 retention convention it would resolve, not vanish.

    WHAT WOULD BE CHEATING, named in advance. An aggregator stub so weak that
    NOTHING is formable anywhere would satisfy (I) vacuously — this is the
    trivial-satisfaction failure Problem 26 already rejects. So the probe must
    also witness the POSITIVE case: the induced potential must be formable at a
    DEFINED point in the joined signature. A run that shows ill-formedness at
    `Φ_G` without showing formability at a defined Φ has demonstrated nothing.

    RECORDED PRIOR (mine, before writing §8). I expect (I), and I expect it for a
    reason I may be wrong about: `Lattice.S` consumes `{x // Defined x}`, so any
    expression that routes through `S` cannot be formed off the subtype, while an
    expression that routes only through `Substrate.P` and the fiber never touches
    `Defined` at all. If that is right, the interesting question is not whether
    the restriction is ill-formed but WHERE the partiality actually comes from —
    and the honest answer may be that it comes from `S` alone, in which case the
    constraint is satisfied by Definition 3's typing rather than by anything the
    bridging law does. That would make outcome (I) true but much less
    informative than it sounds, and §8 must say so if it lands that way.
-/

/-! ## 8. The probe, run -/

/-- The joined signature: substrate, layer, and the bridge between them. -/
structure Joined where
  L : Layer
  X : Substrate
  formulable : X.State → L.Rep → Prop
  Om : Lattice L

/-- The fiber of a formulable structure: the substrate states that formulate it.
    This is `Π⁻¹(Φ)` of A2, as a predicate on states. -/
def Joined.fiber (J : Joined) (x : J.L.Rep) : J.X.State → Prop :=
  fun s => J.formulable s x

/-- The aggregation operator, left ABSTRACT exactly as `large` is. It consumes
    the fiber, the substrate potential, and the measure, and returns a value. No
    property of it is assumed. -/
abbrev Aggregator (J : Joined) : Type :=
  (J.X.State → Prop) → (J.X.State → J.X.Val) → ((J.X.State → Prop) → J.X.Val) → J.X.Val

/-- THE CANDIDATE. Induced potential as fiber aggregation against `ρ_∞`.
    Note the domain: `J.L.Rep`, TOTAL — no `Defined` anywhere. -/
def Joined.induced (J : Joined) (agg : Aggregator J) (x : J.L.Rep) : J.X.Val :=
  agg (J.fiber x) J.X.P J.X.rho

/-- POSITIVE WITNESS (anti-cheating, required by the pre-registration). The
    induced potential IS formable at a point carrying a `Defined` proof, so the
    aggregator stub is not vacuous. -/
def Joined.induced_at_defined (J : Joined) (agg : Aggregator J)
    (x : { y : J.L.Rep // J.Om.Defined y }) : J.X.Val :=
  J.induced agg x.val

/-- AND AT AN UNDEFINED POINT. `x` carries a proof that the lattice has NO
    opinion, and the induced potential is formed at it anyway, for an arbitrary
    aggregator. -/
def Joined.induced_at_boundary (J : Joined) (agg : Aggregator J)
    (x : J.L.Rep) (_h : ¬ J.Om.Defined x) : J.X.Val :=
  J.induced agg x

/-! ### 8.1 Readout — NEITHER pre-registered outcome, and that is the finding

    Everything above compiles. `induced_at_defined` and `induced_at_boundary`
    both form, for an ARBITRARY aggregator, so the anti-cheating witness is
    satisfied: the stub is not vacuous, and formability at `Φ_G` is not an
    artifact of an aggregator too weak to compute anything.

    THE TEMPTING MISREADING IS (II). `induced_at_boundary` forms at a point
    carrying `¬ Om.Defined x`, so it looks as though totality leaked and the
    fiber-aggregation family is dead. It is NOT dead, and reporting (II) here
    would be wrong. Re-read the constraint: it *requires* totality in the joined
    signature. `Joined.induced` takes `J : Joined` — it is an expression IN the
    joined signature. Its formability at `Φ_G` is the constraint's first clause
    being satisfied, not its second clause being violated.

    WHY (I) IS NOT ESTABLISHED EITHER. The second clause asks whether the
    restriction to "the layer's own vocabulary" stays partial. Attempting that
    restriction has two readings, and both are uninformative:

      · Read as "an expression mentioning only `Layer` and `Lattice`": it cannot
        form, but only because there is no way to produce a `Val` from nothing.
        That is true of every function of the substrate whatsoever and says
        nothing about `Defined`.
      · Read as "formable somewhere in the joined signature": it forms, which is
        the first clause and permitted.

    THE ACTUAL FINDING, and it is the fourth instance of the named failure mode.
    "Restriction to the layer's vocabulary" has no formal referent yet. The
    pre-registered criterion was stated in prose, transcribed here, and turned
    out not to be sharp enough to discriminate — the probe cannot fail it or pass
    it, which is different from passing. Problem 26's type-level half is
    therefore NOT discharged, and NOT refuted; it is underspecified, in exactly
    the way Definition 16's membership, Problem 21's "encoding", and A2's fiber
    were underspecified.

    AND THE FRAME ALREADY CONTAINS THE FIX. "Layer-available" was given a formal
    referent in §2, under exactly this pressure: `L.Method` with `L.run` and
    `L.available`. So the sharpened second clause is not "no expression in the
    layer's vocabulary evaluates P at `Φ_G`" but:

      no method the layer can afford yields the induced potential's verdict at
      `Φ_G` — i.e. the bridging law must not let the layer CONSTRUCT an
      `m : L.Method` whose `run` tracks `Defined`.

    That is testable, and it is not testable in this signature as written:
    `L.run` returns `Bool` and knows nothing of `Val`, so no method can consume
    an induced potential at all. Closing that gap means deciding how methods read
    values — which is another representation choice, and the honest place to stop
    this run rather than make it silently.

    PRIOR, SCORED. I predicted (I). The prediction was wrong; neither outcome
    landed. Worse — or better — the prior's own reasoning contained the
    refutation: it observed that "an expression that routes only through
    `Substrate.P` and the fiber never touches `Defined` at all", which is exactly
    why `induced_at_boundary` forms. I stated the mechanism of the result and
    then predicted against it. The deflation the prior worried about was also
    real but landed elsewhere than expected: partiality does come from `S` alone,
    and the induced potential never routes through `S`, so `Defined` was never in
    a position to make anything ill-formed.

    The instructive part is not that the prediction was wrong but HOW: mechanism-
    identification and prediction ran as separate processes and neither checked
    the other. Pre-registration is what makes that visible afterward instead of
    laundering it into "as expected". The file's record now holds one confirmed
    prior (§6, discriminator), one wrong prior (here), and — the same one — a
    prior refuted by its own stated mechanism. §15 clause 4 adds a fourth category:
    PREDICTION WRONG, CONCLUSION RIGHT, MECHANISM REPLACED — `Blum2` was predicted
    idle and turned out lethal, to the wrong hardness notion, so the downstream
    conclusion survived by a route nobody predicted. That is the category where a
    correct conclusion would have been mis-credited to a false mechanism had the
    mechanism not been pre-registered separately from the prediction. That
    distribution is healthier
    than three confirmations would have been, and it is the reason none of these
    sections is allowed to edit its own pre-registration. -/

/-! ## 9. Problem 27 — PRE-REGISTRATION

    Written 2026-09-09 BEFORE §10 exists and committed before it. Outcome space
    and destinations drafted by the reviewer, who is not running the experiment;
    the pre-commitment below is mine, and is the only part they left open.

    THE QUESTION. Does type-level partiality imply method-quantified
    inaccessibility? That is, given a lattice with an undefined point, does it
    follow that no affordable method decides the relevant question there?

    PRE-COMMITMENT: THE RELEVANT QUESTION IS DEFINEDNESS ITSELF. Three candidates
    were on the table — identity with `x`, definedness, threshold clearance — and
    they may behave differently, so one must be fixed before compiling.

      · Threshold clearance is excluded by dependency: it is Problem 26's object
        and needs the run/Val choice that is logged and unmade.
      · Identity with `x` is what §4 happens to use, but it is a statement about
        one element, not about the invariant.
      · Definedness is the invariant. Definition 17's content is that the lattice
        has no opinion about `Φ_G` and the layer cannot get one; its method-
        relative form is therefore `L.undecidable Ω.Defined`, which typechecks
        directly since `Ω.Defined : L.Rep → Prop` is exactly what
        `Layer.undecidable` consumes.

    So the statement under test is:

      ∀ (L : Layer) (Ω : Lattice L), (∃ x, ¬ Ω.Defined x) → L.undecidable Ω.Defined

    THREE OUTCOMES, WITH DESTINATIONS DECLARED IN ADVANCE (this is the point of
    writing it down: a positive result must not be absorbable as cleanup).

      (A) PROVABLE in the bare frame. Destination: M.8, as a NUMBERED THEOREM.
          Per this file's header a discharged `sorry` is a mathematical event and
          never a refactor. Consequence: the two implementations of Definition 17
          reconcile, `S`-partiality is a sound if local presentation of the
          invariant, and Problem 27's regrounding becomes a change of emphasis
          rather than of content. Definition 17's history stays continuous.
      (B) REFUTABLE by construction — a `Layer` and `Lattice` with an undefined
          point AND an affordable method deciding definedness there. Destination:
          M.8 also, as a constructed counterexample with the standing of a
          theorem, PLUS a mandatory revision of Definition 17's text, since the
          definition would then have rested since it was written on the strictly
          weaker of two non-equivalent formulations. This is not a failure of the
          framework; it is the strongest possible justification for Problem 27,
          and by the retention convention the counterexample stays in this file
          permanently as the reason the definition says what it then says.
      (C) NOT STATEABLE without further choices. Destination: the choice is
          logged with the usual annotation discipline, and Problem 27 acquires an
          explicit dependency the way Problem 26 acquired one on Problem 27.

    ANTI-TRIVIALITY GUARDS, BOTH ENDS, and the (A)-guard is to be built FIRST so
    it cannot be retrofitted to whatever lands:
      · (B) must not hold vacuously through `available` being unsatisfiable. The
        counterexample must EXHIBIT an affordable method — `cost ≤ budget`
        witnessed, not assumed.
      · (A) must not hold vacuously through the frame making everything
        method-inaccessible. The companion witness is an affordable method that
        DOES decide the relevant question somewhere on the defined region.

    RECORDED PRIORS. The reviewer expects (B), cheaply: nothing in the bare frame
    constrains `run` relative to `Defined`, so a layer whose method computes
    definedness exactly looks constructible in a few lines. I share that
    expectation — and both of us are on notice from §8.1, where identifying a
    mechanism was mistaken for predicting an outcome. The mechanism here
    ("nothing constrains `run` relative to `Defined`") is not the outcome; the
    compile decides.

    AND THE RESIDUE TO WATCH IF (B) LANDS TRIVIALLY. Whether the counterexample
    survives the run/Val choice once made. One that dies under the Boolean
    threshold-query extension would mean the implication's truth depends on the
    representation choice — a (C)-shaped finding hiding inside a (B), and it must
    be reported as such rather than as a clean refutation.
-/

/-! ## 10. Problem 27, run

    Order of construction, per the pre-registration: the (A)-guard witness is
    built FIRST, so it cannot be retrofitted to whatever lands. -/

/-- A two-element layer. One method, costing nothing, which returns the
    structure itself. Nothing exotic: this is the smallest layer that can have
    an opinion. -/
def L0 : Layer where
  Rep := Bool
  Method := Unit
  run := fun _ b => b
  encode := fun _ => true
  decode := fun b => match b with | true => some () | false => none
  decode_encode := by intro m; cases m; rfl
  cost := fun _ => 0
  budget := 0

/-- A lattice on it with a genuine gap: it has an opinion about `true` and none
    about `false`. -/
def Om0 : Lattice L0 where
  Val := Unit
  zero := ()
  lt := fun _ _ => False
  Defined := fun b => b = true
  S := fun _ => ()

/-- (A)-GUARD, BUILT FIRST. The frame does not make everything method-
    inaccessible: `()` is affordable. -/
theorem guard_affordable : L0.available () := Nat.le_refl 0

/-- (A)-GUARD, second half. An affordable method DOES decide the relevant
    question on the defined region — indeed everywhere. So an (A) result could
    not have been vacuous. -/
theorem guard_decides_somewhere : ∀ x : L0.Rep, L0.run () x = true ↔ Om0.Defined x :=
  fun _ => Iff.rfl

/-- The gap is real: `false` is undefined. -/
theorem gap_exists : ¬ Om0.Defined false := by
  intro h; exact Bool.noConfusion h

/-- THE RESULT. Type-level partiality does NOT imply method-quantified
    inaccessibility. Outcome (B), by construction, with both guards discharged
    above rather than assumed. -/
theorem partiality_does_not_imply_inaccessibility :
    ¬ (∀ (L : Layer) (Ω : Lattice L),
        (∃ x : L.Rep, ¬ Ω.Defined x) → L.undecidable Ω.Defined) := by
  intro h
  exact h L0 Om0 ⟨false, gap_exists⟩ () guard_affordable guard_decides_somewhere

/-! ### 10.1 Readout

    OUTCOME (B). Type-level partiality does not imply method-quantified
    inaccessibility. The refutation is a construction, it carries no `sorry`, and
    `#print axioms` reports it and all four supporting lemmas as depending on NO
    axioms — not `propext`, not `Classical.choice`. This is the file's first
    result rather than its first record of a choice.

    BOTH GUARDS DISCHARGED, and the (A)-guard was built first as required.
    `guard_affordable` exhibits `cost ≤ budget` rather than assuming it, so the
    refutation does not hold vacuously through an unsatisfiable `available`. And
    `guard_decides_somewhere` exhibits an affordable method deciding the relevant
    question — everywhere, in fact — so an (A) result could not have been vacuous
    either. Neither guard was retrofitted.

    WHAT THE COUNTEREXAMPLE ACTUALLY SHOWS. `L0` is two-valued with one free
    method that returns its argument; `Om0` has an opinion about `true` and none
    about `false`. The method decides `Defined` exactly. So the lattice has a
    genuine gap AND the layer can see straight through it. Nothing pathological
    was needed — no large cardinals, no cost trickery — which is the point: the
    bare frame imposes NO relation whatsoever between `run` and `Defined`. The
    two were never connected, and Definition 17 has been quietly assuming they
    were.

    DEVIATION FROM THE PRE-REGISTRATION, declared rather than silently taken.
    The destination for (B) was written as "M.8, as a constructed counterexample
    with the standing of a theorem". M.8 is the CONJECTURES section; M.4 is where
    theorems live. Following the letter would file a proved, axiom-free theorem
    among the conjectures, which inverts the very distinction the destinations
    exist to protect. It goes to M.4 as Theorem 9, and this note records that the
    pre-registration said otherwise and why it was not followed. (The header's
    "belongs in M.8" is the same slip, written by me, and is corrected there too.)

    PRIORS, SCORED. The reviewer expected (B) cheaply, and so did I; both landed.
    Two confirmed priors in a row is worth less than the one falsification in
    §8.1, and the mechanism named in advance — "nothing constrains `run` relative
    to `Defined`" — is exactly what the construction exploits, so this time the
    mechanism and the outcome did cohere. That is not evidence the reasoning
    improved; it is evidence the question was easy.

    THE RESIDUE, still open. Whether this counterexample survives the run/Val
    choice. `L0`'s method decides `Defined` by returning its argument, which is
    available only because `Defined` here is `· = true` — a predicate the layer's
    Boolean `run` can express verbatim. Under the threshold-query extension the
    relevant question changes shape, and it is not obvious the same trick works.
    If it does not, the implication's truth depends on the representation choice,
    which is a (C)-shaped finding inside this (B) and must be reported as such.
    Not tested here; the choice is still unmade. -/

/-! ## 11. The threshold-query extension — PRE-REGISTRATION

    Written by the NON-RUNNER and committed before any line of the interface
    elaborates. The runner does not edit clauses 1–9 (clause 9). Reproduced here
    in condensed form; the reasons are load-bearing and are kept.

    1. INTERFACE IS A SEPARATE STRUCTURE OVER `Layer`, NOT A NEW FIELD. The
       compiled frame stays verbatim, so Theorem 9, both guards and the axiom
       audit need no re-verification. Extension-as-structure makes the signature
       event explicit; a new field would silently assert that every layer
       natively queries values — the unpaid formal promise the front matter now
       warns about. And it makes 27′ well-posed: survival becomes quantification
       over interfaces on the UNCHANGED `L0`.
         `ThresholdInterface (L : Layer) (V : Type)` with `QMethod`, `ask :
         QMethod → V → L.Rep → Bool`, `qcost`, affordability `qcost q ≤ L.budget`.

    2. `ask` IS A FAMILY INDEXED BY θ, not one query per θ. Per-θ supply needs
       θ-indexed budgets or an enumeration of `Val` by methods — an unforced
       choice smuggled in as bookkeeping. A family keeps one cost per method so
       affordability transfers unchanged, and it is the stronger adversary: any
       per-θ decider embeds as a family constant in θ, so inaccessibility against
       families implies it against per-θ deciders, never the reverse.

    3. GROUND TRUTH FOR CLEARANCE LIVES IN THE JOINED SIGNATURE — forced, not
       chosen. In the layer-only signature clearance at an undefined point has no
       truth-value, so the claim would be unstatable and the asymmetry would hold
       vacuously, failing its own guard. Grading is against the induced
       potential's clearance, aggregator abstract. Every outcome is relative to
       how the aggregator is quantified, and clause 6 makes that quantifier the
       experiment's subject rather than a nuisance parameter.

    4. PHASE DISCIPLINE: ELABORATE FIRST, PROVE SECOND. Statements are committed
       before any proof attempt. A statement that fails to elaborate is outcome
       (C) for its clause, recorded with the failing term kept in a comment, and
       no proving is attempted on it. Elaboration is the compile-decidable
       meaning of "stateable".

    5. THE TWO DEPENDENTS. 27′ survival `S`: there exist a joined structure over
       `L0`, an affordable `q` (witnessed), and θ with total agreement between
       `ask q θ` and clearance truth, INCLUDING at `L0`'s undefined point. `D`:
       the negation, universally over interfaces. Asymmetry `A`: for the general
       frame, every affordable family fails total agreement at every θ, conjoined
       with poverty guard `G`: some affordable family agrees on the defined
       region for some θ.

    6. THE AGGREGATOR QUANTIFIER IS THE QUESTION, pre-registered as two clauses.
       `S∃`: survival for SOME aggregator. `S∀`: for EVERY aggregator. If
       `S∃ ∧ ¬S∀`, survival is aggregator-relative — the gap persists or closes
       depending on the bridging law — and 27′'s answer is "waits on Problem 26",
       turning the dependency stack into a LOOP that must then be declared in
       both problems' texts rather than found later by a reader.

    7. DESTINATIONS, checked against which sections hold what: M.4 theorems, M.8
       conjectures.
         · `S` proved → M.4. Gap is representation-INDEPENDENT at the strength
           proved; regrounded Definition 17 unaffected (inaccessibility is
           required outright, not derived); `L0`'s undefined point is confirmed
           lattice-partial but NOT a boundary object, and the status note's
           "pending" becomes "not derivable; definitional".
         · `D` proved → M.4. The (C)-inside-(B) made real: the gap was an
           artifact of `Defined` being Boolean-expressible verbatim, and for
           clearance-type questions partiality regains teeth. Licences (does not
           presume) a follow-up: does lattice-partiality IMPLY clearance-
           inaccessibility, reconnecting for A5's actual question what Theorem 9
           severed.
         · `A` proved with `G` witnessed → M.4, and Definition 17's status note
           closes.
         · Any elaborating but unproved → M.8 as conjectures, sorry count rises
           honestly, stall recorded as stall.
         · Elaboration failure → (C), recorded in 27′ or as an explicit
           dependency on Problem 26's aggregator.

    8. PRIORS, RECORDED TO BE DISTRUSTED. Reviewer's: `S∃ ∧ ¬S∀`, by
       parametricity — with the aggregator universally quantified the induced
       value at the undefined point varies with it, so no fixed Boolean answer
       matches all unless `L0`'s fiber structure collapses; existentially
       quantified, choose the aggregator making truth match. Mechanism and
       prediction agree this time, which is a consistency property of the guess
       and not evidence for it (§8.1). Second-order, lower confidence: if `¬S∀`,
       its proof is nearly definitional and the finding is the loop with
       Problem 26 rather than the theorem.

    9. GOVERNANCE. The runner does not edit 1–8. Deviations are declared with
       reasons at the site, per the M.8→M.4 precedent; a deviation whose reason
       is "the clause was wrong" is permitted and expected. Standing addition for
       this run: for each of `S`, `D`, `A`, `G`, report whether the STATEMENT's
       elaboration needed anything from `Layer`'s self-encoding apparatus
       (`encode`, `decode`) or only the interface and joined structure — the
       diagonal bar says self-quotation must be seen to be used, and it matters
       whether the clearance question lives above or below that line.
-/

/-! ## 12. Phase one — elaboration only

    No proof is attempted in this section. Per clause 4, elaboration IS the test
    of "stateable", and a statement that fails here is (C) for its clause.

    DECLARED DEVIATION (clause 9). Clause 4 says to commit the statements "with
    `sorry`". Asserting `S`, `D` and `A` as sorry'd theorems would assert a
    contradiction — `D` is the negation of `S` — so they are committed as `def
    … : Prop`, which is what actually carries the elaboration test. Nothing is
    asserted here. The reason is that the clause as written cannot be followed
    literally without making the file inconsistent; the spirit — no proving
    before the statements are fixed and committed — is followed exactly. -/

/-- Clause 1's interface, as a separate structure over an unchanged `Layer`. -/
structure ThresholdInterface (L : Layer) (V : Type) where
  QMethod : Type
  /-- Clause 2: a family indexed by θ, one cost per method. -/
  ask     : QMethod → V → L.Rep → Bool
  qcost   : QMethod → Nat

/-- Affordability, inherited from the layer's budget rather than re-declared. -/
def ThresholdInterface.affordable {L : Layer} {V : Type}
    (I : ThresholdInterface L V) (q : I.QMethod) : Prop :=
  I.qcost q ≤ L.budget

/-- Clause 3: clearance truth, in the joined signature, graded against the
    induced potential. -/
def Joined.clearsAt (J : Joined) (agg : Aggregator J) (θ : J.X.Val) (x : J.L.Rep) : Prop :=
  J.X.lt θ (J.induced agg x)

/-- Total agreement between a query family and clearance truth. -/
def Agrees (J : Joined) (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val)
    (q : I.QMethod) (θ : J.X.Val) : Prop :=
  ∀ x : J.L.Rep, I.ask q θ x = true ↔ J.clearsAt agg θ x

/-- `S∃` — 27′ survival for SOME aggregator. Agreement is total, so it includes
    `L0`'s undefined point; affordability is witnessed, not assumed. -/
def S_ex : Prop :=
  ∃ (J : Joined), J.L = L0 ∧
    ∃ (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val)
      (q : I.QMethod) (θ : J.X.Val), I.affordable q ∧ Agrees J agg I q θ

/-- `S∀` — survival for EVERY aggregator. -/
def S_all : Prop :=
  ∃ (J : Joined), J.L = L0 ∧
    ∀ (agg : Aggregator J), ∃ (I : ThresholdInterface J.L J.X.Val)
      (q : I.QMethod) (θ : J.X.Val), I.affordable q ∧ Agrees J agg I q θ

/-- `D` — death: the negation, universally over interfaces. -/
def D : Prop := ¬ S_ex

/-- `A` — the asymmetry's invariant form, general frame. -/
def A : Prop :=
  ∀ (J : Joined) (agg : Aggregator J) (x : J.L.Rep), ¬ J.Om.Defined x →
    ∀ (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod), I.affordable q →
      ∀ θ : J.X.Val, ¬ Agrees J agg I q θ

/-- `G` — the poverty guard: some affordable family agrees on the DEFINED
    region. Without this, `A` could hold because nothing is decidable at all. -/
def G : Prop :=
  ∃ (J : Joined) (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val)
    (q : I.QMethod) (θ : J.X.Val), I.affordable q ∧
      ∀ x : J.L.Rep, J.Om.Defined x → (I.ask q θ x = true ↔ J.clearsAt agg θ x)

/-! ## 13. Phase two — the attempts -/

/-- A substrate for `L0`. `Val := Nat` with the usual order, so `rho_basin_pos`
    is discharged honestly rather than by an empty `lt`. -/
def X0 : Substrate where
  State := Unit
  Val   := Nat
  zero  := 0
  one   := 1
  lt    := fun a b => a < b
  sub   := fun a b => a - b
  P     := fun _ => 0
  basin := fun _ => True
  rho   := fun _ => 1
  rho_basin_pos := Nat.zero_lt_one

/-- The joined structure over the UNCHANGED `L0`, per clause 1. -/
def J0 : Joined where
  L := L0
  X := X0
  formulable := fun _ _ => True
  Om := Om0

/-- The constantly-false query family, affordable at zero cost. -/
def Qfalse : ThresholdInterface J0.L J0.X.Val where
  QMethod := Unit
  ask := fun _ _ _ => false
  qcost := fun _ => 0

/-- Threshold `0`, typed through the substrate. -/
def th0 : J0.X.Val := (0 : Nat)

/-- The zero aggregator. -/
def agg0 : Aggregator J0 := fun _ _ _ => (0 : Nat)

/-- With `agg0` and `th0`, clearance is `0 < 0` — false everywhere. -/
theorem clears_false (x : J0.L.Rep) : ¬ J0.clearsAt agg0 th0 x :=
  fun h => absurd h (Nat.lt_irrefl 0)

theorem qfalse_agrees (x : J0.L.Rep) :
    Qfalse.ask () th0 x = true ↔ J0.clearsAt agg0 th0 x := by
  constructor
  · intro h; exact Bool.noConfusion h
  · intro h; exact absurd h (clears_false x)

/-- `S∃` holds. -/
theorem S_ex_holds : S_ex :=
  ⟨J0, rfl, agg0, Qfalse, (), th0, Nat.le_refl 0, qfalse_agrees⟩

/-- `S∀` holds too — and this is the finding, not the theorem. For ANY
    aggregator the query family is chosen after it and simply COMPUTES the
    clearance truth. Nothing in the frame forbids that: `qcost` is a number
    compared against `budget`, wholly unconnected to what `ask` computes. -/
theorem S_all_holds : S_all := by
  refine ⟨J0, rfl, ?_⟩
  intro agg
  refine ⟨⟨Unit, fun _ θ x => @decide _ (Nat.decLt θ (J0.induced agg x)), fun _ => 0⟩,
          (), th0, Nat.le_refl 0, ?_⟩
  intro x
  exact decide_eq_true_iff

/-- Therefore `D` fails. -/
theorem D_fails : ¬ D := fun hD => hD S_ex_holds

/-- And `A` fails, by the `S∃` witness. -/
theorem A_fails : ¬ A := fun hA =>
  hA J0 agg0 false gap_exists Qfalse () (Nat.le_refl 0) th0 qfalse_agrees

/-- `G` holds — the poverty guard is discharged, so `A`'s failure is not the
    frame being unable to decide anything at all. -/
theorem G_holds : G :=
  ⟨J0, agg0, Qfalse, (), th0, Nat.le_refl 0, fun x _ => qfalse_agrees x⟩

/-! ### 13.1 Readout

    RESULTS. `S∃` holds, `S∀` holds, `D` fails, `A` fails, `G` holds. Axiom
    audit: all axiom-free except `S_all_holds`, which uses `propext` (via
    `decide_eq_true_iff`) and no choice. `G` is discharged, so `A`'s failure is
    NOT the frame being unable to decide anything.

    CLAUSE 6 IS ANSWERED, AND THE LOOP DOES NOT FORM. The pre-registration made
    the aggregator quantifier the experiment's subject: `S∃ ∧ ¬S∀` would have
    made survival aggregator-relative and turned the dependency stack into a
    loop with Problem 26. Both hold instead. Survival is aggregator-INDEPENDENT,
    27′ does not wait on Problem 26, and no loop needs declaring.

    THE REVIEWER'S PRIOR IS FALSIFIED, and the parametricity argument behind it
    fails at a specific step. It assumed the induced value at the undefined point
    varies with the aggregator so no fixed Boolean answer matches all of them —
    true, but irrelevant, because the query family is chosen AFTER the aggregator
    in `S∀`'s quantifier order, and may depend on it. `S_all_holds` exploits
    exactly that: given `agg`, the family simply COMPUTES clearance.

    THE FINDING, which is larger than the theorem and generalises §10. Nothing in
    this frame connects what a method computes to what it costs. `qcost` is a
    number compared against `budget`; `ask` is an arbitrary function. So an
    affordable query family can decide anything whatsoever, and no statement of
    the form "no affordable method decides X" is provable here for any X a
    function could compute. Theorem 9 was therefore NOT about `Defined` being
    Boolean-expressible verbatim — that was the local explanation, and it was too
    kind. The general fact is that **this frame cannot express hardness at all**,
    and every inaccessibility claim in it is a stipulation about the method set
    rather than a result.

    CONSEQUENCE FOR THE REGROUNDED DEFINITION 17, and it cuts. The method-
    relative clause is now known to be unprovable in the bare frame for any
    layer whose methods are unconstrained. It is not merely "required outright
    rather than derived" (§10's reading); it is **not derivable in principle
    here**, and the definition's status note must say so. The asymmetry's
    invariant form is not pending a choice — the choice has been made and the
    answer is that `A` is false. What would change this is a frame in which cost
    bounds computation, which this one is not and was never claimed to be.

    CLAUSE 9 STANDING REPORT. No statement and no proof in §§12–13 references
    `encode` or `decode`. The clearance question lives entirely below the
    self-quotation line: it needs the interface and the joined structure and
    nothing from the layer's self-encoding apparatus. That is consistent with the
    diagonal bar and, read the other way, is why it could be settled so cheaply —
    nothing here is a boundary object in the diagonal sense.

    DECLARED DEVIATION (clause 9). Clause 7 gives no destination for `¬A`; it
    anticipated `A` proved or unproved. `¬A` is theorem-grade and axiom-free, so
    it goes to M.4 alongside the others, and Definition 17's status note closes
    NEGATIVELY rather than positively — the outcome the destination table did not
    contemplate. Reason recorded rather than the result being filed under the
    nearest listed heading. -/

/-! ## 14. The cost probe — PRE-REGISTRATION (clauses by the non-runner)

    Committed before any construction. Runner does not edit clauses 1–6.

    THE SHAPE CHANGED. The probe is not "does `CostAxioms` suffice" but "which
    conjecture's debt is cost-shaped at all". Reviewer's prediction: neither. The
    diagonal owed self-application, which it had all along; opacity owes a
    measure.

    1. THE DIAGONAL CONJECTURE'S PROBLEM IS ITS PREDICATE, NOT ITS HYPOTHESIS.
       Comparing an input to a constant is trivial in every complexity theory
       ever proposed, so `undecidable (· = x)` is false under ANY cost axioms,
       including a full machine model. No strengthening rescues it. The Gödel
       transposition was never "some point's identity is undecidable" — it is
       SELF-APPLICATION. Commit instead:
         `D_L y := ∀ m', decode y = some m' → run m' y = false`
         statement: `∀ L m, ¬ (∀ y, run m y = true ↔ D_L y)`
       No `Defined`, no `CostAxioms`, no affordability — every method, not just
       affordable ones. Prior: PROVABLE, axiom-free, using `decode_encode`
       essentially; instantiate at `y := encode m`. Mechanism and prediction
       align, which the record says to distrust. If it proves, it discharges a
       `sorry` positively for the first time — by REPLACEMENT, the file recording
       that the original predicate was refutable under all cost models and that
       the correct transposition needs no cost model at all. The bar note was
       right about the mechanism while the statement was wrong about the object.

    2. THE CANTOR FACT AND CLAUSE 1 ARE ONE THEOREM. Cantor's argument IS
       self-application. Runner's choice whether to derive the cardinality bound
       as a corollary or prove it separately; declared either way. Destination
       for both: M.4. The `¬ Defined x` conjunct is DROPPED, not proved — Theorem
       9 already made lattice-partiality and inaccessibility independent, so the
       diagonal theorem is about inaccessibility alone and the link to boundary
       objects stays definitional at Definition 17's third clause.

    3. ARM 1, THE CONTROL. Refute both restatements under the COMMITTED
       `CostAxioms`: the runner's parity witness for the diagonal, an analogous
       one for opacity. Anti-vacuity by PROVING `CostAxioms` holds for each
       witness and exhibiting the affordable decider. Destination M.4 as
       Corollaries 10.3/10.4 — required, because they refute the committed state
       and the header contract now tracks that.

    4. ARM 3 — `CostAxioms₂` BY RELATIVIZATION. Blum's second axiom stated
       classically falls into §2's trap. Relativize through `encode`:
         `Blum2 L := ∀ n, ∃ m, available m ∧
            ∀ y, run m y = true ↔ (∃ m', decode y = some m' ∧ cost m' ≤ n)`
       — the layer reads a method's price off its code; a referent using only
       existing primitives, no machine model. Test whether Arm 1's opacity
       witness satisfies it. Prior: IT DOES, and rescues nothing. If so, Blum was
       the wrong debt-name for opacity: Blum's axioms are silent on the hardness
       of specific functions, and RR is a lower-bound barrier. Opacity owes
       (i) a `large` with content — Problem 25's prerequisite, now load-bearing
       rather than adjacent — and (ii) a hardness axiom about SETS not points.

    5. PHASE-ONE SHAPE CHECK ON OPACITY, before any arm runs on it. Flagged
       unverified by the reviewer: RR's conclusion is `constructive ∧ large ⟹
       ¬useful`, not `large ⟹ ¬constructive`. If the committed statement has the
       latter shape it is the inverse of the theorem it transposes, no hypothesis
       fixes it, and it is ledger instance nine. If the shape is right, strike
       with a note.

    6. GOVERNANCE AND PRIORS. Clause 1 proves (high, distrusted on principle).
       Clause 3 refutes both (high). Clause 4 elaborates and fails to rescue
       (moderate; `Blum2` is the reviewer's construction and may be too weak or
       mis-aimed — failure to elaborate is (C) and raises the register-boundary
       count, theirs). Destinations: M.4 theorems, M.8 conjectures, open problems
       for (C). Standing report: Clause 1's proof must be SEEN to use
       `decode_encode`; a proof going through without it means the predicate is
       degenerate and the result is wrong, not lucky.
-/

/-! ## 15. The cost probe, run -/

/-- Clause 1's predicate: the method encoded by `y` rejects its own code. -/
def D_L (L : Layer) (y : L.Rep) : Prop :=
  ∀ m', L.decode y = some m' → L.run m' y = false

/-- CLAUSE 1. No method computes `D_L` — no `Defined`, no `CostAxioms`, no
    affordability, every method. `decode_encode` is used essentially. -/
theorem diagonal_self_application (L : Layer) (m : L.Method) :
    ¬ (∀ y, L.run m y = true ↔ D_L L y) := by
  intro h
  have hde : L.decode (L.encode m) = some m := L.decode_encode m
  cases hb : L.run m (L.encode m) with
  | true =>
      have hD : D_L L (L.encode m) := (h (L.encode m)).mp hb
      have hf : L.run m (L.encode m) = false := hD m hde
      rw [hb] at hf; exact Bool.noConfusion hf
  | false =>
      have hD : D_L L (L.encode m) := by
        intro m' hm'
        have hmm : some m = some m' := hde.symm.trans hm'
        have hme : m = m' := Option.some.inj hmm
        subst hme; exact hb
      have ht : L.run m (L.encode m) = true := (h (L.encode m)).mpr hD
      rw [hb] at ht; exact Bool.noConfusion ht

/-- Clause 2, proved separately (declared choice): the computable diagonal. -/
def diagFn (L : Layer) : L.Rep → Bool :=
  fun y => match L.decode y with
           | some m' => !(L.run m' y)
           | none     => true

/-- CLAUSE 2. No layer computes every Boolean function on its own `Rep` — the
    cardinality bound of `encode`-injectivity, constructively. -/
theorem no_omniscient_layer (L : Layer) :
    ¬ (∀ f : L.Rep → Bool, ∃ m : L.Method, ∀ x, L.run m x = f x) := by
  intro h
  obtain ⟨m, hm⟩ := h (diagFn L)
  have hx : L.run m (L.encode m) = !(L.run m (L.encode m)) := by
    have h1 := hm (L.encode m)
    simp [diagFn, L.decode_encode m] at h1
  cases hb : L.run m (L.encode m) <;> rw [hb] at hx <;> simp at hx

/-! ### Arm 1 (clause 3): both restatements fall under the committed `CostAxioms` -/

/-- Parity-priced layer: identity deciders are free, odd methods cost their
    index, so costs are unbounded and `CostAxioms` holds. -/
@[reducible] def Lpar : Layer where
  Rep := Nat
  Method := Nat
  run := fun m x => decide (x = m / 2)
  encode := fun m => m
  decode := fun x => some x
  decode_encode := by intro m; rfl
  cost := fun m => if m % 2 = 0 then 0 else m
  budget := 0

@[reducible] def Ompar : Lattice Lpar where
  Val := Unit
  zero := ()
  lt := fun _ _ => False
  Defined := fun _ => False
  S := fun _ => ()

theorem Lpar_costAxioms : CostAxioms Lpar := by
  constructor
  intro n
  refine ⟨2 * n + 1, ?_⟩
  show n < (if (2 * n + 1) % 2 = 0 then 0 else 2 * n + 1)
  rw [if_neg (by omega : ¬((2 * n + 1) % 2 = 0))]
  omega

/-- Every identity predicate has a FREE decider: method `2x`. -/
theorem Lpar_id_cheap (x : Nat) :
    Lpar.available (2 * x) ∧ ∀ y, Lpar.run (2 * x) y = true ↔ y = x := by
  constructor
  · show (if (2 * x) % 2 = 0 then 0 else 2 * x) ≤ 0
    rw [if_pos (by omega : (2 * x) % 2 = 0)]
    exact Nat.le_refl 0
  · intro y
    show decide (y = 2 * x / 2) = true ↔ y = x
    rw [(by omega : 2 * x / 2 = x)]
    exact decide_eq_true_iff

/-- COROLLARY 10.3. The RESTATED diagonal conjecture is false: `CostAxioms`
    holds here and every identity predicate is still freely decidable. -/
theorem diagonal_restatement_refuted :
    ¬ (∀ (L : Layer) (Ω : Lattice L), CostAxioms L →
        ∃ x : L.Rep, ¬ Ω.Defined x ∧ L.undecidable (fun y => y = x)) := by
  intro h
  obtain ⟨x, _, hu⟩ := h Lpar Ompar Lpar_costAxioms
  obtain ⟨havail, hdec⟩ := Lpar_id_cheap x
  exact hu (2 * x) havail hdec

/-- Opacity witness: same pricing, but `run` can never fire at `0`, so `0` is
    incompressible — `hard` is satisfied, not dodged. -/
@[reducible] def Lopc : Layer where
  Rep := Nat
  Method := Nat
  run := fun m x => decide (x = m / 2 + 1)
  encode := fun m => m
  decode := fun x => some x
  decode_encode := by intro m; rfl
  cost := fun m => if m % 2 = 0 then 0 else m
  budget := 0

@[reducible] def Omopc : Lattice Lopc where
  Val := Unit
  zero := ()
  lt := fun _ _ => False
  Defined := fun _ => False
  S := fun _ => ()

theorem Lopc_costAxioms : CostAxioms Lopc := by
  constructor
  intro n
  refine ⟨2 * n + 1, ?_⟩
  show n < (if (2 * n + 1) % 2 = 0 then 0 else 2 * n + 1)
  rw [if_neg (by omega : ¬((2 * n + 1) % 2 = 0))]
  omega

theorem Lopc_zero_incompressible : Lopc.incompressible 0 := by
  intro m _
  show decide ((0:Nat) = m / 2 + 1) = false
  exact decide_eq_false (by omega)

/-- COROLLARY 10.4. The RESTATED opacity conjecture is false, with `hard`
    satisfied and `CostAxioms` proved. -/
theorem opacity_restatement_refuted :
    ¬ (∀ (L : Layer) (Ω : Lattice L) (large : (L.Rep → Prop) → Prop),
        (∃ x : L.Rep, L.incompressible x) → CostAxioms L →
        ∀ p : L.Rep → Prop, Broad L large p →
          (∀ m : L.Method, L.available m → ¬ (∀ x, L.run m x = true ↔ p x))) := by
  intro h
  refine h Lopc Omopc (fun _ => True) ⟨0, Lopc_zero_incompressible⟩ Lopc_costAxioms
    (fun x => x = 1) trivial 0 ?_ ?_
  · show (if (0:Nat) % 2 = 0 then 0 else 0) ≤ 0
    rw [if_pos (by omega : (0:Nat) % 2 = 0)]
    exact Nat.le_refl 0
  · intro x
    show decide (x = 0 / 2 + 1) = true ↔ x = 1
    rw [(by omega : (0:Nat) / 2 + 1 = 1)]
    exact decide_eq_true_iff

/-! ### Arm 3 (clause 4): `Blum2` by relativization -/

/-- The reviewer's relativized Blum-2: the layer can read a method's price off
    its code. A referent using only existing primitives — no machine model. -/
def Blum2 (L : Layer) : Prop :=
  ∀ n : Nat, ∃ m : L.Method, L.available m ∧
    ∀ y, L.run m y = true ↔ (∃ m', L.decode y = some m' ∧ L.cost m' ≤ n)

/-- CLAUSE 4, FIRST HALF — the prior is FALSIFIED. The Arm-1 opacity witness does
    NOT satisfy `Blum2`: its methods decide singletons, while the price predicate
    at `n = 0` holds of every even index. -/
theorem Lopc_not_blum2 : ¬ Blum2 Lopc := by
  intro hB
  obtain ⟨m, _, hm⟩ := hB 0
  have hcost0 : Lopc.cost 0 ≤ 0 := by
    show (if (0:Nat) % 2 = 0 then 0 else 0) ≤ 0
    rw [if_pos (by omega : (0:Nat) % 2 = 0)]
    exact Nat.le_refl 0
  have h0 : Lopc.run m 0 = true := (hm 0).mpr ⟨0, rfl, hcost0⟩
  have hz : (0:Nat) = m / 2 + 1 := of_decide_eq_true h0
  omega

/-- CLAUSE 4, SECOND HALF, and the reason the first half is not an accident.
    Under `Blum2`, NO element that is a code can be incompressible: the price
    query at that method's own cost fires on it. Incompressibility can therefore
    only live at NON-CODES. -/
theorem blum2_kills_incompressible (L : Layer) (hB : Blum2 L)
    (x : L.Rep) (m' : L.Method) (hx : L.decode x = some m') :
    ¬ L.incompressible x := by
  intro hinc
  obtain ⟨m, havail, hm⟩ := hB (L.cost m')
  have ht : L.run m x = true := (hm x).mpr ⟨m', hx, Nat.le_refl _⟩
  have hf : L.run m x = false := hinc m havail
  rw [ht] at hf; exact Bool.noConfusion hf

/-! ### 15.1 Readout

    CLAUSE 1 — PROVED, AXIOM-FREE. `diagonal_self_application` depends on no
    axioms at all, and `decode_encode` is visible in its proof, as clause 6's
    standing report demanded. The reviewer's diagnosis was right and sharper than
    "the hypothesis is too weak": the transposition's PREDICATE was wrong.
    Identity-with-a-point is cheap in every complexity theory, so no cost axiom
    could ever have rescued it. Self-application needs no cost theory whatever.

    CLAUSE 2 — PROVED (`propext`). `no_omniscient_layer`: no layer computes every
    Boolean function on its own `Rep`. Declared choice: proved separately via a
    computable diagonal rather than derived as a corollary, because the
    constructive form needs no Cantor library and keeps the file Mathlib-free.

    CLAUSE 3 — BOTH RESTATEMENTS REFUTED, with `CostAxioms` PROVED for each
    witness and the affordable decider exhibited, so neither refutation is
    vacuous. Corollaries 10.3 and 10.4.

    CLAUSE 4 — THE PRIOR IS FALSIFIED, AND THE CONCLUSION SURVIVES BY ANOTHER
    ROUTE. `Lopc` does NOT satisfy `Blum2`: its methods decide singletons while
    the price predicate at `n = 0` holds of every even index. So `Blum2` is not
    idle here — it excludes the Arm-1 witness. But it rescues nothing, for a
    reason the pre-registration did not anticipate:
    `blum2_kills_incompressible` (axiom-free) shows that under `Blum2` NO CODE
    CAN BE INCOMPRESSIBLE — the price query at a method's own cost fires on its
    own code. Incompressibility survives only at NON-CODES. So on any layer
    where `decode` is total, `Blum2` makes opacity's hardness hypothesis
    UNSATISFIABLE, and the conjecture holds vacuously. That is worse than being
    refuted: it means `incompressible` as defined is not a formalization of
    Razborov–Rudich hardness at all. The reviewer's downstream conclusion stands
    — opacity's debt is not cost-shaped — reached by a route neither of us
    predicted.

    CLAUSE 5 — FIRES. The committed opacity statement has the shape
    `large p → no affordable method computes p`, i.e. `large ⟹ ¬constructive`.
    Razborov–Rudich concludes `constructive ∧ large ⟹ ¬useful`. The transposition
    dropped USEFULNESS, and the dropped conjunct is exactly what makes the
    statement false: `p := fun _ => True` is broad, trivially computable, and
    useless — which is precisely the witness of Corollaries 10.2 and 10.4. The
    refutations were never deep; they were the missing conjunct showing up. Do
    not attempt to fix this with hypotheses on cost. Ledger instance nine.

    NET. Neither conjecture's debt was cost-shaped. The diagonal owed
    self-application and had it in `decode_encode` since the first commit. Opacity
    owes a `large` with content (Problem 25's prerequisite, now load-bearing) and
    a hardness notion about SETS rather than points, plus the usefulness conjunct
    clause 5 found missing. `CostAxioms` and `Blum2` end this run as honest stubs
    with no dependents — which is the correct outcome for a debt that was
    mis-named, and is recorded rather than tidied away. -/

/-! ## 16. Shape audit of the last `sorry`

    `recipe_inevitability` was the only surviving conjecture marker and the only
    statement in this file whose fidelity nobody but its transcriber had checked.
    The session's record on sorry'd transcriptions was zero for two. It is now
    zero for three.

    FIVE DEVIATIONS FROM THEOREM 7 AS COMMITTED, found by reading the two side by
    side. The first is fatal on its own; the rest are why a patch is not enough.

      1. NORMALIZATION DROPPED. `ρ_∞` in the manuscript is a stationary
         probability measure. `Substrate` lets `rho` and `one` be unrelated, so
         nothing says total mass is `one`. Refuted below.
      2. THE INITIAL CONDITION IS GONE. Theorem 7 says "for any initial condition
         Ψ₀ ∈ 𝒳" — that ANY start reaches the basin is the theorem's content. The
         transcription quantifies over no start at all.
      3. θ AND θ > θ_c ARE GONE. Theorem 7 is parameterized by θ ∈ Ω and its
         hypothesis is conditional on being above the threshold. `Substrate` has
         no θ, so the conditionality vanished in transport.
      4. THE BASIN IS UNLINKED FROM `P`. In Theorem 7 the basin is the basin of a
         non-degenerate local maximum of `P` with depth ΔP > 0 — Morse for
         existence, Kramers for residence. Here `basin` is a free predicate and
         `P` never appears in the statement.
      5. ERGODICITY REPLACED BY BIRKHOFF'S CONCLUSION. Theorem 7 hypothesizes
         that a specific Langevin process is ergodic. `Ergodic` here states that
         time-average occupation approaches `ρ_∞` — which is what Birkhoff
         DELIVERS from that hypothesis, i.e. an intermediate step of the proof
         assumed as a premise. -/

/-- Deviation 1, made concrete: mass `1` spread over a scale where `one` is `10`.
    Nothing in `Substrate` forbids it. -/
@[reducible] def Xbad : Substrate where
  State := Unit
  Val   := Nat
  zero  := 0
  one   := 10
  lt    := fun a b => a < b
  sub   := fun a b => a - b
  P     := fun _ => 0
  basin := fun _ => True
  rho   := fun _ => 1
  rho_basin_pos := Nat.zero_lt_one

@[reducible] def occBad : Nat → (Xbad.State → Prop) → Xbad.Val := fun _ _ => 1

theorem occBad_ergodic : Ergodic Xbad occBad := by
  intro A ε hε
  refine ⟨0, fun t _ => ?_⟩
  have h1 : 1 ≤ ε := hε
  have hz : (1:Nat) - ε = 0 := Nat.sub_eq_zero_of_le h1
  show (1:Nat) - ε < 1
  rw [hz]
  exact Nat.zero_lt_one

/-- THE LAST `sorry` MARKED A FALSEHOOD TOO. The occupation converges to the
    stationary measure exactly as `Ergodic` demands, and the conclusion still
    fails — because `1 - ε` is measured against a `one` that has nothing to do
    with the measure's total mass. -/
theorem recipe_inevitability_refuted :
    ¬ (∀ (X : Substrate) (occupation : Nat → (X.State → Prop) → X.Val),
        Ergodic X occupation →
        ∀ ε : X.Val, X.lt X.zero ε →
          ∃ T : Nat, ∀ t : Nat, T < t → X.lt (X.sub X.one ε) (occupation t X.basin)) := by
  intro h
  obtain ⟨T, hT⟩ := h Xbad occBad occBad_ergodic 1 (by show (0:Nat) < 1; omega)
  have hbad : (10 : Nat) - 1 < 1 := hT (T + 1) (by omega)
  omega

/-! ## 17. Problem 29 — THE ENUMERATION (by the non-transcriber)

    Written by the reviewer, who has never seen a prior transcription of
    Theorem 7, and committed BEFORE any term is written. This is the
    countermeasure of Problem 29 applied for the first time, and to the case that
    motivated it. The transcriber checks each item off against the finished term;
    an item absent from the term is a defect, an item absent from THIS LIST that
    the term reveals is the enumerator's ledger entry.

    A. OBJECTS AND TYPES
     1. `𝒳` substrate state-space — type only; no structure asserted by the
        statement's logic (smoothness serves ∇ and Morse, not the statement).
     2. `Ω` — A6 supplies the TYPE and nothing more; only `θ ∈ Ω` is load-bearing.
     3. `θ ∈ Ω` — one fixed parameter; every θ-mentioning object means THIS θ.
     4. `P : 𝒳 → Ω → Val` — substrate-side `P`, the Problem 26 letter. Never
        written bare.
     5. `θ_c` — UNDEFINED in the appendix. Parameter, not constant.
     6. `Ψ*` — depends on θ; witness of (i)'s existential, same witness in the
        conclusion. Uniqueness NOT asserted; multiple witnesses with different
        basins are not excluded by the statement.
     7. `basin(Ψ*)` — NEVER DEFINED; only characterized via Morse in the sketch.
        Must carry its link to `P(·;θ)` and `Ψ*` IN ITS TYPE — the dropped link.
     8. `>` on `Ω` — UNDEFINED. A6 gives manifold, measure, filtration; none is
        an order, so `θ > θ_c` is ill-typed. Parameter `above : Ω → Prop`. The
        manuscript owes both the threshold AND the relation.
     9. `ΔP > 0` basin depth — parameter with `0 < ΔP`. See item 27.
    10. `γ > 0` — A3's adaptation rate.
    11. `D > 0` diffusion — COLLIDES with Definition 3's `D(Φ,C_j)`. Named
        `Dnoise`. See item 27.
    12. `W_t` — not transcribable Mathlib-free; see 15.
    13. `Ψ_t` — process; depends on `Ψ₀, θ, γ, D`.
    14. `Pr` — over the noise, `Ψ₀` a deterministic point.
    15. DECLARED REPRESENTATION CHOICE: the SDE cannot be written here. Faithful
        abstraction is a family of marginal laws with `Pr[Ψ_t ∈ B] := law t Ψ₀ B`,
        carrying `P, θ, γ, D` as arguments so the dependence is in the type even
        though the dynamics are not. Consequences at item 31.
    16. `Val` — needs `0`, `1`, `<`, and subtraction for `1 − ε`.

    B. HYPOTHESES, each a separate conjunct
    17. (i-a) `above θ`.
    18. (i-b) non-degenerate local maximum — parameter predicate.
    19. NORMALIZATION: `∀ t Ψ₀, law … (fun _ => True) = 1`. The defect that killed
        the last transcription. It lives on `law`, not on any ρ_∞.
    20. (i-c) "of carrier-class type" — undefined in the material supplied;
        parameter predicate, and recorded as a candidate fourth undefined term.
    21. (i-d) `0 < ΔP`.
    22. (ii) ergodicity FOR THIS θ.
    23. `0 < γ`, `0 < Dnoise`.
    24. WHAT ERGODICITY MAY MEAN: unique invariant measure / Birkhoff / mixing.
        The last transcription assumed Birkhoff's CONCLUSION as premise. Faithful
        move: an abstract predicate, NOT unfolded — the statement says "is
        ergodic" and no more.
    25. ρ_∞ IS ABSENT FROM THE STATEMENT. It is a proof object. Checked by grep.

    C. QUANTIFIER ORDER
    26. `∀ P θ, [17–23] → ∀ Ψ₀, ∀ ε > 0, ∃ T, ∀ t > T, Pr > 1 − ε`. `T` may depend
        on `Ψ₀`; the uniform-in-`Ψ₀` reading is STRONGER and is not what is
        written.

    D. STATEMENT/PROOF MISMATCHES — refutation targets, not transcription items
    27. `ΔP` and `Dnoise` appear in hypotheses and NOWHERE in the conclusion; the
        conclusion is quantitatively independent of noise level.
    28. The sketch yields a time fraction equal to `ρ_∞(basin)` — fixed and `< 1`
        for nondegenerate noise, since `e^{P/D} > 0` everywhere. Then no `T`
        exists for `ε < 1 − ρ_∞(basin)`. The sketch supports "fraction → 1 as
        ΔP/D → ∞"; the statement claims "> 1 − ε for every ε at fixed D".
    29. Pointwise-in-time vs time-average: the conclusion is about marginals
        (mixing); Birkhoff gives time averages.
    30. Sketch-internal: stationary density of `γ∇P dt + √(2D)dW` is `∝ e^{γP/D}`,
        not `e^{P/D}`.

    E. PRE-REGISTRATION FOR THE REFUTATION
    31. The witness must be a GENUINE process, not an artifact of item 15's
        abstraction: a finite-state chain with strictly positive transitions,
        hence unique strictly positive stationary distribution. Two states
        suffice. Guards: every hypothesis 17–23 exhibited, and the basin
        non-empty with `Ψ* = in`.
    32. OUTCOME (R) — refuted. THE BOUNDARY SENTENCE FLIPS: the transport was
        faithful, checked item by item; the defect is in Theorem 7 AS STATED.
        Destination M.4, and Theorem 7 is revised. Propagation sites marked in
        advance: its Implication, its contingency note, Theorem 8's table row,
        and any chapter citing recipe inevitability as a theorem.
    33. OUTCOME (F) — faithful, not refuted: a `sorry` marking a believed
        statement, and item 28 was wrong.
    34. OUTCOME (C) — an item lacks a referent even as a parameter. Candidates:
        `above` (8), `carrierClass` (20). A stubbed item is a DECLARED gap, which
        is not a dropped one.
    35. PRIORS: (R) at high confidence via the two-state chain on item 28 —
        mechanism stated alongside the prediction, which the record says is a
        consistency property of the guess. Secondary: item 8 is the sharpest
        MANUSCRIPT finding independent of the refutation, since hypothesis (i)
        has been ill-typed since it was written and Theorem 8's table inherits it.
    36. CALIBRATION: the five defects of Theorem 13 map onto items 19, 26, 17/8,
        7, and 24 — all five are on this list.

    AND A NOTE ON DIRECTION, recorded before the result. Every ledger entry so
    far was a transport loss: the manuscript right, the term lossy. Items 27–29
    are not that. If (R) lands it is the first time the skeleton reaches back
    through a FAITHFUL transcription and finds the informal register claiming
    more than its own proof delivers. It cuts against the manuscript, and the
    record should say so in the voice it used the ten times it cut the other way.
-/

end RE
