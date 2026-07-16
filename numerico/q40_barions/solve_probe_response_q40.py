r"""
GDQ — Hessiana reduzida da sonda eletromagnética/magnética (Q40)

Objetivo:
    Implementar o primeiro solver da resposta linear de superfície:

        H_Sigma(q) deltaPhi(q) = J_em(q),
        Phi = (rho_E, rho_M, T_Sigma).

    A curva física é construída como:

        G_E^phys(q^2) = F_EMT(q) G_E^var(q^2),

    onde F_EMT(q) é obtido do complemento de Schur da Hessiana reduzida.

Importante:
    Este script não ajusta parâmetros para Galster. Galster entra apenas como
    benchmark fenomenológico. Os coeficientes da Hessiana mínima são fixados
    por escalas geométricas já usadas em Q40:

        r_p,
        alpha_tor^(2),
        |mu_n|,
        delta_B.

    O resultado deve ser lido como teste da Hessiana mínima, não como prova
    final da curva experimental.
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


def derivative_wrt_q2_at_zero(func, h=1.0e-5):
    f0 = func(0.0)
    f1 = func(np.sqrt(h))
    f2 = func(np.sqrt(2.0 * h))
    return (-3.0 * f0 + 4.0 * f1 - f2) / (2.0 * h)


def build_geometry():
    alpha = 1.0 / 137.03599907
    Lambda_C = 386.159268  # fm
    R_B = 1.5 * Lambda_C
    epsilon_eff = 0.011591040463
    C_r = 0.125 * (1.0 + alpha / 4.0)
    r_p = C_r * R_B * epsilon_eff

    delta_B = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_n = -(3.0 / 4.0) * delta_B * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)
    mu_p = 1.0 + (3.0 / 5.0) * np.log(2.0 * np.pi**2) * (1.0 + alpha / 4.0)

    alpha_tor = 2.0 * alpha * np.log(2.0 * np.pi**2)
    xi_plus = -0.5 * r_p * alpha_tor
    xi_minus = +0.5 * r_p * alpha_tor
    sigma_r = 0.5 * r_p * alpha_tor
    tau_n = 0.5 * sigma_r**2

    return {
        "alpha": alpha,
        "Lambda_C": Lambda_C,
        "R_B": R_B,
        "epsilon_eff": epsilon_eff,
        "C_r": C_r,
        "r_p": r_p,
        "delta_B": delta_B,
        "mu_n": mu_n,
        "mu_p": mu_p,
        "alpha_tor": alpha_tor,
        "xi_plus": xi_plus,
        "xi_minus": xi_minus,
        "sigma_r": sigma_r,
        "tau_n": tau_n,
    }


def build_variational_curve(pars):
    A = abs(pars["mu_n"])
    xi_plus = pars["xi_plus"]
    xi_minus = pars["xi_minus"]
    tau_n = pars["tau_n"]
    sigma_r = pars["sigma_r"]
    r_p = pars["r_p"]

    half_width = 12.0 * sigma_r
    xi = np.linspace(xi_plus - half_width, xi_minus + half_width, 24001)
    K_plus = heat_kernel(xi, xi_plus, tau_n)
    K_minus = heat_kernel(xi, xi_minus, tau_n)
    K_plus = K_plus / np.trapezoid(K_plus, xi)
    K_minus = K_minus / np.trapezoid(K_minus, xi)
    H = A * (K_plus - K_minus)
    r = r_p + xi

    def G_var(q_fm):
        return np.trapezoid(H * j0(q_fm * r), xi)

    return G_var, xi, H


def galster(q_fm, mu_n, eta=5.6):
    q_fm = np.asarray(q_fm, dtype=float)
    Q2 = (HBARC_GEV_FM * q_fm) ** 2
    tau = Q2 / (4.0 * M_N_GEV**2)
    G_D = (1.0 + Q2 / 0.71) ** -2
    return -mu_n * tau / (1.0 + eta * tau) * G_D


def scalar_surface_filter(q_fm, r_p):
    q_fm = np.asarray(q_fm, dtype=float)
    lambda_sigma = np.sqrt(12.0) / r_p
    return (1.0 + (q_fm / lambda_sigma) ** 2) ** -2


def hessian_emt(q_fm, pars):
    r"""
    Hessiana reduzida em espaço de momento.

    Forma mínima:

        H = [[D_E, C_EM, C_ET],
             [C_EM, D_M, C_MT],
             [C_ET, C_MT, D_T]]

    com acoplamentos proporcionais a q^2 para preservar a carga e a inclinação
    do nêutron no limite q -> 0.

    Escalas:
        Lambda_E = sqrt(12)/r_p: escala de superfície elétrica;
        Lambda_M = sqrt(12)/(r_p sqrt(|mu_n|/mu_p)): magnetização mais larga;
        Lambda_T = 1/sigma_r: escala curta torsional.

    Coeficientes adimensionais:
        g_EM = alpha_tor |mu_n|/mu_p;
        g_ET = alpha_tor;
        g_MT = alpha_tor sqrt(|mu_n|/mu_p).

    Essa escolha codifica que a mistura é torsional e desaparece no limite
    alpha_tor -> 0.
    """
    q = float(q_fm)
    r_p = pars["r_p"]
    alpha_tor = pars["alpha_tor"]
    mu_ratio = abs(pars["mu_n"]) / pars["mu_p"]
    sigma_r = pars["sigma_r"]

    Lambda_E = np.sqrt(12.0) / r_p
    Lambda_M = np.sqrt(12.0) / (r_p * np.sqrt(mu_ratio))
    Lambda_T = 1.0 / sigma_r

    xE = q / Lambda_E
    xM = q / Lambda_M
    xT = q / Lambda_T

    D_E = (1.0 + xE**2) ** 2
    D_M = 1.0 + xM**2
    D_T = 1.0 + xT**2

    g_EM = alpha_tor * mu_ratio
    g_ET = alpha_tor
    g_MT = alpha_tor * np.sqrt(mu_ratio)

    C_EM = g_EM * xE * xM
    C_ET = g_ET * xE * xT
    C_MT = g_MT * xM * xT

    return np.array(
        [
            [D_E, C_EM, C_ET],
            [C_EM, D_M, C_MT],
            [C_ET, C_MT, D_T],
        ],
        dtype=float,
    )


def emt_response_filter(q_fm, pars):
    r"""
    Resposta elétrica efetiva por complemento de Schur.

    A fonte elétrica nua acopla ao canal E. Integrando M e T, o propagador
    efetivo é:

        R_EE = 1 / (D_E - v^T B^{-1} v).

    Como H(0)=I, F_EMT(0)=1.
    """
    q = np.asarray(q_fm, dtype=float)
    out = np.empty_like(q)

    for idx, qq in np.ndenumerate(q):
        H = hessian_emt(float(qq), pars)
        D_E = H[0, 0]
        v = H[0, 1:3]
        B = H[1:3, 1:3]
        D_eff = D_E - v @ np.linalg.solve(B, v)
        out[idx] = 1.0 / D_eff

    if np.ndim(q_fm) == 0:
        return float(out)
    return out


def rms_metrics(q, model, ref):
    masks = {
        "0.0 <= q <= 2.0 fm^-1": (q >= 0.0) & (q <= 2.0),
        "0.0 <= q <= 4.0 fm^-1": (q >= 0.0) & (q <= 4.0),
        "0.5 <= q <= 4.0 fm^-1": (q >= 0.5) & (q <= 4.0),
    }
    rows = []
    for label, mask in masks.items():
        diff = model[mask] - ref[mask]
        rms = np.sqrt(np.mean(diff**2))
        denom = np.sqrt(np.mean(ref[mask] ** 2))
        rel = rms / denom if denom > 0 else np.nan
        rows.append((label, rms, rel))
    return rows


def main():
    print("=" * 100)
    print("      GDQ — HESSIANA REDUZIDA DA SONDA ELETROMAGNÉTICA/MAGNÉTICA — Q40")
    print("=" * 100)

    pars = build_geometry()
    G_var, xi, H_profile = build_variational_curve(pars)

    q = np.linspace(0.0, 8.0, 801)
    G_nua = np.array([G_var(qq) for qq in q])
    F_sigma = scalar_surface_filter(q, pars["r_p"])
    F_emt = emt_response_filter(q, pars)
    G_sigma = F_sigma * G_nua
    G_emt = F_emt * G_nua
    G_ref = galster(q, pars["mu_n"])

    def G_emt_func(qq):
        return emt_response_filter(qq, pars) * G_var(qq)

    rn2_var = -6.0 * derivative_wrt_q2_at_zero(G_var)
    rn2_emt = -6.0 * derivative_wrt_q2_at_zero(G_emt_func)

    print("\n[Parâmetros geométricos]")
    print(f"  r_p                         : {pars['r_p']:.12f} fm")
    print(f"  mu_n                        : {pars['mu_n']:.12f} mu_N")
    print(f"  mu_p                        : {pars['mu_p']:.12f} mu_N")
    print(f"  alpha_tor^(2)               : {pars['alpha_tor']:.12f}")
    print(f"  sigma_r                     : {pars['sigma_r']:.12f} fm")

    lambda_e = np.sqrt(12.0) / pars["r_p"]
    lambda_m = np.sqrt(12.0) / (
        pars["r_p"] * np.sqrt(abs(pars["mu_n"]) / pars["mu_p"])
    )
    lambda_t = 1.0 / pars["sigma_r"]
    print("\n[Escalas da Hessiana]")
    print(f"  Lambda_E                    : {lambda_e:.9f} fm^-1")
    print(f"  Lambda_M                    : {lambda_m:.9f} fm^-1")
    print(f"  Lambda_T                    : {lambda_t:.9f} fm^-1")

    print("\n[Baixa energia]")
    print(f"  G_var(0)                    : {G_var(0.0):+.12e}")
    print(f"  G_EMT(0)                    : {G_emt_func(0.0):+.12e}")
    print(f"  <r_n^2> variacional         : {rn2_var:+.12f} fm^2")
    print(f"  <r_n^2> EMT                 : {rn2_emt:+.12f} fm^2")
    print(f"  diferença                   : {rn2_emt-rn2_var:+.3e} fm^2")

    print("\n[Comparação contra Galster — benchmark, não ajuste]")
    for name, curve in [
        ("nua", G_nua),
        ("superfície", G_sigma),
        ("Hessiana EMT", G_emt),
    ]:
        print(f"\n  {name}:")
        for label, rms, rel in rms_metrics(q, curve, G_ref):
            print(f"    {label:24s}: RMS={rms:.6e} | rel={100.0*rel:.3f}%")

    q_peak_emt = q[np.argmax(G_emt)]
    q_peak_ref = q[np.argmax(G_ref)]
    print("\n[Picos]")
    print(f"  EMT                         : q={q_peak_emt:.3f} fm^-1 | G={np.max(G_emt):.9f}")
    print(f"  Galster                     : q={q_peak_ref:.3f} fm^-1 | G={np.max(G_ref):.9f}")

    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../figs"))
    os.makedirs(fig_dir, exist_ok=True)
    fig_path = os.path.join(fig_dir, "neutron_ge_probe_response_q40.png")

    plt.figure(figsize=(9, 5))
    plt.plot(q, G_nua, label="GDQ nua", alpha=0.75)
    plt.plot(q, G_sigma, label="GDQ + superfície escalar", alpha=0.9)
    plt.plot(q, G_emt, label="GDQ + Hessiana EMT")
    plt.plot(q, G_ref, "--", label="Galster (benchmark)")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel(r"$G_E^n(q^2)$")
    plt.title("Q40 — Resposta de sonda por Hessiana EMT")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()

    response_path = os.path.join(fig_dir, "neutron_probe_filters_q40.png")
    plt.figure(figsize=(9, 5))
    plt.plot(q, F_sigma, label=r"$F_\Sigma$")
    plt.plot(q, F_emt, label=r"$F_{\rm EMT}$")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel("fator de resposta")
    plt.title("Q40 — Fatores de resposta da superfície")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(response_path, dpi=150)
    plt.close()

    sample_q = np.array([0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0])
    sample_nua = np.array([G_var(qq) for qq in sample_q])
    sample_emt = emt_response_filter(sample_q, pars) * sample_nua
    sample_ref = galster(sample_q, pars["mu_n"])
    sample_rows = "\n".join(
        f"| {qq:.2f} | {nn:+.9e} | {ee:+.9e} | {rr:+.9e} | {ee-rr:+.9e} |"
        for qq, nn, ee, rr in zip(sample_q, sample_nua, sample_emt, sample_ref)
    )

    metric_sections = []
    for name, curve in [
        ("GDQ nua", G_nua),
        ("GDQ + superfície escalar", G_sigma),
        ("GDQ + Hessiana EMT", G_emt),
    ]:
        rows = "\n".join(
            f"| {label} | {rms:.6e} | {100.0*rel:.3f}% |"
            for label, rms, rel in rms_metrics(q, curve, G_ref)
        )
        metric_sections.append(
            f"### {name}\n\n| Intervalo | RMS | RMS relativo |\n|---|---:|---:|\n{rows}\n"
        )

    report_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "saida_probe_response_q40.md")
    )
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(
            fr"""# Q40 — Hessiana reduzida da sonda eletromagnética/magnética

## 1. Objetivo

Este relatório implementa o primeiro solver da resposta linear:

\[
H_\Sigma(q)\delta\Phi(q)=J_{{\rm em}}(q),
\qquad
\Phi=(\rho_E,\rho_M,T_\Sigma).
\]

A curva física é:

\[
G_E^{{n,\rm phys}}(q^2)
=
F_{{\rm EMT}}(q)G_E^{{n,\rm var}}(q^2),
\]

onde \(F_{{\rm EMT}}\) é obtido pelo complemento de Schur da Hessiana reduzida.
Galster é usado apenas como benchmark externo de forma.

## 2. Hessiana mínima

\[
H_\Sigma=
\begin{{pmatrix}}
D_E & C_{{EM}} & C_{{ET}}\\
C_{{EM}} & D_M & C_{{MT}}\\
C_{{ET}} & C_{{MT}} & D_T
\end{{pmatrix}}.
\]

Com:

\[
D_E=(1+q^2/\Lambda_E^2)^2,
\qquad
D_M=1+q^2/\Lambda_M^2,
\qquad
D_T=1+q^2/\Lambda_T^2.
\]

Os acoplamentos cruzados são proporcionais a \(q^2\), de modo que a carga e a
inclinação no zero sejam preservadas:

\[
C_{{ij}}\propto q^2.
\]

Escalas usadas:

- \(\Lambda_E={lambda_e:.9f}\,\mathrm{{fm}}^{{-1}}\);
- \(\Lambda_M={lambda_m:.9f}\,\mathrm{{fm}}^{{-1}}\);
- \(\Lambda_T={lambda_t:.9f}\,\mathrm{{fm}}^{{-1}}\).

## 3. Baixa energia

\[
G_E^{{n,\rm var}}(0)={G_var(0.0):+.12e},
\qquad
G_E^{{n,\rm EMT}}(0)={G_emt_func(0.0):+.12e}.
\]

\[
\langle r_n^2\rangle_{{\rm var}}
={rn2_var:+.12f}\,\mathrm{{fm}}^2,
\qquad
\langle r_n^2\rangle_{{\rm EMT}}
={rn2_emt:+.12f}\,\mathrm{{fm}}^2.
\]

Diferença:

\[
\Delta\langle r_n^2\rangle={rn2_emt-rn2_var:+.3e}\,\mathrm{{fm}}^2.
\]

## 4. Comparação fenomenológica

{chr(10).join(metric_sections)}

## 5. Amostra

| q (fm^-1) | GDQ nua | GDQ + Hessiana EMT | Galster | Diferença EMT |
|---:|---:|---:|---:|---:|
{sample_rows}

## 6. Leitura

A Hessiana EMT mínima preserva os vínculos de baixa energia, mas seus
acoplamentos torsionais geométricos são pequenos. Portanto, ela não substitui
sozinha o operador completo de sonda. O resultado separa claramente:

1. vínculos estruturais já fechados: carga e raio;
2. resposta escalar de superfície: melhora parcial;
3. mistura EMT mínima: correção perturbativa pequena;
4. pendência real: calcular os coeficientes de \(H_\Sigma\) diretamente da
   Hessiana completa da ação GDQ no setor de contorno.

Figuras:

- `{fig_path}`;
- `{response_path}`.
"""
        )

    print("\n[Arquivos]")
    print(f"  relatório                    : {report_path}")
    print(f"  curva                         : {fig_path}")
    print(f"  filtros                       : {response_path}")
    print("=" * 100)


if __name__ == "__main__":
    main()
