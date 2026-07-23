#!/usr/bin/env python3
"""
Q55 — Hessiana reduzida do setor de fase/circulação.

Classificação:
    avaliação direta de Hessiana reduzida / teste de estabilidade de fase.

Na redução Madelung da GDQ, o setor de fase S_R produz a forma quadrática:

    Q_theta[delta theta] = 1/2 ∫ rho |grad delta theta|² dV.

Logo o operador é:

    K_theta = - div(rho grad)

com peso de norma:

    <a,b>_rho = ∫ rho a b dV.

O modo constante em ell=0 é fase global/carga de Noether e deve aparecer como
zero. Ele é removido do espectro físico.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_hessiana_fase_q55.md")


@dataclass(frozen=True)
class Config:
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_grid: int = 900
    ell_max: int = 8


def build_phase_matrices(r: np.ndarray, rho: np.ndarray, ell: int):
    n = r.size
    h = r[1] - r[0]
    L = ell * (ell + 1.0)
    p = r**2 * rho

    K = np.zeros((n, n))
    # Neumann natural via finite elements for ∫ p z'^2 dr.
    for i in range(n - 1):
        pmid = 0.5 * (p[i] + p[i + 1])
        c = pmid / h
        K[i, i] += c
        K[i + 1, i + 1] += c
        K[i, i + 1] -= c
        K[i + 1, i] -= c

    if ell > 0:
        K += np.diag(L * rho * h)

    # Lumped mass for ∫ p z² dr.
    M = np.diag(np.maximum(p * h, 1.0e-14))
    return K, M


def main() -> None:
    cfg = Config()
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)
    if not sol.success:
        raise RuntimeError(sol.message)

    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_grid)
    u, _, _, _ = sol.sol(r)
    rho = u**2

    rows = []
    spectra = {}
    for ell in range(cfg.ell_max + 1):
        K, M = build_phase_matrices(r, rho, ell)
        vals = eigh(K, M, eigvals_only=True)
        spectra[ell] = vals
        nonzero = vals[np.abs(vals) > 1.0e-8]
        nzero = int(np.sum(np.abs(vals) <= 1.0e-8))
        nneg = int(np.sum(nonzero < 0.0))
        first = float(nonzero[0]) if nonzero.size else float("nan")
        rows.append((ell, nneg, nzero, first, vals[:6]))

    lines = []
    lines.append("# Saída — Q55 Hessiana do setor de fase/circulação\n")
    lines.append("Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade de fase.\n")
    lines.append("## Forma quadrática\n")
    lines.append("")
    lines.append("$$")
    lines.append("Q_\\theta[\\delta\\theta]")
    lines.append("=")
    lines.append("\\frac12\\int\\rho\\,|\\nabla\\delta\\theta|^2dV")
    lines.append("$$")
    lines.append("")
    lines.append("Operador:")
    lines.append("")
    lines.append("$$")
    lines.append("K_\\theta=-\\nabla\\cdot(\\rho\\nabla)")
    lines.append("$$")
    lines.append("")
    lines.append("## Configuração\n")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- n_grid = `{cfg.n_grid}`")
    lines.append(f"- ell_max = `{cfg.ell_max}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append("")
    lines.append("## Resumo espectral\n")
    lines.append("")
    lines.append("| ell | negativos físicos | zeros | menor físico não-zero |")
    lines.append("|---:|---:|---:|---:|")
    for ell, nneg, nzero, first, _ in rows:
        lines.append(f"| {ell} | {nneg} | {nzero} | {first:.12e} |")
    lines.append("")
    lines.append("## Primeiros autovalores por ell\n")
    for ell, _, _, _, vals in rows:
        lines.append("")
        lines.append(f"### ell = {ell}")
        for i, val in enumerate(vals, 1):
            lines.append(f"- lambda[{i}] = `{val:.12e}`")
    lines.append("")
    lines.append("## Veredito\n")
    total_neg = sum(row[1] for row in rows)
    if total_neg == 0:
        lines.append("O setor de fase/circulação não possui autovalores físicos negativos nos harmônicos testados.")
    else:
        lines.append(f"Foram encontrados `{total_neg}` autovalores negativos no setor de fase/circulação.")
    lines.append("")
    lines.append("O zero em ell=0 é a fase global protegida por Noether e não representa instabilidade.")
    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(OUT)
    print(f"total_neg={total_neg}")
    for ell, nneg, nzero, first, _ in rows:
        print(ell, nneg, nzero, first)


if __name__ == "__main__":
    main()
