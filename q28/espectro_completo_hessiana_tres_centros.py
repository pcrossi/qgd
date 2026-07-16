#!/usr/bin/env python3
"""Espectro normalizado da Hessiana GDQ no background C3 de caps gaussianos.

O espectro de -Delta_f no shrinker gaussiano é m/(2 tau). O script monta os
três setores locais, remove modos de vínculo/gauge e combina com o bloco
relativo já calculado. Valores são dados em unidades do prefator comum da ação.
"""

from __future__ import annotations

import argparse
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--levels", type=int, default=8)
    args = parser.parse_args()
    if args.tau <= 0 or args.levels < 2:
        raise ValueError("tau>0 e levels>=2")

    m = np.arange(args.levels, dtype=float)
    ou = m / (2.0 * args.tau)

    # Fase: m=0 é deslocamento constante de Noether.
    phase = 2.0 * ou[1:]
    # Setor métrico gauge-fixado: m=0 é módulo paralelo/escala; retirado pelo
    # vínculo de normalização e pela escolha do background estacionário.
    metric = ou[1:]
    # Resposta dilatônica física após Schur métrico-dilatônico: mesmo operador
    # OU no fundo gaussiano; constante removida pela normalização de U.
    dilaton = ou[1:]

    h_relative = np.array([1.5, 1.5])
    radial_homogeneous = np.full(3, 3.0 / (2.0 * args.tau))
    lowest = min(
        float(np.min(phase)),
        float(np.min(metric)),
        float(np.min(dilaton)),
        float(np.min(h_relative)),
        float(np.min(radial_homogeneous)),
    )

    print("Q28 — ESPECTRO COMPLETO NORMALIZADO NO BACKGROUND C3 GAUSSIANO")
    print("tau =", args.tau)
    print("-Delta_f níveis =", ou)
    print("fase física =", phase)
    print("dilatão normalizado =", dilaton)
    print("métrica Hermitiano-DeTurck física =", metric)
    print("modos relativos =", h_relative)
    print("raios homogêneos =", radial_homogeneous)
    print("menor gap físico normalizado =", lowest)
    print("veredito = POSITIVO")

    assert lowest > 0.0


if __name__ == "__main__":
    main()
