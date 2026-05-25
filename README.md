# Claim-Checking Trace Lab

This is a greenfield proof artifact for Rahim's current thesis:

> Rahim builds AI systems that help generate, test, and verify new scientific ideas.

The goal is to make one generate/test/verify loop inspectable from the first click.

## What This Lab Does

It captures a small trace:

```txt
claim -> check plan -> executable or inspectable check -> result -> limits -> next step
```

The first trace does not need to be grand. It needs to be real, bounded, and easy for a serious technical reader to inspect.

## Trace Contract

Every trace must include:

- the claim being checked
- why the claim matters
- the check plan
- commands, proof target, simulation, or manual verification method
- raw result or linked output
- limits and failure modes
- next step

## First Target

Start with `traces/001/`.

Trace 001 checks one small Kerr-geometry claim:

```txt
AI-selected claim
-> numeric sanity check against sample Kerr parameters
-> Lean proof check in KerrFormalization
-> explicit limits and next step
```

Run it with:

```bash
python3 scripts/run_trace_001.py
```

Use `KerrFormalization`, `OpenAtoms`, or `aristotle_new_orchestrator` only if they make the trace clearer. If they add friction, keep the first trace small and self-contained, then link outward.

## Success Criteria

- A reader understands the trace in under 10 minutes.
- The trace can be inspected without private context.
- The trace raises a core profile claim toward E3 evidence.
- `profile.md` can link to the result only after the trace exists.
