#!/usr/bin/env python3
"""
Q55 — reconstrução covariante efetiva a partir da sela radial reduzida.

Classificação:
    teste de consistência / reconstrução efetiva.

Entrada:
    solução radial reduzida u=sqrt(rho), M(r), phi(r) do script
    solve_sela_densidade_bohm_q55.py.

Saída:
    métrica estática esférica efetiva, pressão radial/tangencial lidas das
    equações de Einstein efetivas da Q54, condições de energia, horizontes e
    invariantes.

Observação:
    Isto não transforma Einstein-Hilbert em ação fundamental. A Q54 permite
    usar a forma de Einstein como limite macroscópico efetivo da equação
    métrica ponderada da GDQ.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_reconstrucao_covarante_sela_reduzida_q55.md")


@dataclass(frozen=True)
class CovConfig:
    # Use a compactness acima de eta_crit para testar regime BH regular.
    eta: float = 8.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_eval: int = 30000
    lambda_T: float = 3.0


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


def reconstruct(cfg: CovConfig):
    rcfg = radial.RunConfig(
        r_min=cfg.r_min,
        r_max=cfg.r_max,
        lambda_T=cfg.lambda_T,
    )
    sol = radial.solve_reduced(rcfg)
    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_eval)
    u, v, phi_newton, m_norm = sol.sol(r)

    # Escala relativística efetiva. M_geo = eta * M_norm.
    mass = cfg.eta * m_norm
    rho = u**2
    A = 1.0 - 2.0 * mass / r
    mp = cfg.eta * r**2 * u**2
    mpp = cfg.eta * (2.0 * r * u**2 + 2.0 * r**2 * u * v)
    Ap = -2.0 * mp / r + 2.0 * mass / r**2
    App = -2.0 * mpp / r + 4.0 * mp / r**2 - 4.0 * mass / r**3

    # Gauge efetivo mínimo Phi=0. Pressões lidas de G^mu_nu.
    eps = mp / (4.0 * np.pi * r**2)
    pr = ((A - 1.0) / r**2 + Ap / r) / (8.0 * np.pi)
    pt = (0.5 * App + Ap / r) / (8.0 * np.pi)

    # Conservação anisotrópica para g_tt=-A e^{2Phi}.
    # p_r' + (epsilon+p_r)(Phi' + A'/(2A)) + 2(p_r-p_t)/r = 0.
    # Neste teste Phi=0, mas o termo A'/(2A) não pode ser omitido.
    # Excluímos uma vizinhança dos horizontes da métrica estática, onde a
    # coordenada Schwarzschild efetiva é singular.
    # p_r' ainda é diferenciado numericamente; a contribuição dominante de
    # A' e A'' já foi analítica, o que reduz fortemente o erro.
    cons_res = fd(pr, r) + (eps + pr) * (Ap / (2.0 * A)) + 2.0 * (pr - pt) / r

    # Invariantes para Phi=0.
    R = -App - 4.0 * Ap / r + 2.0 * (1.0 - A) / r**2
    Ricci2 = 0.5 * (App + 2.0 * Ap / r) ** 2
    Ricci2 += 2.0 * ((1.0 - A) / r**2 - Ap / r) ** 2
    K = App**2 + 4.0 * (Ap / r) ** 2 + 4.0 * ((1.0 - A) / r**2) ** 2

    # Core diagnostics away from numerical endpoint.
    core = (r > 5.0e-4) & (r < 5.0e-2)
    fit_region = (r > 5.0e-4) & (r < 8.0e-2)
    m_power = np.polyfit(
        np.log(r[fit_region]),
        np.log(np.maximum(mass[fit_region], 1e-300)),
        1,
    )[0]

    # Exterior shell for asymptotic diagnostics.
    ext = r > 0.8 * cfg.r_max

    return {
        "sol": sol,
        "r": r,
        "u": u,
        "rho": rho,
        "mass": mass,
        "A": A,
        "eps": eps,
        "pr": pr,
        "pt": pt,
        "R": R,
        "Ricci2": Ricci2,
        "K": K,
        "horizons": roots(r, A),
        "m_power": float(m_power),
        "core": {
            "eps": float(np.mean(eps[core])),
            "pr": float(np.mean(pr[core])),
            "pt": float(np.mean(pt[core])),
            "eps_plus_pr": float(np.mean((eps + pr)[core])),
            "eps_plus_pt": float(np.mean((eps + pt)[core])),
            "sec": float(np.mean((eps + pr + 2.0 * pt)[core])),
            "R": float(np.mean(R[core])),
            "Ricci2": float(np.mean(Ricci2[core])),
            "K": float(np.mean(K[core])),
            "cons_res_rms": float(np.sqrt(np.mean(cons_res[core] ** 2))),
        },
        "global": {
            "min_A": float(np.min(A)),
            "max_abs_R": float(np.max(np.abs(R))),
            "max_K": float(np.max(K)),
            "mass_ext_mean": float(np.mean(mass[ext])),
            "A_ext_mean": float(np.mean(A[ext])),
            "cons_res_rms_static_patches": float(
                np.sqrt(np.mean(cons_res[np.abs(A) > 5.0e-2] ** 2))
            ),
        },
    }


def report(cfg: CovConfig, data) -> None:
    lines = []
    lines.append("# Saída — Q55 reconstrução covariante efetiva da sela reduzida\n")
    lines.append("Classificação: teste de consistência / reconstrução efetiva.\n")
    lines.append("Não é solução covariante completa da ação oficial.\n")
    lines.append("## Parâmetros\n")
    lines.append(f"- eta = `{cfg.eta}`")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- r_min = `{cfg.r_min}`")
    lines.append(f"- r_max = `{cfg.r_max}`")
    lines.append(f"- solve_bvp success = `{data['sol'].success}`")
    lines.append(f"- mu radial = `{data['sol'].p[0]:.12e}`")
    lines.append("")
    lines.append("## Regularidade central\n")
    lines.append(f"- potência de massa no core = `{data['m_power']:.8f}`")
    lines.append(f"- epsilon_core = `{data['core']['eps']:.12e}`")
    lines.append(f"- p_r_core = `{data['core']['pr']:.12e}`")
    lines.append(f"- p_t_core = `{data['core']['pt']:.12e}`")
    lines.append(f"- epsilon+p_r = `{data['core']['eps_plus_pr']:.12e}`")
    lines.append(f"- epsilon+p_t = `{data['core']['eps_plus_pt']:.12e}`")
    lines.append(f"- SEC combo epsilon+p_r+2p_t = `{data['core']['sec']:.12e}`")
    lines.append("")
    lines.append("## Horizontes\n")
    if data["horizons"]:
        for i, h in enumerate(data["horizons"], 1):
            lines.append(f"- r_H[{i}] = `{h:.12e}`")
    else:
        lines.append("- nenhum horizonte")
    lines.append("")
    lines.append("## Invariantes no core\n")
    lines.append(f"- R_core = `{data['core']['R']:.12e}`")
    lines.append(f"- Ricci2_core = `{data['core']['Ricci2']:.12e}`")
    lines.append(f"- Kretschmann_core = `{data['core']['K']:.12e}`")
    lines.append("")
    lines.append("## Conservação efetiva\n")
    lines.append(
        "- RMS do resíduo de conservação anisotrópica no core "
        f"= `{data['core']['cons_res_rms']:.12e}`"
    )
    lines.append(
        "- RMS do resíduo em patches estáticos `|A|>5e-2` "
        f"= `{data['global']['cons_res_rms_static_patches']:.12e}`"
    )
    lines.append("")
    lines.append("## Assintótica\n")
    lines.append(f"- massa exterior média = `{data['global']['mass_ext_mean']:.12e}`")
    lines.append(f"- A exterior médio = `{data['global']['A_ext_mean']:.12e}`")
    lines.append("")
    lines.append("## Veredito\n")
    if data["horizons"] and abs(data["m_power"] - 3.0) < 0.05:
        lines.append(
            "A sela radial reduzida, quando compactificada acima de eta_crit, "
            "gera métrica efetiva com horizontes e core regular."
        )
    else:
        lines.append(
            "A reconstrução não entrou simultaneamente no regime de horizonte "
            "e core regular para os parâmetros testados."
        )
    lines.append("")
    lines.append(
        "A leitura de pressões por Einstein efetivo é legítima apenas como "
        "camada macroscópica Q54. O fechamento total exige obter Phi(r), "
        "epsilon(r), p_r(r) e p_t(r) por variação direta da ação GDQ reduzida."
    )
    OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cfg = CovConfig()
    data = reconstruct(cfg)
    report(cfg, data)
    print(OUT)
    print(f"horizons={data['horizons']}")
    print(f"m_power={data['m_power']:.8f}")
    print(f"core_SEC={data['core']['sec']:.12e}")


if __name__ == "__main__":
    main()
