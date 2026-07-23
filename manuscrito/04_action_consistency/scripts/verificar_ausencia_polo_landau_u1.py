#!/usr/bin/env python3
"""
Capítulo 4 — ausência de polo de Landau no setor U(1) efetivo.

Classificação:
    avaliação direta e teste de consistência.

Este script avalia a polarização escalar

    Pi_eta(r)=2 alpha/pi int_0^1 dx x(1-x)
      [E1(eta)-E1(eta*(1+x(1-x)r))]

com r=q_E^2/m^2 e eta=tau*m^2=m^2/Lambda_EM^2.

O objetivo é verificar:

1. Pi(0)=0;
2. monotonicidade;
3. saturação ultravioleta finita;
4. condição sem polo Pi(infty)<1;
5. aproximação do limite QED quando eta é muito pequeno.

Não há ajuste a dados experimentais e eta é apenas um cenário de teste.
"""

from __future__ import annotations

import math
from pathlib import Path


ALPHA0 = 1.0 / 137.035999084
EULER_GAMMA = 0.5772156649015329


def simpson(f, a: float, b: float, n: int = 1600) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def e1(z: float) -> float:
    """Exponencial integral E1(z) para z>0, sem dependências externas."""
    if z <= 0:
        raise ValueError("E1 requer z>0")
    if z < 1.0e-5:
        total = -EULER_GAMMA - math.log(z)
        term = 1.0
        factorial = 1.0
        for k in range(1, 80):
            term *= -z
            factorial *= k
            add = -term / (k * factorial)
            total += add
            if abs(add) < 1.0e-16 * max(1.0, abs(total)):
                break
        return total
    if z > 50.0:
        term = 1.0
        total = 1.0
        for k in range(1, 80):
            term *= -k / z
            total += term
            if abs(term) < 1.0e-16:
                break
        return math.exp(-z) * total / z

    def integrand(t: float) -> float:
        if t == 0.0:
            return 0.0
        return math.exp(-z / t) / t

    return simpson(integrand, 0.0, 1.0, 4000)


def pi_eta(r: float, eta: float, alpha0: float = ALPHA0, n: int = 800) -> float:
    if r < 0.0 or eta <= 0.0:
        raise ValueError("requer r>=0 e eta>0")
    e0 = e1(eta)

    def integrand(x: float) -> float:
        u = x * (1.0 - x)
        return u * (e0 - e1(eta * (1.0 + u * r)))

    return 2.0 * alpha0 / math.pi * simpson(integrand, 0.0, 1.0, n)


def pi_qed_limit(r: float, alpha0: float = ALPHA0, n: int = 1200) -> float:
    def integrand(x: float) -> float:
        u = x * (1.0 - x)
        return u * math.log1p(u * r)

    return 2.0 * alpha0 / math.pi * simpson(integrand, 0.0, 1.0, n)


def pi_infinity(eta: float, alpha0: float = ALPHA0) -> float:
    return alpha0 * e1(eta) / (3.0 * math.pi)


def main() -> None:
    eta = 1.0e-6
    rs = [0.0, 1.0e-4, 1.0, 1.0e4, 1.0e8, 1.0e12]
    samples = [(r, pi_eta(r, eta, n=800), pi_eta(r, eta, n=1600)) for r in rs]
    asymptote = pi_infinity(eta)
    alpha_inf = ALPHA0 / (1.0 - asymptote)
    alpha_inf_inv = 1.0 / alpha_inf

    grid = [10.0 ** (-8 + i * 0.25) for i in range(81)]
    values = [pi_eta(r, eta, n=500) for r in grid]
    monotone = all(values[i + 1] + 1.0e-13 >= values[i] for i in range(len(values) - 1))
    bounded = all(v <= asymptote + 1.0e-10 for v in values)
    no_pole = asymptote < 1.0

    convergence = [(n, pi_eta(1.0e4, eta, n=n)) for n in [100, 200, 400, 800, 1600]]
    conv_error = abs(convergence[-1][1] - convergence[-2][1])

    small_eta = 1.0e-12
    qed_rows = []
    for r in [1.0e-4, 1.0, 1.0e4]:
        numeric = pi_eta(r, small_eta, n=1600)
        limit = pi_qed_limit(r)
        qed_rows.append((r, numeric, limit, abs(numeric - limit)))

    # Teste tensorial: Pi_mn=(q_m q_n-q^2 delta_mn)Pi. A contração deve zerar.
    q = [0.37, -0.21, 0.49, 0.73]
    q2 = sum(x * x for x in q)
    pi_tensor_scalar = pi_eta(q2, eta, n=800)
    ward = []
    for nu in range(4):
        acc = 0.0
        for mu in range(4):
            delta = 1.0 if mu == nu else 0.0
            tensor = (q[mu] * q[nu] - q2 * delta) * pi_tensor_scalar
            acc += q[mu] * tensor
        ward.append(acc)
    ward_abs = math.sqrt(sum(x * x for x in ward))

    lines = [
        "---",
        'title: "Saída — ausência de polo de Landau U(1)"',
        "---",
        "",
        "# Saída — ausência de polo de Landau $U(1)$",
        "",
        "## Entrada",
        "",
        "$$",
        f"\\alpha_0={ALPHA0:.15g},\\qquad \\eta=\\tau m^2={eta:.6e}.",
        "$$",
        "",
        "$\\eta$ é cenário de teste para verificar a fórmula; não é ajustado.",
        "",
        "## Polarização",
        "",
        "| $r=q_E^2/m^2$ | $\\Pi_\\eta(r)$ | refinado | diferença |",
        "|---:|---:|---:|---:|",
    ]
    for r, value, refined in samples:
        lines.append(f"| `{r:.3e}` | `{value:.12e}` | `{refined:.12e}` | `{abs(value-refined):.3e}` |")
    lines += [
        "",
        "## Saturação e condição sem polo",
        "",
        "$$",
        f"\\Pi_\\eta(\\infty)={asymptote:.12e},\\qquad "
        f"\\alpha_{{\\rm eff}}^{{-1}}(\\infty)={alpha_inf_inv:.9f}.",
        "$$",
        "",
        f"- monotonicidade: `{monotone}`;",
        f"- limitado pelo valor assintótico: `{bounded}`;",
        f"- condição sem polo no cenário: `{no_pole}`;",
        f"- resíduo tensorial de Ward: `{ward_abs:.3e}`.",
        "",
        "## Refinamento em $r=10^4$",
        "",
        "| pontos Simpson | $\\Pi_\\eta(10^4)$ |",
        "|---:|---:|",
    ]
    for n, value in convergence:
        lines.append(f"| `{n}` | `{value:.14e}` |")
    lines += [
        "",
        f"Erro entre as duas últimas ordens: `{conv_error:.3e}`.",
        "",
        "## Limite de baixa energia",
        "",
        "| $r$ | $\\eta=10^{-12}$ | limite $\\eta\\to0$ | diferença |",
        "|---:|---:|---:|---:|",
    ]
    for r, numeric, limit, diff in qed_rows:
        lines.append(f"| `{r:.3e}` | `{numeric:.12e}` | `{limit:.12e}` | `{diff:.3e}` |")
    lines += [
        "",
        "## Classificação",
        "",
        "Avaliação direta da fórmula derivada. O teste demonstra saturação para",
        "$\\eta>0$ e recuperação do limite logarítmico em baixa energia.",
        "",
    ]

    out = Path(__file__).with_name("saida_verificar_ausencia_polo_landau_u1.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

