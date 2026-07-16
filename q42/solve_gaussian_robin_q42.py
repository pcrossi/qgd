#!/usr/bin/env python3
"""Espectro Robin no background gaussiano variacional da Q42.

Teste histórico do símbolo principal axial com V_H=0 e beta_B explícito.
beta_B é um autovalor Robin diagnóstico; não é calculado dividindo por uma
rigidez global, que o atlas mostrou ser nula.
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
    # Constante de normalização cancela no problema generalizado.
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
    # -eta'(x_c)+robin eta(x_c)=0; termo variacional ponderado.
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
        default=Path(__file__).with_name("saida_gaussian_robin_q42.md"),
    )
    args = parser.parse_args()
    x_c = np.sqrt(6.0)
    plus = spectrum(args.points, x_c, args.x_max, +args.beta_b, args.modes)
    minus = spectrum(args.points, x_c, args.x_max, -args.beta_b, args.modes)
    lines = [
        "# Espectro axial no background gaussiano — Q42",
        "",
        f"- x_c=sqrt(6): `{x_c:.12e}`",
        f"- beta_B: `{args.beta_b:.12e}`",
        f"- pontos: `{args.points}`",
        "- potencial algébrico: `V_H=0` (teste mínimo);",
        "",
        "| modo | lambda+ | lambda- | diferença |",
        "|---:|---:|---:|---:|",
    ]
    for i, (vp, vm) in enumerate(zip(plus, minus), start=1):
        lines.append(f"| {i} | {vp:.9e} | {vm:.9e} | {vp-vm:.9e} |")
    lines += [
        "",
        f"- menor lambda+ positivo: `{bool(plus[0] > 0)}`;",
        f"- menor lambda- positivo: `{bool(minus[0] > 0)}`;",
        "",
        "O canal antiparalelo pode adquirir modo negativo porque é máximo",
        "da energia Zeeman. Isso não invalida os dois canais unitários, mas",
        "impede usar sua Hessiana estática como dois mínimos dissipativos.",
        "",
    ]
    report = "\n".join(lines)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
