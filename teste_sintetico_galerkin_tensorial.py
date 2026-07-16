"""Testes SINTÉTICOS da infraestrutura; não são resultados da GDQ."""

import numpy as np

from ponte_global_local_galerkin_tensorial import (
    GalerkinDensities,
    QuadratureSpec,
    assemble_galerkin,
    convergence_table,
    finite_amplitude_branches,
)


class SyntheticConstantMode:
    """Fixture analítica constante, sem interpretação física."""

    label = "SINTETICO_constante_sem_interpretacao_fisica"

    def densities(self, points, harmonic_cutoff):
        one = np.ones(len(points))
        # Dependência controlada no cutoff testa convergência harmônica.
        tail = 1.0 / (harmonic_cutoff + 2) ** 4
        return GalerkinDensities(
            norm=2 * one,
            quadratic={"curvature": (-4 + tail) * one, "torsion_bismut": one},
            quartic={"curvature": 8 * one},
            sextic=None,
            matching={"a": 2 * one, "c": -4 * one, "u": one},
        )


def main():
    provider = SyntheticConstantMode()
    spec = QuadratureSpec((0.0, 1.0), radial_order=8, angular_order=8)
    result = assemble_galerkin(provider, spec, harmonic_cutoff=30)
    tail = 1.0 / 32**4
    assert abs(result.norm - 4 * np.pi**2) < 1e-8
    assert abs(result.lambda_mu - (-3 + tail) / 2) < 1e-12
    assert abs(result.g_mu - 1 / (np.pi**2)) < 1e-10
    assert abs(result.C_a - 1) < 1e-12
    assert abs(result.C_c + 2) < 1e-12
    assert abs(result.C_u - 0.5) < 1e-12
    branches = finite_amplitude_branches(result)
    assert len(branches) == 1 and branches[0].stable
    rows = convergence_table(provider, spec, [6, 10], [6, 10], [2, 8, 30])
    assert len(rows) == 12
    coarse = [r for r in rows if r["harmonic_cutoff"] == 2][0]["lambda_mu"]
    fine = [r for r in rows if r["harmonic_cutoff"] == 30][0]["lambda_mu"]
    exact = -1.5
    assert abs(fine - exact) < abs(coarse - exact)
    print("TESTE SINTETICO APROVADO — nenhum coeficiente físico foi calculado")
    print("lambda_sintetico =", result.lambda_mu)
    print("g_sintetico =", result.g_mu)
    print("A_sintetica =", branches[0].amplitude)


if __name__ == "__main__":
    main()
