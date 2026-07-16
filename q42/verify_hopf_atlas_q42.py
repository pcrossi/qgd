#!/usr/bin/env python3
"""Verifica numericamente projetor, transição e métrica do atlas de Hopf."""

from __future__ import annotations

import numpy as np


def section_north(w: complex) -> np.ndarray:
    return np.array([1.0, w], dtype=complex) / np.sqrt(1.0 + abs(w) ** 2)


def section_south(w_prime: complex) -> np.ndarray:
    return np.array([w_prime, 1.0], dtype=complex) / np.sqrt(
        1.0 + abs(w_prime) ** 2
    )


def projector(u: np.ndarray) -> np.ndarray:
    return np.outer(u, u.conj())


def main() -> None:
    samples = [0.4 + 0.7j, -1.2 + 0.3j, 2.0 - 1.0j]
    maximum_projector_error = 0.0
    maximum_transition_error = 0.0
    for w in samples:
        north = section_north(w)
        south = section_south(1.0 / w)
        transition = abs(w) / w
        maximum_projector_error = max(
            maximum_projector_error,
            float(np.linalg.norm(projector(north) - projector(south))),
        )
        maximum_transition_error = max(
            maximum_transition_error,
            float(np.linalg.norm(south - transition * north)),
        )

    w = 0.6 + 0.8j
    step = 1e-6
    p0 = projector(section_north(w))
    px = projector(section_north(w + step))
    py = projector(section_north(w + 1j * step))
    dp_x = (px - p0) / step
    dp_y = (py - p0) / step
    metric_xx = float(np.real(np.trace(dp_x @ dp_x)))
    metric_yy = float(np.real(np.trace(dp_y @ dp_y)))
    expected = 2.0 / (1.0 + abs(w) ** 2) ** 2

    print(f"erro máximo dos projetores = {maximum_projector_error:.3e}")
    print(f"erro máximo da transição = {maximum_transition_error:.3e}")
    print(f"Tr(dP_x^2) = {metric_xx:.12e}")
    print(f"Tr(dP_y^2) = {metric_yy:.12e}")
    print(f"métrica esperada = {expected:.12e}")
    print(f"erro relativo x = {abs(metric_xx-expected)/expected:.3e}")
    print(f"erro relativo y = {abs(metric_yy-expected)/expected:.3e}")


if __name__ == "__main__":
    main()
