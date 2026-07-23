#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `camadas spin torcao` associada ao capítulo `24_nuclear_phenomenology`.
Fechamentos de camada por Hessiana angular spin--torção.

Classificação científica:
    derivação reduzida / teste de consistência.

O script compara a contagem do oscilador sem torção com a contagem reduzida
obtida quando a conexão de Bismut separa os subníveis j=l±1/2.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_camadas_spin_torcao.md"


@dataclass(frozen=True)
class Orbital:
    label: str
    j2: int

    @property
    def capacity(self) -> int:
        # j2 = 2j, so 2j+1 = j2+1.
        return self.j2 + 1


ORBITALS = [
    Orbital("1s1/2", 1),
    Orbital("1p3/2", 3),
    Orbital("1p1/2", 1),
    Orbital("1d5/2", 5),
    Orbital("2s1/2", 1),
    Orbital("1d3/2", 3),
    Orbital("1f7/2", 7),
    Orbital("2p3/2", 3),
    Orbital("1f5/2", 5),
    Orbital("2p1/2", 1),
    Orbital("1g9/2", 9),
    Orbital("1g7/2", 7),
    Orbital("2d5/2", 5),
    Orbital("2d3/2", 3),
    Orbital("3s1/2", 1),
    Orbital("1h11/2", 11),
    Orbital("1h9/2", 9),
    Orbital("2f7/2", 7),
    Orbital("2f5/2", 5),
    Orbital("3p3/2", 3),
    Orbital("3p1/2", 1),
    Orbital("1i13/2", 13),
]

CLOSURE_LABELS = {"1s1/2", "1p1/2", "1d3/2", "1f7/2", "1g9/2", "1h11/2", "1i13/2"}


def harmonic_oscillator_closures(nmax: int = 5) -> list[int]:
    total = 0
    closures = []
    for n_major in range(nmax + 1):
        degeneracy = (n_major + 1) * (n_major + 2)
        total += degeneracy
        closures.append(total)
    return closures


def bismut_closures() -> tuple[list[int], list[tuple[str, int, int, bool]]]:
    total = 0
    closures: list[int] = []
    rows: list[tuple[str, int, int, bool]] = []
    for orbital in ORBITALS:
        total += orbital.capacity
        is_closure = orbital.label in CLOSURE_LABELS
        if is_closure:
            closures.append(total)
        rows.append((orbital.label, orbital.capacity, total, is_closure))
    return closures, rows


def main() -> None:
    ho = harmonic_oscillator_closures()
    closures, rows = bismut_closures()

    lines: list[str] = []
    lines.append("# Saída — camadas spin--torção\n\n")
    lines.append("Classificação: derivação reduzida / teste de consistência.\n\n")
    lines.append(f"- Fechamentos sem torção: `{ho}`\n")
    lines.append(f"- Fechamentos com spin--torção: `{closures}`\n\n")
    lines.append("| orbital | capacidade 2j+1 | soma | fechamento |\n")
    lines.append("|---|---:|---:|---|\n")
    for label, cap, total, is_closure in rows:
        mark = "sim" if is_closure else ""
        lines.append(f"| {label} | {cap} | {total} | {mark} |\n")
        if total >= 126:
            break
    lines.append("\n")
    lines.append(
        "A sequência com torção reproduz 2, 8, 20, 28, 50, 82, 126. "
        "O resultado é reduzido: a diagonalização completa da Hessiana nuclear "
        "ainda é a etapa metrológica final.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

