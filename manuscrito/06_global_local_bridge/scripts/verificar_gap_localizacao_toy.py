#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar gap localizacao toy` associada ao capítulo `06_global_local_bridge`.

Toy model de localização e gap uniforme.

Operador discreto:

    K_L = -d^2/dx^2 + V(x)

em [-L,L], Dirichlet, com poço local V=-V0 em |x|<a e exterior V=0.

Aumentamos L. O modo ligado permanece localizado e separado do contínuo
discretizado, ilustrando o papel de Agmon/IMS. Isto não é Hessiana GDQ real.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("saida_verificar_gap_localizacao_toy.md")


def operator(L: float, h: float = 0.04, V0: float = 8.0, a: float = 1.0):
    # Pontos internos com condição de Dirichlet nos extremos.
    n = int(round(2.0 * L / h)) - 1
    x = np.linspace(-L + h, L - h, n)
    h = x[1] - x[0]
    diag = np.full(n, 2.0 / h**2)
    off = np.full(n - 1, -1.0 / h**2)
    V = np.where(np.abs(x) < a, -V0, 0.0)
    K = np.diag(diag + V) + np.diag(off, 1) + np.diag(off, -1)
    return x, K


def main() -> None:
    rows = []
    for L in [4, 6, 8, 10, 14, 18]:
        x, K = operator(L)
        vals, vecs = np.linalg.eigh(K)
        bound = vals[0]
        next_val = vals[1]
        gap = next_val - bound
        psi = vecs[:, 0]
        psi = psi / np.sqrt(np.trapezoid(psi * psi, x))
        outside = np.trapezoid((psi * psi)[np.abs(x) > 2.0], x[np.abs(x) > 2.0])
        rows.append((L, bound, next_val, gap, outside))

    lines = [
        "---",
        'title: "Saída — gap e localização toy"',
        "---",
        "",
        "# Saída — gap e localização toy",
        "",
        "Classificação: toy model espectral / verificação de consistência.",
        "",
        "| $L$ | autovalor ligado | próximo autovalor | gap | massa fora de $|x|>2$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for L, bound, next_val, gap, outside in rows:
        lines.append(
            f"| {L:.0f} | {bound:.10f} | {next_val:.10f} | {gap:.10f} | {outside:.3e} |"
        )

    lines += [
        "",
        "Conclusão: o modo ligado fica localizado no núcleo enquanto o domínio",
        "externo cresce. Isso ilustra por que a ponte global--local deve usar gap",
        "físico do defeito, não gap artificial de compactificação.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()
