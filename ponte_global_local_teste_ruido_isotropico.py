#!/usr/bin/env python3
"""Teste de Itô/Gauss para ruído isotrópico no mapa de colagem.

Para uma perturbação gaussiana centrada com Cov(delta theta)=s I,

    E[F(theta+delta theta)] = F(theta) + (s/2) Delta_theta F + O(s^2).

Este e somente um teste de consistencia em coordenadas de tiro. A identidade
nao e a metrica fisica da GDQ e o parametro s nao pode ser interpretado como
amplitude fisica antes do pullback da forma cinetica oficial.
"""
from __future__ import annotations

import numpy as np

from ponte_global_local_teste_sela_estatistica_vetorial import THETA, field


def main() -> None:
    f0 = field(THETA)
    for step in (5.0e-4, 1.0e-3, 2.0e-3):
        laplacian = np.zeros_like(f0)
        used = []
        for j in range(THETA.size):
            local_step = step
            for _attempt in range(14):
                direction = np.zeros_like(THETA)
                direction[j] = local_step
                try:
                    fp, fm = field(THETA + direction), field(THETA - direction)
                    break
                except (RuntimeError, FloatingPointError):
                    local_step *= 0.5
            else:
                raise RuntimeError(f"direcao {j} nao admite diferenca central")
            laplacian += (fp - 2*f0 + fm)/local_step**2
            used.append(local_step)
        curvature = 0.5*laplacian
        variance = -float(curvature @ f0)/float(curvature @ curvature)
        corrected = f0 + variance*curvature
        print(f"step={step:.1e}")
        print("  isotropic_variance_ls =", variance)
        print("  residual_2_before =", np.linalg.norm(f0))
        print("  residual_2_after =", np.linalg.norm(corrected))
        print("  residual_inf_after =", np.linalg.norm(corrected, ord=np.inf))
        print("  reduction_factor =", np.linalg.norm(corrected)/np.linalg.norm(f0))
        print("  positive_covariance =", variance > 0.0)
        print("  directional_steps =", used)


if __name__ == "__main__":
    main()
