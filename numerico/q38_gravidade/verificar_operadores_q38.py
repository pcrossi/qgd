#!/usr/bin/env python3
"""Verificação independente das identidades operacionais da Q38.

CODATA aparece somente na seção diagnóstica do resíduo. Nenhum valor observado
é usado para construir alpha, Fano, S_inst ou V_eff.
"""

from __future__ import annotations

import math
import numpy as np


PI = math.pi
ALPHA = (9.0 / (8.0 * PI**4)) * ((PI**5 / 1920.0) ** 0.25)
CHI_FANO = 3.0 * math.sqrt(2.0) / 5.0
S_INST = 1.0 / (2.0 * ALPHA)
V_EFF_G = CHI_FANO * math.exp(S_INST) / (ALPHA**4 * (1.0 + ALPHA))
PI1_BARE = 1.0 / V_EFF_G


def schur_spectrum(k_h: float = 1.0, k_t: float = 1.0,
                   g_boundary: float = 0.1) -> np.ndarray:
    """Espectro do Schur no representante isotrópico C=[I_3|0]."""

    c_map = np.zeros((3, 5))
    c_map[:, :3] = np.eye(3)
    k_h_op = k_h * np.eye(3)
    k_t_op = k_t * np.eye(5)
    j_op = math.sqrt(2.0) * g_boundary * c_map
    k_eff = k_h_op - j_op @ np.linalg.solve(k_t_op, j_op.T)
    return np.linalg.eigvalsh(k_eff)


def main() -> None:
    # Referência experimental usada só após a previsão nua.
    g_codata = 6.67430e-11
    mp_codata = 1.672621e-27
    hbar_codata = 1.05457e-34
    c_codata = 299792458.0
    pi1_codata = g_codata * mp_codata**2 / (hbar_codata * c_codata)
    delta_required = math.sqrt(pi1_codata / PI1_BARE) - 1.0

    # Valor legado: apenas controle, não entrada do modelo.
    delta_legacy = 0.0013063
    pi1_legacy = (1.0 + delta_legacy) ** 2 * PI1_BARE

    print("Q38 — VERIFICAÇÃO OPERACIONAL")
    print(f"alpha_geom              = {ALPHA:.15f}")
    print(f"chi_Fano_bulk           = {CHI_FANO:.15f}")
    print(f"S_inst/hbar             = {S_INST:.12f}")
    print(f"exp(-S_inst/hbar)       = {math.exp(-S_INST):.12e}")
    print(f"V_eff_G adimensional    = {V_EFF_G:.12e}")
    print(f"Pi1_bare                = {PI1_BARE:.12e}")
    print(f"Schur eig (teste local) = {schur_spectrum()}")
    print("\nDIAGNÓSTICO POSTERIOR À PREVISÃO")
    print(f"Pi1_CODATA              = {pi1_codata:.12e}")
    print(f"residuo_bare            = {(PI1_BARE/pi1_codata-1)*100:.9f}%")
    print(f"delta_superficie_req    = {delta_required:.12e} ({delta_required*100:.9f}%)")
    print(f"residuo_delta_legado    = {(pi1_legacy/pi1_codata-1)*100:.9f}%")


if __name__ == "__main__":
    main()
