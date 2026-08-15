#!/usr/bin/env python3
"""
GDQ — Chapter 10 / CAR and Pauli

Goal:
    Represent fermionic creation in an exterior algebra of two modes and verify
    that applying the same creation operator twice yields zero.

Theoretical source:
    manuscript/10_spin_statistics_pauli/notes/pauli_car_bohm_barrier.md

Classification:
    Algebraic test. Not a physical prediction.

Output:
    scripts/output_verify_car_pauli.md
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
    out = root / "output_verify_car_pauli.md"

    vacuum: tuple[int, ...] = tuple()
    amp1, s1 = creation(0, vacuum)
    amp2, s2 = creation(0, s1 if s1 is not None else vacuum)
    same_mode_norm = abs(amp1 * amp2)

    amp_a, sa = creation(0, vacuum)
    amp_ab, sab = creation(1, sa if sa is not None else vacuum)
    amp_b, sb = creation(1, vacuum)
    amp_ba, sba = creation(0, sb if sb is not None else vacuum)
    anticomm_sum = amp_a * amp_ab + amp_b * amp_ba

    text = f"""# Output — verify CAR and Pauli

Classification: algebraic test.

| test | value |
|---|---:|
| norm of $(a_0^\\dagger)^2|0\\rangle$ | {same_mode_norm:.12e} |
| amplitude of $a_1^\\dagger a_0^\\dagger|0\\rangle$ | {(amp_a * amp_ab).real:.12f} |
| amplitude of $a_0^\\dagger a_1^\\dagger|0\\rangle$ | {(amp_b * amp_ba).real:.12f} |
| anticommutator sum | {anticomm_sum.real:.12e} |

Interpretation: creating twice in the same mode yields zero; exchanging the order of creation in distinct modes changes the sign.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
