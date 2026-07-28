---
title: "Checklist operacional — Capítulo 14"
---

# Checklist operacional — Capítulo 14

## 1. Enunciado

Construir a taxonomia geométrica de partículas sem tabela livre: matéria como
sóliton/estômato, grupo efetivo como automorfismo do fibrado interno, cargas
como pesos globais e gerações como índice aditivo de três estômatos.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Sóliton/estômato | Estrutural | Matéria como defeito geométrico. |
| Critério de sóliton material | Fechado estruturalmente | Exige equação estacionária, energia finita, carga, spin, Hessiana, modos zero, assintótica e interação. |
| Monotonicidade e estabilidade | Fechada condicionalmente | Monotonicidade é Lyapunov; estabilidade exige Hessiana física sem autovalores negativos. |
| Fibrado interno | Fechado estruturalmente | $E_C\oplus E_W\oplus L_Y$. |
| Grupo efetivo | Fechado estruturalmente | $\operatorname{Aut}_{\rm GDQ}(E_{\rm int})$. |
| $Z_6$ e hipercarga | Fechado como diofantino | Condicional às representações internas. |
| Anomalias | Demonstradas | Cancelamento explícito por geração. |
| Índice APS local | Demonstrado no protótipo Hopf--Bismut | Um estômato primitivo coorientado fornece índice $1$. |
| Elevação às representações | Demonstrada | Uma unidade local gera $15$ componentes de Weyl; três geram $45$. |
| Produto global plano | Excluído como origem de três | Betti/Euler/Berry plano não fornecem $N_G=3$. |
| Três estômatos | Fechado no modelo horizontal reduzido | Posto dois e kernel unidimensional selecionam $N=3$; não é afirmação sobre todo background possível. |
| Hessiana $C_3$ | Demonstrada nos modos coletivos e preenchimento gaussiano reduzido | Dois modos relativos positivos e gap reduzido positivo. |
| Acoplamentos | Razões fechadas | $g_s=g$, $g'^2/g^2=3/5$, $\sin^2\theta_W=3/8$. |
| Massas/misturas | Futuro | Capítulos posteriores. |

## 3. Cadeia dedutiva

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
E_{\rm int}
\to
\operatorname{Aut}_{\rm GDQ}(E_{\rm int})
\to
\mathbb Z_6
\to
\mathcal E_{\rm gen}
\to
N=3
\to
\operatorname{Ind}_{\rm total}=3.
$$

## 4. Construção variacional obrigatória

O capítulo deve manter explícita a cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm estômato}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\text{modos internos}
\to
\text{índice/cargas}.
$$

No setor $C_3$, a Hessiana vinculada é:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}
\left(
K_\perp^{(r,0)}
\right)^{-1}
J_{\theta r}^{\dagger}.
$$

Com conservação da classe de fluxo:

$$
J_{\theta r}=0.
$$

## 5. Scripts

| Script | Classificação |
|---|---|
| `verificar_soliton_gaussiano.py` | Verificação da solução gaussiana neutra, energia $\mathcal W=0$ e gap OU reduzido. |
| `monotonicidade_vs_hessiana.py` | Ilustração de que Lyapunov monotônico não substitui Hessiana positiva. |
| `hipercargas_z6.py` | Busca diofantina e verificação de anomalias. |
| `indice_aps_hopf_bismut.py` | Verificação do fluxo primitivo, eta reduzida, kernel torsional e índice APS local. |
| `elevacao_indice_representacoes.py` | Contagem de componentes de Weyl por unidade de índice e por três estômatos. |
| `global_produto_tres_estomatos.py` | Betti de $T^5\times S^3$, Euler zero, Berry plano e contagem por três estômatos. |
| `hessiana_tres_centros.py` | Verificação da Hessiana vinculada $C_3$. |
| `hessiana_fisica_c3_gap.py` | Projetor físico, Schur e gap reduzido do junction $C_3$. |
| `acoplamentos_normas.py` | Avaliação direta das normas e razões de acoplamento. |
| `selecao_junction_N.py` | Teste reduzido de seleção $N=3$ e modos nulos para $N>3$. |

## 6. Scripts históricos da taxonomia geométrica

Os scripts finais/reduzidos acima substituem a necessidade de migrar todos os
scripts exploratórios da taxonomia geométrica para o corpo do capítulo. A lista completa de
scripts históricos permanece em `o histórico externo de construção` e está registrada em
[[notes/scripts_preservados_taxonomia|Scripts migrados da taxonomia geométrica]].

## 7. Pontos que não podem ser esquecidos

- Não dizer que cargas fracionárias são Chern fracionário literal.
- Não usar o Modelo Padrão como ontologia.
- Não usar $N_G=3$ como entrada.
- Não transformar massas e misturas em parte da a taxonomia geométrica.
- Não comparar acoplamentos de escalas diferentes sem background.
- Não omitir a Hessiana vinculada dos três centros.
