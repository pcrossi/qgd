#!/usr/bin/env python3
"""
Capítulo 4 — verificação da separação de escalas da GDQ.

Classificação:
    teste numérico/simbólico de consistência.

Este script não faz previsão metrológica. Ele verifica a tese conceitual da
nota "Escala de Cartan, resolução de fluxo e escalas setoriais":

1. Lambda_C na ação normalizada é adimensional.
2. A escala do kernel de calor é Lambda_hat_tau = tau^{-1/2}.
3. Massas deslocam o espectro p^2 + m_i^2, mas não são cortes universais.
4. Usar m_e ou 1 GeV como corte gaussiano duro universal destruiria processos
   em GeV/TeV, logo essa leitura é proibida.

Os números de massa/energia abaixo são usados apenas como escalas de referência
para demonstrar a ordem de grandeza da inconsistência.
"""

from __future__ import annotations

import math
from pathlib import Path


def log10_gaussian_suppression(energy_gev: float, cutoff_gev: float) -> float:
    """Retorna log10(exp[-(E/Lambda)^2]) sem underflow."""
    return -((energy_gev / cutoff_gev) ** 2) / math.log(10.0)


def main() -> None:
    # Escalas de referência em GeV.
    electron_mass_gev = 0.00051099895
    one_gev = 1.0

    # Energias externas ilustrativas, não usadas como ajuste.
    energies_gev = [electron_mass_gev, 0.01, 1.0, 100.0, 13000.0]

    # Escalas de fluxo ilustrativas.
    tau_values = [1.0, 0.25, 0.01, 1.0e-4]

    # Exemplo de massa deslocando espectro, não definindo corte.
    p_gev = 10.0
    sector_masses = {
        "eletron": electron_mass_gev,
        "hadronico_1GeV": 1.0,
        "eletrofraco_100GeV": 100.0,
    }

    lines = [
        '---',
        'title: "Saída — separação de escalas"',
        '---',
        '',
        '# Saída — separação de escalas',
        '',
        '## 1. Escala do kernel de calor',
        '',
        '| $\\tau$ | $\\widehat\\Lambda_\\tau=\\tau^{-1/2}$ |',
        '|---:|---:|',
    ]

    for tau in tau_values:
        lam = tau ** -0.5
        lines.append(f'| `{tau:.6e}` | `{lam:.12e}` |')

    lines += [
        '',
        '## 2. Por que $m_e$ não pode ser corte universal duro',
        '',
        'A tabela mostra $\\log_{10}\\{\\exp[-(E/\\Lambda)^2]\\}$.',
        '',
        '| energia externa $E$ [GeV] | corte $m_e$ | corte $1$ GeV |',
        '|---:|---:|---:|',
    ]

    for energy in energies_gev:
        log_me = log10_gaussian_suppression(energy, electron_mass_gev)
        log_one = log10_gaussian_suppression(energy, one_gev)
        lines.append(f'| `{energy:.9e}` | `{log_me:.6e}` | `{log_one:.6e}` |')

    lines += [
        '',
        'Valores muito negativos significam supressão efetivamente nula.',
        'Assim, $m_e$ ou $1$ GeV não podem ser lidos como parede universal de energia externa.',
        '',
        '## 3. Massa como deslocamento espectral',
        '',
        f'Para $p_E={p_gev}$ GeV, com $\\lambda_i=p_E^2+m_i^2$:',
        '',
        '| setor | $m_i$ [GeV] | $p_E^2$ | $m_i^2$ | $\\lambda_i$ | fração $m_i^2/\\lambda_i$ |',
        '|---|---:|---:|---:|---:|---:|',
    ]

    p2 = p_gev * p_gev
    for name, mass in sector_masses.items():
        m2 = mass * mass
        lam = p2 + m2
        frac = m2 / lam
        lines.append(f'| `{name}` | `{mass:.9e}` | `{p2:.9e}` | `{m2:.9e}` | `{lam:.9e}` | `{frac:.9e}` |')

    lines += [
        '',
        '## Conclusão',
        '',
        '$\\Lambda_C$, $\\widehat\\Lambda_\\tau$ e $m_i$ têm funções distintas.',
        'A massa altera o espectro do setor; a resolução vem de $\\tau$; a ação usa $\\Lambda_C$ como número adimensional normalizado.',
        '',
    ]

    out = Path(__file__).with_name('saida_verificar_separacao_escalas.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
