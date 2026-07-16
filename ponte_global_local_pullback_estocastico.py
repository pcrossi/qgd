#!/usr/bin/env python3
"""Verifica que ruído induzido apenas por difeomorfismos é removido por Pphys.

O teste usa álgebra finita genérica. Ele verifica a identidade estrutural
Pphys R = 0 e, consequentemente, Pphys (R D R*) Pphys* = 0.
Não representa um background físico nem fornece uma covariância da GDQ.
"""
from __future__ import annotations

import numpy as np

from ponte_global_local_porta_c import physical_projector


def main() -> None:
    rng = np.random.default_rng(20260714)
    n_fields, n_constraints, n_gauge = 17, 5, 4
    A = rng.normal(size=(n_fields, n_fields))
    G = A.T @ A + np.eye(n_fields)
    DC = rng.normal(size=(n_constraints, n_fields))
    R = rng.normal(size=(n_fields, n_gauge))
    P, _Z, _combined = physical_projector(DC, R, G)

    B = rng.normal(size=(n_gauge, n_gauge))
    D_coordinate = B @ B.T
    D_fields = R @ D_coordinate @ R.T
    D_physical = P @ D_fields @ P.T

    print("norm_P_R =", np.linalg.norm(P @ R))
    print("norm_D_fields =", np.linalg.norm(D_fields))
    print("norm_D_physical =", np.linalg.norm(D_physical))
    print("relative_projected_noise =", np.linalg.norm(D_physical)/np.linalg.norm(D_fields))


if __name__ == "__main__":
    main()
