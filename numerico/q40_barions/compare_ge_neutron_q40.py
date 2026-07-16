r"""
GDQ — Comparação fenomenológica de G_E^n variacional com Galster (Q40)

Este script não ajusta parâmetros da GDQ. Ele usa a curva variacional já
derivada para o nêutron:

    H_n(xi,tau_n) = |mu_n| [K_tau(xi,xi_+) - K_tau(xi,xi_-)]

e compara sua forma com a parametrização de Galster, usada aqui apenas como
referência fenomenológica compacta de espalhamento elástico.

Convenção:
    q em fm^-1,
    Q^2_GeV = (hbar c q)^2.
"""

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import numpy as np
import matplotlib.pyplot as plt


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


def build_gdq_curve():
    alpha = 1.0 / 137.03599907
    Lambda_C = 386.159268  # fm
    R_B = 1.5 * Lambda_C
    epsilon_eff = 0.011591040463
    C_r = 0.125 * (1.0 + alpha / 4.0)
    r_p = C_r * R_B * epsilon_eff

    delta_B = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_B * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)
    A = abs(mu_n)

    alpha_tor = 2.0 * alpha * np.log(2.0 * np.pi**2)
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2

    half_width = 12.0 * sigma_r
    xi = np.linspace(xi_plus - half_width, xi_minus + half_width, 24001)
    K_plus = heat_kernel(xi, xi_plus, tau_n)
    K_minus = heat_kernel(xi, xi_minus, tau_n)
    K_plus = K_plus / np.trapezoid(K_plus, xi)
    K_minus = K_minus / np.trapezoid(K_minus, xi)
    H = A * (K_plus - K_minus)
    r = r_p + xi

    def GEn(q_fm):
        return np.trapezoid(H * j0(q_fm * r), xi)

    return GEn, {
        "alpha": alpha,
        "r_p": r_p,
        "mu_n": mu_n,
        "alpha_tor": alpha_tor,
        "tau_n": tau_n,
    }


def galster(q_fm, mu_n, eta=5.6):
    q_fm = np.asarray(q_fm, dtype=float)
    Q2 = (HBARC_GEV_FM * q_fm) ** 2
    tau = Q2 / (4.0 * M_N_GEV**2)
    G_D = (1.0 + Q2 / 0.71) ** -2
    return -mu_n * tau / (1.0 + eta * tau) * G_D


def gdq_surface_probe(q_fm, r_p):
    r"""
    Operador de sonda/superfície líder.

    A casca composta não é medida como distribuição nua de delta suavizada; a
    sonda eletromagnética enxerga a resposta Green efetiva da superfície. O
    operador bi-Helmholtz mínimo fornece:

        F_Sigma(q) = (1 + q^2/Lambda_Sigma^2)^(-2)

    com Lambda_Sigma fixado pelo raio de superfície:

        Lambda_Sigma = sqrt(12)/r_p.

    Como F_Sigma(0)=1, a carga nula e a inclinação de G_E^n em q=0 são
    preservadas.
    """
    q_fm = np.asarray(q_fm, dtype=float)
    lambda_sigma = np.sqrt(12.0) / r_p
    return (1.0 + (q_fm / lambda_sigma) ** 2) ** -2


def main():
    print("=" * 96)
    print("      GDQ — COMPARAÇÃO G_E^n VARIACIONAL COM GALSTER — Q40")
    print("=" * 96)

    GEn_gdq, pars = build_gdq_curve()
    q = np.linspace(0.0, 8.0, 801)
    gdq = np.array([GEn_gdq(qq) for qq in q])
    gdq_probe = gdq * gdq_surface_probe(q, pars["r_p"])
    ref = galster(q, pars["mu_n"])

    # Métricas em regiões típicas de baixa e média transferência.
    masks = {
        "0.0 <= q <= 2.0 fm^-1": (q >= 0.0) & (q <= 2.0),
        "0.0 <= q <= 4.0 fm^-1": (q >= 0.0) & (q <= 4.0),
        "0.5 <= q <= 4.0 fm^-1": (q >= 0.5) & (q <= 4.0),
    }

    print("\n[Parâmetros GDQ usados]")
    print(f"  r_p                 : {pars['r_p']:.12f} fm")
    print(f"  mu_n                : {pars['mu_n']:.12f} mu_N")
    print(f"  alpha_tor^(2)       : {pars['alpha_tor']:.12f}")
    print(f"  tau_n               : {pars['tau_n']:.12e} fm^2")

    print("\n[Comparação de forma — Galster como referência externa compacta]")
    for label, mask in masks.items():
        diff = gdq[mask] - ref[mask]
        rms = np.sqrt(np.mean(diff**2))
        denom = np.sqrt(np.mean(ref[mask] ** 2))
        rel = rms / denom if denom > 0 else np.nan
        diff_probe = gdq_probe[mask] - ref[mask]
        rms_probe = np.sqrt(np.mean(diff_probe**2))
        rel_probe = rms_probe / denom if denom > 0 else np.nan
        print(
            f"  {label:24s}: nu={rms:.6e} ({100.0*rel:.3f}%) | "
            f"sonda={rms_probe:.6e} ({100.0*rel_probe:.3f}%)"
        )

    q_peak_gdq = q[np.argmax(gdq)]
    q_peak_probe = q[np.argmax(gdq_probe)]
    q_peak_ref = q[np.argmax(ref)]
    print("\n[Picos]")
    print(f"  GDQ     : q={q_peak_gdq:.3f} fm^-1 | G_E^n={np.max(gdq):.9f}")
    print(f"  GDQ+S   : q={q_peak_probe:.3f} fm^-1 | G_E^n={np.max(gdq_probe):.9f}")
    print(f"  Galster : q={q_peak_ref:.3f} fm^-1 | G_E^n={np.max(ref):.9f}")

    sample_q = np.array([0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0])
    sample_gdq = np.array([GEn_gdq(qq) for qq in sample_q])
    sample_probe = sample_gdq * gdq_surface_probe(sample_q, pars["r_p"])
    sample_ref = galster(sample_q, pars["mu_n"])

    print("\n[Amostra]")
    print("  q(fm^-1) | GDQ nua       | GDQ+sonda     | Galster       | Dif. sonda")
    for qq, gg, pp, rr in zip(sample_q, sample_gdq, sample_probe, sample_ref):
        print(f"  {qq:8.2f} | {gg:+.9e} | {pp:+.9e} | {rr:+.9e} | {pp-rr:+.9e}")

    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../figs"))
    os.makedirs(fig_dir, exist_ok=True)
    fig_path = os.path.join(fig_dir, "neutron_ge_gdq_vs_galster_q40.png")

    plt.figure(figsize=(9, 5))
    plt.plot(q, gdq, label="GDQ variacional líder")
    plt.plot(q, gdq_probe, label="GDQ + sonda de superfície")
    plt.plot(q, ref, "--", label="Galster (benchmark)")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel(r"$G_E^n(q^2)$")
    plt.title("Q40 — Comparação fenomenológica de forma para $G_E^n$")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()

    report_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "saida_compare_ge_neutron_q40.md")
    )

    metric_rows = []
    for label, mask in masks.items():
        diff = gdq[mask] - ref[mask]
        rms = np.sqrt(np.mean(diff**2))
        denom = np.sqrt(np.mean(ref[mask] ** 2))
        rel = rms / denom if denom > 0 else np.nan
        diff_probe = gdq_probe[mask] - ref[mask]
        rms_probe = np.sqrt(np.mean(diff_probe**2))
        rel_probe = rms_probe / denom if denom > 0 else np.nan
        metric_rows.append(
            f"| {label} | {rms:.6e} | {100.0*rel:.3f}% | "
            f"{rms_probe:.6e} | {100.0*rel_probe:.3f}% |"
        )

    sample_rows = "\n".join(
        f"| {qq:.2f} | {gg:+.9e} | {pp:+.9e} | {rr:+.9e} | {pp-rr:+.9e} |"
        for qq, gg, pp, rr in zip(sample_q, sample_gdq, sample_probe, sample_ref)
    )

    lambda_sigma = np.sqrt(12.0) / pars["r_p"]
    lambda_sigma_gev = HBARC_GEV_FM * lambda_sigma

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            fr"""# Q40 — Comparação de \(G_E^n\) variacional com Galster

Este relatório compara a curva variacional líder da GDQ para o fator de forma
elétrico do nêutron com a parametrização de Galster. Galster é usado aqui
somente como referência fenomenológica compacta; nenhum parâmetro da GDQ é
ajustado por ela.

## 1. Entrada GDQ

- \(r_p={pars['r_p']:.12f}\\,\\mathrm{{fm}}\);
- \(\mu_n={pars['mu_n']:.12f}\\,\\mu_N\);
- \(\alpha_{{\\rm tor}}^{{(2)}}={pars['alpha_tor']:.12f}\);
- \(\tau_n={pars['tau_n']:.12e}\\,\\mathrm{{fm}}^2\).

## 2. Referência Galster

Foi usada a forma:

\\[
G_E^n(Q^2)
=
-\mu_n
\\frac{{\\tau}}{{1+\\eta\\tau}}
G_D(Q^2),
\\qquad
\\tau=\\frac{{Q^2}}{{4M_N^2}},
\\qquad
G_D=(1+Q^2/0.71)^{{-2}},
\\]

com \(\eta=5.6\), \(M_N={M_N_GEV}\\,\\mathrm{{GeV}}\) e
\(Q^2=(\\hbar c q)^2\).

## 3. Métricas de forma

Além da curva nua, foi testado o operador de sonda/superfície:

\[
F_\Sigma(q)=\left(1+\frac{{q^2}}{{\Lambda_\Sigma^2}}\right)^{{-2}},
\qquad
\Lambda_\Sigma=\frac{{\sqrt{{12}}}}{{r_p}}
={lambda_sigma:.9f}\,\mathrm{{fm}}^{{-1}}
={lambda_sigma_gev:.9f}\,\mathrm{{GeV}}.
\]

Como \(F_\Sigma(0)=1\), esse fator não altera \(G_E^n(0)\) nem a inclinação em
\(q=0\). Ele só representa a resposta finita da superfície composta em
transferência intermediária.

| Intervalo | RMS nu | RMS rel. nu | RMS sonda | RMS rel. sonda |
|---|---:|---:|---:|---:|
{chr(10).join(metric_rows)}

## 4. Picos

- GDQ nua: \(q={q_peak_gdq:.3f}\\,\\mathrm{{fm}}^{{-1}}\),
  \(G_E^n={np.max(gdq):.9f}\);
- GDQ + sonda: \(q={q_peak_probe:.3f}\\,\\mathrm{{fm}}^{{-1}}\),
  \(G_E^n={np.max(gdq_probe):.9f}\);
- Galster: \(q={q_peak_ref:.3f}\\,\\mathrm{{fm}}^{{-1}}\),
  \(G_E^n={np.max(ref):.9f}\).

## 5. Amostra

| q (fm^-1) | GDQ nua | GDQ + sonda | Galster | Dif. sonda |
|---:|---:|---:|---:|---:|
{sample_rows}

## 6. Leitura física

A curva GDQ nua acerta automaticamente a carga nula e o raio quadrático
negativo por construção variacional do perfil torsional. O operador
bi-Helmholtz de superfície reduz a oscilação intermediária sem tocar nos
vínculos de baixa energia. A pendência que sobra é derivar a forma completa do
operador de sonda/magnetização a partir da Hessiana eletromagnética da ação
GDQ, em vez de manter apenas seu fator líder de superfície.

Figura gerada:

`{fig_path}`
"""
        )

    print("\n[Arquivos]")
    print(f"  relatório : {report_path}")
    print(f"  figura    : {fig_path}")
    print("=" * 96)


if __name__ == "__main__":
    main()
