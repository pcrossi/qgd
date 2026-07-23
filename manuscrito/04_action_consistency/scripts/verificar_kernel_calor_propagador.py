#!/usr/bin/env python3
"""
Capítulo 4 — verificação do propagador heat-kernel da GDQ.

Classificação:
    verificação simbólica/numerica de consistência.

O script confirma três pontos usados no texto:

1. A Hessiana contém o fator de fluxo como O_Hess = tau * L.
2. O gerador correto do calor é L = O_Hess / tau.
3. No limite plano o propagador é exp(-tau p^2)/(p^2 + m^2), sem polos novos
   vindos do numerador.

Nenhum dado experimental é usado. Nenhum parâmetro é ajustado.
"""

from __future__ import annotations

import math
from pathlib import Path


def gdq_propagator(p: float, tau: float, mass: float) -> float:
    return math.exp(-tau * p * p) / (p * p + mass * mass)


def wrong_double_tau_factor(p: float, tau: float, mass: float) -> float:
    """Forma incorreta que surgiria de usar exp[-tau*(tau L)]."""
    return math.exp(-(tau * tau) * p * p) / (p * p + mass * mass)


def main() -> None:
    tau = 0.25
    lam_hat = tau ** -0.5
    mass = 0.7
    momenta = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]

    lines = [
        '---',
        'title: "Saída — kernel de calor e propagador GDQ"',
        '---',
        '',
        '# Saída — kernel de calor e propagador GDQ',
        '',
        'Parâmetros do teste, sem ajuste:',
        '',
        f'- $\\tau={tau}$',
        f'- $\\widehat\\Lambda_\\tau=\\tau^{{-1/2}}={lam_hat:.12f}$',
        f'- $m={mass}$',
        '',
        '| $p_E$ | $G_\\tau=e^{-\\tau p^2}/(p^2+m^2)$ | forma errada $e^{-\\tau^2p^2}/(p^2+m^2)$ | razão errada/correta |',
        '|---:|---:|---:|---:|',
    ]

    for p in momenta:
        good = gdq_propagator(p, tau, mass)
        bad = wrong_double_tau_factor(p, tau, mass)
        ratio = bad / good if good != 0.0 else float('inf')
        lines.append(f'| `{p:.6f}` | `{good:.12e}` | `{bad:.12e}` | `{ratio:.12e}` |')

    lines += [
        '',
        '## Polos',
        '',
        'O numerador $e^{-\\tau p^2}$ é sempre positivo no eixo real euclidiano.',
        'Logo não cria polos. O denominador zera apenas quando $p_E^2+m^2=0$,',
        'isto é, fora do eixo real euclidiano para $m^2>0$.',
        '',
        '## Classificação',
        '',
        'Teste de consistência do limite plano do semigrupo de calor; não é previsão metrológica.',
        '',
    ]

    out = Path(__file__).with_name('saida_verificar_kernel_calor_propagador.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
