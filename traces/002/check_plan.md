# Trace 002: Check Plan

## Check Shape

Claim repair:

```txt
overbroad claim -> attempted check -> failure -> narrowed claim -> final status
```

## Inputs

- Original claim: for all real `M, a`, `r_+` is a real root of `Delta`.
- Source: repair pressure from Trace 001's explicit discriminant assumption.
- Check method:
  - evaluate the hidden assumption on a counterexample parameter set
  - run a repaired numeric check
  - run the Lean facade theorem that includes the missing assumption

## Method

```txt
step 1: state the overbroad claim
step 2: test M = 1, a = 2 and observe M^2 - a^2 < 0
step 3: repair the claim by adding the assumption 0 <= M^2 - a^2
step 4: run a passing numeric example under the repaired assumption
step 5: run `lake env lean KerrFormalization/Kerr/Validation.lean`
```

## Pass / Fail Criteria

- Pass: the trace records a real failed, rejected, or constrained check and a narrower final claim.
- Fail: the trace only presents a polished success case.
- Ambiguous: the check does not clearly constrain the original claim.
