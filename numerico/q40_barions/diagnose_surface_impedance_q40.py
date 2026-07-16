r"""
GDQ — Diagnóstico da impedância coletiva de superfície requerida (Q40)

Este script calcula, a partir da curva variacional GDQ e de Galster como
benchmark, qual impedância escalar efetiva seria necessária:

    G_target(q) = G_var(q) / D_required(q)

logo:

    D_required(q) = G_var(q) / G_target(q).

Em seguida comparamos:

    I_required(q) = D_required(q) - D_scalar(q),

onde D_scalar=(1+q^2/Lambda_E^2)^2 é a resposta bi-Helmholtz mínima.

Leitura:
    I_required não é adotado como teoria. Ele é um diagnóstico da forma e da
    escala que a Hessiana coletiva de superfície precisa gerar.
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


def geometry():
    alpha = 1.0 / 137.03599907
    Lambda_C = 386.159268
    R_B = 1.5 * Lambda_C
    epsilon_eff = 0.011591040463
    C_r = 0.125 * (1.0 + alpha / 4.0)
    r_p = C_r * R_B * epsilon_eff
    delta_B = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_B * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)
    alpha_tor = 2.0 * alpha * np.log(2.0 * np.pi**2)
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    return {
        "alpha": alpha,
        "r_p": r_p,
        "mu_n": mu_n,
        "alpha_tor": alpha_tor,
        "sigma_r": sigma_r,
        "tau_n": tau_n,
        "xi_plus": xi_plus,
        "xi_minus": xi_minus,
    }


def build_gvar(pars):
    A = abs(pars["mu_n"])
    half_width = 12.0 * pars["sigma_r"]
    xi = np.linspace(
        pars["xi_plus"] - half_width, pars["xi_minus"] + half_width, 24001
    )
    Kp = heat_kernel(xi, pars["xi_plus"], pars["tau_n"])
    Km = heat_kernel(xi, pars["xi_minus"], pars["tau_n"])
    Kp = Kp / np.trapezoid(Kp, xi)
    Km = Km / np.trapezoid(Km, xi)
    H = A * (Kp - Km)
    r = pars["r_p"] + xi

    def G(q):
        return np.trapezoid(H * j0(q * r), xi)

    return G


def galster(q, mu_n, eta=5.6):
    q = np.asarray(q, dtype=float)
    Q2 = (HBARC_GEV_FM * q) ** 2
    tau = Q2 / (4.0 * M_N_GEV**2)
    GD = (1.0 + Q2 / 0.71) ** -2
    return -mu_n * tau / (1.0 + eta * tau) * GD


def fit_impedance_basis(q, I_req, weights):
    r"""
    Ajuste diagnóstico em base que preserva carga/raio:

        I(q) = a x^2/(1+x) + b x^2/(1+x)^2 + c x^3/(1+x)^2,
        x = q^2/Lambda_E^2.

    Todos os termos começam como q^4, logo não alteram o termo de raio.
    """
    # O peso remove regiões onde Galster cruza muito perto de zero.
    x = q**2
    B = np.vstack(
        [
            x**2 / (1.0 + x),
            x**2 / (1.0 + x) ** 2,
            x**3 / (1.0 + x) ** 2,
        ]
    ).T
    W = np.sqrt(weights)[:, None]
    coeff, *_ = np.linalg.lstsq(W * B, W[:, 0] * I_req, rcond=None)
    return coeff, B @ coeff


def main():
    print("=" * 100)
    print("      GDQ — DIAGNÓSTICO DA IMPEDÂNCIA COLETIVA DE SUPERFÍCIE — Q40")
    print("=" * 100)

    pars = geometry()
    Gvar = build_gvar(pars)

    q = np.linspace(0.05, 6.0, 596)
    gv = np.array([Gvar(qq) for qq in q])
    gt = galster(q, pars["mu_n"])

    lambda_e = np.sqrt(12.0) / pars["r_p"]
    D_scalar = (1.0 + (q / lambda_e) ** 2) ** 2
    D_required = gv / gt
    I_required = D_required - D_scalar

    # Região diagnóstica estável: baixa/média transferência antes da oscilação
    # mais forte da curva nua.
    mask = (q >= 0.25) & (q <= 4.0) & np.isfinite(I_required) & (gt > 1.0e-6)
    weights = 1.0 / (1.0 + q[mask] ** 2)
    coeff, I_fit = fit_impedance_basis(q[mask] / lambda_e, I_required[mask], weights)

    I_model = np.full_like(q, np.nan)
    _, I_all = fit_impedance_basis(q / lambda_e, I_required, np.ones_like(q))
    # Recalcula com coeficientes do intervalo físico.
    x = (q / lambda_e) ** 2
    I_model = (
        coeff[0] * x**2 / (1.0 + x)
        + coeff[1] * x**2 / (1.0 + x) ** 2
        + coeff[2] * x**3 / (1.0 + x) ** 2
    )

    D_model = D_scalar + I_model
    G_model = gv / D_model

    def rms(curve, ref, lo, hi):
        m = (q >= lo) & (q <= hi)
        diff = curve[m] - ref[m]
        denom = np.sqrt(np.mean(ref[m] ** 2))
        return np.sqrt(np.mean(diff**2)), np.sqrt(np.mean(diff**2)) / denom

    print("\n[Parâmetros]")
    print(f"  r_p                         : {pars['r_p']:.12f} fm")
    print(f"  Lambda_E                    : {lambda_e:.9f} fm^-1")
    print(f"  alpha_tor^(2)               : {pars['alpha_tor']:.12f}")

    print("\n[Coeficientes diagnósticos da base q^4]")
    print(f"  a                           : {coeff[0]:+.9f}")
    print(f"  b                           : {coeff[1]:+.9f}")
    print(f"  c                           : {coeff[2]:+.9f}")

    print("\n[Comparação]")
    for lo, hi in [(0.25, 2.0), (0.25, 4.0)]:
        rms_scalar, rel_scalar = rms(gv / D_scalar, gt, lo, hi)
        rms_model, rel_model = rms(G_model, gt, lo, hi)
        print(
            f"  {lo:.2f} <= q <= {hi:.1f}: "
            f"escalar={100.0*rel_scalar:.3f}% | "
            f"impedância diagnóstica={100.0*rel_model:.3f}%"
        )

    sample_q = np.array([0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0])
    sample_gv = np.array([Gvar(qq) for qq in sample_q])
    sample_gt = galster(sample_q, pars["mu_n"])
    sample_D_scalar = (1.0 + (sample_q / lambda_e) ** 2) ** 2
    xs = (sample_q / lambda_e) ** 2
    sample_I = (
        coeff[0] * xs**2 / (1.0 + xs)
        + coeff[1] * xs**2 / (1.0 + xs) ** 2
        + coeff[2] * xs**3 / (1.0 + xs) ** 2
    )
    sample_model = sample_gv / (sample_D_scalar + sample_I)

    print("\n[Amostra]")
    print("  q | G_diag | Galster | I_model")
    for qq, gm, gr, ii in zip(sample_q, sample_model, sample_gt, sample_I):
        print(f"  {qq:4.2f} | {gm:+.9e} | {gr:+.9e} | {ii:+.9e}")

    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../figs"))
    os.makedirs(fig_dir, exist_ok=True)

    fig_imp = os.path.join(fig_dir, "neutron_required_impedance_q40.png")
    fig_curve = os.path.join(fig_dir, "neutron_impedance_diagnostic_curve_q40.png")

    plt.figure(figsize=(9, 5))
    plt.plot(q, I_required, label=r"$I_\Sigma$ requerida")
    plt.plot(q, I_model, "--", label="base diagnóstica $q^4$")
    plt.axhline(0.0, color="black", linewidth=0.8)
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel(r"$I_\Sigma(q)$")
    plt.title("Q40 — Impedância coletiva requerida")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_imp, dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.plot(q, gv / D_scalar, label="GDQ + superfície escalar")
    plt.plot(q, G_model, label="GDQ + impedância diagnóstica")
    plt.plot(q, gt, "--", label="Galster")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel(r"$G_E^n(q^2)$")
    plt.title("Q40 — Diagnóstico da curva com impedância coletiva")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_curve, dpi=150)
    plt.close()

    rows = "\n".join(
        f"| {qq:.2f} | {gm:+.9e} | {gr:+.9e} | {ii:+.9e} |"
        for qq, gm, gr, ii in zip(sample_q, sample_model, sample_gt, sample_I)
    )

    report_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "saida_required_impedance_q40.md")
    )
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            fr"""# Q40 — Diagnóstico da impedância coletiva requerida

## 1. Definição

Este relatório calcula a impedância escalar efetiva que seria necessária para
levar a curva variacional GDQ até uma referência Galster:

\[
D_{{\rm req}}(q)=\frac{{G_E^{{n,\rm var}}(q^2)}}{{G_E^{{n,\rm Galster}}(q^2)}}.
\]

Subtraindo o operador bi-Helmholtz mínimo:

\[
D_\Sigma(q)=\left(1+\frac{{q^2}}{{\Lambda_E^2}}\right)^2,
\]

obtemos:

\[
\mathcal I_\Sigma^{{\rm req}}(q)=D_{{\rm req}}(q)-D_\Sigma(q).
\]

Isso não é adotado como teoria. É um diagnóstico da forma e da escala que a
Hessiana coletiva de superfície precisa produzir.

## 2. Base diagnóstica

Foi usada uma base que começa em \(q^4\), preservando carga e inclinação:

\[
\mathcal I_\Sigma(q)
=
a\frac{{x^2}}{{1+x}}
+b\frac{{x^2}}{{(1+x)^2}}
+c\frac{{x^3}}{{(1+x)^2}},
\qquad
x=\frac{{q^2}}{{\Lambda_E^2}}.
\]

Coeficientes no intervalo \(0.25\le q\le4\,\mathrm{{fm}}^{{-1}}\):

\[
a={coeff[0]:+.9f},
\qquad
b={coeff[1]:+.9f},
\qquad
c={coeff[2]:+.9f}.
\]

## 3. Métricas

| Intervalo | Superfície escalar | Impedância diagnóstica |
|---|---:|---:|
| \(0.25\le q\le2.0\) | {100.0*rms(gv / D_scalar, gt, 0.25, 2.0)[1]:.3f}% | {100.0*rms(G_model, gt, 0.25, 2.0)[1]:.3f}% |
| \(0.25\le q\le4.0\) | {100.0*rms(gv / D_scalar, gt, 0.25, 4.0)[1]:.3f}% | {100.0*rms(G_model, gt, 0.25, 4.0)[1]:.3f}% |

## 4. Amostra

| q (fm^-1) | GDQ + impedância diagnóstica | Galster | \(\mathcal I_\Sigma\) |
|---:|---:|---:|---:|
{rows}

## 5. Leitura

A impedância requerida começa em \(q^4\), portanto pode preservar carga e raio.
Sua magnitude é de ordem geométrica, não de ordem
\((\alpha_{{\rm tor}}^{{(2)}})^2\). Isso explica por que a Hessiana EMT mínima
foi insuficiente: a correção necessária é coletiva da superfície, não apenas
mistura perturbativa local entre \(E\), \(M\) e torção.

Figuras:

- `{fig_imp}`;
- `{fig_curve}`.
"""
        )

    print("\n[Arquivos]")
    print(f"  relatório                    : {report_path}")
    print(f"  impedância                   : {fig_imp}")
    print(f"  curva                         : {fig_curve}")
    print("=" * 100)


if __name__ == "__main__":
    main()
