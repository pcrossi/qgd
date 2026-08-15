#!/usr/bin/env python3
"""
GDQ — Chapter 15 / Rosen--Morse Benchmark

Objective:
    Record the Rosen--Morse route as an auxiliary benchmark, not as the ontology
    of the hierarchy. The script reproduces the reduced spectral structure used
    in the history, but the chapter does not use n_tau=17 as a physical index.

Classification:
    Auxiliary numerical benchmark.

Output:
    scripts/output_rosen_morse_benchmark.md
"""

from __future__ import annotations

import math
from pathlib import Path


def eigenvalue(n: int, s: float, b: float) -> float:
    x = s + n
    return x * x - b * b / (x * x)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_rosen_morse_benchmark.md"

    alpha_inv = 137.03599907
    alpha = 1.0 / alpha_inv
    epsilon = 5.0 * alpha / math.pi
    delta_epsilon = (4.0 / 9.0) * alpha * alpha - (math.pi / 2.0) * alpha**3
    s = epsilon - delta_epsilon
    b = (alpha / (20.0 * math.pi)) * (
        1.0 + (1.5 - (4.0 / 15.0) * alpha) * alpha * math.log(1.0 / epsilon)
    )

    lambdas = {n: eigenvalue(n, s, b) for n in [0, 1, 17]}
    r_mu = math.sqrt(lambdas[1] / lambdas[0])
    r_tau = math.sqrt(lambdas[17] / lambdas[0])

    text = f"""# Output — Rosen-Morse benchmark

Classification: auxiliary numerical benchmark; not hierarchy ontology.

| parameter | value |
|---|---:|
| s | {s:.12e} |
| b | {b:.12e} |
| lambda_0 | {lambdas[0]:.12e} |
| lambda_1 | {lambdas[1]:.12e} |
| lambda_17 | {lambdas[17]:.12e} |
| sqrt(lambda_1/lambda_0) | {r_mu:.12f} |
| sqrt(lambda_17/lambda_0) | {r_tau:.12f} |

Interpretation: the benchmark shows spectral coherence of the auxiliary operator.
It should not be read as proof that tau is the physical $n=17$ mode of GDQ.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
