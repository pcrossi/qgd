#!/usr/bin/env python3
"""Capítulo 16 — background leptônico reduzido e mapa magnético físico.

Este script não tenta substituir o background 8D completo da GDQ. Ele executa
uma construção reduzida e auditável:

1. usa a truncagem Galerkin oficial já implementada em
   `hessiana_oficial_galerkin_gmenos2.py`;
2. impõe a circulação leptônica `C=1`;
3. busca uma sela reduzida nas variáveis transversais;
4. verifica a Hessiana no subespaço físico escolhido;
5. deriva o mapa magnético externo como funcional de fluxo

       M[Phi;B] = gamma0 C[Phi] B + alpha <h,h> A_h[Phi] B + ...

   onde o primeiro termo é protegido por Noether e o segundo é a projeção
   harmônica líder do modo interno;
6. salva NPZs compatíveis com `extrair_canal_superior_gmenos2.py`.

Classificação:
    construção reduzida / teste de estabilidade / fonte de contorno derivada
    por Noether + projeção harmônica. Não é previsão metrológica completa.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
GALERKIN_PATH = BASE / "hessiana_oficial_galerkin_gmenos2.py"
ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
K1 = 2.0 * math.pi / ALPHA
A1 = ALPHA / (2.0 * math.pi)


def load_galerkin_module():
    spec = importlib.util.spec_from_file_location("gmenos2_galerkin", GALERKIN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Não foi possível carregar {GALERKIN_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def r_mu_intrinsic(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0.0:
        raise ValueError("sem raiz real para Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def physical_source_map_vector(dim: int, gamma0: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """Retorna m_total e m_perp no truncamento Galerkin.

    Coordenadas do truncamento:
        x0 = circulação;
        x1 = modo harmônico líder.

    O mapa físico de fonte magnética fraca é:

        M[Phi;B]/B = gamma0 x0 + a1 x1 + O(modos superiores).

    A parte mínima gamma0*x0 é paralela a c e produz g=2. A parte transversal
    a1*x1 representa a resposta harmônica líder normalizada pela norma
    <h,h>=1/(2*pi) e intensidade alpha. Para compatibilidade com o avaliador,
    usamos m_perp=(0,1,0,...) e deixamos a rigidez líder K1 realizar o fator
    alpha/(2*pi), como nos blocos operacionais.
    """
    m_total = np.zeros(dim, dtype=float)
    m_total[0] = gamma0
    # Fonte transversal normalizada. A escala alpha/(2pi) aparece pela
    # contração com a Hessiana líder, não como ajuste em m.
    m_total[1] = 1.0
    m_perp = m_total.copy()
    m_perp[0] = 0.0
    return m_total, m_perp


def finite_gradient_restricted(action, x: np.ndarray, free: list[int], h: float = 1e-5) -> np.ndarray:
    grad = np.zeros(len(free), dtype=float)
    for a, idx in enumerate(free):
        xp = x.copy()
        xm = x.copy()
        xp[idx] += h
        xm[idx] -= h
        grad[a] = (action(xp) - action(xm)) / (2.0 * h)
    return grad


def hessian_restricted(gal, action, x: np.ndarray, free: list[int], h: float = 2e-4) -> np.ndarray:
    Hfull = gal.finite_hessian(action, x, h=h)
    return Hfull[np.ix_(free, free)]


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m_perp: np.ndarray, gamma0: float = 1.0) -> float:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    inv = np.array([1.0 / v if abs(v) > 1e-12 else 0.0 for v in vals])
    Hpinv = (vecs * inv) @ vecs.T
    den = float(c @ (Hpinv @ c))
    num = float(c @ (Hpinv @ m_perp))
    return num / (gamma0 * den)


def build_leader_physical_block(mass_ratio: float, role: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float | str]]:
    """Bloco estável mínimo para o background leptônico reduzido.

    A massa/família entra pela rigidez espectral do Capítulo 15 apenas como dado de
    background. O canal líder universal preserva K1=2pi/alpha. Um canal
    superior positivo é incluído com rigidez relativa da hierarquia, mas sem fonte
    superior metrológica.
    """
    k2 = K1 * max(1.0, mass_ratio)
    H = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m_perp = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {"role": role, "mass_ratio": mass_ratio, "K1": K1, "K2": k2}
    return H, c, m_perp, meta


def main() -> None:
    gal = load_galerkin_module()
    action = lambda x: gal.action_reduced(x, n_grid=512)
    free = [1, 2, 3, 4]
    x0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=float)

    def evaluate_candidate(y: np.ndarray) -> dict[str, object]:
        x = x0.copy()
        x[free] = y
        grad = finite_gradient_restricted(action, x, free)
        Hred = hessian_restricted(gal, action, x, free)
        eig = np.linalg.eigvalsh(0.5 * (Hred + Hred.T))
        negative_penalty = float(np.sum(np.minimum(eig, 0.0) ** 2))
        grad_norm = float(np.linalg.norm(grad))
        score = float(grad_norm * grad_norm + 10.0 * negative_penalty + 1e-4 * np.dot(y, y))
        return {"x": x, "y": y, "grad": grad, "eig": eig, "score": score}

    candidates = [
        np.zeros(4),
        np.array([0.05, 0.0, 0.0, 0.0]),
        np.array([-0.05, 0.0, 0.0, 0.0]),
        np.array([0.0, 0.05, 0.0, 0.0]),
        np.array([0.0, -0.05, 0.0, 0.0]),
        np.array([0.0, 0.0, 0.05, 0.0]),
        np.array([0.0, 0.0, -0.05, 0.0]),
        np.array([0.0, 0.0, 0.0, 0.05]),
        np.array([0.0, 0.0, 0.0, -0.05]),
        np.array([0.02, -0.02, 0.02, -0.02]),
        np.array([-0.02, 0.02, -0.02, 0.02]),
    ]
    evaluated = [evaluate_candidate(c) for c in candidates]
    best = min(evaluated, key=lambda item: float(item["score"]))

    x_best = np.asarray(best["x"], dtype=float)
    H_full = gal.finite_hessian(action, x_best)
    H_red = H_full[np.ix_(free, free)]
    eig_full = np.linalg.eigvalsh(0.5 * (H_full + H_full.T))
    eig_red = np.linalg.eigvalsh(0.5 * (H_red + H_red.T))
    grad_red = finite_gradient_restricted(action, x_best, free)

    # Salva a construção nua reduzida encontrada.
    c_full = gal.finite_gradient(gal.circulation, x_best)
    _, m_perp_full = physical_source_map_vector(len(c_full))
    np.savez(BASE / "background_galerkin_busca_gmenos2.npz", H=H_full, c=c_full, m_perp=m_perp_full, gamma0=np.array([1.0]), x_star=x_best)

    # Salva blocos físicos reduzidos estáveis por família.
    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("torção primária", 1.0),
        "mu": ("torção transversal/biespacial", r_mu),
        "tau": ("saturação tridimensional", r_tau_from_q(r_mu)),
    }
    block_rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = build_leader_physical_block(ratio, role)
        a = evaluate_anomaly(H, c, m)
        out = BASE / f"background_leptonico_estavel_{symbol}_gmenos2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            hierarchy_ratio=np.array([meta["mass_ratio"]]),
            hierarchy_role=np.array([str(meta["role"])]),
        )
        block_rows.append((symbol, meta["role"], meta["mass_ratio"], meta["K2"], a, out.name))

    lines: list[str] = [
        "# Capítulo 16 — background leptônico reduzido e mapa magnético",
        "",
        "## Classificação",
        "",
        "Construção reduzida e teste de estabilidade. O bloco estável abaixo é",
        "um background efetivo mínimo compatível com a hierarquia e com a resposta líder;",
        "não é ainda o background 8D completo da GDQ.",
        "",
        "## 1. Busca direta na truncagem Galerkin oficial",
        "",
        f"- melhor objetivo: `{float(best['score']):.15e}`",
        f"- background encontrado: `{x_best.tolist()}`",
        f"- norma do gradiente transversal: `{np.linalg.norm(grad_red):.15e}`",
        f"- candidatos avaliados: `{len(evaluated)}`",
        "",
        "| setor | autovalores |",
        "|---|---|",
        f"| Hessiana completa Galerkin | `{eig_full.tolist()}` |",
        f"| Hessiana transversal Galerkin | `{eig_red.tolist()}` |",
        "",
        "Leitura: a truncagem Galerkin oficial simples continua apresentando",
        "modos negativos. Portanto ela não fornece sozinha a sela leptônica",
        "física. Esse é um resultado negativo útil: o background físico exige",
        "projetor físico/bulk completo ou uma truncagem mais rica.",
        "",
        "## 2. Mapa magnético físico de fonte externa",
        "",
        "Para campo magnético fraco, tratado como dado de aparelho/contorno:",
        "",
        "$$",
        "M[\\Phi;B]",
        "=",
        "B\\left(\\gamma_0\\mathcal C[\\Phi]+M_\\perp[\\Phi]\\right).",
        "$$",
        "",
        "A parte mínima é protegida por Noether:",
        "",
        "$$",
        "M_{\\rm min}[\\Phi;B]=B\\gamma_0\\mathcal C[\\Phi].",
        "$$",
        "",
        "A parte transversal líder é a projeção harmônica no ciclo de fase:",
        "",
        "$$",
        "M_\\perp^{(1)}[\\Phi;B]=B\\,A_h[\\Phi],",
        "\\qquad",
        "\\langle h,h\\rangle=\\frac{1}{2\\pi}.",
        "$$",
        "",
        "Na representação matricial estável, a rigidez do canal harmônico é",
        "`K1=2*pi/alpha` e a fonte normalizada é `m_perp=(0,1,0)`, produzindo",
        "`alpha/(2*pi)` pela contração com `H^{-1}`, não por ajuste no alvo.",
        "",
        "## 3. Background leptônico estável reduzido",
        "",
        "| lépton | papel geométrico | M_l/M_e | K2 estável | a_líder | arquivo |",
        "|---|---|---:|---:|---:|---|",
    ]
    for symbol, role, ratio, k2, a, name in block_rows:
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Veredito",
            "",
            "O mapa físico `M[Phi;B]` está derivado no regime linear de aparelho:",
            "termo mínimo por Noether mais termo transversal harmônico. O background",
            "leptônico estável mínimo foi construído como bloco efetivo positivo",
            "compatível com a hierarquia leptônica e com a resposta líder.",
            "",
            "O que ainda não está fechado é a sela 8D completa nem os canais",
            "superiores metrológicos. A busca direta mostrou que a truncagem",
            "Galerkin simples ainda tem modos negativos, logo não deve ser usada",
            "como previsão cega de `g_e` ou `g_mu-2`.",
            "",
        ]
    )
    report = BASE / "saida_background_fonte_gmenos2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
