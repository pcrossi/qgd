r"""
GDQ — Solução variacional de H_n(chi) e curva G_E^n(q^2) (Q40)

Este script implementa o fechamento fenomenológico líder do fator de forma
elétrico do nêutron a partir do perfil torsional variacional H_n.

O perfil é obtido como solução do fluxo de calor de Perelman na camada local de
superfície:

    H_n(xi, tau) = |mu_n| [K_tau(xi, xi_+) - K_tau(xi, xi_-)]

com:

    xi = r - r_p = C_r R_B (chi - epsilon_eff)
    xi_+ = -0.5 r_p alpha_tor^(2)
    xi_- = +0.5 r_p alpha_tor^(2)
    sigma_r = sqrt(2 tau) = 0.5 r_p alpha_tor^(2)

Nenhum raio elétrico experimental do nêutron é usado como entrada.
"""

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import numpy as np
import matplotlib.pyplot as plt


def j0(x):
    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    mask = np.abs(x) > 1.0e-12
    out[mask] = np.sin(x[mask]) / x[mask]
    return out


def heat_kernel(x, center, tau):
    return np.exp(-((x - center) ** 2) / (4.0 * tau)) / np.sqrt(4.0 * np.pi * tau)


def derivative_wrt_q2_at_zero(func, h=1.0e-5):
    f0 = func(0.0)
    f1 = func(np.sqrt(h))
    f2 = func(np.sqrt(2.0 * h))
    return (-3.0 * f0 + 4.0 * f1 - f2) / (2.0 * h)


def main():
    print("=" * 96)
    print("      GDQ — SOLUÇÃO VARIACIONAL DE H_n(chi) E G_E^n(q^2) — Q40")
    print("=" * 96)

    alpha = 1.0 / 137.03599907
    Lambda_C = 386.159268  # fm
    R_B = 1.5 * Lambda_C
    epsilon_eff = 0.011591040463
    C_r = 0.125 * (1.0 + alpha / 4.0)
    c_scale = C_r * R_B
    r_p = c_scale * epsilon_eff

    delta_B = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_B * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)
    A = abs(mu_n)

    alpha_tor = 2.0 * alpha * np.log(2.0 * np.pi**2)
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2

    # Grid local suficiente para normalizar os núcleos em precisão de máquina.
    half_width = 12.0 * sigma_r
    xi = np.linspace(xi_plus - half_width, xi_minus + half_width, 24001)
    K_plus = heat_kernel(xi, xi_plus, tau_n)
    K_minus = heat_kernel(xi, xi_minus, tau_n)

    # Normalização numérica explícita para eliminar erro de cauda finita.
    K_plus = K_plus / np.trapezoid(K_plus, xi)
    K_minus = K_minus / np.trapezoid(K_minus, xi)
    H = A * (K_plus - K_minus)
    r = r_p + xi

    charge = np.trapezoid(H, xi)
    rn2_moment = np.trapezoid(H * r**2, xi)
    rn2_analytic = -2.0 * A * alpha_tor * r_p**2

    def GEn(q):
        return np.trapezoid(H * j0(q * r), xi)

    rn2_slope = -6.0 * derivative_wrt_q2_at_zero(GEn)

    print("\n[Parâmetros geométricos]")
    print(f"  alpha                             : {alpha:.12f}")
    print(f"  Lambda_C                          : {Lambda_C:.6f} fm")
    print(f"  R_B                               : {R_B:.6f} fm")
    print(f"  C_r                               : {C_r:.12f}")
    print(f"  epsilon_eff                       : {epsilon_eff:.12f}")
    print(f"  r_p                               : {r_p:.12f} fm")
    print(f"  mu_n                              : {mu_n:.12f} mu_N")

    print("\n[Perfil H_n variacional]")
    print(f"  alpha_tor^(2)                     : {alpha_tor:.12f}")
    print(f"  xi_+                              : {xi_plus:+.12f} fm")
    print(f"  xi_-                              : {xi_minus:+.12f} fm")
    print(f"  sigma_r=sqrt(2 tau_n)             : {sigma_r:.12f} fm")
    print(f"  tau_n                             : {tau_n:.12e} fm^2")
    print(f"  integral H_n                      : {charge:+.12e}")

    print("\n[Baixa energia]")
    print(f"  G_E^n(0)                          : {GEn(0.0):+.12e}")
    print(f"  <r_n^2> por momento               : {rn2_moment:+.12f} fm^2")
    print(f"  <r_n^2> analítico                 : {rn2_analytic:+.12f} fm^2")
    print(f"  -6 dG_E^n/dq^2|0                  : {rn2_slope:+.12f} fm^2")
    print(f"  erro momento vs analítico         : {(rn2_moment-rn2_analytic):+.3e} fm^2")
    print(f"  erro inclinação vs analítico      : {(rn2_slope-rn2_analytic):+.3e} fm^2")

    q = np.linspace(0.0, 8.0, 801)
    GE = np.array([GEn(qq) for qq in q])

    # Amostragem compacta para o relatório.
    sample_q = np.array([0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0])
    sample_GE = np.array([GEn(qq) for qq in sample_q])

    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../figs"))
    os.makedirs(fig_dir, exist_ok=True)

    profile_path = os.path.join(fig_dir, "neutron_hn_variational_q40.png")
    form_path = os.path.join(fig_dir, "neutron_ge_variational_q40.png")

    plt.figure(figsize=(9, 5))
    plt.plot(xi, H, label=r"$H_n(\xi,\tau_n)$")
    plt.axvline(xi_plus, color="tab:green", linestyle=":", label=r"$\xi_+$")
    plt.axvline(xi_minus, color="tab:red", linestyle=":", label=r"$\xi_-$")
    plt.xlabel(r"$\xi=r-r_p$ (fm)")
    plt.ylabel(r"$H_n$ (fm$^{-1}$)")
    plt.title("Q40 — Perfil torsional variacional do nêutron")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(profile_path, dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.plot(q, GE, label=r"$G_E^n$ variacional")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel(r"$G_E^n(q^2)$")
    plt.title("Q40 — Fator de forma elétrico do nêutron")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(form_path, dpi=150)
    plt.close()

    report_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "saida_hn_variational_q40.md")
    )

    table = "\n".join(
        f"| {qq:.2f} | {gg:+.12e} |" for qq, gg in zip(sample_q, sample_GE)
    )

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            f"""# Relatório: solução variacional de H_n(chi) — Q40

## 1. Equação variacional

O perfil torsional do nêutron é tratado como solução do fluxo de calor de
Perelman na camada local de superfície:

\\[
H_n(\\xi,\\tau_n)
=
|\\mu_n|
\\left[
K_{{\\tau_n}}(\\xi,\\xi_+)-K_{{\\tau_n}}(\\xi,\\xi_-)
\\right].
\\]

Com:

\\[
K_\\tau(\\xi,\\xi_0)
=
\\frac{{1}}{{\\sqrt{{4\\pi\\tau}}}}
\\exp\\left[-\\frac{{(\\xi-\\xi_0)^2}}{{4\\tau}}\\right].
\\]

## 2. Parâmetros derivados

- \\(r_p={r_p:.12f}\\,\\mathrm{{fm}}\\);
- \\(|\\mu_n|={A:.12f}\\);
- \\(\\alpha_{{\\rm tor}}^{{(2)}}={alpha_tor:.12f}\\);
- \\(\\xi_+={xi_plus:+.12f}\\,\\mathrm{{fm}}\\);
- \\(\\xi_-={xi_minus:+.12f}\\,\\mathrm{{fm}}\\);
- \\(\\sigma_r={sigma_r:.12f}\\,\\mathrm{{fm}}\\);
- \\(\\tau_n={tau_n:.12e}\\,\\mathrm{{fm}}^2\\).

## 3. Verificações

\\[
\\int H_n d\\xi={charge:+.12e}.
\\]

\\[
G_E^n(0)={GEn(0.0):+.12e}.
\\]

Momento direto:

\\[
\\langle r_n^2\\rangle={rn2_moment:+.12f}\\,\\mathrm{{fm}}^2.
\\]

Forma analítica:

\\[
-2|\\mu_n|\\alpha_{{\\rm tor}}^{{(2)}}r_p^2
={rn2_analytic:+.12f}\\,\\mathrm{{fm}}^2.
\\]

Inclinação:

\\[
-6\\left.\\frac{{dG_E^n}}{{dq^2}}\\right|_0
={rn2_slope:+.12f}\\,\\mathrm{{fm}}^2.
\\]

## 4. Amostra da curva

| q (fm^-1) | G_E^n(q^2) |
|---:|---:|
{table}

## 5. Status

O perfil \\(H_n(\\chi)\\) foi obtido por solução variacional líder do setor de
contorno. A curva \\(G_E^n(q^2)\\) fica determinada sem usar o raio experimental
do nêutron como entrada.

Próxima etapa, se desejada: comparar essa curva com parametrizações
experimentais de espalhamento elástico e acrescentar correções de sonda/magnetização.
"""
        )

    print("\n[Arquivos]")
    print(f"  relatório                         : {report_path}")
    print(f"  perfil H_n                        : {profile_path}")
    print(f"  curva G_E^n                       : {form_path}")
    print("=" * 96)


if __name__ == "__main__":
    main()
