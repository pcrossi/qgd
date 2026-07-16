# Q28 — Fechamento da seleção de três estômatos

## 1. Resultado

A contagem de três estômatos não é introduzida como dado experimental. Ela
segue da combinação entre conservação do fluxo, geometria horizontal de Hopf
e definição de um junction elementar estável.

Escrevendo

$$
f=u+iv,
$$

a invariância da ação oficial sob

$$
v\mapsto v+\varepsilon
$$

produz a corrente de Noether de fase. A integração dessa corrente numa pequena
região que contém o junction fornece

$$
\sum_{a=1}^{N}\mathbf T_a=0.
$$

As tensões relativas pertencem à distribuição horizontal da fibração de Hopf,

$$
\mathcal H=\ker\eta_H,
\qquad
\dim_{\mathbb R}\mathcal H=2.
$$

No setor isotrópico, o funcional universal de fechamento é

$$
\mathcal E_{\rm close}
=\frac{\kappa_{\rm rel}}2
\left|\sum_{a=1}^{N}\mathbf T_a\right|^2.
$$

## 2. Teorema de seleção

Um junction elementar deve ser:

1. fechado pela corrente de Noether;
2. não colinear na distribuição horizontal;
3. isolado depois de removida a rotação global.

As duas primeiras condições exigem

$$
N\geq3.
$$

No ponto de fechamento, a Hessiana angular é uma matriz de Gram de vetores em
duas dimensões. Portanto,

$$
\operatorname{rank}H_N\leq2
$$

e, após remover a rotação global, existem pelo menos

$$
N-3
$$

modos internos nulos. A condição de isolamento exige

$$
N-3=0.
$$

Logo,

$$
\boxed{N=3.}
$$

Para esse caso, a conservação fixa, módulo rotação e permutação,

$$
(\theta_1,\theta_2,\theta_3)
=(\theta_0,\theta_0+2\pi/3,\theta_0+4\pi/3),
$$

e

$$
\operatorname{spec}H_3
=\kappa_{\rm rel}T^2
\left\{0,\frac32,\frac32\right\}.
$$

O zero é apenas a rotação global; os dois modos relativos são positivos para
$\kappa_{\rm rel}>0$.

## 3. Verificação numérica

O solver específico da Q28 minimizou o funcional a partir de 64 condições
iniciais aleatórias para cada valor

$$
N=2,\ldots,8.
$$

Sem fornecer os ângulos de equilíbrio, o caso $N=3$ convergiu para

$$
(0^\circ,120^\circ,240^\circ)
$$

e para o espectro

$$
\{0,1{,}5,1{,}5\}.
$$

Para todo $N>3$, foram encontrados exatamente $N-3$ modos internos nulos. O
cálculo numérico não substitui a prova algébrica; ele verifica sua implementação
e mostra que o número três não foi inserido no minimizador.

## 4. Passagem ao índice geracional

Cada estômato primitivo coorientado possui índice APS local unitário. Pela
aditividade da colagem,

$$
\operatorname{Ind}_{\rm total}
=\sum_{a=1}^{3}\operatorname{Ind}_a
=1+1+1=3.
$$

A condição global $\mathbb Z_6$ associa seis unidades de carga a cada setor
primitivo:

$$
A=6\operatorname{Ind}_{\rm total}=18.
$$

Como

$$
N_G=\frac A6,
$$

segue

$$
\boxed{N_G=3.}
$$

## 5. Classificação rigorosa

A **contagem estrutural** da Q28 está fechada sob as hipóteses físicas já
declaradas de junction elementar, isotrópico, horizontal e de três componentes
primitivas coorientadas. A cadeia não usa previamente $N_G=3$:

$$
\text{ação oficial}
\to\text{Noether}
\to\text{fechamento em }\mathcal H
\to N=3
\to\text{índice APS}=3
\to A=18
\to N_G=3.
$$

O cálculo do background multicítrico completo e de seu complemento de Schur
continua importante como teste de existência e robustez dinâmica. Ele não é
mais a origem lógica do número três: poderá confirmar ou refutar se o junction
selecionado é realizado por uma solução global específica da ação oficial.

Do mesmo modo, valores de acoplamentos, massas e matrizes de mistura são
problemas quantitativos posteriores e não pertencem à prova da contagem.
