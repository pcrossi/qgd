#!/usr/bin/env python3
"""Norma cinética do potencial de 2-forma associado ao harmônico l=1."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--radius", type=float, default=1.998411184770)
    parser.add_argument("--tau", type=float, default=1.0)
    args = parser.parse_args()
    eigenvalue = 3.0 / args.radius**2
    mean_y2 = 0.25
    norm_a2 = mean_y2 / eigenvalue
    z_reduced = args.tau * norm_a2
    print("Q29 — NORMALIZAÇÃO CINÉTICA DO MODO DE HOPF")
    print(f"lambda_l1 = {eigenvalue:.12e}")
    print(f"<Y²> = {mean_y2:.12e}")
    print(f"<|A_EW|²> = {norm_a2:.12e}")
    print(f"Z_beta/C_GDQ = tau <|A_EW|²> = {z_reduced:.12e}")
    assert eigenvalue > 0.0
    assert norm_a2 > 0.0


if __name__ == "__main__":
    main()
