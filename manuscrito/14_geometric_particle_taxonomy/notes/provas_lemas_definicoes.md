---
title: "Provas, lemas e definições — Capítulo 14"
---

# Provas, lemas e definições — Capítulo 14

## 1. Construção GDQ do problema

Status: cadeia estrutural completa.

Nota:

[[construcao_gdq_taxonomia|Construção GDQ da taxonomia geométrica]]

## 2. Fibrado interno efetivo

Status: definição estrutural.

Nota:

[[fibrado_interno_efetivo|Fibrado interno efetivo]]

## 3. Hipercargas

Status: teorema diofantino condicional às representações internas.

Nota:

[[hipercargas_z6_anomalias|Hipercargas por Z6 e anomalias]]

Certificação Lean:
[HyperchargeDiophantine.lean](../../../formal/GDQ/HyperchargeDiophantine.lean).
O módulo verifica diretamente as quatro equações de anomalia e as congruências
$\mathbb Z_6$, e prova que, no setor primitivo orientado com $q=1$ e com a
ordenação que fixa o nome dos dois singletos coloridos,

$$
(q,u,d,\ell,e)
=
(1,-4,2,-3,6).
$$

Sem a ordenação, as equações preservam a troca entre os dois singletos; ela é
uma convenção de rotulagem, não uma nova equação física.

## 4. Três estômatos

Status: fechado no modelo horizontal reduzido.

Nota:

[[noether_tres_estomatos_hessiana|Noether, três estômatos e Hessiana]]

Complementos:

[[indice_aps_hopf_bismut|Índice local APS, Hopf e Bismut]]

[[global_produto_e_tres_estomatos|Produto global, não circularidade e três estômatos]]

Certificação Lean:
[GenerationJunction.lean](../../../formal/GDQ/GenerationJunction.lean).
Se $D\mathcal C:\mathbb R^N\to\mathbb R^2$ tem posto dois e seu kernel tem
dimensão um — apenas a rotação comum —, posto--nulidade fornece:

$$
2+1=N.
$$

Logo, $N=3$. O módulo também prova que, sob posto dois e $N\ge3$, a remoção
da rotação comum deixa exatamente $N-3$ modos nulos internos. Portanto,
isolamento é equivalente a não haver esses modos adicionais dentro da classe
horizontal declarada.

O teorema não afirma que toda sela possível da ação oficial possui posto dois
e kernel unidimensional. Essas são as condições geométricas que definem o
junction elementar não colinear e isolado analisado neste capítulo.

## 5. Hessiana vinculada

Status: demonstrada no setor coletivo $C_3$ e no preenchimento gaussiano
reduzido após projeção dos modos de simetria.

Nota:

[[noether_tres_estomatos_hessiana|Noether, três estômatos e Hessiana]]

[[hessiana_fisica_c3_gap|Hessiana física C3 e gap reduzido]]

## 6. Acoplamentos

Status: razões geométricas no ponto comum.

Nota:

[[acoplamentos_normas_fibrado|Acoplamentos como normas do fibrado]]

## 7. Geradores locais

Status: rota geométrica local.

Nota:

[[potenciais_killing_geradores|Potenciais de Killing e geradores]]

Certificação Lean:
[KillingPoissonLie.lean](../../../formal/GDQ/KillingPoissonLie.lean). Os
potenciais locais são tipados como homomorfismo de Lie, de modo que

$$
P([X,Y])
=
\{P(X),P(Y)\}.
$$

Se o mapa de potenciais é injetivo, as relações de Poisson também refletem as
relações entre os geradores. A existência e a colagem global dos potenciais
continuam condições do fibrado.

## 8. Elevação às representações

Status: demonstração estrutural da multiplicidade de uma geração e de três
gerações, separando índice geométrico de hipercarga.

Nota:

[[elevacao_indice_representacoes|Elevação do índice às representações]]

Certificação Lean do núcleo APS:
[APSHopfBismut.lean](../../../formal/GDQ/APSHopfBismut.lean). O módulo prova
os invariantes discretos

$$
c_1(L_1)=1,
\qquad
h_1=2,
$$

a invariância do índice quando o fluxo espectral é nulo e

$$
\operatorname{ind}_{\rm final}
=
\operatorname{ind}_{\rm inicial}
-\operatorname{SF}
=1
$$

para índice inicial zero e travessia primitiva orientada
$\operatorname{SF}=-1$. O cálculo analítico da eta e a existência desse
caminho de Bismut permanecem hipóteses verificadas na prova humana.

O módulo
[GenerationJunction.lean](../../../formal/GDQ/GenerationJunction.lean)
compõe esse índice local com a seleção do junction: três unidades primitivas
coorientadas somam índice APS total três. A contagem independente
$6+3+3+2+1=15$ fornece 45 componentes de Weyl para as três unidades. Essa
contagem não identifica índice com hipercarga; apenas eleva a multiplicidade
quiral às representações internas já selecionadas.
