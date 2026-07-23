#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar resolvente riesz toy` associada ao capítulo `06_global_local_bridge`.

Toy model de resolvente e projetor de Riesz.

Criamos uma matriz simétrica K0 com cluster isolado de dimensão 2. Perturbamos
por eps*V e comparamos os projetores espectrais do cluster. O objeto estável é
o projetor, não cada autovetor individual.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("saida_verificar_resolvente_riesz_toy.md")


def projector(K: np.ndarray, rank: int = 2) -> np.ndarray:
    vals, vecs = np.linalg.eigh(K)
    U = vecs[:, :rank]
    return U @ U.T


def main() -> None:
    rng = np.random.default_rng(12345)
    K0 = np.diag([1.0, 1.2, 5.0, 6.0, 8.0, 10.0])
    A = rng.normal(size=(6, 6))
    V = (A + A.T) / 2.0
    P0 = projector(K0)

    z = 3.0
    R0 = np.linalg.inv(K0 - z * np.eye(6))

    rows = []
    for eps in [0.2, 0.1, 0.05, 0.02, 0.01]:
        Ke = K0 + eps * V
        Pe = projector(Ke)
        Re = np.linalg.inv(Ke - z * np.eye(6))
        proj_err = np.linalg.norm(Pe - P0, ord=2)
        res_err = np.linalg.norm(Re - R0, ord=2)
        vals = np.linalg.eigvalsh(Ke)
        cluster_gap = min(vals[2] - vals[1], vals[0] - (-np.inf))
        rows.append((eps, proj_err, res_err, vals[0], vals[1], vals[2], cluster_gap))

    lines = [
        "---",
        'title: "Saída — resolvente e Riesz toy"',
        "---",
        "",
        "# Saída — resolvente e Riesz toy",
        "",
        "Classificação: toy model espectral / verificação de consistência.",
        "",
        "| $\\varepsilon$ | erro projetor | erro resolvente em $z=3$ | $\\lambda_1$ | $\\lambda_2$ | $\\lambda_3$ | gap cluster |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for eps, proj_err, res_err, l1, l2, l3, gap in rows:
        lines.append(
            f"| {eps:.3f} | {proj_err:.6e} | {res_err:.6e} | {l1:.6f} | {l2:.6f} | {l3:.6f} | {gap:.6f} |"
        )

    lines += [
        "",
        "Conclusão: quando o cluster permanece separado, os projetores espectrais",
        "convergem com a perturbação. Essa é a forma finita do argumento de",
        "herança por resolventes e projetores de Riesz.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

