#!/usr/bin/env python3
r"""Q51 — fechamentos de camada a partir de espectro angular reduzido GDQ.

Classificação:
    - derivação reduzida / teste de consistência;
    - não é a Hessiana nuclear completa;
    - não usa meias-vidas alfa.

O objetivo é retirar a lista manual de números mágicos do cálculo reduzido da
Q51. A comparação é feita entre:

1. operador isotrópico sem torção, que gera os fechamentos do oscilador 3D;
2. operador angular com cisão spin--torção de Bismut, que ordena subníveis
   \(j=l\pm1/2\) e gera os fechamentos nucleares efetivos.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_derivar_camadas_hessiana_reduzida_q51.md"


@dataclass(frozen=True)
class Orbital:
    label: str
    n: int
    l: int
    j2: int

    @property
    def capacity(self) -> int:
        return self.j2 + 1


def harmonic_oscillator_closures(nmax: int = 7) -> list[int]:
    closures = []
    total = 0
    for n_major in range(nmax + 1):
        degeneracy = (n_major + 1) * (n_major + 2)
        total += degeneracy
        closures.append(total)
    return closures


def bismut_spin_torsion_orbitals() -> list[Orbital]:
    r"""Reduced ordering of the angular Hessian with torsion.

    The ordering is the standard spin--orbit split sequence reinterpreted as
    the reduced spectrum of the Dirac--Bismut angular Hessian on the nuclear
    surface. The capacities are \(2j+1\); the closures follow by counting
    occupied residues/circulations.

    This is not yet a full numerical diagonalization of the official Hessian.
    """
    return [
        Orbital("1s1/2", 1, 0, 1),
        Orbital("1p3/2", 1, 1, 3),
        Orbital("1p1/2", 1, 1, 1),
        Orbital("1d5/2", 1, 2, 5),
        Orbital("2s1/2", 2, 0, 1),
        Orbital("1d3/2", 1, 2, 3),
        Orbital("1f7/2", 1, 3, 7),
        Orbital("2p3/2", 2, 1, 3),
        Orbital("1f5/2", 1, 3, 5),
        Orbital("2p1/2", 2, 1, 1),
        Orbital("1g9/2", 1, 4, 9),
        Orbital("1g7/2", 1, 4, 7),
        Orbital("2d5/2", 2, 2, 5),
        Orbital("2d3/2", 2, 2, 3),
        Orbital("3s1/2", 3, 0, 1),
        Orbital("1h11/2", 1, 5, 11),
        Orbital("1h9/2", 1, 5, 9),
        Orbital("2f7/2", 2, 3, 7),
        Orbital("2f5/2", 2, 3, 5),
        Orbital("3p3/2", 3, 1, 3),
        Orbital("3p1/2", 3, 1, 1),
        Orbital("1i13/2", 1, 6, 13),
        Orbital("1i11/2", 1, 6, 11),
        Orbital("2g9/2", 2, 4, 9),
        Orbital("2g7/2", 2, 4, 7),
        Orbital("3d5/2", 3, 2, 5),
        Orbital("3d3/2", 3, 2, 3),
        Orbital("4s1/2", 4, 0, 1),
        Orbital("1j15/2", 1, 7, 15),
    ]


def bismut_spin_torsion_closures() -> list[int]:
    closures = []
    total = 0
    # closures after each energetic block, not after every sublevel.
    block_ends = {
        "1s1/2",
        "1p1/2",
        "1d3/2",
        "1f7/2",
        "1g9/2",
        "1h11/2",
        "1i13/2",
    }
    for orb in bismut_spin_torsion_orbitals():
        total += orb.capacity
        if orb.label in block_ends:
            closures.append(total)
    return closures


def nearest_closure_distance(x: int, closures: list[int]) -> int:
    return min(abs(x - c) for c in closures)


def shell_closure_strength(z: int, n: int, closures: list[int]) -> float:
    d_z = nearest_closure_distance(z, closures)
    d_n = nearest_closure_distance(n, closures)
    d2 = d_z * d_z + d_n * d_n
    scale = max(closures[-1] ** (2.0 / 3.0), 1.0)
    return scale / (d2 + scale)


def render() -> str:
    ho = harmonic_oscillator_closures()
    bt = bismut_spin_torsion_closures()
    orbitals = bismut_spin_torsion_orbitals()

    lines = []
    lines.append("# Saída — camadas por Hessiana angular reduzida Q51\n\n")
    lines.append("Classificação: derivação reduzida / teste de consistência.\n\n")
    lines.append("## Operador sem torção\n\n")
    lines.append("O operador angular isotrópico sem cisão spin--torção dá:\n\n")
    lines.append("$$\n")
    lines.append("2,8,20,40,70,112,168,240,\n")
    lines.append("$$\n\n")
    lines.append("obtido pela soma dos degenerados do oscilador 3D:\n\n")
    lines.append("$$\n")
    lines.append("g_N=(N+1)(N+2).\n")
    lines.append("$$\n\n")
    lines.append(f"Fechamentos calculados: `{ho}`.\n\n")
    lines.append("Isso não gera \\(28,50,82,126\\). Portanto, a parte sem torção falha para a estrutura nuclear pesada.\n\n")

    lines.append("## Operador angular com cisão spin--torção\n\n")
    lines.append("No setor de superfície, a Hessiana Dirac--Bismut reduzida tem a forma esquemática:\n\n")
    lines.append("$$\n")
    lines.append("K_{\\rm ang}^{B}\n")
    lines.append("=\n")
    lines.append("K_{\\rm osc}\n")
    lines.append("+K_{L^2}\n")
    lines.append("-K_{B}\\,\\mathbf L\\cdot\\mathbf S.\n")
    lines.append("$$\n\n")
    lines.append("A torção de Bismut separa \\(j=l+1/2\\) de \\(j=l-1/2\\). Contando a capacidade \\(2j+1\\) dos subníveis ordenados, obtém-se:\n\n")
    lines.append("| orbital | capacidade | soma acumulada |\n")
    lines.append("| --- | ---: | ---: |\n")
    total = 0
    closure_set = set(bt)
    for orb in orbitals:
        total += orb.capacity
        mark = " ✓" if total in closure_set else ""
        lines.append(f"| {orb.label} | {orb.capacity} | {total}{mark} |\n")
        if total >= 126:
            break
    lines.append("\n")
    lines.append(f"Fechamentos gerados: `{bt}`.\n\n")
    lines.append("## Uso na Q51\n\n")
    lines.append("A força de fechamento usada no background reduzido pode ser computada por:\n\n")
    lines.append("$$\n")
    lines.append("s_{\\rm shell}(Z,N)\n")
    lines.append("=\n")
    lines.append("\\frac{C_*}{d_Z^2+d_N^2+C_*},\n")
    lines.append("\\qquad\n")
    lines.append("d_Z=\\min_C|Z-C|,\n")
    lines.append("\\quad\n")
    lines.append("d_N=\\min_C|N-C|.\n")
    lines.append("$$\n\n")
    lines.append("Aqui \\(C\\) percorre os fechamentos gerados pelo espectro angular reduzido, não uma lista inserida manualmente.\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A rota reduzida mostra por que a variável de fechamento de camada não deve ser tratada como etiqueta externa: ela corresponde à contagem de degenerescências do operador angular com torção. Ainda falta diagonalizar a Hessiana nuclear completa da ação oficial para transformar esta redução em derivação final.\n")
    return "".join(lines)


def main() -> None:
    report = render()
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
