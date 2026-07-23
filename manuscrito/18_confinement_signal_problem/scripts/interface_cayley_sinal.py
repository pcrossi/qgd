#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `interface cayley sinal` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / Interface de Cayley.

Constrói uma impedância Hermitiana reduzida Z e calcula:

    S = (I - i Z)(I + i Z)^-1

verificando S†S=I. Também registra um canal aberto contrativo simples.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_interface_cayley_sinal.md"

    z = np.array([[0.4, 0.1], [0.1, -0.2]], dtype=float)
    eye = np.eye(2, dtype=complex)
    s = (eye - 1j * z) @ np.linalg.inv(eye + 1j * z)
    unitarity_error = np.linalg.norm(s.conj().T @ s - eye, ord=2)

    # Canal aberto: multiplica por perda escalar para demonstrar contração.
    loss = 0.96
    s_open = loss * s
    contraction_min = np.linalg.eigvalsh(eye - s_open.conj().T @ s_open).min().real

    text = f"""# Saída — interface de Cayley

Classificação: teste de consistência de interface reduzida.

| quantidade | valor |
|---|---:|
| erro de unitariedade fechado | {unitarity_error:.15e} |
| perda aberta | {loss:.12f} |
| min eig(I-S†S) aberto | {contraction_min:.15e} |

Interpretação: impedância Hermitiana gera interface fechada unitária; perda de
aparelho gera contração. Isso não prova complexidade assintótica.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
