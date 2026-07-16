#!/usr/bin/env python3
"""Simulação diagnóstica das massas W/Z na Q29, sem ajuste às massas alvo."""

from __future__ import annotations

import math
import numpy as np


V_GDQ = 246.111195995615


def spectrum(alpha_inverse: float, sin2: float) -> dict[str, float]:
    alpha = 1.0 / alpha_inverse
    e = math.sqrt(4.0 * math.pi * alpha)
    g = e / math.sqrt(sin2)
    gp = e / math.sqrt(1.0 - sin2)
    charged = 0.5 * g * V_GDQ
    neutral = (V_GDQ**2 / 4.0) * np.array(
        [[g**2, -g * gp], [-g * gp, gp**2]], dtype=float
    )
    eigenvalues = np.linalg.eigvalsh(neutral)
    return {
        "alpha_inverse": alpha_inverse,
        "sin2": sin2,
        "e": e,
        "g": g,
        "gp": gp,
        "mW": charged,
        "mPhoton": math.sqrt(max(0.0, float(eigenvalues[0]))),
        "mZ": math.sqrt(float(eigenvalues[1])),
        "ratio": charged / math.sqrt(float(eigenvalues[1])),
    }


def main() -> None:
    cases = [
        ("geométrico comum", 137.03599907, 3.0 / 8.0),
        ("interface + 2/9", 137.03599907, 2.0 / 9.0),
        ("resolução EW + 3/8", 128.0, 3.0 / 8.0),
        ("resolução EW + 2/9", 128.0, 2.0 / 9.0),
    ]
    print("Q29 — SIMULAÇÃO W/Z")
    print(f"v = {V_GDQ:.12f} GeV")
    print("caso | alpha^-1 | sin² | g | g' | mW | mZ | mγ | mW/mZ")
    for label, alpha_inverse, sin2 in cases:
        result = spectrum(alpha_inverse, sin2)
        print(
            f"{label} | {alpha_inverse:.8f} | {sin2:.8f} | "
            f"{result['g']:.8f} | {result['gp']:.8f} | "
            f"{result['mW']:.8f} | {result['mZ']:.8f} | "
            f"{result['mPhoton']:.3e} | {result['ratio']:.8f}"
        )
        assert result["mPhoton"] < 1.0e-6
        assert math.isclose(result["ratio"], math.sqrt(1.0 - sin2), rel_tol=1e-12)


if __name__ == "__main__":
    main()
