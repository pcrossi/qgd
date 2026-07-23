#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `cosmologia escalas gdq` associada ao capítulo `25_astrophysics_cosmology`.
Escalas cosmológicas reduzidas da GDQ.

Classificação científica:
    avaliação direta de fórmulas estruturais condicionadas ao contorno global.

O script calcula rho_Lambda^GDQ, a0=cH0/(2pi) e a escala auxiliar de de Sitter.
H0 e Omega_Lambda são tratados como dados de contorno cosmológico, não como
parâmetros ajustados pela teoria.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_cosmologia_escalas_gdq.md"


def main() -> None:
    c = 299_792_458.0
    G = 6.67430e-11
    mpc = 3.0856775814913673e22
    alpha_inv = 137.035999084
    alpha = 1.0 / alpha_inv
    m_p = 1.67262192595e-27
    r_p = 0.84077876545e-15
    H0_planck_km = 67.4
    H0_local_km = 73.0
    Omega_Lambda = 0.6847
    a0_ref = 1.20e-10

    H0 = H0_planck_km * 1000.0 / mpc
    H0_local = H0_local_km * 1000.0 / mpc
    R_H = c / H0
    n_cartan = 28
    volume_p = (4.0 / 3.0) * math.pi * r_p**3
    rho_uv = m_p * c**2 / volume_p
    rho_lambda_j = alpha**2 * n_cartan * rho_uv * (r_p / R_H)
    rho_lambda_kg = rho_lambda_j / c**2
    rho_crit = 3.0 * H0**2 / (8.0 * math.pi * G)
    rho_ref = Omega_Lambda * rho_crit
    rho_err = (rho_lambda_kg - rho_ref) / rho_ref

    a0_planck = c * H0 / (2.0 * math.pi)
    a0_local = c * H0_local / (2.0 * math.pi)
    a_ds = c * H0 * math.sqrt(Omega_Lambda) / (2.0 * math.pi)

    lines: list[str] = []
    lines.append("# Saída — escalas cosmológicas GDQ\n\n")
    lines.append("Classificação: avaliação direta de fórmulas estruturais condicionadas ao contorno.\n\n")
    lines.append("## Energia escura\n\n")
    lines.append(f"- alpha^-1: `{alpha_inv:.12f}`\n")
    lines.append(f"- r_p: `{r_p:.12e} m`\n")
    lines.append(f"- H0: `{H0_planck_km:.6f} km/s/Mpc`\n")
    lines.append(f"- Omega_Lambda: `{Omega_Lambda:.8f}`\n")
    lines.append(f"- R_H: `{R_H:.12e} m`\n")
    lines.append(f"- rho_UV: `{rho_uv:.12e} J/m^3`\n")
    lines.append(f"- rho_Lambda_GDQ: `{rho_lambda_kg:.12e} kg/m^3`\n")
    lines.append(f"- rho_ref: `{rho_ref:.12e} kg/m^3`\n")
    lines.append(f"- erro relativo: `{rho_err:+.12e}`\n\n")

    lines.append("## Acelerações\n\n")
    lines.append("| escala | valor [m/s^2] | erro vs 1.20e-10 |\n")
    lines.append("|---|---:|---:|\n")
    for name, value in [
        ("cH0 Planck / 2pi", a0_planck),
        ("cH0 local / 2pi", a0_local),
        ("cH0 sqrt(Omega_Lambda) / 2pi", a_ds),
    ]:
        lines.append(f"| {name} | {value:.12e} | {(value/a0_ref - 1.0):+.6%} |\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

