#!/usr/bin/env python3
"""
Verificação reduzida da reconstrução operacional de Hilbert.

Classificação:
    Teste de consistência algébrico-numérica.

O que este script verifica:
    1. uma forma positiva semidefinida possui subespaço nulo;
    2. o quociente pelo kernel produz um espaço físico de dimensão menor;
    3. estados puros e matrizes densidade normalizadas têm probabilidades de
       Born não negativas e soma unitária;
    4. observáveis Hermitianos têm valores esperados reais;
    5. evolução por Hamiltoniano Hermitiano preserva a norma;
    6. produto tensorial fatoriza o produto interno em estados produto.

O que este script NÃO prova:
    - reflexão positiva da ação GDQ completa;
    - existência de medida funcional em todos os setores;
    - autoadjunticidade essencial de operadores físicos reais;
    - fatorização tensorial para solitons interagentes.

Ele é um modelo mínimo autocontido da álgebra que a reconstrução setorial deve
produzir depois do quociente por nulos e redundâncias.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("saida_verificar_hilbert_operacional.md")


def unitary_from_hermitian(H: np.ndarray, t: float, hbar: float = 1.0) -> np.ndarray:
    """Calcula exp(-i H t / hbar) por decomposição espectral Hermitiana."""
    vals, vecs = np.linalg.eigh(H)
    phases = np.exp(-1j * vals * t / hbar)
    return vecs @ np.diag(phases) @ vecs.conj().T


def main() -> None:
    # Forma positiva semidefinida em D_+ antes do quociente.
    # O terceiro vetor é nulo: ele deve ser removido no espaço físico.
    G = np.diag([1.0, 0.5, 0.0])
    evals, evecs = np.linalg.eigh(G)
    positive = evals > 1.0e-12
    null_dim = int((~positive).sum())
    quotient_dim = int(positive.sum())

    # Base física ortonormal obtida mantendo apenas autovetores positivos e
    # reescalando pelo peso da forma.
    V = evecs[:, positive] @ np.diag(1.0 / np.sqrt(evals[positive]))
    G_phys = V.conj().T @ G @ V
    quotient_orth_error = float(np.linalg.norm(G_phys - np.eye(quotient_dim)))

    # Estado puro no espaço físico de dimensão 2.
    psi = np.array([1.0 + 0.0j, 2.0 - 1.0j])
    psi = psi / np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    trace_rho = np.trace(rho)
    rho_evals = np.linalg.eigvalsh(rho)

    # Observável Hermitiano e seus projetores espectrais.
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    obs_vals, obs_vecs = np.linalg.eigh(sigma_z)
    probs = []
    for k in range(len(obs_vals)):
        v = obs_vecs[:, k]
        P = np.outer(v, v.conj())
        probs.append(float(np.real(np.trace(rho @ P))))
    prob_sum_error = abs(sum(probs) - 1.0)
    min_prob = min(probs)
    expectation = np.trace(rho @ sigma_z)
    expectation_imag = abs(float(np.imag(expectation)))

    # Evolução unitária por Hamiltoniano Hermitiano.
    H = np.array([[0.7, 0.2 - 0.1j], [0.2 + 0.1j, 1.3]], dtype=complex)
    U = unitary_from_hermitian(H, t=3.7)
    unitarity_error = float(np.linalg.norm(U.conj().T @ U - np.eye(2)))
    norm_error = abs(np.linalg.norm(U @ psi) - np.linalg.norm(psi))

    # Produto tensorial: fatorização do produto interno em estados produto.
    a = np.array([1.0, 1.0j]) / np.sqrt(2.0)
    b = np.array([2.0, -1.0j])
    b = b / np.linalg.norm(b)
    c = np.array([1.0 - 1.0j, 0.5])
    c = c / np.linalg.norm(c)
    d = np.array([0.25, 1.5j])
    d = d / np.linalg.norm(d)

    lhs = np.vdot(np.kron(a, b), np.kron(c, d))
    rhs = np.vdot(a, c) * np.vdot(b, d)
    tensor_factor_error = abs(lhs - rhs)

    lines = [
        "---",
        'title: "Saída — Hilbert operacional"',
        "---",
        "",
        "# Saída — Hilbert operacional",
        "",
        "Classificação: teste de consistência algébrico-numérica.",
        "",
        "Este teste não é uma previsão metrológica. Ele verifica, em dimensão",
        "finita, a álgebra mínima esperada após a reconstrução operacional:",
        "quociente por nulos, estados, observáveis, evolução unitária e",
        "composição tensorial.",
        "",
        "## Resultados",
        "",
        "| Quantidade | Valor | Critério |",
        "|---|---:|---|",
        f"| dimensão nula removida | {null_dim} | $\\ge 1$ neste toy model |",
        f"| dimensão física do quociente | {quotient_dim} | `2` |",
        f"| erro de ortonormalização no quociente | {quotient_orth_error:.3e} | próximo de zero |",
        f"| $\\operatorname{{Tr}}\\varrho$ | {trace_rho.real:.12f} | `1` |",
        f"| menor autovalor de $\\varrho$ | {rho_evals.min():.3e} | não negativo |",
        f"| menor probabilidade espectral | {min_prob:.12f} | não negativa |",
        f"| erro na soma das probabilidades | {prob_sum_error:.3e} | próximo de zero |",
        f"| parte imaginária de $\\langle A\\rangle$ | {expectation_imag:.3e} | próxima de zero |",
        f"| erro de unitariedade de $U(t)$ | {unitarity_error:.3e} | próximo de zero |",
        f"| erro de preservação de norma | {norm_error:.3e} | próximo de zero |",
        f"| erro de fatorização tensorial | {tensor_factor_error:.3e} | próximo de zero |",
        "",
        "## Interpretação",
        "",
        "O teste confirma que, uma vez obtido o espaço físico positivo por",
        "quociente, a linguagem operacional usual segue: estados normalizados,",
        "matrizes densidade positivas, probabilidades espectrais, evolução",
        "unitária por Hamiltoniano Hermitiano e composição por produto tensorial.",
        "",
        "Na GDQ, essa camada é reconstruída a partir da geometria e não substitui",
        "a ação oficial.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()
