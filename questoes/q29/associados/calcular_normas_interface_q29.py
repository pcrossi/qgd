#!/usr/bin/env python3
"""Transporta normas SU(2)_L e U(1)_Y para a interface l=1 deformada."""

from __future__ import annotations

import argparse
import numpy as np


def generators() -> tuple[list[np.ndarray], np.ndarray]:
    """Geradores anti-simétricos reais em u=(x1+ix2,x3+ix4), com fator 1/2."""
    l1 = np.array(
        [[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0]],
        dtype=float,
    ) / 2.0
    l2 = np.array(
        [[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]],
        dtype=float,
    ) / 2.0
    l3 = np.array(
        [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
        dtype=float,
    ) / 2.0
    hypercharge = np.array(
        [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
        dtype=float,
    ) / 2.0
    return [l1, l2, l3], hypercharge


def norm_integral(points: np.ndarray, generator: np.ndarray, epsilon: float) -> float:
    tangent = points @ generator.T
    y = points[:, 3]
    radial = 1.0 + epsilon * y
    delta_y = tangent[:, 3]
    norm2 = radial**2 * np.sum(tangent**2, axis=1) + epsilon**2 * delta_y**2
    grad_y2 = 1.0 - y**2
    area_weight = radial**3 * np.sqrt(1.0 + epsilon**2 * grad_y2 / radial**2)
    return float(np.sum(area_weight * norm2) / np.sum(area_weight))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=1_000_000)
    parser.add_argument("--epsilon", type=float, default=0.2731376424291)
    args = parser.parse_args()
    rng = np.random.default_rng(29029)
    points = rng.normal(size=(args.samples, 4))
    points /= np.linalg.norm(points, axis=1)[:, None]

    su2, hypercharge = generators()
    norms_w = np.array([norm_integral(points, item, args.epsilon) for item in su2])
    norm_y = norm_integral(points, hypercharge, args.epsilon)
    norms_w_round = np.array([norm_integral(points, item, 0.0) for item in su2])
    norm_y_round = norm_integral(points, hypercharge, 0.0)

    mean_w = float(np.mean(norms_w))
    mean_w_round = float(np.mean(norms_w_round))
    transport = (mean_w / norm_y) / (mean_w_round / norm_y_round)
    ratio_gp2_g2 = (3.0 / 5.0) * transport
    sin2 = ratio_gp2_g2 / (1.0 + ratio_gp2_g2)

    print("Q29 — NORMAS NA INTERFACE DEFORMADA")
    print("epsilon =", args.epsilon)
    print("I_W round =", norms_w_round, "mean=", mean_w_round)
    print("I_Y round =", norm_y_round)
    print("I_W deformed =", norms_w, "mean=", mean_w)
    print("I_Y deformed =", norm_y)
    print("transport ratio =", transport)
    print("g'^2/g^2 transported =", ratio_gp2_g2)
    print("sin² theta transported =", sin2)

    assert np.allclose(norms_w_round, 0.25, atol=2e-4)
    assert abs(norm_y_round - 0.25) < 2e-4
    assert 0.0 < sin2 < 1.0


if __name__ == "__main__":
    main()
