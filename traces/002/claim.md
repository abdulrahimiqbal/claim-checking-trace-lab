# Trace 002: Claim Repair

## Original Claim

For all real Kerr parameters `M` and `a`, the outer horizon expression

```txt
r_+ = M + sqrt(M^2 - a^2)
```

is a real root of the Kerr Delta function.

## Why It Is Too Broad

The claim hides an assumption. The expression `sqrt(M^2 - a^2)` is a real
horizon expression only when:

```txt
0 <= M^2 - a^2
```

For example, `M = 1` and `a = 2` gives discriminant `-3`, so the original
real-valued claim is not well-formed as a universal real-horizon statement.

## Repaired Claim

For Kerr parameters `M` and `a` satisfying `0 <= M^2 - a^2`, the outer horizon
radius `r_+ = M + sqrt(M^2 - a^2)` is a root of `Delta`.

## Evidence Level Target

Current: E2
Target: E3
