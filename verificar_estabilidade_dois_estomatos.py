#!/usr/bin/env python3
"""Verifica monotonicidade da interação local 4D de dois estômatos."""

from __future__ import annotations

import numpy as np


def interaction(distance: np.ndarray, charge_product: float) -> np.ndarray:
    return charge_product / distance**2


def derivative(distance: np.ndarray, charge_product: float) -> np.ndarray:
    return -2.0 * charge_product / distance**3


def main() -> None:
    distance = np.geomspace(1.0e-3, 1.0e3, 10000)
    for product, label in [(1.0, "mesmo sinal"), (-1.0, "sinais opostos")]:
        energy = interaction(distance, product)
        slope = derivative(distance, product)
        stationary = bool(np.any(np.isclose(slope, 0.0, atol=0.0, rtol=1e-13)))
        monotonic = bool(np.all(np.diff(energy) < 0.0) or np.all(np.diff(energy) > 0.0))
        print(label)
        print("  monotônica:", monotonic)
        print("  ponto estacionário finito:", stationary)
        assert monotonic
        assert not stationary


if __name__ == "__main__":
    main()
