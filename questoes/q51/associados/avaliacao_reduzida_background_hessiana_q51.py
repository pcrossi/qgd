#!/usr/bin/env python3
"""Q51 — avaliação reduzida dos pontos 1 a 5.

Este script constrói um background nuclear reduzido e blocos de Hessiana
alfa--núcleo sem usar a meia-vida experimental como alvo.

Classificação:
    - teste de consistência / avaliação reduzida;
    - não é previsão cega metrológica;
    - não substitui a Hessiana completa da ação oficial.

Objetivo:
    executar os cinco elos operacionais:
      1. background nuclear reduzido Phi_N;
      2. blocos K_II, K_Ib, K_bb;
      3. K_partial, P_alpha, S_alpha^GDQ;
      4. nu_GDQ e g_rr^eff reduzidos;
      5. comparação contra meia-vida experimental do dataset diagnóstico.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from riesz_projector_utils_q51 import Window, projection_weight, schur_boundary, spectral_projector
from derivar_camadas_hessiana_reduzida_q51 import bismut_spin_torsion_closures


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_avaliacao_reduzida_background_hessiana_q51.md"
NPZ_DIR = HERE / "npz_backgrounds_reduzidos"

J0 = 1.712091781054
J1 = 1.341454657186
J2 = 1.063840998206
R0_FM = 1.20


def load_benchmark():
    spec = importlib.util.spec_from_file_location("q51_benchmark", BENCH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def nearest_magic_distance(z_d: int, n_d: int) -> tuple[int, int, int]:
    closures = bismut_spin_torsion_closures()
    dz = min(abs(z_d - m) for m in closures)
    dn = min(abs(n_d - m) for m in closures)
    return dz, dn, dz * dz + dn * dn


def exact_closure_count(z_d: int, n_d: int) -> int:
    closures = set(bismut_spin_torsion_closures())
    return int(z_d in closures) + int(n_d in closures)


def impedance_q40_base(x: float) -> float:
    return (
        J0 * J0 * x * x / (1.0 + x)
        + J1 * J1 * x * x / (1.0 + x) ** 2
        + J2 * J2 * x ** 3 / (1.0 + x) ** 2
    )


@dataclass(frozen=True)
class ReducedBackground:
    phi_n: np.ndarray
    phi_alpha: np.ndarray
    K_II: np.ndarray
    K_Ib: np.ndarray
    K_bb: np.ndarray
    P_daughter: np.ndarray
    window: Window
    g_factor: float
    nu_gdq: float
    W_rad_gdq: float
    chi_curv: float
    x_barrier: float
    delta_touch: float
    shell_norm: float
    variant: str
    lambda_alpha: float


def build_reduced_background(q, case, variant: str) -> ReducedBackground:
    """Construct a reduced GDQ surface Hessian from channel geometry only."""
    a_p = case.A_parent
    z_p = case.Z_parent
    a_d = a_p - 4
    z_d = z_p - 2
    n_d = a_d - z_d
    dz, dn, d_shell = nearest_magic_distance(z_d, n_d)

    radius_touch = q.nuclear_radius_fm(a_p, R0_FM)
    radius_parent = R0_FM * a_p ** (1.0 / 3.0)
    x_barrier = q.coulomb_mev_fm(z_p) / (radius_touch * case.q_alpha_mev) - 1.0
    delta_touch = (radius_touch - radius_parent) / radius_parent
    chi_curv = delta_touch * delta_touch / max(x_barrier, 1.0e-12)
    if variant == "mismatch":
        # Variante historica desta rodada: aumenta com distancia a camada.
        # Ela sera preservada porque falha de modo informativo.
        shell_norm = d_shell / (d_shell + a_d ** (2.0 / 3.0))
    elif variant in ("closure", "closure_mobility"):
        # Variante fisicamente corrigida: fechamento de camada aumenta a
        # rigidez espectral do filho, como esperado para Pb-208 em Po-212.
        shell_norm = a_d ** (2.0 / 3.0) / (d_shell + a_d ** (2.0 / 3.0))
    else:
        raise ValueError(f"unknown variant: {variant}")

    # Background trace in a three-channel surface basis:
    # e0: compact alpha cluster; e1: daughter surface; e2: quadrupolar/torsion.
    phi_n = np.array(
        [
            math.sqrt(max(chi_curv, 0.0)),
            math.sqrt(max(shell_norm, 0.0)),
            math.sqrt(max(delta_touch * x_barrier, 0.0)),
        ],
        dtype=float,
    )
    norm = np.linalg.norm(phi_n)
    if norm > 0.0:
        phi_n = phi_n / norm

    phi_alpha = np.array([1.0, 0.0, 0.0], dtype=float)

    # Interior stiffness: bulk restoring modes. Positive by construction.
    k_vol = 1.0 + x_barrier
    k_tors = 1.0 + 4.0 * chi_curv / q.ALPHA
    k_shell = 1.0 + shell_norm
    K_II = np.diag([k_vol, k_tors, k_shell])

    # Boundary stiffness: surface Hessian reduced from curvature, torsion,
    # shell mismatch and Coulomb barrier. No experimental half-life enters.
    i_sigma = impedance_q40_base(chi_curv)
    e_scale = 4.0 * i_sigma / q.ALPHA
    K_bb = np.diag(
        [
            max(e_scale, 1.0e-9),
            1.0 + shell_norm,
            1.0 + x_barrier,
        ]
    )

    # Cross block: Schur/DtN coupling. The coefficients are fixed by the Q40
    # normalized surface currents and by the channel geometry.
    coupling_scale = math.sqrt(max(e_scale, 0.0) + 1.0e-12)
    K_Ib = np.array(
        [
            [J0 * chi_curv, J1 * chi_curv * math.sqrt(shell_norm + 1.0e-12), 0.0],
            [J1 * chi_curv, 0.0, J2 * chi_curv * math.sqrt(x_barrier + 1.0e-12)],
            [0.0, coupling_scale * shell_norm / (1.0 + x_barrier), coupling_scale * delta_touch],
        ],
        dtype=float,
    )

    # Daughter projector as the normalized daughter-surface direction e1/e2.
    daughter_vec = np.array([0.0, math.sqrt(shell_norm), math.sqrt(max(x_barrier, 0.0))])
    d_norm = np.linalg.norm(daughter_vec)
    if d_norm > 0.0:
        daughter_vec = daughter_vec / d_norm
        P_daughter = np.outer(daughter_vec, daughter_vec)
    else:
        P_daughter = np.zeros((3, 3))

    # Window: select the alpha charge/circulation band, not the lightest band.
    # Operationally, in this reduced basis, this is the eigenvector with
    # largest overlap with the primitive alpha vector after removal of the
    # daughter subspace. This does not use half-life data.
    K_partial = schur_boundary(K_II, K_Ib, K_bb)
    eigvals, eigvecs = np.linalg.eigh(K_partial)
    primitive_alpha = np.array([1.0, 0.0, 0.0], dtype=float)
    weights = []
    for idx in range(eigvecs.shape[1]):
        v = eigvecs[:, idx]
        v_phys = (np.eye(3) - P_daughter) @ v
        weights.append(abs(float(v_phys @ primitive_alpha)))
    alpha_idx = int(np.argmax(weights))
    target = float(eigvals[alpha_idx])
    gaps = [abs(float(val - target)) for j, val in enumerate(eigvals) if j != alpha_idx]
    gap = min(gaps) if gaps else 1.0
    low = float(target - 0.25 * max(gap, 1.0e-6))
    high = float(target + 0.25 * max(gap, 1.0e-6))
    window = Window(center=0.5 * (low + high), radius=0.5 * abs(high - low))

    # Reduced internal normal frequency and metric correction.
    # The frequency must use the selected alpha band, not the lightest
    # abstract surface eigenvalue.
    beta = math.sqrt(2.0 * case.q_alpha_mev / q.reduced_mass_mev(a_p))
    nu_bounce = q.C_FM_S * beta / (2.0 * radius_touch)
    lambda_alpha = max(target, 0.0)
    if variant == "closure_mobility":
        n_closed = exact_closure_count(z_d, n_d)
        mobility_power = 0.5 * max(1, n_closed)
    else:
        mobility_power = 0.5
    nu_gdq = nu_bounce * (1.0 + lambda_alpha) ** mobility_power

    # Exponential metric from the reduced Hessian symbol: g=exp(-eta V/Q).
    # eta is not fitted; it is the positive surface response scale.
    eta = lambda_alpha * q.ALPHA / 4.0
    g_factor = eta
    W_rad_gdq = q.action_w(case, geometric=False) - eta * q.action_w(case, geometric=False)

    return ReducedBackground(
        phi_n=phi_n,
        phi_alpha=phi_alpha,
        K_II=K_II,
        K_Ib=K_Ib,
        K_bb=K_bb,
        P_daughter=P_daughter,
        window=window,
        g_factor=g_factor,
        nu_gdq=nu_gdq,
        W_rad_gdq=W_rad_gdq,
        chi_curv=chi_curv,
        x_barrier=x_barrier,
        delta_touch=delta_touch,
        shell_norm=shell_norm,
        variant=variant,
        lambda_alpha=lambda_alpha,
    )


def eval_case(q, case, variant: str):
    bg = build_reduced_background(q, case, variant)
    K_partial = schur_boundary(bg.K_II, bg.K_Ib, bg.K_bb)
    P_alpha = spectral_projector(K_partial, bg.window)
    P_perp = P_alpha @ (np.eye(3) - bg.P_daughter)
    projected = P_perp @ bg.phi_alpha
    E_partial = float(projected.T @ K_partial @ projected)
    S_alpha = math.exp(-max(E_partial, 0.0))
    Gamma = bg.nu_gdq * S_alpha * math.exp(-bg.W_rad_gdq)
    T_half = math.log(2.0) / Gamma if Gamma > 0.0 else math.inf

    eigvals = np.linalg.eigvalsh(K_partial)
    weight = projection_weight(P_perp, bg.phi_alpha)

    return {
        "bg": bg,
        "K_partial": K_partial,
        "eigvals": eigvals,
        "weight": weight,
        "E_partial": E_partial,
        "S_alpha": S_alpha,
        "Gamma": Gamma,
        "T_half": T_half,
        "logT": math.log10(T_half),
        "logT_exp": math.log10(case.half_life_s),
        "residual": math.log10(T_half) - math.log10(case.half_life_s),
    }


def save_npz(case_name: str, result) -> None:
    NPZ_DIR.mkdir(exist_ok=True)
    bg = result["bg"]
    path = NPZ_DIR / f"{case_name.replace('-', '_')}_{bg.variant}.npz"
    np.savez(
        path,
        K_II=bg.K_II,
        K_Ib=bg.K_Ib,
        K_bb=bg.K_bb,
        phi_alpha=bg.phi_alpha,
        P_daughter=bg.P_daughter,
        alpha_window_min=np.array([bg.window.center - bg.window.radius]),
        alpha_window_max=np.array([bg.window.center + bg.window.radius]),
        nu_gdq=np.array([bg.nu_gdq]),
        W_rad_gdq=np.array([bg.W_rad_gdq]),
    )


def main() -> None:
    q = load_benchmark()
    all_results = {}
    for variant in ("mismatch", "closure", "closure_mobility"):
        results = []
        for case in q.CASES:
            res = eval_case(q, case, variant)
            save_npz(case.name, res)
            results.append((case, res))
        all_results[variant] = results

    lines: list[str] = []
    lines.append("# Saída — avaliação reduzida background/Hessiana Q51\n\n")
    lines.append("Classificação: teste de consistência / avaliação reduzida.\n\n")
    lines.append("Esta execução implementa os pontos 1 a 5 em versão reduzida GDQ. ")
    lines.append("Não usa meia-vida experimental para construir os operadores. ")
    lines.append("Ainda não é Hessiana completa da ação oficial.\n\n")
    lines.append("Os fechamentos de camada usados por `closure` agora são gerados por ")
    lines.append("`derivar_camadas_hessiana_reduzida_q51.py`, a partir do espectro angular ")
    lines.append("reduzido com cisão spin--torção, e não por uma lista manual no script.\n\n")

    lines.append("## Definições reduzidas usadas\n\n")
    lines.append("Background de superfície:\n\n")
    lines.append("$$\n")
    lines.append("\\Phi_N=(\\sqrt{\\chi_{curv}},\\sqrt{s_{shell}},\\sqrt{\\delta_{touch}x_{barrier}})/\\|\\cdot\\|.\n")
    lines.append("$$\n\n")
    lines.append("Hessiana de superfície:\n\n")
    lines.append("$$\n")
    lines.append("K_\\partial^{phys}=K_{\\partial\\partial}-K_{\\partial I}K_{II}^{-1}K_{I\\partial}.\n")
    lines.append("$$\n\n")
    lines.append("Taxa:\n\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{GDQ}=\\nu_{GDQ}\\exp(-E_\\partial^{GDQ})\\exp(-W_{rad}^{GDQ}).\n")
    lines.append("$$\n\n")

    rms_gamow = 0.303358
    summary = {}
    for variant, results in all_results.items():
        rms = math.sqrt(sum(res["residual"] ** 2 for _, res in results) / len(results))
        summary[variant] = (rms, 1.0 - rms / rms_gamow)

        lines.append(f"## Comparação — variante `{variant}`\n\n")
        lines.append(
        "| Núcleo | log10 T_exp | log10 T_GDQ_red | resíduo | "
        "chi_curv | shell | lambda_alpha | peso P_perp | E_partial | nu_GDQ |\n"
    )
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n")
        for case, res in results:
            bg = res["bg"]
            lines.append(
                f"| {case.name} | {res['logT_exp']:.6f} | {res['logT']:.6f} | "
                f"{res['residual']:.6f} | {bg.chi_curv:.6f} | {bg.shell_norm:.6f} | "
                f"{bg.lambda_alpha:.6f} | {res['weight']:.6f} | {res['E_partial']:.6f} | "
                f"{bg.nu_gdq:.6e} |\n"
            )

        lines.append("\n")
        lines.append(f"- RMS contra experimento = `{rms:.6f}` décadas\n")
        lines.append(f"- RMS de referência Gamow + nu_int = `{rms_gamow:.6f}` décadas\n")
        lines.append(f"- melhoria relativa = `{100.0 * summary[variant][1]:.3f}%`\n\n")

    lines.append("## Arquivos NPZ gerados\n\n")
    for variant, results in all_results.items():
        for case, _ in results:
            path = NPZ_DIR / f"{case.name.replace('-', '_')}_{variant}.npz"
            lines.append(f"- `{path.relative_to(HERE)}`\n")

    lines.append("\n## Veredito\n\n")
    best_variant = min(summary, key=lambda item: summary[item][0])
    best_rms, best_improvement = summary[best_variant]
    lines.append(
        f"A melhor variante reduzida foi `{best_variant}`, com RMS "
        f"`{best_rms:.6f}` décadas e melhoria `{100.0 * best_improvement:.3f}%` "
        "contra Gamow com `nu_int`.\n\n"
    )
    lines.append(
        "A variante `mismatch` fica preservada como rota falha: ela atribui "
        "rigidez pequena ao fechamento Pb-208 de Po-212 e por isso erra "
        "fisicamente o canal.\n\n"
    )
    lines.append(
        "A variante `closure` corrige esse sinal físico ao aumentar a rigidez "
        "quando o filho está próximo de camada fechada. A variante "
        "`closure_mobility` adiciona a regra de mobilidade de determinante "
        "para filho exatamente duplamente fechado. Mesmo quando melhora o RMS, "
        "continua sendo uma redução espectral angular, não a Hessiana completa "
        "derivada da ação oficial.\n"
    )
    lines.append(
        "O ponto técnico restante é calcular os blocos reais da Hessiana nuclear "
        "da ação oficial, em vez de usar a matriz reduzida acima.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
