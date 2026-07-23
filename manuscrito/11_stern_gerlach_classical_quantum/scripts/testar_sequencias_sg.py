#!/usr/bin/env python3
"""
GDQ — Capítulo 11 / Medições sequenciais

Objetivo:
    Testar p(s'|s;b,a)=(1+s*s'*a·b)/2 para eixos z e x.

Fonte teórica:
    manuscrito/11_stern_gerlach_classical_quantum/11.7 - Medições sequenciais e incompatibilidade de eixos.md

Classificação:
    Teste simbólico de consistência operacional.

Saída:
    scripts/saida_testar_sequencias_sg.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def prob(s: int, sp: int, a: np.ndarray, b: np.ndarray) -> float:
    return 0.5 * (1.0 + s * sp * float(np.dot(a, b)))


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_testar_sequencias_sg.md"

    z = np.array([0.0, 0.0, 1.0])
    x = np.array([1.0, 0.0, 0.0])

    p_z_to_z_plus = prob(+1, +1, z, z)
    p_z_to_x_plus = prob(+1, +1, z, x)
    p_z_to_x_minus = prob(+1, -1, z, x)
    p_x_to_z_plus = prob(+1, +1, x, z)
    p_x_to_z_minus = prob(+1, -1, x, z)

    text = f"""# Saída — sequências Stern--Gerlach

Classificação: teste simbólico de consistência operacional.

| sequência | probabilidade |
|---|---:|
| z+ -> z+ | {p_z_to_z_plus:.12f} |
| z+ -> x+ | {p_z_to_x_plus:.12f} |
| z+ -> x- | {p_z_to_x_minus:.12f} |
| x+ -> z+ | {p_x_to_z_plus:.12f} |
| x+ -> z- | {p_x_to_z_minus:.12f} |

Interpretação: eixos incompatíveis redefinem a decomposição dos canais; o
aparelho não revela uma tabela absoluta de valores simultâneos.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
