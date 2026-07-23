---
title: "Produto global, não circularidade e três estômatos"
---

# Produto global, não circularidade e três estômatos

Esta nota registra a separação entre o cálculo global auxiliar e a seleção
local de três estômatos. Ela evita o erro de escolher uma classe topológica
porque ela produz o número desejado.

## 1. O produto global não gera três por si só

No espaço cosmológico auxiliar:

$$
K=T^5\times S^3,
$$

os números de Betti vêm de Künneth:

$$
P_{T^5}(t)=(1+t)^5,
\qquad
P_{S^3}(t)=1+t^3.
$$

Logo:

$$
P_K(t)=(1+t)^5(1+t^3).
$$

Os Betti são:

$$
(1,5,10,11,10,11,10,5,1).
$$

A característica de Euler é:

$$
\chi(K)=0.
$$

Assim, a topologia produto $T^5\times S^3$ não seleciona
automaticamente três gerações. A ordem três de um subgrupo ou a presença de
$S^3$ também não bastam.

## 2. Kernel de Berry plano

Se o toro é tratado como produto plano com holonomias constantes, a conexão
de Berry do kernel é plana:

$$
F_B=0.
$$

Então:

$$
c_2(E_G)=0,
\qquad
N_{ab}=0.
$$

Esse resultado negativo é importante: ele exclui a tentativa circular de
obter três gerações de uma família trivial de holonomias no toro plano.

## 3. Quando uma classe global pode contribuir

Uma contribuição global real exige uma classe mista:

$$
c_2(E_G)=a_4+b_1\smile u_3,
$$

onde $a_4$ vive no setor toroidal e $u_3$ representa a classe do $S^3$. Para
um setor $SU(2)$, a contribuição de índice assume a forma:

$$
{\rm Ind}
=
\frac16
\langle a_4\smile b_1,[T^5]\rangle.
$$

Defina:

$$
N_{ab}=\langle a_4\smile b_1,[T^5]\rangle.
$$

Então:

$$
N_G=\frac{N_{ab}}6.
$$

Escolher $N_{ab}=18$ apenas para obter $N_G=3$ seria engenharia reversa. Por
isso o capítulo não usa essa rota como fundamento da contagem local.

## 4. Seleção local não circular

A seleção local parte de Noether e da distribuição horizontal de Hopf:

$$
\sum_{a=1}^{N}\mathbf T_a=0,
\qquad
\mathbf T_a\in\mathcal H,
\qquad
\dim_{\mathbb R}\mathcal H=2.
$$

Um junction elementar precisa ser fechado, não colinear e isolado. Em duas
dimensões horizontais:

$$
N=1
\quad\text{não fecha,}
$$

$$
N=2
\quad\text{é colinear,}
$$

$$
N=3
\quad\text{é o primeiro fechado, não colinear e isolado.}
$$

Para $N>3$, aparecem $N-3$ modos internos nulos. Portanto o primeiro
junction elementar estável é:

$$
N=3.
$$

Com três estômatos primitivos coorientados, a aditividade APS fornece:

$$
{\rm Ind}_{\rm total}
=
\sum_{a=1}^{3}{\rm ind}_{a}
=
3.
$$

Como cada unidade primitiva corresponde a seis unidades inteiras na colagem
$\mathbb Z_6$:

$$
A=6\,{\rm Ind}_{\rm total}=18,
\qquad
N_G=\frac A6=3.
$$

## 5. Verificação computacional

O script:

$$
{\tt scripts/global_produto_tres_estomatos.py}
$$

reproduz os Betti de $T^5\times S^3$, confirma $\chi=0$, mostra que o kernel
plano tem $N_{ab}=0$ e verifica a contagem não circular por três estômatos.
