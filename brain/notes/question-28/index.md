---
title: Questão 28 — grupo efetivo e três gerações
status: closed-structurally-reduced
source: questão_28_final.md
updated: 2026-07-16
---

# Questão 28 — grupo efetivo e três gerações

## Estado vigente

A Q28 está fechada no modelo estrutural reduzido quanto ao grupo efetivo, ao
espectro de uma geração e à seleção de três gerações.

O fechamento não usa $N_G=3$ como entrada. A conservação de Noether seleciona
um junction horizontal elementar de três estômatos; a aditividade APS fornece
índice três; a colagem global $\mathbb Z_6$ fornece $A=18$ e $N_G=A/6=3$.

## Cadeia registrada

1. O fibrado interno efetivo é

$$
E_{\rm int}=E_C\oplus E_W\oplus L_Y.
$$

2. Automorfismos preservando os invariantes geram

$$
G_{\rm eff}^{\rm global}
=
\frac{SU(3)_C\times SU(2)_L\times U(1)_Y}{\Gamma},
\qquad
\Gamma\subseteq\mathbb Z_6.
$$

3. O espectro de uma geração e o cancelamento de anomalias são estruturados.
4. O setor local $U(1)$ é fechado por índice APS unitário.
5. A seleção reduzida de três estômatos dá

$$
N=3
\Longrightarrow
\operatorname{Ind}_{\rm APS}=3
\Longrightarrow
A=18
\Longrightarrow
N_G=3.
$$

6. A Hessiana vinculada do setor multicítrico simétrico e modos não
   homogêneos dão gap positivo no modelo reduzido.

## Resultado de acoplamentos

No background reduzido, os índices quadráticos do espectro de uma geração são:

$$
I_3=2,
\qquad
I_2=2,
\qquad
I_Y=\frac{10}{3}.
$$

Da norma comum:

$$
g_s=g,
\qquad
\frac{g'^2}{g^2}=\frac35,
\qquad
\sin^2\theta_W=\frac38.
$$

## Limitações

O resultado é estrutural/reduzido. Para elevar a teorema integral da ação
oficial, ainda é preciso controlar a Hessiana física completa no background
multicítrico e a colagem global. O arquivo final registra avanços fortes
nessa direção, inclusive `q28/hessiana_espectral_completa_background_c3.md`.

## Ponteiros

- Resultado: `brain/conditional-results/q28-effective-sm-three-generations/index.md`

