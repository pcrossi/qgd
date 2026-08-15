#!/usr/bin/env python3
"""Robin spectrum on the variational Gaussian background of Chapter 11.

Historical test of the axial principal symbol with V_H=0 and explicit beta_B.
beta_B is a diagnostic Robin eigenvalue; it is not calculated by dividing by a
global stiffness, which the atlas showed to be zero.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


def assemble(points: int, x_c: float, x_max: float, robin: float):
    x = np.linspace(x_c, x_max, points)
    h = float(x[1] - x[0])
    # Normalization constant cancels in the generalized problem.
    weight = x**3 * np.exp(-x**2 / 4.0)
    K = sp.lil_matrix((points, points), dtype=float)
    M = sp.lil_matrix((points, points), dtype=float)
    for i in range(points - 1):
        wm = 0.5 * (weight[i] + weight[i + 1])
        local_k = wm / h * np.array([[1.0, -1.0], [-1.0, 1.0]])
        local_m = wm * h / 6.0 * np.array([[2.0, 1.0], [1.0, 2.0]])
        for a in range(2):
            for b in range(2):
                K[i + a, i + b] += local_k[a, b]
                M[i + a, i + b] += local_m[a, b]
    # -eta'(x_c)+robin eta(x_c)=0; weighted variational term.
    K[0, 0] += weight[0] * robin
    return x, K.tocsc(), M.tocsc()


def spectrum(points: int, x_c: float, x_max: float, robin: float, modes: int):
    _, K, M = assemble(points, x_c, x_max, robin)
    values, _ = spla.eigsh(K, M=M, k=modes, sigma=0.0, which="LM")
    return np.sort(np.asarray(values, dtype=float))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta-b", type=float, required=True)
    parser.add_argument("--x-max", type=float, default=12.0)
    parser.add_argument("--points", type=int, default=2400)
    parser.add_argument("--modes", type=int, default=8)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_gaussian_robin_sg.md"),
    )
    args = parser.parse_args()
    x_c = np.sqrt(6.0)
    plus = spectrum(args.points, x_c, args.x_max, +args.beta_b, args.modes)
    minus = spectrum(args.points, x_c, args.x_max, -args.beta_b, args.modes)
    lines = [
        "# Axial spectrum on the Gaussian background — Chapter 11",
        "",
        f"- x_c=sqrt(6): `{x_c:.12e}`",
        f"- beta_B: `{args.beta_b:.12e}`",
        f"- points: `{args.points}`",
        "- algebraic potential: `V_H=0` (minimal test);",
        "",
        "| mode | lambda+ | lambda- | difference |",
        "|---:|---:|---:|---:|",
    ]
    for i, (vp, vm) in enumerate(zip(plus, minus), start=1):
        lines.append(f"| {i} | {vp:.9e} | {vm:.9e} | {vp-vm:.9e} |")
    lines += [
        "",
        f"- smallest lambda+ positive: `{bool(plus[0] > 0)}`;",
        f"- smallest lambda- positive: `{bool(minus[0] > 0)}`;",
        "",
        "The antiparallel channel can acquire a negative mode because it is a maximum",
        "of the Zeeman energy. This does not invalidate the two unitary channels, but",
        "prevents using its static Hessian as two dissipative minima.",
        "",
    ]
    report = "\n".join(lines)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
