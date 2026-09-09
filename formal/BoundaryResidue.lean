/-
  BoundaryResidue.lean
  Representation skeleton for Appendix M: Definition 17 (boundary object),
  Conjecture 7 (boundary residue), Open Problems 21, 22, 25.

  WHAT THIS IS
    A record of representation choices. Each choice is annotated with the open
    problem it decides. The payload is the annotations, not the theorems.

  WHAT THIS IS NOT
    It proves nothing. There is no result here that was not already assumed.
    Every `sorry` marks a CONJECTURE — a statement the manuscript asserts and
    has not derived — never an omitted routine step. If a `sorry` here is ever
    discharged, that is a mathematical event and belongs in M.8, not in a
    refactor.

  NOT COMPILED. Written without a Lean toolchain available. Syntax is
    unverified; the structural claims in the comments do not depend on it, but
    any claim of the form "Lean forces X" that is marked (unverified) below
    is reasoning about Lean's rules, not an observation of its behavior.

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

/-- A method the layer can actually afford to run. -/
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
    layer cannot form the comparison that would admit or forbid it. -/
def Lattice.clears {L : Layer} (Ω : Lattice L)
    (mul : Ω.Val → Ω.Val → Ω.Val) (R ΔH : L.Rep → Ω.Val) (θ : Ω.Val)
    (x : { y : L.Rep // Ω.Defined y }) : Prop :=
  Ω.lt θ (Ω.P mul R ΔH x)

/-! ## 2. Why "no `Decidable` instance" cannot carry the claim

    The tempting move is to omit `instance : Decidable (Ω.Defined x)` and let
    that absence mean "the layer cannot decide". It does not mean that.

    (unverified, but a fact about Lean's foundations rather than its elaborator)
    `Classical.dec p : Decidable p` is available as a TERM for every `p : Prop`,
    and `open Classical` promotes it to an instance. Absence of an instance is a
    fact about instance resolution in one file — a namespace accident, revocable
    by an import. It is not a mathematical statement, and a reader who adds
    `open Classical` to make something compute has silently deleted Definition 17.

    THIS IS PROBLEM 22 TALKING, and the skeleton records it instead of yielding:
    the layer's inability must be a QUANTIFIED CLAIM over the layer's own
    internalized methods, not a gap in the ambient logic.
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
    a measure is the substance of Problem 25, not a detail of its statement. -/
def Broad (L : Layer) (large : (L.Rep → Prop) → Prop) (p : L.Rep → Prop) : Prop :=
  large p

/-! ## 4. The two mechanisms, as instances of one frame -/

/-- Diagonal (Theorem 8 (i)). Needs `encode` and nothing else. -/
theorem diagonal_boundary_object (L : Layer) (Ω : Lattice L) :
    ∃ x : L.Rep, ¬ Ω.Defined x ∧ L.undecidable (fun y => y = x) := by
  sorry -- CONJECTURE: this is Theorem 8 (i) transposed. Unconditional in the
        -- manuscript; the transposition to `Layer.undecidable` is not proved.

/-- Opacity (Razborov–Rudich, transposed). Needs largeness AND a hardness
    hypothesis. The extra hypothesis is not decoration: it is what makes this
    mechanism conditional where the diagonal one is not (ch2 §2.11.3). -/
theorem opacity_boundary_object (L : Layer) (Ω : Lattice L)
    (large : (L.Rep → Prop) → Prop)
    (hard : ∃ x : L.Rep, L.incompressible x) :
    ∀ p : L.Rep → Prop, Broad L large p →
      (∀ m : L.Method, L.available m → ¬ (∀ x, L.run m x = true ↔ p x)) := by
  sorry -- CONJECTURE: Conjecture 7 (b), opacity route. The manuscript asserts
        -- this; nothing here derives it. Note `hard` is a HYPOTHESIS, matching
        -- "conditional on cryptographic hardness" in the instance table.

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

    DISCRIMINATOR (pending, cheap). Formalize Theorem 7's ergodic search in this
    same skeleton and inspect the measure it needs. If it is a measure on `Rep` —
    same type, same carrier as `large` — the ingredient is one thing appearing in
    both columns and re-entry gains standing. If it is a measure on states rather
    than on representations, the mechanisms are siblings sharing only the frame,
    and the remark resolves toward nothing. Settleable by construction.
-/

end RE
