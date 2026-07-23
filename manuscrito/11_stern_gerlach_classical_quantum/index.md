---
title: "11. Stern-Gerlach e interação clássico--quântica"
---

# 11. Stern-Gerlach e interação clássico--quântica

Stern--Gerlach é o primeiro experimento em que a teoria da medida da GDQ pode
ser vista de forma concreta. O objeto já possui circulação e setor spinorial;
o aparelho não cria o spin. O aparelho fornece um campo clássico, seleciona um
eixo e transforma a orientação interna em dois canais espacialmente separados.

A ideia central é:

$$
\text{spin pertence ao objeto;}
\qquad
\text{o eixo pertence ao aparelho.}
$$

Por isso, o rótulo $\kappa=\pm1$ nunca deve ser lido como valor absoluto
simultâneo para todos os eixos. Ele é relativo à direção local do campo:

$$
\mathbf n(\mathbf x)=\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

## Roteiro

- [[11.1 - O que o experimento realmente exige]]
- [[11.2 - O soliton com circulação antes da medição]]
- [[11.3 - O aparelho como fonte e contorno magnético]]
- [[11.4 - Hopf, eixo do aparelho e dois projetores]]
- [[11.5 - Força e deflexão de centro de massa]]
- [[11.6 - Probabilidades angulares e Born operacional]]
- [[11.7 - Medições sequenciais e incompatibilidade de eixos]]
- [[11.8 - Condição adiabática e transições entre canais]]
- [[11.9 - O que fica para metrologia de aparelhos reais]]

## Resultado central

A cadeia GDQ para Stern--Gerlach é:

$$
J_{\rm app}^{\rm magnetico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\text{dois feixes}
\to
\text{registro}.
$$

Os dois projetores de canal são:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(I\pm\mathbf n\cdot\sigma\right).
$$

Para preparação $\mathbf a$, os pesos são:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

Em um canal fixo, a deflexão é mecânica:

$$
\Delta z
=
\kappa
\frac{\mu L^2}{2mv_y^2}
\frac{\partial B_z}{\partial z}.
$$

Assim, o experimento é separado em dois problemas:

1. dinâmica de canal, que é mecânica e geométrica;
2. população dos canais, que é Born operacional no Hilbert reconstruído.

## Estatuto do resultado

| Bloco | Status | Observação |
|---|---|---|
| Dois canais | Fechado estruturalmente | Projetores de Hopf/eixo do aparelho. |
| Triplet Hopf--Bismut | Fechado estruturalmente | Orientação complexa seleciona o setor auto-dual; aparelho seleciona direção. |
| Deflexão em canal fixo | Redução efetiva clássica | Usa campo e gradiente do aparelho. |
| Pesos angulares | Fechados operacionalmente | Born no Hilbert reconstruído. |
| Medidas sequenciais | Fechadas no setor efetivo | Eixos incompatíveis não revelam tabela preexistente. |
| Aparelho como fonte/contorno | Estrutural | Não altera a ação oficial. |
| Condição adiabática | Necessária | Fora dela há transições entre canais. |
| Metrologia real | Programa aplicado | Exige $\mathsf R_{\rm SG}$, material, geometria e mobilidade causal. |

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_stern_gerlach|Construção GDQ do Stern-Gerlach]]
- [[notes/fonte_classica_noether_zeeman_sg|Fonte clássica e Noether--Zeeman]]
- [[notes/derivacao_hopf_projetores_sg|Derivação de Hopf dos projetores de Stern-Gerlach]]
- [[notes/selecao_quiral_hopf_bismut|Seleção quiral Hopf--Bismut]]
- [[notes/forca_deflexao_sg_setor_reduzido|Força e deflexão no setor reduzido]]
- [[notes/pesos_born_sg|Pesos Born no Stern-Gerlach]]
- [[notes/condicao_adiabatica_sg|Condição adiabática]]
- [[notes/background_hessiana_e_dtn_sg|Background, Hessiana e DtN no Stern-Gerlach]]
- [[notes/auditoria_numerica_sg|Auditoria numérica de Stern-Gerlach]]

[[../index|← Home]] | [[11.1 - O que o experimento realmente exige|Next →]]
