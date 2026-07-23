#!/usr/bin/env python3
"""
Q55 — diagonalização do bloco radial K_uu^Schur.

Classificação:
    avaliação direta de Hessiana reduzida / teste de estabilidade radial.

Calcula o operador:

    K = -1/2 d²/dr² + V(r) + u D2^{-1} 2u

em variável regular y=r*delta_u, com:

    V = phi - mu + 3 lambda_T u²

e remove o modo de normalização y_N=r*u por projeção ortogonal.

O termo não-local é o complemento de Schur da perturbação do potencial
gravitacional/geométrico:

    delta_psi'' = 2 u y,
    delta_phi = delta_psi/r.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_hessiana_radial_schur_q55.md")


@dataclass(frozen=True)
class Config:
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_grid: int = 650
    n_eigs_report: int = 12


def second_derivative_dirichlet(n: int, h: float) -> np.ndarray:
    main = -2.0 * np.ones(n) / h**2
    off = np.ones(n - 1) / h**2
    return np.diag(main) + np.diag(off, 1) + np.diag(off, -1)


def projector_orthogonal(vec: np.ndarray, h: float) -> np.ndarray:
    # Inner product ∫ y1 y2 dr; h cancels but keep for clarity.
    norm = float(h * np.dot(vec, vec))
    if norm <= 0:
        raise ValueError("zero projector vector")
    return np.eye(vec.size) - (h / norm) * np.outer(vec, vec)


def compute_spectrum(cfg: Config):
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)
    if not sol.success:
        raise RuntimeError(sol.message)

    # Interior grid for Dirichlet y(0)=y(R)=0.
    r_full = np.linspace(cfg.r_min, cfg.r_max, cfg.n_grid + 2)
    h = r_full[1] - r_full[0]
    r = r_full[1:-1]
    u, _, phi, _ = sol.sol(r)
    mu = float(sol.p[0])

    D2 = second_derivative_dirichlet(cfg.n_grid, h)
    V = phi - mu + 3.0 * cfg.lambda_T * u**2
    K_local = -0.5 * D2 + np.diag(V)

    # Schur/nonlocal block. D2 inverse is negative definite with Dirichlet.
    D2_inv = np.linalg.inv(D2)
    K_nonlocal = np.diag(u) @ D2_inv @ np.diag(2.0 * u)
    K_raw = 0.5 * (K_local + K_nonlocal + (K_local + K_nonlocal).T)

    y_norm = r * u
    P = projector_orthogonal(y_norm, h)
    K_phys = 0.5 * (P @ K_raw @ P + (P @ K_raw @ P).T)

    vals_raw = eigh(K_raw, eigvals_only=True)
    vals_phys = eigh(K_phys, eigvals_only=True)

    # Projection introduces one algebraic zero for removed normalization. Drop
    # near-zero numerical nulls for the physical positive/negative count.
    tol_zero = 1.0e-8
    phys_nonzero = vals_phys[np.abs(vals_phys) > tol_zero]
    nneg = int(np.sum(phys_nonzero < 0.0))
    nzero = int(np.sum(np.abs(vals_phys) <= tol_zero))

    return {
        "cfg": cfg,
        "sol": sol,
        "h": h,
        "vals_raw": vals_raw,
        "vals_phys": vals_phys,
        "phys_nonzero": phys_nonzero,
        "nneg": nneg,
        "nzero": nzero,
        "mu": mu,
    }


def main() -> None:
    cfg = Config()
    data = compute_spectrum(cfg)

    # Refinamento curto de malha para o menor autovalor físico.
    conv = []
    for n in (300, 450, 650, 850):
        c = Config(
            lambda_T=cfg.lambda_T,
            r_min=cfg.r_min,
            r_max=cfg.r_max,
            n_grid=n,
            n_eigs_report=cfg.n_eigs_report,
        )
        d = compute_spectrum(c)
        first = float(d["phys_nonzero"][0]) if d["phys_nonzero"].size else float("nan")
        conv.append((n, d["h"], d["nneg"], d["nzero"], first))

    vals_raw = data["vals_raw"]
    vals_phys = data["vals_phys"]
    phys_nonzero = data["phys_nonzero"]
    nneg = data["nneg"]
    nzero = data["nzero"]
    sol = data["sol"]
    mu = data["mu"]
    h = data["h"]

    lines = []
    lines.append("# Saída — Q55 Hessiana radial Schur\n")
    lines.append("Classificação: avaliação direta de Hessiana reduzida / teste de estabilidade radial.\n")
    lines.append("## Configuração\n")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- r_min = `{cfg.r_min}`")
    lines.append(f"- r_max = `{cfg.r_max}`")
    lines.append(f"- n_grid interior = `{cfg.n_grid}`")
    lines.append(f"- h = `{h:.12e}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append(f"- mu = `{mu:.12e}`")
    lines.append("")
    lines.append("## Espectro bruto\n")
    lines.append("")
    for i, val in enumerate(vals_raw[: cfg.n_eigs_report], 1):
        lines.append(f"- lambda_raw[{i}] = `{val:.12e}`")
    lines.append("")
    lines.append("## Espectro físico radial projetado\n")
    lines.append("")
    for i, val in enumerate(vals_phys[: cfg.n_eigs_report], 1):
        lines.append(f"- lambda_phys[{i}] = `{val:.12e}`")
    lines.append("")
    lines.append("## Contagem\n")
    lines.append(f"- modos zero numéricos = `{nzero}`")
    lines.append(f"- autovalores físicos negativos = `{nneg}`")
    if phys_nonzero.size:
        lines.append(f"- menor autovalor físico não-zero = `{phys_nonzero[0]:.12e}`")
    lines.append("")
    lines.append("## Convergência de malha\n")
    lines.append("")
    lines.append("| n_grid | h | negativos | zeros | menor físico não-zero |")
    lines.append("|---:|---:|---:|---:|---:|")
    for n, hh, nn, nz, first in conv:
        lines.append(f"| {n} | {hh:.6e} | {nn} | {nz} | {first:.12e} |")
    lines.append("")
    lines.append("## Veredito\n")
    lines.append("")
    if nneg == 0:
        lines.append("O bloco radial de amplitude com Schur gravitacional não-local não possui autovalor físico negativo após remover a normalização.")
    else:
        lines.append("O bloco radial de amplitude possui autovalores físicos negativos nesta redução; isso indicaria instabilidade radial.")
    lines.append("")
    lines.append("Este resultado cobre apenas o setor radial de amplitude. Ele não substitui os setores métrico, torsional, fase e horizonte de `K_BH^phys`.")
    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(OUT)
    print(f"nneg={nneg} nzero={nzero} first_nonzero={phys_nonzero[0] if phys_nonzero.size else None}")


if __name__ == "__main__":
    main()
