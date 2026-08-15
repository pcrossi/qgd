#!/usr/bin/env python3
"""
Chapter 4 — torsion--Reynolds closure of the electromagnetic sector.

Classification:
    Symbolic-numerical evaluation of a constitutive chain.

Verifies:

    Re_Q = n_B^2/(12*pi^2*R^4) = alpha

and the radial stationary condition

    x^3 - 4*tau*x^2 + tau*n_B^2/pi^2 = 0, x=R^2.

The result is dimensionless. Conversion to physical energy belongs to
global metrological calibration.
"""

from __future__ import annotations

import math
from pathlib import Path


def solve(alpha: float, n_b: int = 1) -> dict[str, float]:
    if not (0.0 < alpha < 1.0 / 3.0):
        raise ValueError("positive solution requires 0<alpha<1/3")
    x = abs(n_b) / (math.sqrt(12.0) * math.pi * math.sqrt(alpha))
    radius = math.sqrt(x)
    tau = x**3 / (4.0 * x**2 - n_b * n_b / math.pi**2)
    reynolds = n_b * n_b / (12.0 * math.pi**2 * radius**4)
    residual = x**3 - 4.0 * tau * x**2 + tau * n_b * n_b / math.pi**2
    return {
        "alpha": alpha,
        "radius": radius,
        "tau": tau,
        "lambda_hat": 1.0 / math.sqrt(tau),
        "length_hat": math.pi * math.sqrt(tau),
        "reynolds": reynolds,
        "residual": residual,
    }


def main() -> None:
    scenarios = [
        ("low energy — $1/137$ approximation", 1.0 / 137.0),
        ("external metrological reference", 1.0 / 137.035999084),
        ("high energy effective benchmark — $1/128$", 1.0 / 128.0),
    ]
    rows = [(name, solve(alpha)) for name, alpha in scenarios]
    lines = [
        "---",
        'title: "Output — torsion-Reynolds closure"',
        "---",
        "",
        "# Output — torsion--Reynolds closure",
        "",
        "| scenario | $\\alpha$ | $R$ | $\\tau_{\\rm EM}$ | $\\widehat\\Lambda_{\\rm EM}$ | $L/\\ell_C$ | residual |",
        "|:---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, row in rows:
        lines.append(
            f"| {name} | `{row['alpha']:.15e}` | `{row['radius']:.12f}` | "
            f"`{row['tau']:.12f}` | `{row['lambda_hat']:.12f}` | "
            f"`{row['length_hat']:.12f}` | `{row['residual']:.3e}` |"
        )
    lines += [
        "",
        "Each row numerically satisfies:",
        "",
        "$$",
        "\\operatorname{Re}_{\\rm Q}=\\alpha,",
        "\\qquad",
        "x^3-4\\tau x^2+\\frac{\\tau n_B^2}{\\pi^2}=0.",
        "$$",
        "",
        "The $1/128$ row is a high energy effective benchmark, not a fundamental",
        "input of the low energy closure.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_reynolds_torsion_closure.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
