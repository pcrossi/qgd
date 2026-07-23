# Ponte global--local da GDQ — Hipótese bulk--interface

> [!warning] Documento histórico superado
> A Hipótese BI não pertence mais à formulação vigente da ponte global--local.
> O limite cosmológico--planar é apontado e não constitui uma interface
> física. Os seis lemas corrigidos estão em
> `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md`; sua hipótese local foi verificada
> para o background gaussiano $C_3$ em
> `topicos/ponte_global_local/ponte_global_local_fechamento_c3.md`. Este arquivo permanece apenas como
> registro do no-go da tentativa de colagem artificial.

> A atualização abaixo é histórica e foi substituída pela formulação sem
> colar indicada acima.

## 1. Finalidade

Este documento isola a única hipótese de existência não linear usada para
prosseguir dos Lemas 1--2 para os Lemas 3--6. Ela não é um novo axioma da
GDQ nem uma afirmação demonstrada. É uma hipótese técnica de trabalho cuja
prova poderá ser realizada posteriormente.

## 2. Hipótese BI

Para uma sequência $\varepsilon\downarrow0$, existe uma família de
backgrounds

$$
\mathfrak B_\varepsilon
=\left(
g_\varepsilon,J_\varepsilon,H_\varepsilon,
f_\varepsilon,\mathcal U_\varepsilon,gamma
\right)
$$

sobre

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
$$

com uma interface interna $Y_\varepsilon\simeq S^3$, satisfazendo as
condições BI.1--BI.9 abaixo.

### BI.1 — Geometria Hermitiana

$$
J_\varepsilon^2=-1,
\qquad
g_\varepsilon(J_\varepsilon X,J_\varepsilon Y)
=g_\varepsilon(X,Y),
$$

$J_\varepsilon$ é integrável e

$$
H_\varepsilon=d^c_{J_\varepsilon}\omega_\varepsilon.
$$

Além disso,

$$
g_\varepsilon\geq\lambda_*g_\varepsilon^{(0)}
$$

para alguma constante $\lambda_*>0$ independente de $\varepsilon$.

### BI.2 — Ação oficial e estacionariedade

O background é ponto crítico da ação oficial na classe de variações que
preservam a estrutura Hermitiana e a carga relativa:

$$
\delta\mathcal S_{\rm GDQ}[\mathfrak B_\varepsilon]=0.
$$

Usa-se exclusivamente

$$
\mathcal R_{\rm GDQ}
=R_{\rm LC}-\frac1{12}|H|^2,
\qquad H=d^c\omega,
$$

sem variar $H$ como campo independente.

### BI.3 — Carga relativa

$$
Q_{\rm st}
=\frac1{2\pi}
\int_{Y_\varepsilon}
(H_\varepsilon-H_\varepsilon^{(0)})
=n_{\rm st}\in\mathbb Z
$$

é independente de $\varepsilon$, e as variações admissíveis satisfazem
$\delta Q_{\rm st}=0$.

### BI.4 — Condição de interface

O problema bulk--interface possui condição elíptica complementar
$\mathsf B_\varepsilon\Phi=0$ — Robin, DtN, APS ou uma condição equivalente
derivada da variação — e não escolhida após conhecer o espectro. Sob as cartas
apontadas,

$$
\mathsf B_\varepsilon\longrightarrow\mathsf B_P
$$

na topologia de operadores de traço apropriada.

### BI.5 — Regularidade uniforme local

Para algum $k\geq4$ e $0<\alpha<1$, em todo compacto apontado $K$,

$$
\|g_\varepsilon\|_{C^{k,\alpha}(K)}
+\|J_\varepsilon\|_{C^{k,\alpha}(K)}
+\|f_\varepsilon\|_{C^{k,\alpha}(K)}
\leq C_K.
$$

Como $H_\varepsilon=d^c\omega_\varepsilon$, segue controle de
$H_\varepsilon$ em $C^{k-1,\alpha}(K)$.

### BI.6 — Limite local

Existem dados limites

$$
\mathfrak B_P
=(g_P,J_P,H_P,f_P,\mathcal U_P,\gamma)
$$

tais que, após pullback,

$$
(g_\varepsilon,J_\varepsilon,f_\varepsilon)
\longrightarrow(g_P,J_P,f_P)
$$

em $C^{k',\alpha}_{\rm loc}$ para todo $k'<k$, e

$$
H_\varepsilon\longrightarrow H_P
$$

em $C^{k'-1,\alpha}_{\rm loc}$.

### BI.7 — Medida e tightness

$$
\mathcal U_\varepsilon
=\frac{e^{-\operatorname{Re}f_\varepsilon}}
{(4\pi z_\tau)^4},
\qquad
\int_{M_\varepsilon}\mathcal U_\varepsilon dV_{g_\varepsilon}=1.
$$

Para todo $\delta>0$, existe $A_\delta$ independente de $\varepsilon$ tal que

$$
\int_{d(x,\mathcal N_\varepsilon)>A_\delta}
\mathcal U_\varepsilon dV_{g_\varepsilon}<\delta.
$$

### BI.8 — Controle causal uniforme

O contorno $\gamma$ é fixo e existe uma função integrável $G_\gamma(\tau)$
que domina, uniformemente em $\varepsilon$, o integrando da ação, sua primeira
variação e sua segunda variação nos vetores teste considerados.

### BI.9 — Sem degeneração espúria

Depois de remover apenas os modos de simetria e vínculos geométricos, a forma
quadrática da segunda variação é fechável e semilimitada inferiormente por uma
constante independente de $\varepsilon$. A coercividade estrita e o gap não
fazem parte desta hipótese; eles constituem o conteúdo do Lema 4.

## 3. O que a hipótese não afirma

A Hipótese BI não afirma:

1. existência ou unicidade já demonstradas;
2. estabilidade espectral;
3. gap uniforme;
4. preservação automática de autovalores;
5. valores de massas ou acoplamentos;
6. equivalência topológica global entre os espaços;
7. que todo background cosmológico satisfaz a ação oficial.

## 4. Status lógico

Sob BI, os Lemas 1B e 2B podem ser usados como resultados condicionais. Se a
existência futura falhar, os Lemas 3--6 continuarão sendo teoremas abstratos
de transporte, mas não se aplicarão ao background físico pretendido.

$$
\boxed{
\text{Hipótese BI: assumida para desenvolver a análise espectral;
prova de existência adiada.}
}
$$
