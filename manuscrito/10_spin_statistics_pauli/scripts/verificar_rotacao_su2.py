#!/usr/bin/env python3
"""
GDQ — Capítulo 10 / rotação spinorial

Objetivo:
    Verificar numericamente a identidade U(2pi)=-I e U(4pi)=I para SU(2).

Fonte teórica:
    manuscrito/10_spin_statistics_pauli/notes/rotacao_2pi_4pi_su2.md
    manuscrito/10_spin_statistics_pauli/notes/

Classificação:
    Teste simbólico. Não é previsão física.

Saída:
    scripts/saida_verificar_rotacao_su2.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_rotacao_su2.md"

    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    n = np.array([0.3, -0.4, 0.5], dtype=float)
    n = n / np.linalg.norm(n)
    nsigma = n[0] * sx + n[1] * sy + n[2] * sz

    def U(theta: float) -> np.ndarray:
        return np.cos(theta / 2) * np.eye(2) - 1j * np.sin(theta / 2) * nsigma

    err_2pi = np.linalg.norm(U(2 * np.pi) + np.eye(2))
    err_4pi = np.linalg.norm(U(4 * np.pi) - np.eye(2))

    text = f"""# Saída — verificar rotação spinorial SU(2)

Classificação: teste simbólico.

| teste | erro Frobenius |
|---|---:|
| $U(2\\pi)+I$ | {err_2pi:.12e} |
| $U(4\\pi)-I$ | {err_4pi:.12e} |

Interpretação: a rotação spinorial realiza $2\\pi\\mapsto -I$ e
$4\\pi\\mapsto I$, como exigido para spin $1/2$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
