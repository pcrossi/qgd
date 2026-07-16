#!/usr/bin/env python3
"""Testes locais que nao dependem de K_gamma nem de dado energetico."""
from __future__ import annotations

import numpy as np

from ponte_global_local_solver_portas_bd import (
    TransportOptions,
    energy_ratio_from_porta_a,
    historical_seed,
    residual_jacobian,
)


def main():
    theta = historical_seed()
    options = TransportOptions(rtol=4e-9, atol=4e-11, collar_steps=90, causal_steps=130)
    residual, jacobian = residual_jacobian(theta, options=options)

    # Auditoria independente: diferenca central do mapa completo somente no
    # teste, em uma direcao deterministica que excita todos os parametros.
    direction = np.arange(1.0, 12.0)
    direction /= np.linalg.norm(direction)
    step = 2.0e-5
    plus, _ = residual_jacobian(theta + step*direction, options=options)
    minus, _ = residual_jacobian(theta - step*direction, options=options)
    finite_difference = (plus - minus)/(2.0*step)
    variational = jacobian @ direction
    relative = np.linalg.norm(finite_difference - variational)/max(1.0, np.linalg.norm(finite_difference))

    singular = np.linalg.svd(jacobian, compute_uv=False)
    assert residual.shape == (10,)
    assert jacobian.shape == (10, 11)
    assert np.all(np.isfinite(residual)) and np.all(np.isfinite(jacobian))
    assert relative < 2.0e-3, relative
    assert np.linalg.matrix_rank(jacobian) == 10

    # A interface energetica exige explicitamente um valor derivado. Testa-se
    # apenas sua regra da cadeia, sem atribuir significado fisico a K=2.
    # Esse valor e fixture de software, nao entrada de busca nem resultado.
    mock = energy_ratio_from_porta_a(2.0)
    residual_e, jacobian_e = residual_jacobian(theta, energy=mock, options=options)
    plus_e, _ = residual_jacobian(theta + step*direction, energy=mock, options=options)
    minus_e, _ = residual_jacobian(theta - step*direction, energy=mock, options=options)
    fd_e = (plus_e - minus_e)/(2.0*step)
    rel_e = np.linalg.norm(fd_e - jacobian_e @ direction)/max(1.0, np.linalg.norm(fd_e))
    assert residual_e.shape == (11,) and jacobian_e.shape == (11, 11)
    assert rel_e < 2.0e-3, rel_e

    print("Teste do transporte variacional das Portas B/D")
    print("relative_directional_error_without_energy =", relative)
    print("relative_directional_error_energy_interface_mock =", rel_e)
    print("singular_values_10x11 =", repr(singular))
    print("rank_10x11 =", np.linalg.matrix_rank(jacobian))
    print("energy_mock_is_software_fixture_only = True")


if __name__ == "__main__":
    main()
