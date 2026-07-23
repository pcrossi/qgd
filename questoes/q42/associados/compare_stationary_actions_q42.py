#!/usr/bin/env python3
"""Compara W on-shell dos ramos gaussiano exterior e cilíndrico."""

from __future__ import annotations

import math


def main() -> None:
    x_c = 1.5
    q2 = math.exp(-x_c) * (1.0 + x_c)
    f0_gaussian = math.log(q2)
    mean_x = (x_c**2 + 2.0 * x_c + 2.0) / (x_c + 1.0)
    bulk_gaussian = 2.0 * mean_x + f0_gaussian - 4.0
    boundary_gaussian = -3.0 * x_c / (1.0 + x_c)
    total_gaussian = bulk_gaussian + boundary_gaussian
    total_cylinder = 0.5 * math.log(math.pi) - 1.5
    difference = total_cylinder - total_gaussian
    print(f"W_G bulk = {bulk_gaussian:.12e}")
    print(f"W_G boundary = {boundary_gaussian:.12e}")
    print(f"W_G total = {total_gaussian:.12e}")
    print(f"W_cylinder = {total_cylinder:.12e}")
    print(f"W_cylinder-W_G = {difference:.12e}")
    print(f"cilindro tem menor W: {difference < 0}")


if __name__ == "__main__":
    main()
