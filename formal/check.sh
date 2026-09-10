#!/usr/bin/env sh
# Guard for BoundaryResidue.lean §2: the frame must stay constructive.
#
# The absence of a `Decidable` instance cannot enforce Definition 17 — a reader
# who adds `open Classical` to make something compute deletes the distinction
# silently. What is NOT silent is the axiom report: anything touching
# `Classical.propDecidable` pulls in [propext, Classical.choice, Quot.sound].
#
# So the invariant is: the six frame definitions below report axiom-free. That
# is ALL this script checks. It does not audit the rest of the file, where
# classical choice enters deliberately through declared representation choices
# (item 15 onward), and it does not count `sorry` sites — those are named in the
# file's compilation record, which is the authority on them. Not wired to CI;
# run it by hand after editing the file.
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
echo "OK: the six frame definitions are axiom-free. (sorry sites: see the compilation record.)"
