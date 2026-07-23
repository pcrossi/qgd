#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular alpha media einstein` associada ao capítulo `16_fine_structure_zeeman_gminus2`.

GDQ — Capítulo 16 / alpha como média de Einstein.

Este script avalia a expressão geométrica

    alpha_E = 9/(8*pi^4) * (pi^5/1920)^(1/4)

sem usar o valor experimental de alpha. A classificação é avaliação direta de
quantidade já derivada na média isotrópica/Hessiana da estrutura fina por média isotrópica/Hessiana.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_alpha_media_einstein.md"

    p_iso = 9.0 / (8.0 * math.pi**4)
    c_e = (math.pi**5 / 1920.0) ** 0.25
    alpha = p_iso * c_e
    z_q = 1.0 / (4.0 * math.pi * alpha)

    text = f"""# Saída — alpha como média de Einstein

Classificação: avaliação direta de quantidade já derivada; não usa CODATA.

| quantidade | valor |
|---|---:|
| P_iso | {p_iso:.15e} |
| C_E | {c_e:.15e} |
| alpha_E_mean | {alpha:.15e} |
| alpha_E_mean^-1 | {1.0/alpha:.12f} |
| Z_Q = 1/(4*pi*alpha) | {z_q:.12f} |

Interpretação: o valor é a média global isotrópica do canal eletromagnético no
espaço cosmológico de Einstein, herdada pelo laboratório sob a ponte
global--local.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
