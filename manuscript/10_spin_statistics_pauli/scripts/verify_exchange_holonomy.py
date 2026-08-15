#!/usr/bin/env python3
"""
GDQ — Chapter 10 / exchange holonomy

Goal:
    Verify the fermionic exchange phase for an odd circulation of pi*hbar.

Theoretical source:
    manuscript/10_spin_statistics_pauli/notes/fermionic_exchange_holonomy.md

Classification:
    Topological/symbolic test. Not a physical prediction.

Output:
    scripts/output_verify_exchange_holonomy.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_exchange_holonomy.md"

    rows = []
    for k in range(-2, 3):
        phase = (2 * k + 1) * np.pi
        hol = np.exp(1j * phase)
        rows.append((k, phase, hol.real, hol.imag, abs(hol + 1)))

    table = "\n".join(
        f"| {k} | {(2*k+1)} pi | {re:.12f} | {im:.12e} | {err:.12e} |"
        for k, phase, re, im, err in rows
    )

    text = f"""# Output — verify fermionic exchange holonomy

Classification: topological/symbolic test.

| k | normalized circulation | Re(Hol) | Im(Hol) | Hol+1 error |
|---:|---:|---:|---:|---:|
{table}

Interpretation: circulation $(2k+1)\\pi\\hbar$ produces $-1$ holonomy.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
