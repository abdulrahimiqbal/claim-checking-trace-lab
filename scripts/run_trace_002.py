#!/usr/bin/env python3
"""Run Trace 002: repair an overbroad Kerr horizon claim."""

from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK_ROOT = ROOT.parent
KERR_REPO = WORK_ROOT / "KerrFormalization"
LEAN_TARGET = "KerrFormalization/Kerr/Validation.lean"


def delta(mass: float, spin: float, radius: float) -> float:
    return radius * radius - 2.0 * mass * radius + spin * spin


def run_failure_case() -> bool:
    mass, spin = 1.0, 2.0
    discriminant = mass * mass - spin * spin
    print("overbroad claim check")
    print("---------------------")
    print(
        "Original claim: for all real M and a, "
        "r_plus = M + sqrt(M^2 - a^2) is a real Delta root."
    )
    print(f"Test case: M={mass:g}, a={spin:g}, discriminant={discriminant:g}")
    if discriminant < 0:
        print("PASS rejected original claim: real sqrt assumption is violated")
        return True
    print("FAIL original claim was not constrained by this test")
    return False


def run_repaired_numeric_check() -> bool:
    mass, spin = 2.0, 1.0
    discriminant = mass * mass - spin * spin
    radius = mass + math.sqrt(discriminant)
    residual = delta(mass, spin, radius)
    passed = abs(residual) <= 1e-9
    print()
    print("repaired claim check")
    print("--------------------")
    print("Repaired claim: if 0 <= M^2 - a^2, then Delta(r_plus) = 0.")
    print(
        f"{'PASS' if passed else 'FAIL'} M={mass:g} a={spin:g} "
        f"r_plus={radius:.12g} delta={residual:.3e}"
    )
    return passed


def run_lean_check() -> bool:
    print()
    print("lean repaired-claim check")
    print("-------------------------")
    if not KERR_REPO.exists():
        print(f"FAIL missing KerrFormalization repo at {KERR_REPO}")
        return False

    command = ["lake", "env", "lean", LEAN_TARGET]
    print(f"$ cd {KERR_REPO}")
    print("$ " + " ".join(command))
    completed = subprocess.run(
        command,
        cwd=KERR_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.stdout.strip():
        print(completed.stdout.rstrip())
    if completed.stderr.strip():
        print(completed.stderr.rstrip())
    if completed.returncode == 0:
        print("PASS Lean accepted the repaired theorem with hdisc assumption")
        return True
    print(f"FAIL Lean exited with status {completed.returncode}")
    return False


def main() -> int:
    print("Trace 002: repair an overbroad Kerr horizon claim")
    print("==================================================")
    ok = run_failure_case()
    ok = run_repaired_numeric_check() and ok
    ok = run_lean_check() and ok

    print()
    print("trace result")
    print("------------")
    if ok:
        print("PASS Trace 002 rejected the overbroad claim and verified the repaired claim.")
        return 0
    print("FAIL Trace 002 did not complete the repair path.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
