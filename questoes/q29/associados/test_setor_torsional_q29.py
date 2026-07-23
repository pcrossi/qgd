#!/usr/bin/env python3
"""Verifica sinais do modo torsional e de sua retroação estável."""

from __future__ import annotations

import numpy as np


def main() -> None:
    tau = 1.0
    a2 = -tau / 6.0
    k = np.diag([0.5, 1.0, 1.5])
    c = np.array([0.2, -0.1, 0.3])
    quartic_backreaction = -0.5 * c @ np.linalg.solve(k, c)
    threshold_intrinsic = -quartic_backreaction
    print("Q29 — SETOR TORSIONAL")
    print("a2 =", a2)
    print("Delta V4 backreaction =", quartic_backreaction)
    print("V4 intrínseco mínimo para estabilidade =", threshold_intrinsic)
    assert a2 < 0.0
    assert quartic_backreaction <= 0.0
    assert threshold_intrinsic >= 0.0


if __name__ == "__main__":
    main()
