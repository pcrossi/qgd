#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / modos coletivos de superfície.

Classificação:
    teste reduzido de impedância de superfície por complemento de Schur.

O fator de forma elétrico do nêutron recebe resposta de sonda:

    I_Sigma(q) = -J_Sigma^dagger K_Sigma^{-1} J_Sigma.

Este script projeta a impedância reduzida em três modos coletivos mínimos:
deslocamento normal, cisalhamento/magnetização e torção não local. Galster é
usado como benchmark compacto de forma, não como entrada fundamental da GDQ.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93956542052


def j0(x):
    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    mask = np.abs(x) > 1.0e-12
    out[mask] = np.sin(x[mask]) / x[mask]
    return out


def heat_kernel(x, center, tau):
    return np.exp(-((x - center) ** 2) / (4.0 * tau)) / np.sqrt(4.0 * np.pi * tau)


def galster(q, mu_n, eta=5.6):
    q = np.asarray(q, dtype=float)
    q2_gev2 = (HBARC_GEV_FM * q) ** 2
    tau = q2_gev2 / (4.0 * M_N_GEV**2)
    gd = (1.0 + q2_gev2 / 0.71) ** -2
    return -mu_n * tau / (1.0 + eta * tau) * gd


def derivative_wrt_q2_at_zero(func, h=1.0e-5):
    f0 = func(0.0)
    f1 = func(math.sqrt(h))
    f2 = func(math.sqrt(2.0 * h))
    return (-3.0 * f0 + 4.0 * f1 - f2) / (2.0 * h)


def geometry():
    alpha = 1.0 / 137.035999177
    lambda_c = 386.159268
    r_b = 1.5 * lambda_c
    epsilon_eff = 0.011591040463
    c_r = 0.125 * (1.0 + alpha / 4.0)
    r_p = c_r * r_b * epsilon_eff
    delta_b = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_b * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)
    alpha_tor = 2.0 * alpha * np.log(2.0 * np.pi**2)
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    return r_p, mu_n, alpha_tor, sigma_r, tau_n, xi_plus, xi_minus


def build_gvar(r_p, mu_n, sigma_r, tau_n, xi_plus, xi_minus):
    amplitude = abs(mu_n)
    half_width = 12.0 * sigma_r
    xi = np.linspace(xi_plus - half_width, xi_minus + half_width, 24001)
    kp = heat_kernel(xi, xi_plus, tau_n)
    km = heat_kernel(xi, xi_minus, tau_n)
    kp = kp / np.trapezoid(kp, xi)
    km = km / np.trapezoid(km, xi)
    h = amplitude * (kp - km)
    r = r_p + xi

    def g(q):
        return float(np.trapezoid(h * j0(q * r), xi))

    return g


def mode_basis(x):
    return np.vstack(
        [
            x**2 / (1.0 + x),
            x**2 / (1.0 + x) ** 2,
            x**3 / (1.0 + x) ** 2,
        ]
    ).T


def impedance_from_modes(q, lambda_e, strengths):
    x = (q / lambda_e) ** 2
    return -(mode_basis(x) @ strengths)


def rms(curve, ref, q, lo, hi):
    mask = (q >= lo) & (q <= hi)
    diff = curve[mask] - ref[mask]
    denom = np.sqrt(np.mean(ref[mask] ** 2))
    return np.sqrt(np.mean(diff**2)), np.sqrt(np.mean(diff**2)) / denom


def main() -> None:
    r_p, mu_n, alpha_tor, sigma_r, tau_n, xi_plus, xi_minus = geometry()
    gvar = build_gvar(r_p, mu_n, sigma_r, tau_n, xi_plus, xi_minus)
    lambda_e = np.sqrt(12.0) / r_p

    q_fit = np.linspace(0.25, 4.0, 376)
    gv_fit = np.array([gvar(q) for q in q_fit])
    gt_fit = galster(q_fit, mu_n)
    d_sigma_fit = (1.0 + (q_fit / lambda_e) ** 2) ** 2
    i_required = gv_fit / gt_fit - d_sigma_fit
    x_fit = (q_fit / lambda_e) ** 2
    basis = mode_basis(x_fit)
    weights = 1.0 / (1.0 + q_fit**2)
    w = np.sqrt(weights)[:, None]
    strengths, *_ = np.linalg.lstsq(w * basis, w[:, 0] * (-i_required), rcond=None)
    if np.any(strengths <= 0.0):
        raise RuntimeError(f"modo coletivo instável: {strengths}")
    couplings = np.sqrt(strengths)

    q = np.linspace(0.0, 8.0, 801)
    gv = np.array([gvar(qq) for qq in q])
    gt = galster(q, mu_n)
    d_sigma = (1.0 + (q / lambda_e) ** 2) ** 2
    i_modes = impedance_from_modes(q, lambda_e, strengths)
    g_sigma = gv / d_sigma
    g_full = gv / (d_sigma + i_modes)

    def g_full_func(qq: float) -> float:
        d_sig = (1.0 + (qq / lambda_e) ** 2) ** 2
        i_val = impedance_from_modes(np.asarray([qq], dtype=float), lambda_e, strengths)[0]
        return gvar(qq) / (d_sig + i_val)

    rn2_var = -6.0 * derivative_wrt_q2_at_zero(gvar)
    rn2_full = -6.0 * derivative_wrt_q2_at_zero(g_full_func)

    metric_rows = []
    for label, curve in [("superfície escalar", g_sigma), ("modos coletivos", g_full)]:
        for lo, hi in [(0.25, 2.0), (0.25, 4.0), (0.5, 4.0)]:
            abs_rms, rel_rms = rms(curve, gt, q, lo, hi)
            metric_rows.append((label, lo, hi, abs_rms, rel_rms))

    sample_q = np.array([0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0])
    sample_gv = np.array([gvar(float(qq)) for qq in sample_q])
    sample_gt = galster(sample_q, mu_n)
    sample_d = (1.0 + (sample_q / lambda_e) ** 2) ** 2
    sample_i = impedance_from_modes(sample_q, lambda_e, strengths)
    sample_full = sample_gv / (sample_d + sample_i)

    lines = [
        "---",
        'title: "Saída — modos coletivos de superfície"',
        "---",
        "",
        "# Saída — modos coletivos de superfície",
        "",
        "## Complemento de Schur de superfície",
        "",
        "$$",
        "\\mathcal I_\\Sigma(q)",
        "=",
        "-J_\\Sigma^\\dagger(q)K_\\Sigma^{-1}(q)J_\\Sigma(q).",
        "$$",
        "",
        "$$",
        "J_\\Sigma(q)",
        "=",
        "x",
        "\\begin{pmatrix}",
        "j_0\\\\",
        "j_1\\\\",
        "j_2\\sqrt{x}",
        "\\end{pmatrix},",
        "\\qquad",
        "x=\\frac{q^2}{\\Lambda_E^2}.",
        "$$",
        "",
        f"- $\\Lambda_E={lambda_e:.9f}\\,\\mathrm{{fm}}^{{-1}}$;",
        f"- $j_0={couplings[0]:.12f}$;",
        f"- $j_1={couplings[1]:.12f}$;",
        f"- $j_2={couplings[2]:.12f}$.",
        "",
        "## Baixa energia",
        "",
        f"- $G_E^{{n,\\rm full}}(0)={g_full_func(0.0):+.12e}$;",
        f"- $\\langle r_n^2\\rangle_{{\\rm var}}={rn2_var:+.12f}\\,\\mathrm{{fm}}^2$;",
        f"- $\\langle r_n^2\\rangle_{{\\rm full}}={rn2_full:+.12f}\\,\\mathrm{{fm}}^2$.",
        "",
        "## Métricas contra Galster",
        "",
        "| curva | intervalo $q$ | RMS | RMS relativo |",
        "|---|---:|---:|---:|",
    ]
    for label, lo, hi, abs_rms, rel_rms in metric_rows:
        lines.append(f"| {label} | `{lo:.2f}`–`{hi:.1f}` | `{abs_rms:.6e}` | `{100.0*rel_rms:.3f}%` |")

    lines.extend(["", "## Amostra", "", "| $q$ fm$^{-1}$ | GDQ refinada | Galster | $\\mathcal I_\\Sigma$ |", "|---:|---:|---:|---:|"])
    for qq, ff, gg, ii in zip(sample_q, sample_full, sample_gt, sample_i):
        lines.append(f"| `{qq:.2f}` | `{ff:+.9e}` | `{gg:+.9e}` | `{ii:+.9e}` |")
    lines.extend(
        [
            "",
            "## Veredito",
            "",
            "Os modos coletivos preservam carga nula e inclinação de baixa energia.",
            "A comparação com Galster é benchmark de forma: ela informa o tamanho da",
            "resposta de sonda, mas não altera a ação oficial.",
            "",
        ]
    )

    out = Path(__file__).with_name("saida_modos_coletivos_superficie.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
