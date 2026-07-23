#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar limite apontado torus esfera` associada ao capítulo `06_global_local_bridge`.

Verificação didática do limite apontado do Capítulo 6.

Modelo:
- círculo de raio R: ds^2 = dx^2 exatamente em coordenada de arco local;
- esfera S^3_R em coordenada normal radial r:
  ds^2 = dr^2 + R^2 sin(r/R)^2 dOmega_2^2.

No espaço plano R^3, o coeficiente angular é r^2.
O erro relativo local é:

    E_R(r) = |R^2 sin(r/R)^2 - r^2| / r^2.

Para uma janela fixa 0 < r <= L, E_R = O((L/R)^2).
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_limite_apontado_torus_esfera.md")


def sphere_error(R: float, L: float, samples: int = 1000) -> float:
    max_error = 0.0
    for k in range(1, samples + 1):
        r = L * k / samples
        angular = R * R * math.sin(r / R) ** 2
        flat = r * r
        max_error = max(max_error, abs(angular - flat) / flat)
    return max_error


def main() -> None:
    L = 1.0
    radii = [5, 10, 20, 50, 100, 200]
    rows = []
    for R in radii:
        err = sphere_error(R, L)
        scaled = err * R * R / (L * L)
        rows.append((R, err, scaled))

    lines = [
        "---",
        'title: "Saída — limite apontado torus/esfera"',
        "---",
        "",
        "# Saída — limite apontado torus/esfera",
        "",
        "Classificação: verificação de consistência / toy model geométrico.",
        "",
        "Janela local fixa: $0<r\\le 1$.",
        "",
        "| $R$ | erro máximo angular em $S^3_R$ | erro reescalado $E_R R^2$ |",
        "|---:|---:|---:|",
    ]
    for R, err, scaled in rows:
        lines.append(f"| {R} | {err:.12e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusão: o erro local decai como $O(R^{-2})$, compatível com a",
        "convergência apontada usada no Capítulo 6.",
        "",
        "Nota: o círculo grande $S^1_R$ em coordenada de arco local já possui",
        "métrica local plana; a não trivialidade global desaparece apenas no",
        "limite apontado, não por identificação global.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

