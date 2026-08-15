#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `cayley signal interface` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / Cayley Interface.

Constructs a reduced Hermitian impedance Z and calculates:

    S = (I - i Z)(I + i Z)^-1

verifying S†S=I. Also records a simple contractive open channel.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_cayley_signal_interface.md"

    z = np.array([[0.4, 0.1], [0.1, -0.2]], dtype=float)
    eye = np.eye(2, dtype=complex)
    s = (eye - 1j * z) @ np.linalg.inv(eye + 1j * z)
    unitarity_error = np.linalg.norm(s.conj().T @ s - eye, ord=2)

    # Open channel: multiply by scalar loss to demonstrate contraction.
    loss = 0.96
    s_open = loss * s
    contraction_min = np.linalg.eigvalsh(eye - s_open.conj().T @ s_open).min().real

    text = f"""# Output — Cayley interface

Classification: consistency test of reduced interface.

| quantity | value |
|---|---:|
| closed unitarity error | {unitarity_error:.15e} |
| open loss | {loss:.12f} |
| open min eig(I-S†S) | {contraction_min:.15e} |

Interpretation: Hermitian impedance generates a closed unitary interface; apparatus loss
generates contraction. This does not prove asymptotic complexity.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
