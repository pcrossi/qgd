#!/usr/bin/env python3
"""
GDQ — Capítulo 10 / CAR e Pauli

Objetivo:
    Representar criação fermiônica em álgebra exterior de dois modos e verificar
    que aplicar duas vezes o mesmo operador de criação dá zero.

Fonte teórica:
    manuscrito/10_spin_statistics_pauli/notes/pauli_car_barreira_bohm.md
    manuscrito/10_spin_statistics_pauli/notes/

Classificação:
    Teste algébrico. Não é previsão física.

Saída:
    scripts/saida_verificar_car_pauli.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def creation(mode: int, state: tuple[int, ...], n_modes: int = 2) -> tuple[complex, tuple[int, ...] | None]:
    if mode in state:
        return 0.0, None
    sign = (-1) ** sum(1 for m in state if m < mode)
    new_state = tuple(sorted(state + (mode,)))
    return complex(sign), new_state


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_car_pauli.md"

    vacuum: tuple[int, ...] = tuple()
    amp1, s1 = creation(0, vacuum)
    amp2, s2 = creation(0, s1 if s1 is not None else vacuum)
    same_mode_norm = abs(amp1 * amp2)

    amp_a, sa = creation(0, vacuum)
    amp_ab, sab = creation(1, sa if sa is not None else vacuum)
    amp_b, sb = creation(1, vacuum)
    amp_ba, sba = creation(0, sb if sb is not None else vacuum)
    anticomm_sum = amp_a * amp_ab + amp_b * amp_ba

    text = f"""# Saída — verificar CAR e Pauli

Classificação: teste algébrico.

| teste | valor |
|---|---:|
| norma de $(a_0^\\dagger)^2|0\\rangle$ | {same_mode_norm:.12e} |
| amplitude de $a_1^\\dagger a_0^\\dagger|0\\rangle$ | {(amp_a * amp_ab).real:.12f} |
| amplitude de $a_0^\\dagger a_1^\\dagger|0\\rangle$ | {(amp_b * amp_ba).real:.12f} |
| soma anticomutadora | {anticomm_sum.real:.12e} |

Interpretação: criar duas vezes no mesmo modo dá zero; trocar a ordem de
criação em modos distintos muda o sinal.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
