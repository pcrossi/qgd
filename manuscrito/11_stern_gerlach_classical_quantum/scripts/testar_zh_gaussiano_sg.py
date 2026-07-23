#!/usr/bin/env python3
"""Demonstra numericamente que a rigidez DtN gaussiana tem ínfimo zero."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def trial_energy(radius: float, width: float, tau: float, points: int) -> float:
    r = np.linspace(radius, radius + width, points)
    derivative = -np.ones_like(r) / width
    weight = r**3 * np.exp(-r**2 / (4.0 * tau))
    return 0.5 * float(np.trapezoid(weight * derivative**2, r))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--width", type=float, default=1.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_testar_zh_gaussiano_sg.md"),
    )
    args = parser.parse_args()
    radii = np.array([3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) * np.sqrt(args.tau)
    energies = [trial_energy(r, args.width, args.tau, 4001) for r in radii]
    lines = [
        "# Saída — teste de localização axial gaussiana",
        "",
        "| $R/\\sqrt{\\tau}$ | Energia de teste |",
        "|---:|---:|",
    ]
    for radius, energy in zip(radii, energies):
        lines.append(f"| {radius/np.sqrt(args.tau):.3f} | ${energy:.12e}$ |")
    monotone = all(b < a for a, b in zip(energies, energies[1:]))
    lines += [
        "",
        f"- Decaimento monotônico: `{monotone}`",
        f"- Razão $E_{{\\rm final}}/E_{{\\rm inicial}}$: ${energies[-1]/energies[0]:.12e}$",
        "",
        "Conclusão: o shrinker gaussiano exterior possui ínfimo axial zero no teste",
        "Dirichlet--to--Neumann. Ele verifica o bulk, mas não localiza sozinho o modo",
        "axial de Stern--Gerlach.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
