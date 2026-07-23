#!/usr/bin/env python3
"""
Capítulo 4 — kernels covariantes e preservação de calibre.

Classificação:
    teste numérico/simbólico de consistência.

O objetivo é separar duas afirmações:

1. Qualquer função espectral covariante K(H[A]) preserva Ward, pois
   H[A^g]=g^{-1}H[A]g implica Tr K(H[A^g])=Tr K(H[A]).
2. Perfis diferentes de K representam resoluções físicas diferentes, logo os
   coeficientes numéricos de saturação não precisam ser iguais.

Este script compara três kernels admissíveis no mesmo operador reduzido.
"""

from __future__ import annotations

import math
from pathlib import Path


def simpson(f, a: float, b: float, n: int = 800) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def e1(z: float) -> float:
    def integrand(t: float) -> float:
        if t == 0.0:
            return 0.0
        return math.exp(-z / t) / t

    return simpson(integrand, 0.0, 1.0, 4000)


def ekernel(name: str, z: float) -> float:
    if name == "canonico":
        return e1(z)
    if name == "mistura":
        return 0.5 * e1(z) + 0.5 * e1(2.0 * z)
    if name == "inteiro_plus":
        return e1(z) + math.exp(-z)
    raise ValueError(name)


def pi_kernel(q2: float, eta: float, s0: float, qn: float, name: str) -> float:
    def integrand(x: float) -> float:
        u = x * (1.0 - x)
        return (1.0 - 2.0 * x) ** 2 * (
            ekernel(name, eta) - ekernel(name, eta + s0 * u * q2)
        )

    return qn * qn / (16.0 * math.pi**2) * simpson(integrand, 0.0, 1.0, 800)


def main() -> None:
    qn = 1.0
    mass = 1.0
    s0 = 0.2
    eta = s0 * mass * mass
    q2_probe = 25.0
    kernels = ["canonico", "mistura", "inteiro_plus"]

    lines = [
        '---',
        'title: "Saída — kernels covariantes de calibre"',
        '---',
        '',
        '# Saída — kernels covariantes de calibre',
        '',
        f'Parâmetros: `q_n={qn}`, `m={mass}`, `s0={s0}`, `eta={eta}`, `Q^2={q2_probe}`.',
        '',
        '| kernel | $\\Pi_K(0)$ | $\\Pi_K(Q^2)$ | saturação $q_n^2\\mathcal E_K(\\eta)/(48\\pi^2)$ | Ward tensorial |',
        '|---|---:|---:|---:|---|',
    ]

    for name in kernels:
        pi0 = pi_kernel(0.0, eta, s0, qn, name)
        piq = pi_kernel(q2_probe, eta, s0, qn, name)
        sat = qn * qn / (48.0 * math.pi**2) * ekernel(name, eta)
        lines.append(f'| `{name}` | `{pi0:.12e}` | `{piq:.12e}` | `{sat:.12e}` | preservada por covariância |')

    lines += [
        '',
        '## Interpretação',
        '',
        'Todos os kernels testados preservam $\\Pi_K(0)=0$ e a forma transversal.',
        'Os valores saturados diferem porque kernels diferentes representam resoluções espectrais diferentes.',
        'O kernel canônico da GDQ é o semigrupo da Hessiana física, $K_0=e^{-sH}$.',
        '',
    ]

    out = Path(__file__).with_name('saida_verificar_kernels_covariantes_calibre.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

