#!/usr/bin/env python3
"""
Q55 — estabilidade da sela radial sob reescala de massa preservada.

Classificação:
    teste de consistência / Hessiana reduzida de um modo coletivo.

Testa a direção coletiva:

    u_a(r) = a^{3/2} u(a r)

que preserva a massa em 3D. Para uma sela estável nessa direção:

    d²E/da² |_{a=1} > 0.

Não substitui K_BH^phys. É apenas o canal radial homogêneo de escala.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import trapezoid

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_estabilidade_escala_sela_q55.md")


@dataclass(frozen=True)
class Config:
    lambda_T: float = 3.0
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_eval: int = 50000
    alphas: tuple[float, ...] = (0.94, 0.96, 0.98, 0.99, 1.0, 1.01, 1.02, 1.04, 1.06)


def energy_scaled(alpha: float, r: np.ndarray, u: np.ndarray, phi: np.ndarray, lambda_T: float):
    # u_alpha(r)=alpha^(3/2) u(alpha r). Interpolate inside domain.
    ar = alpha * r
    u_a = alpha ** 1.5 * np.interp(ar, r, u, left=u[0], right=0.0)
    phi_a = alpha * np.interp(ar, r, phi, left=phi[0], right=0.0)
    v_a = np.gradient(u_a, r, edge_order=2)
    dV = 4.0 * np.pi * r**2
    K = 0.5 * trapezoid(v_a**2 * dV, r)
    U = 0.5 * lambda_T * trapezoid(u_a**4 * dV, r)
    W = 0.5 * trapezoid(phi_a * u_a**2 * dV, r)
    return K + U + W, K, U, W


def main() -> None:
    cfg = Config()
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=cfg.lambda_T)
    sol = radial.solve_reduced(rcfg)
    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_eval)
    u, _, phi, _ = sol.sol(r)

    rows = []
    for a in cfg.alphas:
        E, K, U, W = energy_scaled(a, r, u, phi, cfg.lambda_T)
        rows.append((a, E, K, U, W))

    arr = np.array([[a, E] for a, E, *_ in rows])
    near = np.abs(arr[:, 0] - 1.0) <= 0.02
    coeff = np.polyfit(arr[near, 0] - 1.0, arr[near, 1], 2)
    curvature = 2.0 * coeff[0]
    slope = coeff[1]

    lines = []
    lines.append("# Saída — Q55 estabilidade coletiva de escala\n")
    lines.append("Classificação: teste de consistência / Hessiana reduzida de modo coletivo.\n")
    lines.append("## Direção testada\n")
    lines.append("")
    lines.append("$$")
    lines.append("u_a(r)=a^{3/2}u(ar)")
    lines.append("$$")
    lines.append("")
    lines.append("## Resultado local em a=1\n")
    lines.append("")
    lines.append(f"- lambda_T = `{cfg.lambda_T}`")
    lines.append(f"- solve_bvp success = `{sol.success}`")
    lines.append(f"- inclinação dE/da = `{slope:.12e}`")
    lines.append(f"- curvatura d2E/da2 = `{curvature:.12e}`")
    lines.append("")
    lines.append("| a | E | K | U_T | W |")
    lines.append("|---:|---:|---:|---:|---:|")
    for a, E, K, U, W in rows:
        lines.append(f"| {a:.6f} | {E:.12e} | {K:.12e} | {U:.12e} | {W:.12e} |")
    lines.append("")
    lines.append("## Veredito\n")
    lines.append("")
    if curvature > 0:
        lines.append("A curvatura coletiva é positiva: a sela é estável no modo de escala radial testado.")
    else:
        lines.append("A curvatura coletiva não é positiva: o modo de escala radial não está estabilizado neste teste.")
    lines.append("")
    lines.append("Isto não substitui a diagonalização de `K_BH^phys`; cobre apenas o modo coletivo homogêneo de escala.")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)
    print(f"slope={slope:.12e} curvature={curvature:.12e}")


if __name__ == "__main__":
    main()
