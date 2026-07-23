#!/usr/bin/env python3
"""
Q55 — blocos restantes da Hessiana reduzida.

Classificação:
    avaliação reduzida / diagnóstico espectral e de acoplamentos.

Blocos calculados:
    K_HH  : setor torsional independente reduzido;
    K_gg  : setor métrico axial exterior tipo Regge-Wheeler efetivo;
    K_gf  : norma de acoplamento métrico--dilatônico da medida ponderada;
    K_gH  : norma de acoplamento métrico--torsional efetivo;
    horizonte/Page: temperatura de superfície e curva de Page toy baseada em
                    canais espectrais positivos.

Não é a Hessiana covariante 8D completa. É o fechamento dos blocos que podem
ser avaliados na redução Q55 atual, mantendo a ação oficial como origem e Q54
como leitura macroscópica.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import eigh
from scipy.optimize import brentq

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_blocos_restantes_hessiana_q55.md")


@dataclass(frozen=True)
class Config:
    eta: float = 8.0
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_profile: int = 30000
    n_grid: int = 700
    ell_min_g: int = 2
    ell_max: int = 8
    horizon_cut: float = 5.0e-2


def fd(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.gradient(y, x, edge_order=2)


def roots(x: np.ndarray, f: np.ndarray) -> list[float]:
    out = []
    for i in range(len(x) - 1):
        if f[i] == 0.0:
            out.append(float(x[i]))
        elif f[i] * f[i + 1] < 0:
            out.append(float(brentq(lambda z: np.interp(z, x, f), x[i], x[i + 1])))
    return out


def d2_dirichlet(n: int, h: float) -> np.ndarray:
    main = -2.0 * np.ones(n) / h**2
    off = np.ones(n - 1) / h**2
    return np.diag(main) + np.diag(off, 1) + np.diag(off, -1)


def background(cfg: Config):
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)
    if not sol.success:
        raise RuntimeError(sol.message)

    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_profile)
    u, v, _, m_norm = sol.sol(r)
    mass = cfg.eta * m_norm
    mp = cfg.eta * r**2 * u**2
    mpp = cfg.eta * (2.0 * r * u**2 + 2.0 * r**2 * u * v)
    A = 1.0 - 2.0 * mass / r
    Ap = -2.0 * mp / r + 2.0 * mass / r**2
    eps = mp / (4.0 * np.pi * r**2)
    grad_stress = 0.5 * v**2 / (4.0 * np.pi)
    pr = -eps + grad_stress
    nup = (mass + 4.0 * np.pi * r**3 * pr) / (r**2 * A)
    phip = nup - Ap / (2.0 * A)
    mask = np.abs(A) > cfg.horizon_cut
    safe = np.where(mask, phip, 0.0)
    Phi = -cumulative_trapezoid(safe[::-1], r[::-1], initial=0.0)[::-1]
    rho = u**2
    fR = -np.log(np.maximum(rho, 1.0e-300))
    fRp = fd(fR, r)
    return {
        "sol": sol,
        "r": r,
        "u": u,
        "v": v,
        "rho": rho,
        "fR": fR,
        "fRp": fRp,
        "mass": mass,
        "mp": mp,
        "mpp": mpp,
        "A": A,
        "Ap": Ap,
        "eps": eps,
        "pr": pr,
        "Phi": Phi,
        "horizons": roots(r, A),
    }


def sturm_spectrum(r: np.ndarray, V: np.ndarray, count: int = 6):
    h = r[1] - r[0]
    K = -d2_dirichlet(r.size, h) + np.diag(V)
    vals = eigh(0.5 * (K + K.T), eigvals_only=True)
    return vals[:count], vals


def compute_blocks(cfg: Config, bg):
    r_all = bg["r"]
    r_outer = bg["horizons"][-1] if bg["horizons"] else 0.0
    exterior_mask = (r_all > r_outer + 0.25) & (r_all < cfg.r_max - 0.5)
    if np.count_nonzero(exterior_mask) < cfg.n_grid:
        idx = np.where(exterior_mask)[0]
        pick = idx[np.linspace(0, idx.size - 1, min(cfg.n_grid, idx.size)).astype(int)]
    else:
        idx = np.where(exterior_mask)[0]
        pick = idx[np.linspace(0, idx.size - 1, cfg.n_grid).astype(int)]

    r = r_all[pick]
    A = bg["A"][pick]
    mass = bg["mass"][pick]
    rho = bg["rho"][pick]
    eps = bg["eps"][pick]
    pr = bg["pr"][pick]
    fRp = bg["fRp"][pick]

    rows_HH = []
    rows_gg = []
    for ell in range(0, cfg.ell_max + 1):
        L = ell * (ell + 1.0)
        # Torsion reduced: coexact channel. No artificial IR mass is inserted;
        # the positive floor, if present, must come from the domain and boundary
        # conditions of the exterior patch.
        mH2 = 2.0 * cfg.lambda_T * rho
        V_HH = L / r**2 + mH2
        first_HH, _ = sturm_spectrum(r, V_HH)
        rows_HH.append((ell, float(first_HH[0]), first_HH))

    for ell in range(cfg.ell_min_g, cfg.ell_max + 1):
        L = ell * (ell + 1.0)
        # Effective axial gravitational channel in the exterior static patch.
        # Matter correction is kept as eps-pr from reconstructed source.
        V_gg = A * (L / r**2 - 6.0 * mass / r**3 + 4.0 * np.pi * (eps - pr))
        first_gg, _ = sturm_spectrum(r, V_gg)
        rows_gg.append((ell, float(first_gg[0]), first_gg))

    # Coupling diagnostics on the same exterior patch.
    # K_gf comes from variation of the weighted measure and dilaton gradient.
    J_gf = np.sqrt(np.maximum(A, 0.0)) * np.abs(fRp) * np.sqrt(np.maximum(rho, 0.0))
    # K_gH comes from metric response to torsion energy; in the reduced channel
    # it scales with sqrt(lambda_T)*rho.
    J_gH = np.sqrt(cfg.lambda_T) * rho
    h = r[1] - r[0]
    norm_gf = float(np.sqrt(h * np.dot(J_gf, J_gf)))
    norm_gH = float(np.sqrt(h * np.dot(J_gH, J_gH)))
    gap_scalar = 0.001909625790263
    gap_phase = 0.06572554660398
    gap_HH = min(row[1] for row in rows_HH)
    gap_gg = min(row[1] for row in rows_gg)
    schur_gf = norm_gf**2 / max(gap_scalar * gap_gg, 1.0e-14)
    schur_gH = norm_gH**2 / max(gap_HH * gap_gg, 1.0e-14)

    return {
        "r_patch": r,
        "rows_HH": rows_HH,
        "rows_gg": rows_gg,
        "norm_gf": norm_gf,
        "norm_gH": norm_gH,
        "gap_HH": float(gap_HH),
        "gap_gg": float(gap_gg),
        "gap_scalar": gap_scalar,
        "gap_phase": gap_phase,
        "schur_gf": float(schur_gf),
        "schur_gH": float(schur_gH),
    }


def horizon_page(cfg: Config, bg, blocks):
    horizons = bg["horizons"]
    r = bg["r"]
    A = bg["A"]
    Ap = bg["Ap"]
    Phi = bg["Phi"]
    temps = []
    kappas = []
    for h in horizons:
        Ap_h = float(np.interp(h, r, Ap))
        Phi_h = float(np.interp(h, r, Phi))
        kappa = 0.5 * np.exp(Phi_h) * abs(Ap_h)
        T = kappa / (2.0 * np.pi)
        kappas.append(kappa)
        temps.append(T)

    # Page toy: finite set of positive channels with unitary redistribution.
    gaps = [blocks["gap_scalar"], blocks["gap_phase"], blocks["gap_HH"], blocks["gap_gg"]]
    rates = np.array([np.exp(-g / max(temps[-1], 1.0e-12)) for g in gaps])
    rates = rates / np.sum(rates)
    x = np.linspace(0.0, 1.0, 501)
    # Entropy toy: Page-like rise and fall weighted by channel entropy.
    channel_entropy = -float(np.sum(rates * np.log(np.maximum(rates, 1.0e-300))))
    S = channel_entropy * 4.0 * x * (1.0 - x)
    return {
        "kappas": kappas,
        "temps": temps,
        "rates": rates,
        "Smax": float(np.max(S)),
        "S0": float(S[0]),
        "S1": float(S[-1]),
    }


def main() -> None:
    cfg = Config()
    bg = background(cfg)
    blocks = compute_blocks(cfg, bg)
    hp = horizon_page(cfg, bg, blocks)

    lines = []
    lines.append("# Saída — Q55 blocos restantes da Hessiana reduzida\n")
    lines.append("Classificação: avaliação reduzida / diagnóstico espectral e de acoplamentos.\n")
    lines.append("Não é Hessiana covariante 8D completa.\n")
    lines.append("## Background\n")
    lines.append(f"- eta = `{cfg.eta}`")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- horizontes = `{bg['horizons']}`")
    lines.append(f"- patch exterior usado = `[{blocks['r_patch'][0]:.6e}, {blocks['r_patch'][-1]:.6e}]`")
    lines.append("")
    lines.append("## K_HH — setor torsional independente reduzido\n")
    lines.append("")
    lines.append("| ell | menor autovalor |")
    lines.append("|---:|---:|")
    for ell, first, _ in blocks["rows_HH"]:
        lines.append(f"| {ell} | {first:.12e} |")
    lines.append("")
    lines.append("## K_gg — setor métrico axial exterior reduzido\n")
    lines.append("")
    lines.append("| ell | menor autovalor |")
    lines.append("|---:|---:|")
    for ell, first, _ in blocks["rows_gg"]:
        lines.append(f"| {ell} | {first:.12e} |")
    lines.append("")
    lines.append("## Acoplamentos cruzados reduzidos\n")
    lines.append("")
    lines.append(f"- ||K_gf|| reduzido = `{blocks['norm_gf']:.12e}`")
    lines.append(f"- ||K_gH|| reduzido = `{blocks['norm_gH']:.12e}`")
    lines.append(f"- gap escalar usado = `{blocks['gap_scalar']:.12e}`")
    lines.append(f"- gap fase usado = `{blocks['gap_phase']:.12e}`")
    lines.append(f"- gap K_HH = `{blocks['gap_HH']:.12e}`")
    lines.append(f"- gap K_gg = `{blocks['gap_gg']:.12e}`")
    lines.append(f"- razão Schur gf = `{blocks['schur_gf']:.12e}`")
    lines.append(f"- razão Schur gH = `{blocks['schur_gH']:.12e}`")
    lines.append("")
    lines.append("## Modos de horizonte e Page toy\n")
    for i, (kap, temp) in enumerate(zip(hp["kappas"], hp["temps"]), 1):
        lines.append(f"- horizonte {i}: kappa = `{kap:.12e}`, T = `{temp:.12e}`")
    lines.append(f"- pesos de canais toy = `{hp['rates'].tolist()}`")
    lines.append(f"- S_Page_toy(0) = `{hp['S0']:.12e}`")
    lines.append(f"- max S_Page_toy = `{hp['Smax']:.12e}`")
    lines.append(f"- S_Page_toy(1) = `{hp['S1']:.12e}`")
    lines.append("")
    lines.append("## Veredito\n")
    total_neg_HH = sum(1 for _, first, _ in blocks["rows_HH"] if first < -1.0e-8)
    total_neg_gg = sum(1 for _, first, _ in blocks["rows_gg"] if first < -1.0e-8)
    lines.append(f"- negativos K_HH = `{total_neg_HH}`")
    lines.append(f"- negativos K_gg = `{total_neg_gg}`")
    if total_neg_HH == 0 and total_neg_gg == 0:
        lines.append("Os blocos torsional independente e métrico axial exterior reduzidos são positivos nos setores testados.")
    else:
        lines.append("Há instabilidade reduzida em pelo menos um bloco testado.")
    lines.append("")
    lines.append("As razões Schur são diagnósticos de mistura; se pequenas, os acoplamentos cruzados não fecham o gap. Se grandes, exigem diagonalização acoplada completa.")
    lines.append("")
    lines.append("A Page curve aqui é toy unitário de canais positivos; ainda não é cálculo físico final de informação.")
    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(OUT)
    print(f"K_HH gap={blocks['gap_HH']:.12e} K_gg gap={blocks['gap_gg']:.12e}")
    print(f"Schur gf={blocks['schur_gf']:.12e} gH={blocks['schur_gH']:.12e}")
    print(f"temps={hp['temps']} Smax={hp['Smax']:.12e}")


if __name__ == "__main__":
    main()
