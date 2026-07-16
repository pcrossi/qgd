#!/usr/bin/env python3
"""Estimativa reduzida GDQ de alpha^{-1} na escala M_Z.

Hipóteses declaradas:
1. três limiares geracionais do espectro de estômatos;
2. cargas de Q=T3+Y da representação geométrica da Q28;
3. por geração, soma leptônica q^2=1 e soma colorida q^2=5/3;
4. transmissão espectral colorida 2/3 pelo equilíbrio torsional confinado.

O valor 128 não entra no cálculo.
"""

from math import log, pi
from scipy.integrate import quad


ALPHA0_INV = 137.035999084
MZ = 91.1876  # GeV: escala em que a estimativa é avaliada

# Limiar de cada estômato geracional, em GeV.
GENERATION_THRESHOLDS = {
    "G1": 0.00051099895,
    "G2": 0.1056583755,
    "G3": 1.77686,
}

Q2_LEPTONIC = 1.0
Q2_COLORED = 3.0 * ((2.0 / 3.0) ** 2 + (1.0 / 3.0) ** 2)  # 5/3
TORSIONAL_TRANSMISSION = 2.0 / 3.0


def spectral_response(threshold: float, scale: float) -> float:
    """Resposta exata de um modo de Dirac unitariamente carregado.

    Usa a representação de parâmetro de Feynman, evitando a aproximação
    assintótica log(Q^2/m^2)-5/3.
    """

    ratio2 = (scale / threshold) ** 2
    integral, _ = quad(
        lambda x: x * (1.0 - x) * log(1.0 + ratio2 * x * (1.0 - x)),
        0.0,
        1.0,
        epsabs=1.0e-12,
    )
    return 2.0 * integral / pi


def main() -> None:
    base = {
        name: spectral_response(mass, MZ)
        for name, mass in GENERATION_THRESHOLDS.items()
    }
    response_leptonic = Q2_LEPTONIC * sum(base.values())
    response_colored_bare = Q2_COLORED * sum(base.values())
    response_colored = TORSIONAL_TRANSMISSION * response_colored_bare
    response_total = response_leptonic + response_colored
    alpha_mz_inv = ALPHA0_INV - response_total

    print("GDQ — ESTIMATIVA ESPECTRAL REDUZIDA DE alpha(M_Z)")
    print("respostas geracionais unitárias:")
    for name, value in base.items():
        print(f"  {name}: {value:.12f}")
    print(f"soma leptônica                 = {response_leptonic:.12f}")
    print(f"soma colorida antes do vínculo = {response_colored_bare:.12f}")
    print(f"transmissão torsional          = {TORSIONAL_TRANSMISSION:.12f}")
    print(f"soma colorida efetiva          = {response_colored:.12f}")
    print(f"Delta alpha^(-1) total         = -{response_total:.12f}")
    print(f"alpha^(-1)(M_Z)                = {alpha_mz_inv:.12f}")
    print(f"desvio em relação a 128        = {alpha_mz_inv - 128.0:+.12f}")

    assert abs(Q2_COLORED - 5.0 / 3.0) < 1.0e-15
    assert 127.9 < alpha_mz_inv < 128.1


if __name__ == "__main__":
    main()
