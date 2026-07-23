#!/usr/bin/env python3
"""Q39 — cálculo do complemento toroidal da Hessiana 8D no caso produto.

Este script não ajusta dados físicos. Ele avalia as fórmulas analíticas do
documento calculo_hessiana_8d_produto_q39.md:

    m_perp^2 = C_gamma * tau / R_max^2
    J = 0
    Schur = 0
    ind(H8) = ind(HB)
"""

from __future__ import annotations

from pathlib import Path


def torus_gap(radii: list[float], tau: float = 1.0, c_gamma: float = 1.0) -> float:
    if not radii:
        raise ValueError("radii vazio")
    if any(r <= 0 for r in radii):
        raise ValueError("todos os raios devem ser positivos")
    if tau <= 0:
        raise ValueError("tau deve ser positivo")
    if c_gamma <= 0:
        raise ValueError("C_gamma deve ser positivo")
    r_max = max(radii)
    return c_gamma * tau / (r_max * r_max)


def main() -> None:
    base = Path(__file__).resolve().parent

    radii_t5 = [1.0, 1.0, 1.0, 1.0, 1.0]
    tau = 1.0
    c_gamma = 1.0
    gap = torus_gap(radii_t5, tau=tau, c_gamma=c_gamma)

    j_norm = 0.0
    schur_norm = 0.0

    # Exemplo de índice: o valor de ind(HB) é simbólico; como H_perp é positivo
    # e J=0, o índice 8D é igual ao índice 3D para qualquer ind(HB).
    example_indices = [0, 1, 2, 3]

    lines = [
        "# Q39 — saída do cálculo da Hessiana 8D produto",
        "",
        "## Entrada normalizada",
        "",
        f"- raios de `T^5`: `{radii_t5}`",
        f"- `tau = {tau}`",
        f"- `C_gamma = {c_gamma}`",
        "",
        "## Resultado analítico avaliado",
        "",
        f"- `m_perp^2 = C_gamma * tau / R_max^2 = {gap:.12f}`",
        f"- `||J|| = {j_norm:.12f}`",
        f"- `||J H_perp^-1 J^dagger|| = {schur_norm:.12f}`",
        "",
        "## Índice crítico",
        "",
        "| `ind(H_B)` | `ind(H_perp)` | `ind(H_8)` |",
        "|---:|---:|---:|",
    ]

    for ind_b in example_indices:
        ind_perp = 0
        ind_8 = ind_b + ind_perp
        lines.append(f"| {ind_b} | {ind_perp} | {ind_8} |")

    lines.extend(
        [
            "",
            "## Veredito",
            "",
            "No background produto normalizado, o complemento toroidal é coercivo,",
            "o bloco misto é nulo e o índice crítico 8D coincide com o índice do",
            "setor 3D curvo.",
            "",
            "$$",
            "\\operatorname{ind}^{-}(H_8)",
            "=",
            "\\operatorname{ind}^{-}(H_B).",
            "$$",
            "",
        ]
    )

    report = base / "saida_hessiana_8d_produto_q39.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
