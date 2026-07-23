#!/usr/bin/env python3
"""
Q55 — sela radial reduzida densidade/Bohm/torção.

Classificação:
    teste de consistência / redução efetiva.

Objetivo:
    substituir o perfil fenomenológico m(r)=M r^3/(r^3+ell^3) por um perfil
    estacionário obtido de uma equação variacional radial reduzida.

Não é a sela covariante completa da ação oficial. É o menor modelo radial que
preserva três ingredientes da GDQ usados na Q55:

    1. amplitude u=sqrt(rho);
    2. termo de Bohm como rigidez de gradiente;
    3. repulsão efetiva de torção/densidade por lambda_T u^4.

Sistema adimensional:

    u'   = v
    v'   = 2 (phi + lambda_T u^2 - mu) u - 2 v/r
    phi' = M/r^2
    M'   = r^2 u^2

O termo lambda_T>0 representa a rigidez repulsiva efetiva do setor de torção
na redução radial. O parâmetro mu é autovalor/chemical potential determinado
pela normalização.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import brentq


OUT = Path(__file__).with_name("saida_sela_densidade_bohm_q55.md")


@dataclass(frozen=True)
class RunConfig:
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_mesh: int = 900
    lambda_T: float = 3.0
    compactness: float = 1.0
    max_nodes: int = 40000
    tol: float = 1.0e-5


def initial_guess(r: np.ndarray, width: float = 3.0) -> np.ndarray:
    u0 = np.exp(-0.5 * (r / width) ** 2)
    v0 = -(r / width**2) * u0
    # monotone normalized mass guess with M(0)=0, M(R)~1
    m0 = 1.0 - np.exp(-(r / width) ** 3)
    # smooth attractive potential normalized near outer boundary
    phi0 = -1.0 / np.sqrt(r**2 + width**2)
    return np.vstack([u0, v0, phi0, m0])


def solve_reduced(cfg: RunConfig):
    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_mesh)
    y0 = initial_guess(r)

    def ode(x: np.ndarray, y: np.ndarray, p: np.ndarray) -> np.ndarray:
        mu = p[0]
        rr = np.maximum(x, cfg.r_min)
        u, v, phi, mass = y
        du = v
        dv = 2.0 * (phi + cfg.lambda_T * u**2 - mu) * u - 2.0 * v / rr
        dphi = mass / rr**2
        dm = rr**2 * u**2
        return np.vstack([du, dv, dphi, dm])

    def bc(ya: np.ndarray, yb: np.ndarray, p: np.ndarray) -> np.ndarray:
        return np.array(
            [
                ya[1],                  # regularidade: u'(0)=0
                ya[3],                  # M(0)=0
                yb[0],                  # confinamento/truncamento: u(R)=0
                yb[3] - 1.0,            # massa normalizada
                yb[2] + 1.0 / cfg.r_max # potencial newtoniano exterior
            ]
        )

    sol = solve_bvp(
        ode,
        bc,
        r,
        y0,
        p=np.array([-0.1]),
        tol=cfg.tol,
        max_nodes=cfg.max_nodes,
        verbose=0,
    )
    return sol


def finite_diff(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.gradient(y, x, edge_order=2)


def roots_by_sign(x: np.ndarray, f: np.ndarray):
    roots = []
    for i in range(len(x) - 1):
        if not np.isfinite(f[i]) or not np.isfinite(f[i + 1]):
            continue
        if f[i] == 0:
            roots.append(x[i])
        elif f[i] * f[i + 1] < 0:
            roots.append(brentq(lambda z: np.interp(z, x, f), x[i], x[i + 1]))
    return roots


def analyze(cfg: RunConfig, sol):
    r = np.linspace(cfg.r_min, cfg.r_max, 20000)
    u, v, phi, mass = sol.sol(r)
    rho = u**2

    eta = cfg.compactness
    A = 1.0 - 2.0 * eta * mass / r
    horizons = roots_by_sign(r, A)

    # dimensionless effective energy from mass derivative:
    # M' = r^2 u^2, so epsilon_eff = M'/(4*pi*r^2) up to global units.
    epsilon = rho / (4.0 * np.pi)

    Ap = finite_diff(A, r)
    App = finite_diff(Ap, r)
    # For Phi=0 effective metric. These invariants match the earlier pipeline.
    R = -App - 4.0 * Ap / r + 2.0 * (1.0 - A) / r**2
    Ricci2 = 0.25 * (App + 2.0 * Ap / r) ** 2
    Ricci2 += 0.25 * (App + 2.0 * Ap / r) ** 2
    Ricci2 += 2.0 * ((1.0 - A) / r**2 - Ap / r) ** 2
    Kretsch = App**2 + 4.0 * (Ap / r) ** 2 + 4.0 * ((1.0 - A) / r**2) ** 2

    core = r < 0.05
    fit_region = (r > 5.0e-4) & (r < 0.08)
    coeff = np.polyfit(np.log(r[fit_region]), np.log(np.maximum(mass[fit_region], 1e-300)), 1)
    m_power = coeff[0]

    # proxy radial Hessian: -d2/dr2 + l(l+1)/r^2 + Veff around density lump.
    # We only report positivity of the simple scalar channel; it is not K_phys.
    V_proxy = 6.0 * cfg.lambda_T * rho + np.maximum(-phi, 0.0)
    v_min = float(np.min(V_proxy[(r > 0.1) & (r < cfg.r_max - 0.5)]))

    return {
        "r": r,
        "u": u,
        "rho": rho,
        "phi": phi,
        "mass": mass,
        "A": A,
        "horizons": horizons,
        "epsilon": epsilon,
        "R": R,
        "Ricci2": Ricci2,
        "K": Kretsch,
        "m_power": float(m_power),
        "R_core_mean": float(np.mean(R[core])),
        "Ricci2_core_mean": float(np.mean(Ricci2[core])),
        "K_core_mean": float(np.mean(Kretsch[core])),
        "epsilon_core_mean": float(np.mean(epsilon[core])),
        "rho0": float(rho[0]),
        "V_proxy_min": v_min,
    }


def compactness_scan(sol, cfg: RunConfig, etas: np.ndarray):
    r = np.linspace(cfg.r_min, cfg.r_max, 20000)
    _, _, _, mass = sol.sol(r)
    rows = []
    for eta in etas:
        A = 1.0 - 2.0 * eta * mass / r
        horizons = roots_by_sign(r, A)
        rows.append((float(eta), horizons, float(np.min(A))))
    ratio = r / np.maximum(2.0 * mass, 1e-300)
    eta_crit = float(np.min(ratio))
    return eta_crit, rows


def write_report(cfg: RunConfig, sol, data) -> None:
    lines = []
    lines.append("# Saída — Q55 sela reduzida densidade/Bohm/torção\n")
    lines.append("Classificação: teste de consistência de uma redução efetiva radial da GDQ.\n")
    lines.append("Não é a sela covariante completa da ação oficial.\n")
    lines.append("## Configuração\n")
    lines.append(f"- r_min = `{cfg.r_min}`")
    lines.append(f"- r_max = `{cfg.r_max}`")
    lines.append(f"- n_mesh inicial = `{cfg.n_mesh}`")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- compactness eta = `{cfg.compactness}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append(f"- solve_bvp status = `{sol.status}`")
    lines.append(f"- mensagem = `{sol.message}`")
    lines.append(f"- mu = `{sol.p[0]:.12e}`")
    lines.append(f"- nós finais = `{sol.x.size}`\n")
    lines.append("## Regularidade do core\n")
    lines.append(f"- rho(0) aproximado = `{data['rho0']:.12e}`")
    lines.append(f"- epsilon_core médio = `{data['epsilon_core_mean']:.12e}`")
    lines.append(f"- potência ajustada de M(r) no core = `{data['m_power']:.8f}`")
    lines.append("")
    lines.append("O valor esperado para core regular é `M(r) ~ r^3`.\n")
    lines.append("## Horizontes efetivos\n")
    if data["horizons"]:
        for i, h in enumerate(data["horizons"], 1):
            lines.append(f"- r_H[{i}] = `{h:.12e}`")
    else:
        lines.append("- nenhum horizonte para a compactness escolhida")
    lines.append("")
    eta_crit, scan = compactness_scan(
        sol,
        cfg,
        np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0, 34.0]),
    )
    lines.append("## Varredura de compactness\n")
    lines.append("")
    lines.append(f"- eta_crit aproximado = `{eta_crit:.12e}`")
    lines.append("")
    lines.append("| eta | min A | número de horizontes | horizontes |")
    lines.append("|---:|---:|---:|---|")
    for eta, horizons, amin in scan:
        htxt = ", ".join(f"{h:.6e}" for h in horizons) if horizons else "—"
        lines.append(f"| {eta:.6g} | {amin:.6e} | {len(horizons)} | {htxt} |")
    lines.append("")
    lines.append("## Invariantes efetivos no core\n")
    lines.append(f"- R_core médio = `{data['R_core_mean']:.12e}`")
    lines.append(f"- Ricci2_core médio = `{data['Ricci2_core_mean']:.12e}`")
    lines.append(f"- Kretschmann_core médio = `{data['K_core_mean']:.12e}`")
    lines.append("")
    lines.append("## Estabilidade proxy\n")
    lines.append(f"- V_proxy_min exterior = `{data['V_proxy_min']:.12e}`")
    lines.append("")
    lines.append("## Veredito\n")
    if sol.success and abs(data["m_power"] - 3.0) < 0.05:
        lines.append(
            "A redução radial produz uma densidade estacionária regular com "
            "`M(r) ~ r^3`, portanto confirma dinamicamente o requisito mínimo "
            "do core regular sem escolher o perfil de massa à mão."
        )
    else:
        lines.append(
            "A redução radial ainda não confirmou de forma limpa o core "
            "regular. O resultado deve ser lido como diagnóstico do ansatz."
        )
    lines.append("")
    lines.append(
        "O fechamento total da Q55 continua exigindo a sela covariante completa "
        "`X_*=(g_*,f_*,H_*)` e a Hessiana física `K_BH^phys`."
    )
    OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cfg = RunConfig()
    sol = solve_reduced(cfg)
    data = analyze(cfg, sol)
    write_report(cfg, sol, data)
    print(OUT)
    print(f"success={sol.success} mu={sol.p[0]:.12e} m_power={data['m_power']:.8f}")
    print(f"horizons={data['horizons']}")


if __name__ == "__main__":
    main()
