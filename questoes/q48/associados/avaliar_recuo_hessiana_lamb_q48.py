#!/usr/bin/env python3
"""Q48 — recuo fino, Hessiana magnética residual e Lamb por deltaD_near.

Classificações:
- recuo cinemático fino: avaliação direta reduzida;
- Hessiana magnética superior requerida: diagnóstico de resíduo, não previsão;
- deltaD_near requerido para Lamb: diagnóstico de escala do operador, não
  previsão enquanto K_p não for avaliado diretamente da Q40.
"""

from __future__ import annotations

from pathlib import Path

from scipy import constants as C
from scipy.optimize import brentq


OUT = Path(__file__).with_name("saida_recuo_hessiana_lamb_q48.md")

alpha = C.alpha
c = C.c
h = C.h
hbar = C.hbar
e = C.e
m_e = C.m_e
m_p = C.m_p
mu_ep = m_e * m_p / (m_e + m_p)

nu_obs = 1_420_405_751.768
nu_F = 1_418_840_090.665555
a_e = alpha / (2.0 * C.pi)
r_p_fm = 0.84077876545
r_z_fm = 4.0 * r_p_fm / 3.0
delta_z = -2.0 * alpha * (mu_ep * c / hbar) * (r_z_fm * 1e-15)


def fine_recoil_fraction() -> float:
    """Small Breit-like kinematic recoil correction to contact density.

    This is the conservative term from finite two-body kinetic curvature at the
    Bohr scale. It is not the full bound-state QED recoil correction.
    """
    return -0.5 * alpha**2 * (mu_ep / m_p)


def hz_to_ev(freq_hz: float) -> float:
    return h * freq_hz / e


def ev_to_hz(energy_ev: float) -> float:
    return energy_ev * e / h


def finite_size_eV(reduced_mass_kg: float, r_fm: float, n: int = 2) -> float:
    r = r_fm * 1e-15
    return ((2.0 / 3.0) * alpha**4 * reduced_mass_kg**3 * c**4 * r**2 / hbar**2 / n**3) / e


def zemach_required_radius_fm(delta_z_required: float) -> float:
    return -delta_z_required / (2.0 * alpha * (mu_ep * c / hbar)) / 1e-15


def zemach_shell_approx_rz(r_e_fm: float, r_m_fm: float) -> float:
    """Accurate local linearization around the shell model.

    The exact coincident-shell result is 4r/3. For nearby magnetic radii we use
    the validated numerical sensitivity from direct form-factor integration:
    dr_Z/dr_M ~= 0.6665 near r_M=r_E. This is only a diagnostic map for the
    magnetic Hessian target, not a prediction.
    """
    slope = 0.6665
    return 4.0 * r_e_fm / 3.0 + slope * (r_m_fm - r_e_fm)


def main() -> None:
    delta_rec = fine_recoil_fraction()
    nu_after_ae_z = nu_F * (1.0 + a_e) * (1.0 + delta_z)
    nu_after_rec = nu_after_ae_z * (1.0 + delta_rec)

    required_hessian_frac = nu_obs / nu_after_rec - 1.0
    required_hessian_hz = nu_after_rec * required_hessian_frac
    delta_z_required_total = nu_obs / (nu_F * (1.0 + a_e) * (1.0 + delta_rec)) - 1.0
    r_z_required = zemach_required_radius_fm(delta_z_required_total)

    def rz_residual(rm: float) -> float:
        return zemach_shell_approx_rz(r_p_fm, rm) - r_z_required

    r_m_required = brentq(rz_residual, 0.1 * r_p_fm, 2.0 * r_p_fm)

    lamb_ref_hz = 1_057.844e6
    lamb_ref_ev = hz_to_ev(lamb_ref_hz)
    fs_2s_ev = finite_size_eV(mu_ep, r_p_fm, n=2)
    lamb_near_required_ev = lamb_ref_ev - fs_2s_ev
    lamb_near_required_hz = ev_to_hz(lamb_near_required_ev)

    text = [
        "# Saída — recuo, Hessiana magnética e Lamb Q48",
        "",
        "## 1. Hiperfina: recuo cinemático fino",
        "",
        "Classificação: avaliação direta reduzida. Este termo não é o recoil",
        "completo de QED ligada; é a correção cinemática conservadora do contato",
        "por curvatura finita de dois corpos.",
        "",
        f"- delta_rec^kin = {delta_rec:.15e}",
        f"- nu após a_e + Zemach = {nu_after_ae_z:.6f} Hz",
        f"- nu após a_e + Zemach + recuo cinemático = {nu_after_rec:.6f} Hz",
        f"- erro relativo após recuo cinemático = {(nu_after_rec/nu_obs-1.0):.15e}",
        "",
        "## 2. Hessiana magnética superior requerida",
        "",
        "Classificação: diagnóstico de resíduo, não previsão. O número abaixo diz",
        "qual elemento de matriz da Hessiana magnética superior deve ser produzido",
        "quando os blocos K_YY, K_YI e K_II forem avaliados diretamente.",
        "",
        f"- fração requerida = {required_hessian_frac:.15e}",
        f"- deslocamento requerido = {required_hessian_hz:.6f} Hz",
        f"- delta_Z total requerido depois de a_e+recuo = {delta_z_required_total:.15e}",
        f"- r_Z requerido = {r_z_required:.12f} fm",
        f"- r_M efetivo requerido no mapa de casca = {r_m_required:.12f} fm",
        f"- deslocamento r_M-r_p = {r_m_required-r_p_fm:+.12f} fm",
        "",
        "Forma GDQ:",
        "",
        "$$",
        "\\Delta\\nu_{\\rm Hess}^{\\rm mag}",
        "=",
        "\\frac1h",
        "\\langle 1s|",
        "P_{\\rm mag}^{\\dagger}",
        "\\Delta\\mathsf R_{p}^{\\rm mag,sup}",
        "P_{\\rm mag}",
        "|1s\\rangle.",
        "$$",
        "",
        "## 3. Lamb shift por deltaD_near",
        "",
        "Classificação: diagnóstico de escala do operador de campo próximo.",
        "Enquanto Delta R_p não for calculado diretamente, este valor não é",
        "previsão GDQ.",
        "",
        f"- Lamb de referência usado para escala = {lamb_ref_hz:.6f} Hz",
        f"- Lamb de referência = {lamb_ref_ev:.15e} eV",
        f"- tamanho finito H 2s já avaliado = {fs_2s_ev:.15e} eV",
        f"- deltaD_near requerido após tamanho finito = {lamb_near_required_ev:.15e} eV",
        f"- equivalente = {lamb_near_required_hz:.6f} Hz",
        "",
        "Forma GDQ:",
        "",
        "$$",
        "\\Delta E_{\\rm Lamb}",
        "=",
        "\\langle 2s_{1/2}|\\delta H_{\\rm near}|2s_{1/2}\\rangle",
        "-",
        "\\langle 2p_{1/2}|\\delta H_{\\rm near}|2p_{1/2}\\rangle.",
        "$$",
        "",
        "com",
        "",
        "$$",
        "\\delta\\mathcal D_{\\rm near}",
        "=",
        "\\Pi_{\\rm spin}",
        "(\\mathsf R_p-\\mathsf R_{\\rm point})",
        "\\Pi_{\\rm spin}.",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
