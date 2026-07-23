#!/usr/bin/env python3
"""Capítulo 16 — auditoria de não-unicidade do canal superior.

Mostra que, sem derivar J2, K2 e mu2 da Hessiana oficial, o mesmo valor de
g-2 pode ser reconstruído por infinitas escolhas. Isso prova que os blocos
`required` são diagnóstico inverso, não previsão.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
A1 = ALPHA / (2.0 * math.pi)
K1 = 2.0 * math.pi / ALPHA

CASES = {
    "e": {
        "name": "elétron",
        "a_obs": 1.00115965218059 - 1.0,
    },
    "mu": {
        "name": "múon",
        "a_obs": 116592059e-11,
    },
}


def evaluate(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    inv = 1.0 / vals
    Hinv = (vecs * inv) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


def solve_mu2(target: float, k2: float, j2: float) -> tuple[float, float, float]:
    H = np.array(
        [
            [1.0, -1.0, -j2],
            [-1.0, K1, 0.0],
            [-j2, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0])
    m0 = np.array([0.0, 1.0, 0.0])
    m1 = np.array([0.0, 1.0, 1.0])
    a0 = evaluate(H, c, m0)
    slope = evaluate(H, c, m1) - a0
    mu2 = (target - a0) / slope
    m = np.array([0.0, 1.0, mu2])
    return mu2, evaluate(H, c, m), float(np.min(np.linalg.eigvalsh(H)))


def main() -> None:
    scales = [1.0, 10.0, 100.0, 1_000.0]
    j_values = [0.5, 1.0, 2.0]
    lines: list[str] = []
    lines.append("# Capítulo 16 — auditoria de não-unicidade do canal superior")
    lines.append("")
    lines.append("## Classificação")
    lines.append("")
    lines.append("Teste de consistência negativo. Demonstra não-unicidade do ajuste superior.")
    lines.append("")
    lines.append("## Parâmetros")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `a_leader = {A1:.15e}`")
    lines.append(f"- `K1 = {K1:.15e}`")
    lines.append("")

    for key, case in CASES.items():
        lines.append(f"## Caso: {case['name']}")
        lines.append("")
        lines.append("| J2 | K2/K1 | mu2_required | a_reconstruido | eig_min |")
        lines.append("|---:|---:|---:|---:|---:|")
        for j2 in j_values:
            for scale in scales:
                k2 = K1 * scale
                mu2, arec, emin = solve_mu2(case["a_obs"], k2, j2)
                lines.append(
                    f"| {j2:.3f} | {scale:.3e} | {mu2:.15e} | "
                    f"{arec:.15e} | {emin:.15e} |"
                )
        lines.append("")

    lines.append("## Conclusão")
    lines.append("")
    lines.append(
        "O mesmo valor observado é reconstruído por diferentes triplas "
        "`(J2,K2,mu2)`. Portanto, `mu2_required` não é observável derivado; "
        "é uma coordenada de engenharia inversa até que `J2` e `K2` sejam "
        "calculados pela Hessiana oficial."
    )
    lines.append("")

    out = Path(__file__).with_name("saida_nao_unicidade_canal_superior_gmenos2.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
