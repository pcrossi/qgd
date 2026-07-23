---
title: "Scripts do Capítulo 21"
---

# Scripts do Capítulo 21

Os scripts são finais/reduzidos, autocontidos e comentados. Eles não preservam
tentativas históricas.

| Script | Saída | Função |
|---|---|---|
| `relaxacao_cp_torsional.py` | `saida_relaxacao_cp_torsional.md` | Integra o fluxo $\dot\theta=-\kappa\chi\sin\theta$, calcula $f_B$, $m_B$ e compara com limite de EDM. |
| `periodicidade_cp_carga_inteira.py` | `saida_periodicidade_cp_carga_inteira.md` | Verifica a invariância da fase topológica sob $\theta\mapsto\theta+2\pi$ quando $Q_C\in\mathbb Z$. |
| `hessiana_susceptibilidade_cp.py` | `saida_hessiana_susceptibilidade_cp.md` | Verifica que a Hessiana do potencial periódico é $+\chi$ no mínimo CP e $-\chi$ no máximo instável. |
| `hopf_cauchy_residuo.py` | `saida_hopf_cauchy_residuo.md` | Verifica simbolicamente a meia-monodromia por resíduo $1/2$. |
| `monopolo_vorticidade.py` | `saida_monopolo_vorticidade.md` | Verifica que uma vorticidade regular tem divergência nula e separa domínio local de topologia global. |

Classificação:

1. `relaxacao_cp_torsional.py`: avaliação direta de fluxo reduzido e comparação fenomenológica;
2. `periodicidade_cp_carga_inteira.py`: verificação simbólica/didática de identidade topológica;
3. `hessiana_susceptibilidade_cp.py`: verificação simbólica/numérica de consistência;
4. `hopf_cauchy_residuo.py`: verificação simbólica de identidade topológica;
5. `monopolo_vorticidade.py`: verificação simbólica/didática de identidade diferencial.
