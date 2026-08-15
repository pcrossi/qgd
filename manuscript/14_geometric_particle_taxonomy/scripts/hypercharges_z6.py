#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Hypercharges by Z6 and anomalies

Objective:
    Verify the Diophantine search for integer hypercharges y=6Y.

Tested construction:
    1. The global quotient imposes modulo 6 congruences.
    2. Anomalies impose four integer equations.
    3. Primitivity selects the minimal solution.

Classification:
    Exact symbolic-numerical verification. Not an experimental fitting.

Output:
    scripts/output_hypercharges_z6.md
"""

from __future__ import annotations

from math import gcd
from pathlib import Path


def primitive(values: tuple[int, ...]) -> bool:
    """Return True when the integer charge vector has no common divisor."""

    divisor = 0
    for value in values:
        divisor = gcd(divisor, abs(value))
    return divisor == 1


def anomaly_free(q: int, u: int, d: int, ell: int, e: int) -> bool:
    """Check the four anomaly cancellation equations for one generation."""

    return (
        2 * q + u + d == 0
        and 3 * q + ell == 0
        and 6 * q + 3 * u + 3 * d + 2 * ell + e == 0
        and 6 * q**3 + 3 * u**3 + 3 * d**3 + 2 * ell**3 + e**3 == 0
    )


def quotient_allowed(q: int, u: int, d: int, ell: int, e: int) -> bool:
    """Check the Z6 descent congruences for the five multiplets."""

    return (
        q % 6 == 1
        and u % 6 == 2
        and d % 6 == 2
        and ell % 6 == 3
        and e % 6 == 0
    )


def search(bound: int = 42) -> list[tuple[int, int, int, int, int]]:
    """Search all primitive solutions within an integer box."""

    solutions: list[tuple[int, int, int, int, int]] = []
    for q in range(-bound, bound + 1):
        if q % 6 != 1:
            continue
        ell = -3 * q
        e = 6 * q
        if max(abs(ell), abs(e)) > bound:
            continue
        for u in range(-bound, bound + 1):
            d = -2 * q - u
            values = (q, u, d, ell, e)
            if max(map(abs, values)) > bound:
                continue
            if quotient_allowed(*values) and anomaly_free(*values) and primitive(values):
                solutions.append(values)
    return sorted(set(solutions))


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_hypercharges_z6.md"
    bound = 42
    solutions = search(bound)

    rows = "\n".join(
        f"| {q} | {u} | {d} | {ell} | {e} | "
        f"{q/6:.12g} | {u/6:.12g} | {d/6:.12g} | {ell/6:.12g} | {e/6:.12g} |"
        for q, u, d, ell, e in solutions
    )

    text = f"""# Output — hypercharges by Z6

Classification: exact symbolic-numerical verification.

Searched range:

$$
|y_i|\\le {bound}.
$$

| q | u | d | ell | e | Y_Q | Y_uc | Y_dc | Y_L | Y_ec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{rows}

Number of primitive solutions found: {len(solutions)}.

Interpretation: the minimal oriented solution contains

$$
(q,u,d,\\ell,e)=(1,-4,2,-3,6),
$$

that is,

$$
(Y_Q,Y_{{u^c}},Y_{{d^c}},Y_L,Y_{{e^c}})
=
\\left(\\frac16,-\\frac23,\\frac13,-\\frac12,1\\right).
$$

The other solutions within the box represent the swapping of the color singlets or
equivalent orientations allowed by the global choice.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
