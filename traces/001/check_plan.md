# Trace 001: Check Plan

## Check Shape

Hybrid:

- deterministic numeric sanity check
- formal Lean proof-status check

## Inputs

- Input files:
  - `scripts/run_trace_001.py`
  - `../KerrFormalization/KerrFormalization/Kerr/Validation.lean`
  - `../KerrFormalization/KerrFormalization/Kerr/Horizons.lean`
- Parameters:
  - numeric examples: `(M, a) = (2, 1), (5, 3), (1, 0)`
  - rejected example: `(M, a) = (1, 2)`
- Assumptions:
  - The real-horizon claim requires `0 <= M^2 - a^2`.
  - Lean and Lake are available for the formal proof check.

## Method

```txt
step 1: compute r_+ = M + sqrt(M^2 - a^2) for sample admissible parameters
step 2: evaluate Delta(r_+) and require numerical residual near zero
step 3: reject a sample parameter set with negative discriminant
step 4: run `lake env lean KerrFormalization/Kerr/Validation.lean`
step 5: interpret Lean success as acceptance of the exact theorem facade
```

## Pass / Fail Criteria

- Pass: all admissible numeric examples produce near-zero residuals, the
  negative-discriminant case is rejected, and Lean exits successfully.
- Fail: any numeric residual exceeds tolerance, the bad assumption is accepted,
  or Lean reports an error.
- Ambiguous: Lean is unavailable locally. In that case, the numeric layer can
  pass, but the trace has not reached the formal E3 target.
