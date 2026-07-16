#!/usr/bin/env python3
r"""
GDQ — Solver auditado da gravidade (Q38)

Este script não substitui a derivação variacional. Ele audita a aritmética do
solver V2 separando:

1. Fano bulk: chi_Fano = 3*sqrt(2)/5;
2. planificação: J_flat;
3. condição de contorno;
4. imposição fenomenológica do meio-instantão S_inst = 1/(2 alpha).

Resultado esperado desta versão:

- com a EDO reduzida de vácuo f'' + 2 cot(chi) f' = 0, o perfil regular é
  constante;
- portanto, esta versão testa normalizações globais, não uma dinâmica
  preditiva completa do dilaton;
- o fator 0.4791 do V2 é auditado como chi_Fano/sqrt(pi), isto é, mistura
  Fano e planificação.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_bvp


@dataclass(frozen=True)
class Constants:
    pi: float = math.pi
    G: float = 6.6743e-11
    Mp: float = 1.672621e-27
    hbar: float = 1.05457e-34
    c: float = 2.99792458e8

    @property
    def alpha_geom(self) -> float:
        return (9.0 / (8.0 * self.pi**4)) * ((self.pi**5 / 1920.0) ** 0.25)

    @property
    def S_inst(self) -> float:
        return 1.0 / (2.0 * self.alpha_geom)

    @property
    def chi_fano_bulk(self) -> float:
        return 3.0 * math.sqrt(2.0) / 5.0

    @property
    def J_sqrt_pi(self) -> float:
        return math.sqrt(self.pi)

    @property
    def pi1_obs(self) -> float:
        return (self.G * self.Mp**2) / (self.hbar * self.c)


@dataclass(frozen=True)
class Scenario:
    name: str
    boundary: str
    chi_fano: float
    J_flat: float
    classification: str


def solve_constant_profile(constants: Constants, boundary: str, n: int = 800) -> tuple[np.ndarray, np.ndarray, str]:
    """Resolve ou fixa o perfil reduzido.

    A EDO de vácuo é:

        f'' + 2 cot(chi) f' = 0.

    No setor regular, a solução física é constante. Para Neumann puro há modo
    zero não fixado; portanto fixamos a média em S_inst como normalização
    térmica para comparar com Dirichlet.
    """

    eps = 1e-4
    chi = np.linspace(eps, constants.pi - eps, n)

    if boundary == "neumann_regular_mean_fixed":
        f = np.full_like(chi, constants.S_inst)
        return chi, f, "Neumann regular possui modo zero; média fixada em S_inst para comparação."

    if boundary == "robin_impedance_balanced":
        f = np.full_like(chi, constants.S_inst)
        return chi, f, "Robin balanceado com fonte j=lambda*S_inst; perfil regular constante."

    if boundary != "dirichlet_fixed_instanton":
        raise ValueError(f"boundary desconhecido: {boundary}")

    def odes(x: np.ndarray, u: np.ndarray) -> np.ndarray:
        df = u[1]
        cot = 1.0 / np.tan(x)
        d2f = -2.0 * cot * df
        return np.vstack((df, d2f))

    def bc(ua: np.ndarray, ub: np.ndarray) -> np.ndarray:
        return np.array([ua[0] - constants.S_inst, ub[0] - constants.S_inst])

    u_init = np.zeros((2, n))
    u_init[0] = constants.S_inst
    result = solve_bvp(odes, bc, chi, u_init, tol=1e-7, max_nodes=10000)

    if not result.success:
        raise RuntimeError(result.message)

    return chi, result.sol(chi)[0], "Dirichlet instantônico resolvido por BVP."


def volume_eff_1d(chi: np.ndarray, f: np.ndarray) -> float:
    """Volume radial normalizado por int_0^pi sin^2(chi)dchi = pi/2."""

    raw = np.trapezoid(np.exp(-f) * np.sin(chi) ** 2, chi)
    return raw / (math.pi / 2.0)


def evaluate_scenario(constants: Constants, scenario: Scenario) -> dict[str, float | str]:
    chi, f, note = solve_constant_profile(constants, scenario.boundary)
    v_eff = volume_eff_1d(chi, f)
    pi1_bulk = (
        constants.alpha_geom**4
        * (1.0 + constants.alpha_geom)
        * v_eff
        / scenario.chi_fano
    )
    pi1_obs = pi1_bulk / scenario.J_flat
    error = abs(pi1_obs - constants.pi1_obs) / constants.pi1_obs * 100.0
    return {
        "name": scenario.name,
        "boundary": scenario.boundary,
        "chi_fano": scenario.chi_fano,
        "J_flat": scenario.J_flat,
        "S_inst": constants.S_inst,
        "V_eff": v_eff,
        "Pi_bulk": pi1_bulk,
        "Pi_obs": pi1_obs,
        "Pi_exp": constants.pi1_obs,
        "error": error,
        "classification": scenario.classification,
        "note": note,
    }


def run() -> list[dict[str, float | str]]:
    c = Constants()
    chi_script = c.chi_fano_bulk / c.J_sqrt_pi

    scenarios = [
        Scenario(
            "A_dirichlet_bulk_sem_planificacao",
            "dirichlet_fixed_instanton",
            c.chi_fano_bulk,
            1.0,
            "teste: Fano bulk, sem leitura plana",
        ),
        Scenario(
            "B_dirichlet_bulk_com_sqrtpi",
            "dirichlet_fixed_instanton",
            c.chi_fano_bulk,
            c.J_sqrt_pi,
            "hipotese: Fano bulk + planificacao separada sqrt(pi)",
        ),
        Scenario(
            "C_v2_misturado_reproduzido",
            "dirichlet_fixed_instanton",
            chi_script,
            c.J_sqrt_pi,
            "auditoria: chi=Fano/sqrt(pi) e depois divide por sqrt(pi)",
        ),
        Scenario(
            "D_script_sem_planificacao_final",
            "dirichlet_fixed_instanton",
            chi_script,
            1.0,
            "controle: Fano ja planificado sem divisao final",
        ),
        Scenario(
            "E_neumann_regular_media_fixa",
            "neumann_regular_mean_fixed",
            c.chi_fano_bulk,
            1.0,
            "teste: Neumann regular reduz ao modo constante",
        ),
        Scenario(
            "F_robin_balanceado_media_fixa",
            "robin_impedance_balanced",
            c.chi_fano_bulk,
            1.0,
            "teste: Robin balanceado reduz ao modo constante",
        ),
    ]

    return [evaluate_scenario(c, scenario) for scenario in scenarios]


def write_report(rows: list[dict[str, float | str]]) -> str:
    c = Constants()
    out_path = os.path.join(os.path.dirname(__file__), "saida_gravity_q38_auditado.md")

    def fmt(x: float | str) -> str:
        if isinstance(x, str):
            return x
        return f"{x:.8e}"

    table = [
        "| Cenário | Contorno | chi_Fano | J_flat | V_eff | Pi_obs | Erro | Classificação |",
        "| :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |",
    ]
    for row in rows:
        table.append(
            "| {name} | {boundary} | {chi} | {j} | {v} | {piobs} | {err:.4f}% | {cls} |".format(
                name=row["name"],
                boundary=row["boundary"],
                chi=fmt(row["chi_fano"]),
                j=fmt(row["J_flat"]),
                v=fmt(row["V_eff"]),
                piobs=fmt(row["Pi_obs"]),
                err=float(row["error"]),
                cls=row["classification"],
            )
        )

    notes = "\n".join(
        f"- `{row['name']}`: {row['note']}" for row in rows
    )

    content = f"""# Saída do solver auditado Q38

## 1. Constantes usadas

\\[
\\alpha_{{\\rm geom}}={c.alpha_geom:.12f},
\\qquad
S_{{\\rm inst}}=\\frac1{{2\\alpha}}={c.S_inst:.8f}.
\\]

\\[
\\chi_{{\\rm Fano}}^{{\\rm bulk}}
=
\\frac{{3\\sqrt2}}{{5}}
={c.chi_fano_bulk:.12f},
\\qquad
\\sqrt\\pi={c.J_sqrt_pi:.12f}.
\\]

\\[
\\frac{{\\chi_{{\\rm Fano}}^{{\\rm bulk}}}}{{\\sqrt\\pi}}
={c.chi_fano_bulk / c.J_sqrt_pi:.12f}.
\\]

Valor observado usado apenas como comparação final:

\\[
\\Pi_1^{{\\rm obs}}
=
\\frac{{GM_p^2}}{{\\hbar c}}
={c.pi1_obs:.8e}.
\\]

## 2. Tabela de auditoria

{chr(10).join(table)}

## 3. Notas de contorno

{notes}

## 4. Conclusões

1. Com a EDO reduzida de vácuo, todos os contornos regulares sem fonte efetiva
   colapsam no perfil constante. Portanto, este solver ainda não é uma prova
   dinâmica do dilaton.

2. O cenário `A_dirichlet_bulk_sem_planificacao` já fica próximo do valor
   observado, com erro da ordem de \\(10^{{-1}}\\%\\). Isso corresponde ao uso
   de \\(\\chi_{{\\rm Fano}}^{{\\rm bulk}}\\) sem fator plano separado.

3. O cenário `B_dirichlet_bulk_com_sqrtpi` mostra que aplicar
   \\(J_{{\\rm flat}}=\\sqrt\\pi\\) como fator independente desloca fortemente
   o resultado. Logo, \\(\\sqrt\\pi\\) não pode ser aplicado de forma ingênua
   após usar o Fano bulk.

4. O cenário `C_v2_misturado_reproduzido` confirma a auditoria: usar
   \\(\\chi_{{\\rm Fano}}/\\sqrt\\pi\\) e depois dividir por \\(\\sqrt\\pi\\)
   cancela a planificação e retorna ao cenário bulk.

5. Para fechar Q38, falta substituir o modo fenomenológico
   \\(S_{{\\rm inst}}=1/(2\\alpha)\\) por uma sela derivada da ação reduzida
   euclidiana da GDQ e calcular \\(J_{{\\rm flat}}\\) pela norma do modo
   gravitacional ou por média ponderada.
"""

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(content)
    return out_path


if __name__ == "__main__":
    rows_out = run()
    for item in rows_out:
        print(
            f"{item['name']:34s} Pi_obs={item['Pi_obs']:.8e} "
            f"erro={item['error']:.4f}%"
        )
    path = write_report(rows_out)
    print(f"Relatório salvo em: {path}")
