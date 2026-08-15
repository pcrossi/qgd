#!/usr/bin/env python3
"""
GDQ — Chapter 01 / Reduced Verification

Goal:
    Numerically compare the modulus structure of free Wiener and Feynman kernels
    in one dimension, showing why the Wiener integral defines a positive measure
    while the Feynman integral is oscillatory.

Theoretical source:
    manuscript/01_initial_problem/

Classification:
    Pedagogical consistency test. Not a physical prediction.

Equation:
    K_W(x,t)=(4*pi*D*t)^(-1/2)*exp(-x^2/(4Dt)).
    K_F(x,t)=(m/(2*pi*i*hbar*t))^(1/2)*exp(i*m*x^2/(2*hbar*t)).

Domain and boundary:
    Real line numerically truncated at [-L,L], without physical boundary; the cutoff
    is purely numerical.

Parameters:
    Reduced universal:
        hbar=m=D=t=1.
    Numerical:
        L=8, N=20001.
    Experimental data:
        None.

Output:
    manuscript/01_initial_problem/scripts/output_compare_wiener_feynman_kernel.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "manuscript/01_initial_problem/scripts/output_compare_wiener_feynman_kernel.md"


def main() -> None:
    hbar = m = D = t = 1.0
    L = 8.0
    N = 20_001
    x = np.linspace(-L, L, N)

    K_w = (4.0 * np.pi * D * t) ** -0.5 * np.exp(-(x**2) / (4.0 * D * t))
    K_f = (m / (2.0 * np.pi * hbar * t)) ** 0.5 * np.exp(1j * m * x**2 / (2.0 * hbar * t))

    mass_w = np.trapezoid(K_w, x)
    abs_mass_f = np.trapezoid(np.abs(K_f), x)
    osc_int_f = np.trapezoid(K_f, x)

    lines = [
        "---",
        'title: "Output — Wiener/Feynman comparison"',
        "---",
        "",
        "# Output — Wiener/Feynman comparison",
        "",
        "| Quantity | Value | Interpretation |",
        "|---|---:|---|",
        f"| Truncated Wiener integral | {mass_w:.12f} | approximates positive unit mass |",
        f"| Integral of Feynman modulus | {abs_mass_f:.12f} | grows with cutoff size; not a probability measure |",
        f"| Oscillatory Feynman integral, real part | {osc_int_f.real:.12f} | phase cancellation |",
        f"| Oscillatory Feynman integral, imaginary part | {osc_int_f.imag:.12f} | phase cancellation |",
        "",
        "Conclusion: the initial difference is not a numerical constant. The Wiener kernel "
        "is positive and normalizable as a measure; the Feynman kernel has an oscillatory "
        "phase and requires interpretation by amplitude, stationary phase, or Wick continuation.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Output: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
