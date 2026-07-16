#!/usr/bin/env python3
"""Avalia candidatos externos a Lambda_EM sem promovê-los a derivações."""

import math

from sweep_especies_u1 import (
    charged_fermion_benchmark,
    leptons_gdq,
    pi_infinity,
)


ME_GEV = 0.00051099895
LAMBDA_EW_GEV = 126354.3162


def main() -> int:
    ratio = LAMBDA_EW_GEV / ME_GEV
    log_ratio = math.log10(ratio)
    pi_leptons = pi_infinity(log_ratio, leptons_gdq())
    pi_all = pi_infinity(log_ratio, charged_fermion_benchmark())

    print("Hipótese condicional: Lambda_EM = Lambda_0^EW")
    print(f"Lambda_0^EW/m_e = {ratio:.12e}")
    print(f"log10(Lambda_0^EW/m_e) = {log_ratio:.12f}")
    print(f"Pi_inf (léptons Q39) = {pi_leptons:.12f}")
    print(f"Pi_inf (benchmark completo) = {pi_all:.12f}")

    assert pi_leptons < 1.0
    assert pi_all < 1.0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
