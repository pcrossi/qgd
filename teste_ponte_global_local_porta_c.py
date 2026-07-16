#!/usr/bin/env python3
"""Testes sintéticos da álgebra da Porta C; não são um background GDQ."""
import numpy as np
from ponte_global_local_porta_c import assemble_porta_c, diagnostics


def main():
    rng = np.random.default_rng(3817)
    n = 14
    B = rng.normal(size=(n, n))
    G = B.T @ B + np.eye(n)
    # Dois vínculos; o terceiro é redundante de propósito.
    DC0 = rng.normal(size=(2, n))
    DC = np.vstack((DC0, DC0[0] + 2 * DC0[1]))
    R = rng.normal(size=(n, 3))
    Q = rng.normal(size=(n, n)); Hs = (Q + Q.T) / 2
    Hc = []
    for _ in range(3):
        Q = rng.normal(size=(n, n)); Hc.append((Q + Q.T) / 2)
    lam = np.array([0.3, -0.2, 0.0])
    out = assemble_porta_c(DC, R, G, Hs, lam, Hc)
    d = diagnostics(out, G)
    assert out.physical_basis.shape[1] == n - 2 - 3
    assert max(d.values()) < 2e-10, d

    # Demonstração explícita: a Hessiana física não é DC.T@DC.
    normal = DC.T @ DC
    assert np.linalg.norm(out.augmented_hessian - normal) > 1.0
    print("PORTA C: teste algébrico aprovado")
    for key, value in d.items():
        print(f"{key} = {value:.3e}")
    print("dimensão física =", out.physical_basis.shape[1])
    print("menor autovalor sintético =", out.eigenvalues[0])
    print("AVISO: valor sintético; não é gap da GDQ")


if __name__ == "__main__":
    main()
