#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `positive signal benchmark` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / Positive benchmark of the signal problem.

Records the final/reduced numbers of the benchmark of the signal problem without re-executing the complete
historical chain. Classification: reduced benchmark, not a general proof.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_positive_signal_benchmark.md"

    exact = -0.1698717343244
    mc = -0.16836
    stderr = 6.296327845454e-4
    z = (mc - exact) / stderr
    acceptance = 0.75515
    n_conf = 65536

    text = f"""# Output — positive benchmark of the signal problem

Classification: reduced benchmark; not a general algorithmic proof.

| quantity | value |
|---|---:|
| exact configurations | {n_conf} |
| exact C_s(1) | {exact:.15e} |
| MC C_s(1) | {mc:.15e} |
| MC stderr | {stderr:.15e} |
| internal z | {z:.6f} |
| acceptance | {acceptance:.12f} |

Interpretation: the measure is positive and the antiferromagnetic correlation appears
by circulation/holonomy, not by negative weight.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
