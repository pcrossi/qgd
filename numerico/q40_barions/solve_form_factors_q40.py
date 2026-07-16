r"""
GDQ — Fatores de forma bariônicos de superfície (Q40)

Este script implementa o fechamento estrutural mínimo dos fatores de forma de
Sachs para próton e nêutron.

Regra central:
    O espalhamento eletromagnético mede a coordenada projetada de superfície
    da garganta/estômato:

        r_obs(chi) = C_r R_B chi

    e não o raio volumétrico bruto R_B chi.

O próton é modelado, no limite líder, como uma casca elétrica de superfície em
chi = epsilon_eff. O nêutron é modelado em dois níveis:

    1. polarização líder mínima;
    2. polarização estendida de cola dupla torsional.

Nenhum dos dois usa o raio experimental do nêutron como entrada.
"""

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import numpy as np
import matplotlib.pyplot as plt


def j0(x):
    """Bessel esférica j_0(x)=sin(x)/x com limite regular em x=0."""

    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    mask = np.abs(x) > 1.0e-12
    out[mask] = np.sin(x[mask]) / x[mask]
    return out


def derivative_wrt_q2_at_zero(func, h=1.0e-5):
    """Derivada dF/d(q^2) em q^2=0 usando q=sqrt(t)."""

    t0 = 0.0
    t1 = h
    t2 = 2.0 * h
    f0 = func(np.sqrt(t0))
    f1 = func(np.sqrt(t1))
    f2 = func(np.sqrt(t2))
    # Fórmula progressiva de segunda ordem para f'(0).
    return (-3.0 * f0 + 4.0 * f1 - f2) / (2.0 * h)


def normalized_gaussian(x, center, sigma):
    """Gaussiana normalizada numericamente no grid fornecido."""

    w = np.exp(-0.5 * ((x - center) / sigma) ** 2)
    norm = np.trapezoid(w, x)
    return w / norm


def run():
    print("=" * 92)
    print("  GEOMETRODINÂMICA QUÂNTICA — FATORES DE FORMA DE SUPERFÍCIE (Q40)")
    print("=" * 92)

    alpha = 1.0 / 137.03599907
    Lambda_C = 386.159268  # fm
    R_B = 1.5 * Lambda_C
    epsilon_eff = 0.011591040463
    C_r = 0.125 * (1.0 + alpha / 4.0)
    c_scale = C_r * R_B
    r_p = c_scale * epsilon_eff

    delta_B = np.log(2.0 * np.pi**2) * (3.0 * np.sqrt(2.0) / 5.0)
    mu_p = 1.0 + (3.0 / 5.0) * np.log(2.0 * np.pi**2) * (1.0 + alpha / 4.0)
    mu_n = -(3.0 / 4.0) * delta_B * (1.0 + alpha * 3.0 * np.sqrt(2.0) / 4.0)

    # Modelo estrutural mínimo para polarização elétrica do nêutron.
    # Não usa o raio experimental do nêutron. Apenas codifica: carga total zero,
    # componente negativa mais periférica e escala de separação de superfície.
    A_n = alpha * delta_B
    chi_plus = epsilon_eff * (1.0 - alpha / 2.0)
    chi_minus = epsilon_eff * (1.0 + alpha / 2.0)
    r_plus = c_scale * chi_plus
    r_minus = c_scale * chi_minus
    rn2_model = A_n * (r_plus**2 - r_minus**2)
    rn2_leading = -2.0 * alpha**2 * delta_B * r_p**2

    # Fechamento estendido de cola dupla:
    # A amplitude é a projeção torsional espacial que já fixa |mu_n|.
    # O deslocamento relativo é duas vezes o comprimento torsional global
    # alpha ln(2 pi^2), pois o nêutron contém duas interfaces antiparalelas.
    A_n_ext = abs(mu_n)
    alpha_tor_ext = 2.0 * alpha * np.log(2.0 * np.pi**2)
    r_plus_ext = r_p * (1.0 - alpha_tor_ext / 2.0)
    r_minus_ext = r_p * (1.0 + alpha_tor_ext / 2.0)
    rn2_ext = A_n_ext * (r_plus_ext**2 - r_minus_ext**2)

    # Perfil suave local da camada de superfície.
    # A variável xi atravessa o contorno do estômato: r = r_p + xi.
    # Isso evita cortar artificialmente a componente interna positiva.
    xi_plus = r_plus_ext - r_p
    xi_minus = r_minus_ext - r_p
    sigma_r = 0.5 * r_p * alpha_tor_ext
    xi_span = 10.0 * sigma_r
    xi = np.linspace(xi_plus - xi_span, xi_minus + xi_span, 12001)
    w_plus = normalized_gaussian(xi, xi_plus, sigma_r)
    w_minus = normalized_gaussian(xi, xi_minus, sigma_r)
    rho_smooth = A_n_ext * (w_plus - w_minus)
    r_smooth = r_p + xi

    def GEp(q):
        return j0(q * r_p)

    def GMp(q):
        return mu_p * j0(q * r_p)

    def GEn(q):
        return A_n * (j0(q * r_plus) - j0(q * r_minus))

    def GEn_ext(q):
        return A_n_ext * (j0(q * r_plus_ext) - j0(q * r_minus_ext))

    def GEn_smooth(q):
        return np.trapezoid(rho_smooth * j0(q * r_smooth), xi)

    def GMn(q):
        return mu_n * j0(q * r_p)

    dGEp = derivative_wrt_q2_at_zero(GEp)
    rp2_from_slope = -6.0 * dGEp
    dGEn = derivative_wrt_q2_at_zero(GEn)
    rn2_from_slope = -6.0 * dGEn
    dGEn_ext = derivative_wrt_q2_at_zero(GEn_ext)
    rn2_ext_from_slope = -6.0 * dGEn_ext
    dGEn_smooth = derivative_wrt_q2_at_zero(GEn_smooth)
    rn2_smooth_from_slope = -6.0 * dGEn_smooth
    charge_smooth = np.trapezoid(rho_smooth, xi)

    print("\n[Parâmetros estruturais]")
    print(f"  Lambda_C                         : {Lambda_C:.6f} fm")
    print(f"  R_B                              : {R_B:.6f} fm")
    print(f"  epsilon_eff                      : {epsilon_eff:.12f}")
    print(f"  C_r                              : {C_r:.12f}")
    print(f"  C_r R_B                          : {c_scale:.6f} fm")
    print(f"  r_p                              : {r_p:.9f} fm")
    print(f"  mu_p                             : {mu_p:.9f} mu_N")
    print(f"  mu_n                             : {mu_n:.9f} mu_N")

    print("\n[Normalizações em q^2=0]")
    print(f"  G_E^p(0)                         : {GEp(0.0):.12f}")
    print(f"  G_M^p(0)                         : {GMp(0.0):.12f}")
    print(f"  G_E^n(0)                         : {GEn(0.0):+.12e}")
    print(f"  G_M^n(0)                         : {GMn(0.0):.12f}")

    print("\n[Inclinações de baixa energia]")
    print(f"  r_p^2 estrutural                 : {r_p**2:.12f} fm^2")
    print(f"  -6 dG_E^p/dq^2|0                 : {rp2_from_slope:.12f} fm^2")
    print(f"  erro relativo                    : {(rp2_from_slope / r_p**2 - 1.0):+.3e}")
    print(f"  <r_n^2> modelo polarizado         : {rn2_model:+.12e} fm^2")
    print(f"  <r_n^2> fórmula líder             : {rn2_leading:+.12e} fm^2")
    print(f"  -6 dG_E^n/dq^2|0                 : {rn2_from_slope:+.12e} fm^2")
    print("\n[Fechamento estendido de cola dupla]")
    print(f"  A_n_ext = |mu_n|                  : {A_n_ext:.12f}")
    print(f"  alpha_tor_ext=2 alpha ln(2pi^2)   : {alpha_tor_ext:.12f}")
    print(f"  r_+ ext                           : {r_plus_ext:.9f} fm")
    print(f"  r_- ext                           : {r_minus_ext:.9f} fm")
    print(f"  <r_n^2> ext                       : {rn2_ext:+.12f} fm^2")
    print(f"  -6 dG_E^n_ext/dq^2|0             : {rn2_ext_from_slope:+.12f} fm^2")
    print("\n[Perfil suave de camada de superfície]")
    print(f"  xi_+                              : {xi_plus:+.12f} fm")
    print(f"  xi_-                              : {xi_minus:+.12f} fm")
    print(f"  sigma_r                           : {sigma_r:.12f} fm")
    print(f"  carga integrada                   : {charge_smooth:+.12e}")
    print(f"  G_E^n_suave(0)                    : {GEn_smooth(0.0):+.12e}")
    print(f"  -6 dG_E^n_suave/dq^2|0           : {rn2_smooth_from_slope:+.12f} fm^2")
    print(f"  diferença vs cascas               : {(rn2_smooth_from_slope - rn2_ext):+.3e} fm^2")

    print("\n[Observação]")
    print("  >> O próton está fechado no limite de superfície: normalização e raio.")
    print("  >> O nêutron tem fechamento mínimo e fechamento estendido de cola dupla.")
    print("  >> O perfil suave remove as deltas sem alterar normalização e inclinação.")
    print("  >> H_n(chi) variacional é resolvido em solve_hn_variational_q40.py.")

    q = np.linspace(0.0, 8.0, 600)  # fm^-1
    fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../figs"))
    os.makedirs(fig_dir, exist_ok=True)
    plot_path = os.path.join(fig_dir, "baryon_form_factors_surface_q40.png")

    plt.figure(figsize=(9, 6))
    plt.plot(q, GEp(q), label=r"$G_E^p$")
    plt.plot(q, GMp(q) / mu_p, label=r"$G_M^p/\mu_p$", linestyle="--")
    plt.plot(q, GEn(q), label=r"$G_E^n$ líder")
    plt.plot(q, GEn_ext(q), label=r"$G_E^n$ cola dupla", linestyle="-.")
    plt.plot(q, [GEn_smooth(qq) for qq in q], label=r"$G_E^n$ suave", linestyle="-")
    plt.plot(q, GMn(q) / mu_n, label=r"$G_M^n/\mu_n$", linestyle=":")
    plt.xlabel(r"$q$ (fm$^{-1}$)")
    plt.ylabel("fator de forma normalizado")
    plt.title("Q40 — Fatores de forma de superfície")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()

    output_md_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "saida_form_factors_q40.md")
    )
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(
            f"""# Relatório: Fatores de Forma de Superfície (Q40)

## 1. Regra geométrica

O espalhamento eletromagnético mede a coordenada projetada:

\\[
r_{{\\rm obs}}(\\chi)=C_rR_B\\chi.
\\]

Com:

- \\(C_r={C_r:.12f}\\);
- \\(R_B={R_B:.6f}\\,\\mathrm{{fm}}\\);
- \\(\\epsilon_{{\\rm eff}}={epsilon_eff:.12f}\\);
- \\(r_p={r_p:.9f}\\,\\mathrm{{fm}}\\).

## 2. Normalizações

\\[
G_E^p(0)={GEp(0.0):.12f},
\\qquad
G_M^p(0)={GMp(0.0):.12f}.
\\]

\\[
G_E^n(0)={GEn(0.0):+.12e},
\\qquad
G_M^n(0)={GMn(0.0):.12f}.
\\]

## 3. Inclinação elétrica do próton

\\[
r_p^2={r_p**2:.12f}\\,\\mathrm{{fm}}^2.
\\]

Pela derivada numérica:

\\[
-6\\left.\\frac{{dG_E^p}}{{dq^2}}\\right|_0
={rp2_from_slope:.12f}\\,\\mathrm{{fm}}^2.
\\]

Erro relativo:

\\[
{(rp2_from_slope / r_p**2 - 1.0):+.3e}.
\\]

## 4. Nêutron

Foram avaliados dois níveis.

### 4.1 Fechamento líder mínimo

\\[
G_E^n(q^2)
=
A_n[
j_0(qr_+)-j_0(qr_-)
],
\\qquad
r_->r_+.
\\]

Com:

\\[
A_n=\\alpha\\delta_B={A_n:.12f},
\\quad
r_+={r_plus:.9f}\\,\\mathrm{{fm}},
\\quad
r_-={r_minus:.9f}\\,\\mathrm{{fm}}.
\\]

Isso garante:

\\[
G_E^n(0)=0,
\\qquad
\\langle r_n^2\\rangle={rn2_model:+.12e}\\,\\mathrm{{fm}}^2.
\\]

A forma fechada equivalente é:

\\[
\\langle r_n^2\\rangle_{{\\rm líder}}
=
-2\\alpha^2\\delta_B r_p^2
=
{rn2_leading:+.12e}\\,\\mathrm{{fm}}^2.
\\]

O valor acima não é uma comparação final com dados; ele apenas confirma a
estrutura de polarização com sinal negativo.

### 4.2 Fechamento estendido de cola dupla

A amplitude é a projeção torsional espacial já fixada pelo momento magnético:

\\[
A_n^{{(2)}}=|\\mu_n|={A_n_ext:.12f}.
\\]

O deslocamento relativo vem das duas interfaces antiparalelas:

\\[
\\alpha_{{\\rm tor}}^{{(2)}}
=
2\\alpha\\ln(2\\pi^2)
=
{alpha_tor_ext:.12f}.
\\]

Assim:

\\[
r_+^{{(2)}}={r_plus_ext:.9f}\\,\\mathrm{{fm}},
\\qquad
r_-^{{(2)}}={r_minus_ext:.9f}\\,\\mathrm{{fm}}.
\\]

E:

\\[
\\langle r_n^2\\rangle_{{\\rm ext}}
=
{rn2_ext:+.12f}\\,\\mathrm{{fm}}^2.
\\]

Pela derivada numérica:

\\[
-6\\left.\\frac{{dG_{{E,\\rm ext}}^n}}{{dq^2}}\\right|_0
=
{rn2_ext_from_slope:+.12f}\\,\\mathrm{{fm}}^2.
\\]

Esse valor não foi usado como alvo. Ele sai de \\(|\\mu_n|\\),
\\(2\\alpha\\ln(2\\pi^2)\\) e \\(r_p\\).

### 4.3 Perfil suave de superfície

Para remover as deltas sem transformar a distribuição em densidade de bulk,
usa-se a coordenada local de superfície:

\\[
\\xi=r-r_p.
\\]

A componente positiva fica no lado interno do estômato:

\\[
\\xi_+={xi_plus:+.12f}\\,\\mathrm{{fm}},
\\]

e a componente negativa no lado externo:

\\[
\\xi_-={xi_minus:+.12f}\\,\\mathrm{{fm}}.
\\]

A largura geométrica líder é:

\\[
\\sigma_r
=
\\frac12r_p\\alpha_{{\\rm tor}}^{{(2)}}
=
{sigma_r:.12f}\\,\\mathrm{{fm}}.
\\]

O perfil suave é:

\\[
\\rho_E^n(\\xi)
=
|\\mu_n|[K_\\sigma(\\xi,\\xi_+)-K_\\sigma(\\xi,\\xi_-)].
\\]

Resultado numérico:

\\[
\\int \\rho_E^n d\\xi
=
{charge_smooth:+.12e}.
\\]

\\[
G_{{E,\\rm suave}}^n(0)
=
{GEn_smooth(0.0):+.12e}.
\\]

\\[
-6\\left.\\frac{{dG_{{E,\\rm suave}}^n}}{{dq^2}}\\right|_0
=
{rn2_smooth_from_slope:+.12f}\\,\\mathrm{{fm}}^2.
\\]

A diferença entre a inclinação suave e a inclinação de cascas é:

\\[
{(rn2_smooth_from_slope - rn2_ext):+.3e}\\,\\mathrm{{fm}}^2.
\\]

## 5. Status

\\[
\\boxed{{
\\text{{fatores de forma fechados estruturalmente em normalização e baixa energia.}}
}}
\\]

O perfil \\(H_n(\\chi)\\) variacional é resolvido em
`solve_hn_variational_q40.py`. Este relatório mantém a checagem estrutural por
cascas e perfil suave, enquanto o relatório variacional fornece a curva
\\(G_E^n(q^2)\\) completa líder.
"""
        )


if __name__ == "__main__":
    run()
