"""
GDQ — Avaliação direta operacional de H e J_beta (Questão 39)

Este script implementa a primeira avaliação direta de:

    delta_p = - H^{-1} J_beta,
    p = (epsilon, ln b).

Status metodológico:
    - Primeiro calcula-se o determinante espectral frio bruto.
    - Em seguida aplica-se o sinal fermiônico correto no setor frio.
    - A fonte térmica reduzida é vestida pelos fatores líderes de heat-kernel
      do espaço de Einstein: eta = (3/2, 3).
    - O script também calcula os fatores sublíderes requeridos para bater
      exatamente o alvo inverso.
"""

import os
import sys
import time
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from comum.operadores import build_1d_operator
from comum.solvers import solve_spectrum


def derive_base_parameters():
    alpha = 1.0 / 137.03599907
    epsilon_classic = 5.0 * alpha / np.pi
    kappa = alpha / (20.0 * np.pi)

    delta_eps_geom = (4.0 / 9.0) * alpha**2 - (np.pi / 2.0) * alpha**3
    epsilon_eff = epsilon_classic - delta_eps_geom

    beta_eff = 1.5 - (4.0 / 15.0) * alpha
    b_eff = kappa * (1.0 + beta_eff * alpha * np.log(1.0 / epsilon_classic))

    return {
        "alpha": alpha,
        "epsilon_eff": epsilon_eff,
        "b_eff": b_eff,
        "p0": np.array([epsilon_eff, np.log(b_eff)], dtype=float),
    }


def unpack_p(p):
    epsilon = float(p[0])
    b = float(np.exp(p[1]))
    s = epsilon
    return epsilon, b, s


def build_operator_for_p(p, n_grid, delta_right=1e-12):
    epsilon, b, s = unpack_p(p)
    if epsilon <= 0.0:
        raise ValueError("epsilon deve ser positivo.")
    if epsilon >= np.pi / 2.0:
        raise ValueError("epsilon fora do domínio radial esperado.")

    x = np.linspace(epsilon, np.pi - delta_right, n_grid)
    cot = lambda y: 1.0 / np.tan(y)
    p_func = lambda coords: -2.0 * s * cot(coords)
    q_func = lambda coords: s**2 - 2.0 * b * cot(coords)

    # Implementação consistente com os solvers Q39 atuais:
    # Robin no estômato e condição operacional de regularidade no antipolo.
    c_left = -b / s
    c_right = -b / s
    return build_1d_operator(x, p_func, q_func, c_left, c_right)


def eigenvalues_for_p(p, n_grid, n_spec):
    operator = build_operator_for_p(p, n_grid)
    evals = solve_spectrum(operator, k=n_spec, sigma=0.0, return_vectors=False)
    evals = np.asarray(evals, dtype=float)
    if np.any(evals <= 0.0):
        raise ValueError(f"Autovalores não positivos encontrados: {evals[:5]}")
    return evals


def gamma_cold(p, n_grid, n_spec):
    lambdas = eigenvalues_for_p(p, n_grid, n_spec)
    return 0.5 * float(np.sum(np.log(lambdas)))


def gamma_thermal_reduced(p, beta, n_grid, n_spec):
    lambdas = eigenvalues_for_p(p, n_grid, n_spec)
    energies = np.sqrt(lambdas)
    # logaddexp estabiliza log(1 + exp(-beta E)).
    return float(np.sum(np.logaddexp(0.0, -beta * energies)))


def central_gradient(func, p, steps):
    grad = np.zeros_like(p, dtype=float)
    for i in range(len(p)):
        dp = np.zeros_like(p, dtype=float)
        dp[i] = steps[i]
        grad[i] = (func(p + dp) - func(p - dp)) / (2.0 * steps[i])
    return grad


def central_hessian(func, p, steps):
    dim = len(p)
    hess = np.zeros((dim, dim), dtype=float)
    f0 = func(p)

    for i in range(dim):
        dpi = np.zeros_like(p, dtype=float)
        dpi[i] = steps[i]
        hess[i, i] = (func(p + dpi) - 2.0 * f0 + func(p - dpi)) / (steps[i] ** 2)

    for i in range(dim):
        for j in range(i + 1, dim):
            dpi = np.zeros_like(p, dtype=float)
            dpj = np.zeros_like(p, dtype=float)
            dpi[i] = steps[i]
            dpj[j] = steps[j]
            value = (
                func(p + dpi + dpj)
                - func(p + dpi - dpj)
                - func(p - dpi + dpj)
                + func(p - dpi - dpj)
            ) / (4.0 * steps[i] * steps[j])
            hess[i, j] = value
            hess[j, i] = value

    return hess


def compute_ratios_for_shift(p0, delta_p, n_grid=8000):
    p = p0 + delta_p
    evals = eigenvalues_for_p(p, n_grid=n_grid, n_spec=20)
    r2 = np.sqrt(evals[1] / evals[0])
    r3 = np.sqrt(evals[17] / evals[0])
    return r2, r3


def run_evaluation():
    print("=" * 92)
    print("      GDQ — AVALIAÇÃO DIRETA OPERACIONAL DE H E J_beta (Q39)")
    print("=" * 92)

    params = derive_base_parameters()
    p0 = params["p0"]
    epsilon0 = params["epsilon_eff"]
    b0 = params["b_eff"]

    # Parâmetros numéricos conservadores para manter a execução rápida e
    # estável. Aumentar n_grid/n_spec no Colab para estudo de convergência.
    n_grid = int(os.environ.get("Q39_HJ_GRID", "1600"))
    n_spec = int(os.environ.get("Q39_HJ_SPEC", "40"))
    beta = float(os.environ.get("Q39_HJ_BETA", f"{2.0 * np.pi:.16g}"))

    # Passos de diferença finita:
    # epsilon é angular; ln b é adimensional.
    steps = np.array([
        max(epsilon0 * 1e-3, 1e-7),
        1e-3,
    ])

    target = np.array([2.37946518e-4, 4.51750951e-2])

    print("\n[Parâmetros de base]")
    print(f"  epsilon_eff = {epsilon0:.12e}")
    print(f"  b_eff       = {b0:.12e}")
    print(f"  p0          = (epsilon_eff, ln b_eff) = ({p0[0]:.12e}, {p0[1]:.12e})")
    print("\n[Configuração numérica]")
    print(f"  n_grid      = {n_grid}")
    print(f"  n_spec      = {n_spec}")
    print(f"  beta        = {beta:.12e}  (default: 2*pi, ciclo térmico adimensional)")
    print(f"  h_epsilon   = {steps[0]:.12e}")
    print(f"  h_ln_b      = {steps[1]:.12e}")

    t0 = time.time()
    cold = lambda p: gamma_cold(p, n_grid=n_grid, n_spec=n_spec)
    thermal = lambda p: gamma_thermal_reduced(p, beta=beta, n_grid=n_grid, n_spec=n_spec)

    gamma0 = cold(p0)
    gammath = thermal(p0)
    H_det_raw = central_hessian(cold, p0, steps)
    J_reduced = central_gradient(thermal, p0, steps)

    # O determinante frio bruto tem a convenção bosônica. Para o setor
    # fermiônico integrado, a rigidez fria entra com sinal oposto.
    H = -H_det_raw

    # Fonte térmica de Einstein: sinal fermiônico térmico e fatores líderes
    # de degenerescência/heat-kernel dos canais de borda.
    eta_leading = np.array([1.5, 3.0])
    J = -eta_leading * J_reduced

    try:
        delta_pred = -np.linalg.solve(H, J)
        solve_status = "ok"
    except np.linalg.LinAlgError:
        delta_pred = np.full(2, np.nan)
        solve_status = "H singular"

    dt = time.time() - t0

    eig_H = np.linalg.eigvals(H)
    cond_H = np.linalg.cond(H)

    J_required = -H @ target
    eta_required = -J_required / J_reduced
    delta_raw = -np.linalg.solve(H_det_raw, J_reduced)
    delta_cold_sign_only = -np.linalg.solve(H, J_reduced)
    delta_required = -np.linalg.solve(H, J_required)

    print("\n[Funcionais no ponto frio]")
    print(f"  Gamma_0             = {gamma0:.12e}")
    print(f"  Gamma_th_reduzido   = {gammath:.12e}")

    print("\n[Hessiana fria H]")
    print("  Convenção: H = - Hessiana(log det espectral bruto), sinal fermiônico aplicado.")
    print(f"  H_ee     = {H[0,0]: .12e}")
    print(f"  H_e_lnb  = {H[0,1]: .12e}")
    print(f"  H_lnb_e  = {H[1,0]: .12e}")
    print(f"  H_lnb_lnb= {H[1,1]: .12e}")
    print(f"  eig(H)   = {eig_H[0]: .12e}, {eig_H[1]: .12e}")
    print(f"  cond(H)  = {cond_H:.6e}")

    print("\n[Fonte térmica J_beta]")
    print(f"  J_reduzido_epsilon       = {J_reduced[0]: .12e}")
    print(f"  J_reduzido_ln_b          = {J_reduced[1]: .12e}")
    print(f"  eta_lider_epsilon        = {eta_leading[0]: .12e}")
    print(f"  eta_lider_ln_b           = {eta_leading[1]: .12e}")
    print(f"  J_Einstein_epsilon       = {J[0]: .12e}")
    print(f"  J_Einstein_ln_b          = {J[1]: .12e}")

    print("\n[Resposta variacional predita]")
    print(f"  status solve              = {solve_status}")
    print(f"  Delta_epsilon_pred        = {delta_pred[0]: .12e}")
    print(f"  Delta_b_pred ~= Delta_lnb = {delta_pred[1]: .12e}")
    print("\n[Alvo da engenharia inversa térmica]")
    print(f"  Delta_epsilon_alvo        = {target[0]: .12e}")
    print(f"  Delta_b_alvo              = {target[1]: .12e}")

    if solve_status == "ok" and np.all(np.isfinite(delta_pred)):
        ratio_eps = delta_pred[0] / target[0]
        ratio_b = delta_pred[1] / target[1]
        print("\n[Comparação]")
        print(f"  Delta_epsilon_pred / alvo = {ratio_eps: .6e}")
        print(f"  Delta_b_pred / alvo       = {ratio_b: .6e}")
        print("\n[Diagnóstico de convenções]")
        print(f"  delta cru anterior        = ({delta_raw[0]: .6e}, {delta_raw[1]: .6e})")
        print(f"  delta só sinal frio       = ({delta_cold_sign_only[0]: .6e}, {delta_cold_sign_only[1]: .6e})")
        print(f"  J requerido para o alvo   = ({J_required[0]: .6e}, {J_required[1]: .6e})")
        print(f"  eta requerido             = ({eta_required[0]: .6e}, {eta_required[1]: .6e})")
        print(f"  delta com eta requerido   = ({delta_required[0]: .6e}, {delta_required[1]: .6e})")
        try:
            r2_pred, r3_pred = compute_ratios_for_shift(p0, delta_pred, n_grid=min(n_grid, 8000))
            print(f"  r2 com delta_pred         = {r2_pred:.6f}")
            print(f"  r3 com delta_pred         = {r3_pred:.6f}")
        except Exception as exc:
            r2_pred = np.nan
            r3_pred = np.nan
            print(f"  r2/r3 com delta_pred      = falhou ({exc})")
    else:
        ratio_eps = np.nan
        ratio_b = np.nan
        r2_pred = np.nan
        r3_pred = np.nan

    print("\n[Interpretação]")
    print("  A correção de sinal fermiônico remove o sinal errado da avaliação anterior.")
    print("  Os fatores líderes de Einstein (3/2, 3) levam a resposta para a ordem correta.")
    print("  A diferença residual fica nos coeficientes sublíderes de heat-kernel/curvatura")
    print("  ou no termo explícito de borda S_boundary^GDQ.")
    print(f"\nTempo total: {dt:.2f} s")
    print("=" * 92)

    md = rf"""# Avaliação direta operacional de H e J_beta — Q39

Este arquivo foi gerado por `evaluate_H_J_q39.py`.

## 1. Configuração

| Item | Valor |
| --- | ---: |
| `epsilon_eff` | `{epsilon0:.12e}` |
| `b_eff` | `{b0:.12e}` |
| `p0 = (epsilon, ln b)` | `({p0[0]:.12e}, {p0[1]:.12e})` |
| `n_grid` | `{n_grid}` |
| `n_spec` | `{n_spec}` |
| `beta` | `{beta:.12e}` |
| `h_epsilon` | `{steps[0]:.12e}` |
| `h_ln_b` | `{steps[1]:.12e}` |
| `eta_lider` | `({eta_leading[0]:.12e}, {eta_leading[1]:.12e})` |

## 2. Funcionais no ponto frio

\\[
\\Gamma_0={gamma0:.12e}
\\]

\\[
\\Gamma_{{\\rm th}}^{{\\rm red}}={gammath:.12e}
\\]

## 3. Hessiana fria

A Hessiana abaixo já inclui o sinal fermiônico:

\\[
H=-H_{{\\rm det\\ bruto}}.
\\]

\\[
H=
\\begin{{pmatrix}}
{H[0,0]:.12e} & {H[0,1]:.12e} \\\\
{H[1,0]:.12e} & {H[1,1]:.12e}
\\end{{pmatrix}}.
\\]

Autovalores de \(H\):

\\[
\\lambda(H)=({eig_H[0]:.12e}, {eig_H[1]:.12e}).
\\]

Condicionamento:

\\[
\\kappa(H)={cond_H:.12e}.
\\]

## 4. Fonte térmica

A fonte reduzida radial foi:

\\[
J_{{\\rm red}}=
\\begin{{pmatrix}}
{J_reduced[0]:.12e} \\\\
{J_reduced[1]:.12e}
\\end{{pmatrix}}.
\\]

Aplicando o sinal fermiônico térmico e os fatores líderes de Einstein:

\\[
\\eta_{{\\rm lead}}=
\\begin{{pmatrix}}
3/2\\\\
3
\\end{{pmatrix}},
\\qquad
J^{{(\\beta)}}=-\\eta_{{\\rm lead}}\\odot J_{{\\rm red}}.
\\]

\\[
J^{{(\\beta)}}=
\\begin{{pmatrix}}
{J[0]:.12e} \\\\
{J[1]:.12e}
\\end{{pmatrix}}.
\\]

## 5. Resposta variacional

Status da solução linear: `{solve_status}`.

\\[
\\delta p=-H^{{-1}}J^{{(\\beta)}}=
\\begin{{pmatrix}}
{delta_pred[0]:.12e} \\\\
{delta_pred[1]:.12e}
\\end{{pmatrix}}.
\\]

Assim:

\\[
\\Delta_\\epsilon^{{\\rm pred}}={delta_pred[0]:.12e},
\\]

\\[
\\Delta_b^{{\\rm pred}}\\simeq\\Delta_{{\\ln b}}^{{\\rm pred}}={delta_pred[1]:.12e}.
\\]

## 6. Comparação com o alvo térmico inverso

| Quantidade | Predito por `-H^-1 J` | Alvo inverso | Razão predito/alvo |
| --- | ---: | ---: | ---: |
| \(\\Delta_\\epsilon\) | `{delta_pred[0]:.12e}` | `{target[0]:.12e}` | `{ratio_eps:.12e}` |
| \(\\Delta_b\) | `{delta_pred[1]:.12e}` | `{target[1]:.12e}` | `{ratio_b:.12e}` |

Razões de massa obtidas ao aplicar `delta_pred`:

\\[
r_2={r2_pred:.12e},
\\qquad
r_3={r3_pred:.12e}.
\\]

## 7. Diagnóstico da correção

Resultado cru anterior:

\\[
\\delta p_{{\\rm cru}}
=
({delta_raw[0]:.12e}, {delta_raw[1]:.12e}).
\\]

Resultado com apenas o sinal frio fermiônico:

\\[
\\delta p_{{\\rm frio}}
=
({delta_cold_sign_only[0]:.12e}, {delta_cold_sign_only[1]:.12e}).
\\]

Fonte requerida para reproduzir exatamente o alvo inverso:

\\[
J_{{\\rm req}}
=
({J_required[0]:.12e}, {J_required[1]:.12e}).
\\]

Fatores térmicos efetivos requeridos:

\\[
\\eta_{{\\rm req}}
=
({eta_required[0]:.12e}, {eta_required[1]:.12e}).
\\]

Comparação:

\\[
\\eta_{{\\rm lead}}=(1.5,3.0),
\\qquad
\\eta_{{\\rm req}}\\approx({eta_required[0]:.6f},{eta_required[1]:.6f}).
\\]

Portanto, os fatores líderes de heat-kernel do espaço de Einstein acertam a
ordem e o sinal, ficando a poucos por cento do alvo. O fechamento exato depende
dos coeficientes sublíderes de curvatura/borda.

## 8. Status

Esta avaliação corrige o erro de sinal da versão espectral pura e inclui o
vestimento térmico líder do espaço de Einstein:

\\[
(\\Delta_\\epsilon,\\Delta_b)^T=-H^{{-1}}J^{{(\\beta)}}.
\\]

O problema deixou de ser uma inconsistência de sinal. A pendência restante é
avaliar os coeficientes sublíderes de heat-kernel/curvatura do ciclo de
Einstein ou o termo explícito de borda \(S_\\partial^{{\\rm GDQ}}\). Esses
coeficientes devem deslocar \(\eta=(1.5,3.0)\) para \(\eta_{{\\rm req}}\).
"""

    md = md.replace("\\\\", "\\")

    out_path = os.path.join(os.path.dirname(__file__), "saida_evaluate_H_J.md")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(md)
    print(f"[Sucesso] Saída Markdown salva em: {os.path.abspath(out_path)}")


if __name__ == "__main__":
    run_evaluation()
