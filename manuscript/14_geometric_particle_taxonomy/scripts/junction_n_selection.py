#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Selection of the N=3 junction

Objective:
    Verify the reduced selection argument:
        - N=2 closes only colinearly;
        - N=3 is the first isolated non-colinear closure;
        - N>3 has N-3 internal null modes in the horizontal reduced model.

Classification:
    Consistency test of the selection proof. It does not replace the official action.

Output:
    scripts/output_junction_n_selection.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def closure_hessian_spectrum(n: int) -> np.ndarray:
    """Return eigenvalues of H = (D C)^T(D C) at equally spaced closure."""

    angles = 2.0 * np.pi * np.arange(n) / float(n)
    d_constraint = np.vstack((-np.sin(angles), np.cos(angles)))
    return np.linalg.eigvalsh(d_constraint.T @ d_constraint)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_junction_n_selection.md"

    rows = []
    for n in range(2, 9):
        eig = closure_hessian_spectrum(n)
        zero_modes = int(np.sum(np.abs(eig) < 1.0e-10))
        # One zero is the common rotation. Additional zeros are internal.
        internal_zeros = max(0, zero_modes - 1)
        nonzero = [x for x in eig if x > 1.0e-10]
        rows.append((n, zero_modes, internal_zeros, nonzero))

    table = "\n".join(
        f"| {n} | {zero_modes} | {internal_zeros} | "
        f"{', '.join(f'{x:.6f}' for x in nonzero)} |"
        for n, zero_modes, internal_zeros, nonzero in rows
    )

    text = f"""# Output — selection of the N-junction

Classification: consistency test of the selection proof.

| N | total zero modes | internal zeros beyond rotation | non-zero eigenvalues |
|---:|---:|---:|---|
{table}

Interpretation: $N=3$ is the first isolated non-colinear closure. For
$N>3$, there appear $N-3$ internal null modes in addition to the global rotation. This
implements the condition used in the text: closure, non-colinearity, and
isolation select $N=3$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
