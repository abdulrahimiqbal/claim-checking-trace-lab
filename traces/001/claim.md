# Trace 001: Kerr Outer Horizon Claim

## Claim

For Kerr parameters `M` and `a` satisfying `0 <= M^2 - a^2`, the outer
horizon radius

```txt
r_+ = M + sqrt(M^2 - a^2)
```

is a root of the Kerr Delta function

```txt
Delta(r) = r^2 - 2 M r + a^2
```

so:

```txt
Delta(r_+) = 0
```

## Why It Matters

This is intentionally small. It demonstrates the profile loop in a form a
technical reader can inspect quickly:

```txt
generate/select a scientific claim
-> test it with deterministic examples
-> verify the exact statement in Lean
-> record the proof boundary
```

The claim is recognizable to readers with general relativity context, but the
check is bounded enough to avoid overclaiming about the whole Kerr
formalization.

## Source

- Generated/refined by: Codex from the current profile goal: make one
  generate/test/verify trace inspectable.
- Selected from: the local `KerrFormalization` proof surface.
- Related artifact:
  `../KerrFormalization/KerrFormalization/Kerr/Validation.lean`, theorem
  `KerrFormalization.Kerr.outerHorizonIsDeltaRoot`.

## Evidence Level Target

Current: E2
Target: E3
