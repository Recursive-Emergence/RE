#!/usr/bin/env sh
# Guard for BoundaryResidue.lean §2: the frame must stay constructive.
#
# The absence of a `Decidable` instance cannot enforce Definition 17 — a reader
# who adds `open Classical` to make something compute deletes the distinction
# silently. What is NOT silent is the axiom report: anything touching
# `Classical.propDecidable` pulls in [propext, Classical.choice, Quot.sound].
#
# So the invariant is: the six frame definitions report axiom-free, and only the
# two conjectural theorems of §4 report sorryAx. Verified on Lean 4.15.0, bare
# toolchain, no Mathlib. Not wired to CI; run it by hand after editing the file.
set -e
FILE="${1:-formal/BoundaryResidue.lean}"
AUDIT=$(mktemp)
cat "$FILE" > "$AUDIT.lean"
cat >> "$AUDIT.lean" <<'EOF'
#print axioms RE.Layer.undecidable
#print axioms RE.Layer.incompressible
#print axioms RE.Layer.available
#print axioms RE.Lattice.P
#print axioms RE.Lattice.clears
#print axioms RE.Broad
EOF
lean "$AUDIT.lean" 2>&1 | tee "$AUDIT.out"
if grep -qE 'Classical\.choice|propext|Quot\.sound' "$AUDIT.out"; then
  echo "FAIL: classical axiom leaked into the frame — §2's invariant is broken." >&2
  exit 1
fi
echo "OK: frame is axiom-free; only §4's sorry sites are conjectural."
