#!/usr/bin/env python3
"""
GDQ — Capítulo 10 / holonomia de troca

Objetivo:
    Verificar a fase de troca fermiônica para circulação ímpar de pi*hbar.

Fonte teórica:
    manuscrito/10_spin_statistics_pauli/notes/holonomia_troca_fermionica.md
    manuscrito/10_spin_statistics_pauli/notes/

Classificação:
    Teste topológico/simbólico. Não é previsão física.

Saída:
    scripts/saida_verificar_holonomia_troca.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_holonomia_troca.md"

    rows = []
    for k in range(-2, 3):
        phase = (2 * k + 1) * np.pi
        hol = np.exp(1j * phase)
        rows.append((k, phase, hol.real, hol.imag, abs(hol + 1)))

    table = "\n".join(
        f"| {k} | {(2*k+1)} pi | {re:.12f} | {im:.12e} | {err:.12e} |"
        for k, phase, re, im, err in rows
    )

    text = f"""# Saída — verificar holonomia de troca fermiônica

Classificação: teste topológico/simbólico.

| k | circulação normalizada | Re(Hol) | Im(Hol) | erro Hol+1 |
|---:|---:|---:|---:|---:|
{table}

Interpretação: circulação $(2k+1)\\pi\\hbar$ produz holonomia $-1$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
