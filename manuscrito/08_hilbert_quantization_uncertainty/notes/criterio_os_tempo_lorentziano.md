---
title: "Critério OS para tempo lorentziano operacional"
---

# Critério OS para tempo lorentziano operacional

Esta nota registra a parte segura da reconstrução lorentziana operacional. Ela
não afirma que todo background da GDQ satisfaz automaticamente os axiomas de
Osterwalder--Schrader. Ela afirma o teorema condicional: se um setor efetivo
euclidiano da GDQ satisfaz as hipóteses OS, então existe espaço de Hilbert
físico, Hamiltoniano positivo e evolução unitária no tempo físico.

## 1. Separação entre assinatura e reconstrução quântica

A assinatura lorentziana da folha física é obtida pela reflexão de uma métrica
Riemanniana $q$ em uma forma-relógio admissível $u$:

$$
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
$$

Em referencial $q$-ortonormal adaptado a $u$, essa expressão dá

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

Isso resolve a assinatura. Mas não prova, por si só, produto interno positivo,
unitariedade ou Hamiltoniano autoadjunto. Esses pontos pertencem à reconstrução
operacional.

## 2. Dados euclidianos do setor

Fixe uma janela efetiva da GDQ e um background admissível. A partir dele,
consideram-se funções de Schwinger de campos efetivos do setor:

$$
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\left\langle
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
\right\rangle_E.
$$

Formalmente,

$$
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\frac1{Z_E}
\int
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
e^{-S_E[\Phi]}
\mathcal D\Phi.
$$

Aqui $S_E$ é uma ação euclidiana efetiva induzida pelo setor GDQ. Ela não
substitui a ação oficial; é a camada reconstruída usada para testar
positividade operacional.

## 3. Hipóteses OS exigidas

O setor deve satisfazer:

1. regularidade das distribuições $S_n$;
2. invariância euclidiana no setor plano, ou covariância local em background
   curvo com recuperação plana;
3. simetria graduada por permutação;
4. positividade por reflexão;
5. propriedade de cluster.

A condição central é a positividade por reflexão. Seja $\mathcal D_+$ o espaço
de funcionais com suporte em tempos euclidianos positivos e seja $\Theta$ a
reflexão temporal do setor. Exige-se

$$
\langle \Theta F\,F\rangle_E\ge0
\qquad
\forall F\in\mathcal D_+.
$$

Em termos das funções de Schwinger, para funcionais polinomiais

$$
F
=
\sum_i c_i
\Phi_{a_{i1}}(x_{i1})\cdots\Phi_{a_{im_i}}(x_{im_i}),
\qquad
x_{ik}^0>0,
$$

a condição é

$$
\sum_{i,j}
\bar c_i c_j\,
S_{m_i+m_j}
(\Theta x_{i m_i},\ldots,\Theta x_{i1},
x_{j1},\ldots,x_{jm_j})
\ge0.
$$

Essa positividade não segue apenas de $J^2=-1$, nem da escrita histórica
$t=-i\tau$, nem do cancelamento de formas exatas no contorno causal.

## 4. Espaço de Hilbert e Hamiltoniano

Define-se o produto semidefinido:

$$
(F,G)
=
\langle \Theta F\,G\rangle_E.
$$

O subespaço nulo é

$$
\mathcal N
=
\{F\in\mathcal D_+:(F,F)=0\}.
$$

Depois de quocientar normas nulas e redundâncias geométricas $\mathcal G$,
obtém-se

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

As translações euclidianas positivas no tempo induzem um semigrupo de
contrações:

$$
T_E(a+b)=T_E(a)T_E(b),
\qquad
\|T_E(a)\|\le1,
\qquad
a\ge0.
$$

Pelo teorema de reconstrução, existe um operador autoadjunto positivo $H$ tal
que

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\ge0.
$$

A evolução no tempo físico reconstruído é então

$$
U(t)=e^{-itH/\hbar}.
$$

Pelo teorema espectral, $U(t)$ é unitário.

## 5. Relação com $\tau$, $t$, $z_\tau$ e $\gamma$

O tempo físico $t$ não é identificado com $\tau$. A variável causal complexa
da GDQ permanece

$$
z_\tau
=
\tau+i\nu_0t.
$$

O contorno $\gamma\subset\mathbb C_{z_\tau}$ organiza a prescrição causal,
incluindo ramos retardados e avançados quando aplicável. A positividade da
norma, porém, vem da condição OS do setor efetivo, não de $\gamma$ isolado.

Portanto, a formulação segura é:

$$
\boxed{
\text{OS fornece }(\mathcal H_{\rm phys},H,U(t));
\qquad
\gamma\text{ fornece a prescrição causal compatível em }z_\tau.
}
$$

## 6. Status

Este é um teorema condicional setorial. Para cada setor concreto, ainda é
necessário verificar regularidade, positividade, domínio, cluster e remoção de
modos nulos/gauge. Quando essas hipóteses valem, a reconstrução lorentziana
operacional está fechada.
