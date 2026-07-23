#!/usr/bin/env python3
"""
Q55 — espectro escalar não homogêneo do bloco K_uu^Schur.

Classificação:
    avaliação direta de Hessiana reduzida / teste de estabilidade escalar.

Generaliza o bloco radial para harmônicos angulares:

    delta u(r,Omega) = y_l(r)/r * Y_lm(Omega)

O operador local recebe l(l+1)/(2 r^2). O complemento de Schur gravitacional
usa o Green radial do mesmo l:

    (d²/dr² - l(l+1)/r²) delta_psi_l = 2 u y_l.

Para l>=1, não há modo de normalização global a remover. Para l=0, removemos
y_N=r u como antes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_hessiana_escalar_l_q55.md")


@dataclass(frozen=True)
class Config:
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_grid: int = 650
    ell_max: int = 8


def d2_dirichlet(n: int, h: float) -> np.ndarray:
    main = -2.0 * np.ones(n) / h**2
    off = np.ones(n - 1) / h**2
    return np.diag(main) + np.diag(off, 1) + np.diag(off, -1)


def projector(vec: np.ndarray, h: float) -> np.ndarray:
    norm = h * float(np.dot(vec, vec))
    return np.eye(vec.size) - (h / norm) * np.outer(vec, vec)


def spectrum_for_l(ell: int, r: np.ndarray, h: float, u: np.ndarray, phi: np.ndarray, mu: float, lambda_T: float):
    n = r.size
    D2 = d2_dirichlet(n, h)
    L = ell * (ell + 1.0)

    K_rad = -0.5 * D2 + np.diag(0.5 * L / r**2 + phi - mu + 3.0 * lambda_T * u**2)

    # Green operator for psi_l with Dirichlet at endpoints:
    # psi'' - L/r^2 psi = 2u y.
    Gop = D2 - np.diag(L / r**2)
    Ginv = np.linalg.inv(Gop)
    K_schur = np.diag(u) @ Ginv @ np.diag(2.0 * u)
    K = 0.5 * (K_rad + K_schur + (K_rad + K_schur).T)

    if ell == 0:
        P = projector(r * u, h)
        K = 0.5 * (P @ K @ P + (P @ K @ P).T)

    vals = eigh(K, eigvals_only=True)
    nonzero = vals[np.abs(vals) > 1.0e-8]
    nneg = int(np.sum(nonzero < 0.0))
    nzero = int(np.sum(np.abs(vals) <= 1.0e-8))
    first = float(nonzero[0]) if nonzero.size else float("nan")
    return vals, nneg, nzero, first


def main() -> None:
    cfg = Config()
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)
    if not sol.success:
        raise RuntimeError(sol.message)

    r_full = np.linspace(cfg.r_min, cfg.r_max, cfg.n_grid + 2)
    h = r_full[1] - r_full[0]
    r = r_full[1:-1]
    u, _, phi, _ = sol.sol(r)
    mu = float(sol.p[0])

    rows = []
    spectra = {}
    for ell in range(cfg.ell_max + 1):
        vals, nneg, nzero, first = spectrum_for_l(ell, r, h, u, phi, mu, cfg.lambda_T)
        rows.append((ell, nneg, nzero, first, vals[:6]))
        spectra[ell] = vals

    lines = []
    lines.append("# Saída — Q55 Hessiana escalar por harmônicos\n")
    lines.append("Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade escalar.\n")
    lines.append("## Configuração\n")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- n_grid = `{cfg.n_grid}`")
    lines.append(f"- ell_max = `{cfg.ell_max}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append(f"- mu = `{mu:.12e}`")
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
        lines.append("Nenhum harmônico escalar testado possui autovalor físico negativo.")
    else:
        lines.append(f"Foram detectados `{total_neg}` autovalores negativos nos setores escalares testados.")
    lines.append("")
    lines.append("Este teste cobre o bloco de amplitude escalar. Não cobre métrica, torção, fase/circulação nem modos de horizonte.")
    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(OUT)
    print(f"total_neg={total_neg}")
    for ell, nneg, nzero, first, _ in rows:
        print(ell, nneg, nzero, first)


if __name__ == "__main__":
    main()
