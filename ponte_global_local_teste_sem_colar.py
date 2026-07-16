#!/usr/bin/env python3
"""Teste apontado global--local sem colar em um canal radial de S3.

Com u=R sin(r/R) psi, o Laplaciano radial de S3_R torna-se
    -u'' - R^{-2} u.
O limite local radial em R3 e -u''. Um potencial localizado representa apenas
um operador de teste do defeito; não é a Hessiana completa da GDQ.

Classificacao: teste de consistencia da arquitetura sem interface artificial.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh_tridiagonal


RC = 1.0
V0 = 10.0
H = 0.01
LOCAL_DOMAIN = 80.0


def lowest(length: float, curvature_shift: float):
    n = int(np.ceil(length/H)) - 1
    h = length/(n+1)
    r = h*np.arange(1, n+1)
    potential = -V0*np.exp(-(r/RC)**2) + curvature_shift
    diagonal = 2.0/h**2 + potential
    off = -np.ones(n-1)/h**2
    values, vectors = eigh_tridiagonal(
        diagonal, off, select="i", select_range=(0, 0),
        check_finite=False,
    )
    u = vectors[:, 0]
    probability = u*u
    localized = float(np.sum(probability[r <= 5*RC])/np.sum(probability))
    return float(values[0]), localized, h, n, r, u/np.sqrt(h*np.sum(u*u))


def main() -> None:
    flat, flat_loc, flat_h, flat_n, flat_r, flat_u = lowest(LOCAL_DOMAIN, 0.0)
    print("flat_eigenvalue =", flat)
    print("flat_localization_r_le_5rc =", flat_loc)
    print("flat_h =", flat_h, "flat_n =", flat_n)
    print("R eigenvalue error_to_flat localization predicted_shift")
    errors = []
    for radius in (5.0, 10.0, 20.0, 40.0, 80.0):
        value, loc, h, n, global_r, global_u = lowest(
            np.pi*radius, -1.0/radius**2,
        )
        cutoff = min(10.0, global_r[-1])
        mask = flat_r <= cutoff
        transported = np.interp(flat_r[mask], global_r, global_u)
        transported /= np.sqrt(flat_h*np.sum(transported*transported))
        flat_cut = flat_u[mask]
        flat_cut /= np.sqrt(flat_h*np.sum(flat_cut*flat_cut))
        overlap = abs(flat_h*np.sum(flat_cut*transported))
        projector_error = np.sqrt(max(0.0, 1.0-overlap**2))
        error = value-flat
        errors.append((radius, abs(error)))
        print(radius, value, error, loc, -1.0/radius**2, h, n,
              overlap, projector_error)
    scaled = [err*radius**2 for radius, err in errors]
    print("abs_error_times_R2 =", scaled)
    print("converges =", errors[-1][1] < errors[0][1])


if __name__ == "__main__":
    main()
