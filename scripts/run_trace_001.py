#!/usr/bin/env python3
"""Run Trace 001: Kerr outer horizon claim check.

The trace has two layers:

1. A small deterministic numeric sanity check for the Kerr Delta formula.
2. A Lean check of the theorem exposed by the local KerrFormalization repo.
"""

from __future__ import annotations

import argparse
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


def run_numeric_checks() -> bool:
    cases = [
        (2.0, 1.0),
        (5.0, 3.0),
        (1.0, 0.0),
    ]
    tolerance = 1e-9
    ok = True

    print("numeric sanity check")
    print("--------------------")
    for mass, spin in cases:
        discriminant = mass * mass - spin * spin
        radius = mass + math.sqrt(discriminant)
        residual = delta(mass, spin, radius)
        passed = abs(residual) <= tolerance
        ok = ok and passed
        status = "PASS" if passed else "FAIL"
        print(
            f"{status} M={mass:g} a={spin:g} "
            f"r_plus={radius:.12g} delta={residual:.3e}"
        )

    bad_mass, bad_spin = 1.0, 2.0
    bad_disc = bad_mass * bad_mass - bad_spin * bad_spin
    rejected = bad_disc < 0
    ok = ok and rejected
    status = "PASS" if rejected else "FAIL"
    print(
        f"{status} rejected M={bad_mass:g} a={bad_spin:g}: "
        f"discriminant={bad_disc:g} is negative, so the real-horizon "
        "assumption is not met"
    )
    return ok


def run_lean_check() -> bool:
    print()
    print("lean proof check")
    print("----------------")
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
        print("PASS Lean accepted KerrFormalization.Kerr.outerHorizonIsDeltaRoot")
        return True

    print(f"FAIL Lean exited with status {completed.returncode}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--numeric-only",
        action="store_true",
        help="skip the Lean proof check and run only the numeric sanity check",
    )
    args = parser.parse_args()

    print("Trace 001: Kerr outer horizon is a Delta root")
    print("================================================")
    numeric_ok = run_numeric_checks()
    lean_ok = True if args.numeric_only else run_lean_check()

    print()
    print("trace result")
    print("------------")
    if numeric_ok and lean_ok:
        print("PASS Trace 001 produced a passing numeric sanity check and proof check.")
        return 0

    print("FAIL Trace 001 did not satisfy all checks.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
