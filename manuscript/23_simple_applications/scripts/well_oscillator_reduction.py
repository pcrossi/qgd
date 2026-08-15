#!/usr/bin/env python3
"""Chapter 23 — reduced verification of ideal well and oscillator.

Objective:
    Verify, in a self-contained script, the two elementary results used
    in the text:

    1. Infinite well in units L=1 and hbar^2/(2mL^2)=1:
       E_n = (n*pi)^2.
    2. Harmonic oscillator in units hbar=m=omega=1:
       E_n = n + 1/2.

Classification:
    Correspondence and numerical consistency test. No experimental data
    enters the calculation. The script is not a complete Hessian of the
    official action; it verifies the reduced Hessian obtained in the flat
    stationary sector.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal


OUT = Path(__file__).with_name("output_well_oscillator_reduction.md")


@dataclass(frozen=True)
class Check:
    name: str
    numerical: np.ndarray
    analytic: np.ndarray

    @property
    def rel_error(self) -> np.ndarray:
        return np.abs(self.numerical - self.analytic) / np.maximum(1.0e-30, np.abs(self.analytic))


def infinite_well_direct(points: int, modes: int) -> Check:
    """Diagonalizes -d^2/dx^2 in (0,1) with Dirichlet at both boundaries."""

    h = 1.0 / (points + 1)
    diagonal = np.full(points, 2.0 / h**2)
    off = np.full(points - 1, -1.0 / h**2)
    numerical = eigh_tridiagonal(
        diagonal,
        off,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    n = np.arange(1, modes + 1, dtype=float)
    analytic = (np.pi * n) ** 2
    return Check("infinite well", numerical, analytic)


def oscillator_direct(points: int, half_width: float, modes: int) -> Check:
    """Diagonalizes -1/2 d^2/dx^2 + x^2/2 in [-A,A] with large A."""

    h = 2.0 * half_width / (points + 1)
    x = -half_width + h * np.arange(1, points + 1)
    diagonal = 1.0 / h**2 + 0.5 * x**2
    off = np.full(points - 1, -0.5 / h**2)
    numerical = eigh_tridiagonal(
        diagonal,
        off,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    n = np.arange(0, modes, dtype=float)
    analytic = n + 0.5
    return Check("harmonic oscillator", numerical, analytic)


def morse_indices(modes: int) -> tuple[list[int], list[int]]:
    """Indices of the reduced Hessian around eigenstates.

    For the well with n=1,2,..., state n has n-1 levels below it.
    For the oscillator with n=0,1,..., state n has n levels below it.
    """

    well = [n - 1 for n in range(1, modes + 1)]
    oscillator = [n for n in range(0, modes)]
    return well, oscillator


def render(checks: list[Check], points_well: int, points_osc: int, half_width: float) -> str:
    lines = [
        "---",
        'title: "Output — Well and Oscillator as Reduction"',
        "---",
        "",
        "# Output — Well and Oscillator as Reduction",
        "",
        "Classification: correspondence test of the flat reduced Hessian.",
        "",
        "## Numerical parameters",
        "",
        f"- well: `{points_well}` internal points, $L=1$, $\\hbar^2/(2mL^2)=1$;",
        f"- oscillator: `{points_osc}` internal points in $[-{half_width:g},{half_width:g}]$, $\\hbar=m=\\omega=1$;",
        "- no experimental value is used.",
        "",
    ]

    for check in checks:
        lines += [
            f"## {check.name}",
            "",
            "| mode | numerical | analytic | relative error |",
            "|---:|---:|---:|---:|",
        ]
        for i, (num, ana, err) in enumerate(zip(check.numerical, check.analytic, check.rel_error)):
            label = i + 1 if check.name == "infinite well" else i
            lines.append(f"| {label} | `{num:.12f}` | `{ana:.12f}` | `{err:.3e}` |")
        lines.append("")

    well_idx, osc_idx = morse_indices(len(checks[0].analytic))
    lines += [
        "## Reduced Morse indices",
        "",
        "| mode | ideal well | oscillator |",
        "|---:|---:|---:|",
    ]
    for i in range(len(well_idx)):
        lines.append(f"| {i + 1} / {i} | `{well_idx[i]}` | `{osc_idx[i]}` |")

    lines += [
        "",
        "## Reading",
        "",
        "- the well retrieves $E_n=(n\\pi)^2$ under the ideal boundary;",
        "- the oscillator retrieves $E_n=n+1/2$ in the flat background;",
        "- remaining errors are due to discretization/truncation;",
        "- the reduced Hessian has a Morse index equal to the number of levels below the chosen state;",
        "- the calculation verifies correspondence, not a new metrological prediction.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    modes = 5
    points_well = 2400
    points_osc = 3200
    half_width = 8.0

    checks = [
        infinite_well_direct(points_well, modes),
        oscillator_direct(points_osc, half_width, modes),
    ]
    report = render(checks, points_well, points_osc, half_width)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
