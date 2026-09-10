/-
  BoundaryResidue.lean
  Representation skeleton for Appendix M: Definition 17 (boundary object),
  Conjecture 7 (boundary residue), Open Problems 21, 22, 25.

  WHAT THIS IS
    A record of representation choices. Each choice is annotated with the open
    problem it decides. The payload is the annotations, not the theorems.

  WHAT IT HAS BECOME (updated 2026-09-10). It began as the above and is no
    longer only that. It proves results about the frame and about the
    manuscript's own theorems — among them a refutation of one of those
    theorems as stated (Theorem 14), of the unamended drafts of its
    replacement, and of the first general statements of that replacement's
    Parts A and B — and it carries exactly two `sorry` sites, the amended
    general statements of §23.

    A CORRECTION, kept rather than deleted. An earlier version of this paragraph
    said the two `sorry` sites present at 247a19a were "the first to arrive
    shape-audited rather than be removed." They did arrive shape-audited, and
    they were FALSE: the hypothesis list itself had dropped that the kernel is a
    kernel, and the reviewer refuted both before the markers were a day old.
    Shape-auditing a statement checks that it says what its hypotheses say; it
    does not check that the hypotheses are the right ones. The contract below
    has now been broken TWICE and recorded both times before repair. It is
    currently kept.

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

  COMPILATION RECORD (branch target-xii, 2026-09-10). Lean 4.15.0
    (commit 11651562caae), bare toolchain, no Mathlib. Exit 0, zero errors.
    Warnings: exactly two, both `declaration uses 'sorry'`, at
    `REamend.general_partA` and `REamend.general_partB` — the file's only
    conjecture markers, restated in §23 against the amended hypotheses, each
    with a proved instance and a refuted predecessor. The false `REgen`
    statements they replace are verified ABSENT, by Lean reporting them as
    unknown constants — not by grep, whose prefix match once reported a second
    declaration that was in fact `general_partA_refuted`. `formal/check.sh`
    passes; it audits only the six frame definitions and is not the authority on
    `sorry` sites — this record is.

    REPRODUCTION HISTORY. The peer reviewer reproduced three commits
    independently, each byte-exact from `git show`, in a separate directory,
    each matching the audit line for line — three machine runs, not readings.
    66c08d5: reproduced. 247a19a: reproduced, and then its two `sorry`'d general
    statements REFUTED (§22). 9872874: reproduced, with the false `REgen`
    statements confirmed unknown to Lean — and then a second witness supplied
    against it, stochastic but not additive, which forces the `additive` field
    that §22 left forced only by argument (§22.2). ff5aef2: reproduced — the
    fourth independent run — with the §22.2 code lines diffed against the peer's
    original and found identical modulo docstrings. The commit that merges to
    main adds only this paragraph to ff5aef2; its code is the code reproduced. The target-ix branch adds §24 — the target (ix)
    confirming instance — on top of that. 7493679: reproduced — the FIFTH
    independent run — including an independent check that the ff5aef2 →
    02feeed diff is a single hunk before the first namespace. The commit that
    merges target-ix adds only this sentence; its code is the code reproduced.
    The p25-pushforward branch adds §§25–27 — the Problem 25 pushforward probe —
    on top of that; the reviewer re-runs only if the report does not add up.
    The target-x branch adds §§28–29, re-checking every result derived from `J0`
    on an A2-conforming witness.
    The target-xi branch adds §§30–31 and AMENDS THE `Substrate` STRUCTURE ITSELF:
    ρ_∞ is now required to be a measure.
    The target-xii branch adds §§32–33: Problem 26's bridging law, and the first
    theorems in the record about Definition 1's potential.

    Axiom audit, as printed:
      'RE.Layer.undecidable' does not depend on any axioms
      'RE.Layer.incompressible' does not depend on any axioms
      'RE.Layer.available' does not depend on any axioms
      'RE.Lattice.P' does not depend on any axioms
      'RE.Lattice.clears' does not depend on any axioms
      'RE.Broad' does not depend on any axioms
      'RE.diagonal_self_application' does not depend on any axioms
      'RE.no_omniscient_layer' depends on axioms: [propext]
      'RE.partiality_does_not_imply_inaccessibility' does not depend on any axioms
      'RE.recipe_inevitability_refuted' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.occBad_ergodic' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.theorem7_as_stated_refuted' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.lawTwo_is_derived' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.S_ex_holds' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.S_all_holds' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.D_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.A_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE.G_holds' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE4.unamendedA_refuted' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RE5.unamendedC_refuted' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REC.iii_singular_fails' depends on axioms: [propext, Quot.sound]
      'REgen.two_state_is_finite_chainU' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REgen.partA_instance' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REgen.partB_instance' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref.unamended_general_partA_false' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref.unamended_general_partB_false' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref.bad_is_finite_chain' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref2.stochastic_alone_insufficient_A' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref2.stochastic_alone_insufficient_B' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref2.stepBad2_not_additive' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REref2.bad2_is_finite_chainU' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REamend.two_state_is_finite_chain' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REamend.bad_not_amended' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REamend.bad2_not_amended' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REamend.stepBad_additive' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.chain3' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.exact3' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.law_ge2' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.ix_partA' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.ix_partB' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.ix_not_stationary_at_one' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REix.ix_rows_distinct' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.pushMass_additive' depends on axioms: [propext, Quot.sound]
      'REp25.pushMass_additive_G' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.pushMass_total_G' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.A2_G' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.pos_mass_true' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.zero_mass_false' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.false_is_formulated' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.hadd_U' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.not_sv_bad' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.additivity_fails_bad' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.large_true' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.not_large_false' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.constructive_true_Lid' depends on axioms: [propext]
      'REp25.rr_hosted_on_Lid_forces' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REp25.rr_hosted_satisfiable' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.legal_J1' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.S_ex_legal' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.S_all_legal' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.D_fails_legal' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.A_fails_legal' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REx.G_holds_legal' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExi.constRho_violates_empty' does not depend on any axioms
      'RExi.constRho_violates_add' does not depend on any axioms
      'RExi.pushMass_additive_intrinsic' depends on axioms: [propext, Quot.sound]
      'RExii.c26_sat' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.c26_ref_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.A1_substrate_discrimination' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.legal_JS' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.fiber_mass_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.S_nonzero' does not depend on any axioms
      'RExii.shared_lattice_data' depends on axioms: [propext, Classical.choice, Quot.sound]
      'RExii.substrates_differ' depends on axioms: [propext, Classical.choice, Quot.sound]
      'REamend.general_partA' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
      'REamend.general_partB' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]

    The six frame definitions report no axioms. `Classical.choice` elsewhere
    enters through declared representation choices (item 15 onward), never the
    frame; `sorryAx` appears at exactly the two amended general statements.

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
    ¬ (∀ (L : Layer) (_Ω : Lattice L) (large : (L.Rep → Prop) → Prop),
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
  /-- (xi) Addition on values, with NO laws: no proof in this file needs one. -/
  add   : Val → Val → Val
  /-- Theorem 7's `P(Ψ; θ)`: emergence potential ON A SUBSTRATE STATE. -/
  P     : State → Val
  /-- `basin(Ψ*)`, the carrier-class local maximum's basin. -/
  basin : State → Prop
  /-- The stationary measure `ρ_∞`. Note the type: a valuation on SETS OF
      STATES. This is the object the discriminator was built to inspect. -/
  rho   : (State → Prop) → Val
  rho_basin_pos : lt zero (rho basin)
  /-- (xi) ρ_∞ is a measure: the empty set has mass zero… -/
  rho_empty : rho (fun _ => False) = zero
  /-- …and masses add over disjoint sets. -/
  rho_add : ∀ A B : State → Prop, (∀ s, ¬ (A s ∧ B s)) →
    rho (fun s => A s ∨ B s) = add (rho A) (rho B)

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

open Classical in
/-- A substrate for `L0`. `Val := Nat` with the usual order, so `rho_basin_pos`
    is discharged honestly rather than by an empty `lt`. -/
noncomputable def X0 : Substrate where
  State := Unit
  Val   := Nat
  zero  := 0
  one   := 1
  lt    := fun a b => a < b
  sub   := fun a b => a - b
  add   := fun a b => a + b
  P     := fun _ => 0
  basin := fun _ => True
  rho   := fun B => if B () then 1 else 0
  rho_basin_pos := by simp
  rho_empty := by simp
  rho_add := by
    intro A B hdis; have h := hdis ()
    by_cases a : A () <;> by_cases b : B () <;> simp_all

/-- The joined structure over the UNCHANGED `L0`, per clause 1. -/
noncomputable def J0 : Joined where
  L := L0
  X := X0
  formulable := fun _ _ => True
  Om := Om0

/-- The constantly-false query family, affordable at zero cost. -/
noncomputable def Qfalse : ThresholdInterface J0.L J0.X.Val where
  QMethod := Unit
  ask := fun _ _ _ => false
  qcost := fun _ => 0

/-- Threshold `0`, typed through the substrate. -/
noncomputable def th0 : J0.X.Val := (0 : Nat)

/-- The zero aggregator. -/
noncomputable def agg0 : Aggregator J0 := fun _ _ _ => (0 : Nat)

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
    ¬ (∀ (L : Layer) (_Ω : Lattice L) (large : (L.Rep → Prop) → Prop),
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

open Classical in
/-- Deviation 1, made concrete: mass `1` spread over a scale where `one` is `10`.
    Nothing in `Substrate` forbids it. -/
@[reducible] noncomputable def Xbad : Substrate where
  State := Unit
  Val   := Nat
  zero  := 0
  one   := 10
  lt    := fun a b => a < b
  sub   := fun a b => a - b
  add   := fun a b => a + b
  P     := fun _ => 0
  basin := fun _ => True
  rho   := fun B => if B () then 1 else 0
  rho_basin_pos := by simp
  rho_empty := by simp
  rho_add := by
    intro A B hdis; have h := hdis ()
    by_cases a : A () <;> by_cases b : B () <;> simp_all

@[reducible] noncomputable def occBad : Nat → (Xbad.State → Prop) → Xbad.Val := fun _ _ => 1

open Classical in
theorem occBad_ergodic : Ergodic Xbad occBad := by
  intro A ε hε
  refine ⟨0, fun t _ => ?_⟩
  have h1 : 1 ≤ ε := hε
  show (if A () then 1 else 0) - ε < 1
  by_cases hA : A ()
  · rw [if_pos hA, Nat.sub_eq_zero_of_le h1]; exact Nat.zero_lt_one
  · rw [if_neg hA, Nat.zero_sub]; exact Nat.zero_lt_one

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

/-! ## 18. The faithful transcription, item by item

    Every parameter below carries its item number. Nothing is resolved silently;
    where the enumeration says "parameter", it is a parameter. -/

/-- Theorem 7, transcribed against §17. Item numbers in comments. -/
def Theorem7_faithful
    (X : Type)                                            -- 1  𝒳
    (Th : Type)                                           -- 2  Ω: type only
    (Val : Type) (zeroV oneV : Val)                       -- 16
    (ltV : Val → Val → Prop) (subV : Val → Val → Val)     -- 16
    (Psub : X → Th → Val)                                 -- 4  never bare `P`
    (above : Th → Prop)                                   -- 5, 8  θ_c AND the order
    (nondegLocalMax : (X → Val) → Th → X → Prop)          -- 18
    (carrierClass : X → Prop)                             -- 20
    (basin : (X → Val) → X → (X → Prop))                  -- 7  link to P and Ψ* in the type
    (depth : (X → Val) → X → Val)                         -- 9  ΔP
    (gamma Dnoise : Val)                                  -- 10, 11
    (law : (X → Val) → Th → Val → Val → Nat → X → (X → Prop) → Val)  -- 15
    (ErgodicLaw : Prop)                                   -- 24  NOT unfolded
    (theta : Th)                                          -- 3
    : Prop :=
  above theta →                                                                    -- 17
  (∀ (t : Nat) (start : X),
      law (fun s => Psub s theta) theta gamma Dnoise t start (fun _ => True)
        = oneV) →                                                                  -- 19 normalization
  ErgodicLaw →                                                                     -- 22
  ltV zeroV gamma → ltV zeroV Dnoise →                                             -- 23
  ∀ Ψstar : X,                                                                     -- 6
    nondegLocalMax (fun s => Psub s theta) theta Ψstar →                           -- 18
    carrierClass Ψstar →                                                           -- 20
    ltV zeroV (depth (fun s => Psub s theta) Ψstar) →                              -- 21
    ∀ start : X, ∀ ε : Val, ltV zeroV ε →                                          -- 26 order as written
      ∃ T : Nat, ∀ t : Nat, T < t →
        ltV (subV oneV ε)
            (law (fun s => Psub s theta) theta gamma Dnoise t start
                 (basin (fun s => Psub s theta) Ψstar))                            -- 26 conclusion

/-! ### 18.1 The refutation witness (item 31): a genuine two-state chain

    Strictly positive transitions — from either state, `in` and `out` each with
    mass one half — so the chain is irreducible and aperiodic with a unique,
    strictly positive stationary distribution, ergodic under any of item 24's
    three readings. `Val := Nat` with `oneV := 100`, so "one half" is `50`.
    At `t = 0` the law is the point mass at the deterministic start (item 14). -/

open Classical in
/-- Marginal laws of the two-state chain. `X := Bool`, `in := true`. -/
noncomputable def lawTwo : (Bool → Nat) → Unit → Nat → Nat → Nat → Bool → ((Bool → Prop) → Nat) :=
  fun _ _ _ _ t start B =>
    if t = 0 then (if B start then 100 else 0)
    else (if B true then 50 else 0) + (if B false then 50 else 0)

/-- Item 19 exhibited, not assumed: the chain is a probability law at every time
    and every start. -/
theorem lawTwo_normalized :
    ∀ (t : Nat) (start : Bool),
      lawTwo (fun _ => 0) () 1 1 t start (fun _ => True) = 100 := by
  intro t start
  by_cases ht : t = 0 <;> simp [lawTwo, ht]

/-- OUTCOME (R). The transcription is faithful to §17 item by item, every
    hypothesis is exhibited by a genuine ergodic process, the basin is non-empty
    with `Ψ* = in` — and the conclusion fails. The defect is in Theorem 7 as
    stated, not in the transport. -/
theorem theorem7_as_stated_refuted :
    ¬ Theorem7_faithful Bool Unit Nat 0 100 (fun a b => a < b) (fun a b => a - b)
        (fun _ _ => 0)                    -- Psub, item 4
        (fun _ => True)                   -- above, items 5/8
        (fun _ _ _ => True)               -- nondegLocalMax, item 18
        (fun _ => True)                   -- carrierClass, item 20
        (fun _ _ => fun s => s = true)    -- basin: non-empty, contains Ψ*, item 7
        (fun _ _ => 1)                    -- depth ΔP, item 9
        1 1                               -- gamma, Dnoise, items 10/11
        lawTwo                            -- item 15
        True                              -- ErgodicLaw, item 24
        () := by
  intro h
  obtain ⟨T, hT⟩ :=
    h trivial lawTwo_normalized trivial (by decide) (by decide)
      true trivial trivial (by decide) true 10 (by decide)
  have hbad := hT (T + 1) (by omega)
  have hval : lawTwo (fun _ => 0) () 1 1 (T + 1) true (fun s => s = true) = 50 := by
    simp [lawTwo]
  rw [hval] at hbad
  have hb2 : (100 : Nat) - 10 < 50 := hbad
  omega

/-! ### 18.2 Checkoff and readout

    ITEMS 1–26, EACH PRESENT IN THE TERM. Every one is annotated at its
    parameter or conjunct above. Items 5 and 8 are stubbed as the single opaque
    predicate `above` — a DECLARED gap (item 34), not a dropped one, and the
    reason is Problem 30. Item 20 (`carrierClass`) likewise. Item 25 verified by
    grep: no `rho`, `ρ_∞` or `stationary` occurs anywhere in `Theorem7_faithful`.
    Item 6 declared: `Ψ*` is universally quantified with (i)'s conditions as
    hypotheses, so the conclusion refers to the same witness, and multiplicity is
    handled by taking every witness rather than choosing one.

    ITEM 34 (C) PARTIALLY: two items are stubs. Both were stubbed knowingly, both
    are named in Problem 30, and both would have been silent drops without the
    enumeration.

    OUTCOME (R), item 32. The refutation goes through. Guards: the witness is a
    genuine two-state chain with strictly positive transitions in both
    directions — irreducible, aperiodic, unique strictly positive stationary
    distribution, ergodic under all three readings of item 24 — and every
    hypothesis 17–23 is exhibited, `lawTwo_normalized` proved rather than
    assumed, with the basin non-empty and containing `Ψ*`.

    AXIOM COST, DECLARED. `theorem7_as_stated_refuted` carries
    `[propext, Classical.choice, Quot.sound]`. The choice enters through item
    15's abstraction: a law consumes `X → Prop`, and deciding membership of an
    arbitrary predicate needs classical decidability. It is a cost of the
    representation, not a hidden hypothesis, and it does not touch the frame —
    `check.sh` is unaffected.

    ITEM 36, CALIBRATION OF THE COUNTERMEASURE — ITS FIRST DATA POINT. The
    enumeration was written by someone who had never transcribed the theorem and
    committed before the term. All five defects of Theorem 13 appear on it
    (19, 26, 17/8, 7, 24). The transcription checked off every item, and the
    refutation still went through — which is the designed outcome: the method
    produced a faithful term whose falsity belongs to the theorem. The
    enumerator's list also caught three undefined terms and one type error
    (Problem 30) that eleven prior readings by both of us had not. NO ITEM WAS
    FOUND DURING TRANSCRIPTION THAT THE LIST HAD MISSED, so there is no
    enumerator's ledger entry from this run.

    ITEM 35 SCORED. Prior (R) at high confidence: correct, by the predicted
    mechanism — item 28's two-state chain. Mechanism and prediction agreed, which
    §8.1 says is a consistency property of the guess and not evidence; recorded
    as such. Secondary prior — that item 8 would be the sharpest manuscript
    finding independent of the refutation — also correct, and it is Problem 30.

    POSTSCRIPT, ADDED IN REVIEW. The replacement statement written alongside this
    result was itself false — it claimed basin mass tends to 1 as `ΔP/D → ∞`,
    which holds only for a GLOBAL maximum, while hypothesis (i) asserts merely a
    local one. The stationary density `∝ e^{γP/D}` concentrates on global maxima
    as `D → 0`, so a local `Ψ*` loses its mass in exactly that limit. Refuting
    witness (numerically confirmed, not yet transcribed): three-state path
    `a–b–c` with `P = (1,0,2)`, where basin mass at `a` falls to 4.5e-5 by
    `ΔP/D = 10`. The two-state chain that refuted the original cannot see it —
    one well. The replacement is marked PROPOSED in M.4 with five items
    pre-registered, and must go through this same loop before it is anything.
    Recorded here because the failure is instructive: the batch that opened the
    over-claim category committed the second entry in it, one paragraph later.

    AND THE DIRECTION, as pre-registered before the result was known. This is the
    first finding that cuts against the manuscript rather than the transport.
    Ten times the term lost something the prose had; once now, the prose claimed
    something its own proof does not deliver. The appendix says so in the same
    voice it used the other ten times. That symmetry is the only reason the
    apparatus is worth anything. -/

/-! ## 19. Item 16 — a one-step kernel, and target (viii)

    RULING (peer, 2026-09-10): discrete time, (α). And the forced part: item
    15's signature gives only MARGINALS — `law t start B`. Part A cannot be
    stated against it. Positive Harris recurrence is a property of a transition
    kernel, and two kernels can share every marginal; "almost surely" lives on
    path space, which marginals do not determine. So the signature was too weak
    to host Part A at all.

    ITEM 16, declared representation choice: a one-step kernel `step`, with laws
    DERIVED from it by iteration rather than asserted. On a finite state space
    given by an explicit enumeration `univ`, with `Val := Nat` at scale 100 as in
    §§13–18. Invariance becomes a formula — `ρ ∘ step = ρ` — which is the first
    time `ρ_∞` has a definition in the record rather than a gloss.

    TARGET (viii), pre-registered by the peer as the compile-decidable test of
    whether item 16 is the right shape: `lawTwo` must come out DERIVED. If
    iterating the [[½,½],[½,½]] kernel reproduces the committed `lawTwo` at every
    `t ≥ 1` from either start, the file's counterexample-turned-confirmation was
    already a Markov chain that had not been told so. If not, `lawTwo` was never
    a chain and target (i) is void — to be reported as (i) refuted, not as a
    kernel problem. -/

open Classical in
/-- Item 16: laws by iteration of a kernel, over an explicit enumeration. -/
noncomputable def iterLaw {X : Type} (univ : List X) (step : X → (X → Prop) → Nat) :
    Nat → X → (X → Prop) → Nat
  | 0,     start, B => if B start then 100 else 0
  | t + 1, start, B =>
      (univ.map (fun x => iterLaw univ step t start (fun y => y = x) * step x B)).sum / 100

open Classical in
/-- The two-state kernel `[[½,½],[½,½]]`: from either state, each state with
    mass one half. -/
noncomputable def stepTwo : Bool → (Bool → Prop) → Nat :=
  fun _ B => (if B true then 50 else 0) + (if B false then 50 else 0)

/-- TARGET (viii). Iterating the kernel reproduces the committed `lawTwo` at
    every `t ≥ 1`, from either start, on every set. -/
theorem lawTwo_is_derived :
    ∀ t : Nat, ∀ start : Bool, ∀ B : Bool → Prop,
      iterLaw [true, false] stepTwo (t + 1) start B
        = lawTwo (fun _ => 0) () 1 1 (t + 1) start B := by
  intro t
  induction t with
  | zero =>
      intro start B
      cases start <;> simp [iterLaw, stepTwo, lawTwo]
  | succ n ih =>
      intro start B
      have h1 : ∀ x : Bool,
          iterLaw [true, false] stepTwo (n + 1) start (fun y => y = x) = 50 := by
        intro x
        rw [ih start (fun y => y = x)]
        cases x <;> simp [lawTwo]
      rw [iterLaw]
      simp only [List.map, List.sum_cons, List.sum_nil, h1]
      simp [stepTwo, lawTwo]
      omega

end RE

/-! Target (iv): the escape chain against UNAMENDED Part A (uniqueness only).
    Developed standalone and verified before being appended. -/
namespace RE4

def psum (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | M + 1 => psum f M + f M

theorem psum_zero_below (f : Nat → Nat) : ∀ M, (∀ n, n < M → f n = 0) → psum f M = 0 := by
  intro M; induction M with
  | zero => intro _; rfl
  | succ m ih =>
    intro h; simp only [psum]
    rw [ih (fun n hn => h n (by omega)), h m (by omega)]

theorem psum_single (f : Nat → Nat) (n₀ : Nat) (h₀ : f n₀ = 100)
    (h : ∀ n, n ≠ n₀ → f n = 0) : ∀ M, n₀ < M → psum f M = 100 := by
  intro M; induction M with
  | zero => intro hM; omega
  | succ m ih =>
    intro hM; simp only [psum]
    by_cases hm : m = n₀
    · subst hm; rw [psum_zero_below f m (fun n hn => h n (by omega)), h₀]
    · rw [ih (by omega), h m hm]

/-- ℕ-valued probability measure at scale 100, countably additive in
    stabilization form (a bounded monotone ℕ sequence stabilizes). -/
structure ProbM {X : Type} (μ : (X → Prop) → Nat) : Prop where
  total : μ (fun _ => True) = 100
  add : ∀ A B : X → Prop, (∀ x, ¬ (A x ∧ B x)) → μ (fun x => A x ∨ B x) = μ A + μ B
  countable : ∀ F : Nat → X → Prop, (∀ i j x, i ≠ j → F i x → ¬ F j x) →
      ∃ N, ∀ M, N ≤ M → psum (fun n => μ (F n)) M = μ (fun x => ∃ n, F n x)

def Invariant {X : Type} (T : X → X) (μ : (X → Prop) → Nat) : Prop :=
  ∀ B : X → Prop, μ (fun x => B (T x)) = μ B

theorem ext' {X : Type} {μ : (X → Prop) → Nat} (A B : X → Prop)
    (h : ∀ x, A x ↔ B x) : μ A = μ B := by
  have : A = B := funext (fun x => propext (h x)); rw [this]

theorem ProbM.empty' {X : Type} {μ : (X → Prop) → Nat} (hP : ProbM μ) :
    μ (fun _ : X => False) = 0 := by
  have h := hP.add (fun _ => False) (fun _ => False) (fun _ h => h.1)
  rw [ext' (μ := μ) (fun (_ : X) => False ∨ False) (fun _ => False)
        (fun _ => ⟨fun h => h.elim id id, Or.inl⟩)] at h
  omega

/-- The escape dynamics: `a = none` absorbing, `some n ↦ some (n+1)`. -/
def Tesc : Option Nat → Option Nat
  | none => none
  | some n => some (n + 1)

def iterT {X : Type} (T : X → X) : Nat → X → X
  | 0, x => x
  | n + 1, x => iterT T n (T x)

theorem iter_esc : ∀ s m, iterT Tesc s (some m) = some (m + s) := by
  intro s; induction s with
  | zero => intro m; rfl
  | succ k ih => intro m; simp only [iterT, Tesc]; rw [ih (m + 1)]; congr 1; omega

open Classical in
noncomputable def deltaA : (Option Nat → Prop) → Nat := fun B => if B none then 100 else 0

open Classical in
theorem deltaA_prob : ProbM deltaA where
  total := by simp [deltaA]
  add := by
    intro A B hdis; unfold deltaA
    by_cases ha : A none
    · by_cases hb : B none
      · exact absurd ⟨ha, hb⟩ (hdis none)
      · simp [ha, hb]
    · by_cases hb : B none <;> simp [ha, hb]
  countable := by
    intro F hdis
    by_cases hex : ∃ n, F n none
    · obtain ⟨n₀, hn₀⟩ := hex
      refine ⟨n₀ + 1, fun M hM => ?_⟩
      have rhs : deltaA (fun x => ∃ n, F n x) = 100 := by
        unfold deltaA; rw [if_pos ⟨n₀, hn₀⟩]
      rw [rhs]
      apply psum_single _ n₀
      · unfold deltaA; rw [if_pos hn₀]
      · intro n hne; unfold deltaA
        rw [if_neg (fun hn => hdis n n₀ none hne hn hn₀)]
      · omega
    · refine ⟨0, fun M _ => ?_⟩
      have rhs : deltaA (fun x => ∃ n, F n x) = 0 := by unfold deltaA; rw [if_neg hex]
      rw [rhs]
      exact psum_zero_below _ M (fun n _ => by
        unfold deltaA; rw [if_neg (fun hn => hex ⟨n, hn⟩)])

theorem deltaA_inv : Invariant Tesc deltaA := by intro B; rfl

section uniq
variable (μ : (Option Nat → Prop) → Nat) (hP : ProbM μ) (hI : Invariant Tesc μ)
include hP hI

theorem sing_zero : ∀ n, μ (fun x => x = some n) = 0 := by
  intro n; induction n with
  | zero =>
    rw [← hI (fun x => x = some 0)]
    rw [ext' (μ := μ) (fun x => Tesc x = some 0) (fun _ => False)
          (by intro x; cases x <;> simp [Tesc])]
    exact hP.empty'
  | succ m ih =>
    rw [← hI (fun x => x = some (m + 1))]
    rw [ext' (μ := μ) (fun x => Tesc x = some (m + 1)) (fun x => x = some m)
          (by intro x; cases x <;> simp [Tesc])]
    exact ih

theorem npart_zero : μ (fun x => ∃ n, x = some n) = 0 := by
  obtain ⟨N, hN⟩ := hP.countable (fun n x => x = some n)
    (by intro i j x hij hi hj; rw [hi] at hj; exact hij (Option.some.inj hj))
  rw [← hN N (Nat.le_refl N)]
  exact psum_zero_below _ N (fun n _ => sing_zero μ hP hI n)

theorem none_full : μ (fun x => x = none) = 100 := by
  have h := hP.add (fun x => x = none) (fun x => ∃ n, x = some n)
    (by intro x ⟨h1, n, h2⟩; rw [h1] at h2; cases h2)
  rw [ext' (μ := μ) (fun x => x = none ∨ ∃ n, x = some n) (fun _ => True)
        (by intro x; cases x <;> simp)] at h
  rw [hP.total, npart_zero μ hP hI] at h; omega

open Classical in
/-- Uniqueness: the ONLY invariant probability measure is `δ_a`. -/
theorem unique_escape : μ = deltaA := by
  funext B
  have hsplit := hP.add (fun x => B x ∧ x = none) (fun x => B x ∧ ∃ n, x = some n)
    (by intro x ⟨⟨_, h1⟩, _, n, h2⟩; rw [h1] at h2; cases h2)
  rw [ext' (μ := μ) (fun x => (B x ∧ x = none) ∨ (B x ∧ ∃ n, x = some n)) B
        (by intro x; cases x <;> simp)] at hsplit
  have hN := hP.add (fun x => B x ∧ ∃ n, x = some n) (fun x => ¬ B x ∧ ∃ n, x = some n)
    (by intro x ⟨⟨h1, _⟩, h2, _⟩; exact h2 h1)
  rw [ext' (μ := μ) (fun x => (B x ∧ ∃ n, x = some n) ∨ (¬ B x ∧ ∃ n, x = some n))
        (fun x => ∃ n, x = some n) (by intro x; by_cases hb : B x <;> simp [hb])] at hN
  rw [npart_zero μ hP hI] at hN
  have hBN : μ (fun x => B x ∧ ∃ n, x = some n) = 0 := by omega
  rw [hBN] at hsplit
  unfold deltaA
  by_cases hb : B none
  · rw [if_pos hb]
    rw [ext' (μ := μ) (fun x => B x ∧ x = none) (fun x => x = none)
          (by intro x; constructor
              · exact fun h => h.2
              · intro h; subst h; exact ⟨hb, rfl⟩)] at hsplit
    rw [none_full μ hP hI] at hsplit; omega
  · rw [if_neg hb]
    rw [ext' (μ := μ) (fun x => B x ∧ x = none) (fun _ => False)
          (by intro x; constructor
              · intro ⟨h1, h2⟩; subst h2; exact hb h1
              · intro h; exact h.elim)] at hsplit
    rw [hP.empty'] at hsplit; omega
end uniq

/-- The escape orbit never meets `a`, stated for ANY `Decidable` instance on the
    condition. The transcribed statement's `if` carries the classical instance
    (its condition was an arbitrary `basin` predicate), while `… = none` also has
    a genuine `DecidableEq` instance; the two print identically and do not
    unify syntactically. `if_neg` is instance-polymorphic, which is the fix. -/
theorem psum_escape_zero (d : ∀ s, Decidable (iterT Tesc s (some 1) = none)) :
    ∀ t, psum (fun s => @ite Nat (iterT Tesc s (some 1) = none) (d s) 100 0) t = 0 :=
  fun t => psum_zero_below _ t (fun n _ => by rw [if_neg (by rw [iter_esc]; simp)])

open Classical in
/-- UNAMENDED Part A (uniqueness only), specialized to deterministic dynamics,
    in the record's Cesàro-marginal form. For deterministic dynamics the path is
    a single trajectory, so the a.s. time average and the Cesàro average of the
    point-mass marginals coincide: refuting this refutes both forms. Stubs carried
    exactly as in `Theorem7_faithful`. -/
def UnamendedA_det : Prop :=
  ∀ (X Th : Type) (T : X → X) (ρ : (X → Prop) → Nat)
    (P : X → Th → Nat) (above : Th → Prop) (θ : Th)
    (nondegLocalMax : (X → Nat) → Th → X → Prop) (carrierClass : X → Prop)
    (basin : X → (X → Prop)),
    above θ → ProbM ρ → Invariant T ρ → (∀ μ, ProbM μ → Invariant T μ → μ = ρ) →
    ∀ Ψstar : X, nondegLocalMax (fun x => P x θ) θ Ψstar → carrierClass Ψstar →
    ∀ start : X, ∀ ε : Nat, 0 < ε → ∃ T0 : Nat, ∀ t : Nat, T0 < t →
      t * ρ (basin Ψstar)
        < psum (fun s => if basin Ψstar (iterT T s start) then 100 else 0) t + t * ε ∧
      psum (fun s => if basin Ψstar (iterT T s start) then 100 else 0) t
        < t * ρ (basin Ψstar) + t * ε

open Classical in
/-- TARGET (iv): unamended Part A is false. `δ_a` is the unique invariant
    probability measure, PROVED (not assumed); `basin(a) = {a}` is the genuine
    basin of attraction; from `Ψ₀ = some 1` the orbit never meets `a`. -/
theorem unamendedA_refuted : ¬ UnamendedA_det := by
  intro h
  obtain ⟨T0, hT⟩ := h (Option Nat) Unit Tesc deltaA (fun _ _ => 0) (fun _ => True) ()
    (fun _ _ _ => True) (fun _ => True) (fun g x => x = g)
    trivial deltaA_prob deltaA_inv (fun μ hP hI => unique_escape μ hP hI)
    none trivial trivial (some 1) 1 (by decide)
  have h1 := (hT (T0 + 1) (by omega)).1
  have hρ : deltaA (fun x => x = none) = 100 := by unfold deltaA; simp
  rw [hρ] at h1
  first
    | rw [psum_escape_zero (fun s => Classical.propDecidable _) (T0 + 1)] at h1
    | simp only [psum_escape_zero] at h1
  omega

end RE4

/-! Target (v): a point-mass reference measure against UNAMENDED Part C.
    Developed standalone and verified before being appended. -/
namespace RE5

inductive Tri where
  | a | b | c
  deriving DecidableEq

def triList : List Tri := [Tri.a, Tri.b, Tri.c]

/-- The three-state path `a – b – c`, `P = (1, 0, 2)`. -/
def Pt : Tri → Nat
  | .a => 1
  | .b => 0
  | .c => 2

open Classical in
noncomputable def numR {X : Type} (univ : List X) (w : X → Nat) (E : Nat → X → Nat)
    (k : Nat) (B : X → Prop) : Nat :=
  (univ.map (fun x => if B x then w x * E k x else 0)).sum

def denR {X : Type} (univ : List X) (w : X → Nat) (E : Nat → X → Nat) (k : Nat) : Nat :=
  (univ.map (fun x => w x * E k x)).sum

/-- UNAMENDED Part C (before A3 and A4), on a finite state space with an explicit
    enumeration. Declared representation choices: the reference measure is a
    weight `w`; the Gibbs weight `e^{γP/D}` is an ARBITRARY positive `E k x`
    (the refutation below holds for every `E`, hence for the Gibbs one); small
    noise is reparametrized as `k → ∞`; probabilities at scale 100. -/
def UnamendedC : Prop :=
  ∀ (X : Type) (univ : List X) (P : X → Nat) (w : X → Nat) (E : Nat → X → Nat)
    (G : X → Prop) (nondeg : X → Prop) (localMax : X → Prop) (basin : X → (X → Prop)),
    (∀ k x, 0 < E k x) →
    (∀ x, G x ↔ ∀ y, P y ≤ P x) →
    (∀ g, G g → nondeg g) →
    ∀ ε : Nat, 0 < ε → ε < 100 → ∃ k0 : Nat, ∀ k : Nat, k0 < k →
      (100 - ε) * denR univ w E k < 100 * numR univ w E k (fun x => ∃ g, G g ∧ basin g x) ∧
      ∀ ψ, localMax ψ → ¬ G ψ → 100 * numR univ w E k (basin ψ) < ε * denR univ w E k

/-- The reference measure: a point mass at the NON-global local maximum `a`. -/
def wDelta : Tri → Nat := fun x => if x = Tri.a then 1 else 0

/-- Global maxima of `Pt`, defined as the statement requires. -/
def Gt : Tri → Prop := fun x => ∀ y, Pt y ≤ Pt x

theorem a_not_global : ¬ Gt Tri.a := fun h => by have := h Tri.c; simp [Pt] at this

/-- Clause 1 fails at the witness for EVERY weight `E` — so in particular for
    `e^{γP/D}`, at every `γ` and every `D`. The Gibbs factor cancels against a
    point mass, which is why no real exponential is needed. -/
theorem clause1_fails (E : Nat → Tri → Nat) (k ε : Nat) :
    ¬ ((100 - ε) * denR triList wDelta E k
        < 100 * numR triList wDelta E k (fun x => ∃ g, Gt g ∧ x = g)) := by
  have ha : ¬ (∃ g, Gt g ∧ Tri.a = g) := fun ⟨g, hg, he⟩ => by subst he; exact a_not_global hg
  have hnum : numR triList wDelta E k (fun x => ∃ g, Gt g ∧ x = g) = 0 := by
    simp [numR, triList, wDelta, ha]
  rw [hnum]; simp

/-- TARGET (v): unamended Part C is false. -/
theorem unamendedC_refuted : ¬ UnamendedC := by
  intro h
  obtain ⟨k0, hk⟩ := h Tri triList Pt wDelta (fun _ _ => 1) Gt (fun _ => True)
    (fun x => x = Tri.a ∨ x = Tri.c) (fun g x => x = g)
    (fun _ _ => Nat.one_pos) (fun _ => Iff.rfl) (fun _ _ => trivial)
    1 (by decide) (by decide)
  exact clause1_fails (fun _ _ => 1) (k0 + 1) 1 (hk (k0 + 1) (by omega)).1

/-- Target (vi), concretely: at the witness the basins ARE disjoint — so the
    refutation does not lean on overlapping basins. -/
theorem witness_basins_disjoint : ∀ x, ¬ (x = Tri.a ∧ x = Tri.c) := by
  intro x ⟨h1, h2⟩; rw [h1] at h2; cases h2

end RE5

/-! Targets (ii) and (iii): confirmations of AMENDED Part C on the three-state
    path. Declared representation: Gibbs weight `b^{P x}` with `b = e^{γ/D}`, so
    small noise ↔ large `b`; reference measure = counting measure (A3(a)); finite
    space (A3(b), A3(c)). Probabilities at scale 100: a mass `m = num/den` is
    within `ε/100` of a target `q/100` iff `|100·num − q·den| < ε·den`. -/
namespace REC

/-! (ii) `P = (1, 0, 2)`: weights `a ↦ b`, `b ↦ 1`, `c ↦ b²`; `den = b + 1 + b²`.
    `G = {c}`; `a` is a non-global local maximum. -/

/-- Second clause: the non-global local basin `{a}` empties — `100·b < ε·den`. -/
theorem ii_local_basin_empties : ∀ ε : Nat, 0 < ε → ∃ b0 : Nat, ∀ b : Nat, b0 < b →
    100 * b < ε * (b + 1 + b * b) := by
  intro ε hε
  refine ⟨100, fun b hb => ?_⟩
  have h1 : 100 * b < b * b := Nat.mul_lt_mul_of_pos_right hb (by omega)
  have h2 : 1 * (b + 1 + b * b) ≤ ε * (b + 1 + b * b) :=
    Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  omega

/-- First clause: the global basin `{c}` fills — `100·(den − b²) < ε·den`. -/
theorem ii_global_basin_fills : ∀ ε : Nat, 0 < ε → ∃ b0 : Nat, ∀ b : Nat, b0 < b →
    100 * (b + 1) < ε * (b + 1 + b * b) := by
  intro ε hε
  refine ⟨200, fun b hb => ?_⟩
  have h1 : 200 * b < b * b := Nat.mul_lt_mul_of_pos_right hb (by omega)
  have h2 : 1 * (b + 1 + b * b) ≤ ε * (b + 1 + b * b) :=
    Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  omega

/-! (iii) `P = (2, 0, 2)`: weights `a ↦ b²`, `b ↦ 1`, `c ↦ b²`; `den = 2b² + 1`.
    `G = {a, c}` — TWO global maxima at equal height. -/

/-- Each global basin tends to ONE HALF, not to one: `|100·b² − 50·den| < ε·den`.
    A statement written for "the global maximum" would claim one here, and fail. -/
theorem iii_each_basin_half : ∀ ε : Nat, 0 < ε → ∃ b0 : Nat, ∀ b : Nat, b0 < b →
    50 * (2 * (b * b) + 1) < 100 * (b * b) + ε * (2 * (b * b) + 1) ∧
    100 * (b * b) < 50 * (2 * (b * b) + 1) + ε * (2 * (b * b) + 1) := by
  intro ε hε
  refine ⟨10, fun b hb => ?_⟩
  have h1 : 10 * b < b * b := Nat.mul_lt_mul_of_pos_right hb (by omega)
  have h2 : 1 * (2 * (b * b) + 1) ≤ ε * (2 * (b * b) + 1) :=
    Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  constructor <;> omega

/-- The UNION of the global basins tends to one: `100·(den − 2b²) < ε·den`. -/
theorem iii_union_one : ∀ ε : Nat, 0 < ε → ∃ b0 : Nat, ∀ b : Nat, b0 < b →
    100 * (2 * (b * b) + 1) < 100 * (2 * (b * b)) + ε * (2 * (b * b) + 1) := by
  intro ε hε
  refine ⟨10, fun b hb => ?_⟩
  have h1 : 10 * b < b * b := Nat.mul_lt_mul_of_pos_right hb (by omega)
  have h2 : 1 * (2 * (b * b) + 1) ≤ ε * (2 * (b * b) + 1) :=
    Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  omega

/-- And the singular reading is FALSE at (iii): no single global basin tends to
    one. Mass exactly `b² / (2b² + 1) < ½` for every `b`. -/
theorem iii_singular_fails : ∀ b : Nat, 2 * (100 * (b * b)) < 100 * (2 * (b * b) + 1) := by
  intro b; omega

end REC

/-! Target (i): Theorem 14's two-state chain as a MODEL of amended Parts A and B.
    The chain is now derived from a kernel (target (viii)), so its hypotheses are
    statements about `stepTwo`, not about a bare family of marginals. -/
namespace REi
open RE RE4

open Classical in
/-- `ρ_∞` for the two-state chain: mass one half on each state. -/
noncomputable def rhoTwo : (Bool → Prop) → Nat :=
  fun B => (if B true then 50 else 0) + (if B false then 50 else 0)

/-- Invariance as a FORMULA under item 16: one kernel step from `ρ` returns `ρ`. -/
theorem rhoTwo_invariant : ∀ B : Bool → Prop,
    ([true, false].map (fun x => rhoTwo (fun y => y = x) * stepTwo x B)).sum / 100
      = rhoTwo B := by
  intro B; simp [rhoTwo, stepTwo]; omega

/-- Strict positivity of the kernel. On a finite state space this gives positive
    Harris recurrence — the standard fact, DECLARED here and not re-derived,
    since Harris recurrence itself is not formalized in this file. -/
theorem stepTwo_positive : ∀ x y : Bool, 0 < stepTwo x (fun z => z = y) := by
  intro x y; cases y <;> simp [stepTwo]

/-- PART B CONFIRMED: from either start, the marginal law of `{true}` equals
    `ρ_∞({true})` at every `t ≥ 1`. -/
theorem partB_two : ∀ start : Bool, ∀ t : Nat,
    iterLaw [true, false] stepTwo (t + 1) start (fun y => y = true) = rhoTwo (fun y => y = true) := by
  intro start t
  rw [lawTwo_is_derived]
  simp [lawTwo, rhoTwo]

theorem cesaro_two (start : Bool) : ∀ t : Nat,
    psum (fun s => iterLaw [true, false] stepTwo s start (fun y => y = true)) (t + 1)
      = iterLaw [true, false] stepTwo 0 start (fun y => y = true) + 50 * t := by
  intro t; induction t with
  | zero => simp [psum]
  | succ n ih =>
    have hf : iterLaw [true, false] stepTwo (n + 1) start (fun y => y = true) = 50 := by
      rw [partB_two start n]; simp [rhoTwo]
    show psum _ (n + 1) + iterLaw [true, false] stepTwo (n + 1) start (fun y => y = true) = _
    rw [ih, hf]; omega

/-- PART A CONFIRMED, in the Cesàro-marginal form the record holds (A9): the
    average of the marginals of `{true}` converges to `ρ_∞({true}) = ½`, from
    either start. -/
theorem partA_cesaro_two (start : Bool) : ∀ ε : Nat, 0 < ε → ∃ T0 : Nat, ∀ t : Nat, T0 < t →
    t * 50 < psum (fun s => iterLaw [true, false] stepTwo s start (fun y => y = true)) t + t * ε ∧
    psum (fun s => iterLaw [true, false] stepTwo s start (fun y => y = true)) t < t * 50 + t * ε := by
  intro ε hε
  refine ⟨100, fun t ht => ?_⟩
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 1 := ⟨t - 1, by omega⟩
  rw [cesaro_two start m]
  have hc : iterLaw [true, false] stepTwo 0 start (fun y => y = true) ≤ 100 := by
    cases start <;> simp [iterLaw]
  have hte : 1 * (m + 1) ≤ ε * (m + 1) := Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  have hcomm : (m + 1) * ε = ε * (m + 1) := Nat.mul_comm _ _
  constructor <;> omega

end REi


/-! ## 20. Targets (i)–(viii): results

    Reported as target, expected, observed. Every theorem named below compiles
    and is audited free of `sorryAx`.

    (viii) lawTwo derived from a kernel | expected: derivable | OBSERVED: derivable
           (`RE.lawTwo_is_derived`). Target (i) is not void.
    (iv)   escape chain vs UNAMENDED A  | expected: refuted   | OBSERVED: refuted
           (`RE4.unamendedA_refuted`). `δ_a` is PROVED the unique invariant
           probability (`RE4.unique_escape`), not assumed. A1 was forced.
    (v)    point-mass λ vs UNAMENDED C  | expected: refuted   | OBSERVED: refuted
           (`RE5.unamendedC_refuted`), for EVERY Gibbs weight (`clause1_fails`):
           the exponential cancels against a point mass. A3 was forced.
    (i)    two-state chain, A and B     | expected: model     | OBSERVED: model
           Part B pointwise (`REi.partB_two`); Part A in the record's Cesàro form
           (`REi.partA_cesaro_two`); invariance as a formula (`rhoTwo_invariant`).
    (ii)   P = (1,0,2)                  | expected: local → 0 | OBSERVED: local → 0,
           global → 1 (`REC.ii_local_basin_empties`, `ii_global_basin_fills`).
    (iii)  P = (2,0,2)                  | expected: each ½, ∪ → 1 | OBSERVED: each ½,
           ∪ → 1, and the SINGULAR reading fails at every b (`iii_singular_fails`).
    (vi)   basin disjointness           | expected: provable or stub | OBSERVED:
           STUB. `basin` is a declared parameter in every transcription here, so
           disjointness is not derivable and goes into Part C as an explicit
           hypothesis. It holds concretely at the witnesses
           (`RE5.witness_basins_disjoint`), so no refutation leans on overlap.
    (vii)  carrier of 𝒳                 | expected: choose and log | LOGGED: 𝒳 stays
           an opaque `Type` in the general transcriptions. The display's "volume"
           and "∇P" require ℝⁿ or a manifold, which this Mathlib-free file cannot
           host. Every refutation and confirmation lives on a FINITE or COUNTABLE
           state space, where volume is counting measure and the gradient is
           replaced by the discrete structure.

    DECLARED REPRESENTATION CHOICES, each a cost rather than a hidden hypothesis:
      · (iv) uses DETERMINISTIC dynamics on `Option Nat`. `iterLaw` needs a finite
        enumeration and cannot host the escape chain, and no finite chain can
        serve as that witness: on a finite space a unique invariant probability
        forces one recurrent class that every start reaches. For deterministic
        dynamics the a.s. time average and the Cesàro average coincide, so
        refuting one refutes both.
      · Measures are ℕ-valued at scale 100, countably additive in stabilization
        form — the Theorem 14 precedent.
      · (ii)/(iii) reparametrize small noise as large `b = e^{γ/D}`, with Gibbs
        weight `b^{P x}` and counting reference measure.
      · Harris recurrence for (i) is not formalized. What is proved is the
        kernel's strict positivity (`stepTwo_positive`); that this gives positive
        Harris recurrence on a finite space is the standard fact, declared.

    THE GAP, stated rather than left out. The AMENDED Parts A–C are not
    transcribed as general Lean statements. The record holds refutations of the
    unamended versions (in the specialization each refutation needs) and
    confirmations on concrete witnesses. The general Laplace statement of Part C
    in particular is not machine-checked: it needs ℝⁿ.

    PRIORS, SCORED. The reviewer's: A3 most likely to come back incomplete, (b)
    the likeliest omission. A3 came back complete — all of (a)(b)(c) present and
    (v) confirms the point-mass case (a) is aimed at. The prior did not land.
    Mine, never stated in advance and so not scored.

    AND ONE FINDING THE PRE-REGISTRATION DID NOT ANTICIPATE: two superficially
    identical `if`-expressions failed to unify in (iv) because one carried the
    classical `Decidable` instance and the other a genuine `DecidableEq`. They
    print identically. That is the register-boundary failure mode one level
    down, inside the formal register itself — same surface text, different
    objects — and it was caught by the compiler, not by reading. -/

/-! ## 21. General Parts A and B on finite spaces (merge condition 1)

    EXACTNESS, a declared hypothesis. `iterLaw` composes by `.sum / 100`, which
    is ℕ division: exact for `stepTwo` (5000 / 100) and TRUNCATING for a kernel
    whose sums 100 does not divide. A general statement quantifying over every
    `step` would quantify over a truncating object — the wrong one. So kernels
    are required to be exact at scale 100. This is STRONGER THAN IT LOOKS: a law
    confined to the 1/100 grid that keeps approaching `ρ` must eventually hit it,
    so exact positive kernels are close to those that reach stationarity in
    finitely many steps. It excludes no witness this file uses; `stepTwo` is
    exact (`stepTwo_exact`).

    HOW THE GENERAL STATEMENTS COMPARE TO THE DISPLAY — weaker in three ways,
    stronger in one, and the file says which:
      · weaker: finite state space; exact kernel; STRICT POSITIVITY in place of
        positive Harris recurrence — strictly stronger than Harris, since
        irreducible aperiodic chains may have zero entries, so these hypotheses
        admit fewer chains than the display's.
      · stronger: the conclusions hold for EVERY set, not only basins, so the
        stubs `above`, nondegenerate-local-maximum and carrier-class drop out and
        `basin` is universally quantified. A proof of these would imply the
        display's conclusion for any `Ψ*`, on the class of chains they cover. -/
namespace REgen
open RE RE4 REi

open Classical in
/-- The kernel is exact at scale 100 along every iterate. -/
def ExactKernel {X : Type} (univ : List X) (step : X → (X → Prop) → Nat) : Prop :=
  ∀ (t : Nat) (start : X) (B : X → Prop),
    100 ∣ (univ.map (fun x => iterLaw univ step t start (fun y => y = x) * step x B)).sum

open Classical in
/-- UNAMENDED — FROZEN COPY. The hypotheses general Parts A and B were first
    stated against. Refuted in §22: no field makes `step` a kernel, so a
    positive, exact kernel with unequal row totals satisfies every field and
    never converges. Kept, not deleted, so the record shows the amendment of §23
    was forced. `positive` is the DECLARED stand-in for positive Harris
    recurrence, as in target (i). -/
structure FiniteChainU {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) : Prop where
  complete  : ∀ x, x ∈ univ
  nodup     : univ.Nodup
  exact     : ExactKernel univ step
  positive  : ∀ x y, 0 < step x (fun z => z = y)
  measure   : ∀ B, ρ B = (univ.map (fun x => if B x then ρ (fun y => y = x) else 0)).sum
  total     : ρ (fun _ => True) = 100
  invariant : ∀ B, (univ.map (fun x => ρ (fun y => y = x) * step x B)).sum / 100 = ρ B

/-- Part A's conclusion, in the Cesàro-marginal form the record holds (A9). -/
def PartA_concl {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) (start : X) (basin : X → Prop) : Prop :=
  ∀ ε : Nat, 0 < ε → ∃ T0 : Nat, ∀ t : Nat, T0 < t →
    t * ρ basin < psum (fun s => iterLaw univ step s start basin) t + t * ε ∧
    psum (fun s => iterLaw univ step s start basin) t < t * ρ basin + t * ε

/-- Part B's conclusion, pointwise. -/
def PartB_concl {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) (start : X) (basin : X → Prop) : Prop :=
  ∀ ε : Nat, 0 < ε → ∃ T0 : Nat, ∀ t : Nat, T0 < t →
    iterLaw univ step t start basin < ρ basin + ε ∧
    ρ basin < iterLaw univ step t start basin + ε

/-! The general statements that first stood here — `general_partA` and
    `general_partB` over `FiniteChainU` — were FALSE as stated and are removed,
    not left `sorry`'d: a `sorry` on a false statement breaks the header's
    contract. Their refutation is §22; their restatement, against the amended
    hypotheses, is §23. -/

/-! ### The instance check the reviewer asked for

    The two-state chain satisfies every `FiniteChainU` hypothesis, and its PROVED
    theorems are instances of the general conclusions. These proofs use
    `partA_cesaro_two` and `partB_two`, NOT the sorry'd general theorems, so they
    check that the general statements have the right shape without borrowing
    their unproved content. -/

theorem stepTwo_exact : ExactKernel [true, false] stepTwo := by
  intro t start B
  simp only [List.map, List.sum_cons, List.sum_nil]
  cases t with
  | zero => cases start <;> simp [iterLaw, stepTwo] <;> omega
  | succ m =>
    rw [lawTwo_is_derived m start (fun y => y = true),
        lawTwo_is_derived m start (fun y => y = false)]
    simp [lawTwo, stepTwo] <;> omega

theorem two_state_is_finite_chainU : FiniteChainU [true, false] stepTwo rhoTwo where
  complete  := by intro x; cases x <;> simp
  nodup     := by decide
  exact     := stepTwo_exact
  positive  := stepTwo_positive
  measure   := by intro B; simp [rhoTwo]
  total     := by simp [rhoTwo]
  invariant := rhoTwo_invariant

theorem partA_instance (start : Bool) :
    PartA_concl [true, false] stepTwo rhoTwo start (fun y => y = true) := by
  have h50 : rhoTwo (fun y => y = true) = 50 := by simp [rhoTwo]
  unfold PartA_concl; rw [h50]; exact partA_cesaro_two start

theorem partB_instance (start : Bool) :
    PartB_concl [true, false] stepTwo rhoTwo start (fun y => y = true) := by
  intro ε hε
  refine ⟨0, fun t ht => ?_⟩
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 1 := ⟨t - 1, by omega⟩
  rw [partB_two start m]; constructor <;> omega

/-! ### Part C has no Lean marker, and that is stated here rather than left
    implicit. A general term would need ℝⁿ — volume, gradient, the Laplace
    integral — which this Mathlib-free file cannot host. The record holds Part
    C's refutation-of-predecessor (target (v)) and its finite confirmations
    ((ii), (iii)) only. The manuscript's "not machine-checked" sentence at Part C
    is its marker. -/

end REgen

/-! ## 22. The unamended general statements are false (refutation by the peer)

    Supplied by the peer reviewer against 247a19a, verified here before being
    appended, and adapted only by naming the frozen structure `FiniteChainU`.
    The kernel below is positive and exact, and its rows total 50 and 150 — so
    it is not a kernel. `FiniteChainU` has no field that says otherwise. -/
namespace REref
open Classical
open REgen

/-- A positive, exact kernel whose rows have different totals: the `false` row
    is (25, 25) — total 50 — and the `true` row is (75, 75) — total 150. -/
noncomputable def stepBad : Bool → (Bool → Prop) → Nat :=
  fun x B => (if x then 75 else 25) * ((if B true then 1 else 0) + (if B false then 1 else 0))

/-- The invariant measure (50, 50): it averages the two row totals to 100. -/
noncomputable def rhoBad : (Bool → Prop) → Nat :=
  fun B => (if B true then 50 else 0) + (if B false then 50 else 0)

theorem lawBad_false : ∀ n : Nat, ∀ b : Bool,
    RE.iterLaw [true, false] stepBad (n + 1) false (fun y => y = b) = 25 := by
  intro n
  induction n with
  | zero => intro b; cases b <;> simp [RE.iterLaw, stepBad]
  | succ n ih =>
    intro b
    rw [RE.iterLaw]
    simp only [List.map, List.sum_cons, List.sum_nil]
    rw [ih true, ih false]
    cases b <;> simp [stepBad]

theorem lawBad_true : ∀ n : Nat, ∀ b : Bool,
    RE.iterLaw [true, false] stepBad (n + 1) true (fun y => y = b) = 75 := by
  intro n
  induction n with
  | zero => intro b; cases b <;> simp [RE.iterLaw, stepBad]
  | succ n ih =>
    intro b
    rw [RE.iterLaw]
    simp only [List.map, List.sum_cons, List.sum_nil]
    rw [ih true, ih false]
    cases b <;> simp [stepBad]

theorem stepBad_exact : ExactKernel [true, false] stepBad := by
  intro t start B
  simp only [List.map, List.sum_cons, List.sum_nil, Nat.add_zero]
  cases t with
  | zero =>
    cases start <;> simp [RE.iterLaw, stepBad] <;>
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
      first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)
  | succ n =>
    cases start
    · rw [lawBad_false, lawBad_false]; simp [stepBad]
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
        first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)
    · rw [lawBad_true, lawBad_true]; simp [stepBad]
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
        first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)

theorem bad_is_finite_chain : FiniteChainU [true, false] stepBad rhoBad := by
  refine ⟨?_, ?_, stepBad_exact, ?_, ?_, ?_, ?_⟩
  · intro x; cases x <;> simp
  · simp
  · intro x y; cases x <;> cases y <;> simp [stepBad]
  · intro B; simp [rhoBad]
  · simp [rhoBad]
  · intro B; simp [stepBad, rhoBad]
    by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2]

/-- Part B fails from `start = false` on the basin `{false}`: the law sits at 25
    for every `t ≥ 1` while `ρ` gives 50. -/
theorem general_partB_refuted :
    ¬ (∀ (start : Bool) (basin : Bool → Prop),
        PartB_concl [true, false] stepBad rhoBad start basin) := by
  intro h
  obtain ⟨T0, hT⟩ := h false (fun y => y = false) 1 (by omega)
  have := (hT (T0 + 1) (by omega)).2
  rw [lawBad_false] at this
  simp [rhoBad] at this

theorem psumBad : ∀ n : Nat,
    RE4.psum (fun s => RE.iterLaw [true, false] stepBad s false (fun y => y = false)) (n + 1)
      = 25 * n + 100 := by
  intro n
  induction n with
  | zero => simp [RE4.psum, RE.iterLaw]
  | succ n ih =>
    show RE4.psum _ (n + 1) + _ = _
    rw [ih]; dsimp only; rw [lawBad_false]; omega

/-- Part A (Cesàro form) fails the same way: the running sum is `25t + 75`,
    against `50t` demanded. -/
theorem general_partA_refuted :
    ¬ (∀ (start : Bool) (basin : Bool → Prop),
        PartA_concl [true, false] stepBad rhoBad start basin) := by
  intro h
  obtain ⟨T0, hT⟩ := h false (fun y => y = false) 1 (by omega)
  have := (hT (T0 + 4) (by omega)).1
  have e := psumBad (T0 + 3)
  simp only [show T0 + 3 + 1 = T0 + 4 from rfl] at e
  rw [e] at this
  simp [rhoBad] at this
  omega

/-- The unamended GENERAL Part A, as it stood `sorry`'d at 247a19a, is false. -/
theorem unamended_general_partA_false :
    ¬ (∀ (X : Type) (univ : List X) (step : X → (X → Prop) → Nat) (ρ : (X → Prop) → Nat),
        FiniteChainU univ step ρ → ∀ start basin, PartA_concl univ step ρ start basin) :=
  fun h => general_partA_refuted (h Bool _ _ _ bad_is_finite_chain)

/-- The unamended GENERAL Part B, as it stood `sorry`'d at 247a19a, is false. -/
theorem unamended_general_partB_false :
    ¬ (∀ (X : Type) (univ : List X) (step : X → (X → Prop) → Nat) (ρ : (X → Prop) → Nat),
        FiniteChainU univ step ρ → ∀ start basin, PartB_concl univ step ρ start basin) :=
  fun h => general_partB_refuted (h Bool _ _ _ bad_is_finite_chain)

end REref

/-! ## 22.2 Stochastic alone is not enough (second refutation, by the peer)

    The §22 witness is additive, so §22 forced `stochastic` and nothing else. The
    argument that `additive` is needed as well — `stochastic` constrains
    `step x univ` but not `Σ_y step x {y}` — was right, and the peer turned it
    into a witness against 9872874: the §22 kernel with `step x univ` corrected to
    100. It is stochastic, positive and exact, `ρ = (50, 50)` is invariant, and
    yet its singleton laws still sit at 25 and 75. Supplied by the peer, verified
    here verbatim against the 9872874 blob before being appended, unchanged except
    for docstrings. -/
namespace REref2
open Classical
open REgen

/-- The §22 kernel with `step x univ` corrected to 100: STOCHASTIC, but not
    additive — the `false` row's singletons sum to 50 and the `true` row's to
    150. -/
noncomputable def stepBad2 : Bool → (Bool → Prop) → Nat :=
  fun x B => if B true ∧ B false then 100
    else (if x then 75 else 25) * ((if B true then 1 else 0) + (if B false then 1 else 0))

theorem stepBad2_stochastic : ∀ x, stepBad2 x (fun _ => True) = 100 := by
  intro x; simp [stepBad2]

theorem stepBad2_not_additive :
    ¬ (∀ (x : Bool) (B : Bool → Prop),
        stepBad2 x B = ([true, false].map (fun y => if B y then stepBad2 x (fun z => z = y) else 0)).sum) := by
  intro h
  have := h false (fun _ => True)
  simp [stepBad2] at this

theorem law2_false : ∀ n : Nat, ∀ b : Bool,
    RE.iterLaw [true, false] stepBad2 (n + 1) false (fun y => y = b) = 25 := by
  intro n
  induction n with
  | zero => intro b; cases b <;> simp [RE.iterLaw, stepBad2]
  | succ n ih =>
    intro b
    rw [RE.iterLaw]
    simp only [List.map, List.sum_cons, List.sum_nil]
    rw [ih true, ih false]
    cases b <;> simp [stepBad2]

theorem law2_true : ∀ n : Nat, ∀ b : Bool,
    RE.iterLaw [true, false] stepBad2 (n + 1) true (fun y => y = b) = 75 := by
  intro n
  induction n with
  | zero => intro b; cases b <;> simp [RE.iterLaw, stepBad2]
  | succ n ih =>
    intro b
    rw [RE.iterLaw]
    simp only [List.map, List.sum_cons, List.sum_nil]
    rw [ih true, ih false]
    cases b <;> simp [stepBad2]

theorem stepBad2_exact : ExactKernel [true, false] stepBad2 := by
  intro t start B
  simp only [List.map, List.sum_cons, List.sum_nil, Nat.add_zero]
  cases t with
  | zero =>
    cases start <;> simp [RE.iterLaw, stepBad2] <;>
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
      first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)
  | succ n =>
    cases start
    · rw [law2_false, law2_false]; simp [stepBad2]
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
        first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)
    · rw [law2_true, law2_true]; simp [stepBad2]
      by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2] <;>
        first | decide | exact Nat.dvd_of_mod_eq_zero (by decide)

theorem bad2_is_finite_chainU : FiniteChainU [true, false] stepBad2 REref.rhoBad := by
  refine ⟨?_, ?_, stepBad2_exact, ?_, ?_, ?_, ?_⟩
  · intro x; cases x <;> simp
  · simp
  · intro x y; cases x <;> cases y <;> simp [stepBad2]
  · intro B; simp [REref.rhoBad]
  · simp [REref.rhoBad]
  · intro B; simp [stepBad2, REref.rhoBad]
    by_cases h1 : B true <;> by_cases h2 : B false <;> simp [h1, h2]

theorem partB_refuted2 :
    ¬ (∀ (start : Bool) (basin : Bool → Prop),
        PartB_concl [true, false] stepBad2 REref.rhoBad start basin) := by
  intro h
  obtain ⟨T0, hT⟩ := h false (fun y => y = false) 1 (by omega)
  have := (hT (T0 + 1) (by omega)).2
  rw [law2_false] at this
  simp [REref.rhoBad] at this

theorem psum2 : ∀ n : Nat,
    RE4.psum (fun s => RE.iterLaw [true, false] stepBad2 s false (fun y => y = false)) (n + 1)
      = 25 * n + 100 := by
  intro n
  induction n with
  | zero => simp [RE4.psum, RE.iterLaw]
  | succ n ih =>
    show RE4.psum _ (n + 1) + _ = _
    rw [ih]; dsimp only; rw [law2_false]; omega

theorem partA_refuted2 :
    ¬ (∀ (start : Bool) (basin : Bool → Prop),
        PartA_concl [true, false] stepBad2 REref.rhoBad start basin) := by
  intro h
  obtain ⟨T0, hT⟩ := h false (fun y => y = false) 1 (by omega)
  have := (hT (T0 + 4) (by omega)).1
  have e := psum2 (T0 + 3)
  simp only [show T0 + 3 + 1 = T0 + 4 from rfl] at e
  rw [e] at this
  simp [REref.rhoBad] at this
  omega

/-- `FiniteChainU` plus `stochastic` alone does NOT give Part B: `additive` is
    forced. -/
theorem stochastic_alone_insufficient_B :
    ¬ (∀ (X : Type) (univ : List X) (step : X → (X → Prop) → Nat) (ρ : (X → Prop) → Nat),
        FiniteChainU univ step ρ → (∀ x, step x (fun _ => True) = 100) →
        ∀ start basin, PartB_concl univ step ρ start basin) :=
  fun h => partB_refuted2 (h Bool _ _ _ bad2_is_finite_chainU stepBad2_stochastic)

/-- Same for Part A. -/
theorem stochastic_alone_insufficient_A :
    ¬ (∀ (X : Type) (univ : List X) (step : X → (X → Prop) → Nat) (ρ : (X → Prop) → Nat),
        FiniteChainU univ step ρ → (∀ x, step x (fun _ => True) = 100) →
        ∀ start basin, PartA_concl univ step ρ start basin) :=
  fun h => partA_refuted2 (h Bool _ _ _ bad2_is_finite_chainU stepBad2_stochastic)

end REref2

/-! ## 23. The amendment: the kernel is a kernel

    Two fields, both logged. `stochastic` is `total` stated for every row of
    `step`; `additive` is `measure` stated for every row. With both, `iterLaw`
    is a genuine Markov iteration and general A and B become the standard finite
    Doeblin statements — believed true, still `sorry`'d, and this time attacked
    before commit.

    THIS IS NOT A WEAKENING OF THE DISPLAY. The display's process is positive
    Harris recurrent, hence a Markov process, hence one whose kernel is
    stochastic and countably additive by definition. So these fields are not a
    fourth narrowing alongside finite space, exactness and strict positivity:
    they are the hypothesis the transcription dropped.

    BOTH FIELDS ARE FORCED, each by its own witness. §22's kernel FAILS
    `stochastic` (`stepBad_not_stochastic`) and satisfies `additive`
    (`stepBad_additive`), so it forces `stochastic`. §22.2's kernel is stochastic
    and FAILS `additive` (`stepBad2_not_additive`), and still refutes Parts A and
    B (`stochastic_alone_insufficient_A`, `_B`), so it forces `additive`. Each
    witness fails the amended structure at exactly its own field
    (`bad_not_amended`, `bad2_not_amended`) — two compile-decidable checks that
    the fix is aimed where it has to be. An earlier version of this paragraph
    said no witness forced `additive`; it was true then and is superseded.

    TARGET (ix), ACCEPTED, FOR AFTER MERGE. The amended statements' only proved
    instance is the two-state chain they were built around. Wanted: a confirming
    instance that is not — three states, positive, stochastic, additive, exact,
    rows unequal. Recorded in advance: `ExactKernel` confines such chains to ones
    that reach stationarity in finitely many steps — on three states, a rank-one
    part plus a nilpotent deviation — so the confirmation will be weaker than a
    generic one, and must say so when it lands. -/
namespace REamend
open Classical
open RE RE4 REi REgen REref

/-- AMENDED hypotheses of general A and B. -/
structure FiniteChain {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) : Prop where
  base       : FiniteChainU univ step ρ
  stochastic : ∀ x, step x (fun _ => True) = 100
  additive   : ∀ (x : X) (B : X → Prop),
    step x B = (univ.map (fun y => if B y then step x (fun z => z = y) else 0)).sum

/-- GENERAL PART A, amended. CONJECTURE: the finite Doeblin statement in the
    record's Cesàro form. Its unamended predecessor is refuted in §22; its
    two-state instance is proved (`REgen.partA_instance`); and this time it was
    attacked before commit — the §22 witness is excluded by `stochastic`. -/
theorem general_partA {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) (_hC : FiniteChain univ step ρ) :
    ∀ (start : X) (basin : X → Prop), PartA_concl univ step ρ start basin := by
  sorry -- CONJECTURE: needs a Doeblin contraction, not formalized here.

/-- GENERAL PART B, amended. CONJECTURE: strict positivity on a finite
    stochastic kernel gives mixing. Proved instance: `REgen.partB_instance`. -/
theorem general_partB {X : Type} (univ : List X) (step : X → (X → Prop) → Nat)
    (ρ : (X → Prop) → Nat) (_hC : FiniteChain univ step ρ) :
    ∀ (start : X) (basin : X → Prop), PartB_concl univ step ρ start basin := by
  sorry -- CONJECTURE: Perron–Frobenius / Doeblin, not formalized here.

/-- The two-state chain satisfies the AMENDED hypotheses, so the proved
    instances still witness the general statements' shape. -/
theorem two_state_is_finite_chain : FiniteChain [true, false] stepTwo rhoTwo where
  base       := two_state_is_finite_chainU
  stochastic := by intro x; simp [stepTwo]
  additive   := by intro x B; simp [stepTwo]

/-- The peer's witness FAILS the amendment — the compile-decidable sign that the
    fix is the right one. One row totals 50, not 100. -/
theorem stepBad_not_stochastic : ¬ (∀ x, stepBad x (fun _ => True) = 100) := by
  intro h; have := h false; simp [stepBad] at this

theorem bad_not_amended : ¬ FiniteChain [true, false] stepBad rhoBad :=
  fun h => stepBad_not_stochastic h.stochastic

/-- …but it SATISFIES `additive`, so §22 forces `stochastic` only; `additive`
    is forced by §22.2. -/
theorem stepBad_additive : ∀ (x : Bool) (B : Bool → Prop),
    stepBad x B = ([true, false].map (fun y => if B y then stepBad x (fun z => z = y) else 0)).sum := by
  intro x B
  cases x <;> by_cases h1 : B true <;> by_cases h2 : B false <;> simp [stepBad, h1, h2]

/-- The §22.2 witness FAILS the amendment too — at `additive`. The mirror of
    `bad_not_amended`, and the second compile-decidable check on the fix. -/
theorem bad2_not_amended : ¬ FiniteChain [true, false] REref2.stepBad2 REref.rhoBad :=
  fun h => REref2.stepBad2_not_additive h.additive

end REamend

/-! ## 24. Target (ix): a confirming instance that is not the two-state chain -/
namespace REix
open Classical
open RE RE4 REgen REamend

inductive T3 where
  | a | b | c
  deriving DecidableEq

/-- `abbrev`, so rewrites stated with `u3` match a goal where it has been
    unfolded to the literal list. -/
abbrev u3 : List T3 := [T3.a, T3.b, T3.c]

/-- Point masses of the kernel, in percent. Rows a = (31,42,27), b = (37,34,29),
    c = (55,10,35): positive, each summing to 100, pairwise distinct, none equal
    to ρ. Built as ρ + ½·u vᵀ with u = (3,1,−5) ⊥ ρ and v = 1 × u = (−6,8,−2),
    so the deviation is nilpotent: M² = 1ρᵀ. -/
def M3 : T3 → T3 → Nat
  | .a, .a => 31 | .a, .b => 42 | .a, .c => 27
  | .b, .a => 37 | .b, .b => 34 | .b, .c => 29
  | .c, .a => 55 | .c, .b => 10 | .c, .c => 35

noncomputable def step3 : T3 → (T3 → Prop) → Nat :=
  fun x B => (if B T3.a then M3 x T3.a else 0) + (if B T3.b then M3 x T3.b else 0)
    + (if B T3.c then M3 x T3.c else 0)

noncomputable def rho3 : (T3 → Prop) → Nat :=
  fun B => (if B T3.a then 40 else 0) + (if B T3.b then 30 else 0) + (if B T3.c then 30 else 0)

theorem law1 : ∀ (start : T3) (B : T3 → Prop), iterLaw u3 step3 1 start B = step3 start B := by
  intro start B
  cases start <;> simp [iterLaw, u3]

theorem rho3_invariant : ∀ B : T3 → Prop,
    (u3.map (fun x => rho3 (fun y => y = x) * step3 x B)).sum / 100 = rho3 B := by
  intro B
  by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
    simp [u3, rho3, step3, M3, ha, hb, hc]

theorem law2 : ∀ (start : T3) (B : T3 → Prop), iterLaw u3 step3 2 start B = rho3 B := by
  intro start B
  rw [iterLaw]
  simp only [u3, List.map, List.sum_cons, List.sum_nil]
  rw [law1 start (fun y => y = T3.a), law1 start (fun y => y = T3.b), law1 start (fun y => y = T3.c)]
  cases start <;> by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
    simp [step3, M3, rho3, ha, hb, hc]

theorem law_ge2 : ∀ (t : Nat) (start : T3) (B : T3 → Prop),
    iterLaw u3 step3 (t + 2) start B = rho3 B := by
  intro t
  induction t with
  | zero => exact law2
  | succ n ih =>
    intro start B
    rw [iterLaw]
    simp only [u3, List.map, List.sum_cons, List.sum_nil]
    rw [ih start (fun y => y = T3.a), ih start (fun y => y = T3.b), ih start (fun y => y = T3.c)]
    have := rho3_invariant B
    simp only [u3, List.map, List.sum_cons, List.sum_nil] at this
    exact this

theorem exact3 : ExactKernel u3 step3 := by
  intro t start B
  simp only [u3, List.map, List.sum_cons, List.sum_nil]
  cases t with
  | zero =>
    cases start <;> by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
      simp [iterLaw, step3, M3, ha, hb, hc] <;> omega
  | succ t =>
    cases t with
    | zero =>
      rw [law1 start (fun y => y = T3.a), law1 start (fun y => y = T3.b), law1 start (fun y => y = T3.c)]
      cases start <;> by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
        simp [step3, M3, ha, hb, hc] <;> omega
    | succ t =>
      rw [law_ge2 t start (fun y => y = T3.a), law_ge2 t start (fun y => y = T3.b),
          law_ge2 t start (fun y => y = T3.c)]
      by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
        simp [rho3, step3, M3, ha, hb, hc] <;> omega

/-- The instance satisfies the AMENDED hypotheses. -/
theorem chain3 : REamend.FiniteChain u3 step3 rho3 where
  base :=
    { complete  := by intro x; cases x <;> simp [u3]
      nodup     := by decide
      exact     := exact3
      positive  := by intro x y; cases x <;> cases y <;> simp [step3, M3]
      measure   := by
        intro B
        by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
          simp [u3, rho3, ha, hb, hc]
      total     := by simp [rho3]
      invariant := rho3_invariant }
  stochastic := by intro x; cases x <;> simp [step3, M3]
  additive   := by intro x B; simp [step3, u3, Nat.add_assoc]

/-- REQUIREMENT (1): convergence is NOT stationarity from step one. From start `a`
    the law of `{a}` at t = 1 is 31, not ρ's 40. -/
theorem ix_not_stationary_at_one :
    iterLaw u3 step3 1 T3.a (fun y => y = T3.a) ≠ rho3 (fun y => y = T3.a) := by
  rw [law1]; simp [step3, M3, rho3]

/-- REQUIREMENT (2): the three rows are pairwise distinct, and none equals ρ —
    witnessed on `{a}`, where they give 31, 37, 55 against ρ's 40. -/
theorem ix_rows_distinct :
    step3 T3.a (fun y => y = T3.a) ≠ step3 T3.b (fun y => y = T3.a) ∧
    step3 T3.a (fun y => y = T3.a) ≠ step3 T3.c (fun y => y = T3.a) ∧
    step3 T3.b (fun y => y = T3.a) ≠ step3 T3.c (fun y => y = T3.a) ∧
    step3 T3.a (fun y => y = T3.a) ≠ rho3 (fun y => y = T3.a) ∧
    step3 T3.b (fun y => y = T3.a) ≠ rho3 (fun y => y = T3.a) ∧
    step3 T3.c (fun y => y = T3.a) ≠ rho3 (fun y => y = T3.a) := by
  simp [step3, M3, rho3]

theorem bound_rho (B : T3 → Prop) : rho3 B ≤ 100 := by
  by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;> simp [rho3, ha, hb, hc]

theorem bound_law0 (start : T3) (B : T3 → Prop) : iterLaw u3 step3 0 start B ≤ 100 := by
  by_cases h : B start <;> simp [iterLaw, h]

theorem bound_law1 (start : T3) (B : T3 → Prop) : iterLaw u3 step3 1 start B ≤ 100 := by
  rw [law1]
  cases start <;> by_cases ha : B T3.a <;> by_cases hb : B T3.b <;> by_cases hc : B T3.c <;>
    simp [step3, M3, ha, hb, hc]

/-- PART B CONFIRMED on this instance, for EVERY start and EVERY set. -/
theorem ix_partB : ∀ (start : T3) (basin : T3 → Prop), PartB_concl u3 step3 rho3 start basin := by
  intro start basin ε hε
  refine ⟨1, fun t ht => ?_⟩
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 2 := ⟨t - 2, by omega⟩
  rw [law_ge2]; constructor <;> omega

theorem psum3 (start : T3) (B : T3 → Prop) : ∀ m : Nat,
    psum (fun s => iterLaw u3 step3 s start B) (m + 2)
      = iterLaw u3 step3 0 start B + iterLaw u3 step3 1 start B + m * rho3 B := by
  intro m
  induction m with
  | zero => simp [psum]
  | succ n ih =>
    show psum _ (n + 2) + iterLaw u3 step3 (n + 2) start B = _
    rw [ih, law_ge2]; rw [Nat.succ_mul]; omega

/-- PART A CONFIRMED on this instance, in the record's Cesàro form, for EVERY
    start and EVERY set. -/
theorem ix_partA : ∀ (start : T3) (basin : T3 → Prop), PartA_concl u3 step3 rho3 start basin := by
  intro start basin ε hε
  refine ⟨300, fun t ht => ?_⟩
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 2 := ⟨t - 2, by omega⟩
  rw [psum3]
  have h0 := bound_law0 start basin
  have h1 := bound_law1 start basin
  have hr := bound_rho basin
  have hte : 1 * (m + 2) ≤ ε * (m + 2) := Nat.mul_le_mul_right _ (by omega : 1 ≤ ε)
  have hcomm : (m + 2) * ε = ε * (m + 2) := Nat.mul_comm _ _
  have hmr : (m + 2) * rho3 basin = m * rho3 basin + 2 * rho3 basin := by rw [Nat.add_mul]
  constructor <;> omega

end REix

/-! ### 24.1 Readout — target (ix)

    (ix) confirming instance beyond the two-state chain | expected: confirmed,
    narrow | OBSERVED: CONFIRMED. `chain3` proves the three-state kernel satisfies
    every AMENDED hypothesis — positive, stochastic, additive, exact, with
    ρ = (40, 30, 30) invariant. `ix_partA` and `ix_partB` prove Parts A and B for
    EVERY start and EVERY set, from the instance lemmas alone and never from the
    `sorry`'d general statements.

    REQUIREMENT (1), proved: from start `a` the law of `{a}` at t = 1 is 31, not
    ρ's 40 (`ix_not_stationary_at_one`), so convergence is not stationarity from
    step one. REQUIREMENT (2), proved: the rows are pairwise distinct and none
    equals ρ (`ix_rows_distinct`).

    THE WEAKENING, ruled by the reviewer and recorded before the attempt: ONE
    INSTANCE, FINITE-HORIZON BY CONSTRUCTION. The kernel is ρ plus a nilpotent
    deviation, so M² = 1ρᵀ and the law equals ρ exactly from t = 2 on
    (`law_ge2`). That is what `ExactKernel` permits on a 1/100 grid, and it is
    why the confirmation is narrow: it exercises the amended hypotheses and the
    conclusions' quantifier structure, not the asymptotic mixing that makes
    Parts A and B hard. THE GENERIC FINITE DOEBLIN CASE REMAINS THE SORRY.

    One mechanical note: `u3` is an `abbrev`, not a `def`. As a `def`, rewrites
    stated with `u3` failed to match goals where it had been unfolded to the
    literal list — the same surface-text-versus-object gap the file records
    elsewhere, in a smaller form. -/

/-! ## 25. Problem 25's pushforward probe — PRE-REGISTRATION

    Outcome space by the peer reviewer, who is not running it; committed before
    any probe code, on my user's go (2026-09-10). The runner does not edit these
    items. Deviations get declared at the site, as before.

    THE CANDIDATE. Push ρ_∞ from `State` to `Rep` through the fibers: for a
    property `p : L.Rep → Prop`, its preimage is the set of substrate states that
    formulate some `x` with `p x`, and its mass is `J.X.rho` of that preimage.
    "Large" means that mass is not small. This is ρ_∞'s THIRD role — not on `Rep`
    directly (the resolved remark), not Problem 26's aggregation — built only from
    objects already in `Joined`: `rho`, `formulable`, `fiber`.

    (i) THE FORK, and the first target. `formulable` is a relation, not a map, so
        the pushforward needs no choice of section — but it does need
        single-valuedness. If each state formulates at most one structure, the
        pushforward is a measure: disjoint properties have disjoint preimages.
        If not, a state in two fibers is counted twice and the pushforward is only
        subadditive — an outer measure, which does not meet Problem 25's
        prerequisite. A2 says Π is a many-to-one FUNCTION, which reads as
        functional. FIRST, COMMIT-DECIDABLE CHECK (peer's addendum, folded in
        here): does any hypothesis in `Joined` or its witnesses make `formulable`
        single-valued? If none does, the gap gets a Problem-30-style entry BEFORE
        the pushforward is defined, and the restriction goes in as an explicit
        hypothesis citing A2. Then both sides of the fork are exhibited: a
        witness where `formulable` is functional and the pushforward is proved
        additive, and one where it is not and additivity fails.
    (ii) NON-VACUITY: on the same witness, a property with positive pushforward
        mass AND a property with zero pushforward mass. Without both, Large is
        everything or nothing, and the RR shape is trivially satisfied or
        trivially refuted — which is how the last two transpositions of this
        conjecture died.
    (iii) HOSTABILITY: instantiate `RR_shape` with the pushforward Large. Hard and
        Useful stay parameters; the pushforward fills one slot of three. The
        result says "Large now has a referent; Hard and Useful don't", and no
        more. If the instantiated shape can be evaluated on the transparent layer
        `Lid`, it is — Theorem 10's mechanism has refuted every prior
        transposition and gets its turn on this one.

    THRESHOLD, a logged choice. "Not small" means POSITIVE MASS (`lt zero`),
    since `Val` offers `lt` and needs nothing more. Razborov–Rudich use "at least
    a fixed fraction of total mass", which needs a scale on `Val` the frame lacks;
    adding one would be a representation item. Positive mass is WEAKER than RR's
    largeness, and the result must say so.

    OUTCOMES.
      (A) `formulable` functional in the intended reading, pushforward proved
          additive, both guards exhibited, `RR_shape` instantiated with Large
          filled: Problem 25's prerequisite has a candidate from inside the file.
          Not a derivation of opacity — a hosting of its largeness slot.
      (B) Functional, but non-vacuity fails on every witness tried: a measure
          with no content in this frame. Record and stop.
      (C) `formulable` not functional, and the manuscript does not say it must
          be: the pushforward is not a measure. Log the choice — restrict
          `Joined` to functional, as a hypothesis — and re-run under it.
    PRIOR, the peer's, distrusted as usual: (C), with the restriction then giving
    (A) one level down. Under the addendum, (C) is the EXPECTED path if no
    hypothesis in the file supplies single-valuedness. -/

/-! ## 26. Problem 25 probe, item (i): the first check, and a gap logged BEFORE
    the pushforward is defined

    RESULT OF THE FIRST CHECK: NO hypothesis anywhere in the file makes
    `formulable` single-valued. `Joined.formulable` and `Bridge.formulable` are
    both bare relations `X.State → L.Rep → Prop`, constrained by nothing. The
    file's only `Joined` witness, `J0`, sets `formulable := fun _ _ => True` —
    the MAXIMALLY non-functional relation: every state formulates every
    structure.

    A2, verbatim: "Π is a surjective function from 𝒮 to 𝒪. Π is many-to-one."
    So the transcription of A2 into `Joined`, written during the Problem 26
    probe, dropped three properties at once: SINGLE-VALUEDNESS and TOTALITY —
    what "function" means — and SURJECTIVITY. Which of them the pushforward
    needs: single-valuedness for ADDITIVITY, since disjoint properties then have
    disjoint preimages; totality for NORMALIZATION, since the pushforward of the
    whole space is then the whole mass; surjectivity for neither. Logged as Open
    Problem 31 and as ledger entry twelve.

    CONSEQUENCE, as pre-registered: outcome (C) is the expected path. The
    restriction goes in as explicit hypotheses citing A2 — `SingleValued`, and
    `Total` for normalization — and the probe runs under them. This section is
    committed before the pushforward is defined; the definition comes next. -/

/-! ## 27. The pushforward probe, run

    Under the restriction logged in §26: `SingleValued` and `Total` as explicit
    hypotheses citing A2. -/
namespace REp25
open Classical
open RE RE4 REgen REamend

/-- The pushforward of the substrate's measure through the fibers of `formulable`:
    the mass of the set of states that formulate SOME structure with `p`. -/
noncomputable def pushMass (J : Joined) (p : J.L.Rep → Prop) : J.X.Val :=
  J.X.rho (fun s => ∃ x, J.formulable s x ∧ p x)

/-- A2's "function", part one: each state formulates at most one structure. -/
def SingleValued (J : Joined) : Prop :=
  ∀ s x y, J.formulable s x → J.formulable s y → x = y

/-- A2's "function", part two: each state formulates some structure. -/
def Total (J : Joined) : Prop := ∀ s, ∃ x, J.formulable s x

/-- Under single-valuedness, the pushforward inherits additivity from `ρ`. The
    hypothesis is exactly what is needed: without it, a state in two fibers lands
    in both preimages. -/
theorem pushMass_additive (J : Joined) (hsv : SingleValued J)
    (add : J.X.Val → J.X.Val → J.X.Val)
    (hadd : ∀ A B : J.X.State → Prop, (∀ s, ¬ (A s ∧ B s)) →
      J.X.rho (fun s => A s ∨ B s) = add (J.X.rho A) (J.X.rho B))
    (p q : J.L.Rep → Prop) (hpq : ∀ x, ¬ (p x ∧ q x)) :
    pushMass J (fun x => p x ∨ q x) = add (pushMass J p) (pushMass J q) := by
  unfold pushMass
  have e : (fun s => ∃ x, J.formulable s x ∧ (p x ∨ q x))
      = (fun s => (∃ x, J.formulable s x ∧ p x) ∨ (∃ x, J.formulable s x ∧ q x)) := by
    funext s; apply propext; constructor
    · rintro ⟨x, hf, hp | hq⟩
      · exact Or.inl ⟨x, hf, hp⟩
      · exact Or.inr ⟨x, hf, hq⟩
    · rintro (⟨x, hf, hp⟩ | ⟨x, hf, hq⟩)
      · exact ⟨x, hf, Or.inl hp⟩
      · exact ⟨x, hf, Or.inr hq⟩
  rw [e]
  apply hadd
  rintro s ⟨⟨x, hfx, hp⟩, ⟨y, hfy, hq⟩⟩
  have hxy := hsv s x y hfx hfy
  subst hxy
  exact hpq x ⟨hp, hq⟩

/-! ### The functional side of the fork -/

inductive S3 where
  | s1 | s2 | s3
  deriving DecidableEq

/-- Three substrate states with masses (50, 50, 0). -/
@[reducible] noncomputable def XG : Substrate where
  State := S3
  Val := Nat
  zero := 0
  one := 100
  lt := fun a b => a < b
  sub := fun a b => a - b
  add := fun a b => a + b
  P := fun _ => 0
  basin := fun _ => True
  rho := fun B => (if B S3.s1 then 50 else 0) + (if B S3.s2 then 50 else 0)
  rho_basin_pos := by show (0:Nat) < _; simp
  rho_empty := by simp
  rho_add := by
    intro A B hdis
    have h1 := hdis S3.s1; have h2 := hdis S3.s2
    by_cases a1 : A S3.s1 <;> by_cases b1 : B S3.s1 <;> by_cases a2 : A S3.s2 <;>
      by_cases b2 : B S3.s2 <;> simp_all

/-- Functional, total, surjective, many-to-one: `s₁, s₂ ↦ true`, `s₃ ↦ false`. -/
@[reducible] noncomputable def Jg : Joined where
  L := Lid
  X := XG
  formulable := fun s x => match s with
    | S3.s1 => x = true
    | S3.s2 => x = true
    | S3.s3 => x = false
  Om := Omid

theorem sv_G : SingleValued Jg := by
  intro s x y hx hy
  cases s <;> (simp only [Jg] at hx hy; rw [hx, hy])

theorem total_G : Total Jg := by
  intro s; cases s
  · exact ⟨true, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨false, rfl⟩

theorem hadd_G : ∀ A B : Jg.X.State → Prop, (∀ s, ¬ (A s ∧ B s)) →
    Jg.X.rho (fun s => A s ∨ B s) = Jg.X.rho A + Jg.X.rho B := by
  intro A B hdis
  have h1 := hdis S3.s1; have h2 := hdis S3.s2
  by_cases a1 : A S3.s1 <;> by_cases b1 : B S3.s1 <;> by_cases a2 : A S3.s2 <;>
    by_cases b2 : B S3.s2 <;> simp_all [Jg, XG]

/-- FORK, functional side: the pushforward is additive. -/
theorem pushMass_additive_G (p q : Jg.L.Rep → Prop) (hpq : ∀ x, ¬ (p x ∧ q x)) :
    pushMass Jg (fun x => p x ∨ q x) = pushMass Jg p + pushMass Jg q :=
  pushMass_additive Jg sv_G (· + ·) hadd_G p q hpq

/-- Normalization, from totality: the pushforward of everything is the full mass. -/
theorem pushMass_total_G : pushMass Jg (fun _ => True) = 100 := by
  unfold pushMass; simp [Jg, XG]

/-! ### Item (ii): both non-vacuity guards, on the same witness -/

theorem pos_mass_true : pushMass Jg (fun x => x = true) = 100 := by
  unfold pushMass; simp [Jg, XG]

/-- ZERO mass on a property that is NOT empty and IS formulated — by `s₃`, a
    zero-mass state. Not the trivial zero of the empty property. -/
theorem zero_mass_false : pushMass Jg (fun x => x = false) = 0 := by
  unfold pushMass; simp [Jg, XG]

theorem false_is_formulated : ∃ s, Jg.formulable s false := ⟨S3.s3, rfl⟩

/-! ### The non-functional side of the fork -/

/-- One state, with an ADDITIVE point-mass `ρ`, so any failure of additivity
    below is `formulable`'s fault, not `ρ`'s. -/
@[reducible] noncomputable def XU : Substrate where
  State := Unit
  Val := Nat
  zero := 0
  one := 100
  lt := fun a b => a < b
  sub := fun a b => a - b
  add := fun a b => a + b
  P := fun _ => 0
  basin := fun _ => True
  rho := fun B => if B () then 100 else 0
  rho_basin_pos := by show (0:Nat) < _; simp
  rho_empty := by simp
  rho_add := by
    intro A B hdis; have h := hdis ()
    by_cases a : A () <;> by_cases b : B () <;> simp_all

/-- The state formulates BOTH structures — the shape of the file's own `J0`. -/
@[reducible] noncomputable def Jbad : Joined where
  L := Lid
  X := XU
  formulable := fun _ _ => True
  Om := Omid

theorem hadd_U : ∀ A B : Jbad.X.State → Prop, (∀ s, ¬ (A s ∧ B s)) →
    Jbad.X.rho (fun s => A s ∨ B s) = Jbad.X.rho A + Jbad.X.rho B := by
  intro A B hdis
  have h := hdis ()
  by_cases a : A () <;> by_cases b : B () <;> simp_all [Jbad, XU]

theorem not_sv_bad : ¬ SingleValued Jbad := by
  intro h; have := h () true false trivial trivial; cases this

/-- FORK, non-functional side: on two DISJOINT properties, with `ρ` additive, the
    pushforward is not — 100 against 100 + 100. -/
theorem additivity_fails_bad :
    pushMass Jbad (fun x => x = true ∨ x = false)
      ≠ pushMass Jbad (fun x => x = true) + pushMass Jbad (fun x => x = false) := by
  unfold pushMass; simp [Jbad, XU]

/-! ### Item (iii): `RR_shape` with the largeness slot filled -/

/-- Largeness as POSITIVE pushforward mass — the logged threshold, weaker than
    Razborov–Rudich's fraction-largeness. -/
noncomputable def LargePush (J : Joined) : (J.L.Rep → Prop) → Prop :=
  fun p => J.X.lt J.X.zero (pushMass J p)

/-- The RR shape with ONE of its three slots filled. `Hard` and `Useful` stay
    parameters. -/
def RR_hosted (J : Joined) (Hard : Prop) (Useful : (J.L.Rep → Prop) → Prop) : Prop :=
  RR_shape J.L (LargePush J) Hard Useful

theorem large_true : LargePush Jg (fun x => x = true) := by
  show (0:Nat) < pushMass Jg (fun x => x = true)
  rw [pos_mass_true]; decide

theorem not_large_false : ¬ LargePush Jg (fun x => x = false) := by
  show ¬ (0:Nat) < pushMass Jg (fun x => x = false)
  rw [zero_mass_false]; exact Nat.lt_irrefl 0

/-- On the transparent layer `Lid`, the large property IS constructive — so
    Theorem 10's mechanism can fire the shape's antecedent. -/
theorem constructive_true_Lid : constructiveFor Lid (fun x => x = true) :=
  ⟨true, Nat.le_refl 0, fun _ => decide_eq_true_iff⟩

/-- Lid's turn. With the antecedent firing, the hosted shape FORCES `¬ Useful` on
    the large constructive property whenever `Hard` holds. It constrains the
    unfilled slot; it does not fall. -/
theorem rr_hosted_on_Lid_forces (Hard : Prop) (Useful : (Jg.L.Rep → Prop) → Prop) :
    RR_hosted Jg Hard Useful → Hard → ¬ Useful (fun x => x = true) :=
  fun h hH => h hH _ constructive_true_Lid large_true

/-- …and it is satisfiable on Lid, for every `Hard`: take `Useful` empty. So
    Theorem 10's mechanism does not refute this transposition. -/
theorem rr_hosted_satisfiable (Hard : Prop) : RR_hosted Jg Hard (fun _ => False) :=
  fun _ _ _ _ h => h


/-! ### The functional witness satisfies ALL of A2, not only what the probe needs -/

/-- A2's "surjective". -/
def Surjective (J : Joined) : Prop := ∀ x, ∃ s, J.formulable s x

theorem surj_G : Surjective Jg := by
  intro x; cases x
  · exact ⟨S3.s3, rfl⟩
  · exact ⟨S3.s1, rfl⟩

/-- A2 in full on the witness: a single-valued, total, surjective relation — a
    surjective function — and many-to-one, since `s₁` and `s₂` both formulate
    `true`. So `Jg` witnesses the reading A2 intends, not a convenient part of it. -/
theorem A2_G : SingleValued Jg ∧ Total Jg ∧ Surjective Jg ∧
    (Jg.formulable S3.s1 true ∧ Jg.formulable S3.s2 true) :=
  ⟨sv_G, total_G, surj_G, rfl, rfl⟩

end REp25

/-! ### 27.1 Readout — Problem 25 pushforward probe

    (i) single-valuedness | expected: a gap, likely | OBSERVED: GAP. No hypothesis
        in the file makes `formulable` single-valued, and the file's only witness
        is maximally non-functional. Logged in §26 BEFORE the pushforward was
        defined. The fork is exhibited on both sides. Functional: the pushforward
        is additive, as a general theorem under `SingleValued`
        (`pushMass_additive`) and on the witness (`pushMass_additive_G`).
        Non-functional: additivity FAILS — 100 against 100 + 100 on two disjoint
        properties (`additivity_fails_bad`) — with `ρ` itself PROVED additive
        there (`hadd_U`), so the failure is `formulable`'s. Normalization from
        totality: `pushMass_total_G`. The functional witness satisfies all of A2
        (`A2_G`): single-valued, total, surjective, many-to-one.
    (ii) non-vacuity | expected: both guards | OBSERVED: BOTH, on one witness.
        Positive mass 100 on `(· = true)` (`pos_mass_true`); mass ZERO on
        `(· = false)` (`zero_mass_false`), a property that is non-empty and IS
        formulated (`false_is_formulated`) — by a zero-mass state. Not the
        trivial zero of the empty property.
    (iii) hostability | expected: one slot filled | OBSERVED: ONE SLOT FILLED.
        `RR_hosted` instantiates `RR_shape` with the pushforward largeness.
        LARGE NOW HAS A REFERENT; HARD AND USEFUL DON'T. On Lid the hosted shape
        is CONSISTENT (`rr_hosted_satisfiable`, with `Useful` empty), and it
        CONSTRAINS `Useful` ON ONE PROPERTY WHEN `Hard` HOLDS
        (`rr_hosted_on_Lid_forces`, via `constructive_true_Lid` and
        `large_true`). Nothing stronger is claimed: satisfiability is consistency,
        not content, and `Hard` and `Useful` remain empty slots. The transparent
        layer that refuted every earlier transposition does not refute this one,
        because the shape now runs in Razborov–Rudich's direction. The next
        transposition that claims more than consistency plus this one constraint
        is the one to attack.

    TWO FINDINGS, not just audit lines.
      · `pushMass_additive` is CHOICE-FREE: `[propext, Quot.sound]`, no
        `Classical.choice`. Single-valuedness ⇒ additivity is a constructive fact
        about the relation; every witness needs choice only to evaluate its
        classical `if`s. Same shape as the §2 frame, axiom-free up to exactly the
        point where assertions begin.
      · `zero_mass_false` is a property that is non-empty, formulated, and of
        zero mass. It is the first place in the file where LARGE SEPARATES FROM
        NON-EMPTY — largeness is measure content, not set content — and it is
        exactly what the two dead transpositions of this conjecture lacked. That
        is why (ii) matters.

    OUTCOME, AS RULED BY THE REVIEWER: (A), UNDER A HYPOTHESIS THE MANUSCRIPT
    ALREADY STATES AND THE TRANSCRIPTION HAD DROPPED (Problem 31). Outcome (C) had
    two conjuncts, and the second — the manuscript silent on whether the
    projection is a function — is false: A2 says function. What separates the
    cases is where the hypothesis comes from. `SingleValued` is imported from A2,
    not invented for the proof, so it repairs the transcription rather than
    adding an assumption. The result hosts opacity's largeness slot from inside
    the file; it does not derive opacity.

    THE PRIOR, scored as the reviewer asked: it landed in substance for the WRONG
    REASON. It predicted a choice to log and got a loss to repair — a worse miss
    than a plain wrong call, because the right outcome was reached by a mechanism
    it never named.

    THE WEAKENING, as logged: largeness here is POSITIVE mass, weaker than
    Razborov–Rudich's "at least a fixed fraction of total mass". Fraction-
    largeness needs a scale on `Val` the frame does not have; adding one is a
    representation item, not taken here. -/

/-! ## 28. Target (x) — PRE-REGISTRATION: is any result an artifact of `J0`?

    Outcome space by the peer reviewer; committed before the run. One DECLARED
    DEVIATION, with its reason at the site, per the governance clause.

    THE CONCERN. `J0` sets `formulable := fun _ _ => True`, violating A2 three
    ways (§26). Every result derived from `J0` is suspect as an artifact of a
    witness the manuscript rules out.

    DECLARED DEVIATION: THE ENUMERATION. The reviewer's draft named §6–§8 — the
    discriminator, the Problem 26 aggregation probe, and the type-level
    partiality result feeding Problem 27 — as what was concluded from `J0`. The
    file says otherwise. `J0` is defined in §13, and a transitive closure over
    every declaration that references it, computed on the code with comments
    stripped, finds exactly ten dependents, all in §13: `Qfalse`, `th0`, `agg0`,
    `clears_false`, `qfalse_agrees`, and the five theorems `S_ex_holds`,
    `S_all_holds`, `D_fails`, `A_fails`, `G_holds` — the whole evidence for
    THEOREM 10. A second, raw search for `J0` in code outside §13, qualified or
    bare, finds nothing. §6 (`Substrate`, `Bridge`), §8 (`Joined.induced` and
    `induced_at_boundary`, generic over every `Joined`) and Theorem 9 (`L0` and
    `Om0`, no `Joined` at all) reference no witness of `Joined`. So the targets
    are the five §13 theorems, and the numbered result at stake is Theorem 10,
    not the §6 discriminator. The draft is kept in spirit; its section pointers
    are corrected because they would have re-checked results that cannot move.

    WHY ONLY THESE CAN MOVE. Restricting to A2-conforming witnesses NARROWS the
    class of `Joined`. A result quantified over every `Joined` survives any
    narrowing. What can move is an EXISTENTIAL result or a REFUTATION OF A
    UNIVERSAL — anything whose force came from exhibiting a witness, which may
    be the illegal one. All five `J0` theorems are of that kind.

    TARGETS. For each of the five: re-establish it restricted to legal witnesses
    — `SingleValued ∧ Total ∧ Surjective`, over `L0` where the original requires
    it — or show that it does not reproduce.

    OUTCOMES. (S) all stand. (M) some move and are relabeled. (X) a numbered
    result — here Theorem 10 — depended on the illegal witness and is withdrawn.

    PRIORS. The reviewer's: most stand, with the §6 discriminator the likeliest to
    move — its second half answered by the deviation, since §6 has no witness to
    move. Mine: (S), because every `J0` proof runs through an aggregator or query
    family that never reads `formulable` — the constant aggregator in `S_ex`, `A`
    and `G`, and a query family reading the induced potential directly in
    `S_all`. Mechanism stated beside the prediction, which this record says to
    distrust. -/

/-! ## 29. Target (x), run -/
namespace REx
open Classical
open RE RE4 REgen REamend REp25

/-- A2-conformance, the restriction every re-established result carries. -/
def Legal (J : Joined) : Prop := SingleValued J ∧ Total J ∧ Surjective J

/-- An A2-conforming witness over `L0`, where §13's `J0` was not: three states,
    `s₁, s₂ ↦ true`, `s₃ ↦ false`. Single-valued, total, surjective, many-to-one. -/
@[reducible] noncomputable def J1 : Joined where
  L := L0
  X := XG
  formulable := fun s x => match s with
    | S3.s1 => x = true
    | S3.s2 => x = true
    | S3.s3 => x = false
  Om := Om0

theorem legal_J1 : Legal J1 := by
  refine ⟨?_, ?_, ?_⟩
  · intro s x y hx hy; cases s <;> (simp only [J1] at hx hy; rw [hx, hy])
  · intro s; cases s
    · exact ⟨true, rfl⟩
    · exact ⟨true, rfl⟩
    · exact ⟨false, rfl⟩
  · intro x; cases x
    · exact ⟨S3.s3, rfl⟩
    · exact ⟨S3.s1, rfl⟩

/-- §13's objects, rebuilt over the legal witness. -/
noncomputable def Qfalse1 : ThresholdInterface J1.L J1.X.Val where
  QMethod := Unit
  ask := fun _ _ _ => false
  qcost := fun _ => 0

noncomputable def th1 : J1.X.Val := (0 : Nat)

noncomputable def agg1 : Aggregator J1 := fun _ _ _ => (0 : Nat)

theorem clears_false1 (x : J1.L.Rep) : ¬ J1.clearsAt agg1 th1 x :=
  fun h => absurd h (Nat.lt_irrefl 0)

theorem qfalse_agrees1 (x : J1.L.Rep) :
    Qfalse1.ask () th1 x = true ↔ J1.clearsAt agg1 th1 x := by
  constructor
  · intro h; exact Bool.noConfusion h
  · intro h; exact absurd h (clears_false1 x)

/-- `S_ex_holds`, restricted to legal witnesses. -/
theorem S_ex_legal : ∃ J : Joined, J.L = L0 ∧ Legal J ∧
    ∃ (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod) (θ : J.X.Val),
      I.affordable q ∧ Agrees J agg I q θ :=
  ⟨J1, rfl, legal_J1, agg1, Qfalse1, (), th1, Nat.le_refl 0, qfalse_agrees1⟩

/-- `S_all_holds`, restricted to legal witnesses: for EVERY aggregator, an
    affordable query family computes clearance. -/
theorem S_all_legal : ∃ J : Joined, J.L = L0 ∧ Legal J ∧
    ∀ (agg : Aggregator J), ∃ (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod) (θ : J.X.Val),
      I.affordable q ∧ Agrees J agg I q θ := by
  refine ⟨J1, rfl, legal_J1, ?_⟩
  intro agg
  refine ⟨⟨Unit, fun _ θ x => @decide _ (Nat.decLt θ (J1.induced agg x)), fun _ => 0⟩,
          (), th1, Nat.le_refl 0, ?_⟩
  intro x
  exact decide_eq_true_iff

/-- `D_fails`, restricted: "no legal witness survives" is false. -/
theorem D_fails_legal : ¬ ¬ (∃ J : Joined, J.L = L0 ∧ Legal J ∧
    ∃ (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod) (θ : J.X.Val),
      I.affordable q ∧ Agrees J agg I q θ) :=
  fun h => h S_ex_legal

/-- `A_fails`, restricted: the asymmetry's invariant form is false EVEN over
    legal witnesses. -/
theorem A_fails_legal : ¬ (∀ (J : Joined), Legal J →
    ∀ (agg : Aggregator J) (x : J.L.Rep), ¬ J.Om.Defined x →
    ∀ (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod), I.affordable q →
      ∀ θ : J.X.Val, ¬ Agrees J agg I q θ) :=
  fun hA => hA J1 legal_J1 agg1 false gap_exists Qfalse1 () (Nat.le_refl 0) th1 qfalse_agrees1

/-- `G_holds`, restricted: the poverty guard holds on a legal witness. -/
theorem G_holds_legal : ∃ (J : Joined), Legal J ∧
    ∃ (agg : Aggregator J) (I : ThresholdInterface J.L J.X.Val) (q : I.QMethod) (θ : J.X.Val),
      I.affordable q ∧ ∀ x : J.L.Rep, J.Om.Defined x → (I.ask q θ x = true ↔ J.clearsAt agg θ x) :=
  ⟨J1, legal_J1, agg1, Qfalse1, (), th1, Nat.le_refl 0, fun x _ => qfalse_agrees1 x⟩

end REx

/-! ### 29.1 Readout — target (x)

    (x) is any result an artifact of `J0`? | expected: (S), all stand |
    OBSERVED: (S). All five §13 theorems re-establish, restricted to LEGAL
    witnesses — single-valued, total, surjective — on `J1` over `L0`:
    `S_ex_legal`, `S_all_legal`, `D_fails_legal`, `A_fails_legal` and
    `G_holds_legal`, with `legal_J1` proving the witness conforms to A2. No
    `sorryAx`. THEOREM 10 STANDS, now on a witness the manuscript permits.

    WHY, as the mechanism stated in advance: no §13 proof reads `formulable`. The
    constant aggregator ignores the fiber, and the query family in `S_all` reads
    the induced potential directly. `J0`'s illegality was idle in every proof
    that used it.

    A SECOND ILLEGALITY IN `J0`, found on the way. Its substrate `X0` carries
    `rho := fun _ => 1` — mass 1 on every set, the empty set included — which is
    not a measure. Harmless for the same reason: no §13 proof reads ρ. The legal
    witness carries a genuine additive ρ (`REp25.XG`, additivity proved as
    `hadd_G`). Underneath it sits a question this target does not settle:
    `Substrate.rho` is never REQUIRED to be additive. Theorem 13 caught the
    missing normalization of Theorem 7's measure; nothing caught this. Flagged
    for the reviewer rather than entered in the ledger here.

    THE PRICE, stated. The originals were nearly axiom-free: `S_ex`, `A` and `G`
    used no axioms, and `S_all` only `propext`. Every legal re-establishment
    carries `Classical.choice`. The cause is the repair of the second
    illegality: a genuine measure on arbitrary predicates must decide
    membership, which is classical, and `X0` was computable precisely because
    its ρ was not a measure. Moving to a legal witness costs choice — the same
    representation cost this file declares at item 15, arriving for the same
    reason.

    PRIORS. Mine, (S): landed, by the mechanism it named. The reviewer's "§6
    discriminator likeliest to move" was answered before the run, by the
    declared deviation: §6 had no witness to move.

    RULING ON THE DEVIATION (reviewer, 2026-09-10): accepted, and the draft was
    wrong about where the risk sat. It named sections from memory of the
    exchange; the file's dependency graph named §13 and Theorem 10. Closure over
    the dependents of the illegal witness is the method; recall is not.

    THE GENERAL LEMMA, stated once so later legality checks can cite it instead
    of redoing it. Restricting a class of witnesses preserves every result
    quantified universally over the class, and can disturb only results that
    got their force from EXHIBITING a witness — existential results and
    refutations of universals. A witness-legality audit therefore needs only the
    dependency closure of the illegal witness, filtered to results of those two
    kinds.

    ρ, RULED: ledger thirteen and Open Problem 32. `Substrate.rho` carries
    `rho_basin_pos` and nothing else, so "ρ_∞ is a measure" was a gloss. The
    repair is blocked on `Val` having no addition, and it goes before Problem
    26, whose aggregation consumes ρ. -/

/-! ## 30. Target (xi) — PRE-REGISTRATION: make ρ_∞ a measure in the signature

    Outcome space by the peer reviewer; committed before any code, on my user's
    go (2026-09-10). Enumeration first, as the lemma of §29.1 prescribes.

    ENUMERATION, from the file and not from recall. Four `Substrate` instances,
    no anonymous literals:
      X0   (§13)  rho := fun _ => 1        NOT a measure. 11 dependents: J0 and
                                           all of §13 — Theorem 10's original
                                           evidence.
      Xbad (§16)  rho := fun _ => 1        NOT a measure. 3 dependents: occBad,
                  (one := 10)              occBad_ergodic, and
                                           recipe_inevitability_refuted — i.e.
                                           Theorem 13.
      XG   (§27)  point masses 50/50/0     A measure. 27 dependents.
      XU   (§27)  point mass 100           A measure. 4 dependents.

    DECLARED DEVIATIONS from the reviewer's guard (c), with reasons.
      · The guard said "X0 must fail; XG and the Theorem 13/14 substrates must
        pass". Theorem 13's witness `Xbad` is ALSO a constant, non-measure ρ and
        fails too. Theorem 14 builds no `Substrate` at all — `Theorem7_faithful`
        takes its ingredients as bare parameters — so there is nothing there to
        pass or fail.
      · "X0 must fail" and "every existing theorem must still compile" cannot
        both hold of the file as it stands: `X0` failing takes `J0` and all
        eleven §13 dependents with it. Resolution: each non-measure ρ is kept as
        a FROZEN, compile-decidable failure — a theorem that the old ρ violates
        the new fields — and the witness itself is REPAIRED with a genuine measure
        that preserves the result it supports. The pattern of `bad_not_amended`.

    THE REPAIR.
      (a) `Substrate` gains `add : Val → Val → Val`, with NO laws unless some
          proof needs one; any law that is needed will be named by the theorem
          that needs it.
      (b) `Substrate` gains `rho_empty` (the empty set has mass `zero`) and
          `rho_add` (masses add over disjoint sets).
      (c) GUARD: the old constant ρ of `X0` and `Xbad` is recorded as violating
          the new fields; `XG` and `XU` keep their ρ unchanged and gain the new
          fields; every theorem that compiled before compiles after, with every
          repaired witness and reworked proof listed.
      (d) CHOICE: witnesses keep `Classical.choice`; the general statement about
          ρ — the pushforward's additivity, now derivable from `rho_add` instead
          of a supplied hypothesis — stays choice-free.
      NORMALIZATION (`rho` of everything equals `one`) IS NOT ADDED. It is
      Theorem 13's separate finding, and adding it here would change what
      Theorem 13's witness demonstrates.

    OUTCOMES. (R) repaired, all prior results re-compile unchanged. (R−)
    repaired, some prior witness needs rework beyond X0, listed. (B) blocked,
    because a prior theorem depends on ρ NOT being additive — itself a finding.

    PRIORS. The reviewer's: (R). Mine, from the enumeration: (R−). `Xbad` needs
    rework as well as `X0`, and `occBad_ergodic`'s proof — which assumes ρ is
    constant — will change. Expected also: repairing `X0` and `Xbad` with genuine
    measures makes them noncomputable, so their computable dependents in §13 and
    §16 will need `noncomputable` — the price of honest measures, a fourth time.
    (B) is not expected: the §13 proofs never read ρ, and Theorem 13's refutation
    reads only `one` and the occupation — a genuine point mass of 1 on a scale
    where `one` is 10 still breaks normalization. -/

/-! ## 30.1 Pre-registration addendum — the reviewer's amended guard, and Theorem 13

    Committed after §30 and before any run lands. Two items from the reviewer and
    one reading of mine, all recorded before the result is known.

    AMENDED GUARD (c), the reviewer's, replacing the one §30 declared a deviation
    from. Every existing theorem compiles, either unchanged or against a frozen
    copy of the unamended structure; and every NUMBERED result established on a
    witness with an illegal ρ is either re-established on a legal witness or
    explicitly relabeled as holding over the unamended structure only. By the
    witness-legality lemma (§29.1), only existentials and refutations need
    checking: Theorem 10 (§13), Theorem 13 (§16), and whatever else the closure
    finds.

    THE REVIEWER'S EXPECTED ANSWER FOR THEOREM 13, verbatim in substance.
    Theorem 14's two-state chain also refuted Theorem 7's original statement,
    with a genuine measure ρ = (½, ½). So even if `Xbad` cannot be repaired, the
    refutation survives legality via Theorem 14, and Theorem 13 reads "refuted
    over the unamended structure, and independently by a legal witness".

    MY READING, recorded as a prior against that expectation. Theorems 13 and 14
    refute DIFFERENT statements. Theorem 13 refutes the first TRANSCRIPTION:
    `recipe_inevitability_refuted` quantifies over `Substrate`, with `Ergodic`
    standing for Birkhoff's conclusion. Theorem 14 refutes Theorem 7 AS STATED,
    faithfully transcribed as `Theorem7_faithful`, whose signature builds no
    `Substrate`. So Theorem 14 cannot stand in for Theorem 13, and "survives via
    Theorem 14" is not available. What I expect instead: Theorem 13
    re-establishes DIRECTLY, because `Xbad` repairs with a genuine point mass of
    1 on a scale where `one` is 10 — still a normalization failure, which is all
    Theorem 13's refutation reads. And Theorem 14 is untouched by (xi)
    altogether, having no `Substrate` to amend. -/

/-! ## 31. Target (xi), run -/
namespace RExi
open Classical
open RE REp25

/-- The constant ρ that `X0` and `Xbad` used to carry. -/
def constRho : (Unit → Prop) → Nat := fun _ => 1

/-- FROZEN FAILURE 1: the old constant ρ cannot satisfy `rho_empty` — it gives the
    empty set mass 1, not 0. -/
theorem constRho_violates_empty : constRho (fun _ => False) ≠ 0 := by
  unfold constRho; decide

/-- FROZEN FAILURE 2: nor `rho_add` — on the disjoint pair (everything, nothing)
    it gives 1 against 1 + 1. -/
theorem constRho_violates_add :
    constRho (fun s => (fun _ : Unit => True) s ∨ (fun _ : Unit => False) s)
      ≠ constRho (fun _ => True) + constRho (fun _ => False) := by
  unfold constRho; decide

/-- (d) The pushforward's additivity, now INTRINSIC: derived from the structure's
    own `rho_add`, not from a supplied hypothesis. -/
theorem pushMass_additive_intrinsic (J : Joined) (hsv : SingleValued J)
    (p q : J.L.Rep → Prop) (hpq : ∀ x, ¬ (p x ∧ q x)) :
    pushMass J (fun x => p x ∨ q x) = J.X.add (pushMass J p) (pushMass J q) :=
  pushMass_additive J hsv J.X.add J.X.rho_add p q hpq

end RExi

/-! ### 31.1 Readout — target (xi)

    OUTCOME: (R−), as my prior predicted; the reviewer's prior was (R). ρ_∞ is
    now a measure in the signature: `Substrate` gains `add` (with NO laws — no
    proof in the file uses one), `rho_empty` and `rho_add`. Every theorem that
    compiled before compiles after; the 68-line audit guard is clean.

    REWORK BEYOND `X0`, listed:
      · `X0` (§13): ρ repaired to a genuine point mass of 1. The repair is
        classical, so `X0` becomes noncomputable, and with it `J0`, `Qfalse`,
        `th0` and `agg0`. No §13 PROOF changed — none reads ρ.
      · `Xbad` (§16): ρ repaired to a genuine point mass of 1, on a scale where
        `one` is still 10. Noncomputable, with `occBad`. `occBad_ergodic`'s PROOF
        changed: it had assumed ρ constant, and now cases on whether the set
        contains the one state.
      · `XG`, `XU` (§27): ρ unchanged; the new fields added and proved.
    FROZEN FAILURES: `constRho_violates_empty` and `constRho_violates_add` — the
    old constant ρ, recorded as ruled out by both new fields. Axiom-free.

    NUMBERED RESULTS, under the reviewer's amended guard:
      · THEOREM 10's original evidence (§13) re-establishes on its own repaired
        witness — in addition to (x)'s re-establishment on a legal one.
      · THEOREM 13 re-establishes DIRECTLY on the repaired `Xbad`: a genuine
        point mass of 1 still breaks normalization against `one = 10`, and that
        is all its refutation reads. The reviewer's expectation — that it would
        survive via Theorem 14 — did not apply. Theorem 14 refutes a different
        statement and builds no `Substrate`: zero occurrences in the signature
        of `Theorem7_faithful`, confirmed by Lean's own type for it. Theorem 14
        is untouched by (xi).
      · No result depended on ρ NOT being additive. Outcome (B) did not occur.

    (d) CHOICE, as predicted. `pushMass_additive_intrinsic` — additivity now
    DERIVED from the structure's own `rho_add` rather than supplied — is
    choice-free, `[propext, Quot.sound]`. Every repaired witness, and every
    theorem resting on one, now carries `Classical.choice`: Theorem 13's
    refutation moves from `[propext, Quot.sound]` to `[propext, Classical.choice,
    Quot.sound]`, and §13's originals, which were nearly axiom-free, likewise.
    The price of honest measures, a fourth time.

    A MISFIRE OF MINE, recorded. The §30.1 addendum asserted that
    `Theorem7_faithful` builds no `Substrate`, and was committed BEFORE the check
    meant to support it. That check then reported nine occurrences — because its
    range, bounded by an indentation pattern that never matched, ran from the
    signature to the end of the file. Re-run, bounded by the signature itself and
    by Lean's own `#check`, it finds none, so the addendum stands. But a reading
    committed ahead of its evidence, and a check failing silently in a new way,
    both belong in the record: the second guard to misfire through a
    text-matching shortcut, after the prefix-match of §22.

    THE INVARIANT OF THIS COMMIT, stated rather than implied, and checked
    mechanically against 277b2cf: NO THEOREM STATEMENT'S TEXT CHANGED —
    129 theorems compared, none differ, none removed. What changed:
    witnesses (`X0`, `Xbad`, `XG`, `XU`, plus the `noncomputable` marks their
    repair forced), and the PROOF of 1 theorem(s): `occBad_ergodic`. A
    signature-extension commit is judged by that line. One precision the
    textual check cannot see: statements that quantify over `Substrate` now
    range over the NARROWER class of measure-substrates. A universal over that
    class is weaker than before and a refutation of one is STRONGER; every such
    statement in the file still holds, and Theorem 13's refutation is the one
    whose content grew while its text did not.

    ORIENTATION, noted. With `add` law-free, `rho_add` is oriented:
    ρ(A ∪ B) = add (ρ A) (ρ B), with A first. Adding no law that nobody uses is
    correct; but the first proof that needs ρ(A ∪ B) = ρ(B ∪ A) will need
    commutativity, and it must arrive as a logged law with that theorem's name
    attached, as the (xi) pre-registration requires.

    THE REVIEWER'S PRIOR, scored at the reviewer's request: WRONG. It expected
    Theorem 13 to survive via Theorem 14, conflating two refuted statements
    because both refute the same manuscript theorem — Theorem 13 refutes the
    first transcription, Theorem 14 the faithful one. Lean's own type for
    `Theorem7_faithful` settled it. -/

/-! ## 32. Target (xii) — PRE-REGISTRATION: Problem 26, the bridging law

    Drafted FROM THE FILE'S CLOSURE, ruled by the reviewer (2026-09-10), and
    committed before any code. From here on, pre-registrations are drafted this
    way: from the record's dependency graph, not from recall of the exchange.

    ENUMERATION, at kernel-term level. The file was compiled to a module, and a
    meta command walked the constants each theorem's TYPE and PROOF actually
    contain, transitively, classifying each statement after unfolding
    definitions. 236 theorems; 14 reach the aggregation family
    {`Joined.induced`, `Aggregator`, `Joined.clearsAt`}: §13's `S_ex_holds`,
    `S_all_holds`, `G_holds` (EXISTENTIAL), `A_fails`, `D_fails` (REFUTATION),
    `clears_false`, `qfalse_agrees`; and §29's seven legal versions. None from
    §8, none from §27, none elsewhere.

    FINDING — ZERO theorems reach `Lattice.P`. Definition 1's emergence
    potential, as the frame carries it, has never been the subject of a theorem.
    Whatever (xii-a) proves about it is the first.

    FINDING, AND A PRACTICE. The enumeration was first attempted by a regex over
    the source. It returned 85 dependents — polluted by §12's single-letter
    constants `A`, `D`, `G` matching every bound variable of the same name,
    `∀ A B` inside `Substrate` included — and read existentials hidden behind
    definitions as universals. It was discarded before use. From now on,
    enumerations over the record are done at kernel-term level. The fifth instance
    of the surface-text pattern, and the first caught before it fed anything.

    MECHANISM. None of the 14 uses a property of any aggregator: `S_all` ranges
    over every aggregator; `S_ex`, `A` and `G` use a constant aggregator that
    ignores its arguments. Their failures are Theorem 10's.

    THE SPLIT, as ruled. (xii-b) partiality-below: all 14 results belong here.
    BLOCKED on `CostAxioms`, Theorem 10's declared debt — recorded, not
    attempted, not counted against any bridging law. (xii-a) the bridging law
    proper: no existing result; probed below. §8's vocabulary clause: no formal
    referent; Open Problem 33, no probe.

    (xii-a). Candidate: the ρ-weighted conditional expectation, CROSS-MULTIPLIED
    as ruled, so that only multiplication is needed:
      C26(x) :  Defined x → P(x) · ρ(fiber x) = Σ_{s ∈ fiber x} ρ{s} · Psub(s)
    over a legal joined signature with finitely many states. Representation
    items, logged as they arrive: R1 multiplication on values, with laws only as
    a named theorem needs them — the first candidate law, `mul a zero = zero`, is
    what makes the form hold trivially on zero-mass fibers; R2 a finite sum by
    explicit enumeration; R3 no division; R4 point masses from ρ. CONSEQUENCE of
    R3, stated: the cross-multiplied form agrees with the divided one exactly on
    positive-mass fibers and says NOTHING on zero-mass fibers — which is why g2 is
    load-bearing.

    GUARDS. g1: legal witness — A2-conforming, ρ a measure. g2: at least one
    defined x of positive fiber mass. g3′, tightened by the ruling: the
    satisfying and refuting witnesses share ALL lattice data — layer, lattice, R,
    ΔH, S, the lattice's multiplication — and differ ONLY on the substrate side:
    states, Psub, ρ, formulable. Anti-cheat on g3′: the refuting substrate is
    legal and has positive fiber mass at the same defined x, so the failure is a
    mismatch of values and not a zero-mass trivialization. g4: S nonzero at the
    defined points. g5: the lattice side is literally `Lattice.P` —
    Definition 1's form, not a function that happens to equal it.

    THE CEILING, pre-registered. Ruled: do NOT stub R and ΔH, since that would
    invent manuscript content. R (Definition 2) and ΔH (Definition 4) have no
    referents, so the most (A1) can honestly give is CONSISTENCY PLUS
    SUBSTRATE-DISCRIMINATION UNDER FIXED LAYER DATA: with the layer held fixed,
    C26 accepts some substrates and rejects others under the same R·ΔH. Content
    about R and ΔH themselves stays blocked on their referents — a further entry.

    OUTCOMES. (A1), read under g3′: satisfiable non-vacuously, and refutable with
    all lattice data held fixed. (A2): satisfiable only vacuously. (A3):
    unsatisfiable on legal witnesses — a manuscript decision.

    PRIORS. (A1), mine and the reviewer's — agreement, which earns extra
    distrust. The reviewer names g5 as the guard likeliest to bite: "literally
    Definition 1's form" tends to become "a function that happens to equal it"
    during transcription. -/

/-! ## 33. Target (xii-a), run -/
namespace RExii
open Classical
open RE RE4 REgen REamend REp25 REx

/-- (xii-a) The bridging condition C26, cross-multiplied. Representation items:
    `mulX` (R1), the explicit enumeration `univ` (R2), no division (R3), point
    masses from ρ (R4) — and `ι` (R5), FORCED by the signature: the frame keeps
    the lattice's values `Om.Val` and the substrate's values `X.Val` as two
    different types, so the two P's cannot even be compared without an
    identification. The lattice side is `Lattice.P` itself — guard g5. -/
noncomputable def C26 (J : Joined)
    (mulL : J.Om.Val → J.Om.Val → J.Om.Val) (R ΔH : J.L.Rep → J.Om.Val)
    (ι : J.Om.Val → J.X.Val) (mulX : J.X.Val → J.X.Val → J.X.Val)
    (univ : List J.X.State) (x : J.L.Rep) (h : J.Om.Defined x) : Prop :=
  mulX (ι (Lattice.P J.Om mulL R ΔH ⟨x, h⟩)) (J.X.rho (J.fiber x))
    = (univ.map (fun s => if J.formulable s x
                          then mulX (J.X.rho (fun t => t = s)) (J.X.P s) else J.X.zero)).foldr
        J.X.add J.X.zero

/-- THE SHARED LATTICE SIDE (g3′): defined exactly at `true`, with `S` nonzero there
    (g4). Both witnesses use this very lattice. -/
@[reducible] noncomputable def OmN : Lattice L0 where
  Val := Nat
  zero := 0
  lt := fun a b => a < b
  Defined := fun b => b = true
  S := fun _ => 1

/-- THE SUBSTRATE, as a function of its potential `Pf` ALONE. Satisfying and
    refuting witnesses are this one construction at two arguments, so g3′ — differ
    only on the substrate side — holds by construction, not by care. ρ is the
    measure (50, 50, 0), a genuine measure under (xi)'s fields. -/
@[reducible] noncomputable def XS (Pf : S3 → Nat) : Substrate where
  State := S3
  Val := Nat
  zero := 0
  one := 100
  lt := fun a b => a < b
  sub := fun a b => a - b
  add := fun a b => a + b
  P := Pf
  basin := fun _ => True
  rho := fun B => (if B S3.s1 then 50 else 0) + (if B S3.s2 then 50 else 0)
  rho_basin_pos := by show (0:Nat) < _; simp
  rho_empty := by simp
  rho_add := by
    intro A B hdis
    have h1 := hdis S3.s1; have h2 := hdis S3.s2
    by_cases a1 : A S3.s1 <;> by_cases b1 : B S3.s1 <;> by_cases a2 : A S3.s2 <;>
      by_cases b2 : B S3.s2 <;> simp_all

@[reducible] noncomputable def JS (Pf : S3 → Nat) : Joined where
  L := L0
  X := XS Pf
  formulable := fun s x => match s with
    | S3.s1 => x = true
    | S3.s2 => x = true
    | S3.s3 => x = false
  Om := OmN

/-- Shared lattice data, fixed across both witnesses: R = 2, ΔH = 3, and the
    lattice's multiplication. -/
def mulN : Nat → Nat → Nat := fun a b => a * b
def R2 : Bool → Nat := fun _ => 2
def D3 : Bool → Nat := fun _ => 3
def u3s : List S3 := [S3.s1, S3.s2, S3.s3]

/-- The satisfying potential, and the refuting one — differing at `s₂` only. -/
def Psat : S3 → Nat := fun _ => 6
def Pref : S3 → Nat := fun s => match s with
  | S3.s1 => 6
  | S3.s2 => 0
  | S3.s3 => 0

/-- g1: both witnesses are legal — the relation conforms to A2 for EVERY `Pf`. -/
theorem legal_JS (Pf : S3 → Nat) : Legal (JS Pf) := by
  refine ⟨?_, ?_, ?_⟩
  · intro s x y hx hy; cases s <;> (simp only [JS] at hx hy; rw [hx, hy])
  · intro s; cases s
    · exact ⟨true, rfl⟩
    · exact ⟨true, rfl⟩
    · exact ⟨false, rfl⟩
  · intro x; cases x
    · exact ⟨S3.s3, rfl⟩
    · exact ⟨S3.s1, rfl⟩

/-- g2 and the anti-cheat on g3′: the fiber of the defined point `true` has
    POSITIVE mass, 100, on BOTH witnesses. -/
theorem fiber_mass_pos (Pf : S3 → Nat) : (JS Pf).X.rho ((JS Pf).fiber true) = 100 := by
  simp [JS, XS, Joined.fiber]

/-- g4: `S` is nonzero at the defined point. -/
theorem S_nonzero : OmN.S ⟨true, rfl⟩ ≠ 0 := by decide

/-- g3′: the two witnesses share the layer and the lattice exactly. -/
theorem shared_lattice_data : (JS Psat).L = (JS Pref).L ∧ (JS Psat).Om = (JS Pref).Om :=
  ⟨rfl, rfl⟩

/-- …and differ on the substrate's potential. -/
theorem substrates_differ : (JS Psat).X.P S3.s2 ≠ (JS Pref).X.P S3.s2 := by decide

/-- C26 HOLDS on the satisfying substrate: 6 · 100 = 50·6 + 50·6. -/
theorem c26_sat : C26 (JS Psat) mulN R2 D3 (fun v => v) mulN u3s true rfl := by
  simp [C26, Lattice.P, JS, XS, OmN, Joined.fiber, mulN, R2, D3, u3s, Psat]

/-- C26 FAILS on the refuting substrate under the SAME lattice data: 600 against
    50·6 + 50·0 = 300. -/
theorem c26_ref_fails : ¬ C26 (JS Pref) mulN R2 D3 (fun v => v) mulN u3s true rfl := by
  simp [C26, Lattice.P, JS, XS, OmN, Joined.fiber, mulN, R2, D3, u3s, Pref]

/-- (A1) under g3′: with the layer held fixed, C26 accepts one substrate and
    rejects another. -/
theorem A1_substrate_discrimination :
    C26 (JS Psat) mulN R2 D3 (fun v => v) mulN u3s true rfl ∧
    ¬ C26 (JS Pref) mulN R2 D3 (fun v => v) mulN u3s true rfl :=
  ⟨c26_sat, c26_ref_fails⟩

end RExii

/-! ### 33.1 Readout — target (xii-a)

    OUTCOME: (A1), read under g3′. With ALL lattice data held fixed — layer `L0`,
    lattice `OmN`, R = 2, ΔH = 3, S = 1, the lattice's multiplication — C26
    ACCEPTS one substrate (`c26_sat`) and REJECTS another (`c26_ref_fails`),
    together `A1_substrate_discrimination`. The two substrates are one
    construction, `XS`, at two potentials, so they differ on the substrate side
    and nowhere else by construction. What the law says, on this evidence:
    Definition 1's potential at a defined structure is the stationary-weighted
    average of the substrate potential over the states that formulate it. It
    accepts the substrate whose average is 6 and rejects the one whose average is 3.

    GUARDS, each with its witness. g1 `legal_JS` (A2-conforming for every
    potential; ρ a measure under (xi)). g2 and the anti-cheat on g3′
    `fiber_mass_pos`: the fiber of `true` has mass 100 on BOTH witnesses, so the
    refutation is a mismatch of values, not a zero-mass trivialization. g3′
    `shared_lattice_data` and `substrates_differ`. g4 `S_nonzero`. g5 CHECKED AT
    KERNEL-TERM LEVEL rather than asserted: C26's own definition body contains
    `RE.Lattice.P`, so the lattice side is literally Definition 1's form. The guard
    the reviewer named as likeliest to bite did not.

    FINDING — THE FIRST THEOREMS ABOUT DEFINITION 1's POTENTIAL. A kernel-term
    search finds exactly three theorems reaching `Lattice.P`: `c26_sat`,
    `c26_ref_fails` and `A1_substrate_discrimination`. (It also lists two
    equation lemmas Lean generated while unfolding `Lattice.P` and `C26`; they are
    the proof assistant's, not the record's, and are not counted.) Before this run
    the number was zero.

    FINDING — R5 WAS FORCED BY THE SIGNATURE. The frame stores the lattice's
    values and the substrate's values as two different types, so the two P's
    cannot even be compared without an identification `ι`. On the witness both
    are ℕ and `ι` is the identity; in general it is a representation item, and it
    is one more thing the shared letter P had been hiding.

    R1, as logged: no law of multiplication is used by any theorem here — the
    witnesses use ℕ's. `mul a zero = zero`, the law that makes the cross-multiplied
    form hold trivially on zero-mass fibers, was not needed: no defined point of
    zero fiber mass occurs.

    THE CEILING, as pre-registered: consistency plus substrate-discrimination
    under fixed layer data. Content about R and ΔH themselves stays blocked on
    their referents, now Open Problem 34. The witnesses carry
    `Classical.choice`, through the substrate's genuine measure, as expected.

    PRIORS. (A1) — mine and the reviewer's, and it landed. Agreement earned extra
    distrust, and the guard chosen to absorb it (g5) was checked mechanically
    rather than taken on trust.

    A FAILURE IN THIS RUN'S OWN COMMIT CHAIN, recorded. The first commit of this
    section, 48efe23 — never merged, pushed or reported — carried the Lean half
    only. The step that wrote the manuscript half stopped on a failed assertion:
    its anchor put the italic mark after "The" where the manuscript has it
    before, a surface-text mismatch in my own markup. But the chain around it had
    no stop-on-failure, so it went on to verify, audit, compile and commit, and
    the commit message named manuscript changes that were not in it. The
    assertion worked; the chain did not honour it. Caught before anything was
    reported and amended into this commit, whose chain now aborts on any failed
    step. A second slip inside the first: I diagnosed the wrong assertion before
    counting which line had failed — a conclusion ahead of its check, harmless
    only because the next check caught it.

    READOUT NOTES, at the reviewer's request. (1) The satisfying substrate is the
    CONSTANT potential equal to the layer's value — the weakest possible way to
    satisfy C26, and exactly what the ceiling predicted. Read `c26_sat` as
    consistency and nothing more; the content is in the PAIR, not in either
    witness. (2) The identification ι is the sixth thing the shared letter P was
    hiding; the six are listed together under Problem 26. (3) The two slips above
    are one lesson — the order-of-operations entry recorded at (xi) — now at two
    instances, and folded into that entry rather than opened anew. -/

