#!/usr/bin/env python3
"""Contagem de componentes versus multiplicidade geracional na Q28."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Multiplet:
    name: str
    dim_color: int
    dim_weak: int
    six_y: int
    color_label: str
    weak_label: str

    @property
    def dimension(self) -> int:
        return self.dim_color * self.dim_weak


MULTIPLETS = (
    Multiplet("Q_L", 3, 2, 1, "3", "2"),
    Multiplet("u_R^c", 3, 1, -4, r"\bar 3", "1"),
    Multiplet("d_R^c", 3, 1, 2, r"\bar 3", "1"),
    Multiplet("L_L", 1, 2, -3, "1", "2"),
    Multiplet("e_R^c", 1, 1, 6, "1", "1"),
)


def render(local_index: int = 1, generations: int = 3) -> str:
    lines = [
        "# Q28 — Elevação do índice às representações",
        "",
        f"Índice geométrico local: ${local_index}$.",
        "",
        "| multiplet | $\\dim SU(3)$ | $\\dim SU(2)$ | $6Y$ | índice ordinário local | classe equivarante |",
        "|:---|---:|---:|---:|---:|:---|",
    ]
    total = 0
    for multiplet in MULTIPLETS:
        ordinary = local_index * multiplet.dimension
        total += ordinary
        representation = (
            f"({multiplet.color_label},{multiplet.weak_label})"
            f"_{{{multiplet.six_y}/6}}"
        )
        lines.append(
            f"| {multiplet.name} | {multiplet.dim_color} | {multiplet.dim_weak} | "
            f"{multiplet.six_y} | {ordinary} | ${representation}$ |"
        )

    lines += [
        "",
        f"Total de componentes de Weyl por geração: ${total}$.",
        f"Total para {generations} estômatos equivalentes: ${generations * total}$.",
        "",
        "A multiplicidade geracional é o fator externo; as dimensões 2, 3 e 6",
        "são dimensões das representações, não números adicionais de gerações.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_elevacao_representacoes.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
