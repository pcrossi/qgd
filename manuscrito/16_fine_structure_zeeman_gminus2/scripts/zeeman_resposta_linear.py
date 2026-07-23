#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `zeeman resposta linear` associada ao capítulo `16_fine_structure_zeeman_gminus2`.

GDQ — Capítulo 16 / resposta Zeeman linear.

Verifica a forma reduzida:

    E_pm = E0 ∓ gamma_eff (hbar/2) |B|
    F_pm = ± gamma_eff (hbar/2) grad |B|

O script usa unidades reduzidas hbar=1 e gamma_eff=1 para demonstrar a
estrutura de sinais. B e gradB são dados de aparelho.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_zeeman_resposta_linear.md"

    hbar = 1.0
    gamma_eff = 1.0
    e0 = 0.0
    b_abs = 0.25
    grad_b = 0.03

    e_plus = e0 - gamma_eff * 0.5 * hbar * b_abs
    e_minus = e0 + gamma_eff * 0.5 * hbar * b_abs
    f_plus = gamma_eff * 0.5 * hbar * grad_b
    f_minus = -gamma_eff * 0.5 * hbar * grad_b

    text = f"""# Saída — resposta Zeeman linear

Classificação: teste simbólico-numérico reduzido.

Unidades reduzidas: $\\hbar=1$, $\\gamma_{{\\rm eff}}=1$.

| quantidade | valor |
|---|---:|
| modulo de B | {b_abs:.12f} |
| gradiente do modulo de B | {grad_b:.12f} |
| E_+ | {e_plus:.12f} |
| E_- | {e_minus:.12f} |
| E_+-E_- | {e_plus-e_minus:.12f} |
| F_+ | {f_plus:.12f} |
| F_- | {f_minus:.12f} |

Interpretação: os dois canais têm energias e forças opostas porque o aparelho
seleciona as duas orientações estáveis da circulação.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
