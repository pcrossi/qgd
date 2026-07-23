#!/usr/bin/env python3
"""Q43 — contração do canal superior mediado pela densidade.

Objetivo:
    Implementar a consequência do cálculo de variações superiores:

        T123 ~= -2*pi

    O termo direto líder² -> superior é nulo na truncagem reduzida; o canal
    superior robusto é mediado pela densidade Re(f). Se o background leptônico
    físico tiver uma amplitude estacionária eta_l no modo de densidade, a
    Hessiana efetiva recebe:

        (H_eff)12 = (H0)12 + eta_l T123.

    Este script calcula a resposta resultante sem usar valores experimentais.

Classificação:
    avaliação condicional de canal derivado. Com eta_l=0, é teste de
    consistência dos backgrounds efetivos atuais; com eta_l vindo de uma sela
    8D, torna-se avaliação direta da quantidade derivada.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
ALPHA = 1.0 / 137.035999177
T123_REDUCED = -6.283174869281538


def load_block(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, dict[str, str | float]]:
    data = np.load(path, allow_pickle=True)
    H = np.asarray(data["H"], dtype=float)
    c = np.asarray(data["c"], dtype=float).reshape(-1)
    m = np.asarray(data["m_perp"], dtype=float).reshape(-1)
    gamma0 = float(np.asarray(data["gamma0"]).reshape(-1)[0]) if "gamma0" in data else 1.0
    meta: dict[str, str | float] = {}
    if "ratio_q39" in data:
        meta["ratio_q39"] = float(np.asarray(data["ratio_q39"]).reshape(-1)[0])
    if "role_q39" in data:
        meta["role_q39"] = str(np.asarray(data["role_q39"]).reshape(-1)[0])
    return H, c, m, gamma0, meta


def anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray, gamma0: float) -> float:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    if np.min(vals) <= 0.0:
        raise ValueError(f"Hessiana não positiva: min eig = {np.min(vals):.6e}")
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (gamma0 * (c @ (Hinv @ c))))


def apply_density_channel(H: np.ndarray, eta_density: float, t123: float) -> np.ndarray:
    """Acrescenta a correção mediada pela densidade ao bloco líder-superior.

    Convenção do bloco efetivo:
        índice 0: circulação protegida;
        índice 1: harmônico líder;
        índice 2: harmônico superior.

    Pela expansão:
        S = S0 + 1/2 H_ij dx_i dx_j + 1/6 T_ijk dx_i dx_j dx_k + ...

    se x3 = eta é uma amplitude estacionária do background, então:
        d²S/dx1dx2 = H12 + T123 eta.

    Como o bloco reduzido de três modos não contém explicitamente x3, essa
    contribuição é projetada em H[1,2].
    """
    H_eff = np.array(H, dtype=float, copy=True)
    if H_eff.shape[0] < 3:
        raise ValueError("o bloco precisa conter circulação, líder e superior")
    delta = eta_density * t123
    H_eff[1, 2] += delta
    H_eff[2, 1] += delta
    return 0.5 * (H_eff + H_eff.T)


def default_blocks() -> list[Path]:
    return [
        BASE / "background_leptonico_estavel_e_q43.npz",
        BASE / "background_leptonico_estavel_mu_q43.npz",
        BASE / "background_leptonico_estavel_tau_q43.npz",
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--eta-density",
        type=float,
        default=0.0,
        help="amplitude estacionária do modo de densidade Re(f) no background",
    )
    parser.add_argument(
        "--t123",
        type=float,
        default=T123_REDUCED,
        help="coeficiente cúbico reduzido T123",
    )
    args = parser.parse_args()

    rows = []
    for path in default_blocks():
        H, c, m, gamma0, meta = load_block(path)
        a0 = anomaly(H, c, m, gamma0)
        H_eff = apply_density_channel(H, args.eta_density, args.t123)
        eig_min = float(np.min(np.linalg.eigvalsh(H_eff)))
        a_eff = anomaly(H_eff, c, m, gamma0)
        rows.append(
            {
                "file": path.name,
                "role": meta.get("role_q39", ""),
                "ratio": meta.get("ratio_q39", float("nan")),
                "a0": a0,
                "a_eff": a_eff,
                "delta_a": a_eff - a0,
                "eig_min": eig_min,
            }
        )

    lines = [
        "# Q43 — contração do canal superior mediado pela densidade",
        "",
        "## Classificação",
        "",
        "Avaliação condicional de um canal derivado da ação reduzida. Não usa",
        "valores experimentais de `g-2`.",
        "",
        "## 1. Entrada",
        "",
        f"- `eta_density = {args.eta_density:.15e}`",
        f"- `T123 = {args.t123:.15e}`",
        f"- `alpha/(2*pi) = {ALPHA/(2.0*math.pi):.15e}`",
        "",
        "O canal aplicado é:",
        "",
        "$$",
        "\\Delta H_{12}",
        "=",
        "\\eta_\\ell T_{123}.",
        "$$",
        "",
        "Aqui \\(\\eta_\\ell\\) deve vir de uma sela admissível. A sela angular",
        "reduzida normalizada foi calculada separadamente e fornece",
        "\\(\\eta_\\ell=0\\). Um valor não nulo exigiria o background 8D",
        "não homogêneo, warped ou misto.",
        "",
        "## 2. Resultados",
        "",
        "| bloco | papel Q39 | M_l/M_e | eig_min | a0 | a_eff | delta_a |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['file']}` | {row['role']} | {row['ratio']:.15e} | "
            f"{row['eig_min']:.15e} | {row['a0']:.15e} | "
            f"{row['a_eff']:.15e} | {row['delta_a']:.15e} |"
        )

    lines.extend(
        [
            "",
            "## 3. Leitura",
            "",
            "Para o valor informado acima, a tabela mostra diretamente a resposta",
            "do canal mediado pela densidade. A execução canônica usa",
            "\\(\\eta_\\ell=0\\), valor da sela angular reduzida normalizada; nesse",
            "caso, a contração não altera a resposta líder.",
            "",
            "Logo, o próximo dado físico necessário para a metrologia não é",
            "`mu2_required`; é \\(\\eta_\\ell\\) ou, mais geralmente, o perfil",
            "estacionário completo de \\(\\operatorname{Re}f\\) na sela leptônica",
            "8D. Uma vez fornecido esse background, este mesmo operador calcula",
            "a correção sem ajuste experimental.",
            "",
        ]
    )

    out = BASE / "saida_contracao_canal_densidade_q43.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
