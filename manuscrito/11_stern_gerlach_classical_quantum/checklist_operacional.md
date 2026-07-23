---
title: "Checklist operacional — Capítulo 11"
---

# Checklist operacional — Capítulo 11

## 1. Enunciado

Explicar Stern--Gerlach como interação clássico--quântica na GDQ: o aparelho
fornece campo/contorno, seleciona eixo, separa dois canais e registra pesos
Born.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Eixo do aparelho | Definição operacional | $\mathbf n=\mathbf B/|\mathbf B|$. |
| Dois projetores | Fechado estruturalmente | Hopf/Pauli local. |
| Triplet Hopf--Bismut | Fechado estruturalmente | A estrutura complexa seleciona $SU(2)_+$; o aparelho seleciona uma direção. |
| Deflexão | Redução efetiva | Canal fixo, regime adiabático. |
| Pesos angulares | Fechados operacionalmente | Born do Cap. 9. |
| Sequências incompatíveis | Fechadas no setor efetivo | Sem tabela preexistente. |
| Adiabaticidade | Hipótese de validade | Fora dela há transições. |
| $\mathsf R_{\rm SG}$ real | Programa metrológico | Depende do aparelho. |

## 3. Cadeia dedutiva

$$
\mathcal S_{\rm GDQ}
\to
J_{\rm SG}^{\rm clássico}
\to
\Phi_\ast^{\rm SG}
\to
K_{\rm phys}^{\rm SG}
\to
\mathsf R_{\rm SG}
\to
\text{spin/Hopf}
\to
\mathbf n_{\rm app}
\to
P_{\mathbf n}^{\pm}
\to
E_\pm
\to
\mathbf F_\pm
\to
\Delta z_\pm
\to
p_\pm.
$$

Construção técnica chamada:

- [[notes/construcao_gdq_stern_gerlach|Construção GDQ do Stern-Gerlach]]
- [[notes/selecao_quiral_hopf_bismut|Seleção quiral Hopf--Bismut]]

## 4. Scripts

| Script | Classificação |
|---|---|
| `calcular_pesos_sg.py` | Teste de consistência operacional. |
| `simular_deflexao_sg.py` | Redução efetiva/aparelho. |
| `testar_sequencias_sg.py` | Teste simbólico de medições sequenciais. |
| `verificar_triplet_hopf_bismut.py` | Verificação do triplet auto-dual de Hopf. |

## 5. Pontos que não podem ser esquecidos

- Spin pertence ao objeto; eixo pertence ao aparelho.
- $\kappa$ é relativo a $\mathbf n$.
- Trajetória em canal fixo é determinística; população é estatística.
- O aparelho é contorno/fonte, não alteração da ação oficial.
- Pauli matrices são representação local, não ontologia nova.
