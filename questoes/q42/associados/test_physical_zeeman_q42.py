#!/usr/bin/env python3
"""Teste dimensional de Delta e v com dados externos de um aparelho SG."""

from __future__ import annotations

import argparse
import math


E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
MU_B = 9.2740100657e-24
HBAR = 1.054571817e-34


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--g-geom", type=float, required=True)
    parser.add_argument("--b-perp-tesla", type=float, required=True)
    parser.add_argument("--gradient-tesla-per-m", type=float, required=True)
    parser.add_argument("--speed-m-per-s", type=float, required=True)
    args = parser.parse_args()
    gyromagnetic = abs(args.g_geom) * MU_B / HBAR
    delta = gyromagnetic * abs(args.b_perp_tesla)
    velocity = gyromagnetic * abs(args.speed_m_per_s * args.gradient_tesla_per_m)
    probability = math.exp(-math.pi * delta**2 / (2.0 * velocity))
    print(f"Delta = {delta:.12e} s^-1")
    print(f"v = {velocity:.12e} s^-2")
    print(f"Delta^2/v = {delta**2/velocity:.12e}")
    print(f"P_LZ = {probability:.12e}")


if __name__ == "__main__":
    main()
