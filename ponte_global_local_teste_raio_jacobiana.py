#!/usr/bin/env python3
"""Teste de posto após inserir o vínculo de raio cosmológico.

Classificação: teste de consistência da formulação reduzida. Não é busca de
sela física e não usa dado experimental como alvo ajustável.
"""
import numpy as np
from ponte_global_local_busca_jacobiana_variacional import value_jac_with_radius

SEED=np.array([
    -7.75631235e-1,-1.00456477,-4.39191944e-5,-1.43954597,
    -9.33914189e-1,-3.63068075e-1,-1.54334445e-3,-2.28771423,
    -2.90976275,-1.15737646e-2,
])

def main():
    residual,jac=value_jac_with_radius(SEED,log_R_cos=0.0)
    singular=np.linalg.svd(jac,compute_uv=False)
    tol=max(jac.shape)*np.finfo(float).eps*singular[0]
    print("Teste do vínculo de raio cosmológico")
    print("residual =",residual)
    print("singular_values =",singular)
    print("rank =",np.sum(singular>tol))
    print("null_rows_expected = 1  # fluxo de fase; deve virar C_E")

if __name__=="__main__":
    main()
