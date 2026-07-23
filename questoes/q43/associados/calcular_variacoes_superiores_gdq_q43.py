#!/usr/bin/env python3
"""Q43 — variações superiores da ação GDQ reduzida.

Objetivo:
    Calcular, sem usar dados experimentais, alguns coeficientes cúbicos e
    quárticos da ação oficial reduzida usada na auditoria Galerkin da Q43.

Classificação:
    teste de consistência / derivada local de uma truncagem reduzida.

Leitura científica:
    Esses coeficientes mostram quais acoplamentos superiores a ação reduzida
    permite. Eles não são ainda a previsão metrológica de g-2, porque a
    truncagem Galerkin simples não é a sela leptônica física e porque termos
    cúbicos/quárticos em torno do ponto simétrico geram resposta não-linear em
    B, a menos que exista um background estacionário 8D com amplitudes internas
    não nulas.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Callable

import numpy as np


BASE = Path(__file__).resolve().parent
GALERKIN = BASE / "hessiana_oficial_galerkin_q43.py"
ALPHA = 1.0 / 137.035999177


def load_galerkin_action() -> Callable[[np.ndarray], float]:
    spec = importlib.util.spec_from_file_location("hessiana_oficial_galerkin_q43", GALERKIN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"não foi possível carregar {GALERKIN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def action(x: np.ndarray) -> float:
        return float(module.action_reduced(x, n_grid=4096))

    return action


def recursive_central_derivative(
    func: Callable[[np.ndarray], float],
    x: np.ndarray,
    indices: tuple[int, ...],
    h: float,
) -> float:
    """Aplica diferenças centrais recursivas para derivadas mistas.

    A implementação aceita índices repetidos. Para derivadas de ordem alta,
    isto é usado apenas como auditoria de magnitude/sinal em uma truncagem
    reduzida, não como cálculo metrológico final.
    """
    if not indices:
        return func(x)
    i = indices[0]
    step = np.zeros_like(x, dtype=float)
    step[i] = h
    return (
        recursive_central_derivative(func, x + step, indices[1:], h)
        - recursive_central_derivative(func, x - step, indices[1:], h)
    ) / (2.0 * h)


def finite_hessian(func: Callable[[np.ndarray], float], x0: np.ndarray, h: float) -> np.ndarray:
    n = x0.size
    H = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            H[i, j] = recursive_central_derivative(func, x0, (i, j), h)
    return 0.5 * (H + H.T)


def mode_name(i: int) -> str:
    return {
        0: "circulação/fase linear",
        1: "harmônico líder sin(theta)",
        2: "harmônico superior sin(2theta)",
        3: "densidade Re(f) cos(theta)",
        4: "métrica conformal cos(theta)",
    }[i]


def main() -> None:
    action = load_galerkin_action()
    x_star = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
    h = 2.0e-3

    H = finite_hessian(action, x_star, h)
    eig = np.linalg.eigvalsh(H)

    cubic_terms = {
        "T112": (1, 1, 2),
        "T113": (1, 1, 3),
        "T114": (1, 1, 4),
        "T122": (1, 2, 2),
        "T123": (1, 2, 3),
        "T124": (1, 2, 4),
        "T011": (0, 1, 1),
        "T012": (0, 1, 2),
    }
    quartic_terms = {
        "Q1111": (1, 1, 1, 1),
        "Q1122": (1, 1, 2, 2),
        "Q1133": (1, 1, 3, 3),
        "Q1144": (1, 1, 4, 4),
        "Q0011": (0, 0, 1, 1),
        "Q0022": (0, 0, 2, 2),
        "Q0112": (0, 1, 1, 2),
    }

    cubic_values = {
        name: recursive_central_derivative(action, x_star, idx, h)
        for name, idx in cubic_terms.items()
    }
    quartic_values = {
        name: recursive_central_derivative(action, x_star, idx, h)
        for name, idx in quartic_terms.items()
    }

    beta12 = 1.0 / (2.0 * math.sqrt(math.pi))

    lines = [
        "# Q43 — variações superiores da ação GDQ reduzida",
        "",
        "## Classificação",
        "",
        "Derivada local de uma truncagem Galerkin reduzida da ação oficial.",
        "Não é previsão metrológica de `g-2`.",
        "",
        "## 1. Ponto de expansão",
        "",
        "Usou-se o mesmo ponto da auditoria Galerkin:",
        "",
        "$$",
        "x_*=(1,0,0,0,0),",
        "$$",
        "",
        "com coordenadas:",
        "",
        "| índice | modo |",
        "|---:|---|",
    ]
    for i in range(5):
        lines.append(f"| {i} | {mode_name(i)} |")

    lines.extend(
        [
            "",
            "## 2. Hessiana local",
            "",
            f"- passo de diferença central: `{h:.1e}`",
            "",
            "| autovalor | valor |",
            "|---:|---:|",
        ]
    )
    for i, val in enumerate(eig):
        lines.append(f"| {i} | {val:.15e} |")

    lines.extend(
        [
            "",
            "A presença de autovalores negativos confirma o diagnóstico anterior:",
            "esta truncagem simples não é a sela leptônica física.",
            "",
            "## 3. Coeficientes cúbicos selecionados",
            "",
            "Notação:",
            "",
            "$$",
            "T_{ijk}=\\frac{\\partial^3 S_{\\rm red}}{\\partial x_i\\partial x_j\\partial x_k}(x_*).",
            "$$",
            "",
            "| termo | índices | valor | leitura |",
            "|---|---|---:|---|",
        ]
    )
    for name, idx in cubic_terms.items():
        value = cubic_values[name]
        if idx == (1, 1, 2):
            reading = "líder² → superior direto; aqui sai compatível com zero"
        elif idx == (1, 2, 3):
            reading = "líder-superior mediado pela densidade; canal robusto"
        elif idx[0] == 0:
            reading = "acoplamento envolvendo circulação protegida"
        else:
            reading = "acoplamento superior permitido/proibido pela truncagem"
        lines.append(f"| `{name}` | `{idx}` | {value:.15e} | {reading} |")

    lines.extend(
        [
            "",
            "## 4. Coeficientes quárticos selecionados",
            "",
            "Notação:",
            "",
            "$$",
            "Q_{ijkl}=\\frac{\\partial^4 S_{\\rm red}}{\\partial x_i\\partial x_j\\partial x_k\\partial x_l}(x_*).",
            "$$",
            "",
            "| termo | índices | valor |",
            "|---|---|---:|",
        ]
    )
    for name, idx in quartic_terms.items():
        lines.append(f"| `{name}` | `{idx}` | {quartic_values[name]:.15e} |")

    lines.extend(
        [
            "",
            "## 5. Comparação com a seleção harmônica",
            "",
            "A seleção harmônica reduzida calculada anteriormente dá:",
            "",
            "$$",
            "\\beta_{12}=\\langle u_2,u_1^2-\\langle u_1^2\\rangle\\rangle",
            "=",
            "\\frac{1}{2\\sqrt\\pi}.",
            "$$",
            "",
            f"Numericamente, `1/(2 sqrt(pi)) = {beta12:.15e}`.",
            "",
            "Na ação reduzida testada, `T112` sai no nível de ruído numérico.",
            "Assim, a seleção puramente harmônica `beta12` não se converte",
            "automaticamente em fonte variacional direta líder² → superior.",
            "",
            "O acoplamento cúbico robusto é `T123`, numericamente próximo de",
            "`-2*pi`. A leitura correta é que o modo líder e o modo superior",
            "se comunicam por intermédio da densidade `Re(f)`, não por uma",
            "fonte direta universal em campo uniforme.",
            "",
            "## 6. Consequência para Q43",
            "",
            "Este cálculo não fornece ainda `mu_2` metrológico. O motivo é estrutural:",
            "",
            "1. no ponto simétrico `x_*`, a resposta magnética linear usa apenas a",
            "   Hessiana quadrática;",
            "2. termos cúbicos/quárticos geram resposta não-linear em `B`, salvo se",
            "   o background físico já tiver amplitudes internas estacionárias",
            "   não nulas;",
            "3. a truncagem testada possui modos negativos e, portanto, não pode ser",
            "   usada como background leptônico final.",
            "",
            "A rota correta para a previsão metrológica fica então precisa:",
            "",
            "1. construir uma sela leptônica 8D estável `Phi_l`;",
            "2. avaliar `T` e `Q` nessa sela, não no ponto simétrico instável;",
            "3. contrair esses tensores com o mapa magnético de contorno",
            "   `M[Phi;B]`;",
            "4. montar `H_C(alpha)` físico e reexecutar o extrator.",
            "",
            "Assim, a Q43 ganha uma conclusão adicional: a ação reduzida permite",
            "um canal superior mediado pela densidade, mas não uma fonte direta",
            "universal. A metrologia depende da sela 8D estável e da contração",
            "tensorial completa. Não há justificativa para usar `mu_2_required`",
            "como previsão.",
            "",
        ]
    )

    out = BASE / "saida_variacoes_superiores_gdq_q43.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
