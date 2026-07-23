#!/usr/bin/env python3
"""Q25.01 — rede mínima de domínios GDQ e matriz de interface.

Classificação: teste de consistência.

O script não importa QMC como ontologia. Ele verifica o núcleo algorítmico GDQ:
medida positiva local, interface unitária/contrativa e holonomia fermiônica
armazenada na fase.
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resultados" / "saida_q25_01_domain_interface.md"


def unitary_interface(theta: float, holonomy: complex = -1.0 + 0.0j) -> np.ndarray:
    """Interface 2x2 fechada com fase de holonomia no canal transmitido."""
    r = math.cos(theta)
    t = math.sin(theta)
    # Forma SU(2) com fase no canal de transmissao.
    return np.array(
        [[r, t * holonomy], [-t * np.conjugate(holonomy), r]],
        dtype=np.complex128,
    )


def contractive_interface(theta: float, loss: float, holonomy: complex = -1.0 + 0.0j) -> np.ndarray:
    """Interface aberta: multiplicar a interface fechada por sqrt(1-loss)."""
    if not 0.0 <= loss <= 1.0:
        raise ValueError("loss deve estar em [0,1]")
    return math.sqrt(1.0 - loss) * unitary_interface(theta, holonomy)


def main() -> None:
    rng = np.random.default_rng(2501)
    n_domains = 4
    raw = rng.uniform(0.2, 1.0, size=n_domains)
    rho = raw / raw.sum()

    theta = 0.37
    hol = -1.0 + 0.0j
    s_closed = unitary_interface(theta, hol)
    s_open = contractive_interface(theta, loss=0.08, holonomy=hol)

    ident = np.eye(2, dtype=np.complex128)
    unitary_error = float(np.linalg.norm(s_closed.conj().T @ s_closed - ident))
    contraction_eigs = np.linalg.eigvalsh(ident - s_open.conj().T @ s_open)
    contraction_min = float(contraction_eigs.min())
    positivity_min = float(rho.min())

    # Probabilidades induzidas na interface fechada preservam norma.
    psi_in = np.array([math.sqrt(rho[0]), math.sqrt(rho[1])], dtype=np.complex128)
    psi_out = s_closed @ psi_in
    norm_in = float(np.vdot(psi_in, psi_in).real)
    norm_out = float(np.vdot(psi_out, psi_out).real)
    norm_error = abs(norm_out - norm_in)

    rows = [
        ("dominios", str(n_domains)),
        ("min rho_a", f"{positivity_min:.12e}"),
        ("Hol(P_ij)", f"{hol.real:.1f}"),
        ("erro unitariedade fechado", f"{unitary_error:.12e}"),
        ("min eig(I-S†S) aberto", f"{contraction_min:.12e}"),
        ("erro conservacao norma", f"{norm_error:.12e}"),
    ]

    verdict = (
        "aprovado"
        if positivity_min > 0 and abs(hol + 1) < 1e-14 and unitary_error < 1e-14 and norm_error < 1e-14 and contraction_min > -1e-14
        else "falhou"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# Q25.01 — Domínios, interface e holonomia\n\n"
        "Classificação: teste de consistência algorítmica GDQ.\n\n"
        "| item | valor |\n|---|---:|\n"
        + "".join(f"| {k} | {v} |\n" for k, v in rows)
        + f"\nVeredito: **{verdict}**.\n\n"
        "Interpretação: a medida local é positiva, a fase de troca fica em "
        "`Hol(P_ij)=-1`, a interface fechada conserva fluxo e a interface "
        "aberta é contrativa. Isto ainda não prova variância polinomial.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
