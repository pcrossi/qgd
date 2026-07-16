#!/usr/bin/env python3
"""Q29 — auditoria sem ajuste do setor eletrofraco com entradas já derivadas."""

from __future__ import annotations

import math


def main() -> None:
    alpha = 1.0 / 137.03599907
    e = math.sqrt(4.0 * math.pi * alpha)
    sin2 = 3.0 / 8.0
    g = e / math.sqrt(sin2)
    gp = e / math.sqrt(1.0 - sin2)

    # Candidato geométrico já existente; usa m_p como calibração dimensional.
    proton_mass = 0.93827208816
    volume_k = 6.0 * math.pi**5
    transverse_dimension = 7.0
    v_candidate = proton_mass * volume_k / transverse_dimension

    mw = 0.5 * g * v_candidate
    mz = 0.5 * math.hypot(g, gp) * v_candidate
    gf = 1.0 / (math.sqrt(2.0) * v_candidate**2)

    references = {
        "v": 246.21965,
        "mW": 80.379,
        "mZ": 91.1876,
        "GF": 1.1663787e-5,
    }

    def deviation(value: float, reference: float) -> float:
        return 100.0 * (value / reference - 1.0)

    print("Q29 — AUDITORIA COM ENTRADAS GDQ JÁ DERIVADAS")
    print(f"e = {e:.12f}")
    print(f"g = {g:.12f}")
    print(f"g' = {gp:.12f}")
    print(f"sin²(theta_W) = {sin2:.12f}")
    print(f"v candidato = {v_candidate:.12f} GeV ({deviation(v_candidate, references['v']):+.6f}%)")
    print(f"G_F = {gf:.12e} GeV^-2 ({deviation(gf, references['GF']):+.6f}%)")
    print(f"m_W = {mw:.12f} GeV ({deviation(mw, references['mW']):+.6f}%)")
    print(f"m_Z = {mz:.12f} GeV ({deviation(mz, references['mZ']):+.6f}%)")
    print("a2 e a4: não determinados pela ação nos documentos atuais")


if __name__ == "__main__":
    main()
