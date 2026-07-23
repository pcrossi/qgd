#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / perfil torsional variacional do nêutron.

Classificação:
    avaliação direta do perfil de contorno reduzido.

O perfil elétrico torsional do nêutron é tratado como solução do fluxo de calor
de Perelman na camada de superfície:

    H_n(xi,tau_n) = |mu_n| [K_tau(xi,xi_+) - K_tau(xi,xi_-)].

Com isso, G_E^n(0)=0 e o raio quadrático elétrico decorre da separação
torsional, sem usar o raio experimental do nêutron como entrada.
"""

from __future__ import annotations

import math
from pathlib import Path


def j0(x: float) -> float:
    return 1.0 if abs(x) < 1.0e-12 else math.sin(x) / x


def heat_kernel(x: float, center: float, tau: float) -> float:
    return math.exp(-((x - center) ** 2) / (4.0 * tau)) / math.sqrt(4.0 * math.pi * tau)


def trapz(xs: list[float], ys: list[float]) -> float:
    return sum(0.5 * (ys[i] + ys[i + 1]) * (xs[i + 1] - xs[i]) for i in range(len(xs) - 1))


def derivative_wrt_q2_at_zero(func, h: float = 1.0e-5) -> float:
    f0 = func(0.0)
    f1 = func(math.sqrt(h))
    f2 = func(math.sqrt(2.0 * h))
    return (-3.0 * f0 + 4.0 * f1 - f2) / (2.0 * h)


def main() -> None:
    alpha = 1.0 / 137.035999177
    lambda_c_fm = 386.159268
    r_b = 1.5 * lambda_c_fm
    epsilon_eff = 0.011591040463
    c_r = 0.125 * (1.0 + alpha / 4.0)
    r_p = c_r * r_b * epsilon_eff

    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_b * (1.0 + alpha * 3.0 * math.sqrt(2.0) / 4.0)
    amplitude = abs(mu_n)
    alpha_tor = 2.0 * alpha * math.log(2.0 * math.pi**2)
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2

    n = 24001
    half_width = 12.0 * sigma_r
    xi_min = xi_plus - half_width
    xi_max = xi_minus + half_width
    step = (xi_max - xi_min) / (n - 1)
    xi = [xi_min + i * step for i in range(n)]
    kp = [heat_kernel(x, xi_plus, tau_n) for x in xi]
    km = [heat_kernel(x, xi_minus, tau_n) for x in xi]
    norm_p = trapz(xi, kp)
    norm_m = trapz(xi, km)
    kp = [v / norm_p for v in kp]
    km = [v / norm_m for v in km]
    h_profile = [amplitude * (a - b) for a, b in zip(kp, km)]
    radii = [r_p + x for x in xi]

    charge = trapz(xi, h_profile)
    rn2_moment = trapz(xi, [h * r * r for h, r in zip(h_profile, radii)])
    rn2_analytic = -2.0 * amplitude * alpha_tor * r_p**2

    def ge_n(q: float) -> float:
        return trapz(xi, [h * j0(q * r) for h, r in zip(h_profile, radii)])

    rn2_slope = -6.0 * derivative_wrt_q2_at_zero(ge_n)
    sample_q = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0]

    lines = [
        "---",
        'title: "Saída — perfil torsional do nêutron"',
        "---",
        "",
        "# Saída — perfil torsional do nêutron",
        "",
        "## Perfil variacional",
        "",
        "$$",
        "H_n(\\xi,\\tau_n)",
        "=",
        "|\\mu_n|",
        "\\left[K_{\\tau_n}(\\xi,\\xi_+)-K_{\\tau_n}(\\xi,\\xi_-)\\right].",
        "$$",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $r_p$ | `{r_p:.12f}` fm |",
        f"| $\\mu_n$ | `{mu_n:.12f}` $\\mu_N$ |",
        f"| $\\alpha_{{\\rm tor}}^{{(2)}}$ | `{alpha_tor:.12f}` |",
        f"| $\\xi_+$ | `{xi_plus:+.12f}` fm |",
        f"| $\\xi_-$ | `{xi_minus:+.12f}` fm |",
        f"| $\\sigma_r$ | `{sigma_r:.12f}` fm |",
        f"| $\\tau_n$ | `{tau_n:.12e}` fm$^2$ |",
        "",
        "## Verificações",
        "",
        f"- $\\int H_n d\\xi = {charge:+.12e}$;",
        f"- $G_E^n(0) = {ge_n(0.0):+.12e}$;",
        f"- $\\langle r_n^2\\rangle$ por momento = `{rn2_moment:+.12f}` fm$^2$;",
        f"- expressão analítica = `{rn2_analytic:+.12f}` fm$^2$;",
        f"- inclinação $-6dG_E^n/dq^2|_0$ = `{rn2_slope:+.12f}` fm$^2$.",
        "",
        "## Amostra da curva líder",
        "",
        "| $q$ fm$^{-1}$ | $G_E^n(q^2)$ |",
        "|---:|---:|",
    ]
    for q in sample_q:
        lines.append(f"| `{q:.2f}` | `{ge_n(q):+.12e}` |")
    lines.extend(
        [
            "",
            "## Veredito",
            "",
            "O perfil suave preserva carga total nula, fixa a inclinação de baixa",
            "energia e fornece uma curva líder de superfície. A forma completa em",
            "$q$ intermediário exige a impedância coletiva da sonda.",
            "",
        ]
    )

    out = Path(__file__).with_name("saida_perfil_torcional_neutron.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
