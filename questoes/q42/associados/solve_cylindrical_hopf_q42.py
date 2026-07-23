#!/usr/bin/env python3
"""Calcula o DtN axial no shrinker cilíndrico com V_H tau = 2."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.integrate import solve_bvp


def solve_profile(x_max: float, points: int):
    x = np.linspace(0.0, x_max, points)

    def ode(xv, y):
        return np.vstack((y[1], 0.5 * xv * y[1] + 2.0 * y[0]))

    def boundary(ya, yb):
        return np.array([ya[0] - 1.0, yb[0]])

    initial = np.vstack((np.exp(-x), -np.exp(-x)))
    solution = solve_bvp(ode, boundary, x, initial, tol=1e-10, max_nodes=100000)
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution, -float(solution.y[1, 0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-max-values", default="6,8,10,12")
    parser.add_argument("--points", type=int, default=1200)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_cylindrical_hopf_q42.md"),
    )
    args = parser.parse_args()
    x_values = [float(value) for value in args.x_max_values.split(",")]
    rows = []
    last_solution = None
    for x_max in x_values:
        solution, z_h = solve_profile(x_max, args.points)
        rows.append((x_max, z_h, solution.rms_residuals.max()))
        last_solution = solution
    lines = [
        "# DtN axial do shrinker cilíndrico — Q42",
        "",
        "Equação: `-eta''+(x/2)eta'+2 eta=0`, `eta(0)=1`, `eta(inf)=0`.",
        "",
        "| x_max | z_H=-eta'(0) | resíduo BVP |",
        "|---:|---:|---:|",
    ]
    for x_max, z_h, residual in rows:
        lines.append(f"| {x_max:.1f} | {z_h:.12e} | {residual:.3e} |")
    z_final = rows[-1][1]
    monotone_profile = bool(np.all(last_solution.y[0] >= -1e-10)) and bool(
        np.all(last_solution.y[1] <= 1e-9)
    )
    lines += [
        "",
        f"- z_H convergido: `{z_final:.12e}`;",
        f"- perfil positivo e decrescente: `{monotone_profile}`;",
        "- V_H tau=2 vem do harmônico l=2 do mapa de Hopf em S3;",
        "- a conversão dimensional ainda contém Z_bulk.",
        "",
    ]
    report = "\n".join(lines)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
