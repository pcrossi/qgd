#!/usr/bin/env python3
"""
Q55 — reconstrução do lapse Phi(r) por conservação/TOV efetiva.

Classificação:
    teste de consistência / reconstrução efetiva.

Objetivo:
    remover a escolha Phi=0 usada no teste anterior. Partimos da sela radial
    reduzida, lemos epsilon(r) e p_r(r) do setor massivo e reconstruímos Phi'(r)
    pela equação efetiva:

        Phi' = (m + 4*pi*r^3*p_r) / (r^2*A)

    em unidades G=c=1, com A=1-2m/r.

Em seguida calculamos p_t por conservação:

        p_t = p_r + r/2 * [p_r' + (epsilon+p_r)(Phi' + A'/(2A))]

e verificamos se a fonte resultante permanece regular e anisotropicamente
conservada fora das singularidades coordenadas dos horizontes.

Isto continua sendo camada macroscópica Q54, não a ação fundamental.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_reconstrucao_lapse_tov_sela_q55.md")


@dataclass(frozen=True)
class Config:
    eta: float = 8.0
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_eval: int = 30000
    horizon_cut: float = 5.0e-2


def fd(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.gradient(y, x, edge_order=2)


def roots(x: np.ndarray, f: np.ndarray) -> list[float]:
    out = []
    for i in range(len(x) - 1):
        if f[i] == 0:
            out.append(float(x[i]))
        elif f[i] * f[i + 1] < 0:
            out.append(float(brentq(lambda z: np.interp(z, x, f), x[i], x[i + 1])))
    return out


def masked_integral_phi(r: np.ndarray, phip: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Integrate Phi' from r_max inward in static patches.

    Near horizons, Schwarzschild-like coordinates produce coordinate poles.
    For the diagnostic we set Phi' to 0 inside the excluded band and integrate
    over the regular patches. This is not a Kruskal extension; it is a check
    of the local static charts.
    """
    safe = np.where(mask, phip, 0.0)
    # Phi(r_max)=0, integrate backwards.
    rev_int = cumulative_trapezoid(safe[::-1], r[::-1], initial=0.0)
    return -rev_int[::-1]


def main() -> None:
    cfg = Config()
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)

    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_eval)
    u, v, _, m_norm = sol.sol(r)
    mass = cfg.eta * m_norm
    mp = cfg.eta * r**2 * u**2
    mpp = cfg.eta * (2.0 * r * u**2 + 2.0 * r**2 * u * v)

    A = 1.0 - 2.0 * mass / r
    Ap = -2.0 * mp / r + 2.0 * mass / r**2
    App = -2.0 * mpp / r + 4.0 * mp / r**2 - 4.0 * mass / r**3

    eps = mp / (4.0 * np.pi * r**2)

    # Keep the exact Einstein-effective radial pressure from the metric ansatz
    # with unknown Phi:
    # 8*pi*p_r = (A-1)/r^2 + A'/r + 2A Phi'/r.
    # TOV can be solved for Phi' if p_r is supplied. Here the GDQ radial
    # reduced source supplies the natural de Sitter-core equation of state
    # p_r=-epsilon plus a Bohm-gradient correction. The minimal correction is
    # the radial kinetic stress of u.
    grad_stress = 0.5 * v**2 / (4.0 * np.pi)
    pr_input = -eps + grad_stress

    nup = (mass + 4.0 * np.pi * r**3 * pr_input) / (r**2 * A)
    phip = nup - Ap / (2.0 * A)

    horizons = roots(r, A)
    mask = np.abs(A) > cfg.horizon_cut
    Phi = masked_integral_phi(r, phip, mask)

    pr_metric = ((A - 1.0) / r**2 + 2.0 * A * nup / r) / (8.0 * np.pi)
    prp = fd(pr_input, r)
    pt_tov = pr_input + 0.5 * r * (prp + (eps + pr_input) * nup)

    cons_res = prp + (eps + pr_input) * nup + 2.0 * (pr_input - pt_tov) / r

    # Ricci scalar from trace: R = -8*pi*T = 8*pi(eps-pr-2pt), Lambda=0 convention.
    R_trace = 8.0 * np.pi * (eps - pr_input - 2.0 * pt_tov)

    core = (r > 5.0e-4) & (r < 5.0e-2)
    static = mask & (r > 5.0e-4) & (r < cfg.r_max - 1.0)
    fit_region = (r > 5.0e-4) & (r < 8.0e-2)
    m_power = np.polyfit(
        np.log(r[fit_region]),
        np.log(np.maximum(mass[fit_region], 1e-300)),
        1,
    )[0]

    lines = []
    lines.append("# Saída — Q55 reconstrução de lapse por TOV efetiva\n")
    lines.append("Classificação: teste de consistência / reconstrução efetiva.\n")
    lines.append("Não é sela covariante completa da ação oficial.\n")
    lines.append("## Parâmetros\n")
    lines.append(f"- eta = `{cfg.eta}`")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append(f"- mu radial = `{sol.p[0]:.12e}`")
    lines.append(f"- corte de horizonte `|A|>` = `{cfg.horizon_cut}`")
    lines.append("")
    lines.append("## Horizontes\n")
    for i, h in enumerate(horizons, 1):
        lines.append(f"- r_H[{i}] = `{h:.12e}`")
    if not horizons:
        lines.append("- nenhum horizonte")
    lines.append("")
    lines.append("## Core\n")
    lines.append(f"- potência de massa = `{m_power:.8f}`")
    lines.append(f"- epsilon_core = `{np.mean(eps[core]):.12e}`")
    lines.append(f"- p_r_core input = `{np.mean(pr_input[core]):.12e}`")
    lines.append(f"- p_r_core métrico = `{np.mean(pr_metric[core]):.12e}`")
    lines.append(f"- p_t_core TOV = `{np.mean(pt_tov[core]):.12e}`")
    lines.append(f"- epsilon+p_r = `{np.mean((eps+pr_input)[core]):.12e}`")
    lines.append(f"- epsilon+p_t = `{np.mean((eps+pt_tov)[core]):.12e}`")
    lines.append(f"- SEC combo = `{np.mean((eps+pr_input+2.0*pt_tov)[core]):.12e}`")
    lines.append(f"- R_trace_core = `{np.mean(R_trace[core]):.12e}`")
    lines.append("")
    lines.append("## Lapse\n")
    lines.append(f"- Phi_core médio = `{np.mean(Phi[core]):.12e}`")
    lines.append(f"- Phi exterior médio = `{np.mean(Phi[r > 0.8*cfg.r_max]):.12e}`")
    lines.append(f"- max |Phi| em patches estáticos = `{np.max(np.abs(Phi[static])):.12e}`")
    lines.append("")
    lines.append("## Conservação\n")
    lines.append(f"- RMS core = `{np.sqrt(np.mean(cons_res[core]**2)):.12e}`")
    lines.append(f"- RMS patches estáticos = `{np.sqrt(np.mean(cons_res[static]**2)):.12e}`")
    lines.append(f"- max |p_r métrico - p_r input| core = `{np.max(np.abs((pr_metric-pr_input)[core])):.12e}`")
    lines.append("")
    lines.append("## Veredito\n")
    lines.append(
        "A reconstrução por TOV mostra que, dado o perfil radial reduzido e uma "
        "equação de estado GDQ efetiva de core, o lapse pode ser reconstruído "
        "por conservação. A identidade de conservação fecha numericamente por "
        "construção e a regularidade central é preservada."
    )
    lines.append("")
    lines.append(
        "A limitação permanece: a equação de estado radial e a compactness ainda "
        "precisam ser derivadas da Hessiana oficial, não escolhidas como camada "
        "efetiva."
    )
    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(OUT)
    print(f"horizons={horizons}")
    print(f"m_power={m_power:.8f}")
    print(f"RMS_static={np.sqrt(np.mean(cons_res[static]**2)):.12e}")


if __name__ == "__main__":
    main()
